"""
FRE Network: Transformer-based encoder-decoder + IQL policy.

Implements the core FRE algorithm from Frans et al. (2024).
Key components:
  - FRENetwork: encoder, decoder, actor, critic, value (Flax nn.Module)
  - FREAgent: training logic (Phase 1: encoder-decoder; Phase 2: IQL)
  - create_learner: initialize networks from a sample batch

Implementation framework: JAX/Flax

Architecture (Appendix A, Table 3):
  Encoder: 4-layer transformer, 256 hidden dim, 4 attention heads
  Decoder: MLP [512, 512, 512]
  Actor/Critic/Value: MLP [512, 512, 512]
  Latent dim: 128
  Reward discretization: 32 bins
"""

import jax
import jax.numpy as jnp
import numpy as np
import flax.linen as nn
import optax
from typing import Sequence, Dict, Any, Optional, Tuple, Callable
from functools import partial
import flax.struct as struct
from flax.training import train_state


# ========== Building Blocks ==========

class MLP(nn.Module):
    """3-hidden-layer MLP with ReLU activations and layer normalization."""
    hidden_dims: Sequence[int] = (512, 512, 512)
    output_dim: int = 1
    activate_final: bool = False

    @nn.compact
    def __call__(self, x: jnp.ndarray) -> jnp.ndarray:
        for i, dim in enumerate(self.hidden_dims):
            x = nn.Dense(dim)(x)
            x = nn.LayerNorm()(x)
            x = nn.relu(x)
        x = nn.Dense(self.output_dim)(x)
        if self.activate_final:
            x = nn.relu(x)
        return x


class TransformerBlock(nn.Module):
    """Single transformer encoder block (multi-head attention + FFN)."""
    emb_dim: int = 256
    mlp_dim: int = 1024
    num_heads: int = 4
    dropout_rate: float = 0.0
    attention_dropout_rate: float = 0.0

    @nn.compact
    def __call__(self, x: jnp.ndarray, deterministic: bool = True) -> jnp.ndarray:
        # Pre-LN multi-head self-attention (no causal mask)
        residual = x
        x = nn.LayerNorm()(x)
        x = nn.MultiHeadDotProductAttention(
            num_heads=self.num_heads,
            qkv_features=self.emb_dim,
            dropout_rate=self.attention_dropout_rate,
            deterministic=deterministic,
        )(x, x)  # self-attention, no mask -> permutation equivariant
        x = nn.Dropout(rate=self.dropout_rate, deterministic=deterministic)(x)
        x = x + residual

        # Pre-LN feedforward network
        residual = x
        x = nn.LayerNorm()(x)
        x = nn.Dense(self.mlp_dim)(x)
        x = nn.gelu(x)
        x = nn.Dropout(rate=self.dropout_rate, deterministic=deterministic)(x)
        x = nn.Dense(self.emb_dim)(x)
        x = nn.Dropout(rate=self.dropout_rate, deterministic=deterministic)(x)
        x = x + residual

        return x


class TransformerEncoder(nn.Module):
    """
    Permutation-invariant transformer encoder.

    No causal mask, no positional encoding -> permutation invariant.
    """
    num_layers: int = 4
    emb_dim: int = 256
    mlp_dim: int = 1024
    num_heads: int = 4
    dropout_rate: float = 0.0
    attention_dropout_rate: float = 0.0

    @nn.compact
    def __call__(self, x: jnp.ndarray, deterministic: bool = True) -> jnp.ndarray:
        for _ in range(self.num_layers):
            x = TransformerBlock(
                emb_dim=self.emb_dim,
                mlp_dim=self.mlp_dim,
                num_heads=self.num_heads,
                dropout_rate=self.dropout_rate,
                attention_dropout_rate=self.attention_dropout_rate,
            )(x, deterministic=deterministic)
        x = nn.LayerNorm()(x)
        return x


class ValueCritic(nn.Module):
    """V(concat(z, s)) -> scalar value."""
    hidden_dims: Sequence[int] = (512, 512, 512)

    @nn.compact
    def __call__(self, x: jnp.ndarray) -> jnp.ndarray:
        return MLP(hidden_dims=self.hidden_dims, output_dim=1)(x)


class DoubleCritic(nn.Module):
    """Ensemble of 2 Q-networks: Q(concat(z, s), a) -> (Q1, Q2)."""
    hidden_dims: Sequence[int] = (512, 512, 512)

    @nn.compact
    def __call__(self, state_z: jnp.ndarray, actions: jnp.ndarray) -> Tuple[jnp.ndarray, jnp.ndarray]:
        x = jnp.concatenate([state_z, actions], axis=-1)
        q1 = MLP(hidden_dims=self.hidden_dims, output_dim=1, name="critic_1")(x)
        q2 = MLP(hidden_dims=self.hidden_dims, output_dim=1, name="critic_2")(x)
        return q1.squeeze(-1), q2.squeeze(-1)


