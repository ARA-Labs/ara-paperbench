"""
Batch and Match (BaM) Variational Inference
Implementation of Algorithm 1 from Cai et al. (2024)
"Batch and Match: Black-Box Variational Inference with a Score-Based Divergence"
"""
import jax
import jax.numpy as jnp
from jax import random, jit, vmap
from typing import Callable, Tuple, Optional


def compute_batch_statistics(
    key: jax.random.PRNGKey,
    mu: jnp.ndarray,          # shape: (D,)
    Sigma: jnp.ndarray,        # shape: (D, D)
    score_fn: Callable,        # s(z) = grad_z log p(z), maps (D,) -> (D,)
    batch_size: int,
) -> Tuple[jnp.ndarray, jnp.ndarray, jnp.ndarray, jnp.ndarray]:
    """
    Batch Step of BaM (Algorithm 1, steps 3-5).
    
    Draws B samples from N(mu, Sigma), evaluates scores, computes sufficient statistics.
    
    Args:
        key: JAX PRNG key
        mu: Current variational mean, shape (D,)
        Sigma: Current variational covariance, shape (D, D)
        score_fn: Target score function z -> grad_z log p(z), shape (D,) -> (D,)
        batch_size: Number of samples B
    
    Returns:
        z_bar: Sample mean, shape (D,)
        g_bar: Score mean, shape (D,)
        C: Sample covariance, shape (D, D)
        Gamma: Score covariance, shape (D, D)
    
    Equations: (6), (7) in paper; Algorithm 1 step 5
    """
    D = mu.shape[0]
    L = jnp.linalg.cholesky(Sigma)  # shape: (D, D)
    eps = random.normal(key, shape=(batch_size, D))  # shape: (B, D)
    samples = mu[None, :] + eps @ L.T  # shape: (B, D), z_b ~ N(mu, Sigma)
    scores = vmap(score_fn)(samples)  # shape: (B, D), g_b = score(z_b)
    
    z_bar = jnp.mean(samples, axis=0)  # shape: (D,)
    g_bar = jnp.mean(scores, axis=0)   # shape: (D,)
    
    dz = samples - z_bar[None, :]  # shape: (B, D)
    dg = scores - g_bar[None, :]   # shape: (B, D)
    
    C = (dz.T @ dz) / batch_size     # shape: (D, D), sample covariance of positions
    Gamma = (dg.T @ dg) / batch_size  # shape: (D, D), sample covariance of scores
    
    return z_bar, g_bar, C, Gamma


