"""
ADVI Score and Fisher Variants — Baseline Implementations
Paper: "Batch and Match: BBVI with a Score-Based Divergence"

Two variants of ADVI using alternative loss functions:
  1. ADVI (Score): Uses score-based divergence D(q;p) instead of ELBO
  2. ADVI (Fisher): Uses Fisher divergence E_q[||∇log(q/p)||²_I] instead of ELBO

Both variants use the same Adam optimizer as standard ADVI.
Architecture: identical to ADVI — full-covariance Gaussian via Cholesky parameterization.

Key finding from paper:
  - Score variant more sensitive to learning rate; can diverge for highly skewed targets (s=1.8)
  - Fisher variant performs similarly to standard ADVI
  - Neither variant benefits from the closed-form structure exploited by BaM
"""

import numpy as np
import jax
import jax.numpy as jnp
from jax import jit, grad
import optax
from numpyro.distributions import MultivariateNormal
from typing import Callable, Optional


class ADVIScore:
    """
    ADVI with score-based divergence loss instead of ELBO.
    
    Loss: D(q; p) ≈ (1/B) Σ_b ||∇log q(z_b) - ∇log p(z_b)||²_{Σ}
    
    Learning rates used in paper (Gaussian targets, B=2):
      D=4:   lr=0.01
      D=16:  lr=0.005
      D=64:  lr=0.001
      D=256: lr=0.001
    For non-Gaussian targets: per-configuration grid search (can diverge at s=1.8).
    """
    def __init__(self, D: int, lp: Callable, lp_g: Callable):
        """
        Args:
            D:    Dimension
            lp:   Log-probability function (for monitoring)
            lp_g: Score function: lp_g(x: (N,D)) -> (N,D)
        """
        self.D = D
        self.lp = lp
        self.lp_g = lp_g
        self.idx_tril = jnp.stack(jnp.tril_indices(D)).T

    def scales_to_cov(self, scales: jnp.ndarray) -> np.ndarray:
        """Convert Cholesky vector to full covariance."""
        L = jnp.zeros((self.D, self.D))
        L = L.at[self.idx_tril[:, 0], self.idx_tril[:, 1]].set(scales)
        return np.array(L @ L.T)

    def score_divergence_loss(
        self,
        params: tuple,
        key,
        batch_size: int,
    ) -> jnp.ndarray:
        """
        Empirical score-based divergence loss.
        D̂(q;p) = (1/B) Σ_b ||∇log q(z_b) - ∇log p(z_b)||²_{Σ}
        """
        loc, scales = params
        L = jnp.zeros((self.D, self.D))
        L = L.at[self.idx_tril[:, 0], self.idx_tril[:, 1]].set(scales)
        q = MultivariateNormal(loc=loc, scale_tril=L)
        cov = L @ L.T

        samples = q.sample(key, (batch_size,))  # (B, D)
        # Score of q: ∇log N(z; μ, Σ) = -Σ^{-1}(z-μ)
        score_q = -(samples - loc) @ jnp.linalg.inv(cov).T
        # Score of p (via provided function)
        score_p = self.lp_g(samples)
        # Covariance-weighted squared difference: ||s_q - s_p||²_Σ per sample
        diff = score_q - score_p
        loss = jnp.mean(jax.vmap(lambda d: d @ cov @ d)(diff))
        return loss

    def fit(
        self,
        key,
        opt,
        mean: Optional[np.ndarray] = None,
        cov: Optional[np.ndarray] = None,
        batch_size: int = 2,
        niter: int = 10000,
        nprint: int = 10,
        monitor=None,
    ):
        """Fit using score-based divergence loss with Adam optimizer."""
        if mean is None:
            mean = jnp.zeros(self.D)
        if cov is None:
            cov = np.identity(self.D)

        L = np.linalg.cholesky(cov)
        scales = jnp.array(L[np.tril_indices(self.D)])
        params = (jnp.array(mean), scales)
        lossf = jit(self.score_divergence_loss, static_argnums=(2,))

        @jit
        def opt_step(params, opt_state, key):
            loss, grads = jax.value_and_grad(lossf)(params, key, batch_size)
            updates, opt_state = opt.update(grads, opt_state, params)
            params = optax.apply_updates(params, updates)
            return params, opt_state, loss

        opt_state = opt.init(params)
        losses = []
        nevals = 1

        for i in range(niter + 1):
            if i % (niter // nprint) == 0:
                print(f"Iteration {i} of {niter}")
            if monitor is not None and i % monitor.checkpoint == 0:
                mu = params[0]
                cv = self.scales_to_cov(params[1] * 1.0)
                monitor(i, [mu, cv], self.lp, key, nevals=nevals)
                nevals = 0

            params, opt_state, loss = opt_step(params, opt_state, key)
            key, _ = jax.random.split(key)
            losses.append(float(loss))
            nevals += batch_size

        mean_fit = params[0]
        cov_fit = self.scales_to_cov(params[1] * 1.0)
        if monitor is not None:
            monitor(niter, [mean_fit, cov_fit], self.lp, key, nevals=nevals)
        return mean_fit, cov_fit, losses


class ADVIFisher:
    """
    ADVI with Fisher divergence loss instead of ELBO.
    
    Loss: E_q[||∇log q(z) - ∇log p(z)||²_I]  (unweighted, NOT affine invariant)
    
    Learning rates used in paper (all dimensions, B=2):
      Gaussian targets:     lr=0.01
      Non-Gaussian targets: lr=0.05
    
    Key finding: performs similarly to standard ADVI.
    Fisher divergence is not affine invariant (unlike BaM's score-based divergence).
    """
    def __init__(self, D: int, lp: Callable, lp_g: Callable):
        self.D = D
        self.lp = lp
        self.lp_g = lp_g
        self.idx_tril = jnp.stack(jnp.tril_indices(D)).T

    def scales_to_cov(self, scales: jnp.ndarray) -> np.ndarray:
        L = jnp.zeros((self.D, self.D))
        L = L.at[self.idx_tril[:, 0], self.idx_tril[:, 1]].set(scales)
        return np.array(L @ L.T)

    def fisher_divergence_loss(
        self,
        params: tuple,
        key,
        batch_size: int,
    ) -> jnp.ndarray:
        """
        Empirical Fisher divergence: (1/B) Σ_b ||∇log q(z_b) - ∇log p(z_b)||²_I
        Identity-weighted (NOT affine invariant).
        """
        loc, scales = params
        L = jnp.zeros((self.D, self.D))
        L = L.at[self.idx_tril[:, 0], self.idx_tril[:, 1]].set(scales)
        q = MultivariateNormal(loc=loc, scale_tril=L)
        cov = L @ L.T

        samples = q.sample(key, (batch_size,))
        score_q = -(samples - loc) @ jnp.linalg.inv(cov).T
        score_p = self.lp_g(samples)
        diff = score_q - score_p
        # Unweighted L2 norm (Fisher divergence, not score-based divergence)
        loss = jnp.mean(jnp.sum(diff ** 2, axis=-1))
        return loss

    def fit(
        self,
        key,
        opt,
        mean: Optional[np.ndarray] = None,
        cov: Optional[np.ndarray] = None,
        batch_size: int = 2,
        niter: int = 10000,
        nprint: int = 10,
        monitor=None,
    ):
        """Fit using Fisher divergence loss with Adam optimizer."""
        if mean is None:
            mean = jnp.zeros(self.D)
        if cov is None:
            cov = np.identity(self.D)

        L = np.linalg.cholesky(cov)
        scales = jnp.array(L[np.tril_indices(self.D)])
        params = (jnp.array(mean), scales)
        lossf = jit(self.fisher_divergence_loss, static_argnums=(2,))

        @jit
        def opt_step(params, opt_state, key):
            loss, grads = jax.value_and_grad(lossf)(params, key, batch_size)
            updates, opt_state = opt.update(grads, opt_state, params)
            params = optax.apply_updates(params, updates)
            return params, opt_state, loss

        opt_state = opt.init(params)
        losses = []
        nevals = 1

        for i in range(niter + 1):
            if i % (niter // nprint) == 0:
                print(f"Iteration {i} of {niter}")
            if monitor is not None and i % monitor.checkpoint == 0:
                mu = params[0]
                cv = self.scales_to_cov(params[1] * 1.0)
                monitor(i, [mu, cv], self.lp, key, nevals=nevals)
                nevals = 0

            params, opt_state, loss = opt_step(params, opt_state, key)
            key, _ = jax.random.split(key)
            losses.append(float(loss))
            nevals += batch_size

        mean_fit = params[0]
        cov_fit = self.scales_to_cov(params[1] * 1.0)
        if monitor is not None:
            monitor(niter, [mean_fit, cov_fit], self.lp, key, nevals=nevals)
        return mean_fit, cov_fit, losses