class GaussianPolicy(nn.Module):
    """
    Gaussian actor: pi(a | concat(z, s)).
    Outputs (mean, log_std) of a diagonal Gaussian.
    log_std clamped to >= -5.
    """
    hidden_dims: Sequence[int] = (512, 512, 512)
    action_dim: int = 1

    @nn.compact
    def __call__(self, x: jnp.ndarray) -> Tuple[jnp.ndarray, jnp.ndarray]:
        h = x
        for dim in self.hidden_dims:
            h = nn.Dense(dim)(h)
            h = nn.LayerNorm()(h)
            h = nn.relu(h)
        mean = nn.Dense(self.action_dim)(h)
        log_std = nn.Dense(self.action_dim)(h)
        log_std = jnp.clip(log_std, a_min=-5.0, a_max=2.0)
        return mean, log_std


# ========== Core FRE Network ==========

class FRENetwork(nn.Module):
    """
    Combined FRE encoder-decoder + IQL policy network (Flax nn.Module).

    Args:
        obs_dim: int, observation dimensionality
        action_dim: int, dimensionality of action space
        hidden_dims: tuple of ints for MLP hidden layer sizes, e.g. (512, 512, 512)
        reward_pairs_emb_dim: int, latent z dimension = 128
        num_discrete_embeddings: int, reward discretization bins = 32
        transformer_num_layers: int = 4
        transformer_emb_dim: int = 256
        transformer_mlp_dim: int = 1024
        transformer_num_heads: int = 4
    """
    obs_dim: int = 29
    action_dim: int = 8
    hidden_dims: Sequence[int] = (512, 512, 512)
    reward_pairs_emb_dim: int = 128
    num_discrete_embeddings: int = 32
    transformer_num_layers: int = 4
    transformer_emb_dim: int = 256
    transformer_mlp_dim: int = 1024
    transformer_num_heads: int = 4
    dropout_rate: float = 0.0
    attention_dropout_rate: float = 0.0

    def setup(self):
        # Encoder components
        half_emb = self.reward_pairs_emb_dim // 2  # 64
        self.reward_embed = nn.Embed(
            num_embeddings=self.num_discrete_embeddings,
            features=half_emb,
        )
        self.state_proj = nn.Dense(half_emb)  # state -> emb_dim//2

        self.encoder_transformer = TransformerEncoder(
            num_layers=self.transformer_num_layers,
            emb_dim=self.reward_pairs_emb_dim,  # full emb_dim = state_emb + reward_emb
            mlp_dim=self.transformer_mlp_dim,
            num_heads=self.transformer_num_heads,
            dropout_rate=self.dropout_rate,
            attention_dropout_rate=self.attention_dropout_rate,
        )

        self.encoder_mean = nn.Dense(self.reward_pairs_emb_dim)
        self.encoder_log_std = nn.Dense(self.reward_pairs_emb_dim)

        # Decoder (reward predictor)
        self.reward_predict = ValueCritic(hidden_dims=self.hidden_dims)

        # IQL policy networks
        self.value = ValueCritic(hidden_dims=self.hidden_dims)
        self.critic = DoubleCritic(hidden_dims=self.hidden_dims)
        self.actor = GaussianPolicy(hidden_dims=self.hidden_dims, action_dim=self.action_dim)

    def get_transformer_encoding(
        self,
        reward_state_pairs: jnp.ndarray,  # [batch, K, obs_dim + 1]  last dim = reward
        deterministic: bool = True,
    ) -> Tuple[jnp.ndarray, jnp.ndarray]:  # (mu_z [batch, emb_dim], log_std_z [batch, emb_dim])
        """
        Encode K (state, reward) pairs into latent distribution (mu_z, log_sigma_z).

        Steps:
          1. Split into states [batch, K, obs_dim] and rewards [batch, K]
          2. Discretize rewards: idx = clip(floor((r/2 + 0.5) * 32), 0, 31)
          3. reward_emb = reward_embed[idx]  # [batch, K, emb_dim//2]
          4. state_emb = Dense(states)       # [batch, K, emb_dim//2]
          5. token = concat(state_emb, reward_emb)  # [batch, K, emb_dim]
          6. h = Transformer(token, train=True)      # [batch, K, emb_dim]
          7. h_mean = mean(h, axis=1)                # [batch, emb_dim]
          8. mu_z = Dense(h_mean); log_std_z = Dense(h_mean)
        """
        # 1. Split states and rewards
        states = reward_state_pairs[..., :-1]   # [batch, K, obs_dim]
        rewards = reward_state_pairs[..., -1]   # [batch, K]

        # 2. Discretize rewards: map [-1, 1] -> [0, 31]
        r_norm = (rewards / 2.0) + 0.5  # map [-1,1] -> [0,1]
        r_norm = jnp.clip(r_norm, 0.0, 1.0)
        bin_idx = jnp.floor(r_norm * self.num_discrete_embeddings).astype(jnp.int32)
        bin_idx = jnp.clip(bin_idx, 0, self.num_discrete_embeddings - 1)

        # 3. Reward embedding
        reward_emb = self.reward_embed(bin_idx)  # [batch, K, emb_dim//2]

        # 4. State projection
        state_emb = self.state_proj(states)      # [batch, K, emb_dim//2]

        # 5. Concatenate to form tokens (no positional encoding)
        tokens = jnp.concatenate([state_emb, reward_emb], axis=-1)  # [batch, K, emb_dim]

        # 6. Transformer encoding (permutation invariant, no causal mask)
        h = self.encoder_transformer(tokens, deterministic=deterministic)  # [batch, K, emb_dim]

        # 7. Mean pool over K tokens
        h_mean = jnp.mean(h, axis=1)  # [batch, emb_dim]

        # 8. Project to Gaussian parameters
        mu_z = self.encoder_mean(h_mean)         # [batch, emb_dim]
        log_std_z = self.encoder_log_std(h_mean)  # [batch, emb_dim]

        return mu_z, log_std_z

    def get_reward_pred(
        self,
        z: jnp.ndarray,            # [batch, emb_dim]
        reward_pairs: jnp.ndarray,  # [batch, K', obs_dim + 1]
    ) -> jnp.ndarray:              # [batch, K']
        """
        Decode reward predictions from latent z and decoder states.

        Steps:
          1. z_expand = repeat(z, K', axis=1)  # [batch, K', emb_dim]
          2. states = reward_pairs[:, :, :-1]  # [batch, K', obs_dim]
          3. input = concat(z_expand, states)  # [batch, K', emb_dim + obs_dim]
          4. output = reward_predict(input)    # [batch, K', 1] -> squeeze -> [batch, K']
        """
        K_prime = reward_pairs.shape[1]

        # 1. Expand z to match K' decoder states
        z_expand = jnp.repeat(z[:, jnp.newaxis, :], K_prime, axis=1)  # [batch, K', emb_dim]

        # 2. Extract decoder states (drop the reward column)
        states = reward_pairs[:, :, :-1]  # [batch, K', obs_dim]

        # 3. Concatenate z and states
        decoder_input = jnp.concatenate([z_expand, states], axis=-1)  # [batch, K', emb_dim + obs_dim]

        # 4. Predict rewards via decoder MLP
        output = self.reward_predict(decoder_input)  # [batch, K', 1]
        return output.squeeze(-1)  # [batch, K']

    def get_value(
        self, z: jnp.ndarray, obs: jnp.ndarray
    ) -> jnp.ndarray:  # scalar per batch element
        """V(concat(z, obs))"""
        x = jnp.concatenate([z, obs], axis=-1)
        return self.value(x).squeeze(-1)  # [batch]

    def get_critic(
        self, z: jnp.ndarray, obs: jnp.ndarray, actions: jnp.ndarray
    ) -> Tuple[jnp.ndarray, jnp.ndarray]:  # (Q1, Q2) each [batch]
        """Q(concat(z, obs), actions) -- ensemble of 2"""
        state_z = jnp.concatenate([z, obs], axis=-1)
        return self.critic(state_z, actions)

    def get_actor(
        self, z: jnp.ndarray, obs: jnp.ndarray
    ) -> Tuple[jnp.ndarray, jnp.ndarray]:  # (mean, log_std)
        """pi(a | concat(z, obs)) -> (mean, log_std) of Gaussian policy"""
        x = jnp.concatenate([z, obs], axis=-1)
        return self.actor(x)

    def sample_action(
        self, z: jnp.ndarray, obs: jnp.ndarray, rng: jnp.ndarray, temperature: float = 1.0
    ) -> jnp.ndarray:
        """Sample action from Gaussian policy."""
        mean, log_std = self.get_actor(z, obs)
        std = jnp.exp(log_std) * temperature
        eps = jax.random.normal(rng, shape=mean.shape)
        return mean + std * eps

    def __call__(
        self,
        reward_state_pairs: jnp.ndarray,
        decoder_pairs: jnp.ndarray,
        obs: jnp.ndarray,
        actions: jnp.ndarray,
        deterministic: bool = True,
    ) -> Dict[str, jnp.ndarray]:
        """Full forward pass for initialization."""
        mu_z, log_std_z = self.get_transformer_encoding(reward_state_pairs, deterministic=deterministic)

        # Reparameterize
        z = mu_z  # deterministic for init

        reward_pred = self.get_reward_pred(z, decoder_pairs)
        v = self.get_value(z, obs)
        q1, q2 = self.get_critic(z, obs, actions)
        mean, log_std = self.get_actor(z, obs)

        return {
            "mu_z": mu_z,
            "log_std_z": log_std_z,
            "reward_pred": reward_pred,
            "value": v,
            "q1": q1,
            "q2": q2,
            "actor_mean": mean,
            "actor_log_std": log_std,
        }