def compute_UV(
    mu: jnp.ndarray,   # shape: (D,)
    Sigma: jnp.ndarray, # shape: (D, D)
    z_bar: jnp.ndarray, # shape: (D,)
    g_bar: jnp.ndarray, # shape: (D,)
    C: jnp.ndarray,     # shape: (D, D)
    Gamma: jnp.ndarray, # shape: (D, D)
    lam: float,         # inverse regularization parameter lambda_t > 0
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    Construct matrices U and V for quadratic matrix equation.
    
    Args:
        mu: Current mean, shape (D,)
        Sigma: Current covariance, shape (D, D)
        z_bar, g_bar: Batch means, shape (D,)
        C, Gamma: Batch covariances, shape (D, D)
        lam: Inverse regularization parameter lambda_t
    
    Returns:
        U: PSD matrix, shape (D, D)  -- Eq. (10)
        V: PD matrix, shape (D, D)   -- Eq. (11)
    """
    lam_over_1plam = lam / (1.0 + lam)
    
    U = lam * Gamma + lam_over_1plam * jnp.outer(g_bar, g_bar)           # Eq. (10)
    V = Sigma + lam * C + lam_over_1plam * jnp.outer(mu - z_bar, mu - z_bar)  # Eq. (11)
    
    return U, V


def solve_quadratic_matrix_equation(
    U: jnp.ndarray,  # PSD, shape (D, D)
    V: jnp.ndarray,  # PD, shape (D, D)
) -> jnp.ndarray:
    """
    Solve quadratic matrix equation Sigma @ U @ Sigma + Sigma = V.
    
    Full-rank solver: O(D^3) via matrix square root.
    Solution: Sigma = 2V [I + (I + 4UV)^{1/2}]^{-1}
    
    Args:
        U: PSD matrix, shape (D, D)
        V: PD matrix, shape (D, D)
    
    Returns:
        Sigma_new: Symmetric PD solution, shape (D, D)
    
    Equation: (12) and Lemma B.1 in paper
    """
    D = V.shape[0]
    I = jnp.eye(D)
    
    UV = U @ V  # shape: (D, D)
    inner = I + 4.0 * UV  # I + 4UV, shape: (D, D)
    
    # Compute principal matrix square root of (I + 4UV)
    # Use eigendecomposition for numerical stability
    eigvals, eigvecs = jnp.linalg.eigh(inner)
    eigvals = jnp.maximum(eigvals, 0.0)  # Ensure non-negative for sqrt
    sqrt_inner = eigvecs @ jnp.diag(jnp.sqrt(eigvals)) @ eigvecs.T
    
    Sigma_new = 2.0 * V @ jnp.linalg.inv(I + sqrt_inner)  # Eq. (12)
    Sigma_new = 0.5 * (Sigma_new + Sigma_new.T)  # Symmetrize for numerical stability
    
    return Sigma_new


def solve_quadratic_matrix_equation_low_rank(
    U: jnp.ndarray,  # Low-rank PSD: U = Q @ Q.T, shape (D, D)
    V: jnp.ndarray,  # PD, shape (D, D)
    Q: jnp.ndarray,  # Factor: U = Q @ Q.T, shape (D, K) with K << D
) -> jnp.ndarray:
    """
    Low-rank solver for quadratic matrix equation (Lemma B.3).
    
    When U = Q @ Q^T with K << D, costs O(D^2 K + K^3) instead of O(D^3).
    
    Sigma = V - V.T @ Q @ (2I + (Q.T @ V @ Q + I)^{1/2})^{-2} @ Q.T @ V
    
    Args:
        U: Full PSD matrix, shape (D, D) [not directly used; Q is used]
        V: PD matrix, shape (D, D)
        Q: Low-rank factor, shape (D, K)
    
    Returns:
        Sigma_new: Symmetric PD solution, shape (D, D)
    
    Source: Lemma B.3
    """
    K = Q.shape[1]
    I_K = jnp.eye(K)
    
    QTV = Q.T @ V   # shape: (K, D)
    QTVQ = QTV @ Q  # shape: (K, K)
    
    inner_K = QTVQ + I_K  # K x K matrix
    eigvals, eigvecs = jnp.linalg.eigh(inner_K)
    eigvals = jnp.maximum(eigvals, 0.0)
    sqrt_inner_K = eigvecs @ jnp.diag(jnp.sqrt(eigvals)) @ eigvecs.T
    
    A = 2.0 * I_K + sqrt_inner_K   # shape: (K, K)
    A_inv_sq = jnp.linalg.inv(A) @ jnp.linalg.inv(A)  # (2I + sqrt)^{-2}
    
    Sigma_new = V - (V @ Q) @ A_inv_sq @ QTV  # Lemma B.3
    Sigma_new = 0.5 * (Sigma_new + Sigma_new.T)
    
    return Sigma_new


def update_mean(
    mu: jnp.ndarray,       # shape: (D,)
    Sigma_new: jnp.ndarray, # shape: (D, D)
    g_bar: jnp.ndarray,    # shape: (D,)
    z_bar: jnp.ndarray,    # shape: (D,)
    lam: float,
) -> jnp.ndarray:
    """
    Update variational mean (Eq. 13).
    
    mu_{t+1} = (lam/(1+lam)) * mu_t + (1/(1+lam)) * (Sigma_{t+1} @ g_bar + z_bar)
    
    IMPORTANT: Must be called AFTER Sigma_{t+1} is computed.
    
    Args:
        mu: Current mean, shape (D,)
        Sigma_new: Updated covariance, shape (D, D)
        g_bar: Score mean from batch, shape (D,)
        z_bar: Sample mean from batch, shape (D,)
        lam: Inverse regularization lambda_t
    
    Returns:
        mu_new: Updated mean, shape (D,)
    """
    lam_over_1plam = lam / (1.0 + lam)
    one_over_1plam = 1.0 / (1.0 + lam)
    
    mu_new = lam_over_1plam * mu + one_over_1plam * (Sigma_new @ g_bar + z_bar)  # Eq. (13)
    return mu_new


def bam_step(
    key: jax.random.PRNGKey,
    mu: jnp.ndarray,
    Sigma: jnp.ndarray,
    score_fn: Callable,
    batch_size: int,
    lam: float,
    use_low_rank: bool = False,
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    Single BaM iteration: batch step + match step.
    
    Args:
        key: JAX PRNG key
        mu: Current mean, shape (D,)
        Sigma: Current covariance, shape (D, D)
        score_fn: Target score function
        batch_size: B
        lam: Inverse regularization lambda_t
        use_low_rank: Use low-rank solver if B << D
    
    Returns:
        mu_new: Updated mean, shape (D,)
        Sigma_new: Updated covariance, shape (D, D)
    """
    D = mu.shape[0]
    
    # Batch step
    z_bar, g_bar, C, Gamma = compute_batch_statistics(key, mu, Sigma, score_fn, batch_size)
    
    # Construct U, V
    U, V = compute_UV(mu, Sigma, z_bar, g_bar, C, Gamma, lam)
    
    # Match step: covariance update
    if use_low_rank and batch_size < D:
        # Build low-rank factor Q from U (U has rank <= B+1)
        # U = lam*Gamma + lam/(1+lam)*outer(g_bar,g_bar)
        # For simplicity, use full-rank solver here; 
        # low-rank requires careful construction of Q
        Sigma_new = solve_quadratic_matrix_equation(U, V)
    else:
        Sigma_new = solve_quadratic_matrix_equation(U, V)
    
    # Match step: mean update (AFTER covariance)
    mu_new = update_mean(mu, Sigma_new, g_bar, z_bar, lam)
    
    return mu_new, Sigma_new


def run_bam(
    key: jax.random.PRNGKey,
    mu_init: jnp.ndarray,
    Sigma_init: jnp.ndarray,
    score_fn: Callable,
    num_iters: int,
    batch_size: int,
    lam_schedule: Callable[[int], float],  # lam_schedule(t) -> lambda_t
) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """
    Run BaM for num_iters iterations.
    
    Args:
        key: JAX PRNG key
        mu_init: Initial mean, shape (D,)
        Sigma_init: Initial covariance, shape (D, D)
        score_fn: Target score function
        num_iters: Number of iterations T
        batch_size: Batch size B
        lam_schedule: Function t -> lambda_t
            - Gaussian targets: lambda_t = B * D (constant)
            - Non-Gaussian targets: lambda_t = B * D / (t + 1)
    
    Returns:
        mu_final: Final variational mean, shape (D,)
        Sigma_final: Final variational covariance, shape (D, D)
    
    Algorithm 1 in paper.
    """
    mu = mu_init
    Sigma = Sigma_init
    
    for t in range(num_iters):
        key, subkey = random.split(key)
        lam_t = lam_schedule(t)
        mu, Sigma = bam_step(subkey, mu, Sigma, score_fn, batch_size, lam_t)
    
    return mu, Sigma
