"""
General Guidance (Algorithm 1) for the Simformer.

Enables conditioning on interval constraints of the form c(x_hat) <= 0.
Modified score: s_tilde(x_t, t) = s_phi(x_t, t) + grad_{x_t} log sigma(-s(t) * c(x_hat_0_tilde))

Where:
  - x_hat_0_tilde = (x_t + sigma(t)^2 * score) / mu(t) is the denoised estimate
  - s(t) = 1 / sigma(t)^2 (inversely proportional to variance, for VESDE)
  - c(x_hat) <= 0 is the constraint function
  - sigma is the sigmoid function (not noise std)

Self-recurrence (r steps): after each reverse step, re-noise and re-run r times.

Reference: Gloeckler et al., 2024, Algorithm 1; Bansal et al., 2023
"""

import math
import numpy as np
from typing import Callable, Optional


def sigmoid(x: np.ndarray) -> np.ndarray:
    """Numerically stable sigmoid."""
    return np.where(x >= 0, 1 / (1 + np.exp(-x)), np.exp(x) / (1 + np.exp(x)))


def constraint_upper_bound(x: np.ndarray, u: float) -> np.ndarray:
    """Upper bound constraint: c(x) = x - u <= 0."""
    return x - u


def constraint_lower_bound(x: np.ndarray, l: float) -> np.ndarray:
    """Lower bound constraint: c(x) = l - x <= 0."""
    return l - x


def constraint_interval(x: np.ndarray, lower: float, upper: float) -> np.ndarray:
    """
    Interval constraint [lower, upper]:
    c_1(x) = x - upper <= 0  (upper bound)
    c_2(x) = lower - x <= 0  (lower bound)
    Returns stack of both constraint values.
    """
    return np.stack([x - upper, lower - x], axis=-1)


def guided_sample_vesde(
    score_fn: Callable,              # score_fn(x, t, M_E) -> (B, d) scores
    tokenizer,                       # SBITokenizer instance
    x_obs: np.ndarray,               # (d,) observed values
    condition_mask: np.ndarray,      # (d,) binary: 1=observed, 0=to-sample
    var_ids: np.ndarray,             # (d,)
    attention_mask: np.ndarray,      # (d, d)
    constraint_fns: list,            # list of callables: c_i(x) -> scalar/array, each c_i(x) <= 0
    sigma_min: float = 0.0001,
    sigma_max: float = 15.0,
    t_min: float = 1e-5,
    t_max: float = 1.0,
    n_steps: int = 500,
    n_samples: int = 1,
    r: int = 0,                      # self-recurrence steps (0 = no recurrence)
    metadata: Optional[np.ndarray] = None,
) -> np.ndarray:
    """
    General guided diffusion sampling (Algorithm 1, VESDE).

    For each constraint c_i(x) <= 0:
      guidance_score += grad_{x_t} log sigma(-s(t) * c_i(x_hat_0_tilde))
    where x_hat_0_tilde = (x_t + sigma(t)^2 * s_phi) / 1  (mu=1 for VESDE)
    and s(t) = 1 / sigma(t)^2

    Self-recurrence (r > 0):
      After each reverse step, re-noise x_t back to x_{t+1} and re-run the step.
      Increases computation by factor (r+1) but improves accuracy.

    Args:
        score_fn:        Pre-trained Simformer score function
        constraint_fns:  List of constraint functions c_i; c_i(x) <= 0 means satisfied
        r:               Number of self-recurrence steps (0 = standard, 5 = improved)

    Returns:
        samples: (n_samples, d)
    """
    d = len(x_obs)
    B = n_samples
    log_ratio = math.log(sigma_max / sigma_min)

    # VESDE helper functions
    def sigma_t(t: float) -> float:
        return sigma_min * (sigma_max / sigma_min) ** t

    def g_t(t: float) -> float:
        return sigma_t(t) * math.sqrt(2 * log_ratio)

    # Initialize from terminal noise
    sigma_T = sigma_t(t_max)
    x = np.random.randn(B, d) * sigma_T
    x[:, condition_mask == 1] = x_obs[condition_mask == 1]
    M_C = np.broadcast_to(condition_mask[None, :], (B, d)).copy()

    t_schedule = np.linspace(t_max, t_min, n_steps + 1)
    dt = (t_min - t_max) / n_steps   # negative

    for i in range(n_steps):
        t_curr = t_schedule[i]
        t_next = t_schedule[i + 1]

        for j in range(r + 1):
            eps = np.random.randn(B, d)

            # Score from trained model
            t_batch = np.full((B,), t_curr)
            tokens = tokenizer.tokenize(x, var_ids, M_C, metadata)
            s = score_fn(tokens, t_batch, attention_mask)    # (B, d)

            # Denoised estimate x_hat_0_tilde (VESDE: mu(t)=1)
            sig_sq = sigma_t(t_curr) ** 2
            x0_tilde = x + sig_sq * s   # (B, d)  [= x_t + sigma^2 * score for VESDE]

            # Constraint-guided score modification
            # s(t) = 1/sigma(t)^2 (scaling function inversely proportional to variance)
            s_t_scale = 1.0 / sig_sq
            guide_score = np.zeros_like(x)

            for c_fn in constraint_fns:
                c_val = c_fn(x0_tilde)   # (B, d) or (B,) depending on constraint
                # grad_{x_t} log sigma(-s_t * c(x_0_tilde))
                # = -s_t * sigmoid(s_t * c(x_0_tilde)) * grad_{x_t} c(x_0_tilde)
                # Approximate: grad_{x_t} c(x_0_tilde) ≈ I (for linear constraints)
                sig_c = sigmoid(s_t_scale * c_val)
                guide_score += -s_t_scale * sig_c

            # Total score
            s_total = s + guide_score    # (B, d)

            # Euler-Maruyama reverse step (VESDE: f=0)
            g = g_t(t_curr)
            dx = g**2 * s_total * abs(dt) + g * math.sqrt(abs(dt)) * eps
            x_new = x + dx * (1 - M_C)
            x_new[:, condition_mask == 1] = x_obs[condition_mask == 1]

            x = x_new

            # Self-recurrence: re-noise for next inner iteration
            if j < r:
                eps2 = np.random.randn(B, d)
                # Forward SDE step: x_{t+1} = x_t + g(t)*sqrt(|dt|)*eps (f=0)
                x_renoised = x + g * math.sqrt(abs(dt)) * eps2
                x_renoised[:, condition_mask == 1] = x_obs[condition_mask == 1]
                x = x_renoised

    return x