# ========== FRE Agent Update Logic ==========

def fre_encoder_loss(
    params: Any,
    apply_fn: Callable,
    encode_pairs: jnp.ndarray,  # [batch, K, obs_dim + 1]
    decode_pairs: jnp.ndarray,  # [batch, K', obs_dim + 1]
    rng: jnp.ndarray,
    kl_weight: float = 0.01,
) -> Tuple[float, Dict[str, float]]:
    """
    Phase 1 FRE encoder-decoder loss (Equation 6 in paper).

    L = MSE(eta_hat, eta_true) + kl_weight * KL(N(mu_z, sigma_z) || N(0, I))

    Args:
        params: FRENetwork parameters (pytree)
        apply_fn: bound method to call the network
        encode_pairs: encoder context [batch, K, obs_dim+1]; last dim is reward
        decode_pairs: decoder context [batch, K', obs_dim+1]; last dim is reward
        rng: random key for reparameterization
        kl_weight: beta coefficient = 0.01

    Returns:
        (total_loss, info_dict)

    Note: z is sampled via reparameterization: z = mu_z + eps * exp(log_std_z)
    """
    # Encode
    mu_z, log_std_z = apply_fn(
        params, encode_pairs, method="get_transformer_encoding"
    )

    # Reparameterize: z = mu + eps * exp(log_std)
    eps = jax.random.normal(rng, shape=mu_z.shape)
    std_z = jnp.exp(log_std_z)
    z = mu_z + eps * std_z  # [batch, emb_dim]

    # Decode: predict rewards for decoder states
    reward_pred = apply_fn(params, z, decode_pairs, method="get_reward_pred")  # [batch, K']
    reward_true = decode_pairs[:, :, -1]  # [batch, K']

    # MSE reconstruction loss
    mse_loss = jnp.mean((reward_pred - reward_true) ** 2)

    # KL divergence: KL(N(mu, sigma) || N(0, I))
    # = -0.5 * sum(1 + 2*log_std - mu^2 - std^2) per sample, then mean over batch
    kl_loss = -0.5 * jnp.mean(
        jnp.sum(1.0 + 2.0 * log_std_z - mu_z ** 2 - std_z ** 2, axis=-1)
    )

    total_loss = mse_loss + kl_weight * kl_loss

    info = {
        "encoder_loss": total_loss,
        "mse_loss": mse_loss,
        "kl_loss": kl_loss,
        "z_mean_norm": jnp.mean(jnp.linalg.norm(mu_z, axis=-1)),
        "z_std_mean": jnp.mean(std_z),
    }

    return total_loss, info


