"""
Simformer Generalized Diffusion Guidance — Algorithm 1 from paper.
Enables conditioning on observation intervals and arbitrary constraint functions.

Reference: §3.4 and Appendix A3.3 of "All-in-one simulation-based inference"
           Bansal et al. (2023), Universal guidance for diffusion models
           Lugmayr et al. (2022), RePaint (self-recurrence strategy)
"""

import jax
import jax.numpy as jnp
from typing import Callable, Optional
from jaxtyping import Array, PRNGKey


# ─────────────────────────────────────────────────────────────────
# Scaling function s(t) for VESDE
# ─────────────────────────────────────────────────────────────────

def vesde_guidance_scaling(sigma_t: Array) -> Array:
    """
    Scaling function s(t) = 1 / σ(t)² for VESDE.

    This ensures s(t) → ∞ as t → 0, so the constraint is increasingly
    enforced as noise decreases toward the data distribution.

    Args:
        sigma_t: σ(t) for VESDE, shape (...,)
    Returns:
        s(t) = 1/σ(t)², same shape
    """
    return 1.0 / (sigma_t ** 2)


# ─────────────────────────────────────────────────────────────────
# Constraint functions
# ─────────────────────────────────────────────────────────────────

def upper_bound_constraint(x: Array, upper: float) -> Array:
    """c(x) = x - u; satisfied when x ≤ u (c(x) ≤ 0)."""
    return x - upper


def lower_bound_constraint(x: Array, lower: float) -> Array:
    """c(x) = lower - x; satisfied when x ≥ lower (c(x) ≤ 0)."""
    return lower - x


def interval_constraint(x: Array, lower: float, upper: float):
    """Returns both constraints for interval [lower, upper]."""
    return [lower_bound_constraint(x, lower), upper_bound_constraint(x, upper)]


# ─────────────────────────────────────────────────────────────────
# Constraint score modification
# ─────────────────────────────────────────────────────────────────

def constraint_score_modification(
    x_hat: Array,          # (B, d) current noisy state
    score: Array,          # (B, d) current score estimate
    sigma_t: Array,        # (B, 1) noise level
    mu_t: Array,           # (B, 1) mean (= 1 for VESDE)
    constraint_fns: list,  # list of constraint functions c_i(x) <= 0
) -> Array:
    """
    Compute the constrained score as:
      s̃(ˆx_t, t|c) ≈ s(ˆx_t, t) + Σ_i ∇_{ˆx_t} log σ(-s(t) * c_i(ˆx̃₀))

    where ˆx̃₀ = (ˆx_t + σ(t)² * s) / μ(t) is the denoised estimate,
    and s(t) = 1/σ(t)² is the guidance scaling function.

    From §3.4 and Appendix A3.3.

    Args:
        x_hat: (B, d) noisy sample at time t
        score: (B, d) current score estimate from model
        sigma_t: (B, 1) noise level σ(t)
        mu_t: (B, 1) mean factor μ(t) (= 1.0 for VESDE)
        constraint_fns: list of constraint functions c_i: Array → Array

    Returns:
        modified_score: (B, d) constrained score estimate
    """
    # Denoised estimate ˆx̃₀ = (ˆx_t + σ(t)² * s) / μ(t)
    x_hat_0_est = (x_hat + sigma_t ** 2 * score) / mu_t

    # Scaling s(t) = 1/σ(t)²
    scale = vesde_guidance_scaling(sigma_t)

    def constraint_log_grad(x_hat_in):
        def log_sigmoid_constraint(x):
            # Σ_i log σ(-s(t) * c_i(x̃₀))
            total = 0.0
            x0_est = (x + sigma_t ** 2 * score) / mu_t
            for c_fn in constraint_fns:
                c_val = c_fn(x0_est)
                total = total + jnp.sum(jax.nn.log_sigmoid(-scale * c_val))
            return total
        return jax.grad(log_sigmoid_constraint)(x_hat_in)

    # ∇_{ˆx_t} Σ_i log σ(-s(t) * c_i(ˆx̃₀))
    grad_constraint = constraint_log_grad(x_hat)

    return score + grad_constraint


# ─────────────────────────────────────────────────────────────────
# Algorithm 1: General Guidance Sampling
# ─────────────────────────────────────────────────────────────────

