"""
NPSE Core: Neural Posterior Score Estimation
Core algorithm implementation — score network training and probability flow ODE sampling.

This module implements:
1. Forward SDE (VE and VP variants)
2. Denoising Posterior Score Matching (DSM) loss
3. Score network architecture (MLP with separate θt, x, t embeddings)
4. Probability flow ODE sampling
5. Standardization of inputs

Reference: Algorithm in §2.2; SDE definitions in Appendix E.3.1; 
Architecture in Appendix E.3.2; Sampling in Appendix E.3.3
"""

import jax
import jax.numpy as jnp
import jax.random as jr
from typing import Tuple, Callable


# ---------------------------------------------------------------------------
# Score Network Architecture
# ---------------------------------------------------------------------------

def sinusoidal_embedding(t: jnp.ndarray, dim: int = 64, max_positions: int = 10000) -> jnp.ndarray:
    """
    Sinusoidal time embedding for diffusion timestep t.
    
    From Appendix E.3.2, Eq. (138):
      (t_emb)_i = sin(t / 10000^((i-1)/31))   if i <= 32
      (t_emb)_i = cos(t / 10000^((i-32-1)/31)) if i > 32
    
    Args:
        t: scalar diffusion time (or standard deviation std)
        dim: embedding dimension (default 64)
        max_positions: base for frequency calculation (10000)
    
    Returns:
        t_emb: (dim,) sinusoidal embedding
    """
    half_dim = dim // 2
    # log(max_positions) / (half_dim - 1) matches 1/31 when half_dim=32, max_positions=10000
    freqs = jnp.exp(-jnp.arange(half_dim) * jnp.log(max_positions) / (half_dim - 1))
    emb = t * freqs
    return jnp.concatenate([jnp.sin(emb), jnp.cos(emb)], axis=-1)


def score_network_forward(
    theta_emb_params,  # parameters of θt-embedding MLP
    x_emb_params,      # parameters of x-embedding MLP
    main_mlp_params,   # parameters of main score MLP
    theta_t: jnp.ndarray,  # (d,) noised parameter, standardized
    x: jnp.ndarray,         # (p,) observation, standardized
    sigma: float,           # noise std at time t (used as proxy for t)
) -> jnp.ndarray:
    """
    Score network sψ(θt, x, σ) ≈ ∇θ log pt(θt|x).
    
    Architecture (§5.1, Appendix E.3.2):
      - θt-embedding: MLP [d → 256 → 256 → max(30,4d)], SiLU
      - x-embedding: MLP [p → 256 → 256 → max(30,4p)], SiLU
      - t-embedding: sinusoidal, 64 dims
      - main MLP: [max(30,4d)+max(30,4p)+64 → 256 → 256 → d], SiLU
    
    Args:
        theta_t: (d,) standardized noised parameter
        x: (p,) standardized observation
        sigma: standard deviation at current diffusion time t
    
    Returns:
        score: (d,) approximate score ∇θ log pt(θt|x)
    """
    # Embeddings (actual implementation in model.py uses equinox MLP)
    theta_emb = mlp_forward(theta_emb_params, theta_t)   # (d,) -> (max(30,4d),)
    x_emb = mlp_forward(x_emb_params, x)                  # (p,) -> (max(30,4p),)
    t_emb = sinusoidal_embedding(sigma, dim=64)            # (64,)
    # Concatenate and pass through main MLP
    combined = jnp.concatenate([theta_emb, x_emb, t_emb])
    score = mlp_forward(main_mlp_params, combined)         # -> (d,)
    return score


def mlp_forward(params, x: jnp.ndarray) -> jnp.ndarray:
    """
    3-layer fully-connected MLP with SiLU activations.
    depth=2 in equinox (2 hidden + 1 output layer = 3 total layers).
    
    Args:
        params: (W1, b1, W2, b2, W3, b3) tuple of weight matrices and biases
        x: input tensor
    
    Returns:
        output: final layer output
    """
    # Layer 1: hidden
    W1, b1, W2, b2, W3, b3 = params
    h = jax.nn.silu(W1 @ x + b1)
    # Layer 2: hidden
    h = jax.nn.silu(W2 @ h + b2)
    # Layer 3: output (no activation)
    return W3 @ h + b3


# ---------------------------------------------------------------------------
# Forward SDE: Transition Densities
# ---------------------------------------------------------------------------

