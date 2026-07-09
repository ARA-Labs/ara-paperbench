"""
NysNewton-CG (NNCG) optimizer stub.

Implements the core NNCG algorithm from:
  Rathore et al. "Challenges in Training PINNs: A Loss Landscape Perspective"
  ICML 2024, arXiv:2402.01868

Full implementation: src/opts/nys_newton_cg.py in the repository.
"""

import torch
from torch.optim import Optimizer
from typing import Optional, Callable, Tuple


def armijo_line_search(
    f: Callable,
    x: list,          # list of parameter tensors (cloned)
    gx: torch.Tensor, # flat gradient vector, shape (p,)
    dx: torch.Tensor, # flat descent direction, shape (p,)
    t: float = 1.0,
    alpha: float = 0.1,
    beta: float = 0.5,
) -> float:
    """
    Backtracking Armijo line search.
    
    Finds largest t satisfying: f(x + t*dx) <= f(x) + alpha*t*(gx^T dx)
    
    Args:
        f: oracle returning scalar loss given (x_clone, t, dx)
        x: current parameter list
        gx: flat gradient at x, shape (p,)
        dx: flat descent direction (should be negative Newton direction), shape (p,)
        t: initial step size
        alpha: sufficient decrease constant (default: 0.1)
        beta: backtracking factor (default: 0.5)
    
    Returns:
        Accepted step size satisfying Armijo condition.
    """
    f0 = f(x, 0, dx)
    f1 = f(x, t, dx)
    while f1 > f0 + alpha * t * gx.dot(dx):
        t *= beta
        f1 = f(x, t, dx)
    return t


def apply_nystrom_precond_inv(
    U: torch.Tensor,         # approximate eigenvectors, shape (p, s)
    S_mu_inv: torch.Tensor,  # (S + mu)^{-1}, shape (s,)
    mu: float,
    lambd_r: float,          # S[rank-1], smallest retained eigenvalue
    x: torch.Tensor,         # input vector, shape (p,)
) -> torch.Tensor:
    """
    Apply inverse Nystrom preconditioner P^{-1} to vector x.
    
    P^{-1} = (lambd_r + mu) * U @ diag(S_mu_inv) @ U^T @ x + (x - U @ U^T @ x)
    
    Args:
        U: shape (p, s) — approximate eigenvectors
        S_mu_inv: shape (s,) — (eigenvalues + mu)^{-1}
        mu: damping parameter
        lambd_r: S[rank-1]
        x: shape (p,) — input vector
    
    Returns:
        P^{-1} x, shape (p,)
    """
    z = U.T @ x                                    # (s,)
    z = (lambd_r + mu) * (U @ (S_mu_inv * z)) + (x - U @ z)  # (p,)
    return z


def nystrom_pcg(
    hess_vec_prod: Callable[[torch.Tensor], torch.Tensor],  # H @ v
    b: torch.Tensor,         # right-hand side, shape (p,)
    x0: torch.Tensor,        # initial guess (warm start), shape (p,)
    mu: float,               # damping
    U: torch.Tensor,         # Nystrom eigenvectors, shape (p, s)
    S: torch.Tensor,         # Nystrom eigenvalues, shape (s,)
    rank: int,               # s
    tol: float = 1e-16,
    max_iters: int = 1000,
) -> torch.Tensor:
    """
    Solve (H + mu*I) x = b using Nystrom-preconditioned CG.
    
    Preconditioner: P^{-1} = (S[rank-1] + mu) * U @ (S + mu*I)^{-1} @ U^T
                              + (I - U @ U^T)
    
    Args:
        hess_vec_prod: function mapping v -> H @ v (via Hessian-vector products)
        b: RHS vector, shape (p,)
        x0: warm-start initial guess, shape (p,)
        mu: damping parameter
        U: eigenvectors from Nystrom approximation, shape (p, rank)
        S: eigenvalues from Nystrom approximation, shape (rank,)
        rank: sketch rank
        tol: convergence tolerance on residual norm
        max_iters: maximum CG iterations
    
    Returns:
        Approximate solution x to (H + mu*I)x = b, shape (p,)
    """
    lambd_r = S[rank - 1]
    S_mu_inv = (S + mu) ** (-1)

    # Initialize residual and preconditioned direction
    resid = b - (hess_vec_prod(x0) + mu * x0)  # r_0 = b - (H+muI)x_0
    with torch.no_grad():
        z = apply_nystrom_precond_inv(U, S_mu_inv, mu, lambd_r, resid)
        p = z.clone()

    x = x0.clone()
    i = 0
    while torch.norm(resid) > tol and i < max_iters:
        v = hess_vec_prod(p) + mu * p
        with torch.no_grad():
            alpha = torch.dot(resid, z) / torch.dot(p, v)
            x = x + alpha * p
            rTz = torch.dot(resid, z)
            resid = resid - alpha * v
            z = apply_nystrom_precond_inv(U, S_mu_inv, mu, lambd_r, resid)
            beta = torch.dot(resid, z) / rTz
            p = z + beta * p
        i += 1

    return x


