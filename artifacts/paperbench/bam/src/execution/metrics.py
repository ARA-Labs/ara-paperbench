"""
Evaluation metrics for BaM experiments.
Implements forward/reverse KL divergence, relative mean error, relative SD error, and MSE.

Reference: paper §5, Appendix E.5; gsmvi/monitors.py
"""
import numpy as np
from typing import Callable, Optional


def reverse_kl(
    q_samples: np.ndarray,          # (N, D) — samples from variational q
    log_q: Callable[[np.ndarray], np.ndarray],  # log q(z) function
    log_p: Callable[[np.ndarray], np.ndarray],  # log p̃(z) function (unnorm OK)
) -> float:
    """
    Empirical estimate of reverse KL divergence KL(q; p).

    KL(q; p) = E_q[log q(z) - log p(z)] ≈ (1/N) Σ [log q(z_b) - log p(z_b)]

    Note: log p̃ can be used since normalization constant cancels in relative comparisons.

    Args:
        q_samples: N samples from current variational approximation q
        log_q: Log density of q
        log_p: Log density of target p (or unnormalized log p̃)

    Returns:
        Estimate of KL(q; p) (scalar)
    """
    log_q_vals = log_q(q_samples)    # (N,)
    log_p_vals = log_p(q_samples)    # (N,)
    return float(np.mean(log_q_vals - log_p_vals))


def forward_kl(
    p_samples: np.ndarray,           # (N, D) — reference samples from target p
    log_q: Callable[[np.ndarray], np.ndarray],  # log q(z) function
    log_p: Callable[[np.ndarray], np.ndarray],  # log p̃(z) function
) -> float:
    """
    Empirical estimate of forward KL divergence KL(p; q).

    KL(p; q) = E_p[log p(z) - log q(z)] ≈ (1/N) Σ [log p(z_b) - log q(z_b)]

    Requires reference samples from target p (e.g., HMC samples or analytical samples).

    Args:
        p_samples: N samples from target p (reference)
        log_q: Log density of variational approximation q
        log_p: Log density of target p

    Returns:
        Estimate of KL(p; q) (scalar)
    """
    log_p_vals = log_p(p_samples)    # (N,)
    log_q_vals = log_q(p_samples)    # (N,)
    return float(np.mean(log_p_vals - log_q_vals))


def relative_mean_error(
    mu_vi: np.ndarray,    # (D,) — VI posterior mean estimate
    mu_hmc: np.ndarray,   # (D,) — HMC reference posterior mean
) -> float:
    """
    Relative mean error for posteriordb evaluation (eq. 242).

    relative_mean_error = ||μ - μ̂|| / ||μ||

    where μ is from HMC and μ̂ is from VI.

    Args:
        mu_vi: Variational inference posterior mean estimate
        mu_hmc: Reference HMC posterior mean

    Returns:
        Relative mean error (scalar)
    """
    return float(np.linalg.norm(mu_hmc - mu_vi) / np.linalg.norm(mu_hmc))


def relative_sd_error(
    sigma_vi: np.ndarray,   # (D,) — VI posterior standard deviation estimate
    sigma_hmc: np.ndarray,  # (D,) — HMC reference posterior standard deviation
) -> float:
    """
    Relative standard deviation error for posteriordb evaluation (eq. 242).

    relative_sd_error = ||σ - σ̂|| / ||σ||

    where σ is from HMC and σ̂ is from VI.

    Args:
        sigma_vi: Variational inference marginal standard deviation estimates
        sigma_hmc: Reference HMC marginal standard deviations

    Returns:
        Relative SD error (scalar)
    """
    return float(np.linalg.norm(sigma_hmc - sigma_vi) / np.linalg.norm(sigma_hmc))


def reconstruction_mse(
    reconstructed: np.ndarray,  # (H, W, C) or flat — decoded image
    original: np.ndarray,       # (H, W, C) or flat — original image
) -> float:
    """
    Mean Squared Error between reconstructed and original image.

    MSE = ||Ω(E[z'|x'], θ̂) - x'||² / dim

    Used in deep generative model experiment (Section 5.3, Figure 5.4).

    Args:
        reconstructed: Decoded image from posterior mean E[z'|x'] fed into decoder Ω
        original: Original test image x'

    Returns:
        MSE (scalar)
    """
    diff = reconstructed.flatten() - original.flatten()
    return float(np.mean(diff ** 2))


def gaussian_kl_exact(
    mu_q: np.ndarray,      # (D,) — mean of q
    Sigma_q: np.ndarray,   # (D, D) — covariance of q
    mu_p: np.ndarray,      # (D,) — mean of p
    Sigma_p: np.ndarray,   # (D, D) — covariance of p
) -> Tuple[float, float]:
    """
    Exact forward and reverse KL divergences between two Gaussians.
    Used when target is a known Gaussian distribution.

    KL(p; q) = 0.5 [tr(Σ_q^{-1} Σ_p) + (μ_q-μ_p)⊤ Σ_q^{-1}(μ_q-μ_p) - D + log|Σ_q|/|Σ_p|]
    KL(q; p) = 0.5 [tr(Σ_p^{-1} Σ_q) + (μ_p-μ_q)⊤ Σ_p^{-1}(μ_p-μ_q) - D + log|Σ_p|/|Σ_q|]

    Args:
        mu_q, Sigma_q: Parameters of variational distribution q
        mu_p, Sigma_p: Parameters of target distribution p

    Returns:
        (forward_kl, reverse_kl): Exact KL values
    """
    D = len(mu_q)
    
    Sigma_p_inv = np.linalg.inv(Sigma_p)
    Sigma_q_inv = np.linalg.inv(Sigma_q)
    
    sign_p, logdet_p = np.linalg.slogdet(Sigma_p)
    sign_q, logdet_q = np.linalg.slogdet(Sigma_q)
    
    diff_pq = mu_p - mu_q
    
    # KL(p; q) - forward KL
    fkl = 0.5 * (
        np.trace(Sigma_q_inv @ Sigma_p)
        + diff_pq @ Sigma_q_inv @ diff_pq
        - D
        + logdet_q - logdet_p
    )
    
    # KL(q; p) - reverse KL  
    rkl = 0.5 * (
        np.trace(Sigma_p_inv @ Sigma_q)
        + diff_pq @ Sigma_p_inv @ diff_pq
        - D
        + logdet_p - logdet_q
    )
    
    return float(fkl), float(rkl)
