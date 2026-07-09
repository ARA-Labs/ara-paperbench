"""
Experiment runner: end-to-end experiment execution for BaM paper experiments.

Implements the experimental procedures described in:
  - Section 5.1: Gaussian and non-Gaussian targets
  - Section 5.2: PosteriorDB hierarchical models
  - Section 5.3: CIFAR-10 deep generative model

All experiments use:
  - JAX backend with 64-bit precision: config.update("jax_enable_x64", True)
  - NumPy seeded sampling for multivariate Gaussian
  - KLMonitor for tracking forward/reverse KL divergence

ITERATION COUNTS (from paper):
  - Gaussian targets: ≥ 10,000 iterations (implied by convergence curves)
  - Non-Gaussian targets: ≥ 10,000 iterations
  - PosteriorDB: No explicit count (convergence-based); typically ≥ 1,000
  - Deep generative model: T=100 (pilot) + T=1000 (main)

SEEDED RUNS:
  - Gaussian targets: 10 independent seeded runs
  - Non-Gaussian targets: 10 independent seeded runs
  - PosteriorDB: 5 independent seeded runs
  - Deep generative model: 1 run (single test image)
"""
import numpy as np
from typing import Callable, Optional


# ============================================================
# Gaussian Target Experiment (Section 5.1, Figure 5.1)
# ============================================================

GAUSSIAN_EXPERIMENT_CONFIG = {
    "dimensions": [4, 16, 64, 256],
    "bam_batch_sizes": {4: [2, 5], 16: [2, 15], 64: [2, 40], 256: [2, 150]},
    "gsm_batch_size": 2,
    "advi_batch_size": 2,
    "score_batch_size": 2,
    "fisher_batch_size": 2,
    "n_iterations": 10000,          # ≥ 10,000 iterations
    "n_seeds": 10,                   # 10 independent seeded runs
    "bam_lr_schedule": "constant",   # λt = BD
    "bam_lr_formula": "B * D",
    "advi_lr": 0.01,                 # Selected via grid search
    "fisher_lr": 0.01,
    "score_lr_by_dim": {4: 0.01, 16: 0.005, 64: 0.001, 256: 0.001},
    "initialization_mu": "uniform[0, 0.1]",
    "initialization_cov": "identity",
}


# ============================================================
# Non-Gaussian Target Experiment (Section 5.1, Figure 5.2)
# ============================================================

NONGAUSSIAN_EXPERIMENT_CONFIG = {
    "D": 10,
    "skew_configs": [                # varying skew, τ=1
        {"s": 0.2, "tau": 1.0},
        {"s": 1.0, "tau": 1.0},
        {"s": 1.8, "tau": 1.0},
    ],
    "tail_configs": [                # varying tails, s=0
        {"s": 0.0, "tau": 0.1},
        {"s": 0.0, "tau": 0.9},
        {"s": 0.0, "tau": 1.7},
    ],
    "bam_batch_sizes": [5, 10],
    "gsm_batch_size": 5,
    "advi_batch_size": 5,
    "score_batch_size": 5,
    "fisher_batch_size": 5,
    "n_iterations": 10000,           # ≥ 10,000 iterations
    "n_seeds": 10,                    # 10 independent seeded runs
    "bam_lr_schedule": "decaying",    # λt = BD/(t+1)
    "bam_lr_formula": "B * D / (t + 1)",
    "advi_lr": 0.02,                  # Grid-searched for non-Gaussian targets
    "fisher_lr": 0.05,
    "score_lr_by_skew": {0.2: 0.01, 1.0: 0.001, 1.8: 0.001},
    "score_lr_by_tail": {0.1: 0.001, 0.9: 0.01, 1.7: 0.01},
    "initialization_mu": "random",
    "initialization_cov": "identity",
}


# ============================================================
# PosteriorDB Experiment (Section 5.2, Figure 5.3)
# ============================================================

