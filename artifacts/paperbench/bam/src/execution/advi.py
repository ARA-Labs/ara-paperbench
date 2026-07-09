"""
Automatic Differentiation Variational Inference (ADVI) Baseline
Implementation of Algorithm 2 from Cai et al. (2024) appendix.
Supports ELBO loss, score-based divergence loss, and Fisher divergence loss.
"""
import jax
import jax.numpy as jnp
from jax import random, grad, jit, vmap
from typing import Callable, Tuple


def negative_elbo_loss(
    mu: jnp.ndarray,
    Sigma: jnp.ndarray,
    log_p_unnorm: Callable,  # log unnormalized target: z -> scalar
    samples: jnp.ndarray,    # shape: (B, D), pre-drawn samples
) -> float:
    """
    Stochastic estimate of negative ELBO (Algorithm 2, step 4).
    
    L_ELBO(z_{1:B}) = -(1/B) sum_b [log p_tilde(z_b) - log q(z_b)]
    
    Args:
        mu: Variational mean, shape (D,)
        Sigma: Variational covariance, shape (D, D)
        log_p_unnorm: Log unnormalized target density
        samples: z_b ~ N(mu, Sigma), shape (B, D)
    
    Returns:
        Negative ELBO estimate (scalar)
    """
    B = samples.shape[0]
    D = mu.shape[0]
    
    # Log likelihood under target
    log_p_vals = vmap(log_p_unnorm)(samples)  # shape: (B,)
    
    # Log likelihood under variational distribution
    Sigma_inv = jnp.linalg.inv(Sigma)
    log_det = jnp.log(jnp.linalg.det(Sigma))
    diffs = samples - mu[None, :]  # shape: (B, D)
    mahal = jnp.sum(diffs @ Sigma_inv * diffs, axis=-1)  # shape: (B,)
    log_q_vals = -0.5 * (D * jnp.log(2 * jnp.pi) + log_det + mahal)  # shape: (B,)
    
    neg_elbo = -jnp.mean(log_p_vals - log_q_vals)
    return neg_elbo


def score_divergence_loss(
    mu: jnp.ndarray,
    Sigma: jnp.ndarray,
    score_fn: Callable,  # grad_z log p
    samples: jnp.ndarray, # shape: (B, D)
) -> float:
    """
    Stochastic estimate of score-based divergence (ADVI-Score variant).
    
    D(q;p) ≈ (1/B) sum_b ||grad log q(z_b) - grad log p(z_b)||^2_{Sigma}
    
    For gradient-based optimization of ADVI with score divergence.
    """
    B = samples.shape[0]
    Sigma_inv = jnp.linalg.inv(Sigma)
    
    # Score of q at samples: grad_z log q(z) = -Sigma^{-1}(z - mu)
    score_q = -(samples - mu[None, :]) @ Sigma_inv.T  # shape: (B, D)
    
    # Score of p at samples
    score_p = vmap(score_fn)(samples)  # shape: (B, D)
    
    # Score difference weighted by Sigma (covariance weighting)
    diff = score_q - score_p  # shape: (B, D)
    # ||diff||^2_Sigma = diff @ Sigma @ diff^T (per sample)
    weighted = diff @ Sigma  # shape: (B, D)
    loss = jnp.mean(jnp.sum(weighted * diff, axis=-1))
    
    return loss


def fisher_divergence_loss(
    mu: jnp.ndarray,
    Sigma: jnp.ndarray,
    score_fn: Callable,
    samples: jnp.ndarray, # shape: (B, D)
) -> float:
    """
    Stochastic estimate of Fisher divergence (ADVI-Fisher variant).
    
    F(q;p) ≈ (1/B) sum_b ||grad log q(z_b) - grad log p(z_b)||^2
    (unweighted, not affine invariant)
    """
    Sigma_inv = jnp.linalg.inv(Sigma)
    score_q = -(samples - mu[None, :]) @ Sigma_inv.T  # shape: (B, D)
    score_p = vmap(score_fn)(samples)  # shape: (B, D)
    diff = score_q - score_p
    return jnp.mean(jnp.sum(diff**2, axis=-1))


