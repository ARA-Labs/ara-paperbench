"""
SDE implementations for the Simformer.

Implements VESDE and VPSDE as used in the paper (Song et al., 2021b).
Parameters:
  VESDE: sigma_max=15, sigma_min=0.0001, t in [1e-5, 1]
  VPSDE: beta_min=0.01, beta_max=10, t in [1e-5, 1]

Reference: Gloeckler et al., 2024; Song et al., 2021b
"""

import math
import numpy as np
from typing import Tuple


class VESDE:
    """
    Variance Exploding SDE.

    f(x, t) = 0
    g(t) = sigma_min * (sigma_max / sigma_min)^t * sqrt(2 * log(sigma_max / sigma_min))

    Perturbation kernel: p(x_t | x_0) = N(x_t; x_0, sigma(t)^2 * I)
    sigma(t) = sigma_min * (sigma_max / sigma_min)^t

    Paper parameters: sigma_max=15, sigma_min=0.0001, t in [1e-5, 1]
    """

    def __init__(self, sigma_min: float = 0.0001, sigma_max: float = 15.0):
        self.sigma_min = sigma_min
        self.sigma_max = sigma_max
        self.log_ratio = math.log(sigma_max / sigma_min)

    def sigma(self, t: np.ndarray) -> np.ndarray:
        """Noise standard deviation at time t. Shape: same as t."""
        return self.sigma_min * (self.sigma_max / self.sigma_min) ** t

    def sigma_sq(self, t: np.ndarray) -> np.ndarray:
        """Noise variance at time t."""
        return self.sigma(t) ** 2

    def mu(self, t: np.ndarray) -> np.ndarray:
        """Mean scaling (= 1 for VESDE): x_t = mu(t)*x_0 + sigma(t)*eps."""
        return np.ones_like(t)

    def drift(self, x: np.ndarray, t: np.ndarray) -> np.ndarray:
        """f(x, t) = 0 for VESDE."""
        return np.zeros_like(x)

    def diffusion(self, t: np.ndarray) -> np.ndarray:
        """g(t) = sigma_min * (sigma_max/sigma_min)^t * sqrt(2 * log(sigma_max/sigma_min))"""
        return self.sigma(t) * math.sqrt(2 * self.log_ratio)

    def perturb(
        self, x0: np.ndarray, t: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Sample x_t ~ p(x_t | x_0) = N(x_0, sigma(t)^2 * I).

        Args:
            x0: (B, d) clean samples
            t:  (B,) noise levels in [1e-5, 1]
        Returns:
            x_t: (B, d) noisy samples
            eps: (B, d) noise used
        """
        sigma_t = self.sigma(t)[:, None]   # (B, 1)
        eps = np.random.randn(*x0.shape)
        x_t = x0 + sigma_t * eps
        return x_t, eps

    def target_score(
        self, x0: np.ndarray, x_t: np.ndarray, t: np.ndarray
    ) -> np.ndarray:
        """
        Target score: nabla_{x_t} log p_t(x_t | x_0) = -(x_t - x_0) / sigma(t)^2

        Args:
            x0:  (B, d)
            x_t: (B, d)
            t:   (B,)
        Returns:
            score: (B, d)
        """
        sigma_sq_t = self.sigma_sq(t)[:, None]   # (B, 1)
        return -(x_t - x0) / sigma_sq_t

    def loss_weight(self, t: np.ndarray) -> np.ndarray:
        """Weighting function lambda(t) = g(t)^2 for the loss."""
        return self.diffusion(t) ** 2

    def reverse_drift(
        self, x: np.ndarray, t: np.ndarray, score: np.ndarray
    ) -> np.ndarray:
        """
        Drift of the reverse SDE: f(x,t) - g(t)^2 * score(x, t).
        For VESDE: 0 - g(t)^2 * score = -g(t)^2 * score.
        """
        g_t = self.diffusion(t)[:, None]   # (B, 1) or scalar
        return -g_t**2 * score


class VPSDE:
    """
    Variance Preserving SDE.

    f(x, t) = -0.5 * beta(t) * x
    g(t) = sqrt(beta(t))
    beta(t) = beta_min + t * (beta_max - beta_min)

    Paper parameters: beta_min=0.01, beta_max=10, t in [1e-5, 1]
    """

    def __init__(self, beta_min: float = 0.01, beta_max: float = 10.0):
        self.beta_min = beta_min
        self.beta_max = beta_max

    def beta(self, t: np.ndarray) -> np.ndarray:
        """Linear noise schedule beta(t)."""
        return self.beta_min + t * (self.beta_max - self.beta_min)

    def drift(self, x: np.ndarray, t: np.ndarray) -> np.ndarray:
        """f(x, t) = -0.5 * beta(t) * x"""
        return -0.5 * self.beta(t)[:, None] * x

    def diffusion(self, t: np.ndarray) -> np.ndarray:
        """g(t) = sqrt(beta(t))"""
        return np.sqrt(self.beta(t))

    def alpha(self, t: np.ndarray) -> np.ndarray:
        """Mean coefficient: alpha(t) = exp(-0.5 * integral_0^t beta(s) ds)"""
        integral = self.beta_min * t + 0.5 * (self.beta_max - self.beta_min) * t**2
        return np.exp(-0.5 * integral)

    def sigma(self, t: np.ndarray) -> np.ndarray:
        """Noise std: sigma(t) = sqrt(1 - alpha(t)^2)"""
        return np.sqrt(1 - self.alpha(t)**2 + 1e-8)

    def perturb(
        self, x0: np.ndarray, t: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Sample x_t ~ p(x_t | x_0) = N(alpha(t)*x_0, sigma(t)^2 * I).

        Returns:
            x_t: (B, d)
            eps: (B, d) noise
        """
        alpha_t = self.alpha(t)[:, None]
        sigma_t = self.sigma(t)[:, None]
        eps = np.random.randn(*x0.shape)
        x_t = alpha_t * x0 + sigma_t * eps
        return x_t, eps

    def target_score(
        self, x0: np.ndarray, x_t: np.ndarray, t: np.ndarray
    ) -> np.ndarray:
        """Target score for VPSDE."""
        alpha_t = self.alpha(t)[:, None]
        sigma_t = self.sigma(t)[:, None]
        return -(x_t - alpha_t * x0) / (sigma_t**2)
