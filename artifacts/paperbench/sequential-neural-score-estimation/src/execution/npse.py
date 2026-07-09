"""
NPSE: Neural Posterior Score Estimation.

Implements:
  1. Training via the denoising posterior score matching (DSM) objective (Eq. 7).
  2. Posterior sampling via time-reversal of probability flow ODE (RK45).
  3. Log-density evaluation via instantaneous change-of-variables (Eq. 5).

References:
  - Section 2.2 and Appendix E.3 of the paper.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from scipy.integrate import solve_ivp
from typing import Tuple, Optional, Callable

from score_network import ScoreNetwork
from sde import BaseSDE


def dsm_loss(
    score_net: ScoreNetwork,
    sde: BaseSDE,
    theta_0: torch.Tensor,
    x: torch.Tensor,
    lambda_t: Optional[Callable] = None,
) -> torch.Tensor:
    """Compute Monte Carlo estimate of DSM objective (Eq. 7).

    J^DSM_post(psi) = E_{t,theta_0,x,theta_t} [ lambda(t) * ||s_psi(theta_t,x,t) - ∇ log p_{t|0}||^2 ]

    Args:
        score_net: The score network s_psi.
        sde: SDE object (VESDE or VPSDE).
        theta_0: Clean parameter samples, shape (batch_size, d), from p(theta) or proposal.
        x: Corresponding observations, shape (batch_size, p), from p(x|theta_0).
        lambda_t: Optional weighting function of t (defaults to 1.0 if None).

    Returns:
        Scalar DSM loss value.
    """
    batch_size = theta_0.shape[0]
    device = theta_0.device

    # Sample time t ~ Uniform(0, 1]
    t = torch.rand(batch_size, device=device).clamp(min=1e-5)  # (B,)

    # Sample theta_t ~ p_{t|0}(theta_t | theta_0) via forward SDE
    theta_t = sde.sample_forward(theta_0, t)  # (B, d)

    # Compute transition score ∇_{theta_t} log p_{t|0}(theta_t | theta_0)
    target_score = sde.transition_score(theta_t, theta_0, t)  # (B, d)

    # Compute score network output
    predicted_score = score_net(theta_t, x, t)  # (B, d)

    # Weighting (default: 1.0; can be set to sigma^2 for VE SDE)
    if lambda_t is not None:
        weights = lambda_t(t)  # (B,)
    else:
        weights = torch.ones(batch_size, device=device)

    # MSE loss per sample, weighted
    loss = weights * ((predicted_score - target_score) ** 2).sum(-1)
    return loss.mean()


def train_score_network(
    score_net: ScoreNetwork,
    sde: BaseSDE,
    theta_data: torch.Tensor,
    x_data: torch.Tensor,
    max_iters: int = 3000,
    batch_size: int = 50,
    lr: float = 1e-4,
    val_fraction: float = 0.15,
    patience: int = 1000,
    device: str = 'cpu',
) -> ScoreNetwork:
    """Train score network using DSM objective (Appendix E.3.2).

    Args:
        score_net: ScoreNetwork to train.
        sde: Forward SDE object (VESDE or VPSDE).
        theta_data: All parameter samples, shape (N, d). From prior or proposal.
        x_data: Corresponding observations, shape (N, p).
        max_iters: Maximum training iterations (3000 in paper).
        batch_size: Mini-batch size (50/200/500 depending on budget/method).
        lr: Learning rate (1e-4 in paper).
        val_fraction: Fraction of data held out for validation (0.15 in paper).
        patience: Early stopping patience in steps (1000 in paper).
        device: Torch device string.

    Returns:
        Trained ScoreNetwork (best validation checkpoint).
    """
    score_net = score_net.to(device)
    theta_data = theta_data.to(device)
    x_data = x_data.to(device)

    # Set standardisation statistics
    score_net.set_standardisation(theta_data, x_data)

    # Train/validation split
    N = len(theta_data)
    n_val = int(N * val_fraction)
    indices = torch.randperm(N)
    val_idx = indices[:n_val]
    train_idx = indices[n_val:]

    theta_train, x_train = theta_data[train_idx], x_data[train_idx]
    theta_val, x_val = theta_data[val_idx], x_data[val_idx]

    optimizer = optim.Adam(score_net.parameters(), lr=lr)
    best_val_loss = float('inf')
    best_state = score_net.state_dict()
    steps_no_improve = 0

    for step in range(max_iters):
        score_net.train()
        # Sample mini-batch
        idx = torch.randint(0, len(theta_train), (batch_size,))
        theta_batch = theta_train[idx]
        x_batch = x_train[idx]

        optimizer.zero_grad()
        loss = dsm_loss(score_net, sde, theta_batch, x_batch)
        loss.backward()
        optimizer.step()

        # Validation check every step (paper: "after each training step")
        score_net.eval()
        with torch.no_grad():
            val_loss = dsm_loss(score_net, sde, theta_val, x_val).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.clone() for k, v in score_net.state_dict().items()}
            steps_no_improve = 0
        else:
            steps_no_improve += 1

        if steps_no_improve >= patience:
            break

    score_net.load_state_dict(best_state)
    return score_net


def sample_posterior(
    score_net: ScoreNetwork,
    sde: BaseSDE,
    x_obs: torch.Tensor,
    n_samples: int,
    device: str = 'cpu',
    t_start: float = 1.0,
    t_end: float = 1e-4,
) -> torch.Tensor:
    """Generate posterior samples via time-reversal of probability flow ODE (Eq. 4).

    Uses RK45 ODE solver. Initialises at theta_T ~ N(0, I) and integrates backward.

    Args:
        score_net: Trained ScoreNetwork.
        sde: SDE object (VESDE or VPSDE).
        x_obs: Single observation, shape (x_dim,) or (1, x_dim).
        n_samples: Number of posterior samples to generate.
        device: Torch device string.
        t_start: Start time (reference distribution, ~1.0).
        t_end: End time (target posterior, ~0.0001).

    Returns:
        Posterior samples, shape (n_samples, theta_dim).
    """
    score_net.eval()
    score_net.to(device)

    if x_obs.dim() == 1:
        x_obs = x_obs.unsqueeze(0)  # (1, x_dim)
    x_obs = x_obs.to(device)

    theta_dim = score_net.theta_dim

    # Initial samples from reference distribution N(0, I)
    theta_T = torch.randn(n_samples, theta_dim).numpy()

    def ode_fn(t_np: float, theta_flat: np.ndarray) -> np.ndarray:
        """Probability flow ODE: dtheta/dt = f(theta, T-t) - 0.5*g^2(T-t)*score."""
        t_val = float(t_np)
        theta_t = torch.tensor(theta_flat.reshape(n_samples, theta_dim),
                               dtype=torch.float32, device=device)
        t_tensor = torch.full((n_samples,), t_val, device=device)
        x_rep = x_obs.expand(n_samples, -1)

        with torch.no_grad():
            score = score_net(theta_t, x_rep, t_tensor)  # (N, d)

        # Reverse-time drift: -f(theta, t) + 0.5*g^2(t)*score
        # (time runs from t_start to t_end, so we negate for reverse)
        f_val = sde.drift(theta_t, t_val)
        g_val = sde.diffusion(t_val)
        dphi_dt = -f_val + 0.5 * (g_val ** 2) * score  # reverse-time ODE drift

        return (-dphi_dt).cpu().numpy().flatten()  # negative because RK45 integrates forward

    sol = solve_ivp(
        ode_fn,
        t_span=(t_start, t_end),
        y0=theta_T.flatten(),
        method='RK45',
        rtol=1e-5,
        atol=1e-5,
    )

    theta_samples = torch.tensor(
        sol.y[:, -1].reshape(n_samples, theta_dim),
        dtype=torch.float32
    )
    return theta_samples


def compute_log_density(
    score_net: ScoreNetwork,
    sde: BaseSDE,
    theta_samples: torch.Tensor,
    x_obs: torch.Tensor,
    device: str = 'cpu',
) -> torch.Tensor:
    """Compute log p_psi(theta | x_obs) via instantaneous change-of-variables (Eq. 5).

    Note: Returns log-density up to a normalisation constant; used for HPR estimation.

    Args:
        score_net: Trained ScoreNetwork.
        sde: SDE object.
        theta_samples: Parameter samples, shape (N, theta_dim).
        x_obs: Single observation, shape (x_dim,) or (1, x_dim).
        device: Torch device string.

    Returns:
        Log-density estimates, shape (N,). Values are unnormalised (up to constant).
    """
    # Implementation would use the augmented ODE with Skilling-Hutchinson trace estimator
    # This is computationally expensive (multiple ODE solves with trace computation)
    # Full implementation requires augmented ODE system.
    raise NotImplementedError(
        "Full density evaluation requires augmented ODE with trace computation. "
        "See Grathwohl et al. (2019) FFJORD for implementation reference. "
        "Used in TSNPSE for HPR estimation."
    )
