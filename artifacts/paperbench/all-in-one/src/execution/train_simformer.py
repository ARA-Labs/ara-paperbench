"""
Training script for the Simformer model.

Complete pipeline:
  1. Generate simulated data from a simulator
  2. Initialize Simformer components (tokenizer, score model)
  3. Training loop with denoising score-matching loss
  4. Evaluation with reverse SDE sampling
  5. C2ST evaluation against reference MCMC samples
  6. Supports different attention mask types (dense, undirected, directed)

Hyperparameters (from paper Appendix A2.1):
  - batch_size=1000, optimizer=Adam, early_stopping on val loss
  - VESDE: sigma_max=15, sigma_min=0.0001, t in [1e-5, 1]
  - token_dim=50, n_layers=6/8, n_heads=4, head_dim=10, widening=3
  - 500 reverse SDE steps for sampling
  - Condition mask: uniformly sample from 5 mask types per batch

Reference: Gloeckler et al., 2024, "All-in-one simulation-based inference"
"""

import math
import numpy as np
from typing import Optional, Dict, Any, Callable, Tuple

from simformer import (
    SBITokenizer,
    SimformerScoreModel,
    simformer_loss,
    sample_conditional,
    layer_norm,
)
from c2st import c2st, expected_coverage
from build_masks import dense_mask, undirected_mask, directed_mask


# ---------------------------------------------------------------------------
# Simulator Interface
# ---------------------------------------------------------------------------

class Simulator:
    """
    Abstract simulator interface.

    Subclass this for specific tasks. A simulator defines:
      - prior p(theta): sample parameters
      - likelihood p(x | theta): run forward simulation
      - joint p(theta, x): sample (theta, x) pairs for training
      - variable metadata: which indices are params vs data, variable IDs

    Example implementations for benchmark tasks below.
    """

    def __init__(self, d_theta: int, d_x: int, name: str = "simulator"):
        self.d_theta = d_theta
        self.d_x = d_x
        self.d = d_theta + d_x
        self.name = name

        # Variable indices
        self.param_indices = np.arange(d_theta)
        self.data_indices = np.arange(d_theta, d_theta + d_x)
        self.var_ids = np.arange(self.d)

    def sample_joint(self, n: int) -> np.ndarray:
        """Sample n joint (theta, x) pairs. Returns (n, d) array."""
        raise NotImplementedError

    def sample_prior(self, n: int) -> np.ndarray:
        """Sample n parameter vectors from the prior. Returns (n, d_theta)."""
        raise NotImplementedError

    def simulate(self, theta: np.ndarray) -> np.ndarray:
        """Run forward simulation. theta: (n, d_theta) -> x: (n, d_x)."""
        raise NotImplementedError

    def reference_posterior(self, x_obs: np.ndarray, n_samples: int) -> np.ndarray:
        """MCMC reference posterior samples. Returns (n_samples, d_theta)."""
        raise NotImplementedError


class LinearGaussianSimulator(Simulator):
    """
    Linear Gaussian model (benchmark task).

    theta ~ N(0, I_{d_theta})
    x | theta ~ N(A @ theta, sigma^2 * I_{d_x})

    Posterior is analytically tractable (conjugate Gaussian).
    """

    def __init__(
        self,
        d_theta: int = 5,
        d_x: int = 5,
        sigma: float = 1.0,
        seed: int = 42,
    ):
        super().__init__(d_theta, d_x, name="linear_gaussian")
        self.sigma = sigma
        rng = np.random.RandomState(seed)
        self.A = rng.randn(d_x, d_theta) * 0.5   # fixed linear map

    def sample_prior(self, n: int) -> np.ndarray:
        return np.random.randn(n, self.d_theta)

    def simulate(self, theta: np.ndarray) -> np.ndarray:
        mean = theta @ self.A.T   # (n, d_x)
        noise = np.random.randn(*mean.shape) * self.sigma
        return mean + noise

    def sample_joint(self, n: int) -> np.ndarray:
        theta = self.sample_prior(n)
        x = self.simulate(theta)
        return np.concatenate([theta, x], axis=1)   # (n, d_theta + d_x)

    def reference_posterior(self, x_obs: np.ndarray, n_samples: int) -> np.ndarray:
        """Analytically compute posterior for linear Gaussian model."""
        # Prior: theta ~ N(0, I)
        # Likelihood: x | theta ~ N(A @ theta, sigma^2 * I)
        # Posterior: theta | x ~ N(mu_post, Sigma_post)
        # Sigma_post = (I + A^T A / sigma^2)^{-1}
        # mu_post = Sigma_post @ A^T @ x_obs / sigma^2
        d = self.d_theta
        prior_prec = np.eye(d)
        likelihood_prec = self.A.T @ self.A / (self.sigma ** 2)
        post_prec = prior_prec + likelihood_prec
        post_cov = np.linalg.inv(post_prec)
        post_mean = post_cov @ self.A.T @ x_obs.flatten() / (self.sigma ** 2)
        L = np.linalg.cholesky(post_cov)
        samples = post_mean[None, :] + (np.random.randn(n_samples, d) @ L.T)
        return samples


