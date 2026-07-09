"""
TSNPSE: Truncated Sequential Neural Posterior Score Estimation (Algorithm 1).

Implements the sequential loop with:
  - Truncated proposal prior via HPR estimation
  - Rejection sampling from truncated proposal (with cheap hypercube pre-rejection)
  - Round-by-round score network training (accumulating dataset D)

References:
  - Section 3.1 and Appendix E.3.3 of the paper.
  - Proposition 3.1: truncated proposal requires NO importance weight correction.
"""

import torch
import numpy as np
from typing import Callable, Optional, List, Tuple

from score_network import ScoreNetwork
from npse import train_score_network, sample_posterior, compute_log_density
from sde import BaseSDE


def estimate_hpr_threshold(
    score_net: ScoreNetwork,
    sde: BaseSDE,
    x_obs: torch.Tensor,
    n_hpr_samples: int = 20000,
    epsilon: float = 5e-4,
    device: str = 'cpu',
) -> Tuple[float, torch.Tensor]:
    """Estimate HPR threshold kappa and return posterior samples.

    Procedure (Appendix E.3.3):
      1. Draw 20000 samples from approximate posterior via ODE.
      2. Compute log-densities via instantaneous change-of-variables.
      3. Compute kappa = epsilon-th quantile of log-densities.

    Args:
        score_net: Trained ScoreNetwork.
        sde: SDE object.
        x_obs: Observed data, shape (x_dim,).
        n_hpr_samples: Number of posterior samples for HPR estimation (20000 in paper).
        epsilon: HPR threshold (5e-4 in paper); kappa = epsilon-th quantile.
        device: Torch device string.

    Returns:
        Tuple of (kappa, posterior_samples):
          kappa: float log-probability rejection threshold.
          posterior_samples: shape (n_hpr_samples, theta_dim).
    """
    # Step 1: Generate posterior samples via ODE
    posterior_samples = sample_posterior(
        score_net, sde, x_obs, n_samples=n_hpr_samples, device=device
    )  # (n_hpr_samples, theta_dim)

    # Step 2: Compute log-densities via change-of-variables
    log_probs = compute_log_density(
        score_net, sde, posterior_samples, x_obs, device=device
    )  # (n_hpr_samples,)

    # Step 3: kappa = epsilon-th quantile (log-probability rejection threshold)
    kappa = float(torch.quantile(log_probs, epsilon))

    return kappa, posterior_samples


def sample_truncated_proposal(
    prior_sampler: Callable[[int], torch.Tensor],
    score_net: ScoreNetwork,
    sde: BaseSDE,
    x_obs: torch.Tensor,
    kappa: float,
    posterior_samples: torch.Tensor,
    n_samples: int,
    device: str = 'cpu',
    max_attempts: int = 10_000_000,
) -> torch.Tensor:
    """Sample from truncated proposal prior using rejection sampling (Appendix E.3.3).

    Two-stage rejection:
      1. [Cheap] Reject if not within empirical bounding hypercube of posterior_samples.
      2. [Expensive] Compute log p_psi(theta | x_obs) via ODE; accept if >= kappa.

    Args:
        prior_sampler: Callable that returns (n,) samples from p(theta).
        score_net: Trained ScoreNetwork.
        sde: SDE object.
        x_obs: Observed data, shape (x_dim,).
        kappa: Log-probability rejection threshold from HPR estimation.
        posterior_samples: Approximate posterior samples used to define hypercube,
                          shape (n_hpr_samples, theta_dim).
        n_samples: Number of accepted samples required.
        device: Torch device string.
        max_attempts: Maximum total prior samples to draw.

    Returns:
        Accepted samples from truncated proposal, shape (n_samples, theta_dim).
    """
    # Compute empirical bounding hypercube from posterior samples
    theta_min = posterior_samples.min(0).values  # (d,)
    theta_max = posterior_samples.max(0).values  # (d,)

    accepted = []
    total_drawn = 0

    while len(accepted) < n_samples and total_drawn < max_attempts:
        # Draw batch from prior
        batch_size = max(n_samples * 10, 1000)
        theta_candidates = prior_sampler(batch_size)  # (batch_size, d)
        total_drawn += batch_size

        # [Stage 1: Cheap pre-rejection] Filter to hypercube
        in_hypercube = ((theta_candidates >= theta_min) & (theta_candidates <= theta_max)).all(-1)
        theta_filtered = theta_candidates[in_hypercube]  # (n_filtered, d)

        if len(theta_filtered) == 0:
            continue

        # [Stage 2: Expensive] Compute log-density under approximate posterior
        log_probs = compute_log_density(
            score_net, sde, theta_filtered, x_obs, device=device
        )  # (n_filtered,)

        # Accept if log p_psi(theta | x_obs) >= kappa
        accept_mask = log_probs >= kappa
        newly_accepted = theta_filtered[accept_mask]
        accepted.append(newly_accepted)

        if sum(len(a) for a in accepted) >= n_samples:
            break

    all_accepted = torch.cat(accepted, dim=0)[:n_samples]  # (n_samples, d)
    return all_accepted


