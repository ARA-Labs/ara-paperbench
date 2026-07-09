"""
SDE Definitions for NPSE/TSNPSE.

Implements VE-SDE and VP-SDE forward noising processes, including:
  - drift f(theta_t, t) and diffusion g(t) coefficients
  - Sampling from transition density p_{t|0}(theta_t | theta_0)
  - Computing transition log-density and its gradient ∇_{θ_t} log p_{t|0}(θ_t|θ_0)

References:
  - Song et al., 2021 (ICLR): Score-Based Generative Modeling via SDEs, Appendices B-C
  - Appendix E.3.1 of this paper
"""

import torch
import math
from abc import ABC, abstractmethod
from typing import Tuple


class BaseSDE(ABC):
    """Abstract base class for SDEs used in NPSE."""

    @abstractmethod
    def drift(self, theta_t: torch.Tensor, t: float) -> torch.Tensor:
        """Compute drift f(theta_t, t).

        Args:
            theta_t: Current state, shape (batch_size, d).
            t: Current time scalar in (0, 1].

        Returns:
            Drift term, shape (batch_size, d).
        """
        pass

    @abstractmethod
    def diffusion(self, t: float) -> float:
        """Compute diffusion coefficient g(t).

        Args:
            t: Current time scalar in (0, 1].

        Returns:
            Scalar diffusion coefficient.
        """
        pass

    @abstractmethod
    def sample_forward(self, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Sample theta_t ~ p_{t|0}(theta_t | theta_0).

        Args:
            theta_0: Initial parameters, shape (batch_size, d).
            t: Time values, shape (batch_size,).

        Returns:
            Noised parameters theta_t, shape (batch_size, d).
        """
        pass

    @abstractmethod
    def transition_score(self, theta_t: torch.Tensor, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Compute ∇_{θ_t} log p_{t|0}(θ_t | θ_0) in closed form.

        Args:
            theta_t: Noised parameters, shape (batch_size, d).
            theta_0: Clean parameters, shape (batch_size, d).
            t: Time values, shape (batch_size,).

        Returns:
            Transition score, shape (batch_size, d).
        """
        pass

    @abstractmethod
    def transition_log_density(self, theta_t: torch.Tensor, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Compute log p_{t|0}(theta_t | theta_0).

        Args:
            theta_t: Noised parameters, shape (batch_size, d).
            theta_0: Clean parameters, shape (batch_size, d).
            t: Time values, shape (batch_size,).

        Returns:
            Log-density values, shape (batch_size,).
        """
        pass


class VESDE(BaseSDE):
    """Variance-Exploding SDE (Appendix E.3.1, Eq. 134-135).

    f(theta_t, t) = 0
    g(t) = sigma_min * (sigma_max/sigma_min)^t * sqrt(2 * log(sigma_max/sigma_min))
    p_{t|0}(theta_t | theta_0) = N(theta_0, sigma_min^2 * (sigma_max/sigma_min)^{2t} * I)

    Args:
        sigma_min: Minimum noise level. 0.01 for 2D tasks (SIR, Two Moons);
                   0.05 for all other tasks.
        sigma_max: Maximum noise level. Set to max pairwise Euclidean distance
                   among training data (Technique 1, Song & Ermon 2020).
                   For sequential methods: computed from first-round training data.
    """

    def __init__(self, sigma_min: float, sigma_max: float):
        self.sigma_min = sigma_min
        self.sigma_max = sigma_max
        self._log_ratio = math.log(sigma_max / sigma_min)

    def sigma(self, t: torch.Tensor) -> torch.Tensor:
        """Compute noise std at time t: sigma_min * (sigma_max/sigma_min)^t."""
        return self.sigma_min * (self.sigma_max / self.sigma_min) ** t

    def drift(self, theta_t: torch.Tensor, t: float) -> torch.Tensor:
        """VE SDE has zero drift."""
        return torch.zeros_like(theta_t)

    def diffusion(self, t: float) -> float:
        """g(t) = sigma_min * (sigma_max/sigma_min)^t * sqrt(2*log(sigma_max/sigma_min))."""
        return self.sigma_min * (self.sigma_max / self.sigma_min) ** t * math.sqrt(2 * self._log_ratio)

    def sample_forward(self, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Sample theta_t ~ N(theta_0, sigma(t)^2 * I)."""
        sigma_t = self.sigma(t).unsqueeze(-1)  # (B, 1)
        noise = torch.randn_like(theta_0)
        return theta_0 + sigma_t * noise

    def transition_score(self, theta_t: torch.Tensor, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """∇_{θ_t} log p_{t|0}(θ_t|θ_0) = -(θ_t - θ_0) / σ(t)^2."""
        sigma_t = self.sigma(t).unsqueeze(-1)  # (B, 1)
        return -(theta_t - theta_0) / (sigma_t ** 2)

    def transition_log_density(self, theta_t: torch.Tensor, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """log p_{t|0}(theta_t|theta_0) = log N(theta_t; theta_0, sigma(t)^2 * I)."""
        sigma_t = self.sigma(t).unsqueeze(-1)  # (B, 1)
        d = theta_0.shape[-1]
        diff = theta_t - theta_0
        log_det = d * torch.log(sigma_t.squeeze(-1))
        quad = 0.5 * (diff ** 2 / sigma_t ** 2).sum(-1)
        return -0.5 * d * math.log(2 * math.pi) - log_det - quad


class VPSDE(BaseSDE):
    """Variance-Preserving SDE (Appendix E.3.1, Eq. 136-137).

    f(theta_t, t) = -0.5 * beta_t * theta_t
    g(t) = sqrt(beta_t)
    beta_t = beta_min + t * (beta_max - beta_min)
    p_{t|0}(theta_t | theta_0) = N(alpha_t * theta_0, (1 - alpha_t^2) * I)
    where alpha_t = exp(-0.5 * integral_0^t beta_s ds)

    Args:
        beta_min: 0.1 (paper default, following Song & Ermon 2020).
        beta_max: 11.0 (paper default, following Song & Ermon 2020).
    """

    def __init__(self, beta_min: float = 0.1, beta_max: float = 11.0):
        self.beta_min = beta_min
        self.beta_max = beta_max

    def beta(self, t: torch.Tensor) -> torch.Tensor:
        """Linear noise schedule: beta_t = beta_min + t*(beta_max - beta_min)."""
        return self.beta_min + t * (self.beta_max - self.beta_min)

    def integral_beta(self, t: torch.Tensor) -> torch.Tensor:
        """∫_0^t beta_s ds = beta_min * t + 0.5 * (beta_max - beta_min) * t^2."""
        return self.beta_min * t + 0.5 * (self.beta_max - self.beta_min) * t ** 2

    def alpha(self, t: torch.Tensor) -> torch.Tensor:
        """alpha_t = exp(-0.5 * ∫_0^t beta_s ds)."""
        return torch.exp(-0.5 * self.integral_beta(t))

    def drift(self, theta_t: torch.Tensor, t: float) -> torch.Tensor:
        """f(theta_t, t) = -0.5 * beta_t * theta_t."""
        beta_t = self.beta_min + t * (self.beta_max - self.beta_min)
        return -0.5 * beta_t * theta_t

    def diffusion(self, t: float) -> float:
        """g(t) = sqrt(beta_t)."""
        beta_t = self.beta_min + t * (self.beta_max - self.beta_min)
        return math.sqrt(beta_t)

    def sample_forward(self, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Sample theta_t ~ N(alpha_t * theta_0, (1 - alpha_t^2) * I)."""
        alpha_t = self.alpha(t).unsqueeze(-1)        # (B, 1)
        var_t = (1.0 - alpha_t ** 2).clamp(min=1e-8)  # (B, 1)
        noise = torch.randn_like(theta_0)
        return alpha_t * theta_0 + torch.sqrt(var_t) * noise

    def transition_score(self, theta_t: torch.Tensor, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """∇_{θ_t} log p_{t|0}(θ_t|θ_0) = -(θ_t - α_t θ_0) / (1 - α_t^2)."""
        alpha_t = self.alpha(t).unsqueeze(-1)        # (B, 1)
        var_t = (1.0 - alpha_t ** 2).clamp(min=1e-8)  # (B, 1)
        return -(theta_t - alpha_t * theta_0) / var_t

    def transition_log_density(self, theta_t: torch.Tensor, theta_0: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """log p_{t|0}(theta_t|theta_0) = log N(theta_t; alpha_t*theta_0, (1-alpha_t^2)*I)."""
        alpha_t = self.alpha(t).unsqueeze(-1)        # (B, 1)
        var_t = (1.0 - alpha_t ** 2).clamp(min=1e-8)  # (B, 1)
        d = theta_0.shape[-1]
        diff = theta_t - alpha_t * theta_0
        log_det = 0.5 * d * torch.log(var_t.squeeze(-1))
        quad = 0.5 * (diff ** 2 / var_t).sum(-1)
        return -0.5 * d * math.log(2 * math.pi) - log_det - quad