POSTERIORDB_EXPERIMENT_CONFIG = {
    "models": [
        {"name": "arK", "D": 7, "type": "nearly_gaussian"},
        {"name": "gp-pois-regr", "D": 13, "type": "non_gaussian"},
        {"name": "eight-schools-centered", "D": 10, "type": "hierarchical"},
    ],
    "batch_sizes": [8, 32],
    "n_seeds": 5,                    # 5 independent seeded runs (NOT 10)
    "bam_lr_schedule": "decaying",   # λt = BD/(t+1)
    "initialization_mu": "uniform[0, 0.1]",
    "initialization_cov": "identity",
    "evaluation": "relative_mean_error + relative_sd_error",
    "reference": "HMC samples from posteriordb",
}


# ============================================================
# Deep Generative Model Experiment (Section 5.3, Figure 5.4)
# ============================================================

DEEP_GEN_EXPERIMENT_CONFIG = {
    "dataset": "CIFAR-10",
    "D": 256,                          # Latent dimension
    "image_dim": 3072,                 # 32×32×3
    "sigma2_likelihood": 0.1,         # Likelihood variance (eq. 29)
    "pretrain_epochs": 100,
    "vae_architecture": {
        "encoder": "5-layer convolutional",
        "decoder": "5-layer convolutional",
        "variational_family": "factorized Gaussian",
    },
    "batch_sizes_vi": [10, 100, 300],
    "pilot_iters": 100,               # T=100 for LR selection
    "main_iters": 1000,               # T=1000 for main run
    "advi_lr": 0.02,
    "bam_lr": {"B=10": 0.1, "B=100": 50, "B=300": 7500},
    "initialization": "N(0, I_256)",
    "evaluation": "MSE of reconstructed image",
    "budget_analysis": "3000 gradient evaluations",
}


def run_bam_gaussian(
    D: int,
    batch_size: int,
    n_iter: int = 10000,
    n_seeds: int = 10,
    seed_offset: int = 0,
) -> dict:
    """
    Run BaM on D-dimensional Gaussian target.

    Configuration:
        λt = B*D (constant; best for Gaussian targets)
        Initialization: μ₀ ~ Uniform[0, 0.1], Σ₀ = I
        Runs: n_seeds independent seeded runs

    Args:
        D: Dimension (4, 16, 64, 256)
        batch_size: B (2, 5, 15, 40, or 150 depending on D)
        n_iter: Number of iterations (≥ 10,000)
        n_seeds: Number of independent runs (10 for Gaussian)
        seed_offset: Offset for seed generation

    Returns:
        dict with keys: 'forward_kl', 'reverse_kl' (both lists of n_seeds arrays)
    """
    from .bam import bam_update, Regularizers
    from .targets import make_random_gaussian_target
    from .metrics import gaussian_kl_exact

    lam = float(batch_size * D)       # λ = BD (constant)
    reg = Regularizers().constant(lam)

    results = {"forward_kl": [], "reverse_kl": [], "n_grad_evals": []}

    for seed in range(seed_offset, seed_offset + n_seeds):
        rng = np.random.default_rng(seed)
        mu_star, Sigma_star, log_p, score, sample_fn = make_random_gaussian_target(D, seed)

        # Initialization
        mu = rng.uniform(0, 0.1, size=D)
        Sigma = np.eye(D)

        fkl_history = []
        rkl_history = []
        n_evals = 0

        for t in range(n_iter):
            # Sample batch
            samples = np.random.multivariate_normal(mu, Sigma, size=batch_size)
            scores = score(samples)
            n_evals += batch_size

            # BaM update
            lam_t = reg(t)
            mu, Sigma = bam_update(samples, scores, mu, Sigma, lam_t)

            # Track KL divergence at checkpoints
            if t % 100 == 0:
                fkl, rkl = gaussian_kl_exact(mu, Sigma, mu_star, Sigma_star)
                fkl_history.append((n_evals, fkl))
                rkl_history.append((n_evals, rkl))

        results["forward_kl"].append(fkl_history)
        results["reverse_kl"].append(rkl_history)

    return results
