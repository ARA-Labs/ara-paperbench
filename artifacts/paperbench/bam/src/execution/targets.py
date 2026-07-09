"""
Target Distribution Implementations for BaM Experiments
Paper: "Batch and Match: BBVI with a Score-Based Divergence"

Implements:
  1. Gaussian targets (D=4, 16, 64, 256) with analytical score functions
  2. Sinh-arcsinh normal distributions (D=10, varying skew and tail)
  3. VAE posterior target (D=256, CIFAR-10)
  
All score functions return ∇ log p(z) for samples z ∈ R^{D}.
Score computation uses JAX autodiff via jax.grad for non-Gaussian targets.
"""

import numpy as np
import jax
import jax.numpy as jnp
from jax import jit, grad, vmap
import numpyro.distributions as dist
from typing import Tuple, Callable


# ============================================================
# 1. GAUSSIAN TARGET DISTRIBUTIONS
#    Used in: Experiment E01 (D=4, 16, 64, 256)
# ============================================================

def make_gaussian_target(D: int, seed: int = 42) -> Tuple[np.ndarray, np.ndarray, Callable, Callable]:
    """
    Construct a random Gaussian target distribution N(μ*, Σ*).
    Σ* = AA^T where A is random D×D.
    
    Used in Figure 5.1 experiments with:
      - D=4:   BaM B=2 and B=5;   ADVI/GSM/Score/Fisher B=2
      - D=16:  BaM B=2 and B=15;  ADVI/GSM/Score/Fisher B=2
      - D=64:  BaM B=2 and B=40;  ADVI/GSM/Score/Fisher B=2
      - D=256: BaM B=2 and B=150; ADVI/GSM/Score/Fisher B=2
    
    Args:
        D:    Dimension
        seed: Random seed for reproducibility
    
    Returns:
        mean_star: (D,) true posterior mean
        cov_star:  (D,D) true posterior covariance
        lp:        Log-probability function lp(x: (N,D)) -> (N,)
        lp_g:      Score function lp_g(x: (N,D)) -> (N,D)
    """
    rng = np.random.default_rng(seed)
    mean_star = rng.random(D)
    A = rng.standard_normal((D, D))
    cov_star = A @ A.T + np.eye(D) * 1e-3

    model = dist.MultivariateNormal(
        loc=jnp.array(mean_star),
        covariance_matrix=jnp.array(cov_star)
    )

    @jit
    def lp(x):
        """Log probability of batch x: (N, D) -> (N,)"""
        return model.log_prob(x)

    @jit
    def lp_g(x):
        """Score = ∇ log p(z): (N, D) -> (N, D)"""
        # Analytical score for Gaussian: ∇ log N(z; μ, Σ) = -Σ^{-1}(z - μ)
        # Uses JAX autodiff for generality:
        score_fn = vmap(grad(lambda z: jnp.sum(lp(z[None]))))
        return score_fn(x)

    return mean_star, cov_star, lp, lp_g


def gaussian_score_analytical(
    samples: np.ndarray,   # (N, D)
    mean: np.ndarray,      # (D,)
    cov: np.ndarray,       # (D, D)
) -> np.ndarray:
    """
    Analytical score for Gaussian: ∇ log N(z; μ, Σ) = -Σ^{-1}(z - μ).
    Faster than autodiff for large batches.
    
    Args:
        samples: (N, D) sample points
        mean:    (D,) Gaussian mean
        cov:     (D, D) Gaussian covariance
    Returns:
        scores:  (N, D) score vectors
    """
    cov_inv = np.linalg.inv(cov)
    return -(samples - mean) @ cov_inv.T


# ============================================================
# 2. SINH-ARCSINH NORMAL DISTRIBUTION
#    Used in: Experiment E02 (D=10, varying s and τ)
# ============================================================

