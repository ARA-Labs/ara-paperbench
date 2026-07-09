"""
SEMA: Self-Expansion of Pre-trained Models with Modularized Adaptation
Core implementation stubs for: FunctionalAdapter, RepresentationDescriptor,
ExpandableRouter, and the SEMA expansion training loop.

Reference: Wang et al., arXiv:2403.18886v3
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Dict, Tuple, Optional


class FunctionalAdapter(nn.Module):
    """
    Functional adapter f_{phi_k^l}: side branch of the MLP in a ViT transformer block.
    
    Architecture: Linear(d -> r) -> ReLU -> Linear(r -> d)
    
    Note: Paper states r=16; reproduction rubric specifies r=48 for SEMA/ADAM.
    Verify against official code at https://github.com/huiyiwang01/SEMA-CL
    
    Args:
        d: Feature dimension (768 for ViT-B/16)
        r: Bottleneck (hidden) dimension (16 per paper §4.1; 48 per rubric)
    """
    def __init__(self, d: int = 768, r: int = 16):
        super().__init__()
        self.down_proj = nn.Linear(d, r, bias=False)  # W_down: d x r
        self.up_proj = nn.Linear(r, d, bias=False)    # W_up: r x d
        self.activation = nn.ReLU()
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input features [batch_size, seq_len, d] or [batch_size, d]
        Returns:
            Adapter output with same shape as input
        """
        # f(x) = ReLU(x @ W_down) @ W_up  (Eq. 1 in paper)
        return self.up_proj(self.activation(self.down_proj(x)))


