"""
Classifier Two-Sample Test (C2ST) implementation.

Measures distributional similarity between two sample sets P and Q.
Uses 5-fold cross-validation with a random forest classifier (100 trees).

Metric:
  C2ST = 0.5: distributions are identical (classifier at chance)
  C2ST = 1.0: distributions are perfectly distinguishable

Reference: Lueckmann et al., 2021; Hermans et al., 2022; Gloeckler et al., 2024
"""

import numpy as np
from typing import Tuple


def c2st(
    P: np.ndarray,   # (n_P, d) samples from distribution P (e.g., Simformer posterior)
    Q: np.ndarray,   # (n_Q, d) samples from distribution Q (e.g., MCMC ground truth)
    n_folds: int = 5,
    n_trees: int = 100,
    random_state: int = 0,
) -> float:
    """
    Compute the Classifier Two-Sample Test (C2ST) accuracy.

    Trains a random forest binary classifier to distinguish samples from P vs Q.
    Returns the 5-fold cross-validation accuracy.

    A score of 0.5 indicates indistinguishable distributions (perfect approximation).
    A score of 1.0 indicates perfectly distinguishable distributions (poor approximation).

    Args:
        P: (n_P, d) samples from distribution P (approximation)
        Q: (n_Q, d) samples from distribution Q (ground truth)
        n_folds: number of cross-validation folds (default: 5)
        n_trees: number of decision trees in random forest (default: 100)
        random_state: random seed for reproducibility

    Returns:
        c2st_accuracy: float in [0.5, 1.0]
    """
    # Combine samples and create labels
    X = np.concatenate([P, Q], axis=0)    # (n_P + n_Q, d)
    y = np.concatenate([
        np.ones(len(P)),
        np.zeros(len(Q))
    ])

    # Shuffle
    rng = np.random.RandomState(random_state)
    idx = rng.permutation(len(X))
    X, y = X[idx], y[idx]

    # 5-fold cross-validation with RandomForestClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score

    clf = RandomForestClassifier(n_estimators=n_trees, random_state=random_state)
    scores = cross_val_score(clf, X, y, cv=n_folds, scoring='accuracy')
    return float(scores.mean())


def c2st_from_posterior(
    posterior_samples: np.ndarray,   # (N, d_theta) Simformer posterior samples
    reference_samples: np.ndarray,   # (N, d_theta) MCMC reference posterior samples
) -> float:
    """
    Convenience wrapper for C2ST between posterior approximation and reference.

    Args:
        posterior_samples: (N, d_theta) samples from approximated posterior
        reference_samples: (N, d_theta) samples from ground-truth MCMC posterior

    Returns:
        c2st_accuracy: float in [0.5, 1.0]; lower is better
    """
    return c2st(posterior_samples, reference_samples)


def expected_coverage(
    posterior_fn,          # callable: obs -> posterior samples
    true_params: np.ndarray,  # (N, d_theta) true parameter values
    observations: np.ndarray, # (N, d_x) corresponding observations
    alpha_levels: np.ndarray = np.linspace(0, 1, 21),
    n_samples: int = 1000,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute expected coverage for calibration analysis (Hermans et al., 2022).

    For each credibility level alpha, computes the fraction of cases where
    the true parameter lies within the top-alpha% highest density region.

    A well-calibrated posterior satisfies: coverage(alpha) ≈ alpha for all alpha.

    Args:
        posterior_fn: function mapping observation to posterior samples
        true_params: (N, d_theta) ground truth parameters
        observations: (N, d_x) corresponding observations
        alpha_levels: credibility levels to evaluate at
        n_samples: number of posterior samples per observation

    Returns:
        alpha_levels: (n_alpha,) credibility levels
        coverage: (n_alpha,) observed coverage fractions
    """
    coverages = []
    for alpha in alpha_levels:
        in_region = 0
        for i in range(len(true_params)):
            # Draw posterior samples for this observation
            samples = posterior_fn(observations[i:i+1])  # (n_samples, d_theta)

            # Distance-based credible region: compute distance of each sample
            # from the true parameter and define the alpha-percentile threshold
            dists = np.linalg.norm(samples - true_params[i], axis=1)  # (n_samples,)
            threshold = np.percentile(dists, alpha * 100)

            # Check if the true parameter falls within the credible region
            true_dist = np.min(np.linalg.norm(samples - true_params[i], axis=1))
            if true_dist <= threshold:
                in_region += 1

        coverages.append(in_region / len(true_params))

    return alpha_levels, np.array(coverages)
