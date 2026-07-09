"""
Utilities for running BaM/GSM/ADVI on PosteriorDB models.

PosteriorDB models used in paper (Section 5.2):
  1. arK (nearly Gaussian): D=7
  2. gp-pois-regr (GP Poisson regression): D=13
  3. eight-schools-centered (hierarchical): D=10

Reference PosteriorDB HMC samples are used for:
  - relative mean error = ||μ - μ̂|| / ||μ||
  - relative SD error = ||σ - σ̂|| / ||σ||

Requires: bridgestan (BridgeStan), posteriordb
  pip install bridgestan posteriordb
"""
import numpy as np
from typing import Tuple, Dict


# PosteriorDB model identifiers
POSTERIORDB_MODELS = {
    "arK": {
        "model_id": "arK-arK",
        "D": 7,
        "type": "nearly_gaussian",
    },
    "gp-pois-regr": {
        "model_id": "gp-pois-regr-gp_pois_regr",
        "D": 13,
        "type": "non_gaussian_gp",
    },
    "eight-schools-centered": {
        "model_id": "eight_schools-eight_schools_centered",
        "D": 10,
        "type": "hierarchical",
    },
}

# Experimental configuration (Section 5.2, Appendix E.5)
POSTERIORDB_CONFIG = {
    "batch_sizes": [8, 32],               # B = 8 (dashed), B = 32 (solid)
    "bam_lr_schedule": "BD/(t+1)",        # λt = BD/(t+1) decaying
    "n_seeds": 5,                          # 5 independent seeded runs (NOT 10)
    "initialization_mu": "uniform[0, 0.1]",
    "initialization_cov": "identity",
    "reference": "HMC samples from posteriordb",
}


def load_posteriordb_model(model_name: str):
    """
    Load a PosteriorDB model via BridgeStan.

    Returns functions for:
        - log_p(z): unnormalized log posterior
        - score(z): gradient ∇_z log p(z | x) via BridgeStan

    Args:
        model_name: One of "arK", "gp-pois-regr", "eight-schools-centered"

    Returns:
        log_p: Log unnormalized posterior function
        score: Score function (requires BridgeStan + posteriordb installed)
        D: Dimension of the model
    """
    model_info = POSTERIORDB_MODELS[model_name]
    D = model_info["D"]

    # BridgeStan integration (requires posteriordb + BridgeStan installation)
    # from bridgestan import StanModel
    # import posteriordb
    # ...
    raise NotImplementedError(
        "Requires posteriordb and BridgeStan packages. "
        "See: github.com/stan-dev/posteriordb and github.com/roualdes/bridgestan"
    )


def load_hmc_reference_samples(model_name: str) -> np.ndarray:
    """
    Load reference HMC samples from posteriordb for a given model.

    Used to compute:
        - mu_hmc = posterior mean (mean of samples)
        - sigma_hmc = marginal posterior SD (std of samples per dimension)

    Args:
        model_name: Model identifier

    Returns:
        hmc_samples: Reference samples, shape (N_hmc, D)
    """
    raise NotImplementedError(
        "Requires posteriordb package. "
        "Provides reference samples generated via Hamiltonian Monte Carlo."
    )


def compute_posteriordb_metrics(
    mu_vi: np.ndarray,      # (D,) VI posterior mean estimate
    cov_vi: np.ndarray,     # (D, D) VI posterior covariance estimate
    hmc_samples: np.ndarray, # (N_hmc, D) reference HMC samples
) -> Dict[str, float]:
    """
    Compute relative mean error and relative SD error (eq. 242 in Appendix E.5).

    Metrics:
        relative_mean_error = ||μ_hmc - μ_vi|| / ||μ_hmc||
        relative_sd_error   = ||σ_hmc - σ_vi|| / ||σ_hmc||

    Args:
        mu_vi: VI posterior mean estimate
        cov_vi: VI posterior covariance estimate
        hmc_samples: HMC reference samples from posteriordb

    Returns:
        dict with 'relative_mean_error' and 'relative_sd_error'
    """
    mu_hmc = np.mean(hmc_samples, axis=0)    # (D,)
    sigma_hmc = np.std(hmc_samples, axis=0)  # (D,) marginal SDs

    sigma_vi = np.sqrt(np.diag(cov_vi))       # (D,) marginal SDs

    rel_mean = np.linalg.norm(mu_hmc - mu_vi) / np.linalg.norm(mu_hmc)
    rel_sd = np.linalg.norm(sigma_hmc - sigma_vi) / np.linalg.norm(sigma_hmc)

    return {
        "relative_mean_error": float(rel_mean),
        "relative_sd_error": float(rel_sd),
    }


# ============================================================
# Grid search for ADVI learning rate (posteriordb experiments)
# ============================================================

def grid_search_advi_lr(
    model_name: str,
    batch_size: int,
    lr_candidates: list = None,
    n_iter: int = 1000,
) -> float:
    """
    Grid search for optimal ADVI learning rate on a posteriordb model.

    Procedure: run ADVI for n_iter iterations, select lr minimizing relative mean error.

    Default search range (not specified in paper for posteriordb; use same as non-Gaussian):
        lr_candidates = [0.001, 0.01, 0.02, 0.05]

    Args:
        model_name: PosteriorDB model name
        batch_size: ADVI batch size
        lr_candidates: Learning rates to search over
        n_iter: Iterations per candidate

    Returns:
        best_lr: Learning rate achieving lowest relative mean error
    """
    if lr_candidates is None:
        lr_candidates = [0.001, 0.01, 0.02, 0.05]
    # Implementation requires loading model and running ADVI
    raise NotImplementedError("Requires posteriordb and ADVI implementation.")