class TwoMoonsSimulator(Simulator):
    """
    Two Moons benchmark task.

    theta ~ Uniform([-1, -1], [1, 1])
    x | theta: bimodal crescent-shaped likelihood

    Standard SBI benchmark from Greenberg et al. (2019).
    """

    def __init__(self):
        super().__init__(d_theta=2, d_x=2, name="two_moons")

    def sample_prior(self, n: int) -> np.ndarray:
        return np.random.uniform(-1, 1, size=(n, self.d_theta))

    def simulate(self, theta: np.ndarray) -> np.ndarray:
        n = len(theta)
        # Two Moons generative model
        a = np.random.uniform(-0.5 * math.pi, 0.5 * math.pi, size=(n,))
        r = np.random.normal(0.1, 0.01, size=(n,))
        p = np.stack([r * np.cos(a) + 0.25, r * np.sin(a)], axis=1)   # (n, 2)
        # Absolute value of first component + shift by theta
        x = np.stack([
            p[:, 0] + np.abs(theta[:, 0] + theta[:, 1]) / np.sqrt(2),
            p[:, 1] + (-theta[:, 0] + theta[:, 1]) / np.sqrt(2),
        ], axis=1)
        return x

    def sample_joint(self, n: int) -> np.ndarray:
        theta = self.sample_prior(n)
        x = self.simulate(theta)
        return np.concatenate([theta, x], axis=1)


# ---------------------------------------------------------------------------
# Parameter Initialization
# ---------------------------------------------------------------------------

def xavier_init(fan_in: int, fan_out: int, rng: np.random.RandomState) -> np.ndarray:
    """Xavier/Glorot uniform initialization."""
    limit = math.sqrt(6.0 / (fan_in + fan_out))
    return rng.uniform(-limit, limit, size=(fan_in, fan_out)).astype(np.float32)


