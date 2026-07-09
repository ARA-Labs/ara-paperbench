"""
Gaussian Score Matching (GSM) Variational Inference Baseline
Implementation of Algorithm 3 from Cai et al. (2024) appendix.
Reference: Modi et al. (2023), "Variational Inference with Gaussian Score Matching"
"""
import jax
import jax.numpy as jnp
from jax import random, vmap
from typing import Callable, Tuple


def gsm_sample_update(
    z_b: jnp.ndarray,   # shape: (D,), single sample
    s_b: jnp.ndarray,   # shape: (D,), target score at z_b
    mu: jnp.ndarray,    # shape: (D,), current mean
    Sigma: jnp.ndarray, # shape: (D, D), current covariance
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    GSM update for a single sample (Algorithm 3, steps 5-7).
    
    Solves the GSM matching condition for one sample:
    min_{q} KL(q_t; q) such that grad log q(z_b) = grad log p(z_b)
    
    Args:
        z_b: Sample from current approximation, shape (D,)
        s_b: Score of target at z_b: s_b = grad log p(z_b), shape (D,)
        mu: Current mean, shape (D,)
        Sigma: Current covariance, shape (D, D)
    
    Returns:
        delta_mu_b: Mean update contribution, shape (D,)
        delta_Sigma_b: Covariance update contribution, shape (D, D)
    
    Reference: Equations in Algorithm 3, Modi et al. (2023)
    """
    # epsilon_b = Sigma @ s_b - mu + z_b
    eps_b = Sigma @ s_b - mu + z_b  # shape: (D,)
    
    # Solve for rho > 0: rho(1+rho) = s_b^T @ Sigma @ s_b + (mu-z_b)^T @ s_b / 2
    # Quadratic: rho^2 + rho - c = 0, where c = s_b^T Sigma s_b + (mu-z_b).T s_b / 2
    c = s_b @ Sigma @ s_b + 0.5 * (mu - z_b) @ s_b
    rho = 0.5 * (-1.0 + jnp.sqrt(1.0 + 4.0 * jnp.maximum(c, 0.0)))  # positive root
    
    # Mean update for this sample
    mu_tilde_b = mu + (1.0 / (1.0 + rho)) * (
        eps_b - (mu - z_b) @ s_b[:, None] * jnp.eye(mu.shape[0]) @ (mu - z_b) / 
        (1.0 + rho + (mu - z_b) @ s_b)
    )
    # Simplified formula from Algorithm 3:
    denom = 1.0 + rho + (mu - z_b) @ s_b
    delta_mu_b = (1.0 / (1.0 + rho)) * (Sigma @ s_b - (mu - z_b) * (mu - z_b) @ s_b / denom)
    
    mu_tilde_b_val = mu + delta_mu_b
    
    # Covariance update
    delta_Sigma_b = (
        jnp.outer(mu - z_b, mu - z_b) 
        - jnp.outer(mu_tilde_b_val - z_b, mu_tilde_b_val - z_b)
    )
    
    return delta_mu_b, delta_Sigma_b


def run_gsm(
    key: jax.random.PRNGKey,
    mu_init: jnp.ndarray,
    Sigma_init: jnp.ndarray,
    score_fn: Callable,  # s(z) = grad_z log p(z)
    num_iters: int,
    batch_size: int,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    Run GSM for num_iters iterations (Algorithm 3).
    
    No learning rate required (GSM does not use regularization).
    
    Args:
        key: JAX PRNG key
        mu_init: Initial mean, shape (D,)
        Sigma_init: Initial covariance, shape (D, D)
        score_fn: Target score function z -> grad_z log p(z)
        num_iters: Number of iterations T
        batch_size: Batch size B
    
    Returns:
        mu_final: shape (D,)
        Sigma_final: shape (D, D)
    
    Algorithm 3 in paper appendix.
    """
    D = mu_init.shape[0]
    mu = mu_init
    Sigma = Sigma_init
    
    for t in range(num_iters):
        key, subkey = random.split(key)
        
        # Step 3: Sample batch from current approximation
        L = jnp.linalg.cholesky(Sigma)
        eps = random.normal(subkey, shape=(batch_size, D))
        samples = mu[None, :] + eps @ L.T  # shape: (B, D)
        
        # Step 4-8: Compute per-sample updates
        delta_mu_sum = jnp.zeros_like(mu)
        delta_Sigma_sum = jnp.zeros_like(Sigma)
        
        for b in range(batch_size):
            z_b = samples[b]
            s_b = score_fn(z_b)
            delta_mu_b, delta_Sigma_b = gsm_sample_update(z_b, s_b, mu, Sigma)
            delta_mu_sum += delta_mu_b
            delta_Sigma_sum += delta_Sigma_b
        
        # Step 9: Average updates
        mu = mu + delta_mu_sum / batch_size
        Sigma = Sigma + delta_Sigma_sum / batch_size
        
        # Ensure positive definiteness
        Sigma = 0.5 * (Sigma + Sigma.T)
        min_eig = jnp.min(jnp.linalg.eigvalsh(Sigma))
        if min_eig < 1e-6:
            Sigma = Sigma + (1e-6 - min_eig) * jnp.eye(D)
    
    return mu, Sigma