def sinh_arcsinh_transform(y: jnp.ndarray, s: float, tau: float) -> jnp.ndarray:
    """
    Sinh-arcsinh transformation: z = sinh((1/τ)(arcsinh(y) + s))
    
    From Jones & Pewsey (2009, 2019). Gaussian recovered at s=0, τ=1.
    
    Args:
        y:   Input samples (Gaussian)
        s:   Skewness parameter (s=0: symmetric)
        tau: Tail parameter (τ=1: normal tails; τ<1: lighter; τ>1: heavier)
    Returns:
        z:   Transformed samples
    """
    return jnp.sinh((1.0 / tau) * (jnp.arcsinh(y) + s))


def make_sinh_arcsinh_target(
    D: int = 10,
    skew: float = 0.0,    # s parameter
    tail: float = 1.0,    # τ parameter
    seed: int = 42,
) -> Tuple[Callable, Callable]:
    """
    Construct D-dimensional sinh-arcsinh normal target distribution.
    
    Configurations tested in Figure 5.2 (all D=10, B=5 for ADVI/GSM; B=5,10 for BaM):
      Normal tails (τ=1), varying skew:
        - (τ=1, s=0.2): mild skew
        - (τ=1, s=1.0): moderate skew
        - (τ=1, s=1.8): high skew (GSM/Score diverge here)
      No skew (s=0), varying tails:
        - (τ=0.1, s=0): very light tails
        - (τ=0.9, s=0): slightly light tails
        - (τ=1.7, s=0): heavy tails
    
    Learning rate: λ_t = BD/(t+1) (decaying) for BaM; 10^4 iterations; 10 seeds.
    ADVI lr: 0.02; Fisher lr: 0.05; Score lr: per-configuration via grid search.
    
    Args:
        D:    Dimension (10 in paper)
        skew: s parameter
        tail: τ parameter
        seed: Random seed
    
    Returns:
        lp:   Log-probability function (unnormalized OK; uses autodiff)
        lp_g: Score function via JAX autodiff
    """
    rng = np.random.default_rng(seed)
    base_mean = rng.random(D) * 0.1
    base_cov = np.eye(D)

    base_dist = dist.MultivariateNormal(
        loc=jnp.array(base_mean),
        covariance_matrix=jnp.array(base_cov)
    )

    def log_prob_single(z: jnp.ndarray) -> jnp.ndarray:
        """
        Log prob of sinh-arcsinh normal at z.
        Uses change-of-variables: z = sinh_arcsinh(y), y ~ N(base_mean, base_cov).
        Log |dz/dy| term included for proper density.
        """
        # Inverse transform: y = sinh(τ * arcsinh(z) - s)
        y = jnp.sinh(tail * jnp.arcsinh(z) - skew)
        # Log Jacobian of inverse: d/dz[sinh(τ*arcsinh(z)-s)] = τ*cosh(τ*arcsinh(z)-s)/sqrt(1+z²)
        log_jac = (jnp.log(tail)
                   + jnp.log(jnp.cosh(tail * jnp.arcsinh(z) - skew))
                   - 0.5 * jnp.log(1.0 + z ** 2))
        return jnp.sum(base_dist.log_prob(y) + log_jac)

    @jit
    def lp(x: jnp.ndarray) -> jnp.ndarray:
        """Log probability for batch x: (N, D) -> (N,)"""
        return vmap(log_prob_single)(x)

    @jit
    def lp_g(x: jnp.ndarray) -> jnp.ndarray:
        """Score ∇ log p(z) for batch x: (N, D) -> (N, D) via autodiff."""
        return vmap(grad(log_prob_single))(x)

    return lp, lp_g


# ============================================================
# 3. KL DIVERGENCE MEASUREMENT
#    Used in: All synthetic target experiments (E01, E02)
# ============================================================

def empirical_forward_kl(
    ref_samples: np.ndarray,   # (N, D) samples from target p
    q_log_prob: Callable,      # log q(x): (N, D) -> (N,)
    p_log_prob: Callable,      # log p(x): (N, D) -> (N,)
) -> float:
    """
    Empirical estimate of forward KL: KL(p; q) = E_p[log p - log q].
    
    Used in all synthetic experiments to monitor convergence.
    Requires reference samples from p (HMC or analytical).
    
    Args:
        ref_samples:  (N, D) samples drawn from the target distribution p
        q_log_prob:   Current variational log-probability function
        p_log_prob:   Target log-probability function
    Returns:
        fkl: Empirical forward KL estimate
    """
    log_p = p_log_prob(ref_samples)
    log_q = q_log_prob(ref_samples)
    return float(jnp.mean(log_p - log_q))