def ve_sde_marginal(
    theta0: jnp.ndarray, t: float, sigma_min: float, sigma_max: float
) -> Tuple[jnp.ndarray, float]:
    """
    VE SDE marginal distribution at time t.
    p_{t|0}(θt|θ0) = N(θ0, σ²_min (σmax/σmin)^{2t} I)
    
    Args:
        theta0: (d,) parameter sample
        t: diffusion time in (0, T]
        sigma_min: minimum noise scale (0.01 for 2D tasks, 0.05 for others)
        sigma_max: maximum noise scale (task-specific)
    
    Returns:
        mean: (d,) = theta0
        std: scalar noise std = sigma_min * (sigma_max/sigma_min)^t
    """
    std = sigma_min * (sigma_max / sigma_min) ** t
    return theta0, std


def vp_sde_marginal(
    theta0: jnp.ndarray, t: float, beta_min: float, beta_max: float
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    VP SDE marginal distribution at time t.
    p_{t|0}(θt|θ0) = N(θ0 exp(-0.5 ∫βs ds), (I - I exp(-∫βs ds)))
    
    Args:
        theta0: (d,) parameter sample
        t: diffusion time in (0, T]
        beta_min: 0.1 (paper) / 0.01 (code default)
        beta_max: 11.0 (paper) / 10.0 (code default)
    
    Returns:
        mean: (d,) = theta0 * exp(-0.25 t²(βmax-βmin) - 0.5 t βmin)
        std: scalar noise std = sqrt(1 - exp(2 * log_mean_coeff))
    """
    log_mean_coeff = -0.25 * t**2 * (beta_max - beta_min) - 0.5 * t * beta_min
    mean = jnp.exp(log_mean_coeff) * theta0
    std = jnp.sqrt(1.0 - jnp.exp(2.0 * log_mean_coeff))
    return mean, std


def sample_forward_diffusion(
    theta0: jnp.ndarray, t: float, sde_type: str,
    sigma_min: float = 0.05, sigma_max: float = 8.0,
    beta_min: float = 0.1, beta_max: float = 11.0,
    key: jnp.ndarray = None
) -> Tuple[jnp.ndarray, jnp.ndarray, float]:
    """
    Sample θt ~ p_{t|0}(·|θ0) from the forward noising process.
    
    Returns:
        theta_t: (d,) noised parameter
        noise: (d,) sampled noise ε ~ N(0, I)
        std: noise standard deviation
    """
    if sde_type == "vesde":
        mean, std = ve_sde_marginal(theta0, t, sigma_min, sigma_max)
    else:  # vpsde
        mean, std = vp_sde_marginal(theta0, t, beta_min, beta_max)
    noise = jr.normal(key, theta0.shape)
    theta_t = mean + std * noise
    return theta_t, noise, std


# ---------------------------------------------------------------------------
# DSM Loss
# ---------------------------------------------------------------------------

def dsm_loss_single(
    score_fn: Callable,
    theta0: jnp.ndarray,   # (d,) clean parameter
    x: jnp.ndarray,         # (p,) observation
    t: float,               # diffusion time
    sde_type: str,
    key: jnp.ndarray,
    **sde_kwargs
) -> float:
    """
    Single-sample DSM loss (Eq. 7 in paper):
    λ_t * ||sψ(θt, x, std) + noise/std||²
    
    where λ_t = std² (variance weighting, §E.3.2).
    The score network predicts -noise/std, so (pred + noise/std)² measures error.
    
    Args:
        score_fn: callable sψ(θt, x, std) -> (d,)
        theta0: (d,) clean parameter from prior
        x: (p,) observation from simulator
        t: diffusion time sampled uniformly from (0.0001, T)
        sde_type: "vesde" or "vpsde"
        key: JAX random key
    
    Returns:
        loss: scalar DSM loss value
    """
    theta_t, noise, std = sample_forward_diffusion(theta0, t, sde_type, key=key, **sde_kwargs)
    pred = score_fn(theta_t, x, std)
    # Variance-weighted loss: std² * ||pred + noise/std||²
    return (std ** 2) * jnp.mean((pred + noise / std) ** 2)


def batch_dsm_loss(
    score_fn: Callable,
    theta_batch: jnp.ndarray,   # (B, d) batch of clean parameters
    x_batch: jnp.ndarray,        # (B, p) batch of observations
    sde_type: str,
    key: jnp.ndarray,
    t_min: float = 0.0001,
    T: float = 1.0,
    **sde_kwargs
) -> float:
    """
    Batch DSM loss. Samples t ~ Uniform(t_min, T) per sample.
    
    Returns:
        loss: scalar mean DSM loss over batch
    """
    B = theta_batch.shape[0]
    tkey, noise_key = jr.split(key)
    t_batch = jr.uniform(tkey, (B,), minval=t_min, maxval=T)
    noise_keys = jr.split(noise_key, B)
    
    losses = jax.vmap(
        lambda theta0, x, t, k: dsm_loss_single(
            score_fn, theta0, x, t, sde_type, k, **sde_kwargs
        )
    )(theta_batch, x_batch, t_batch, noise_keys)
    return jnp.mean(losses)


# ---------------------------------------------------------------------------
# Training Loop
# ---------------------------------------------------------------------------

def train_npse(
    score_fn_init,          # initial score network parameters
    theta_ds: jnp.ndarray,  # (N, d) dataset of parameters
    x_ds: jnp.ndarray,      # (N, p) dataset of observations
    sde_type: str,
    config: dict,           # training config (lr, max_iters, patience, eval_prop, batch_size)
    key: jnp.ndarray,
    **sde_kwargs
):
    """
    Full NPSE training procedure (§5.1, Appendix E.3.2):
    1. Standardize θ and x by empirical mean/std
    2. Split 90/10 train/validation (paper says 15%; code uses eval_prop=0.10)
    3. Train with Adam, early stopping
    4. Return best model by validation loss
    
    Args:
        score_fn_init: initial score network (equinox model in actual code)
        theta_ds: (N, d) parameter samples from (truncated) prior
        x_ds: (N, p) corresponding simulator outputs
        sde_type: "vesde" or "vpsde"
        config: dict with keys: lr, max_iters, max_patience, batch_size, eval_prop
        key: JAX random key
    
    Returns:
        best_model: model with lowest validation loss
        theta_mean, theta_std, x_mean, x_std: standardization statistics
    """
    # Standardize
    theta_mean, theta_std = theta_ds.mean(axis=0), theta_ds.std(axis=0)
    x_mean, x_std = x_ds.mean(axis=0), x_ds.std(axis=0)
    theta_norm = (theta_ds - theta_mean) / theta_std
    x_norm = (x_ds - x_mean) / x_std
    
    # Train/val split
    N = theta_ds.shape[0]
    split_idx = int(N * config['eval_prop'])
    # ... Adam optimizer setup, training loop with patience-based early stopping
    # Implementation in training.py: train_score_network()
    
    raise NotImplementedError(
        "Full implementation in training.py:train_score_network(). "
        "Key steps: Adam optimizer (optax), batch DSM loss, patience-based early stopping, "
        "return best_model by val loss."
    )


# ---------------------------------------------------------------------------
# Probability Flow ODE Sampling
# ---------------------------------------------------------------------------

def sample_posterior(
    score_fn: Callable,
    x_obs: jnp.ndarray,         # (p,) target observation (standardized)
    n_samples: int,
    sde_type: str,
    T: float = 1.0,
    t0: float = 1e-5,
    dt: float = 0.01,
    sigma_max: float = 8.0,     # for VE SDE base distribution
    key: jnp.ndarray = None,
    **sde_kwargs
) -> jnp.ndarray:
    """
    Generate posterior samples by reversing the probability flow ODE (§2.2, Eq. 4).
    
    Procedure (Appendix E.3.3):
    1. Sample θ_T ~ π (N(0, σ²_max I) for VE; N(0, I) for VP)
    2. Integrate ODE backward: t: T → t0
       VE: dθ/dt = -0.5 g²(t) * sψ(θ, x, std(t))
       VP: dθ/dt = -0.5 βt [θ + sψ(θ, x, std(t))]
    3. Return θ(t0) as posterior sample
    
    Solver: Tsit5 (diffrax) with dt=0.01, or RK45
    
    Args:
        score_fn: trained score network (must accept (θt, x, std) -> (d,))
        x_obs: (p,) standardized observation
        n_samples: number of posterior samples
        sde_type: "vesde" or "vpsde"
        T: diffusion horizon (1.0)
        t0: small positive lower bound (1e-5)
        dt: ODE solver step size (0.01)
        sigma_max: VE SDE base distribution scale
        key: JAX random key
    
    Returns:
        samples: (n_samples, d) posterior samples (in standardized θ space)
    """
    # Actual implementation in cnf.py: CNF.batch_sample_fn -> CNF.single_sample_fn
    # Uses diffrax.diffeqsolve with Tsit5 solver
    raise NotImplementedError(
        "Full implementation in cnf.py:CNF.single_sample_fn(). "
        "Uses diffrax.Tsit5() solver, integrates from t=T to t=1e-5, "
        "starting from sde.base_dist(key) (N(0, σmax²I) for VE, N(0,I) for VP)."
    )