def run_tsnpse(
    prior_sampler: Callable[[int], torch.Tensor],
    simulator: Callable[[torch.Tensor], torch.Tensor],
    x_obs: torch.Tensor,
    score_net: ScoreNetwork,
    sde: BaseSDE,
    n_rounds: int = 10,
    n_simulations_total: int = 10000,
    batch_size: int = 200,
    max_iters: int = 3000,
    lr: float = 1e-4,
    patience: int = 1000,
    val_fraction: float = 0.15,
    epsilon: float = 5e-4,
    n_hpr_samples: int = 20000,
    device: str = 'cpu',
) -> ScoreNetwork:
    """Run TSNPSE sequential algorithm (Algorithm 1).

    Distributes N simulations evenly across R rounds (M = N/R per round).
    Round 1: sample from prior. Rounds 2,...,R: sample from truncated proposal.
    Accumulates all data in dataset D across rounds.

    Args:
        prior_sampler: Returns n samples from p(theta), shape (n, theta_dim).
        simulator: Returns observations given parameters, shape (n, x_dim).
        x_obs: Single target observation, shape (x_dim,).
        score_net: ScoreNetwork instance to train.
        sde: Forward SDE (VESDE or VPSDE).
        n_rounds: Number of rounds R (10 in benchmark experiments).
        n_simulations_total: Total simulation budget N.
        batch_size: Mini-batch size for training.
        max_iters: Max training iterations per round (3000 in paper).
        lr: Learning rate (1e-4 in paper).
        patience: Early stopping patience (1000 in paper).
        val_fraction: Validation split fraction (0.15 in paper).
        epsilon: HPR truncation threshold (5e-4 in paper).
        n_hpr_samples: Samples for HPR estimation per round (20000 in paper).
        device: Torch device string.

    Returns:
        Trained ScoreNetwork (from final round).
    """
    M = n_simulations_total // n_rounds  # Simulations per round

    # Accumulated dataset D
    theta_list: List[torch.Tensor] = []
    x_list: List[torch.Tensor] = []

    kappa = None
    posterior_samples_hpr = None

    for r in range(1, n_rounds + 1):
        print(f"Round {r}/{n_rounds}: collecting {M} simulations...")

        # Sample from proposal prior (prior in round 1; truncated in subsequent rounds)
        if r == 1 or kappa is None:
            # Round 1: sample from prior
            theta_new = prior_sampler(M)  # (M, theta_dim)
        else:
            # Subsequent rounds: sample from truncated proposal via rejection sampling
            theta_new = sample_truncated_proposal(
                prior_sampler=prior_sampler,
                score_net=score_net,
                sde=sde,
                x_obs=x_obs,
                kappa=kappa,
                posterior_samples=posterior_samples_hpr,
                n_samples=M,
                device=device,
            )

        # Simulate observations
        x_new = simulator(theta_new)  # (M, x_dim)

        # Accumulate in D
        theta_list.append(theta_new)
        x_list.append(x_new)
        theta_D = torch.cat(theta_list, dim=0)
        x_D = torch.cat(x_list, dim=0)

        print(f"  Training on {len(theta_D)} accumulated samples...")

        # Train score network on full accumulated dataset D
        score_net = train_score_network(
            score_net=score_net,
            sde=sde,
            theta_data=theta_D,
            x_data=x_D,
            max_iters=max_iters,
            batch_size=batch_size,
            lr=lr,
            val_fraction=val_fraction,
            patience=patience,
            device=device,
        )

        # Compute truncated proposal for next round (HPR estimation)
        if r < n_rounds:
            print(f"  Estimating HPR (epsilon={epsilon}, {n_hpr_samples} samples)...")
            kappa, posterior_samples_hpr = estimate_hpr_threshold(
                score_net=score_net,
                sde=sde,
                x_obs=x_obs,
                n_hpr_samples=n_hpr_samples,
                epsilon=epsilon,
                device=device,
            )
            print(f"  HPR threshold kappa = {kappa:.4f}")

    return score_net
