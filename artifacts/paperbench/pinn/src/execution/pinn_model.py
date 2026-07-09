"""
PINN Model: MLP + loss function + training pipeline for Convection, Reaction, Wave PDEs.
Implements the core model from Rathore et al. 2024 (arXiv:2402.01868).
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Tuple, Dict, Optional


class PINN(nn.Module):
    """
    Multi-Layer Perceptron for Physics-Informed Neural Networks.
    
    Architecture: 3 hidden layers, equal width, tanh activations.
    Initialization: Xavier normal weights, zero biases.
    """
    
    def __init__(self, input_dim: int = 2, hidden_width: int = 100, output_dim: int = 1,
                 num_hidden: int = 3):
        """
        Args:
            input_dim: Number of input coordinates (2 for x,t)
            hidden_width: Width of each hidden layer (50, 100, 200, or 400)
            output_dim: Output dimension (1 for scalar u)
            num_hidden: Number of hidden layers (3 in paper)
        """
        super().__init__()
        layers = []
        dims = [input_dim] + [hidden_width] * num_hidden + [output_dim]
        for i in range(len(dims) - 1):
            layer = nn.Linear(dims[i], dims[i+1])
            # Xavier normal initialization
            nn.init.xavier_normal_(layer.weight)
            nn.init.zeros_(layer.bias)
            layers.append(layer)
            if i < len(dims) - 2:
                layers.append(nn.Tanh())
        self.net = nn.Sequential(*layers)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input tensor of shape (N, input_dim)
        Returns:
            u: Output tensor of shape (N, 1)
        """
        return self.net(x)


def convection_residual(model: PINN, x_r: torch.Tensor, beta: float = 40.0) -> torch.Tensor:
    """
    Compute PDE residual for convection: du/dt + beta * du/dx = 0.
    
    Args:
        model: PINN network
        x_r: Residual collocation points, shape (n_res, 2) = [(x, t), ...]
        beta: Convection coefficient (40 in paper)
    Returns:
        residual: Shape (n_res, 1)
    """
    x_r = x_r.requires_grad_(True)
    u = model(x_r)  # (n_res, 1)
    grads = torch.autograd.grad(u.sum(), x_r, create_graph=True)[0]  # (n_res, 2)
    du_dx = grads[:, 0:1]  # spatial derivative
    du_dt = grads[:, 1:2]  # time derivative
    return du_dt + beta * du_dx


def reaction_residual(model: PINN, x_r: torch.Tensor, rho: float = 5.0) -> torch.Tensor:
    """
    Compute ODE residual for reaction: du/dt - rho*u*(1-u) = 0.
    
    Args:
        model: PINN network
        x_r: Residual points, shape (n_res, 2)
        rho: Reaction rate coefficient (5 in paper)
    Returns:
        residual: Shape (n_res, 1)
    """
    x_r = x_r.requires_grad_(True)
    u = model(x_r)  # (n_res, 1)
    du_dt = torch.autograd.grad(u.sum(), x_r, create_graph=True)[0][:, 1:2]
    return du_dt - rho * u * (1.0 - u)


def wave_residual(model: PINN, x_r: torch.Tensor, wave_speed: float = 2.0) -> torch.Tensor:
    """
    Compute PDE residual for wave: d²u/dt² - c²*d²u/dx² = 0, c=2.
    
    Args:
        model: PINN network
        x_r: Residual points, shape (n_res, 2)
        wave_speed: wave speed c (sqrt(4)=2 for the 4*d²u/dx² term)
    Returns:
        residual: Shape (n_res, 1)
    """
    x_r = x_r.requires_grad_(True)
    u = model(x_r)
    grads1 = torch.autograd.grad(u.sum(), x_r, create_graph=True)[0]  # (n_res, 2)
    du_dx = grads1[:, 0:1]
    du_dt = grads1[:, 1:2]
    d2u_dx2 = torch.autograd.grad(du_dx.sum(), x_r, create_graph=True)[0][:, 0:1]
    d2u_dt2 = torch.autograd.grad(du_dt.sum(), x_r, create_graph=True)[0][:, 1:2]
    return d2u_dt2 - wave_speed**2 * d2u_dx2


