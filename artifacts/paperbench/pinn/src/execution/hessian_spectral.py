"""
Hessian Spectral Density Estimation and L-BFGS Preconditioned Hessian.
Implements Sections 5.1–5.3 and Appendix C.2 of Rathore et al. (2024).
"""

import torch
from typing import Callable, Tuple, List, Optional


def compute_hvp(
    loss_fn: Callable[[], torch.Tensor],
    params: List[torch.Tensor],
    v_flat: torch.Tensor,   # (p,) vector for Hessian-vector product
) -> torch.Tensor:
    """
    Compute Hessian-vector product H_L(w) @ v via double backpropagation.
    Complexity: O((n_res + n_bc) * p).
    
    Returns:
        hvp: (p,) Hessian-vector product
    """
    loss = loss_fn()
    grads = torch.autograd.grad(loss, params, create_graph=True)
    grad_flat = torch.cat([g.flatten() for g in grads])
    
    v_list = v_flat.split([p.numel() for p in params])
    hvp = torch.autograd.grad(grad_flat, params, grad_outputs=v_list)
    return torch.cat([h.flatten() for h in hvp]).detach()


def unroll_lbfgs_update(
    saved_y: List[torch.Tensor],   # Saved gradient differences (y_i = ∇f_{k+1} - ∇f_k)
    saved_s: List[torch.Tensor],   # Saved iterate differences (s_i = w_{k+1} - w_k)
    saved_rho: List[float],        # Saved 1/(y_i^T s_i) scalars
    gamma_k: float,                # Initial Hessian scaling (y^T s / y^T y)
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Algorithm 2: Unroll L-BFGS update to form matrices Ỹ, Ṽ, S̃.
    
    Used to compute spectral density of preconditioned Hessian Ĥ_k^T H_L Ĥ_k
    as described in Appendix C.2.
    
    Returns:
        Y_tilde: (p, m) matrix
        V_tilde: (p, m) matrix
        S_tilde: (p, m) matrix
    """
    m = len(saved_s)
    p = saved_s[0].numel()
    device = saved_s[0].device
    
    Y_tilde = torch.zeros(p, m, device=device)
    V_tilde = torch.zeros(p, m, device=device)
    S_tilde = torch.zeros(p, m, device=device)
    
    # Most recent index is k-1 (index 0 in lists = most recent)
    for i in range(m):
        rho_i = saved_rho[i]
        y_i = saved_y[i]
        s_i = saved_s[i]
        
        Y_tilde[:, i] = rho_i * y_i
        
        # ṽ_i = s_i - Σ_{j=0}^{i-1} (ỹ_j^T s_i) ṽ_j
        v_i = s_i.clone()
        for j in range(i):
            v_i -= (Y_tilde[:, j] @ s_i) * V_tilde[:, j]
        V_tilde[:, i] = v_i
        
        # s̃_i = sqrt(rho_i) * (s_i - Σ_{j=0}^{i-1} (ỹ_j^T s_i) ṽ_j)
        S_tilde[:, i] = (rho_i ** 0.5) * v_i
    
    return Y_tilde, V_tilde, S_tilde


def preconditioned_hvp(
    H_L_hvp: Callable[[torch.Tensor], torch.Tensor],  # Raw HVP function
    Y_tilde: torch.Tensor,    # (p, m)
    V_tilde: torch.Tensor,    # (p, m)
    S_tilde: torch.Tensor,    # (p, m)
    gamma_k: float,
    v: torch.Tensor,          # (p + m,) input vector
    p: int,
    m: int,
) -> torch.Tensor:
    """
    Algorithm 3: Compute Ĥ_k^T H_L(w) Ĥ_k @ v.
    
    Used for SLQ spectral density estimation of the preconditioned Hessian.
    Split input v = [v1 (p,), v2 (m,)].
    
    Returns:
        result: (p + m,) output vector
    """
    v1 = v[:p]
    v2 = v[p:]
    
    # Step 1: v' = sqrt(γ_k) * (v1 - Ṽ Ỹ^T v1) + S̃ v2
    sqrt_gamma = gamma_k ** 0.5
    v_prime = sqrt_gamma * (v1 - V_tilde @ (Y_tilde.T @ v1)) + S_tilde @ v2
    
    # Step 2: v'' = H_L(w) @ v'
    v_double_prime = H_L_hvp(v_prime)
    
    # Step 3: result = [sqrt(γ_k)(v'' - Ỹ Ṽ^T v''), S̃^T v'']
    result_1 = sqrt_gamma * (v_double_prime - Y_tilde @ (V_tilde.T @ v_double_prime))
    result_2 = S_tilde.T @ v_double_prime
    
    return torch.cat([result_1, result_2])


def estimate_spectral_density_slq(
    matvec: Callable[[torch.Tensor], torch.Tensor],  # Matrix-vector product
    dim: int,                  # Matrix dimension
    n_vectors: int = 100,      # Number of random probe vectors
    n_lanczos: int = 100,      # Lanczos iterations
    device: torch.device = torch.device('cuda'),
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Estimate Hessian spectral density via Stochastic Lanczos Quadrature (SLQ).
    Compatible with PyHessian-style interface.
    
    Returns:
        eigenvalues: Estimated eigenvalues from all Lanczos runs
        weights: Corresponding Lanczos weights
    """
    all_eigenvalues = []
    all_weights = []
    
    for _ in range(n_vectors):
        # Random unit vector
        v = torch.randn(dim, device=device)
        v = v / v.norm()
        
        # Lanczos iteration
        V = torch.zeros(dim, n_lanczos + 1, device=device)
        T_diag = torch.zeros(n_lanczos, device=device)
        T_offdiag = torch.zeros(n_lanczos - 1, device=device)
        
        V[:, 0] = v
        w = matvec(v)
        alpha = torch.dot(w, v)
        T_diag[0] = alpha
        w = w - alpha * v
        
        for j in range(1, n_lanczos):
            beta = w.norm()
            if beta < 1e-10:
                break
            V[:, j] = w / beta
            T_offdiag[j - 1] = beta
            w = matvec(V[:, j])
            alpha = torch.dot(w, V[:, j])
            T_diag[j] = alpha
            w = w - alpha * V[:, j] - beta * V[:, j - 1]
        
        # Eigendecompose tridiagonal T
        T = torch.diag(T_diag) + torch.diag(T_offdiag, 1) + torch.diag(T_offdiag, -1)
        eigvals, eigvecs = torch.linalg.eigh(T)
        weights = eigvecs[0] ** 2  # First row squared
        
        all_eigenvalues.append(eigvals)
        all_weights.append(weights)
    
    return torch.cat(all_eigenvalues), torch.cat(all_weights)
