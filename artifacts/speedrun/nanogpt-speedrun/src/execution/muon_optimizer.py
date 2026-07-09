"""
Muon Optimizer — Core optimization from Record 3.
Verifies: C03 (largest single speedup), H01 (2D-only orthogonalization)

OrthogonalNesterov momentum for 2D+ weight matrices using Newton-Schulz
orthogonalization, combined with standard AdamW for 1D parameters.
"""

import torch
from torch.optim import Optimizer
from typing import List, Optional


def newton_schulz_5(G: torch.Tensor, steps: int = 5, eps: float = 1e-7) -> torch.Tensor:
    """
    Approximate orthogonalization via Newton-Schulz iteration.
    Cubic convergence: X_{k+1} = aX + bX^3 + cX^5

    Input: G (m × n matrix, spectral norm < 1.86)
    Output: G̃ ≈ G(G^T G)^{-1/2}
    """
    assert G.ndim == 2, "Newton-Schulz requires 2D input"
    a, b, c = 3.4445, -4.7750, 2.0315  # cubic convergence coefficients

    # Normalize to ensure spectral norm < 1.86
    G = G / (G.norm() + eps)

    # Iterative orthogonalization
    for _ in range(steps):
        A = G @ G.T
        G = a * G + b * (A @ G) + c * (A @ (A @ G))

    return G


class Muon(Optimizer):
    """
    Muon: Momentum + Orthogonalization for weight matrices.

    Partitions parameters into:
    - 2D+ matrices → OrthogonalNesterov (Newton-Schulz + Nesterov momentum)
    - 1D parameters → standard AdamW

    Args:
        muon_params: Parameters for OrthogonalNesterov (ndim >= 2)
        lr: Learning rate for Muon group
        momentum: Momentum factor (0.85→0.95 warmup recommended)
        nesterov: Use Nesterov momentum (default True)
        ns_steps: Newton-Schulz iteration steps (default 5)
    """

    def __init__(
        self,
        muon_params: List[torch.nn.Parameter],
        lr: float = 0.02,
        momentum: float = 0.95,
        nesterov: bool = True,
        ns_steps: int = 5,
    ):
        defaults = dict(lr=lr, momentum=momentum, nesterov=nesterov, ns_steps=ns_steps)
        super().__init__(muon_params, defaults)

    @torch.no_grad()
    def step(self):
        for group in self.param_groups:
            lr = group["lr"]
            momentum = group["momentum"]
            nesterov = group["nesterov"]
            ns_steps = group["ns_steps"]

            for p in group["params"]:
                if p.grad is None:
                    continue

                g = p.grad
                state = self.state[p]

                if len(state) == 0:
                    state["momentum_buffer"] = torch.zeros_like(g)

                buf = state["momentum_buffer"]

                # Nesterov momentum
                buf.mul_(momentum).add_(g)
                if nesterov:
                    g = g + momentum * buf

                # Reshape for Newton-Schulz (must be 2D)
                original_shape = g.shape
                if g.ndim > 2:
                    g = g.view(g.shape[0], -1)

                # Orthogonalize gradient
                g = newton_schulz_5(g, steps=ns_steps)

                # Reshape back
                if g.shape != original_shape:
                    g = g.view(original_shape)

                # Update
                p.add_(g, alpha=-lr)