def pinn_loss(
    model: PINN,
    x_res: torch.Tensor,   # (n_res, 2) interior residual points
    x_ic: torch.Tensor,    # (n_ic, 2) initial condition points (t=0)
    u_ic: torch.Tensor,    # (n_ic, 1) initial condition values
    x_bc: torch.Tensor,    # (n_bc, 2) boundary condition points
    u_bc: torch.Tensor,    # (n_bc, 1) boundary condition values (or same for periodic)
    residual_fn,           # callable: (model, x_r) -> residual
    return_components: bool = False
) -> torch.Tensor:
    """
    Compute PINN loss = (1/2n_res)||residual||^2 + (1/2n_bc)||BC violation||^2.
    
    Note: IC and BC are both included in the boundary term per the paper formulation.
    
    Args:
        model: PINN network
        x_res: Residual collocation points, shape (n_res, 2)
        x_ic: Initial condition points, shape (n_ic, 2)
        u_ic: Initial condition values, shape (n_ic, 1)
        x_bc: Boundary condition points, shape (n_bc, 2)
        u_bc: Boundary condition target values, shape (n_bc, 1)
        residual_fn: Function computing PDE residual
        return_components: If True, return dict of individual loss terms
    Returns:
        total_loss: Scalar tensor
    """
    res = residual_fn(model, x_res)
    L_res = 0.5 * (res ** 2).mean()
    
    u_ic_pred = model(x_ic)
    L_ic = 0.5 * ((u_ic_pred - u_ic) ** 2).mean()
    
    u_bc_pred = model(x_bc)
    L_bc = 0.5 * ((u_bc_pred - u_bc) ** 2).mean()
    
    total = L_res + L_ic + L_bc
    
    if return_components:
        return {'total': total, 'residual': L_res, 'ic': L_ic, 'bc': L_bc}
    return total


def l2_relative_error(u_pred: torch.Tensor, u_true: torch.Tensor) -> float:
    """
    Compute L2 Relative Error (L2RE) = ||u_pred - u_true||_2 / ||u_true||_2.
    
    Args:
        u_pred: Predicted solution, shape (N,) or (N, 1)
        u_true: Ground truth, shape (N,) or (N, 1)
    Returns:
        l2re: Scalar float
    """
    u_pred = u_pred.reshape(-1)
    u_true = u_true.reshape(-1)
    return (torch.norm(u_pred - u_true) / torch.norm(u_true)).item()


def sample_training_points(pde: str = 'convection') -> Dict[str, torch.Tensor]:
    """
    Sample training points as specified in Section 2.2.
    
    10000 residual points from 255x100 grid interior.
    257 equally-spaced IC points at t=0.
    101 equally-spaced BC points per boundary.
    
    Args:
        pde: 'convection', 'reaction', or 'wave'
    Returns:
        dict with keys: x_res, x_ic, u_ic, x_bc, u_bc
    """
    if pde in ['convection', 'reaction']:
        x_min, x_max = 0.0, 2 * np.pi
        t_min, t_max = 0.0, 1.0
    else:  # wave
        x_min, x_max = 0.0, 1.0
        t_min, t_max = 0.0, 1.0
    
    # Interior grid 255 x 100
    x_grid = np.linspace(x_min, x_max, 255, endpoint=False)[1:]  # exclude boundary
    t_grid = np.linspace(t_min, t_max, 100, endpoint=False)[1:]
    XX, TT = np.meshgrid(x_grid, t_grid)
    interior = np.stack([XX.ravel(), TT.ravel()], axis=1)
    
    # Sample 10000 points
    idx = np.random.choice(len(interior), size=10000, replace=False)
    x_res = torch.tensor(interior[idx], dtype=torch.float32)
    
    # IC: 257 equally-spaced x at t=0
    x_ic_pts = np.linspace(x_min, x_max, 257)
    x_ic = torch.tensor(np.stack([x_ic_pts, np.zeros(257)], axis=1), dtype=torch.float32)
    
    # IC values depend on PDE
    if pde == 'convection':
        u_ic = torch.tensor(np.sin(x_ic_pts).reshape(-1, 1), dtype=torch.float32)
    elif pde == 'reaction':
        h = np.exp(-(x_ic_pts - np.pi)**2 / (2 * (np.pi/4)**2))
        u_ic = torch.tensor(h.reshape(-1, 1), dtype=torch.float32)
    else:  # wave, beta=5
        beta = 5.0
        u_ic = torch.tensor((np.sin(np.pi * x_ic_pts) + 0.5 * np.sin(beta * np.pi * x_ic_pts)).reshape(-1, 1),
                            dtype=torch.float32)
    
    # BC: 101 equally-spaced t at x=x_min and x=x_max
    t_bc_pts = np.linspace(t_min, t_max, 101)
    
    if pde in ['convection', 'reaction']:
        # Periodic BC: u(0,t) = u(2pi, t)
        x_bc_left = np.stack([np.full(101, x_min), t_bc_pts], axis=1)
        x_bc_right = np.stack([np.full(101, x_max), t_bc_pts], axis=1)
        x_bc = torch.tensor(np.concatenate([x_bc_left, x_bc_right], axis=0), dtype=torch.float32)
        u_bc = None  # periodic BC handled separately in loss
    else:  # wave: Dirichlet u=0
        x_bc_left = np.stack([np.full(101, x_min), t_bc_pts], axis=1)
        x_bc_right = np.stack([np.full(101, x_max), t_bc_pts], axis=1)
        x_bc = torch.tensor(np.concatenate([x_bc_left, x_bc_right], axis=0), dtype=torch.float32)
        u_bc = torch.zeros(202, 1, dtype=torch.float32)
    
    return {'x_res': x_res, 'x_ic': x_ic, 'u_ic': u_ic, 'x_bc': x_bc, 'u_bc': u_bc}
