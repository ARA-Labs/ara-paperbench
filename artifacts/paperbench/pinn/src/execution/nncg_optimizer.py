"""
NysNewton-CG (NNCG) Optimizer — Algorithm 4 from Appendix E of Rathore et al. (2024).
Implements: RandomizedNystromApproximation (Alg. 5), NystromPCG (Alg. 6),
             Armijo line search (Alg. 7), and the main NNCG loop (Alg. 4).
"""

import torch
from typing import Callable, Tuple, List, Optional


def randomized_nystrom_approximation(
    hvp_fn: Callable[[torch.Tensor], torch.Tensor],  # Hessian-vector product function
    p: int,                # Number of model parameters
    s: int = 60,           # Sketch size (paper: s=60)
    device: torch.device = torch.device('cuda'),
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Algorithm 5: Randomized Nyström Approximation of the Hessian.
    
    Computes low-rank approximation H ≈ V̂ Λ̂ V̂^T where V̂ ∈ R^{p×s}, Λ̂ ∈ R^{s×s}.
    
    Args:
        hvp_fn: Function computing H @ v for given vector v (shape: p,)
        p: Total number of parameters
        s: Sketch size
        device: Computation device
    
    Returns:
        V_hat: (p, s) approximate eigenvectors
        Lambda_hat: (s,) approximate eigenvalues (non-negative)
    """
    # Generate test matrix Q = orth(S), S ~ N(0, I_p)
    S = torch.randn(p, s, device=device)
    Q, _ = torch.linalg.qr(S)  # (p, s) orthonormal columns
    
    # Compute sketch Y = H @ Q column by column
    Y = torch.stack([hvp_fn(Q[:, i]) for i in range(s)], dim=1)  # (p, s)
    
    # Compute shift for numerical stability: ν = √p * ε_mach * ‖Y‖_2
    nu = (p ** 0.5) * torch.finfo(Y.dtype).eps * torch.linalg.norm(Y, ord=2)
    Y_nu = Y + nu * Q  # (p, s)
    
    # Cholesky: C^T C = Q^T Y_nu, then B = Y_nu C^{-1}
    M_small = Q.T @ Y_nu  # (s, s) small matrix
    lam_shift = 0.0
    try:
        C = torch.linalg.cholesky(M_small)  # Lower triangular
        B = torch.linalg.solve_triangular(C.T, Y_nu.T, upper=True).T  # (p, s)
    except RuntimeError:
        # Fallback: eigendecomposition for indefinite case
        W, Gamma = torch.linalg.eigh(M_small)
        lam_shift = float(W.min().abs().item())
        R = W @ torch.diag(1.0 / (Gamma + lam_shift * torch.ones_like(Gamma)) ** 0.5) @ W.T
        B = Y_nu @ R
    
    # Thin SVD of B: B = V̂ Σ Ṽ^T
    V_hat, Sigma, _ = torch.linalg.svd(B, full_matrices=False)  # V_hat: (p, s)
    
    # Eigenvalues: Λ̂ = max(0, Σ² - (ν + |λ_shift|) · I)
    Lambda_hat = torch.clamp(Sigma ** 2 - (nu + lam_shift), min=0.0)
    
    return V_hat, Lambda_hat


def nystrom_pcg(
    hvp_fn: Callable[[torch.Tensor], torch.Tensor],  # Hessian-vector product
    grad: torch.Tensor,    # (p,) gradient = right-hand side b
    x0: torch.Tensor,      # (p,) initial guess
    V_hat: torch.Tensor,   # (p, s) Nyström eigenvectors
    Lambda_hat: torch.Tensor,  # (s,) Nyström eigenvalues
    s: int,
    mu: float,             # Damping parameter
    tol: float = 1e-16,
    max_iter: int = 1000,
) -> torch.Tensor:
    """
    Algorithm 6: NystromPCG — Solves (H + μI) x = b via preconditioned CG.
    
    Preconditioner: P^{-1} = ((λ̂_s + μ) / 1) V̂(Λ̂ + μI)^{-1}V̂^T + (I - V̂V̂^T)
    where λ̂_s = Lambda_hat[s-1] (smallest nonzero approximate eigenvalue).
    
    Args:
        hvp_fn: Computes H @ v
        grad: Right-hand side vector b = ∇L(w)
        x0: Initial guess (warm-started from previous Newton step)
        V_hat: (p, s) approximate eigenvectors from Nyström
        Lambda_hat: (s,) approximate eigenvalues
        mu: Damping parameter μ
        tol: CG convergence tolerance
        max_iter: Maximum CG iterations
    
    Returns:
        x: (p,) approximate solution to (H + μI)x = b
    """
    lambda_s = Lambda_hat[-1].item() if s > 0 else 0.0
    
    def precond_inv(v: torch.Tensor) -> torch.Tensor:
        """Apply P^{-1} to vector v."""
        # Component in Nyström subspace: (λ̂_s + μ) V̂(Λ̂ + μI)^{-1}V̂^T v
        alpha_coeffs = V_hat.T @ v                        # (s,)
        scaled = alpha_coeffs / (Lambda_hat + mu)          # (s,)
        nystrom_part = (lambda_s + mu) * (V_hat @ scaled) # (p,)
        # Component in orthogonal complement: (I - V̂V̂^T) v / 1 (identity scaling)
        ortho_part = v - V_hat @ (V_hat.T @ v)
        return nystrom_part + ortho_part
    
    def matvec_A(v: torch.Tensor) -> torch.Tensor:
        """Apply (H + μI) to vector v."""
        return hvp_fn(v) + mu * v
    
    # PCG iterations
    x = x0.clone()
    r = grad - matvec_A(x)
    z = precond_inv(r)
    p = z.clone()
    rz = torch.dot(r, z)
    
    for _ in range(max_iter):
        if torch.norm(r) < tol:
            break
        Ap = matvec_A(p)
        alpha = rz / torch.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        z = precond_inv(r)
        rz_new = torch.dot(r, z)
        beta = rz_new / rz
        p = z + beta * p
        rz = rz_new
    
    return x


def armijo_line_search(
    loss_fn: Callable[[], torch.Tensor],
    params: List[torch.Tensor],
    grad_flat: torch.Tensor,   # (p,) current gradient
    direction: torch.Tensor,   # (p,) search direction (Newton step; applied as -direction)
    eta: float = 1.0,          # Initial step size
    alpha: float = 0.1,        # Sufficient decrease parameter
    beta: float = 0.5,         # Backtracking factor
    max_backtracks: int = 50,
) -> float:
    """
    Algorithm 7: Armijo backtracking line search.
    
    Finds largest t ∈ {η, ηβ, ηβ², ...} such that:
        f(x - t*d) ≤ f(x) - α·t·(∇f(x)^T d)
    
    Args:
        loss_fn: Closure that returns current loss (no grad)
        params: List of parameter tensors
        grad_flat: Flattened current gradient
        direction: Newton step d (update is w ← w - t*d)
        eta: Initial step size
        alpha: Armijo sufficient decrease parameter (paper: 0.1)
        beta: Backtracking factor (paper: 0.5)
    
    Returns:
        t: Accepted step size
    """
    with torch.no_grad():
        f0 = loss_fn().item()
    
    # Gradient dot direction (should be positive for descent)
    gTd = torch.dot(grad_flat, direction).item()
    
    # Save current params
    orig_vals = [p.data.clone() for p in params]
    
    t = eta
    for _ in range(max_backtracks):
        # Apply step: w ← w - t * direction
        offset = 0
        for p in params:
            numel = p.numel()
            p.data = orig_vals[params.index(p)] - t * direction[offset:offset + numel].view(p.shape)
            offset += numel
        
        with torch.no_grad():
            f_new = loss_fn().item()
        
        if f_new <= f0 - alpha * t * gTd:
            break
        t *= beta
    else:
        # Restore original params if no decrease found
        for p, orig in zip(params, orig_vals):
            p.data = orig
        t = 0.0
    
    return t


def nncg_optimizer(
    model: torch.nn.Module,
    loss_fn: Callable[[], torch.Tensor],  # Returns scalar loss
    n_iterations: int = 2000,             # K in Algorithm 4 (paper: 2000)
    eta: float = 1.0,                     # Initial step size
    s: int = 60,                          # Nyström sketch size
    F: int = 20,                          # Preconditioner update frequency
    mu: float = 1e-2,                     # Damping parameter (tune from {1e-5,...,1e-1})
    cg_tol: float = 1e-16,               # CG convergence tolerance
    cg_max_iter: int = 1000,             # Maximum CG iterations
    armijo_alpha: float = 0.1,           # Armijo sufficient decrease
    armijo_beta: float = 0.5,            # Backtracking factor
    device: torch.device = torch.device('cuda'),
) -> Tuple[List[float], List[float]]:
    """
    Algorithm 4: NysNewton-CG (NNCG) optimizer.
    
    Applied after Adam+L-BFGS to overcome L-BFGS stalling.
    Uses Armijo line search (not strong Wolfe) to guarantee loss decrease.
    
    Returns:
        losses: Loss at each iteration
        grad_norms: Gradient norm at each iteration
    """
    params = list(model.parameters())
    p = sum(param.numel() for param in params)
    
    V_hat, Lambda_hat = None, None
    d_prev = torch.zeros(p, device=device)
    
    losses, grad_norms = [], []
    
    for k in range(n_iterations):
        # Compute loss and gradient
        for param in params:
            if param.grad is not None:
                param.grad.zero_()
        
        loss = loss_fn()
        loss.backward(create_graph=False)
        
        grad_flat = torch.cat([p.grad.flatten() for p in params])
        losses.append(loss.item())
        grad_norms.append(grad_flat.norm().item())
        
        # Update Nyström preconditioner every F iterations
        if k % F == 0:
            def hvp_fn(v: torch.Tensor) -> torch.Tensor:
                """Compute Hessian-vector product H @ v via double backprop."""
                # Recompute loss for HVP
                loss_for_hvp = loss_fn()
                grad_for_hvp = torch.autograd.grad(
                    loss_for_hvp, params, create_graph=True
                )
                grad_flat_hvp = torch.cat([g.flatten() for g in grad_for_hvp])
                hvp = torch.autograd.grad(
                    grad_flat_hvp, params, grad_outputs=v.split([p.numel() for p in params])
                )
                return torch.cat([h.flatten() for h in hvp]).detach()
            
            V_hat, Lambda_hat = randomized_nystrom_approximation(hvp_fn, p, s, device)
        
        # Compute Newton step via NystromPCG
        def hvp_fn_step(v: torch.Tensor) -> torch.Tensor:
            loss_for_hvp = loss_fn()
            grad_for_hvp = torch.autograd.grad(
                loss_for_hvp, params, create_graph=True
            )
            gf = torch.cat([g.flatten() for g in grad_for_hvp])
            hvp = torch.autograd.grad(
                gf, params, grad_outputs=v.split([p2.numel() for p2 in params])
            )
            return torch.cat([h.flatten() for h in hvp]).detach()
        
        d_k = nystrom_pcg(
            hvp_fn_step, grad_flat.detach(), d_prev,
            V_hat, Lambda_hat, s, mu, cg_tol, cg_max_iter
        )
        
        # Armijo line search
        def loss_fn_no_grad():
            with torch.no_grad():
                return loss_fn()
        
        eta_k = armijo_line_search(
            loss_fn_no_grad, params, grad_flat.detach(), d_k,
            eta, armijo_alpha, armijo_beta
        )
        
        # Update parameters: w ← w - η_k * d_k
        with torch.no_grad():
            offset = 0
            for param in params:
                numel = param.numel()
                param.data -= eta_k * d_k[offset:offset + numel].view(param.shape)
                offset += numel
        
        d_prev = d_k.detach()
    
    return losses, grad_norms
