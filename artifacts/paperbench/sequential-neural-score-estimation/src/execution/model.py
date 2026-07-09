"""
Score network architectures for NPSE/TSNPSE.

Implements NCMLP (direct score) and NCMLP_ENERGY (energy-based score).
Both use independent MLP embeddings for θ_t and x, sinusoidal embedding for t,
concatenation, and a main MLP.

Paper Section: §5.1, Appendix E.3.2 (Eq. 138 for sinusoidal embedding).
Code reference: model.py, model_energy.py in repository.
"""
import jax
import jax.numpy as jnp
import jax.random as jr
from typing import Callable
import equinox as eqx


def get_timestep_embedding(sigma: float, embedding_dim: int = 64,
                           max_positions: int = 10000) -> jnp.ndarray:
    """
    Sinusoidal time embedding (Eq. 138, Appendix E.3.2).
    
    (t_emb)_i = sin(t / 10000^{(i-1)/31})   if i <= 32
    (t_emb)_i = cos(t / 10000^{(i-32-1)/31}) if i > 32
    
    Args:
        sigma: scalar (noise level, used as time proxy)
        embedding_dim: output dimension (64 by default)
        max_positions: 10000 (fixed)
    Returns:
        embedding: shape (embedding_dim,)
    """
    half_dim = embedding_dim // 2
    emb = jnp.log(max_positions) / (half_dim - 1)
    emb = jnp.exp(jnp.arange(half_dim, dtype=jnp.float32) * -emb)
    # sigma is used as the time input; shape () → (1,)
    emb = jnp.array([sigma], dtype=jnp.float32)[:, None] * emb
    emb = jnp.concatenate([jnp.sin(emb), jnp.cos(emb)], axis=1)
    return emb.squeeze()  # shape (embedding_dim,)


class NCMLP(eqx.Module):
    """
    Neural Conditional Score Network (direct score parameterisation).
    
    Architecture:
      θ_t → MLP_θ(d → theta_embed_dim, depth=3, width=256, SiLU) → θ_emb
      x   → MLP_x(p → x_embed_dim,     depth=3, width=256, SiLU) → x_emb
      σ   → sinusoidal_embedding(→ 64)                            → t_emb
      [θ_emb || x_emb || t_emb] → MLP_main(→ d, depth=3, width=256, SiLU) → score
    
    Output: s_ψ(θ_t, x, σ) ∈ R^d  (score vector)
    
    Note: In code, depth=2 means 2 hidden layers (3 total layers including output).
    """
    mlp_theta: eqx.nn.MLP
    mlp_x: eqx.nn.MLP
    mlp_main: eqx.nn.MLP
    t_embed_dim: int = 64

    def __init__(self, key: jnp.ndarray, dim_parameters: int, dim_data: int,
                 width: int = 256, depth: int = 2,
                 theta_embed_dim: int = None, x_embed_dim: int = None,
                 t_embed_dim: int = 64,
                 activation: Callable = jax.nn.silu):
        """
        Args:
            dim_parameters: d, input dimension for θ
            dim_data: p, input dimension for x
            width: hidden units per layer (256)
            depth: number of hidden layers per MLP (2 in code = 3 total layers)
            theta_embed_dim: output dim of θ embedding = max(30, 4*d)
            x_embed_dim: output dim of x embedding = max(30, 4*p)
            t_embed_dim: time embedding dimension (64)
        """
        if theta_embed_dim is None:
            theta_embed_dim = max(30, 4 * dim_parameters)
        if x_embed_dim is None:
            x_embed_dim = max(30, 4 * dim_data)
        
        key1, key2, key3 = jr.split(key, 3)
        self.t_embed_dim = t_embed_dim
        
        self.mlp_theta = eqx.nn.MLP(
            in_size=dim_parameters, out_size=theta_embed_dim,
            depth=depth, width_size=width, activation=activation, key=key1)
        self.mlp_x = eqx.nn.MLP(
            in_size=dim_data, out_size=x_embed_dim,
            depth=depth, width_size=width, activation=activation, key=key2)
        self.mlp_main = eqx.nn.MLP(
            in_size=theta_embed_dim + x_embed_dim + t_embed_dim,
            out_size=dim_parameters,
            depth=depth, width_size=width, activation=activation, key=key3)

    def __call__(self, theta_t: jnp.ndarray, x: jnp.ndarray, sigma: float) -> jnp.ndarray:
        """
        Forward pass: sψ(θ_t, x, σ).
        
        Args:
            theta_t: shape (d,), noisy (standardised) parameters
            x: shape (p,), (standardised) observation
            sigma: scalar noise level (used as time proxy)
        Returns:
            score: shape (d,)
        """
        t_emb = get_timestep_embedding(sigma, self.t_embed_dim)
        theta_emb = self.mlp_theta(theta_t)
        x_emb = self.mlp_x(x)
        out = jnp.concatenate([theta_emb, x_emb, t_emb])
        return self.mlp_main(out)


class NCMLP_ENERGY(eqx.Module):
    """
    Energy-based score network (preferred for TSNPSE).
    
    Same architecture as NCMLP but output is scalar energy E_ψ ∈ R.
    Score is obtained as: s_ψ(θ_t, x, σ) = -∇_{θ_t} E_ψ(θ_t, x, σ)
    
    Advantage: unnormalised log-probability p(θ|x_obs) ∝ exp(-E_ψ(θ, x_obs, σ(t_0)))
    requires only a single forward pass — no ODE solve needed for HPRε in TSNPSE.
    """
    mlp_theta: eqx.nn.MLP
    mlp_x: eqx.nn.MLP
    mlp_main: eqx.nn.MLP  # output dim = 1
    t_embed_dim: int = 64

    def energy(self, theta_t: jnp.ndarray, x: jnp.ndarray, sigma: float) -> float:
        """
        Computes scalar energy E_ψ(θ_t, x, σ).
        
        Args:
            theta_t: shape (d,), noisy (standardised) parameters
            x: shape (p,), (standardised) observation
            sigma: scalar noise level
        Returns:
            energy: scalar
        """
        t_emb = get_timestep_embedding(sigma, self.t_embed_dim)
        theta_emb = self.mlp_theta(theta_t)
        x_emb = self.mlp_x(x)
        out = jnp.concatenate([theta_emb, x_emb, t_emb])
        return self.mlp_main(out).squeeze()

    def __call__(self, theta_t: jnp.ndarray, x: jnp.ndarray, sigma: float) -> jnp.ndarray:
        """
        Compute score as negative gradient of energy: s_ψ = -∇_{θ_t} E_ψ.
        
        Args:
            theta_t: shape (d,), noisy (standardised) parameters
            x: shape (p,), (standardised) observation
            sigma: scalar noise level
        Returns:
            score: shape (d,)
        """
        energy_fn = lambda theta: self.energy(theta, x, sigma)
        return jax.grad(energy_fn)(theta_t)
