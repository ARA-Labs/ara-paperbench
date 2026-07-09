"""
PINN Training Module — Core PINN loss computation and Adam+L-BFGS pipeline.
Implements Section 2.1–2.2 of Rathore et al. (2024).
"""

import torch
import torch.nn as nn
from typing import Callable, Tuple, List, Optional


class MLP(nn.Module):
    """
    Multi-layer perceptron for PINN solution approximation.
    
    Architecture: input_dim → [width]*n_hidden → 1
    Activation: tanh between all hidden layers.
    Initialization: Xavier normal weights, zero biases.
    
    Args:
        input_dim: Spatial/temporal input dimension (e.g., 2 for (x,t))
        width: Number of neurons in each hidden layer (50, 100, 200, or 400)
        n_hidden: Number of hidden layers (3 in all paper experiments)
    """
    def __init__(self, input_dim: int, width: int, n_hidden: int = 3):
        super().__init__()
        layers = [nn.Linear(input_dim, width), nn.Tanh()]
        for _ in range(n_hidden - 1):
            layers += [nn.Linear(width, width), nn.Tanh()]
        layers += [nn.Linear(width, 1)]
        self.net = nn.Sequential(*layers)
        self._init_weights()
    
    def _init_weights(self):
        """Xavier normal initialization for weights; zeros for biases."""
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_normal_(m.weight)
                nn.init.zeros_(m.bias)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input coordinates, shape (N, input_dim)
        Returns:
            u: Predicted solution, shape (N, 1)
        """
        return self.net(x)


def compute_pinn_loss(
    model: MLP,
    x_res: torch.Tensor,           # (n_res, 2) residual collocation points (x, t)
    x_bc: torch.Tensor,            # (n_bc, 2) boundary/initial condition points
    residual_fn: Callable,         # D[u](x; w) → (n_res, 1) residual
    bc_fn: Callable,               # B[u](x; w) → (n_bc, 1) BC/IC residual
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Compute PINN loss: L(w) = (1/2n_res)‖D[u]‖² + (1/2n_bc)‖B[u]‖²
    
    Returns:
        total_loss: Scalar total PINN loss
        res_loss:   Residual component loss
        bc_loss:    Boundary/initial condition component loss
    """
    n_res = x_res.shape[0]
    n_bc = x_bc.shape[0]
    
    residual = residual_fn(model, x_res)          # (n_res, 1)
    bc_residual = bc_fn(model, x_bc)              # (n_bc, 1)
    
    res_loss = (1.0 / (2 * n_res)) * torch.sum(residual ** 2)
    bc_loss = (1.0 / (2 * n_bc)) * torch.sum(bc_residual ** 2)
    total_loss = res_loss + bc_loss
    
    return total_loss, res_loss, bc_loss


