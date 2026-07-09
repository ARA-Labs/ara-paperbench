"""
Compute spectral density of L-BFGS preconditioned Hessian (Algorithms 2 & 3).
Implements Appendix C.2 of Rathore et al. 2024.
"""

import torch
import numpy as np
from typing import List, Tuple, Callable, Optional


def unroll_lbfgs_update(
    ys: List[torch.Tensor],   # stored y_i = grad_{i+1} - grad_i
    ss: List[torch.Tensor],   # stored s_i = w_{i+1} - w_i
    rhos: List[torch.Tensor], # stored rho_i = 1 / (y_i^T s_i)
    gamma: float,             # scaling factor for H_0
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Unroll L-BFGS update to form Ỹ, Ṡ, Ṽ matrices (Algorithm 2).
    
    Args:
        ys: List of m gradient difference vectors (most recent first)
        ss: List of m step vectors
        rhos: List of m inverse inner products
        gamma: Scaling for initial Hessian H_0 = gamma * I
    Returns:
        Y_tilde: Matrix columns = rho_i * y_i, shape (p, m)
        S_tilde: Matrix s̃ vectors, shape (p, m)
        V_tilde: Matrix ṽ vectors, shape (p, m)
    """
    m = len(ys)
    p = ys[0].numel()
    
    Y_tilde = torch.zeros(p, m)
    S_tilde = torch.zeros(p, m)
    V_tilde = torch.zeros(p, m)
    
    # Initialize most recent entry
    Y_tilde[:, 0] = rhos[0] * ys[0]
    V_tilde[:, 0] = ss[0]
    S_tilde[:, 0] = rhos[0].sqrt() * ss[0]
    
    # Build remaining columns
    for i in range(1, m):
        Y_tilde[:, i] = rhos[i] * ys[i]
        
        # Compute alpha = sum_{j < i} (ỹ_j^T s_i) ṽ_j
        alpha = torch.zeros(p)
        for j in range(i):
            alpha = alpha + (Y_tilde[:, j] @ ss[i]) * V_tilde[:, j]
        
        V_tilde[:, i] = ss[i] - alpha
        S_tilde[:, i] = rhos[i].sqrt() * V_tilde[:, i]
    
    return Y_tilde, S_tilde, V_tilde


def preconditioned_hessian_matvec(
    Y_tilde: torch.Tensor,  # (p, m)
    S_tilde: torch.Tensor,  # (p, m)
    V_tilde: torch.Tensor,  # (p, m)
    gamma: float,
    hessian_vec_prod: Callable[[torch.Tensor], torch.Tensor],
    v: torch.Tensor         # (p + m,) — extended vector for SLQ
) -> torch.Tensor:
    """
    Matrix-vector product with preconditioned Hessian H̃_k^T H_L H̃_k (Algorithm 3).
    
    The preconditioned matrix acts on extended vectors of size (p + m).
    
    Args:
        Y_tilde, S_tilde, V_tilde: From unroll_lbfgs_update
        gamma: L-BFGS initial Hessian scaling
        hessian_vec_prod: H_L(w) @ v
        v: Input vector of size (p + m,)
    Returns:
        result: Output vector of size (p + m,)
    """
    p = Y_tilde.shape[0]
    m = Y_tilde.shape[1]
    
    v1 = v[:p]    # (p,)
    v2 = v[p:]    # (m,)
    
    # H̃_k = sqrt(gamma) * (I - Ỹ Ṽ^T) extended by Ṡ
    # v' = sqrt(gamma) * (v1 - Ṽ Ỹ^T v1) + Ṡ v2
    v_prime = (gamma**0.5) * (v1 - V_tilde @ (Y_tilde.T @ v1)) + S_tilde @ v2
    
    # v'' = H_L v'
    v_pp = hessian_vec_prod(v_prime)
    
    # Stack: sqrt(gamma) * (v'' - Ỹ Ṽ^T v'') | Ṡ^T v''
    part1 = (gamma**0.5) * (v_pp - Y_tilde @ (V_tilde.T @ v_pp))
    part2 = S_tilde.T @ v_pp
    
    return torch.cat([part1, part2])


def compute_preconditioned_spectral_density(
    ys: List[torch.Tensor],
    ss: List[torch.Tensor],
    rhos: List[float],
    gamma: float,
    hessian_vec_prod: Callable[[torch.Tensor], torch.Tensor],
    p: int,
    num_slq_vectors: int = 10,
    num_lanczos_steps: int = 100
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Estimate spectral density of preconditioned Hessian via SLQ.
    
    Args:
        ys, ss, rhos: L-BFGS stored vectors (m most recent)
        gamma: L-BFGS scaling
        hessian_vec_prod: H_L(w) @ v function
        p: Parameter dimension
        num_slq_vectors: Number of random probe vectors for SLQ
        num_lanczos_steps: Lanczos iterations per probe
    Returns:
        eigenvalues: Estimated eigenvalue locations
        density: Estimated density at each eigenvalue
    """
    rho_tensors = [torch.tensor(r) for r in rhos]
    Y_tilde, S_tilde, V_tilde = unroll_lbfgs_update(ys, ss, rho_tensors, gamma)
    
    m = len(ys)
    extended_dim = p + m
    
    def matvec(v: torch.Tensor) -> torch.Tensor:
        return preconditioned_hessian_matvec(
            Y_tilde, S_tilde, V_tilde, gamma, hessian_vec_prod, v
        )
    
    # SLQ: compute spectral density using Lanczos with random probe vectors
    all_eigenvalues = []
    all_weights = []
    
    for _ in range(num_slq_vectors):
        q = torch.randn(extended_dim)
        q = q / q.norm()
        
        # Lanczos iteration
        alphas = []
        betas = []
        qs = [q]
        
        for j in range(num_lanczos_steps):
            z = matvec(qs[-1])
            alpha = (qs[-1] * z).sum().item()
            alphas.append(alpha)
            
            if j > 0:
                z = z - betas[-1] * qs[-2]
            z = z - alpha * qs[-1]
            
            beta = z.norm().item()
            betas.append(beta)
            
            if beta < 1e-10:
                break
            qs.append(z / beta)
        
        # Build tridiagonal matrix
        T = np.diag(alphas) + np.diag(betas[:-1], 1) + np.diag(betas[:-1], -1)
        evals, evecs = np.linalg.eigh(T)
        weights = evecs[0, :]**2
        
        all_eigenvalues.extend(evals.tolist())
        all_weights.extend(weights.tolist())
    
    return np.array(all_eigenvalues), np.array(all_weights)
