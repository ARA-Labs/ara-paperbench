"""
NysNewton-CG (NNCG) optimizer — Algorithms 4, 5, 6, 7 from Rathore et al. 2024.

Implements:
- RandomizedNyströmApproximation (Algorithm 5)
- NyströmPCG (Algorithm 6) 
- Armijo line search (Algorithm 7)
- NNCG main loop (Algorithm 4)
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Callable, List, Tuple, Optional


def randomized_nystrom_approximation(
    hessian_vec_prod: Callable[[torch.Tensor], torch.Tensor],
    p: int,
    s: int,
    device: torch.device = torch.device('cpu')
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Randomized Nyström Approximation of symmetric PSD matrix H (Algorithm 5).
    
    Computes rank-s approximation: H ≈ V̂ Λ̂ V̂^T
    
    Args:
        hessian_vec_prod: Function mapping vector v (shape p,) to H@v
        p: Matrix dimension (number of model parameters)
        s: Sketch size (60 in paper)
        device: Compute device
    Returns:
        V_hat: Approximate eigenvectors, shape (p, s)
        Lambda_hat: Approximate eigenvalues (shifted), shape (s,)
    """
    # Generate test matrix and orthogonalize
    S = torch.randn(p, s, device=device)
    Q, _ = torch.linalg.qr(S)  # Q: (p, s)
    
    # Compute sketch Y = H Q
    Y = torch.zeros(p, s, device=device)
    for i in range(s):
        Y[:, i] = hessian_vec_prod(Q[:, i])
    
    # Stability shift: nu = sqrt(p) * eps(||Y||_2)
    nu = (p ** 0.5) * torch.finfo(Y.dtype).eps * torch.linalg.norm(Y)
    Y_nu = Y + nu * Q
    
    # Cholesky factorization
    try:
        C = torch.linalg.cholesky(Q.T @ Y_nu)  # s x s
        B = torch.linalg.solve_triangular(C.T, Y.T, upper=True).T  # p x s
        lam_shift = 0.0
    except torch.linalg.LinAlgError:
        # Fallback: eigendecomposition
        W, Gamma = torch.linalg.eigh(Q.T @ Y_nu)
        lam_shift = float(W.min().abs().item())
        R = W @ torch.diag(1.0 / (Gamma + lam_shift).sqrt()) @ W.T
        B = Y @ R
    
    # Thin SVD
    U, Sigma, _ = torch.linalg.svd(B, full_matrices=False)  # U: (p,s), Sigma: (s,)
    
    # Remove shift, clamp to non-negative
    Lambda_hat = torch.clamp(Sigma**2 - (nu + lam_shift), min=0.0)
    
    return U, Lambda_hat


def nystrom_pcg(
    hessian_vec_prod: Callable[[torch.Tensor], torch.Tensor],
    b: torch.Tensor,
    x0: torch.Tensor,
    U: torch.Tensor,
    Lambda_hat: torch.Tensor,
    s: int,
    mu: float,
    eps: float = 1e-16,
    max_iters: int = 1000
) -> torch.Tensor:
    """
    NyströmPCG: Solve (H + mu*I)x = b using preconditioned CG (Algorithm 6).
    
    Preconditioner P^{-1} = (lambda_s + mu) * U * (Lambda_hat + mu*I)^{-1} * U^T + (I - U*U^T)
    
    Args:
        hessian_vec_prod: Function computing H@v
        b: Right-hand side vector, shape (p,)
        x0: Initial guess, shape (p,)
        U: Approximate eigenvectors from Nyström, shape (p, s)
        Lambda_hat: Approximate eigenvalues, shape (s,)
        s: Sketch size
        mu: Damping parameter
        eps: CG tolerance
        max_iters: Maximum CG iterations (M in paper)
    Returns:
        x: Solution to (H + mu*I)x ≈ b, shape (p,)
    """
    lambda_s = Lambda_hat[-1].item() if len(Lambda_hat) > 0 else 0.0
    
    def precond_inv(v: torch.Tensor) -> torch.Tensor:
        """Apply P^{-1} to v."""
        Utv = U.T @ v  # (s,)
        # Term 1: (lambda_s + mu) * U * (Lambda_hat + mu)^{-1} * U^T * v
        term1 = (lambda_s + mu) * (U @ (Utv / (Lambda_hat + mu)))
        # Term 2: (I - U*U^T) * v
        term2 = v - U @ Utv
        return term1 + term2
    
    def mat_vec(v: torch.Tensor) -> torch.Tensor:
        """Apply (H + mu*I) to v."""
        return hessian_vec_prod(v) + mu * v
    
    x = x0.clone()
    r = b - mat_vec(x)
    z = precond_inv(r)
    p = z.clone()
    rz = (r * z).sum()
    
    for _ in range(max_iters):
        if r.norm() < eps:
            break
        Ap = mat_vec(p)
        alpha = rz / (p * Ap).sum()
        x = x + alpha * p
        r = r - alpha * Ap
        z = precond_inv(r)
        rz_new = (r * z).sum()
        beta = rz_new / rz
        p = z + beta * p
        rz = rz_new
    
    return x