def sample_collocation_points(
    n_res: int,
    grid_shape: Tuple[int, int],   # (255, 100) for interior
    n_ic: int,                     # 257 equally spaced IC points
    n_bc_per_side: int,            # 101 equally spaced BC points per boundary
    domain_x: Tuple[float, float], # (x_min, x_max)
    domain_t: Tuple[float, float], # (t_min, t_max)
    device: torch.device,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Sample fixed collocation points for PINN training (sampled once, fixed throughout).
    
    n_res points randomly sampled from the interior grid (255×100 = 25500 points).
    BC/IC points equally spaced along boundaries and initial time.
    
    Returns:
        x_res: (n_res, 2) residual points (x, t)
        x_bc:  (n_ic + 2*n_bc_per_side, 2) boundary/initial condition points
    """
    # Build full interior grid
    nx, nt = grid_shape
    x_vals = torch.linspace(domain_x[0], domain_x[1], nx, device=device)
    t_vals = torch.linspace(domain_t[0], domain_t[1], nt, device=device)
    grid_x, grid_t = torch.meshgrid(x_vals, t_vals, indexing='ij')
    all_interior = torch.stack([grid_x.flatten(), grid_t.flatten()], dim=1)  # (nx*nt, 2)
    
    # Randomly sample n_res points from interior (without replacement)
    idx = torch.randperm(all_interior.shape[0], device=device)[:n_res]
    x_res = all_interior[idx]
    
    # Initial condition points (t=t_min, x equally spaced)
    x_ic = torch.linspace(domain_x[0], domain_x[1], n_ic, device=device)
    t_ic = torch.full((n_ic,), domain_t[0], device=device)
    pts_ic = torch.stack([x_ic, t_ic], dim=1)
    
    # Boundary condition points (x=x_min, t equally spaced)
    t_bc = torch.linspace(domain_t[0], domain_t[1], n_bc_per_side, device=device)
    x_left = torch.full((n_bc_per_side,), domain_x[0], device=device)
    x_right = torch.full((n_bc_per_side,), domain_x[1], device=device)
    pts_bc_left = torch.stack([x_left, t_bc], dim=1)
    pts_bc_right = torch.stack([x_right, t_bc], dim=1)
    
    x_bc = torch.cat([pts_ic, pts_bc_left, pts_bc_right], dim=0)
    return x_res, x_bc


def train_adam_lbfgs(
    model: MLP,
    x_res: torch.Tensor,
    x_bc: torch.Tensor,
    residual_fn: Callable,
    bc_fn: Callable,
    adam_lr: float,
    adam_steps: int,            # Number of Adam steps before switching
    total_steps: int,           # Total steps (Adam + L-BFGS); paper: 41000
    lbfgs_lr: float = 1.0,
    lbfgs_memory: int = 100,
    device: torch.device = torch.device('cuda'),
) -> Tuple[List[float], List[float]]:
    """
    Adam+L-BFGS training pipeline (Section 2.2).
    
    Phase 1: Adam optimizer for adam_steps iterations.
    Phase 2: L-BFGS with strong Wolfe line search for remaining iterations.
    
    Returns:
        losses: List of training losses at each step
        grad_norms: List of gradient norms at each step
    """
    losses, grad_norms = [], []
    
    # Phase 1: Adam
    adam_opt = torch.optim.Adam(model.parameters(), lr=adam_lr)
    for _ in range(adam_steps):
        adam_opt.zero_grad()
        loss, _, _ = compute_pinn_loss(model, x_res, x_bc, residual_fn, bc_fn)
        loss.backward()
        losses.append(loss.item())
        grad_norms.append(
            sum(p.grad.norm().item()**2 for p in model.parameters() if p.grad is not None)**0.5
        )
        adam_opt.step()
    
    # Phase 2: L-BFGS with strong Wolfe line search
    lbfgs_opt = torch.optim.LBFGS(
        model.parameters(),
        lr=lbfgs_lr,
        max_iter=1,
        history_size=lbfgs_memory,
        line_search_fn='strong_wolfe',
    )
    
    def closure():
        lbfgs_opt.zero_grad()
        loss, _, _ = compute_pinn_loss(model, x_res, x_bc, residual_fn, bc_fn)
        loss.backward()
        return loss
    
    for _ in range(total_steps - adam_steps):
        loss = lbfgs_opt.step(closure)
        losses.append(loss.item())
        grad_norms.append(
            sum(p.grad.norm().item()**2 for p in model.parameters() if p.grad is not None)**0.5
        )
    
    return losses, grad_norms


def compute_l2re(
    model: MLP,
    x_eval: torch.Tensor,    # (N, 2) evaluation points
    u_exact: torch.Tensor,   # (N,) exact solution values
) -> float:
    """
    Compute L2 relative error: ‖u_pred - u_exact‖₂ / ‖u_exact‖₂
    
    Evaluated on full 255×100 grid + IC + BC points as in Section 2.2.
    """
    with torch.no_grad():
        u_pred = model(x_eval).squeeze(-1)
    return (torch.norm(u_pred - u_exact) / torch.norm(u_exact)).item()
