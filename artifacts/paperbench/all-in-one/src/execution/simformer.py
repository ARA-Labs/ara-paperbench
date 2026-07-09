"""
Simformer: Core implementation stubs for the all-in-one simulation-based inference model.

Implements:
- Tokenizer: maps (values, ids, condition_mask, optional metadata) → token sequence
- SimformerScoreModel: transformer-based score estimator
- Training loss (denoising score-matching)
- Sampling (Euler-Maruyama reverse SDE)

Architecture (default benchmark tasks):
  - Token dimension: 50
  - Layers: 6 (8 for LV/SIRD/HH)
  - Heads: 4
  - Attention size: 10
  - FF hidden dim: 150 (widening factor 3)
  - Diffusion time embedding: 128-dim random Fourier features

Reference: Gloeckler et al., 2024, "All-in-one simulation-based inference"
"""

import math
import numpy as np
from typing import Optional, Tuple


# ---------------------------------------------------------------------------
# Tokenizer
# ---------------------------------------------------------------------------

class SBITokenizer:
    """
    Maps a sequence of scalar variables to a sequence of fixed-size tokens.

    Each token = concat([id_embed, value_embed, metadata_embed*, cond_embed])
    where:
      - id_embed:       learnable vector for the variable's integer ID
      - value_embed:    scalar value repeated to match embed_dim
      - metadata_embed: random Fourier embedding of index (for fn-valued params)
      - cond_embed:     learnable vector if observed (M_C=1), else zero vector

    Args:
        num_vars (int): Total number of unique variable IDs.
        token_dim (int): Output token dimension (default: 50).
        fourier_dim (int): Dimension of random Fourier embedding for metadata (default: 128).
    """

    def __init__(self, num_vars: int, token_dim: int = 50, fourier_dim: int = 128):
        self.num_vars = num_vars
        self.token_dim = token_dim
        self.fourier_dim = fourier_dim

        # Learnable embeddings (shape: [num_vars, token_dim])
        # id_embeddings[i] is the identifier embedding for variable i
        self.id_embeddings = None       # shape: (num_vars, token_dim)
        self.cond_true_embedding = None # shape: (token_dim,) — for M_C=1
        # M_C=0 → zero vector of shape (token_dim,)

        # Random Fourier features for metadata (fixed, not learned)
        # W: (fourier_dim // 2, metadata_dim)
        self.fourier_weights = None     # shape: (fourier_dim // 2, metadata_input_dim)
        # Learnable linear projection: fourier_dim → token_dim
        self.fourier_proj = None        # shape: (fourier_dim, token_dim)

    def tokenize(
        self,
        values: np.ndarray,        # shape: (B, d) — scalar values for each variable
        var_ids: np.ndarray,       # shape: (d,) — integer IDs for each variable
        condition_mask: np.ndarray, # shape: (B, d) — 1=observed, 0=unobserved
        metadata: Optional[np.ndarray] = None,  # shape: (d, metadata_dim) — e.g. time indices
    ) -> np.ndarray:
        """
        Tokenize a batch of variable observations.

        Returns:
            tokens: shape (B, d, token_dim)
        """
        B, d = values.shape

        # 1. ID embeddings: (d, token_dim)
        id_emb = self.id_embeddings[var_ids]  # (d, token_dim)
        id_emb = np.broadcast_to(id_emb, (B, d, self.token_dim))

        # 2. Value embeddings: repeat scalar to match token_dim → (B, d, token_dim)
        val_emb = np.repeat(values[:, :, None], self.token_dim, axis=-1)  # (B, d, token_dim)

        # 3. Metadata embeddings (optional, for function-valued params): (d, token_dim)
        if metadata is not None:
            # Random Fourier embedding: fourier(x) = [sin(Wx), cos(Wx)]
            proj = metadata @ self.fourier_weights.T  # (d, fourier_dim//2)
            meta_fourier = np.concatenate([np.sin(proj), np.cos(proj)], axis=-1)  # (d, fourier_dim)
            meta_emb = meta_fourier @ self.fourier_proj  # (d, token_dim)
            meta_emb = np.broadcast_to(meta_emb, (B, d, self.token_dim))
        else:
            meta_emb = np.zeros((B, d, self.token_dim))

        # 4. Condition state embeddings: (B, d, token_dim)
        # M_C=1 → learnable cond_true_embedding; M_C=0 → zero vector
        cond_emb = condition_mask[:, :, None] * self.cond_true_embedding[None, None, :]  # (B, d, token_dim)

        # 5. Concatenate and project to token_dim
        # Note: all components have shape (B, d, token_dim) and are summed
        tokens = id_emb + val_emb + meta_emb + cond_emb  # (B, d, token_dim)
        return tokens