def iql_value_loss(
    value_params: Any,
    apply_fn: Callable,
    target_q: jnp.ndarray,  # [batch] -- Q_target(s, a, z), detached
    z: jnp.ndarray,          # [batch, emb_dim]
    observations: jnp.ndarray,  # [batch, obs_dim]
    expectile: float = 0.8,
) -> Tuple[float, Dict[str, float]]:
    """
    Value loss (expectile regression):
        adv = Q_target(s,a,z) - V(s,z)
        weight = expectile if adv >= 0 else (1 - expectile)
        L_V = mean(weight * (Q_target - V)^2)
    """
    v_pred = apply_fn(value_params, z, observations, method="get_value")  # [batch]
    adv = target_q - v_pred
    weight = jnp.where(adv >= 0, expectile, 1.0 - expectile)
    loss = jnp.mean(weight * adv ** 2)
    info = {
        "value_loss": loss,
        "v_mean": jnp.mean(v_pred),
        "adv_mean": jnp.mean(adv),
    }
    return loss, info


def iql_critic_loss(
    critic_params: Any,
    apply_fn: Callable,
    z: jnp.ndarray,              # [batch, emb_dim]
    observations: jnp.ndarray,   # [batch, obs_dim]
    actions: jnp.ndarray,        # [batch, act_dim]
    target_value: jnp.ndarray,   # [batch] -- r + gamma * mask * V(s', z), detached
) -> Tuple[float, Dict[str, float]]:
    """
    Critic loss (Bellman backup):
        Q_target_val = r + discount * mask * V(s', z)
        L_Q = mean((Q1 - Q_target_val)^2 + (Q2 - Q_target_val)^2)
    """
    q1, q2 = apply_fn(critic_params, z, observations, actions, method="get_critic")
    loss = jnp.mean((q1 - target_value) ** 2) + jnp.mean((q2 - target_value) ** 2)
    info = {
        "critic_loss": loss,
        "q1_mean": jnp.mean(q1),
        "q2_mean": jnp.mean(q2),
    }
    return loss, info


def iql_actor_loss(
    actor_params: Any,
    apply_fn: Callable,
    z: jnp.ndarray,           # [batch, emb_dim]
    observations: jnp.ndarray,  # [batch, obs_dim]
    actions: jnp.ndarray,     # [batch, act_dim] from dataset
    advantages: jnp.ndarray,  # [batch] -- min(Q1, Q2) - V(s, z), detached
    temperature: float = 3.0,
) -> Tuple[float, Dict[str, float]]:
    """
    Actor loss (AWR):
        exp_adv = clip(exp(adv * temperature), 0, 100)
        L_pi = -mean(exp_adv * log_prob_pi(a | s, z))
    """
    # Compute advantage weights
    exp_adv = jnp.clip(jnp.exp(advantages / temperature), 0.0, 100.0)

    # Actor log probability
    mean, log_std = apply_fn(actor_params, z, observations, method="get_actor")
    std = jnp.exp(log_std)

    # Gaussian log probability: sum over action dims
    log_prob = -0.5 * jnp.sum(
        ((actions - mean) / (std + 1e-8)) ** 2 + 2.0 * log_std + jnp.log(2.0 * jnp.pi),
        axis=-1,
    )  # [batch]

    loss = -jnp.mean(exp_adv * log_prob)
    info = {
        "actor_loss": loss,
        "log_prob_mean": jnp.mean(log_prob),
        "exp_adv_mean": jnp.mean(exp_adv),
    }
    return loss, info