def guided_sde_sampler(
    params,
    key: PRNGKey,
    x_observed: Array,              # (d,) observed variable values
    condition_mask: Array,          # (d,) M_C binary (1=observed)
    node_ids: Array,                # (d,) variable integer IDs
    edge_mask: Array,               # (d, d) M_E attention mask
    score_net_fn: Callable,
    constraint_fns: list,           # list of constraint functions c_i(x) <= 0
    n_samples: int = 1000,
    n_steps: int = 500,             # default from backward_sde.yaml
    self_recurrence: int = 0,       # r; default=0, r=5 for high-accuracy (5× compute)
    sigma_max: float = 15.0,
    sigma_min: float = 0.0001,
    T_max: float = 1.0,
    T_min: float = 1e-5,
) -> Array:
    """
    Algorithm 1: General Guidance sampling with optional self-recurrence.

    Samples from p(x_unobserved | x_observed, c(x) <= 0) by modifying the
    score estimate during reverse SDE to enforce constraint functions.

    Self-recurrence (r > 0): after each reverse step, re-perturb the sample
    forward by one step and repeat, improving accuracy at r× computational cost.
    Based on Lugmayr et al. (2022) RePaint and Bansal et al. (2023).

    Args:
        params: model parameters
        key: PRNG key
        x_observed: (d,) values of observed/conditioned variables
        condition_mask: (d,) binary mask, 1=observed
        node_ids: (d,) integer variable IDs
        edge_mask: (d, d) transformer attention mask
        score_net_fn: score model function
        constraint_fns: list of constraint functions c_i(x) <= 0
        n_samples: number of samples
        n_steps: number of reverse SDE steps (500 default)
        self_recurrence: r number of self-recurrence steps (0 default; 5 for high accuracy)
        sigma_max, sigma_min, T_max, T_min: VESDE parameters
    Returns:
        samples: (n_samples, d)
    """
    d = x_observed.shape[0]
    cond_mask_2d = condition_mask[None, :]

    # Initialize at terminal noise distribution
    key, k_init = jax.random.split(key)
    x_hat = jax.random.normal(k_init, (n_samples, d)) * sigma_max
    x_hat = (1.0 - cond_mask_2d) * x_hat + cond_mask_2d * x_observed[None, :]

    timesteps = jnp.linspace(T_max, T_min, n_steps + 1)
    dt = (T_max - T_min) / n_steps

    for i in range(n_steps):
        t_i = timesteps[i]

        for j in range(self_recurrence + 1):
            key, k_noise, k_resamp = jax.random.split(key, 3)
            t_batch = jnp.full((n_samples, 1), t_i + dt)  # t_{i+1}

            # Tokenize
            tokens = _tokenize_stub(x_hat, node_ids, condition_mask)

            # Score estimate from model
            s = score_net_fn(params, t_batch, tokens, edge_mask)  # (n_samples, d)

            # Noise level σ(t_{i+1}) and mean μ(t_{i+1}) = 1 for VESDE
            sigma_t1 = sigma_min * (sigma_max / sigma_min) ** (t_i + dt)
            mu_t1 = jnp.ones((n_samples, 1))

            # Apply constraint-modified score
            s_tilde = constraint_score_modification(x_hat, s, sigma_t1, mu_t1, constraint_fns)

            # Euler-Maruyama step (VESDE: f=0, g(t) = diffusion coeff)
            log_ratio = jnp.log(sigma_max / sigma_min)
            g_t = sigma_min * (sigma_max / sigma_min) ** t_i * jnp.sqrt(2 * log_ratio)
            noise = jax.random.normal(k_noise, x_hat.shape)
            x_hat = x_hat - g_t ** 2 * s_tilde * (-dt) + g_t * jnp.sqrt(dt) * noise

            # Keep observed variables fixed
            x_hat = (1.0 - cond_mask_2d) * x_hat + cond_mask_2d * x_observed[None, :]

            # Self-recurrence: re-perturb sample forward (t_i → t_{i+1})
            if j < self_recurrence:
                noise_resamp = jax.random.normal(k_resamp, x_hat.shape)
                g_t_fwd = sigma_min * (sigma_max / sigma_min) ** t_i * jnp.sqrt(2 * log_ratio)
                x_hat = x_hat + g_t_fwd * jnp.sqrt(dt) * noise_resamp
                x_hat = (1.0 - cond_mask_2d) * x_hat + cond_mask_2d * x_observed[None, :]

    return x_hat


def _tokenize_stub(x_hat, node_ids, condition_mask):
    """Placeholder — actual tokenization uses haiku ScalarTokenizer."""
    return x_hat