# ---------------------------------------------------------------------------
# Score Model (Transformer)
# ---------------------------------------------------------------------------

class MultiHeadAttention:
    """
    Standard multi-head self-attention with optional attention mask.

    Args:
        token_dim (int): Input/output token dimension (default: 50).
        num_heads (int): Number of attention heads (default: 4).
        head_dim (int): Dimension per head / attention size (default: 10).
    """

    def __init__(self, token_dim: int = 50, num_heads: int = 4, head_dim: int = 10):
        self.token_dim = token_dim
        self.num_heads = num_heads
        self.head_dim = head_dim

        # Learnable projection matrices (initialize as None; set during training init)
        # W_Q: (token_dim, num_heads * head_dim)  e.g. (50, 40)
        self.W_Q = None
        # W_K: (token_dim, num_heads * head_dim)  e.g. (50, 40)
        self.W_K = None
        # W_V: (token_dim, num_heads * head_dim)  e.g. (50, 40)
        self.W_V = None
        # W_O: (num_heads * head_dim, token_dim)  e.g. (40, 50)
        self.W_O = None

    def forward(
        self,
        x: np.ndarray,                      # (B, d, token_dim)
        attention_mask: np.ndarray,          # (d, d) binary mask; 1=allow, 0=block
    ) -> np.ndarray:                         # (B, d, token_dim)
        """
        Apply masked multi-head self-attention.

        attention_mask[i, j] = 1 means token j can attend to token i.
        (Rows = query variable, Cols = key/value variable.)
        """
        B, d, _ = x.shape
        H = self.num_heads
        dk = self.head_dim

        # 1. Project x → Q, K, V  each: (B, d, num_heads * head_dim)
        Q = x @ self.W_Q   # (B, d, H*dk)
        K = x @ self.W_K   # (B, d, H*dk)
        V = x @ self.W_V   # (B, d, H*dk)

        # 2. Reshape to (B, num_heads, d, head_dim) for batched attention
        Q = Q.reshape(B, d, H, dk).transpose(0, 2, 1, 3)   # (B, H, d, dk)
        K = K.reshape(B, d, H, dk).transpose(0, 2, 1, 3)   # (B, H, d, dk)
        V = V.reshape(B, d, H, dk).transpose(0, 2, 1, 3)   # (B, H, d, dk)

        # 3. Compute attention scores: Q @ K^T / sqrt(head_dim)
        scores = np.matmul(Q, K.transpose(0, 1, 3, 2)) / math.sqrt(dk)  # (B, H, d, d)

        # 4. Apply attention mask: set scores to -1e9 where mask == 0
        # attention_mask is (d, d); broadcast to (1, 1, d, d)
        mask = attention_mask[None, None, :, :]   # (1, 1, d, d)
        scores = np.where(mask == 1, scores, -1e9)

        # 5. Softmax over key dimension (last axis)
        scores_max = scores.max(axis=-1, keepdims=True)
        exp_scores = np.exp(scores - scores_max)
        attn_weights = exp_scores / (exp_scores.sum(axis=-1, keepdims=True) + 1e-12)  # (B, H, d, d)

        # 6. Apply attention weights to V: context = attn_weights @ V
        context = np.matmul(attn_weights, V)   # (B, H, d, dk)

        # 7. Reshape back to (B, d, num_heads * head_dim)
        context = context.transpose(0, 2, 1, 3).reshape(B, d, H * dk)  # (B, d, H*dk)

        # 8. Output projection: (B, d, H*dk) @ (H*dk, token_dim) → (B, d, token_dim)
        out = context @ self.W_O   # (B, d, token_dim)
        return out