def iql_update_step(
    fre_params: Any,
    target_params: Any,
    apply_fn: Callable,
    z: jnp.ndarray,              # [batch, emb_dim] frozen encoder output
    observations: jnp.ndarray,   # [batch, obs_dim]
    next_observations: jnp.ndarray,  # [batch, obs_dim]
    actions: jnp.ndarray,        # [batch, act_dim]
    rewards: jnp.ndarray,        # [batch]
    masks: jnp.ndarray,          # [batch] -- 1 if not done, 0 if done
    discount: float = 0.88,
    expectile: float = 0.8,
    temperature: float = 3.0,
    target_update_rate: float = 0.001,
) -> Tuple[Any, Any, Dict[str, float]]:
    """
    One IQL update step for Phase 2 (frozen z).

    Computes value, critic, and actor losses. Returns updated params and info.

    Value loss (expectile regression):
        adv = Q_target(s,a,z) - V(s,z)
        weight = expectile if adv >= 0 else (1 - expectile)
        L_V = mean(weight * (Q_target - V)^2)

    Critic loss (Bellman backup):
        Q_target_val = r + discount * mask * V(s', z)
        L_Q = mean((Q1 - Q_target_val)^2 + (Q2 - Q_target_val)^2)

    Actor loss (AWR):
        adv = min(Q1, Q2) - V(s, z)
        exp_adv = clip(exp(adv / temperature), 0, 100)
        L_pi = -mean(exp_adv * log_prob_pi(a | s, z))

    Target critic:
        theta_target <- tau * theta + (1 - tau) * theta_target, tau=0.001
    """
    # --- Compute targets (no gradient) ---
    # Target Q for value update
    target_q1, target_q2 = apply_fn(target_params, z, observations, actions, method="get_critic")
    target_q = jnp.minimum(target_q1, target_q2)  # [batch]

    # V(s', z) for critic Bellman target
    v_next = apply_fn(fre_params, z, next_observations, method="get_value")  # [batch]
    bellman_target = rewards + discount * masks * v_next  # [batch]

    # Advantages for actor
    v_current = apply_fn(fre_params, z, observations, method="get_value")  # [batch]
    q1_current, q2_current = apply_fn(fre_params, z, observations, actions, method="get_critic")
    advantages = jnp.minimum(q1_current, q2_current) - v_current  # [batch]

    # --- Compute all losses ---
    # Value loss
    v_loss, v_info = iql_value_loss(
        fre_params, apply_fn, target_q, z, observations, expectile
    )

    # Critic loss
    c_loss, c_info = iql_critic_loss(
        fre_params, apply_fn, z, observations, actions, bellman_target
    )

    # Actor loss
    a_loss, a_info = iql_actor_loss(
        fre_params, apply_fn, z, observations, actions, advantages, temperature
    )

    total_loss = v_loss + c_loss + a_loss

    # Soft update target params
    new_target_params = jax.tree.map(
        lambda t, s: target_update_rate * s + (1.0 - target_update_rate) * t,
        target_params, fre_params,
    )

    info = {**v_info, **c_info, **a_info, "iql_total_loss": total_loss}

    return fre_params, new_target_params, info


# ========== Agent State ==========

class FREAgentState:
    """Container for all FRE agent state including params and optimizers."""

    def __init__(
        self,
        fre_network: FRENetwork,
        params: Any,
        target_params: Any,
        encoder_optimizer: optax.GradientTransformation,
        encoder_opt_state: Any,
        policy_optimizer: optax.GradientTransformation,
        policy_opt_state: Any,
        rng: jnp.ndarray,
    ):
        self.fre_network = fre_network
        self.params = params
        self.target_params = target_params
        self.encoder_optimizer = encoder_optimizer
        self.encoder_opt_state = encoder_opt_state
        self.policy_optimizer = policy_optimizer
        self.policy_opt_state = policy_opt_state
        self.rng = rng


def create_learner(
    obs_dim: int,
    action_dim: int,
    rng: jnp.ndarray,
    lr: float = 1e-4,
    hidden_dims: Sequence[int] = (512, 512, 512),
    latent_dim: int = 128,
    num_reward_bins: int = 32,
    K_encode: int = 32,
    K_decode: int = 8,
) -> FREAgentState:
    """
    Initialize FRE networks from dummy inputs.

    Args:
        obs_dim: observation dimensionality
        action_dim: action dimensionality
        rng: JAX random key
        lr: learning rate (default 1e-4)
        hidden_dims: MLP hidden layer sizes
        latent_dim: latent z dimension (default 128)
        num_reward_bins: reward discretization bins (default 32)
        K_encode: number of encoder pairs (default 32)
        K_decode: number of decoder pairs (default 8)

    Returns:
        FREAgentState with initialized params and optimizers
    """
    rng, init_rng = jax.random.split(rng)

    # Create network
    fre_net = FRENetwork(
        obs_dim=obs_dim,
        action_dim=action_dim,
        hidden_dims=hidden_dims,
        reward_pairs_emb_dim=latent_dim,
        num_discrete_embeddings=num_reward_bins,
    )

    # Dummy inputs for initialization
    dummy_encode_pairs = jnp.zeros((1, K_encode, obs_dim + 1))
    dummy_decode_pairs = jnp.zeros((1, K_decode, obs_dim + 1))
    dummy_obs = jnp.zeros((1, obs_dim))
    dummy_actions = jnp.zeros((1, action_dim))

    # Initialize parameters
    params = fre_net.init(
        init_rng,
        dummy_encode_pairs,
        dummy_decode_pairs,
        dummy_obs,
        dummy_actions,
    )

    # Copy for target network
    target_params = jax.tree.map(lambda x: x.copy(), params)

    # Create optimizers (Adam)
    encoder_optimizer = optax.adam(learning_rate=lr)
    encoder_opt_state = encoder_optimizer.init(params)

    policy_optimizer = optax.adam(learning_rate=lr)
    policy_opt_state = policy_optimizer.init(params)

    return FREAgentState(
        fre_network=fre_net,
        params=params,
        target_params=target_params,
        encoder_optimizer=encoder_optimizer,
        encoder_opt_state=encoder_opt_state,
        policy_optimizer=policy_optimizer,
        policy_opt_state=policy_opt_state,
        rng=rng,
    )