def adam_update(
    params: Tuple[jnp.ndarray, jnp.ndarray],
    grads: Tuple[jnp.ndarray, jnp.ndarray],
    m: Tuple[jnp.ndarray, jnp.ndarray],
    v: Tuple[jnp.ndarray, jnp.ndarray],
    t: int,
    lr: float,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> Tuple:
    """Standard Adam optimizer update step."""
    m_new = tuple(beta1 * mi + (1 - beta1) * gi for mi, gi in zip(m, grads))
    v_new = tuple(beta2 * vi + (1 - beta2) * gi**2 for vi, gi in zip(v, grads))
    
    m_hat = tuple(mi / (1 - beta1**t) for mi in m_new)
    v_hat = tuple(vi / (1 - beta2**t) for vi in v_new)
    
    params_new = tuple(p - lr * mh / (jnp.sqrt(vh) + eps)
                      for p, mh, vh in zip(params, m_hat, v_hat))
    
    return params_new, m_new, v_new


def run_advi(
    key: jax.random.PRNGKey,
    mu_init: jnp.ndarray,
    Sigma_init: jnp.ndarray,
    log_p_or_score_fn: Callable,  # Either log p (unnorm) or score function
    num_iters: int,
    batch_size: int,
    learning_rate: float,
    loss_type: str = 'elbo',      # 'elbo', 'score', or 'fisher'
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    Run ADVI for num_iters iterations (Algorithm 2).
    
    Supports three loss variants:
    - 'elbo': Standard ADVI (ELBO maximization via ADAM)
    - 'score': Score-based divergence with ADAM
    - 'fisher': Fisher divergence with ADAM
    
    Args:
        key: JAX PRNG key
        mu_init: Initial mean, shape (D,)
        Sigma_init: Initial covariance, shape (D, D)
        log_p_or_score_fn: Log unnorm density (elbo) or score function (score/fisher)
        num_iters: T
        batch_size: B
        learning_rate: Adam learning rate (e.g., 0.01 for ELBO/Fisher Gaussian)
        loss_type: Which divergence to minimize
    
    Returns:
        mu_final: shape (D,)
        Sigma_final: shape (D, D)
    """
    D = mu_init.shape[0]
    mu = mu_init
    Sigma = Sigma_init
    
    m_mu = jnp.zeros_like(mu)
    m_Sigma = jnp.zeros_like(Sigma)
    v_mu = jnp.zeros_like(mu)
    v_Sigma = jnp.zeros_like(Sigma)
    
    def compute_loss_and_grad(mu, Sigma, samples):
        if loss_type == 'elbo':
            loss = negative_elbo_loss(mu, Sigma, log_p_or_score_fn, samples)
        elif loss_type == 'score':
            loss = score_divergence_loss(mu, Sigma, log_p_or_score_fn, samples)
        elif loss_type == 'fisher':
            loss = fisher_divergence_loss(mu, Sigma, log_p_or_score_fn, samples)
        else:
            raise ValueError(f"Unknown loss_type: {loss_type}")
        return loss
    
    for t in range(1, num_iters + 1):
        key, subkey = random.split(key)
        L = jnp.linalg.cholesky(Sigma)
        eps = random.normal(subkey, shape=(batch_size, D))
        samples = mu[None, :] + eps @ L.T  # shape: (B, D)
        
        # Compute gradients via JAX
        loss_fn = lambda mu_, Sigma_: compute_loss_and_grad(mu_, Sigma_, samples)
        grads = grad(loss_fn, argnums=(0, 1))(mu, Sigma)
        
        params = (mu, Sigma)
        m = (m_mu, m_Sigma)
        v = (v_mu, v_Sigma)
        
        params, m, v = adam_update(params, grads, m, v, t, learning_rate)
        mu, Sigma = params
        m_mu, m_Sigma = m
        v_mu, v_Sigma = v
        
        # Project Sigma to be PD (add small regularization if needed)
        Sigma = 0.5 * (Sigma + Sigma.T)
        min_eig = jnp.min(jnp.linalg.eigvalsh(Sigma))
        if min_eig < 1e-6:
            Sigma = Sigma + (1e-6 - min_eig) * jnp.eye(D)
    
    return mu, Sigma