class FeedForward:
    """
    Position-wise feed-forward block with diffusion time injection.

    hidden_dim = token_dim * widening_factor (default: 50 * 3 = 150)
    Diffusion time t is projected and added after the FF block.
    """

    def __init__(self, token_dim: int = 50, widening_factor: int = 3, time_dim: int = 128):
        self.token_dim = token_dim
        self.hidden_dim = token_dim * widening_factor   # 150
        self.time_dim = time_dim

        # Learnable parameters (initialize as None; set during training init)
        # W1: (token_dim, hidden_dim)   e.g. (50, 150)
        self.W1 = None
        # b1: (hidden_dim,)             e.g. (150,)
        self.b1 = None
        # W2: (hidden_dim, token_dim)   e.g. (150, 50)
        self.W2 = None
        # b2: (token_dim,)              e.g. (50,)
        self.b2 = None
        # W_time: (time_dim * 2, token_dim)  e.g. (256, 50) — diffusion time projection
        self.W_time = None

    def forward(self, x: np.ndarray, t_emb: np.ndarray) -> np.ndarray:
        """
        Position-wise feed-forward with diffusion time injection.

        Args:
            x: (B, d, token_dim)
            t_emb: (B, time_dim*2) — random Fourier embedding of diffusion time t
        Returns:
            out: (B, d, token_dim)
        """
        # 1. First linear layer + ReLU: (B, d, token_dim) → (B, d, hidden_dim)
        h = x @ self.W1 + self.b1          # (B, d, hidden_dim=150)
        h = np.maximum(h, 0)               # ReLU

        # 2. Second linear layer: (B, d, hidden_dim) → (B, d, token_dim)
        h = h @ self.W2 + self.b2          # (B, d, token_dim=50)

        # 3. Project diffusion time embedding: (B, time_dim*2) → (B, token_dim)
        t_proj = t_emb @ self.W_time       # (B, token_dim=50)

        # 4. Add time projection (broadcast across all tokens)
        h = h + t_proj[:, None, :]         # (B, d, token_dim)

        return h


class SimformerBlock:
    """Single transformer block: LayerNorm → Attention → Residual → LayerNorm → FF → Residual."""

    def __init__(self, token_dim: int = 50, num_heads: int = 4, head_dim: int = 10,
                 widening_factor: int = 3, time_dim: int = 128):
        self.attn = MultiHeadAttention(token_dim, num_heads, head_dim)
        self.ff = FeedForward(token_dim, widening_factor, time_dim)

    def forward(self, x: np.ndarray, t_emb: np.ndarray, attention_mask: np.ndarray) -> np.ndarray:
        """x: (B, d, token_dim) → (B, d, token_dim)"""
        # LayerNorm → Attention → Residual
        x = x + self.attn.forward(layer_norm(x), attention_mask)
        # LayerNorm → FeedForward (with time injection) → Residual
        x = x + self.ff.forward(layer_norm(x), t_emb)
        return x


class SimformerScoreModel:
    """
    Transformer-based score model for the Simformer.

    Inputs:
        tokens:         (B, d, token_dim) — tokenized variables from SBITokenizer
        t:              (B,) — diffusion time
        attention_mask: (d, d) — binary mask encoding dependency structure M_E
    Output:
        scores:         (B, d) — estimated score for each variable at noise level t

    Default config (benchmark tasks):
        token_dim=50, n_layers=6, n_heads=4, head_dim=10, hidden_dim=150, time_fourier_dim=128
    For LV/SIRD/HH: n_layers=8.
    """

    def __init__(
        self,
        token_dim: int = 50,
        n_layers: int = 6,
        n_heads: int = 4,
        head_dim: int = 10,
        widening_factor: int = 3,
        time_fourier_dim: int = 128,
    ):
        self.token_dim = token_dim
        self.n_layers = n_layers

        # Random Fourier features for diffusion time (fixed, not learned)
        # W_time: (time_fourier_dim, 1) — sampled from N(0,1) at init
        self.time_fourier_weights = None   # shape: (time_fourier_dim // 2,)

        # Transformer blocks
        self.blocks = [
            SimformerBlock(token_dim, n_heads, head_dim, widening_factor, time_fourier_dim)
            for _ in range(n_layers)
        ]

        # Output head: token_dim → 1 (one score per variable)
        self.output_proj = None   # shape: (token_dim, 1)

    def time_embedding(self, t: np.ndarray) -> np.ndarray:
        """
        Embed scalar diffusion time t using 128-dim random Gaussian Fourier features.

        t: (B,) → t_emb: (B, 256)
        fourier(t) = [sin(W*t), cos(W*t)] where W ~ N(0,1)
        """
        # W: (time_fourier_dim // 2,)
        proj = t[:, None] * self.time_fourier_weights[None, :]   # (B, fourier_dim//2)
        return np.concatenate([np.sin(proj), np.cos(proj)], axis=-1)   # (B, fourier_dim)

    def forward(
        self,
        tokens: np.ndarray,          # (B, d, token_dim)
        t: np.ndarray,               # (B,)
        attention_mask: np.ndarray,  # (d, d) binary mask
    ) -> np.ndarray:                 # (B, d) scores
        """Forward pass through transformer; returns score for each variable."""
        t_emb = self.time_embedding(t)    # (B, 256)
        x = tokens                         # (B, d, token_dim)

        for block in self.blocks:
            x = block.forward(x, t_emb, attention_mask)

        # Linear output head: (B, d, token_dim) → (B, d)
        scores = (x @ self.output_proj).squeeze(-1)   # (B, d)
        return scores


