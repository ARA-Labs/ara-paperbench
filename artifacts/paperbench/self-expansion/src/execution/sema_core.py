"""
SEMA Core Modules: AdapterModule, SEMAModules, AE (Representation Descriptor), Records buffer.
Implements the novel contribution: on-demand z-score-based self-expansion of adapters
within a frozen ViT, with an expandable soft-mixture routing mechanism.

Source: backbone/sema_components.py, backbone/sema_block.py
"""

import math
import copy
import logging
from typing import List

import torch
import torch.nn as nn
import torch.nn.functional as F

device = 'cuda' if torch.cuda.is_available() else 'cpu'


# ─────────────────────────────────────────────────────────────────────────────
# 1. Functional Adapter
# ─────────────────────────────────────────────────────────────────────────────

class FunctionalAdapter(nn.Module):
    """
    Lightweight bottleneck adapter: down_proj → ReLU → up_proj.
    Equation (1): f_{φ_k^l}(x^l) = ReLU(x^l · W_down) · W_up

    Args:
        d_model (int): Input/output feature dimension (768 for ViT-B).
        bottleneck (int): Bottleneck dimension r (16 by default in SEMA).
        dropout (float): Dropout rate (0.1 in SEMA).
    """
    def __init__(self, d_model: int = 768, bottleneck: int = 16, dropout: float = 0.1):
        super().__init__()
        self.down_proj = nn.Linear(d_model, bottleneck)
        self.non_linear_func = nn.ReLU()
        self.up_proj = nn.Linear(bottleneck, d_model)
        self.dropout = nn.Dropout(dropout)
        # LoRA-style init: zero output at initialization
        with torch.no_grad():
            nn.init.kaiming_uniform_(self.down_proj.weight, a=math.sqrt(5))
            nn.init.zeros_(self.up_proj.weight)
            nn.init.zeros_(self.down_proj.bias)
            nn.init.zeros_(self.up_proj.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [B, S, d_model] — sequence of token features at layer l
        Returns:
            [B, S, d_model] — adapter output (zero at init)
        """
        down = self.down_proj(x)
        down = self.non_linear_func(down)
        output = self.up_proj(down)
        return output


# ─────────────────────────────────────────────────────────────────────────────
# 2. Representation Descriptor (Autoencoder)
# ─────────────────────────────────────────────────────────────────────────────

class RepresentationDescriptor(nn.Module):
    """
    Autoencoder-based representation descriptor g_{φ_k^l}.
    Trained to reconstruct mean-pooled layer features, serving as a
    distribution shift indicator via reconstruction error z-scores.

    Equation (2): L_{RD,k}^l(x) = Σ ||x - g_{φ_k^l}(x)||_2^2

    Architecture:
        Encoder: Linear(d_model → rd_dim) → LeakyReLU
        Decoder: Linear(rd_dim → d_model)
    """
    def __init__(self, d_model: int = 768, rd_dim: int = 128):
        super().__init__()
        self.encoder = nn.Linear(d_model, rd_dim)
        self.activation = nn.LeakyReLU()
        self.decoder = nn.Linear(rd_dim, d_model)
        # Kaiming init
        with torch.no_grad():
            nn.init.kaiming_uniform_(self.encoder.weight, a=math.sqrt(5))
            nn.init.zeros_(self.encoder.bias)
            nn.init.kaiming_uniform_(self.decoder.weight, a=math.sqrt(5))
            nn.init.zeros_(self.decoder.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: [B, d_model]; returns reconstruction [B, d_model]"""
        encoded = self.activation(self.encoder(x))
        return self.decoder(encoded)

    def compute_reconstruction_loss(self, x: torch.Tensor) -> torch.Tensor:
        """
        Compute per-sample MSE reconstruction loss on mean-pooled features.
        Args:
            x: [B, S, d_model] — layer features (sequence including CLS token)
        Returns:
            losses: [B] — per-sample reconstruction MSE
        """
        x_pooled = x.mean(dim=1)       # [B, d_model]: mean-pool over sequence
        reconstruction = self.forward(x_pooled)
        losses = F.mse_loss(reconstruction, x_pooled, reduction='none').mean(dim=-1)  # [B]
        return losses


# ─────────────────────────────────────────────────────────────────────────────
# 3. Records Buffer (running statistics for z-score)
# ─────────────────────────────────────────────────────────────────────────────

class Records:
    """
    Sliding-window buffer of size max_len (500) tracking reconstruction errors.
    Used to compute running mean and std for z-score normalization.
    """
    def __init__(self, max_len: int = 500):
        self._max_len = max_len
        self._curr_len = 0
        self.record = torch.zeros(self._max_len)
        self._mean: float = 0.0
        self._var: float = 0.0
        self.updating: bool = True

    @property
    def length(self) -> int:
        return self._curr_len

    @property
    def mean(self) -> float:
        return float(self._mean)

    @property
    def stddev(self) -> float:
        return math.sqrt(float(self._var)) if float(self._var) > 0 else 1e-8

    def add_record(self, v: torch.Tensor):
        """Add new reconstruction error values (CPU tensor) to the sliding window."""
        if not self.updating:
            return
        if self._curr_len < self._max_len:
            place_left = self._max_len - self._curr_len
            to_add = v[:place_left]
            self.record[self._curr_len:self._curr_len + len(to_add)] = to_add
            self._curr_len += len(to_add)
        else:
            self.record = torch.cat([self.record, v])[-self._max_len:]
        self._mean = self.record[:self._curr_len].mean().item()
        self._var = self.record[:self._curr_len].var().item()


# ─────────────────────────────────────────────────────────────────────────────
# 4. AdapterModule: Paired (FunctionalAdapter, RepresentationDescriptor)
# ─────────────────────────────────────────────────────────────────────────────

class AdapterModule(nn.Module):
    """
    Paired modular adapter unit: functional adapter f_{φ_k^l} + RD g_{φ_k^l}.
    Handles forward pass, z-score computation, and buffer updating.

    Args:
        d_model: ViT hidden dimension (768).
        bottleneck: Adapter bottleneck dim (16).
        rd_dim: RD bottleneck dim (128).
        buffer_size: Sliding window size for reconstruction error stats (500).
        is_expansion_layer: If False, RD is disabled (layer outside eligible range).
    """
    def __init__(self, d_model: int = 768, bottleneck: int = 16, rd_dim: int = 128,
                 buffer_size: int = 500, is_expansion_layer: bool = True):
        super().__init__()
        self.functional = FunctionalAdapter(d_model, bottleneck)
        self.rd = RepresentationDescriptor(d_model, rd_dim) if is_expansion_layer else None
        self.rd_loss_record = Records(max_len=buffer_size)
        self.newly_added: bool = True
        self.is_expansion_layer = is_expansion_layer

    def forward(self, x: torch.Tensor):
        """
        Args:
            x: [B, S, d_model] — layer input features
        Returns:
            func_out: [B, S, d_model]
            rd_loss: scalar tensor (0 if not expansion layer)
            z_score: [B] per-sample z-scores (0 if not expansion layer or buffer < 2)
        """
        func_out = self.functional(x)
        if not self.is_expansion_layer or self.rd is None:
            return func_out, torch.tensor(0.).to(x.device), torch.zeros(x.shape[0]).to(x.device)

        rd_losses = self.rd.compute_reconstruction_loss(x)   # [B]
        z_scores = self._compute_z_scores(rd_losses)          # [B]

        if self.training:
            self.rd_loss_record.add_record(rd_losses.detach().cpu())

        return func_out, rd_losses, z_scores

    def _compute_z_scores(self, rd_losses: torch.Tensor) -> torch.Tensor:
        """Normalize reconstruction errors to z-scores using running buffer stats."""
        if self.rd_loss_record.length <= 2:
            return torch.zeros_like(rd_losses)
        mean = self.rd_loss_record.mean
        std = self.rd_loss_record.stddev
        return torch.abs((rd_losses - mean) / std)


# ─────────────────────────────────────────────────────────────────────────────
# 5. SEMAModules: Layer-wise Expandable Container
# ─────────────────────────────────────────────────────────────────────────────

class SEMAModules(nn.Module):
    """
    Layer-wise container managing all AdapterModules and the expandable router
    for a single transformer block.

    Self-expansion logic (Sec 3.6):
    - Expansion fires when: all adapters' mean z_score > exp_threshold,
      and not already added_for_task, and detecting_outlier=True.
    - At most one adapter added per layer per task.
    - After expansion: adapter + RD trained; then frozen.
    - Router is expanded: only new column is trainable; old columns frozen.

    Equation (3): x^l_out = MLP(x^l) + Σ_k w_k * f_{φ_k^l}(x^l)

    Args:
        d_model: ViT hidden dimension (768).
        bottleneck: Adapter bottleneck dim (16).
        rd_dim: RD bottleneck dim (128).
        exp_threshold: Z-score threshold τ for expansion signal.
        buffer_size: Sliding window size (500).
        layer_id: 0-indexed transformer block id.
        adapt_start_layer: First layer eligible for expansion (9 by default).
        adapt_end_layer: Last layer eligible for expansion (11 by default).
    """
    def __init__(self, d_model: int = 768, bottleneck: int = 16, rd_dim: int = 128,
                 exp_threshold: float = 2.0, buffer_size: int = 500,
                 layer_id: int = 0, adapt_start_layer: int = 9, adapt_end_layer: int = 11):
        super().__init__()
        self.d_model = d_model
        self.exp_threshold = exp_threshold
        self.layer_id = layer_id
        self.adapt_start_layer = adapt_start_layer
        self.adapt_end_layer = adapt_end_layer
        self.is_expansion_layer = (adapt_start_layer <= layer_id <= adapt_end_layer)

        self.adapters: List[AdapterModule] = nn.ModuleList()
        self.newly_added: bool = True
        self.added_for_task: bool = True
        self.detecting_outlier: bool = False

        # Initialize with one adapter
        self._add_adapter(bottleneck=bottleneck, rd_dim=rd_dim, buffer_size=buffer_size)

        # Router: Linear(d_model → K^l); starts with K^l=1
        self.router = nn.Linear(d_model, 1).to(device)
        self.new_router: nn.Linear = None  # temporary new column during expansion

    def _add_adapter(self, bottleneck: int = 16, rd_dim: int = 128, buffer_size: int = 500):
        """Add a new (functional adapter, RD) pair and prepare new router column."""
        new_adapter = AdapterModule(
            d_model=self.d_model, bottleneck=bottleneck, rd_dim=rd_dim,
            buffer_size=buffer_size, is_expansion_layer=self.is_expansion_layer
        ).to(device)
        self.adapters.append(new_adapter)
        self.newly_added = True
        self.added_for_task = True
        if len(self.adapters) > 1:
            # Prepare new router column (trained separately)
            self.new_router = nn.Linear(self.d_model, 1).to(device)
        logging.info(f"Adapter added at layer {self.layer_id} (total: {len(self.adapters)})")

    def _merge_router(self):
        """Merge new_router column into main router; freeze all existing columns."""
        if self.new_router is None:
            return
        K = len(self.adapters)
        merged_router = nn.Linear(self.d_model, K).to(device)
        # Concatenate old and new weight/bias along output dim
        old_w = self.router.weight.data       # [K-1, d_model]
        new_w = self.new_router.weight.data   # [1, d_model]
        merged_router.weight = nn.Parameter(torch.cat([old_w, new_w], dim=0))
        old_b = self.router.bias.data
        new_b = self.new_router.bias.data
        merged_router.bias = nn.Parameter(torch.cat([old_b, new_b], dim=0))
        self.router = merged_router
        self.new_router = None

    def forward(self, x: torch.Tensor) -> dict:
        """
        Args:
            x: [B, S, d_model] — post-norm2 features (before MLP in parallel config)
        Returns:
            dict with keys: func_out [B, S, d_model], rd_loss (scalar), added (bool)
        """
        if not self.is_expansion_layer:
            # Non-expansion layer: use only the last (single) adapter, no z-score check
            func_out, _, _ = self.adapters[-1](x)
            return {"func_out": func_out, "rd_loss": torch.tensor(0.).to(device), "added": False}

        func_outs, rd_losses, z_scores = [], [], []
        for adapter in self.adapters:
            fo, rdl, zs = adapter(x)
            func_outs.append(fo)      # [B, S, d_model]
            rd_losses.append(rdl)     # [B]
            z_scores.append(zs)       # [B]

        # z_scores: list of K tensors, each [B]
        # Expansion criterion: mean z-score over batch for each adapter, then min over adapters
        z_tensor = torch.stack(z_scores)           # [K, B]
        min_mean_z = z_tensor.mean(dim=1).min()    # scalar: most "familiar" adapter's mean z

        expansion_criteria = (
            min_mean_z > self.exp_threshold and
            not self.added_for_task and
            self.detecting_outlier
        )

        if expansion_criteria:
            self._add_adapter()
            return {"func_out": torch.zeros_like(func_outs[0]), "rd_loss": torch.tensor(0.).to(device), "added": True}

        # Compute router weights
        logits = self.router(x.mean(dim=1))                # [B, K]
        if self.new_router is not None:
            new_logits = self.new_router(x.mean(dim=1))   # [B, 1]
            logits = torch.cat([logits, new_logits], dim=1)  # [B, K+1]
        weights = torch.softmax(logits, dim=1)              # [B, K]

        # Weighted sum of adapter outputs
        func_outs_stacked = torch.stack(func_outs)          # [K, B, S, d_model]
        weights_expanded = weights.T.unsqueeze(-1).unsqueeze(-1)  # [K, B, 1, 1]
        func_out = (func_outs_stacked * weights_expanded).sum(dim=0)  # [B, S, d_model]

        # RD loss: only for the newest adapter (if newly added this task)
        rd_loss = rd_losses[-1].mean() if self.adapters[-1].newly_added else torch.tensor(0.).to(device)

        return {"func_out": func_out, "rd_loss": rd_loss, "added": False}

    def end_of_task_training(self):
        """Freeze all adapters and RDs; merge router; reset state for next task."""
        self._freeze_all_functional()
        self._freeze_all_rds()
        self._merge_router()
        self._freeze_router()
        self._reset_newly_added()
        self.added_for_task = False

    def _freeze_all_functional(self):
        for adapter in self.adapters:
            for p in adapter.functional.parameters():
                p.requires_grad_(False)
                p._grad = None

    def _freeze_all_rds(self):
        for adapter in self.adapters:
            if adapter.rd is not None:
                for p in adapter.rd.parameters():
                    p.requires_grad_(False)
                    p._grad = None
                adapter.rd_loss_record.updating = False

    def _freeze_router(self):
        for p in self.router.parameters():
            p.requires_grad_(False)
            p._grad = None

    def _reset_newly_added(self):
        self.newly_added = False
        for adapter in self.adapters:
            adapter.newly_added = False
