"""
Training loop for NPSE/TSNPSE score networks.

Implements the denoising score matching (DSM) objective (Eq. 7 of paper):
  J_DSM(ψ) = ∫₀ᵀ λ_t E[‖s_ψ(θ_t, x, σ) + noise/std‖²] dt

Key features:
- Adam optimizer with lr=1e-4
- Early stopping with patience=1000 steps
- Max 3000 iterations
- 85%/15% train/val split (re-computed each sequential round)
- Data standardisation: (θ, x) → (θ - μ) / σ

Paper Section: §5.1, Appendix E.3.2.
Code reference: training.py in repository.
"""
import jax
import jax.numpy as jnp
import jax.random as jr
import equinox as eqx
import optax
import math
from copy import deepcopy
from typing import Tuple


def dsm_loss_single(model, sde, weight_fn, theta_0: jnp.ndarray, x: jnp.ndarray,
                    t: float, key: jnp.ndarray) -> float:
    """
    Compute DSM loss for a single (θ_0, x, t) triple.
    
    loss = weight(t) * ‖s_ψ(θ_t, x, std) + noise/std‖²
    
    where θ_t = mean(θ_0, t) + std * noise, noise ~ N(0, I)
    and weight(t) = std² (signal-to-noise weighting, use_weighted_loss=True)
    
    Args:
        model: score network (NCMLP or NCMLP_ENERGY)
        sde: VESDE or VPSDE instance
        weight_fn: function t → scalar weight λ_t
        theta_0: shape (d,), clean parameters (standardised)
        x: shape (p,), observation (standardised)
        t: scalar time ~ U(0.0001, T)
        key: JAX PRNGKey
    Returns:
        scalar loss
    """
    mean, std = sde.marginal_prob(theta_0, t)
    noise = jr.normal(key, theta_0.shape)
    theta_t = mean + std * noise
    # score prediction
    pred = model(theta_t, x, std)
    # target: -noise/std = ∇_{θ_t} log p_{t|0}(θ_t|θ_0)
    return weight_fn(t) * jnp.mean((pred + noise / std) ** 2)


def dsm_loss_batch(model, sde, weight_fn, theta_batch: jnp.ndarray,
                   x_batch: jnp.ndarray, key: jnp.ndarray) -> float:
    """
    Batch DSM loss: average over batch, sample t ~ U(0.0001, T) per element.
    
    Args:
        theta_batch: shape (B, d), batch of clean parameters
        x_batch: shape (B, p), batch of observations
    Returns:
        scalar mean loss
    """
    batch_size = theta_batch.shape[0]
    tkey, losskey = jr.split(key)
    loss_keys = jr.split(losskey, batch_size)
    # Sample t uniformly for each element
    t = jr.uniform(tkey, (batch_size,), minval=0.0001, maxval=sde.T)
    loss_fn = jax.vmap(lambda th, x_, t_, k_: dsm_loss_single(model, sde, weight_fn, th, x_, t_, k_))
    return jnp.mean(loss_fn(theta_batch, x_batch, t, loss_keys))


def train_score_network(
    model,
    sde,
    theta_ds: jnp.ndarray,  # shape (N, d), raw parameters
    data_ds: jnp.ndarray,   # shape (N, p), raw observations
    key: jnp.ndarray,
    lr: float = 1e-4,
    max_iters: int = 3000,
    max_patience: int = 1000,
    batch_size: int = 50,
    eval_prop: float = 0.15,
    use_weighted_loss: bool = True,
    t_sample_size: int = 10,
) -> Tuple:
    """
    Full training loop for the score network.
    
    Steps:
    1. Concatenate θ and x, compute empirical mean/std, standardise
    2. 85%/15% train/val split (shuffled)
    3. Adam optimiser with early stopping
    4. Return best model (lowest validation loss) and normalisation stats
    
    Args:
        theta_ds: shape (N, d), raw parameter samples
        data_ds: shape (N, p), raw observation samples
        eval_prop: fraction held out for validation (0.15 = 15%)
        max_patience: number of steps without val loss improvement before stopping
        t_sample_size: number of t samples per data point per iteration
    Returns:
        (best_model, ds_mean, ds_std): best model + normalisation stats
    """
    # Standardise data
    ds = jnp.concatenate([theta_ds, data_ds], axis=1)
    ds_mean = ds.mean(axis=0)
    ds_std = ds.std(axis=0)
    ds_norm = (ds - ds_mean) / ds_std

    # Train/val split
    data_split_key, train_key = jr.split(key)
    indices = jr.permutation(data_split_key, jnp.arange(ds_norm.shape[0]))
    split_index = int(ds_norm.shape[0] * eval_prop)
    eval_ds = ds_norm[indices[:split_index]]
    train_ds = ds_norm[indices[split_index:]]
    dim_parameters = theta_ds.shape[1]

    # Weight function: λ_t = std²(t) for weighted loss
    if use_weighted_loss:
        def weight_fn(t):
            _, std = sde.marginal_prob(jnp.zeros(dim_parameters), t)
            return std ** 2
    else:
        def weight_fn(t): return jnp.ones_like(t)

    # Optimiser
    opt = optax.adam(lr)
    opt_state = opt.init(eqx.filter(model, eqx.is_inexact_array))

    best_model = deepcopy(model)
    best_loss = float("inf")
    patience = 0

    for step in range(max_iters):
        # Training step (multiple t samples per data point)
        for _ in range(t_sample_size):
            for batch in dataloader(train_ds, batch_size, key=train_key):
                split_idx = [dim_parameters]
                theta_b = batch[:, :dim_parameters]
                x_b = batch[:, dim_parameters:]
                loss, grads = eqx.filter_value_and_grad(dsm_loss_batch)(
                    model, sde, weight_fn, theta_b, x_b, train_key)
                updates, opt_state = opt.update(grads, opt_state)
                model = eqx.apply_updates(model, updates)
                train_key = jr.split(train_key, 1)[0]

        # Validation
        val_losses = []
        for batch in dataloader(eval_ds, batch_size, key=train_key):
            theta_b = batch[:, :dim_parameters]
            x_b = batch[:, dim_parameters:]
            val_loss = dsm_loss_batch(model, sde, weight_fn, theta_b, x_b, train_key)
            val_losses.append(val_loss.item())
        eval_loss_avg = sum(val_losses) / len(val_losses)

        # Early stopping
        if eval_loss_avg < best_loss:
            best_model = deepcopy(model)
            best_loss = eval_loss_avg
            patience = 0
        else:
            patience += 1
            if patience > max_patience:
                break

    return best_model, ds_mean, ds_std


def dataloader(data: jnp.ndarray, batch_size: int, *, key: jnp.ndarray):
    """Yield shuffled mini-batches from data."""
    dataset_size = data.shape[0]
    perm = jr.permutation(key, jnp.arange(dataset_size))
    start = 0
    while start < dataset_size:
        end = min(start + batch_size, dataset_size)
        yield data[perm[start:end]]
        start = end