# ---------------------------------------------------------------------------
# Training Loss
# ---------------------------------------------------------------------------

def sample_condition_mask(
    batch_size: int,
    d: int,
    data_indices: np.ndarray,    # indices corresponding to data variables
    param_indices: np.ndarray,   # indices corresponding to parameter variables
) -> np.ndarray:
    """
    Sample condition mask M_C for a training batch.

    At each batch, uniformly select one of 5 mask types:
      1. Joint:      all zeros
      2. Posterior:  data=1, params=0
      3. Likelihood: data=0, params=1
      4. Bernoulli(p=0.3): random per element
      5. Bernoulli(p=0.7): random per element

    Returns:
        M_C: (B, d) binary array
    """
    mask_type = np.random.randint(0, 5)
    M_C = np.zeros((batch_size, d), dtype=np.float32)

    if mask_type == 0:       # Joint
        pass
    elif mask_type == 1:     # Posterior: data observed, params latent
        M_C[:, data_indices] = 1.0
    elif mask_type == 2:     # Likelihood: params observed, data latent
        M_C[:, param_indices] = 1.0
    elif mask_type == 3:     # Random Bernoulli p=0.3
        M_C = (np.random.rand(batch_size, d) < 0.3).astype(np.float32)
    elif mask_type == 4:     # Random Bernoulli p=0.7
        M_C = (np.random.rand(batch_size, d) < 0.7).astype(np.float32)

    return M_C


