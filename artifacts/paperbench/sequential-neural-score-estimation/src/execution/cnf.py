"""
Continuous Normalising Flow (CNF) module for NPSE/TSNPSE.

Wraps a trained score network + SDE to provide:
  - batch_sample_fn: posterior samples via backward ODE integration
  - batch_logp_fn: log-probabilities via instantaneous change-of-variables ODE
  - batch_unn_logp_fn: unnormalised log-probs via single energy forward pass

Sampling uses the probability flow ODE (Eq. 4):
  dθ_t/dt = f(θ_t, t) - ½g²(t) s_ψ(θ_t, x, σ(t))
integrated backward from T to 0 using Tsit5 ODE solver.

Log-probability uses the instantaneous change-of-variables (Eq. 5):
  d log p / dt = -Tr(∂v/∂θ)

Paper Section: §2.2, Appendix E.3.3.
Code reference: cnf.py in repository.
"""
import jax
import jax.numpy as jnp
import jax.random as jr
import equinox as eqx
import functools as ft
from typing import Tuple

try:
    import diffrax as dfx
    HAS_DIFFRAX = True
except ImportError:
    HAS_DIFFRAX = False


class CNF(eqx.Module):
    """
    Continuous Normalising Flow for posterior inference.
    
    Stores the trained score network, SDE, and standardisation parameters.
    All inputs are standardised before passing to the network; outputs are
    un-standardised before returning.
    
    Key constants (from cnf.py):
        t1 = T = 1.0    (start of backward ODE / end of forward)
        t0 = 1e-5       (end of backward ODE / start of forward; avoids singularity)
        dt = 0.01       (initial ODE step size)
    """
    score_network: eqx.Module
    sde: object
    parameter_mean: jnp.ndarray   # shape (d,)
    parameter_std: jnp.ndarray    # shape (d,)
    data_mean: jnp.ndarray        # shape (p,)
    data_std: jnp.ndarray         # shape (p,)
    t1: float = 1.0
    t0: float = 1e-5
    dt: float = 0.01

    def batch_sample_fn(self, sample_size: int, x: jnp.ndarray,
                        key: jnp.ndarray) -> jnp.ndarray:
        """
        Generate posterior samples via backward probability flow ODE.
        
        Steps:
          1. Standardise x
          2. Sample θ_T ~ base_dist (Gaussian)
          3. Integrate ODE from t=T to t=t0 backward
          4. Un-standardise θ_0
        
        Args:
            sample_size: number of samples
            x: shape (p,), observed data (raw, un-standardised)
            key: JAX PRNGKey
        Returns:
            samples: shape (sample_size, d), un-standardised posterior samples
        """
        x_norm = (x - self.data_mean) / self.data_std
        sample_keys = jr.split(key, sample_size)
        sample_fn = ft.partial(self._single_sample_fn, x_norm)
        # vmap over sample_keys
        samples_norm = jax.vmap(sample_fn)(sample_keys)
        # Un-standardise
        return self.parameter_mean + self.parameter_std * samples_norm

    def _single_sample_fn(self, x_norm: jnp.ndarray, key: jnp.ndarray) -> jnp.ndarray:
        """
        Single sample via backward ODE integration (Tsit5 solver).
        
        Integrates from t1=T → t0=1e-5 with initial condition θ_T ~ N(0, σ_max^2 I).
        """
        if not HAS_DIFFRAX:
            raise ImportError("diffrax required for ODE integration")
        key, base_key = jr.split(key)
        # Initial condition: sample from base distribution
        theta_T = self.sde.base_dist_sample(base_key)  # shape (d,)
        # Backward ODE: integrate from T to t0
        drift = ft.partial(self.sde.drift_ode, self.score_network, x_norm)
        term = dfx.ODETerm(drift)
        solver = dfx.Tsit5()
        sol = dfx.diffeqsolve(term, solver, self.t1, self.t0, -self.dt, theta_T)
        return sol.ys[0]

    def batch_logp_fn(self, theta: jnp.ndarray, x: jnp.ndarray,
                      key: jnp.ndarray) -> jnp.ndarray:
        """
        Compute log-probabilities via instantaneous change-of-variables ODE (Eq. 5).
        
        Requires solving augmented ODE: (θ_t, Δlog p_t) from t0→t1
        with log p(θ) = Δlog p + base_dist_logp(θ_T)
        
        Args:
            theta: shape (N, d), parameter samples (raw)
            x: shape (p,), observation (raw)
            key: JAX PRNGKey
        Returns:
            log_probs: shape (N,)
        """
        x_norm = (x - self.data_mean) / self.data_std
        theta_norm = (theta - self.parameter_mean) / self.parameter_std
        logp_keys = jr.split(key, theta.shape[0])
        logp_fn = ft.partial(self._single_logp_fn, x_norm)
        return jax.vmap(logp_fn)(theta_norm, logp_keys)

    def _single_logp_fn(self, x_norm: jnp.ndarray, theta_norm: jnp.ndarray,
                        key: jnp.ndarray) -> float:
        """
        Single log-probability via augmented ODE (Tsit5 solver).
        
        Augmented state: (θ_t, Δlog p) where Δlog p accumulates divergence.
        Integrates from t0 → t1 (forward in time for log-p).
        Final: log p(θ) = Δlog p + log p_base(θ_T)
        """
        if not HAS_DIFFRAX:
            raise ImportError("diffrax required for ODE integration")
        drift_logp = ft.partial(self.sde.drift_dlogp_ode, self.score_network, x_norm)
        term = dfx.ODETerm(drift_logp)
        solver = dfx.Tsit5()
        init_state = (theta_norm, 0.0)
        sol = dfx.diffeqsolve(term, solver, self.t0, self.t1, self.dt, init_state)
        (theta_T,), (delta_logp,) = sol.ys
        return delta_logp + self.sde.base_dist_logp(theta_T)

    def batch_unn_logp_fn(self, theta: jnp.ndarray, x: jnp.ndarray,
                          key: jnp.ndarray) -> jnp.ndarray:
        """
        Compute UNNORMALISED log-probabilities using energy model (single forward pass).
        
        Only available when score_network is NCMLP_ENERGY.
        Returns -E_ψ(θ_norm, x_norm, σ(t0)) for each sample.
        
        Used in TSNPSE for HPRε estimation (much cheaper than full ODE).
        
        Args:
            theta: shape (N, d), parameter samples (raw)
            x: shape (p,), observation (raw)
        Returns:
            unn_log_probs: shape (N,) — unnormalised, suitable for quantile thresholding
        """
        x_norm = (x - self.data_mean) / self.data_std
        theta_norm = (theta - self.parameter_mean) / self.parameter_std
        logp_keys = jr.split(key, theta.shape[0])
        logp_fn = ft.partial(self._single_unn_logp_fn, x_norm)
        return jax.vmap(logp_fn)(theta_norm, logp_keys)

    def _single_unn_logp_fn(self, x_norm: jnp.ndarray, theta_norm: jnp.ndarray,
                             key: jnp.ndarray) -> float:
        """
        Single unnormalised log-prob: -E_ψ(θ, x, σ(t0)).
        Single forward pass; no ODE solve required.
        """
        _, sigma = self.sde.marginal_prob(theta_norm, jnp.array(self.t0))
        # energy() method of NCMLP_ENERGY
        return self.score_network.energy(theta_norm, x_norm, sigma)