def init_tokenizer(
    num_vars: int,
    token_dim: int = 50,
    fourier_dim: int = 128,
    metadata_input_dim: int = 1,
    rng: Optional[np.random.RandomState] = None,
) -> SBITokenizer:
    """Initialize tokenizer with learnable embeddings."""
    if rng is None:
        rng = np.random.RandomState(0)

    tok = SBITokenizer(num_vars=num_vars, token_dim=token_dim, fourier_dim=fourier_dim)

    # Learnable embeddings
    tok.id_embeddings = xavier_init(num_vars, token_dim, rng)       # (num_vars, token_dim)
    tok.cond_true_embedding = rng.randn(token_dim).astype(np.float32) * 0.01  # (token_dim,)

    # Random Fourier features for metadata (fixed)
    tok.fourier_weights = rng.randn(fourier_dim // 2, metadata_input_dim).astype(np.float32)
    # Learnable projection
    tok.fourier_proj = xavier_init(fourier_dim, token_dim, rng)     # (fourier_dim, token_dim)

    return tok


def init_score_model(
    token_dim: int = 50,
    n_layers: int = 6,
    n_heads: int = 4,
    head_dim: int = 10,
    widening_factor: int = 3,
    time_fourier_dim: int = 128,
    rng: Optional[np.random.RandomState] = None,
) -> SimformerScoreModel:
    """Initialize score model with learnable weights."""
    if rng is None:
        rng = np.random.RandomState(1)

    model = SimformerScoreModel(
        token_dim=token_dim,
        n_layers=n_layers,
        n_heads=n_heads,
        head_dim=head_dim,
        widening_factor=widening_factor,
        time_fourier_dim=time_fourier_dim,
    )

    # Fixed random Fourier weights for diffusion time embedding
    model.time_fourier_weights = rng.randn(time_fourier_dim // 2).astype(np.float32)

    # Output projection: (token_dim, 1)
    model.output_proj = xavier_init(token_dim, 1, rng)

    hidden_dim = token_dim * widening_factor
    total_head_dim = n_heads * head_dim

    # Initialize each transformer block
    for block in model.blocks:
        # Attention weights
        attn = block.attn
        attn.W_Q = xavier_init(token_dim, total_head_dim, rng)
        attn.W_K = xavier_init(token_dim, total_head_dim, rng)
        attn.W_V = xavier_init(token_dim, total_head_dim, rng)
        attn.W_O = xavier_init(total_head_dim, token_dim, rng)

        # Feed-forward weights
        ff = block.ff
        ff.W1 = xavier_init(token_dim, hidden_dim, rng)
        ff.b1 = np.zeros(hidden_dim, dtype=np.float32)
        ff.W2 = xavier_init(hidden_dim, token_dim, rng)
        ff.b2 = np.zeros(token_dim, dtype=np.float32)
        ff.W_time = xavier_init(time_fourier_dim, token_dim, rng)

    return model


# ---------------------------------------------------------------------------
# Simple Adam Optimizer (numpy-only, for demonstration)
# ---------------------------------------------------------------------------

class AdamOptimizer:
    """
    Minimal Adam optimizer operating on a flat list of named parameter arrays.

    In practice, use JAX optax.adam or PyTorch torch.optim.Adam.
    This numpy implementation demonstrates the parameter update logic.
    """

    def __init__(self, lr: float = 1e-3, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.t = 0
        self.m = {}   # first moments
        self.v = {}   # second moments

    def step(self, params: Dict[str, np.ndarray], grads: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Perform one Adam update step.

        Args:
            params: dict of parameter name -> numpy array
            grads:  dict of parameter name -> gradient array (same shapes)
        Returns:
            updated params dict
        """
        self.t += 1
        updated = {}
        for name, p in params.items():
            g = grads[name]
            if name not in self.m:
                self.m[name] = np.zeros_like(p)
                self.v[name] = np.zeros_like(p)

            self.m[name] = self.beta1 * self.m[name] + (1 - self.beta1) * g
            self.v[name] = self.beta2 * self.v[name] + (1 - self.beta2) * g ** 2

            m_hat = self.m[name] / (1 - self.beta1 ** self.t)
            v_hat = self.v[name] / (1 - self.beta2 ** self.t)

            updated[name] = p - self.lr * m_hat / (np.sqrt(v_hat) + self.eps)

        return updated


# ---------------------------------------------------------------------------
# Training Loop
# ---------------------------------------------------------------------------

def collect_params(model: SimformerScoreModel, tokenizer: SBITokenizer) -> Dict[str, np.ndarray]:
    """Collect all learnable parameters into a flat dictionary."""
    params = {}
    # Tokenizer
    params["tok.id_embeddings"] = tokenizer.id_embeddings
    params["tok.cond_true_embedding"] = tokenizer.cond_true_embedding
    params["tok.fourier_proj"] = tokenizer.fourier_proj

    # Score model output
    params["model.output_proj"] = model.output_proj

    # Transformer blocks
    for i, block in enumerate(model.blocks):
        prefix = f"block.{i}"
        params[f"{prefix}.attn.W_Q"] = block.attn.W_Q
        params[f"{prefix}.attn.W_K"] = block.attn.W_K
        params[f"{prefix}.attn.W_V"] = block.attn.W_V
        params[f"{prefix}.attn.W_O"] = block.attn.W_O
        params[f"{prefix}.ff.W1"] = block.ff.W1
        params[f"{prefix}.ff.b1"] = block.ff.b1
        params[f"{prefix}.ff.W2"] = block.ff.W2
        params[f"{prefix}.ff.b2"] = block.ff.b2
        params[f"{prefix}.ff.W_time"] = block.ff.W_time

    return params


def assign_params(model: SimformerScoreModel, tokenizer: SBITokenizer, params: Dict[str, np.ndarray]):
    """Assign parameter dictionary back to model/tokenizer objects."""
    tokenizer.id_embeddings = params["tok.id_embeddings"]
    tokenizer.cond_true_embedding = params["tok.cond_true_embedding"]
    tokenizer.fourier_proj = params["tok.fourier_proj"]
    model.output_proj = params["model.output_proj"]

    for i, block in enumerate(model.blocks):
        prefix = f"block.{i}"
        block.attn.W_Q = params[f"{prefix}.attn.W_Q"]
        block.attn.W_K = params[f"{prefix}.attn.W_K"]
        block.attn.W_V = params[f"{prefix}.attn.W_V"]
        block.attn.W_O = params[f"{prefix}.attn.W_O"]
        block.ff.W1 = params[f"{prefix}.ff.W1"]
        block.ff.b1 = params[f"{prefix}.ff.b1"]
        block.ff.W2 = params[f"{prefix}.ff.W2"]
        block.ff.b2 = params[f"{prefix}.ff.b2"]
        block.ff.W_time = params[f"{prefix}.ff.W_time"]


def estimate_gradients_fd(
    score_model: SimformerScoreModel,
    tokenizer: SBITokenizer,
    params: Dict[str, np.ndarray],
    x0: np.ndarray,
    var_ids: np.ndarray,
    data_indices: np.ndarray,
    param_indices: np.ndarray,
    attention_mask: np.ndarray,
    eps: float = 1e-4,
) -> Dict[str, np.ndarray]:
    """
    Estimate gradients via finite differences (for demonstration).

    NOTE: In practice, use JAX's jax.grad or PyTorch autograd for efficient
    automatic differentiation. Finite differences are provided here to make the
    training loop fully executable with pure numpy, at the cost of speed.

    For production use, replace this with:
        loss_fn = lambda params: simformer_loss(model_from_params(params), ...)
        grads = jax.grad(loss_fn)(params)
    """
    grads = {}
    assign_params(score_model, tokenizer, params)
    base_loss = simformer_loss(
        score_model, tokenizer, x0, var_ids,
        data_indices, param_indices, attention_mask,
    )

    for name, p in params.items():
        g = np.zeros_like(p)
        flat = p.ravel()
        for idx in range(min(len(flat), 50)):
            # Subsample indices for speed; full FD is O(n_params * batch)
            original = flat[idx]
            flat[idx] = original + eps
            params[name] = flat.reshape(p.shape)
            assign_params(score_model, tokenizer, params)
            loss_plus = simformer_loss(
                score_model, tokenizer, x0, var_ids,
                data_indices, param_indices, attention_mask,
            )
            flat[idx] = original
            params[name] = flat.reshape(p.shape)
            g.ravel()[idx] = (loss_plus - base_loss) / eps

        grads[name] = g

    assign_params(score_model, tokenizer, params)
    return grads


def train(
    simulator: Simulator,
    mask_type: str = "dense",
    adjacency: Optional[np.ndarray] = None,
    n_simulations: int = 10000,
    batch_size: int = 1000,
    max_epochs: int = 200,
    patience: int = 20,
    lr: float = 1e-3,
    val_fraction: float = 0.1,
    token_dim: int = 50,
    n_layers: int = 6,
    n_heads: int = 4,
    head_dim: int = 10,
    widening_factor: int = 3,
    time_fourier_dim: int = 128,
    sigma_min: float = 0.0001,
    sigma_max: float = 15.0,
    seed: int = 0,
    verbose: bool = True,
) -> Tuple[SimformerScoreModel, SBITokenizer, np.ndarray, Dict[str, Any]]:
    """
    Train the Simformer model.

    Args:
        simulator:       Simulator instance providing sample_joint()
        mask_type:       One of "dense", "undirected", "directed"
        adjacency:       Adjacency matrix for undirected/directed masks (d, d)
        n_simulations:   Total number of simulator calls (training data budget)
        batch_size:      Training batch size (default: 1000)
        max_epochs:      Maximum training epochs
        patience:        Early stopping patience (epochs without val improvement)
        lr:              Learning rate for Adam
        val_fraction:    Fraction of data used for validation
        token_dim:       Token dimension (default: 50)
        n_layers:        Number of transformer layers (6 benchmark, 8 complex)
        n_heads:         Number of attention heads (default: 4)
        head_dim:        Per-head attention dimension (default: 10)
        widening_factor: Feed-forward widening factor (default: 3)
        time_fourier_dim: Diffusion time Fourier embedding dim (default: 128)
        sigma_min:       VESDE minimum noise (default: 0.0001)
        sigma_max:       VESDE maximum noise (default: 15)
        seed:            Random seed
        verbose:         Print training progress

    Returns:
        model:       Trained SimformerScoreModel
        tokenizer:   Trained SBITokenizer
        attention_mask: (d, d) attention mask used
        info:        Dict with training history and metadata
    """
    rng = np.random.RandomState(seed)
    np.random.seed(seed)

    d = simulator.d
    d_theta = simulator.d_theta

    # ---- 1. Generate training data from simulator ----
    if verbose:
        print(f"Generating {n_simulations} simulations from {simulator.name}...")
    data = simulator.sample_joint(n_simulations)   # (n_simulations, d)

    # Train/val split
    n_val = max(1, int(n_simulations * val_fraction))
    n_train = n_simulations - n_val
    perm = rng.permutation(n_simulations)
    train_data = data[perm[:n_train]]
    val_data = data[perm[n_train:]]

    if verbose:
        print(f"  Train: {n_train}, Val: {n_val}, d={d} (d_theta={d_theta})")

    # ---- 2. Build attention mask ----
    if mask_type == "dense":
        attention_mask = dense_mask(d)
    elif mask_type == "undirected":
        if adjacency is None:
            raise ValueError("adjacency matrix required for undirected mask")
        attention_mask = undirected_mask(adjacency)
    elif mask_type == "directed":
        if adjacency is None:
            raise ValueError("adjacency matrix required for directed mask")
        attention_mask = directed_mask(adjacency)
    else:
        raise ValueError(f"Unknown mask_type: {mask_type}")

    if verbose:
        print(f"  Attention mask: {mask_type}, shape={attention_mask.shape}")

    # ---- 3. Initialize model and tokenizer ----
    tokenizer = init_tokenizer(
        num_vars=d, token_dim=token_dim, fourier_dim=time_fourier_dim, rng=rng,
    )
    model = init_score_model(
        token_dim=token_dim, n_layers=n_layers, n_heads=n_heads,
        head_dim=head_dim, widening_factor=widening_factor,
        time_fourier_dim=time_fourier_dim, rng=rng,
    )

    var_ids = simulator.var_ids
    param_indices = simulator.param_indices
    data_indices = simulator.data_indices

    if verbose:
        params = collect_params(model, tokenizer)
        n_params = sum(p.size for p in params.values())
        print(f"  Model: {n_layers} layers, {n_params:,} parameters")

    # ---- 4. Training loop ----
    optimizer = AdamOptimizer(lr=lr)
    params = collect_params(model, tokenizer)

    train_losses = []
    val_losses = []
    best_val_loss = float("inf")
    best_params = None
    epochs_no_improve = 0

    n_batches = max(1, n_train // batch_size)

    if verbose:
        print(f"\nTraining (max_epochs={max_epochs}, patience={patience}, batch_size={batch_size})...")

    for epoch in range(max_epochs):
        # Shuffle training data each epoch
        epoch_perm = rng.permutation(n_train)
        epoch_loss = 0.0

        for batch_idx in range(n_batches):
            start = batch_idx * batch_size
            end = min(start + batch_size, n_train)
            x0 = train_data[epoch_perm[start:end]]   # (B, d)

            # Compute loss
            assign_params(model, tokenizer, params)
            loss = simformer_loss(
                model, tokenizer, x0, var_ids,
                data_indices, param_indices, attention_mask,
                sigma_min=sigma_min, sigma_max=sigma_max,
            )
            epoch_loss += loss

            # Estimate gradients and update
            # NOTE: In practice, replace estimate_gradients_fd with jax.grad
            grads = estimate_gradients_fd(
                model, tokenizer, params, x0, var_ids,
                data_indices, param_indices, attention_mask,
            )
            params = optimizer.step(params, grads)

        avg_train_loss = epoch_loss / n_batches
        train_losses.append(avg_train_loss)

        # Validation loss
        assign_params(model, tokenizer, params)
        val_loss = simformer_loss(
            model, tokenizer, val_data, var_ids,
            data_indices, param_indices, attention_mask,
            sigma_min=sigma_min, sigma_max=sigma_max,
        )
        val_losses.append(val_loss)

        # Early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_params = {k: v.copy() for k, v in params.items()}
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if verbose and (epoch % 10 == 0 or epochs_no_improve >= patience):
            print(f"  Epoch {epoch:4d}  train_loss={avg_train_loss:.6f}  "
                  f"val_loss={val_loss:.6f}  best_val={best_val_loss:.6f}")

        if epochs_no_improve >= patience:
            if verbose:
                print(f"  Early stopping at epoch {epoch} (patience={patience})")
            break

    # Restore best parameters
    if best_params is not None:
        assign_params(model, tokenizer, best_params)

    info = {
        "train_losses": train_losses,
        "val_losses": val_losses,
        "best_val_loss": best_val_loss,
        "epochs_trained": len(train_losses),
        "n_simulations": n_simulations,
        "mask_type": mask_type,
    }

    if verbose:
        print(f"\nTraining complete: {info['epochs_trained']} epochs, "
              f"best val loss = {best_val_loss:.6f}")

    return model, tokenizer, attention_mask, info


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate_posterior(
    model: SimformerScoreModel,
    tokenizer: SBITokenizer,
    simulator: Simulator,
    attention_mask: np.ndarray,
    n_test: int = 100,
    n_posterior_samples: int = 1000,
    n_reference_samples: int = 1000,
    n_steps: int = 500,
    sigma_min: float = 0.0001,
    sigma_max: float = 15.0,
    verbose: bool = True,
) -> Dict[str, Any]:
    """
    Evaluate the trained Simformer using C2ST and expected coverage.

    Computes:
      1. C2ST between Simformer posterior samples and reference MCMC samples
      2. Expected coverage curve (calibration analysis)

    Args:
        model:             Trained SimformerScoreModel
        tokenizer:         Trained SBITokenizer
        simulator:         Simulator with reference_posterior() method
        attention_mask:    (d, d) attention mask
        n_test:            Number of test observations
        n_posterior_samples: Number of posterior samples per observation
        n_reference_samples: Number of reference MCMC samples per observation
        n_steps:           Number of reverse SDE steps (default: 500)
        sigma_min, sigma_max: VESDE parameters
        verbose:           Print progress

    Returns:
        results dict with c2st scores, mean c2st, coverage curves
    """
    if verbose:
        print(f"\nEvaluating posterior quality ({n_test} test observations)...")

    d = simulator.d
    var_ids = simulator.var_ids
    c2st_scores = []

    # Generate test observations
    test_data = simulator.sample_joint(n_test)   # (n_test, d)
    test_theta = test_data[:, :simulator.d_theta]
    test_x = test_data[:, simulator.d_theta:]

    # Build condition mask for posterior inference: observe data, infer params
    condition_mask = np.zeros(d)
    condition_mask[simulator.data_indices] = 1.0

    all_simformer_samples = []
    all_reference_samples = []

    for i in range(n_test):
        # Observed values: set data variables to test_x[i], params to 0 (will be sampled)
        x_obs = np.zeros(d)
        x_obs[simulator.data_indices] = test_x[i]

        # Simformer posterior samples via reverse SDE
        posterior_samples = sample_conditional(
            score_model=model,
            tokenizer=tokenizer,
            x_obs=x_obs,
            condition_mask=condition_mask,
            var_ids=var_ids,
            attention_mask=attention_mask,
            n_samples=n_posterior_samples,
            n_steps=n_steps,
            sigma_min=sigma_min,
            sigma_max=sigma_max,
        )
        # Extract parameter dimensions only
        simformer_params = posterior_samples[:, simulator.param_indices]   # (n_samples, d_theta)

        # Reference posterior samples (e.g., MCMC or analytic)
        reference_params = simulator.reference_posterior(test_x[i:i+1], n_reference_samples)

        # C2ST
        score = c2st(simformer_params, reference_params)
        c2st_scores.append(score)

        all_simformer_samples.append(simformer_params)
        all_reference_samples.append(reference_params)

        if verbose and (i + 1) % 10 == 0:
            print(f"  Test {i+1}/{n_test}: C2ST = {score:.4f}")

    mean_c2st = float(np.mean(c2st_scores))

    # Expected coverage (calibration)
    alpha_levels = np.linspace(0, 1, 21)

    def posterior_fn(obs):
        x_obs_local = np.zeros(d)
        x_obs_local[simulator.data_indices] = obs.flatten()[:simulator.d_x]
        samples = sample_conditional(
            score_model=model,
            tokenizer=tokenizer,
            x_obs=x_obs_local,
            condition_mask=condition_mask,
            var_ids=var_ids,
            attention_mask=attention_mask,
            n_samples=n_posterior_samples,
            n_steps=n_steps,
            sigma_min=sigma_min,
            sigma_max=sigma_max,
        )
        return samples[:, simulator.param_indices]

    alphas, coverages = expected_coverage(
        posterior_fn=posterior_fn,
        true_params=test_theta,
        observations=test_x,
        alpha_levels=alpha_levels,
        n_samples=n_posterior_samples,
    )

    results = {
        "c2st_scores": c2st_scores,
        "mean_c2st": mean_c2st,
        "alpha_levels": alphas,
        "coverages": coverages,
        "n_test": n_test,
    }

    if verbose:
        print(f"\n  Mean C2ST: {mean_c2st:.4f}  (0.5 = perfect, 1.0 = poor)")
        print(f"  Coverage deviation: {np.mean(np.abs(coverages - alphas)):.4f} "
              f"(0 = perfectly calibrated)")

    return results


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    """Run a complete Simformer training and evaluation pipeline."""

    # ---- Configuration ----
    # Choose simulator
    simulator = LinearGaussianSimulator(d_theta=5, d_x=5, sigma=1.0, seed=42)

    # Choose attention mask type: "dense", "undirected", or "directed"
    mask_type = "dense"
    adjacency = None   # Set for undirected/directed masks

    # Training hyperparameters (from paper Appendix A2.1)
    config = dict(
        n_simulations=10000,       # simulation budget (10^3, 10^4, or 10^5)
        batch_size=1000,           # training batch size
        max_epochs=200,            # max training epochs
        patience=20,               # early stopping patience
        lr=1e-3,                   # Adam learning rate
        token_dim=50,              # token dimension
        n_layers=6,                # transformer layers (6 benchmark, 8 for LV/SIRD/HH)
        n_heads=4,                 # attention heads
        head_dim=10,               # per-head attention dimension
        widening_factor=3,         # FF widening (hidden_dim = 50 * 3 = 150)
        time_fourier_dim=128,      # diffusion time embedding dimension
        sigma_min=0.0001,          # VESDE sigma_min
        sigma_max=15.0,            # VESDE sigma_max
        seed=0,
    )

    print("=" * 70)
    print(f"Simformer Training Pipeline")
    print(f"  Simulator:    {simulator.name}")
    print(f"  d_theta={simulator.d_theta}, d_x={simulator.d_x}, d={simulator.d}")
    print(f"  Mask type:    {mask_type}")
    print(f"  Simulations:  {config['n_simulations']}")
    print("=" * 70)

    # ---- Train ----
    model, tokenizer, attention_mask, train_info = train(
        simulator=simulator,
        mask_type=mask_type,
        adjacency=adjacency,
        verbose=True,
        **config,
    )

    # ---- Evaluate ----
    eval_results = evaluate_posterior(
        model=model,
        tokenizer=tokenizer,
        simulator=simulator,
        attention_mask=attention_mask,
        n_test=20,
        n_posterior_samples=1000,
        n_reference_samples=1000,
        n_steps=500,
        sigma_min=config["sigma_min"],
        sigma_max=config["sigma_max"],
        verbose=True,
    )

    # ---- Summary ----
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print(f"  Simulator:          {simulator.name}")
    print(f"  Attention mask:     {mask_type}")
    print(f"  Simulation budget:  {config['n_simulations']}")
    print(f"  Epochs trained:     {train_info['epochs_trained']}")
    print(f"  Best val loss:      {train_info['best_val_loss']:.6f}")
    print(f"  Mean C2ST:          {eval_results['mean_c2st']:.4f}")
    print(f"  Coverage deviation: {np.mean(np.abs(eval_results['coverages'] - eval_results['alpha_levels'])):.4f}")
    print("=" * 70)


if __name__ == "__main__":
    main()
