"""
Score-Based and Fisher Divergence Estimators
For evaluation and comparison (not for optimization in BaM).
"""
import jax
import jax.numpy as jnp
from jax import vmap, random
from typing import Callable


def estimate_score_divergence(
    mu: jnp.ndarray,    # Variational mean, shape (D,)
    Sigma: jnp.ndarray, # Variational covariance, shape (D, D)
    score_fn: Callable, # Target score: z -> grad_z log p(z)
    key: jax.random.PRNGKey,
    n_samples: int = 1000,
) -> float:
    """
    Monte Carlo estimate of score-based divergence D(q; p).
    
    D(q; p) = E_q[||grad log q(z) - grad log p(z)||^2_{Sigma}]
    
    For Gaussian q = N(mu, Sigma):
        grad log q(z) = -Sigma^{-1}(z - mu)
    
    Args:
        mu: Variational mean, shape (D,)
        Sigma: Variational covariance, shape (D, D)
        score_fn: Target score function
        key: JAX PRNG key
        n_samples: Number of Monte Carlo samples
    
    Returns:
        Estimated D(q; p) (scalar)
    
    Equation (2) in paper; affine invariant.
    """
    D = mu.shape[0]
    L = jnp.linalg.cholesky(Sigma)
    eps = random.normal(key, shape=(n_samples, D))
    samples = mu[None, :] + eps @ L.T  # shape: (N, D)
    
    Sigma_inv = jnp.linalg.inv(Sigma)
    score_q = -(samples - mu[None, :]) @ Sigma_inv.T  # shape: (N, D)
    score_p = vmap(score_fn)(samples)                  # shape: (N, D)
    
    diff = score_q - score_p  # shape: (N, D)
    # ||diff||^2_Sigma = diff @ Sigma @ diff.T per sample
    weighted = diff @ Sigma  # shape: (N, D)
    per_sample = jnp.sum(weighted * diff, axis=-1)  # shape: (N,)
    
    return jnp.mean(per_sample)


def estimate_fisher_divergence(
    mu: jnp.ndarray,
    Sigma: jnp.ndarray,
    score_fn: Callable,
    key: jax.random.PRNGKey,
    n_samples: int = 1000,
) -> float:
    """
    Monte Carlo estimate of Fisher divergence F(q; p) = E_q[||grad log q - grad log p||^2].
    
    NOT affine invariant (unweighted). Used as baseline in paper (ADVI-Fisher).
    
    Args:
        mu: Variational mean, shape (D,)
        Sigma: Variational covariance, shape (D, D)
        score_fn: Target score function
        key: JAX PRNG key
        n_samples: Number of Monte Carlo samples
    
    Returns:
        Estimated F(q; p) (scalar)
    """
    D = mu.shape[0]
    L = jnp.linalg.cholesky(Sigma)
    eps = random.normal(key, shape=(n_samples, D))
    samples = mu[None, :] + eps @ L.T
    
    Sigma_inv = jnp.linalg.inv(Sigma)
    score_q = -(samples - mu[None, :]) @ Sigma_inv.T
    score_p = vmap(score_fn)(samples)
    
    diff = score_q - score_p
    return jnp.mean(jnp.sum(diff**2, axis=-1))


def gaussian_score_divergence_analytic(
    mu: jnp.ndarray,    # Variational mean, shape (D,)
    Sigma: jnp.ndarray, # Variational covariance, shape (D, D)
    mu_star: jnp.ndarray,    # Target mean, shape (D,)
    Sigma_star: jnp.ndarray, # Target covariance, shape (D, D)
) -> float:
    """
    Analytic score-based divergence between two Gaussians (Proposition A.7).
    
    D(q; p) = tr[(I - Sigma @ Sigma_star^{-1})^2] + (mu - mu_star)^T Sigma_star^{-1} Sigma Sigma_star^{-1} (mu - mu_star)
    
    Used for evaluation when target is Gaussian.
    
    Args:
        mu, Sigma: Variational parameters
        mu_star, Sigma_star: Target Gaussian parameters
    
    Returns:
        D(q; p) (scalar)
    
    Proposition A.7 in paper.
    """
    Sigma_star_inv = jnp.linalg.inv(Sigma_star)
    M = jnp.eye(mu.shape[0]) - Sigma @ Sigma_star_inv  # I - Sigma @ Sigma_star^{-1}
    trace_term = jnp.trace(M @ M)
    diff = mu - mu_star
    quad_term = diff @ Sigma_star_inv @ Sigma @ Sigma_star_inv @ diff
    return trace_term + quad_term


def estimate_kl_gaussian(
    mu: jnp.ndarray,
    Sigma: jnp.ndarray,
    mu_star: jnp.ndarray,
    Sigma_star: jnp.ndarray,
    direction: str = 'reverse',  # 'reverse': KL(q||p); 'forward': KL(p||q)
) -> float:
    """
    Analytic KL divergence between two Gaussians.
    Used as evaluation metric in experiments.
    
    Args:
        mu, Sigma: Variational parameters (q)
        mu_star, Sigma_star: Target parameters (p)
        direction: 'reverse' = KL(q||p), 'forward' = KL(p||q)
    
    Returns:
        KL divergence (scalar)
    """
    D = mu.shape[0]
    
    if direction == 'reverse':
        # KL(q || p) = KL(N(mu,Sigma) || N(mu_star, Sigma_star))
        Sigma_star_inv = jnp.linalg.inv(Sigma_star)
        diff = mu - mu_star
        kl = 0.5 * (
            jnp.trace(Sigma_star_inv @ Sigma)
            + diff @ Sigma_star_inv @ diff
            - D
            + jnp.log(jnp.linalg.det(Sigma_star) / jnp.linalg.det(Sigma))
        )
    else:
        # KL(p || q) = KL(N(mu_star, Sigma_star) || N(mu, Sigma))
        Sigma_inv = jnp.linalg.inv(Sigma)
        diff = mu_star - mu
        kl = 0.5 * (
            jnp.trace(Sigma_inv @ Sigma_star)
            + diff @ Sigma_inv @ diff
            - D
            + jnp.log(jnp.linalg.det(Sigma) / jnp.linalg.det(Sigma_star))
        )
    
    return kl