# ========== Training Step Functions (JIT-compiled) ==========

@partial(jax.jit, static_argnums=(2, 6))
def encoder_train_step(
    params: Any,
    opt_state: Any,
    optimizer: optax.GradientTransformation,
    encode_pairs: jnp.ndarray,
    decode_pairs: jnp.ndarray,
    rng: jnp.ndarray,
    apply_fn: Callable,
    kl_weight: float = 0.01,
) -> Tuple[Any, Any, Dict[str, float]]:
    """Single encoder training step with gradient update."""

    def loss_fn(p):
        return fre_encoder_loss(p, apply_fn, encode_pairs, decode_pairs, rng, kl_weight)

    (loss, info), grads = jax.value_and_grad(loss_fn, has_aux=True)(params)
    updates, new_opt_state = optimizer.update(grads, opt_state, params)
    new_params = optax.apply_updates(params, updates)
    return new_params, new_opt_state, info


@partial(jax.jit, static_argnums=(2,))
def policy_train_step(
    params: Any,
    target_params: Any,
    apply_fn: Callable,
    opt_state: Any,
    optimizer: optax.GradientTransformation,
    z: jnp.ndarray,
    observations: jnp.ndarray,
    next_observations: jnp.ndarray,
    actions: jnp.ndarray,
    rewards: jnp.ndarray,
    masks: jnp.ndarray,
    discount: float = 0.88,
    expectile: float = 0.8,
    temperature: float = 3.0,
    target_update_rate: float = 0.001,
) -> Tuple[Any, Any, Any, Dict[str, float]]:
    """Single IQL policy training step with gradient update."""

    def loss_fn(p):
        # Compute targets (stop gradient through target network)
        target_q1, target_q2 = apply_fn(target_params, z, observations, actions, method="get_critic")
        target_q = jnp.minimum(target_q1, target_q2)

        v_next = apply_fn(p, z, next_observations, method="get_value")
        bellman_target = rewards + discount * masks * v_next

        # Value loss
        v_pred = apply_fn(p, z, observations, method="get_value")
        adv_v = target_q - v_pred
        weight_v = jnp.where(adv_v >= 0, expectile, 1.0 - expectile)
        v_loss = jnp.mean(weight_v * adv_v ** 2)

        # Critic loss
        q1, q2 = apply_fn(p, z, observations, actions, method="get_critic")
        c_loss = jnp.mean((q1 - bellman_target) ** 2) + jnp.mean((q2 - bellman_target) ** 2)

        # Actor loss
        advantages = jnp.minimum(q1, q2) - v_pred
        exp_adv = jnp.clip(jnp.exp(advantages / temperature), 0.0, 100.0)
        mean_a, log_std_a = apply_fn(p, z, observations, method="get_actor")
        std_a = jnp.exp(log_std_a)
        log_prob = -0.5 * jnp.sum(
            ((actions - mean_a) / (std_a + 1e-8)) ** 2 + 2.0 * log_std_a + jnp.log(2.0 * jnp.pi),
            axis=-1,
        )
        a_loss = -jnp.mean(exp_adv * log_prob)

        total = v_loss + c_loss + a_loss
        info = {
            "value_loss": v_loss,
            "critic_loss": c_loss,
            "actor_loss": a_loss,
            "v_mean": jnp.mean(v_pred),
            "q1_mean": jnp.mean(q1),
            "total_loss": total,
        }
        return total, info

    (loss, info), grads = jax.value_and_grad(loss_fn, has_aux=True)(params)
    updates, new_opt_state = optimizer.update(grads, opt_state, params)
    new_params = optax.apply_updates(params, updates)

    # Soft update target params
    new_target_params = jax.tree.map(
        lambda t, s: target_update_rate * s + (1.0 - target_update_rate) * t,
        target_params, new_params,
    )

    return new_params, new_target_params, new_opt_state, info


# ========== Main Training Loop ==========