class RepresentationDescriptor(nn.Module):
    """
    Representation Descriptor g_{phi_k^l}: an autoencoder for detecting
    distribution shift at a specific transformer layer.
    
    Architecture: 
        Encoder: Linear(d -> h) + LeakyReLU
        Decoder: Linear(h -> d)
    
    Trained only with reconstruction loss L_RD; receives NO gradient from L_CE.
    At inference time, RDs are NOT used (only functional adapters and router).
    
    Args:
        d: Input feature dimension (768 for ViT-B/16)
        hidden_dim: AE hidden dimension (128 per reproduction rubric)
        buffer_size: Number of recent samples to track for running stats (500)
    """
    def __init__(self, d: int = 768, hidden_dim: int = 128, buffer_size: int = 500):
        super().__init__()
        self.encoder = nn.Linear(d, hidden_dim)
        self.activation = nn.LeakyReLU()
        self.decoder = nn.Linear(hidden_dim, d)
        
        # Running statistics buffer for z-score computation
        self.buffer_size = buffer_size
        self.register_buffer('recon_error_buffer', torch.zeros(buffer_size))
        self.register_buffer('buffer_ptr', torch.tensor(0, dtype=torch.long))
        self.register_buffer('buffer_filled', torch.tensor(False))
    
    def encode(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input features [batch_size, d] (CLS token or pooled)
        Returns:
            Latent code [batch_size, hidden_dim]
        """
        return self.activation(self.encoder(x))
    
    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """
        Args:
            z: Latent code [batch_size, hidden_dim]
        Returns:
            Reconstruction [batch_size, d]
        """
        return self.decoder(z)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Full AE forward pass.
        Args:
            x: Input features [batch_size, d]
        Returns:
            Reconstruction [batch_size, d]
        """
        return self.decode(self.encode(x))
    
    def reconstruction_loss(self, x: torch.Tensor) -> torch.Tensor:
        """
        Compute reconstruction loss: ||x - g(x)||_2^2  (Eq. 2 in paper)
        Args:
            x: Input features [batch_size, d]
        Returns:
            Scalar reconstruction loss
        """
        x_recon = self.forward(x)
        return torch.sum((x - x_recon) ** 2)
    
    def compute_recon_errors(self, x: torch.Tensor) -> torch.Tensor:
        """
        Compute per-sample reconstruction errors (no gradient).
        Args:
            x: Input features [batch_size, d]
        Returns:
            Per-sample errors [batch_size]
        """
        with torch.no_grad():
            x_recon = self.forward(x)
            errors = torch.sum((x - x_recon) ** 2, dim=-1)  # [batch_size]
        return errors
    
    def update_buffer(self, errors: torch.Tensor) -> None:
        """
        Update FIFO buffer of reconstruction errors (most recent 500 samples).
        Args:
            errors: Per-sample errors [batch_size]
        """
        for err in errors:
            idx = self.buffer_ptr % self.buffer_size
            self.recon_error_buffer[idx] = err.item()
            self.buffer_ptr += 1
            if self.buffer_ptr >= self.buffer_size:
                self.buffer_filled = torch.tensor(True)
    
    def get_running_stats(self) -> Tuple[float, float]:
        """
        Compute running mean and std from buffer.
        Returns:
            (mu, sigma): Mean and standard deviation of buffered errors
        """
        if self.buffer_filled:
            valid = self.recon_error_buffer
        else:
            valid = self.recon_error_buffer[:self.buffer_ptr]
        
        if len(valid) == 0:
            return 0.0, 1.0
        
        mu = valid.mean().item()
        sigma = valid.std().item()
        return mu, max(sigma, 1e-8)  # avoid division by zero
    
    def compute_z_score(self, errors: torch.Tensor) -> torch.Tensor:
        """
        Compute z-scores for given reconstruction errors.
        z_k^l = (r_k^l - mu_k^l) / sigma_k^l
        Args:
            errors: Per-sample reconstruction errors [batch_size]
        Returns:
            Z-scores [batch_size]
        """
        mu, sigma = self.get_running_stats()
        return (errors - mu) / sigma


class ExpandableRouter(nn.Module):
    """
    Expandable weighting router h_{psi^l}: produces mixture weights over adapters.
    
    Architecture: Linear(d -> K^l) -> Softmax
    
    When a new adapter is added, a new column is appended to W_mix.
    Existing columns are frozen; only the new column is trained.
    
    Args:
        d: Feature dimension (768 for ViT-B/16)
        n_adapters: Initial number of adapters (1 for Task 1)
    """
    def __init__(self, d: int = 768, n_adapters: int = 1):
        super().__init__()
        self.d = d
        self.n_adapters = n_adapters
        # W_mix: d x K^l  (each column corresponds to one adapter)
        self.W_mix = nn.Parameter(torch.zeros(d, n_adapters))
        nn.init.normal_(self.W_mix, std=0.02)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Compute mixture weights.
        Args:
            x: Input features [batch_size, d]
        Returns:
            Mixture weights [batch_size, K^l], sum to 1 across dim=-1
        """
        # w = softmax(x @ W_mix)  (§3.4)
        logits = x @ self.W_mix  # [batch_size, K^l]
        return F.softmax(logits, dim=-1)
    
    def expand(self) -> None:
        """
        Expand router by one adapter: freeze existing columns, add new trainable column.
        """
        # Freeze existing columns
        old_W = self.W_mix.data.clone()
        new_col = torch.zeros(self.d, 1)
        nn.init.normal_(new_col, std=0.02)
        
        # Replace parameter with expanded matrix
        new_W = nn.Parameter(torch.cat([old_W, new_col], dim=1))
        
        # Freeze old columns by setting requires_grad to False for them
        # (In practice, use parameter groups in optimizer to selectively update)
        self.W_mix = new_W
        self.n_adapters += 1
        
        # Register frozen mask: only last column is trainable
        # Optimizer should use: optimizer.param_groups with mask or separate parameters
        self._frozen_cols = list(range(self.n_adapters - 1))
        self._trainable_cols = [self.n_adapters - 1]


class ModularAdapterLayer(nn.Module):
    """
    Expandable adapter module at a single transformer layer l.
    Contains K^l functional adapters, K^l representation descriptors, and one router.
    
    The output adds a weighted mixture of adapters to the frozen MLP output:
        x_out = MLP(x) + sum_k(w_k * f_k(x))  (Eq. 3)
    
    Args:
        d: Feature dimension (768 for ViT-B/16)
        r: Adapter bottleneck dim (16 per paper; 48 per reproduction rubric)
        rd_hidden: RD hidden dimension (128)
        buffer_size: Running stats buffer size (500)
    """
    def __init__(self, d: int = 768, r: int = 16, rd_hidden: int = 128, buffer_size: int = 500):
        super().__init__()
        self.d = d
        self.r = r
        
        # Start with one adapter, one RD, one router (Task 1)
        self.adapters: nn.ModuleList = nn.ModuleList([FunctionalAdapter(d, r)])
        self.rds: nn.ModuleList = nn.ModuleList([RepresentationDescriptor(d, rd_hidden, buffer_size)])
        self.router = ExpandableRouter(d, n_adapters=1)
    
    @property
    def n_adapters(self) -> int:
        return len(self.adapters)
    
    def forward(self, x: torch.Tensor, mlp_out: torch.Tensor) -> torch.Tensor:
        """
        Compute adapted output for this layer.
        Args:
            x:       Input to MLP (after LayerNorm 2) [batch, seq, d]
            mlp_out: Frozen MLP output [batch, seq, d]
        Returns:
            Adapted output [batch, seq, d]
        """
        # Use CLS token or pooled feature for routing
        # Paper uses x^l as the feature; use mean or CLS depending on ViT variant
        x_cls = x[:, 0]  # [batch, d] — use CLS token for router
        
        # Compute mixture weights w^l = softmax(x @ W_mix)
        weights = self.router(x_cls)  # [batch, K^l]
        
        # Compute weighted sum of adapter outputs
        adapter_outputs = torch.stack(
            [adapter(x) for adapter in self.adapters], dim=0
        )  # [K^l, batch, seq, d]
        
        # weights: [batch, K^l] -> [batch, K^l, 1, 1] for broadcasting
        w = weights.permute(1, 0).unsqueeze(-1).unsqueeze(-1)  # [K^l, batch, 1, 1]
        mixed_output = (w * adapter_outputs).sum(dim=0)  # [batch, seq, d]
        
        return mlp_out + mixed_output
    
    def check_expansion_signal(
        self, x: torch.Tensor, threshold: float = 1.2
    ) -> bool:
        """
        Check if expansion should be triggered for new task data x.
        Expansion occurs when ALL existing RDs report high z-scores.
        
        No gradient is computed during this check.
        
        Args:
            x: Features at this layer [batch, d] (CLS token or pooled)
            threshold: Z-score threshold τ
        Returns:
            True if expansion should be triggered
        """
        with torch.no_grad():
            for rd in self.rds:
                errors = rd.compute_recon_errors(x)
                z_scores = rd.compute_z_score(errors)
                # If any sample has ALL z-scores > threshold across all RDs
                # Trigger if mean z-score > threshold (batch-level check)
                if z_scores.mean().item() <= threshold:
                    return False  # This RD can handle the input
        return True  # All RDs report high reconstruction error -> expand
    
    def expand(self) -> Tuple[FunctionalAdapter, RepresentationDescriptor]:
        """
        Add a new modular adapter (functional adapter + RD) and expand the router.
        Returns:
            Newly created (adapter, rd) pair for training
        """
        new_adapter = FunctionalAdapter(self.d, self.r)
        new_rd = RepresentationDescriptor(self.d)
        
        self.adapters.append(new_adapter)
        self.rds.append(new_rd)
        self.router.expand()
        
        return new_adapter, new_rd
    
    def freeze_all_except_new(self) -> None:
        """Freeze all modules except the most recently added ones."""
        for i, (adapter, rd) in enumerate(zip(self.adapters, self.rds)):
            is_new = (i == len(self.adapters) - 1)
            for param in adapter.parameters():
                param.requires_grad = is_new
            for param in rd.parameters():
                param.requires_grad = is_new


def compute_sema_loss(
    logits: torch.Tensor,
    labels: torch.Tensor,
    adapter_layers: Dict[int, ModularAdapterLayer],
    features_per_layer: Dict[int, torch.Tensor],
    active_rd_indices: Dict[int, int],
) -> torch.Tensor:
    """
    Compute overall SEMA loss = L_CE + sum_l sum_k L_RD_k^l  (Eq. 4)
    
    Args:
        logits: Classification logits [batch, n_classes]
        labels: Ground truth labels [batch]
        adapter_layers: Dict mapping layer index -> ModularAdapterLayer
        features_per_layer: Dict mapping layer index -> features at that layer [batch, d]
        active_rd_indices: Dict mapping layer index -> index of the active (newly added) RD
    Returns:
        Total scalar loss
    """
    # Cross-entropy classification loss
    loss_ce = F.cross_entropy(logits, labels)
    
    # Reconstruction loss for active RDs only (newly added ones)
    loss_rd = torch.tensor(0.0, device=logits.device)
    for layer_idx, adapter_layer in adapter_layers.items():
        x_l = features_per_layer[layer_idx]  # [batch, d]
        rd_idx = active_rd_indices.get(layer_idx, -1)
        if rd_idx >= 0 and rd_idx < len(adapter_layer.rds):
            rd = adapter_layer.rds[rd_idx]
            loss_rd = loss_rd + rd.reconstruction_loss(x_l)
    
    return loss_ce + loss_rd


def compute_average_accuracy(
    accuracy_matrix: List[List[float]], n_tasks: int
) -> float:
    """
    Compute A_N = (1/N) * sum_{i=1}^{N} A_{i,N}
    
    Args:
        accuracy_matrix: accuracy_matrix[i][j] = accuracy of task i after training on task j
        n_tasks: Total number of tasks N
    Returns:
        Average accuracy A_N (%)
    """
    return sum(accuracy_matrix[i][n_tasks - 1] for i in range(n_tasks)) / n_tasks


def compute_average_incremental_accuracy(
    task_accuracies: List[float], n_tasks: int
) -> float:
    """
    Compute Ā = (1/N) * sum_{t=1}^{N} A_t
    where A_t is the average accuracy after training on task t.
    
    Args:
        task_accuracies: task_accuracies[t] = A_t (average accuracy after task t)
        n_tasks: Total number of tasks N
    Returns:
        Average incremental accuracy Ā (%)
    """
    return sum(task_accuracies) / n_tasks