def empirical_reverse_kl(
    q_samples: np.ndarray,     # (N, D) samples from q
    q_log_prob: Callable,      # log q(x): (N, D) -> (N,)
    p_log_prob: Callable,      # log p(x): (N, D) -> (N,)
) -> float:
    """
    Empirical estimate of reverse KL: KL(q; p) = E_q[log q - log p].
    
    Args:
        q_samples:  (N, D) samples drawn from the current variational distribution q
        q_log_prob: Current variational log-probability function
        p_log_prob: Target log-probability function
    Returns:
        rkl: Empirical reverse KL estimate
    """
    log_q = q_log_prob(q_samples)
    log_p = p_log_prob(q_samples)
    return float(jnp.mean(log_q - log_p))


# ============================================================
# 4. POSTERIORDB TARGET DISTRIBUTIONS
#    Used in: Experiment E03 (arK D=7, gp-pois-regr D=13, eight-schools D=10)
# ============================================================

def make_posteriordb_target(
    model_name: str,    # e.g., "arK-arK", "gp-pois-regr-gp_pois_regr_model", "eight_schools-eight_schools_centered"
) -> Tuple[Callable, Callable, np.ndarray]:
    """
    Load a PosteriorDB model and create score function via BridgeStan.
    
    Models used in paper (Figure 5.3):
      - arK:               D=7,  nearly Gaussian
      - gp-pois-regr:      D=13, GP Poisson regression (non-Gaussian)
      - eight-schools-centered: D=10, hierarchical Bayesian (highly non-Gaussian)
    
    Score computation uses BridgeStan for efficient JAX-compatible gradients.
    HMC reference samples from PosteriorDB used for evaluation metric.
    
    Args:
        model_name: PosteriorDB model identifier
    Returns:
        lp:          Log-probability function
        lp_g:        Score function (via BridgeStan autodiff)
        hmc_samples: (N, D) reference HMC samples for ground-truth evaluation
    
    Note: Requires posteriordb and bridgestan Python packages.
    """
    # Implementation requires:
    # import posteriordb; import bridgestan as bs
    # pdb = posteriordb.PosteriorDatabase()
    # posterior = pdb.posterior(model_name)
    # stan_model = bs.StanModel.from_stan_file(posterior.stan_code_file_path(), ...)
    # hmc_samples = posterior.reference_draws_info()
    raise NotImplementedError("Requires posteriordb and bridgestan packages")


def relative_mean_error(
    mu_hat: np.ndarray,   # (D,) variational posterior mean estimate
    mu_ref: np.ndarray,   # (D,) HMC reference posterior mean
    sigma_ref: np.ndarray, # (D,) HMC reference posterior std dev
) -> float:
    """
    Relative mean error: ||( μ_hat - μ_ref ) / σ_ref||_2 (Equation 242, Appendix E.5).
    
    Measures how well the variational posterior mean matches HMC reference.
    
    Args:
        mu_hat:    (D,) estimated posterior mean
        mu_ref:    (D,) HMC reference mean
        sigma_ref: (D,) HMC reference standard deviation
    Returns:
        Relative mean error (scalar)
    """
    return float(np.linalg.norm((mu_hat - mu_ref) / sigma_ref))


def relative_sd_error(
    sigma_hat: np.ndarray,  # (D,) variational posterior std dev estimate
    sigma_ref: np.ndarray,  # (D,) HMC reference posterior std dev
) -> float:
    """
    Relative standard deviation error: ||(σ_hat - σ_ref) / σ_ref||_2 (Equation 242, Appendix E.5).
    
    Args:
        sigma_hat: (D,) estimated posterior standard deviation (sqrt of diagonal of Σ)
        sigma_ref: (D,) HMC reference standard deviation
    Returns:
        Relative SD error (scalar)
    """
    return float(np.linalg.norm((sigma_hat - sigma_ref) / sigma_ref))