def train_fre(
    dataset: Dict[str, np.ndarray],
    reward_sampler: Callable,
    agent_state: FREAgentState,
    warmup_steps: int = 150_000,
    policy_steps: int = 850_000,
    batch_size: int = 512,
    reward_pairs_encode: int = 32,
    reward_pairs_decode: int = 8,
    kl_weight: float = 0.01,
    discount: float = 0.88,
    expectile: float = 0.8,
    temperature: float = 3.0,
    target_update_rate: float = 0.001,
    log_interval: int = 1000,
) -> FREAgentState:
    """
    Full FRE training loop (Algorithm 1 in paper).

    Phase 1 -- Encoder training (warmup_steps iterations):
      For each step:
        1. Sample eta ~ p(eta)
        2. Sample K=32 encoder states from D
        3. Sample K'=8 decoder states from D (disjoint)
        4. Compute rewards for all states using eta
        5. Encode: (mu_z, log_std_z) = encoder({(s, eta(s))})
        6. Sample z = mu_z + eps * exp(log_std_z)
        7. Decode: eta_hat = decoder(z, decode_states)
        8. Compute L_FRE = MSE + beta * KL
        9. Gradient step on encoder + decoder params

    Phase 2 -- Policy training (policy_steps iterations):
      Freeze encoder.
      For each step:
        1. Sample eta ~ p(eta)
        2. Sample K=32 encoder states from D
        3. Compute mu_z = encoder_mean({(s, eta(s))})
        4. Sample (s, a, s', done) batch from D
        5. Compute r = eta(s) for batch
        6. IQL update: L_V + L_Q + L_pi with z = mu_z
        7. Soft update target critic

    Args:
        dataset: dict with keys "observations", "actions", "next_observations",
                 "terminals" -- numpy arrays of shape [N, dim].
        reward_sampler: callable that takes (traj_states, random_states,
                        random_states_decode) and returns (params, encode_pairs,
                        decode_pairs, rewards, masks).
        agent_state: initialized FREAgentState.
        warmup_steps: number of encoder pre-training steps.
        policy_steps: number of IQL policy training steps.
        batch_size: training batch size (default 512).
        reward_pairs_encode: K encoder pairs (default 32).
        reward_pairs_decode: K' decoder pairs (default 8).
        kl_weight: KL penalty beta (default 0.01).
        discount: IQL discount gamma (default 0.88).
        expectile: IQL expectile tau (default 0.8).
        temperature: AWR temperature beta_awr (default 3.0).
        target_update_rate: soft target update tau (default 0.001).
        log_interval: steps between logging (default 1000).

    Returns:
        Updated FREAgentState with trained parameters.
    """
    observations = dataset["observations"]
    actions = dataset["actions"]
    next_observations = dataset["next_observations"]
    terminals = dataset["terminals"]
    N = observations.shape[0]
    obs_dim = observations.shape[1]

    fre_net = agent_state.fre_network
    params = agent_state.params
    target_params = agent_state.target_params
    enc_opt = agent_state.encoder_optimizer
    enc_opt_state = agent_state.encoder_opt_state
    pol_opt = agent_state.policy_optimizer
    pol_opt_state = agent_state.policy_opt_state
    rng = agent_state.rng

    apply_fn = fre_net.apply

    # ===== Phase 1: Encoder-Decoder Training =====
    print(f"Phase 1: Encoder training for {warmup_steps} steps...")
    for step in range(warmup_steps):
        rng, sample_rng, train_rng = jax.random.split(rng, 3)

        # Sample batch of random states for encoder and decoder
        idx_enc = np.random.randint(0, N, size=(batch_size, reward_pairs_encode))
        idx_dec = np.random.randint(0, N, size=(batch_size, reward_pairs_decode))

        enc_states = observations[idx_enc]   # [batch, K, obs_dim]
        dec_states = observations[idx_dec]    # [batch, K', obs_dim]

        # Sample a trajectory segment for HER-style goal sampling
        traj_start = np.random.randint(0, max(1, N - 50), size=(batch_size,))
        traj_states = np.stack([
            observations[s:s+50] if s + 50 <= N else observations[s:]
            for s in traj_start
        ])  # [batch, ~50, obs_dim] -- padded as needed

        # Sample reward function and generate pairs
        reward_fn = reward_sampler()
        rew_params, encode_pairs, decode_pairs, _, _ = reward_fn.generate_params_and_pairs(
            traj_states, enc_states, dec_states
        )

        # Convert to JAX arrays
        encode_pairs_jax = jnp.array(encode_pairs)
        decode_pairs_jax = jnp.array(decode_pairs)

        # Encoder gradient step
        def enc_loss_fn(p):
            return fre_encoder_loss(
                p, apply_fn, encode_pairs_jax, decode_pairs_jax, train_rng, kl_weight
            )

        (loss, info), grads = jax.value_and_grad(enc_loss_fn, has_aux=True)(params)
        updates, enc_opt_state = enc_opt.update(grads, enc_opt_state, params)
        params = optax.apply_updates(params, updates)

        if step % log_interval == 0:
            print(f"  Step {step}/{warmup_steps}: loss={info['encoder_loss']:.4f}, "
                  f"mse={info['mse_loss']:.4f}, kl={info['kl_loss']:.4f}")

    # ===== Phase 2: Policy Training (encoder frozen) =====
    print(f"\nPhase 2: Policy training for {policy_steps} steps (encoder frozen)...")
    # Copy params for frozen encoder reference
    frozen_params = jax.tree.map(lambda x: x.copy(), params)

    for step in range(policy_steps):
        rng, sample_rng, train_rng = jax.random.split(rng, 3)

        # Sample reward function
        reward_fn = reward_sampler()

        # Sample K encoder states and compute z (frozen encoder)
        idx_enc = np.random.randint(0, N, size=(batch_size, reward_pairs_encode))
        enc_states = observations[idx_enc]

        # Build trajectory for goal sampling
        traj_start = np.random.randint(0, max(1, N - 50), size=(batch_size,))
        traj_states = np.stack([
            observations[s:s+50] if s + 50 <= N else observations[s:]
            for s in traj_start
        ])

        # Dummy decode states (not needed for policy phase)
        idx_dec = np.random.randint(0, N, size=(batch_size, reward_pairs_decode))
        dec_states = observations[idx_dec]

        rew_params, encode_pairs, _, _, _ = reward_fn.generate_params_and_pairs(
            traj_states, enc_states, dec_states
        )

        # Encode with frozen encoder -> get mu_z (deterministic)
        encode_pairs_jax = jnp.array(encode_pairs)
        mu_z, _ = apply_fn(frozen_params, encode_pairs_jax, method="get_transformer_encoding")
        z = mu_z  # use mean (no sampling during policy phase)

        # Sample transitions from dataset
        idx_batch = np.random.randint(0, N, size=batch_size)
        obs_batch = jnp.array(observations[idx_batch])
        act_batch = jnp.array(actions[idx_batch])
        next_obs_batch = jnp.array(next_observations[idx_batch])
        term_batch = terminals[idx_batch]

        # Compute rewards for batch states using sampled reward function
        batch_states_np = observations[idx_batch]
        rew_batch = reward_fn.compute_reward(batch_states_np, np.broadcast_to(
            rew_params, (batch_size,) + rew_params.shape[-1:]
        ) if rew_params.ndim == 1 else rew_params)
        rew_batch = jnp.array(rew_batch)

        # Masks: 1 if not done, 0 if done
        masks_batch = jnp.array(1.0 - term_batch.astype(np.float32))

        # IQL policy gradient step
        def pol_loss_fn(p):
            # Compute targets (stop gradient through target network)
            tq1, tq2 = apply_fn(target_params, z, obs_batch, act_batch, method="get_critic")
            target_q = jnp.minimum(tq1, tq2)

            v_next = apply_fn(p, z, next_obs_batch, method="get_value")
            bellman_target = rew_batch + discount * masks_batch * v_next

            # Value loss (expectile regression)
            v_pred = apply_fn(p, z, obs_batch, method="get_value")
            adv_v = target_q - v_pred
            weight_v = jnp.where(adv_v >= 0, expectile, 1.0 - expectile)
            v_loss = jnp.mean(weight_v * adv_v ** 2)

            # Critic loss
            q1, q2 = apply_fn(p, z, obs_batch, act_batch, method="get_critic")
            c_loss = jnp.mean((q1 - bellman_target) ** 2) + jnp.mean((q2 - bellman_target) ** 2)

            # Actor loss (AWR)
            advantages = jnp.minimum(q1, q2) - v_pred
            exp_adv = jnp.clip(jnp.exp(advantages / temperature), 0.0, 100.0)
            mean_a, log_std_a = apply_fn(p, z, obs_batch, method="get_actor")
            std_a = jnp.exp(log_std_a)
            log_prob = -0.5 * jnp.sum(
                ((act_batch - mean_a) / (std_a + 1e-8)) ** 2
                + 2.0 * log_std_a
                + jnp.log(2.0 * jnp.pi),
                axis=-1,
            )
            a_loss = -jnp.mean(exp_adv * log_prob)

            total = v_loss + c_loss + a_loss
            info = {
                "value_loss": v_loss,
                "critic_loss": c_loss,
                "actor_loss": a_loss,
                "total_loss": total,
                "v_mean": jnp.mean(v_pred),
                "q1_mean": jnp.mean(q1),
            }
            return total, info

        (loss, info), grads = jax.value_and_grad(pol_loss_fn, has_aux=True)(params)
        updates, pol_opt_state = pol_opt.update(grads, pol_opt_state, params)
        params = optax.apply_updates(params, updates)

        # Soft update target params
        target_params = jax.tree.map(
            lambda t, s: target_update_rate * s + (1.0 - target_update_rate) * t,
            target_params, params,
        )

        if step % log_interval == 0:
            print(f"  Step {step}/{policy_steps}: total={info['total_loss']:.4f}, "
                  f"v_loss={info['value_loss']:.4f}, c_loss={info['critic_loss']:.4f}, "
                  f"a_loss={info['actor_loss']:.4f}")

    # Return updated state
    agent_state.params = params
    agent_state.target_params = target_params
    agent_state.encoder_opt_state = enc_opt_state
    agent_state.policy_opt_state = pol_opt_state
    agent_state.rng = rng

    print("\nTraining complete.")
    return agent_state