def vesde_noise(
    x0: np.ndarray,     # (B, d) — clean samples
    t: np.ndarray,      # (B,) — noise levels in [1e-5, 1]
    sigma_min: float = 0.0001,
    sigma_max: float = 15.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Add VESDE noise to samples x0.

    sigma(t) = sigma_min * (sigma_max / sigma_min)^t
    x_t = x0 + sigma(t) * eps,  eps ~ N(0, I)

    Returns:
        x_t:   (B, d) noisy samples
        sigma: (B,) noise standard deviation at each t
    """
    sigma = sigma_min * (sigma_max / sigma_min) ** t    # (B,)
    eps = np.random.randn(*x0.shape)
    x_t = x0 + sigma[:, None] * eps
    return x_t, sigma


def vesde_target_score(
    x0: np.ndarray,   # (B, d)
    x_t: np.ndarray,  # (B, d)
    sigma: np.ndarray, # (B,)
) -> np.ndarray:
    """
    Compute target score for VESDE: ∇_{x_t} log p_t(x_t | x_0) = -(x_t - x_0) / sigma(t)^2.

    Returns:
        target_score: (B, d)
    """
    return -(x_t - x0) / (sigma[:, None] ** 2)


def simformer_loss(
    score_model: SimformerScoreModel,
    tokenizer: SBITokenizer,
    x0: np.ndarray,               # (B, d) — clean joint samples (theta, x)
    var_ids: np.ndarray,          # (d,) — variable IDs
    data_indices: np.ndarray,     # indices of data variables
    param_indices: np.ndarray,    # indices of parameter variables
    attention_mask: np.ndarray,   # (d, d)
    sigma_min: float = 0.0001,
    sigma_max: float = 15.0,
    t_min: float = 1e-5,
    t_max: float = 1.0,
    metadata: Optional[np.ndarray] = None,
) -> float:
    """
    Compute denoising score-matching loss for the Simformer.

    Loss: E_{M_C, t, x0, x_t}[||(1 - M_C) * (score_pred - score_target)||^2]
    Only unobserved variables (M_C=0) contribute to the loss.

    Returns:
        scalar loss value
    """
    B, d = x0.shape

    # 1. Sample condition mask M_C
    M_C = sample_condition_mask(B, d, data_indices, param_indices)   # (B, d)

    # 2. Sample noise level t ~ Uniform(t_min, t_max)
    t = np.random.uniform(t_min, t_max, size=(B,))   # (B,)

    # 3. Add VESDE noise to all variables
    x_t, sigma = vesde_noise(x0, t, sigma_min, sigma_max)   # (B, d), (B,)

    # 4. Mix: observed variables stay clean, unobserved get noise
    x_mixed = (1 - M_C) * x_t + M_C * x0   # (B, d)

    # 5. Tokenize
    tokens = tokenizer.tokenize(x_mixed, var_ids, M_C, metadata)   # (B, d, token_dim)

    # 6. Compute predicted scores
    score_pred = score_model.forward(tokens, t, attention_mask)   # (B, d)

    # 7. Compute target scores (VESDE)
    score_target = vesde_target_score(x0, x_t, sigma)   # (B, d)

    # 8. Loss only on unobserved variables (M_C = 0)
    # Weighting lambda(t) = g(t)^2 for VESDE
    g_t = sigma_min * (sigma_max / sigma_min) ** t * math.sqrt(2 * math.log(sigma_max / sigma_min))
    lam = g_t ** 2   # (B,)

    residual = (1 - M_C) * (score_pred - score_target)   # (B, d)
    loss = np.mean(lam[:, None] * residual ** 2)
    return loss


# ---------------------------------------------------------------------------
# Sampling (Reverse SDE — Euler-Maruyama)
# ---------------------------------------------------------------------------

def sample_conditional(
    score_model: SimformerScoreModel,
    tokenizer: SBITokenizer,
    x_obs: np.ndarray,           # (d,) — observed values (for M_C=1 variables)
    condition_mask: np.ndarray,  # (d,) — 1=observed, 0=to-be-sampled
    var_ids: np.ndarray,         # (d,)
    attention_mask: np.ndarray,  # (d, d)
    n_samples: int = 1,
    n_steps: int = 500,
    sigma_min: float = 0.0001,
    sigma_max: float = 15.0,
    t_min: float = 1e-5,
    t_max: float = 1.0,
    metadata: Optional[np.ndarray] = None,
) -> np.ndarray:
    """
    Sample from the conditional distribution p(x_unobserved | x_observed).

    Uses Euler-Maruyama reverse SDE (VESDE, f=0):
      x_{t-dt} = x_t + g(t)^2 * score(x_t, t) * |dt| + g(t) * sqrt(|dt|) * eps

    Observed variables remain fixed at x_obs throughout.

    Returns:
        samples: (n_samples, d)
    """
    d = len(x_obs)
    B = n_samples

    # Initialize from terminal noise distribution p_T = N(x_obs, sigma_max * I)
    sigma_T = sigma_min * (sigma_max / sigma_min) ** t_max
    x = np.random.randn(B, d) * sigma_T
    # Override observed variables with their clean values
    x[:, condition_mask == 1] = x_obs[condition_mask == 1]

    M_C = np.broadcast_to(condition_mask[None, :], (B, d)).copy()

    # Time schedule: from t_max to t_min
    t_schedule = np.linspace(t_max, t_min, n_steps + 1)

    for i in range(n_steps):
        t_curr = t_schedule[i]
        t_next = t_schedule[i + 1]
        dt = t_next - t_curr   # negative (going backward)

        t_batch = np.full((B,), t_curr)

        # Tokenize current state
        tokens = tokenizer.tokenize(x, var_ids, M_C, metadata)   # (B, d, token_dim)

        # Score estimate
        score = score_model.forward(tokens, t_batch, attention_mask)   # (B, d)

        # VESDE diffusion coefficient: g(t) = sigma_min * (sigma_max/sigma_min)^t * sqrt(2 log(sigma_max/sigma_min))
        log_ratio = math.log(sigma_max / sigma_min)
        g_t = sigma_min * (sigma_max / sigma_min) ** t_curr * math.sqrt(2 * log_ratio)

        eps = np.random.randn(B, d)

        # Reverse Euler-Maruyama step (VESDE f=0, so drift term = g^2 * score)
        dx = g_t**2 * score * abs(dt) + g_t * math.sqrt(abs(dt)) * eps

        # Update only unobserved variables
        x += dx * (1 - M_C)
        # Keep observed variables fixed
        x[:, condition_mask == 1] = x_obs[condition_mask == 1]

    return x


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def layer_norm(x: np.ndarray) -> np.ndarray:
    """Layer normalization along the last dimension."""
    mean = x.mean(axis=-1, keepdims=True)
    std = x.std(axis=-1, keepdims=True) + 1e-6
    return (x - mean) / std