def armijo_line_search(
    loss_fn: Callable[[], torch.Tensor],
    params: List[torch.Tensor],
    direction: List[torch.Tensor],
    grad: List[torch.Tensor],
    t_init: float = 1.0,
    alpha: float = 0.1,
    beta: float = 0.5,
    max_steps: int = 50
) -> float:
    """
    Armijo line search (Algorithm 7).
    
    Finds t such that L(w - t*d) <= L(w) - alpha*t*(grad^T d)
    
    Args:
        loss_fn: Closure returning current loss
        params: List of parameter tensors
        direction: Search direction (list of tensors, same shapes as params)
        grad: Current gradient (list of tensors)
        t_init: Initial step size
        alpha: Armijo sufficient decrease constant (0.1)
        beta: Backtracking factor (0.5)
        max_steps: Maximum backtracking steps
    Returns:
        t: Accepted step size
    """
    L0 = loss_fn().item()
    directional_deriv = sum((g * (-d)).sum().item() for g, d in zip(grad, direction))
    
    t = t_init
    for _ in range(max_steps):
        # Take step
        with torch.no_grad():
            for p, d in zip(params, direction):
                p.data -= t * d
        
        L_new = loss_fn().item()
        
        if L_new <= L0 - alpha * t * abs(directional_deriv):
            return t
        
        # Restore and backtrack
        with torch.no_grad():
            for p, d in zip(params, direction):
                p.data += t * d
        t *= beta
    
    return t


class NNCGOptimizer:
    """
    NysNewton-CG (NNCG) optimizer (Algorithm 4).
    
    Designed to be run after Adam+L-BFGS to further reduce loss using
    damped Newton steps with Nyström-preconditioned CG.
    """
    
    def __init__(
        self,
        model: nn.Module,
        loss_fn: Callable,
        eta: float = 1.0,
        K: int = 2000,
        s: int = 60,
        F: int = 20,
        mu: float = 1e-2,
        eps: float = 1e-16,
        M: int = 1000,
        alpha: float = 0.1,
        beta: float = 0.5
    ):
        """
        Args:
            model: PINN model
            loss_fn: Loss function (no args, uses model's current state)
            eta: Initial maximum learning rate (1.0)
            K: Number of NNCG iterations (2000)
            s: Nyström sketch size (60)
            F: Preconditioner update frequency (20)
            mu: Damping parameter (tuned in [1e-5, 1e-1])
            eps: CG convergence tolerance (1e-16)
            M: Max CG iterations (1000)
            alpha: Armijo alpha (0.1)
            beta: Armijo beta (0.5)
        """
        self.model = model
        self.loss_fn = loss_fn
        self.eta = eta
        self.K = K
        self.s = s
        self.F = F
        self.mu = mu
        self.eps = eps
        self.M = M
        self.alpha = alpha
        self.beta = beta
        
        self._params = list(model.parameters())
        self._p = sum(p.numel() for p in self._params)
        self._device = next(model.parameters()).device
        
        self._U: Optional[torch.Tensor] = None
        self._Lambda_hat: Optional[torch.Tensor] = None
        self._d_prev: Optional[torch.Tensor] = None
    
    def _flat_grad(self) -> torch.Tensor:
        """Compute and return flattened gradient vector."""
        loss = self.loss_fn()
        grads = torch.autograd.grad(loss, self._params, create_graph=False)
        return torch.cat([g.reshape(-1) for g in grads])
    
    def _hvp(self, v: torch.Tensor) -> torch.Tensor:
        """Hessian-vector product H_L(w) @ v via double backprop."""
        loss = self.loss_fn()
        grad = torch.autograd.grad(loss, self._params, create_graph=True)
        grad_flat = torch.cat([g.reshape(-1) for g in grad])
        hvp = torch.autograd.grad((grad_flat * v.detach()).sum(), self._params, retain_graph=False)
        return torch.cat([h.reshape(-1) for h in hvp]).detach()
    
    def step(self, iteration: int) -> float:
        """
        Run one NNCG iteration.
        
        Args:
            iteration: Current iteration index (0-indexed)
        Returns:
            loss: Current loss value
        """
        # Update preconditioner every F iterations
        if iteration % self.F == 0:
            self._U, self._Lambda_hat = randomized_nystrom_approximation(
                self._hvp, self._p, self.s, self._device
            )
        
        # Compute gradient
        g = self._flat_grad()
        
        # Initial guess for CG (warm start from previous Newton direction)
        x0 = self._d_prev if self._d_prev is not None else torch.zeros_like(g)
        
        # Solve (H + mu*I) d = g via NyströmPCG
        d = nystrom_pcg(
            self._hvp, g, x0,
            self._U, self._Lambda_hat,
            self.s, self.mu, self.eps, self.M
        )
        self._d_prev = d.detach().clone()
        
        # Armijo line search and parameter update
        offset = 0
        def apply_step(t: float):
            with torch.no_grad():
                off = 0
                for p in self._params:
                    numel = p.numel()
                    p.data -= t * d[off:off+numel].reshape(p.shape)
                    off += numel
        
        def undo_step(t: float):
            with torch.no_grad():
                off = 0
                for p in self._params:
                    numel = p.numel()
                    p.data += t * d[off:off+numel].reshape(p.shape)
                    off += numel
        
        L0 = self.loss_fn().item()
        dir_deriv = -(g * d).sum().item()  # negative because d is descent direction
        
        t = self.eta
        for _ in range(50):
            apply_step(t)
            L_new = self.loss_fn().item()
            if L_new <= L0 + self.alpha * t * dir_deriv:
                break
            undo_step(t)
            t *= self.beta
        
        return self.loss_fn().item()
    
    def run(self, verbose: bool = True) -> list:
        """
        Run full NNCG optimization for K iterations.
        
        Returns:
            losses: List of loss values per iteration
        """
        losses = []
        for k in range(self.K):
            loss = self.step(k)
            losses.append(loss)
            if verbose and k % 100 == 0:
                print(f"NNCG iter {k}: loss = {loss:.6e}")
        return losses