def randomized_nystrom_approximation(
    hess_vec_prod: Callable,  # maps (p, s) matrix -> (p, s) via batched HVPs
    p: int,                   # number of parameters
    rank: int,                # sketch size s
    device: torch.device,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Compute rank-s Nystrom approximation of Hessian H.
    
    Returns approximate top eigenvectors U (p x rank) and eigenvalues S (rank,).
    
    Algorithm:
        1. Generate random test matrix Phi (rank x p), orthonormalize columns
        2. Compute sketch Y = H @ Phi
        3. Add numerical shift for stability
        4. Cholesky factor of Phi^T Y_nu
        5. Thin SVD of B = Y C^{-1} to get eigenvectors/values
    
    Args:
        hess_vec_prod: batched Hessian-vector product, maps (rank, p) -> (rank, p)
        p: number of parameters
        rank: approximation rank (s=60 in paper)
        device: torch device
    
    Returns:
        U: shape (p, rank) — approximate top eigenvectors
        S: shape (rank,) — approximate top eigenvalues (non-negative, shift removed)
    """
    # Generate and orthonormalize test matrix
    Phi = torch.randn((rank, p), device=device) / (p ** 0.5)   # (rank, p)
    Phi = torch.linalg.qr(Phi.t(), mode='reduced')[0].t()       # (rank, p)

    Y = hess_vec_prod(Phi)   # (rank, p) -> sketch

    # Numerical stability shift
    shift = torch.finfo(Y.dtype).eps
    Y_shifted = Y + shift * Phi

    # Cholesky factorization
    cholesky_target = torch.mm(Y_shifted, Phi.t())   # (rank, rank)
    try:
        C = torch.linalg.cholesky(cholesky_target)
        B = torch.linalg.solve_triangular(C, Y_shifted, upper=False, left=True)
    except Exception:
        eigs, eigvecs = torch.linalg.eigh(cholesky_target)
        shift = shift + torch.abs(torch.min(eigs))
        eigs = eigs + shift
        C = torch.linalg.cholesky(eigvecs @ torch.diag(eigs) @ eigvecs.T)
        B = torch.linalg.solve_triangular(C, Y_shifted, upper=False, left=True)

    # Thin SVD
    _, Sigma, VT = torch.linalg.svd(B, full_matrices=False)
    U = VT.t()                                       # (p, rank)
    S = torch.clamp(Sigma ** 2 - shift, min=0.0)    # remove shift, clamp to 0

    return U, S


class NysNewtonCG(Optimizer):
    """
    NysNewton-CG (NNCG): Damped Newton-CG with Nystrom preconditioning.

    Solves (H_L(w) + mu*I)^{-1} grad L(w) at each step using NystromPCG,
    with Armijo line search. The Nystrom preconditioner is updated every
    `update_freq` iterations.

    Hyperparameters (from paper Appendix E.2):
        lr=1.0, rank=60, mu in {1e-5,...,1e-1} (tuned), update_freq=20,
        cg_tol=1e-16, cg_max_iters=1000, alpha=0.1, beta=0.5

    Args:
        params: model parameters
        lr (float): initial step size for Armijo search (default: 1.0)
        rank (int): Nystrom approximation rank s (default: 60, per paper)
        mu (float): damping parameter (default: 1e-2, tune from {1e-5..1e-1})
        update_freq (int): preconditioner update frequency F (default: 20)
        cg_tol (float): PCG convergence tolerance (default: 1e-16)
        cg_max_iters (int): max PCG iterations M (default: 1000)
        line_search_fn (str): 'armijo' or None (default: 'armijo')
    """

    def __init__(
        self,
        params,
        lr: float = 1.0,
        rank: int = 60,
        mu: float = 1e-2,
        update_freq: int = 20,
        cg_tol: float = 1e-16,
        cg_max_iters: int = 1000,
        line_search_fn: Optional[str] = 'armijo',
    ):
        defaults = dict(lr=lr, rank=rank, mu=mu, update_freq=update_freq,
                        cg_tol=cg_tol, cg_max_iters=cg_max_iters,
                        line_search_fn=line_search_fn)
        super().__init__(params, defaults)
        self.rank = rank
        self.mu = mu
        self.update_freq = update_freq
        self.cg_tol = cg_tol
        self.cg_max_iters = cg_max_iters
        self.line_search_fn = line_search_fn
        self.U: Optional[torch.Tensor] = None
        self.S: Optional[torch.Tensor] = None
        self.n_iters: int = 0
        self._old_dir: Optional[torch.Tensor] = None

    def update_preconditioner(self, grad_tuple: tuple) -> None:
        """
        Update Nystrom approximation of Hessian.
        
        Args:
            grad_tuple: gradients computed with create_graph=True
        """
        # Implementation: calls randomized_nystrom_approximation
        # See full code in repo src/opts/nys_newton_cg.py
        pass

    def step(self, closure: Optional[Callable] = None):
        """
        Perform one NNCG step.
        
        Args:
            closure: returns (loss, grad_tuple) where grad_tuple uses create_graph=True
        
        Returns:
            (loss, grad) tuple
        
        Procedure:
          1. If n_iters % update_freq == 0: update_preconditioner(grad_tuple)
          2. d = nystrom_pcg(H_L, grad, old_dir, mu, U, S, rank, cg_tol, cg_max_iters)
          3. eta = armijo_line_search(loss_fn, params, grad, -d, lr)
          4. params -= eta * d
          5. n_iters += 1
        """
        pass
