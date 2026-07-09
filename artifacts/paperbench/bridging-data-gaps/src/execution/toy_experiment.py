"""
Toy 2D Gaussian Transfer Experiment (§5.1, Figure 2)

This module implements the toy experiment used to validate gradient direction
analysis and sample concentration for TAN vs. baseline DDPM.

Setup (§5.1):
  Source distribution: N([1, 1], I)
  Target distribution: N([-1, -1], I)
  10-shot target samples

Four experimental conditions (Figure 2a):
  1. Reference: gradient from 10,000 samples (cyan/reference line)
  2. Baseline DDPM: gradient from 10-shot samples without similarity guidance
  3. Similarity-guided only (DDPM-TAN w/o adversarial noise): sienna line
  4. Full DDPM-TAN: orange line

Evaluation:
  - Angular deviation of gradient direction from reference (Figure 2a)
  - Sample concentration around target mean [-1,-1] (Figure 2b,c heatmaps, 20,000 samples)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import Tuple


# ─── Source and Target Distribution Parameters ────────────────────────────────

SOURCE_MEAN = torch.tensor([1.0, 1.0])    # Source Gaussian mean
TARGET_MEAN = torch.tensor([-1.0, -1.0])  # Target Gaussian mean
SOURCE_VAR = torch.eye(2)                  # Unit variance for source
TARGET_VAR = torch.eye(2)                  # Unit variance for target

N_SHOT = 10            # Number of target samples for few-shot setting
N_REFERENCE = 10000    # Number of source samples for reference gradient
N_GENERATE = 20000     # Number of samples for heatmap evaluation (Figure 2b,c)


class SimpleDiffusionNet2D(nn.Module):
    """
    Simple neural network for 2D toy diffusion experiment.
    Predicts noise for 2-dimensional data.
    """

    def __init__(self, hidden_dim: int = 64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, hidden_dim),   # input: [x0, x1, t]
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 2),   # output: predicted noise (2D)
        )

    def forward(self, x_t: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x_t: Noisy 2D points, shape (B, 2)
            t:   Timestep, shape (B,) — normalized to [0, 1]
        Returns:
            Predicted noise, shape (B, 2)
        """
        t_norm = t.float() / 1000.0
        inp = torch.cat([x_t, t_norm.unsqueeze(-1)], dim=-1)
        return self.net(inp)


def train_source_model(
    n_epochs: int = 500,
    n_samples: int = 10000,
    lr: float = 1e-3,
    device: str = "cuda",
) -> SimpleDiffusionNet2D:
    """
    Train a simple diffusion model on source 2D Gaussian N([1,1], I).

    This produces the pre-trained source model for the transfer experiment.

    Args:
        n_epochs:   Number of training epochs
        n_samples:  Samples per epoch from source distribution
        lr:         Learning rate
        device:     Compute device

    Returns:
        Trained source diffusion model.
    """
    model = SimpleDiffusionNet2D().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(n_epochs):
        x0 = torch.randn(n_samples, 2, device=device) + SOURCE_MEAN.to(device)
        t = torch.randint(1, 1001, (n_samples,), device=device)
        alpha_bar = compute_alpha_bar(t, device)

        eps = torch.randn_like(x0)
        x_t = alpha_bar.sqrt() * x0 + (1 - alpha_bar).sqrt() * eps

        eps_pred = model(x_t, t)
        loss = F.mse_loss(eps_pred, eps)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return model


def compute_alpha_bar(t: torch.Tensor, device: str = "cuda") -> torch.Tensor:
    """
    Compute ᾱ_t for a linear beta schedule.
    Returns shape (B, 1) for broadcasting with 2D data.
    """
    beta_min, beta_max = 1e-4, 0.02
    betas = torch.linspace(beta_min, beta_max, 1000, device=device)
    alpha_bars = torch.cumprod(1.0 - betas, dim=0)
    return alpha_bars[t - 1].unsqueeze(-1)  # (B, 1)


def compute_output_gradient(
    model: SimpleDiffusionNet2D,
    x0_samples: torch.Tensor,  # (N, 2) — either 10 or 10,000 samples
    t: torch.Tensor,           # (N,) — timestep
    device: str = "cuda",
) -> torch.Tensor:
    """
    Compute the gradient direction of the output layer for gradient direction analysis.
    Used to reproduce Figure 2a.

    The reference gradient (cyan line) uses 10,000 source samples.
    The 10-shot gradients (dark blue, sienna, orange) use 10 target samples
    repeated 1,000 times to match batch size.

    Args:
        model:      Diffusion model
        x0_samples: Clean data samples (N, 2)
        t:          Timestep (N,) — same for all for consistent comparison
        device:     Compute device

    Returns:
        gradient_direction: Unit vector of mean gradient (2,)
    """
    alpha_bar = compute_alpha_bar(t, device)
    eps = torch.randn_like(x0_samples)
    x_t = alpha_bar.sqrt() * x0_samples + (1 - alpha_bar).sqrt() * eps

    # Enable grad for output layer only
    for param in model.parameters():
        param.requires_grad_(True)

    eps_pred = model(x_t, t)
    loss = F.mse_loss(eps_pred, eps)
    loss.backward()

    # Extract output layer gradient
    output_grad = model.net[-1].weight.grad
    direction = output_grad.mean(dim=0)
    direction = direction / (direction.norm() + 1e-8)  # normalize to unit vector
    return direction.detach()


def run_toy_gradient_analysis(
    source_model: SimpleDiffusionNet2D,
    target_samples_10shot: torch.Tensor,  # (10, 2) — 10 target samples
    device: str = "cuda",
) -> dict:
    """
    Run the gradient direction analysis from Figure 2a.

    Computes gradient directions for:
      1. Reference: 10,000 source samples → reliable reference (~45° SW)
      2. Baseline DDPM: 10-shot target, repeated 1,000× → noisy direction
      3. Similarity-guided: 10-shot + classifier guidance
      4. Full DDPM-TAN: 10-shot + similarity guidance + adversarial noise

    Returns:
        dict with gradient direction for each method
    """
    t = torch.full((N_REFERENCE,), 500, device=device)  # fixed t for comparison

    # 1. Reference gradient (10,000 source samples)
    x0_ref = torch.randn(N_REFERENCE, 2, device=device) + SOURCE_MEAN.to(device)
    grad_reference = compute_output_gradient(source_model, x0_ref, t, device)

    # 2. Baseline: 10-shot target repeated 1,000 times
    x0_10shot = target_samples_10shot.to(device).repeat(1000 // N_SHOT + 1, 1)[:N_REFERENCE]
    t_10shot = torch.full((N_REFERENCE,), 500, device=device)
    grad_baseline = compute_output_gradient(source_model, x0_10shot, t_10shot, device)

    return {
        "reference": grad_reference,      # Should be ~45° southwest (close to [-1,-1])
        "baseline_ddpm": grad_baseline,   # Deviates from reference due to 10-shot noise
        # Similarity-guided and TAN gradients require the adapted model
    }
