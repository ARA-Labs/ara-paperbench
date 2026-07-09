"""
LexiFlow: Randomized Direct Search with Lexicographic Preferences (Algorithm 2)
Adapted from Zhang et al. (2023b) for coreset selection (LBCS).

Key modifications vs. original LexiFlow:
  1. No optional input targets
  2. Compromise ε is a relative value (fraction of f1*), not absolute
"""

import numpy as np
from typing import Tuple, List, Optional


class LexiFlow:
    """
    Black-box lexicographic optimizer for two objectives F(m) = [f1(m), f2(m)].

    Uses randomized direct search with:
      - Dynamic step size
      - Random restart
      - Practical lexicographic relations based on history

    Attributes:
        n_dims: Dimension of the search space (effective mask size after grouping)
        epsilon: Relative compromise on f1 (>= 0)
        delta_init: Initial step size
        delta_lower: Step size threshold for random restart
        history: List of (f1, f2) pairs evaluated so far
        incumbent_f1, incumbent_f2: Best observed f1, f2 of incumbent point
        f1_tilde, f2_tilde: Current threshold values
    """

    def __init__(
        self,
        n_dims: int,
        epsilon: float,
        f1_init: float,
        f2_init: float,
        delta_init: float = 1.0,
        delta_lower: float = 1e-4,
    ):
        self.n_dims = n_dims
        self.epsilon = epsilon
        self.delta_init = delta_init
        self.delta_lower = delta_lower
        self.delta = delta_init

        # History of evaluated masks
        self.history: List[Tuple[float, float]] = [(f1_init, f2_init)]
        self._update_thresholds()

        # Incumbent (best found so far)
        self.incumbent_f1 = f1_init
        self.incumbent_f2 = f2_init

        # Counters
        self.t = 0          # total iterations
        self.t_prime = 0    # iteration of last improvement
        self.e = 0          # no-improvement counter
        self.r = 0          # restart counter

    def _update_thresholds(self):
        """
        Update practical threshold vector F_H = [f1_tilde, f2_tilde]
        based on historical evaluations H (Eq. 14).

        f1_tilde = inf{f1 in H} * (1 + epsilon)
        f2_tilde = inf{f2 | f1 <= f1_tilde in H}
        """
        f1_values = np.array([h[0] for h in self.history])
        f2_values = np.array([h[1] for h in self.history])

        f1_hat = float(np.min(f1_values))
        self.f1_tilde = f1_hat * (1.0 + self.epsilon)

        # M1: masks with f1 <= f1_tilde
        m1_mask = f1_values <= self.f1_tilde
        if m1_mask.any():
            self.f2_tilde = float(np.min(f2_values[m1_mask]))
        else:
            self.f2_tilde = float(np.min(f2_values))

    def lex_equal(self, f1_a: float, f2_a: float, f1_b: float, f2_b: float) -> bool:
        """
        Practical lexicographic equality: F(a) =_(FH) F(b).
        True iff for all i: f_i(a) = f_i(b) OR both achieve the threshold.
        (Eq. 11)
        """
        eq1 = (f1_a == f1_b) or (f1_a <= self.f1_tilde and f1_b <= self.f1_tilde)
        eq2 = (f2_a == f2_b) or (f2_a <= self.f2_tilde and f2_b <= self.f2_tilde)
        return eq1 and eq2

    def lex_prec(self, f1_a: float, f2_a: float, f1_b: float, f2_b: float) -> bool:
        """
        Practical lexicographic strict precedence: F(a) ≺_(FH) F(b).
        a is better than b. (Eq. 12)

        F(a) ≺_(FH) F(b) iff ∃ i: f_i(a) < f_i(b) AND f_i(b) > threshold_i
            AND F_{i-1}(a) =_(FH) F_{i-1}(b)
        """
        # Check objective 1 (no previous objectives)
        if f1_a < f1_b and f1_b > self.f1_tilde:
            return True

        # Check objective 2 (conditional on objective 1 equality)
        f0_eq = (f1_a == f1_b) or (f1_a <= self.f1_tilde and f1_b <= self.f1_tilde)
        if f0_eq and f2_a < f2_b and f2_b > self.f2_tilde:
            return True

        return False

    def sample_candidate(self, current_mask: np.ndarray) -> np.ndarray:
        """
        Sample a candidate mask as current_mask ± delta * u,
        where u is a unit sphere random direction.

        Args:
            current_mask: Current binary mask, shape (n_dims,)

        Returns:
            candidate: Perturbed binary mask (rounded to {0,1}), shape (n_dims,)
        """
        u = np.random.randn(self.n_dims)
        u = u / (np.linalg.norm(u) + 1e-12)
        candidate = current_mask + self.delta * u
        # Project to [0,1] and round to binary
        candidate = np.clip(candidate, 0.0, 1.0)
        candidate = (candidate > 0.5).astype(np.float32)
        return candidate

    def update(
        self,
        f1_current: float,
        f2_current: float,
        f1_candidate: float,
        f2_candidate: float,
    ) -> Tuple[bool, bool]:
        """
        Update incumbent and step size based on lexicographic comparison.

        Args:
            f1_current, f2_current: Objectives of current mask
            f1_candidate, f2_candidate: Objectives of candidate mask

        Returns:
            accepted: Whether to replace current mask with candidate
            is_global_best: Whether candidate is the new global incumbent m*
        """
        self.t += 1
        self.history.append((f1_candidate, f2_candidate))
        self._update_thresholds()

        # Check if candidate is better than current (for local move)
        accepted = self.lex_prec(f1_candidate, f2_candidate, f1_current, f2_current)
        if not accepted:
            # Tie: candidate equals current but is better than incumbent
            accepted = (
                self.lex_equal(f1_candidate, f2_candidate, f1_current, f2_current) and
                self.lex_prec(f1_candidate, f2_candidate, self.incumbent_f1, self.incumbent_f2)
            )

        is_global_best = False
        if accepted:
            self.t_prime = self.t
            self.e = 0
            # Check if candidate improves the global incumbent
            if self.lex_prec(f1_candidate, f2_candidate, self.incumbent_f1, self.incumbent_f2):
                self.incumbent_f1 = f1_candidate
                self.incumbent_f2 = f2_candidate
                is_global_best = True
        else:
            self.e += 1

        # Dynamic step size (Eq. in Algorithm 2)
        if self.e >= 2 * self.n_dims - 1:
            self.e = 0
            self.delta = self.delta * np.sqrt((self.t_prime + 1) / (self.t + 1))

        # Random restart if step size too small
        if self.delta < self.delta_lower:
            self.r += 1
            self.delta = self.delta_init + self.r
            # Note: mask reinitialization handled externally

        return accepted, is_global_best
