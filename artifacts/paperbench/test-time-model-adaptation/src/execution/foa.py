"""
Forward-Optimization Adaptation (FOA) — Core Algorithm
Paper: "Test-Time Model Adaptation with Only Forward Passes" (ICML 2024)
arXiv: 2404.01650

This module implements the main FOA loop (Algorithm 1) combining:
1. CMA-ES based prompt adaptation (Section 3.1)
2. Back-to-source activation shifting (Section 3.2)

NO backpropagation is used. All model weights are frozen.
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Dict, List, Optional, Tuple


class FOAAdapter:
    """
    Forward-Optimization Adaptation wrapper for a frozen ViT model.

    Attributes:
        model: Frozen ViT-Base (or compatible transformer) model.
        source_stats: Precomputed source in-distribution statistics.
            Dict with keys 'mean' and 'std', each a list of N tensors
            {μ^S_i, σ^S_i}_{i=0}^{N}, one per transformer layer CLS token.
        cma: CMA-ES optimizer instance (from pycma).
        prompt_dim: Total prompt dimension = d × Np.
        Np: Number of prompt embeddings (default 3).
        d: Embedding dimension (768 for ViT-Base).
        K: Population size for CMA-ES.
        lam: Trade-off parameter λ in fitness function.
        gamma: Step size γ for activation shifting.
        alpha: EMA factor α for activation shifting direction update.
        mu_N_ema: Running EMA estimate of test distribution center μ_N(t).
    """

    def __init__(
        self,
        model: nn.Module,
        source_stats: Dict[str, List[torch.Tensor]],
        Np: int = 3,
        d: int = 768,
        K: int = 28,
        lam: float = 0.4,
        gamma: float = 1.0,
        alpha: float = 0.1,
    ) -> None:
        """
        Initialize FOA adapter.

        Args:
            model: Frozen ViT model with get_cls_features() and head() methods.
            source_stats: {'mean': [μ^S_0, ..., μ^S_N], 'std': [σ^S_0, ..., σ^S_N]}
                          Each element is a tensor of shape (d,).
            Np: Number of prompt embeddings (default 3).
            d: Embedding dimension (768 for ViT-Base).
            K: CMA population size (default 28 = 4 + 3*log(d*Np)).
            lam: Trade-off parameter λ in fitness function Eq. 5.
            gamma: Activation shifting step size γ (default 1.0).
            alpha: EMA factor α for μ_N(t) update (default 0.1).
        """
        import cma  # pycma

        self.model = model
        self.model.eval()
        for p in model.parameters():
            p.requires_grad_(False)

        self.source_stats = source_stats
        self.Np = Np
        self.d = d
        self.K = K
        self.lam = lam
        self.gamma = gamma
        self.alpha = alpha

        self.prompt_dim = d * Np  # 768 * 3 = 2304 for ViT-Base

        # Initialize CMA-ES: m^(0)=0, Σ^(0)=I, τ^(0)=1 (Algorithm 1 line 1)
        self.cma_es = cma.CMAEvolutionStrategy(
            x0=np.zeros(self.prompt_dim),  # m^(0) = 0
            sigma0=1.0,                     # τ^(0) = 1
            inopts={"popsize": K, "verbose": -9},
        )

        # EMA estimate of OOD domain center μ_N(t), initialized to None
        # (initialized on first batch to μ_N(X_1))
        self.mu_N_ema: Optional[torch.Tensor] = None

    @torch.no_grad()
    def compute_source_stats(
        self,
        source_loader: torch.utils.data.DataLoader,
        device: torch.device,
    ) -> Dict[str, List[torch.Tensor]]:
        """
        Precompute source in-distribution statistics {μ^S_i, σ^S_i}_{i=0}^N.
        Called ONCE before TTA begins. Does NOT use prompt insertion.

        Args:
            source_loader: DataLoader over Q unlabeled source samples (Q ≥ 32).
            device: Target device.

        Returns:
            Dict with 'mean' and 'std', each a list of N tensors of shape (d,).
        """
        all_cls_features: List[List[torch.Tensor]] = []

        for images, _ in source_loader:
            images = images.to(device)
            # Forward pass WITHOUT prompts to get CLS features at each layer
            cls_features = self.model.get_cls_features(images)
            # cls_features: list of N tensors, each (batch, d)
            if not all_cls_features:
                all_cls_features = [[] for _ in range(len(cls_features))]
            for i, feat in enumerate(cls_features):
                all_cls_features[i].append(feat.cpu())

        source_means = []
        source_stds = []
        for i in range(len(all_cls_features)):
            concat = torch.cat(all_cls_features[i], dim=0)  # (Q, d)
            source_means.append(concat.mean(dim=0))   # (d,)
            source_stds.append(concat.std(dim=0))     # (d,)

        return {"mean": source_means, "std": source_stds}

    def prompt_from_flat(self, flat: np.ndarray, device: torch.device) -> torch.Tensor:
        """
        Convert flat CMA solution vector to prompt tensor.

        Args:
            flat: np.ndarray of shape (prompt_dim,) = (d * Np,)
            device: Target device.

        Returns:
            Prompt tensor of shape (Np, d).
        """
        p = torch.tensor(flat, dtype=torch.float32, device=device)
        return p.view(self.Np, self.d)

    @torch.no_grad()
    def adapt_batch(
        self,
        X_t: torch.Tensor,
        device: torch.device,
    ) -> torch.Tensor:
        """
        Adapt to a single test batch X_t using FOA (Algorithm 1).

        Args:
            X_t: Test batch tensor of shape (B, C, H, W).
            device: Target device.

        Returns:
            Predictions Ŷ_t of shape (B, num_classes).
        """
        X_t = X_t.to(device)

        # --- Step 1: Sample K candidate prompts from CMA distribution (Eq. 6) ---
        candidate_solutions = self.cma_es.ask()  # list of K numpy arrays, each (prompt_dim,)

        fitness_values = []
        best_fitness = float("inf")
        best_logits = None

        for k, flat_prompt in enumerate(candidate_solutions):
            # Convert to prompt tensor (Np, d)
            p_k = self.prompt_from_flat(flat_prompt, device)

            # --- Step 2: Forward pass with prompt k: [p_k; X_t] ---
            cls_features, logits = self.model.forward_with_prompt(X_t, p_k)
            # cls_features: list of N tensors, each (B, d)
            # logits: (B, num_classes)

            # --- Step 3: Activation shifting on final layer CLS (Eq. 7) ---
            e0_N = cls_features[-1]  # (B, d)
            e0_N_shifted = self._apply_activation_shift(e0_N, update_ema=(k == 0))
            # Re-predict with shifted feature
            shifted_logits = self.model.head(e0_N_shifted)  # (B, num_classes)

            # --- Step 4: Compute fitness value v_k (Eq. 5) ---
            v_k = self._compute_fitness(shifted_logits, cls_features)
            fitness_values.append(float(v_k))

            if v_k < best_fitness:
                best_fitness = v_k
                best_logits = shifted_logits

        # --- Step 5: Update CMA distribution using fitness values ---
        # CMA-ES minimizes fitness, so pass fitness values directly
        self.cma_es.tell(candidate_solutions, fitness_values)

        return best_logits  # (B, num_classes)

    @torch.no_grad()
    def _apply_activation_shift(
        self,
        e0_N: torch.Tensor,
        update_ema: bool = True,
    ) -> torch.Tensor:
        """
        Apply back-to-source activation shifting (Eqs. 7–9).

        Args:
            e0_N: Final layer CLS features of shape (B, d).
            update_ema: Whether to update the EMA estimate μ_N(t).

        Returns:
            Shifted CLS features ê^0_N of shape (B, d).
        """
        # Compute batch mean μ_N(X_t)
        mu_N_batch = e0_N.mean(dim=0)  # (d,)

        # Initialize or update EMA (Eq. 9)
        if self.mu_N_ema is None:
            self.mu_N_ema = mu_N_batch.clone()
        elif update_ema:
            self.mu_N_ema = self.alpha * mu_N_batch + (1.0 - self.alpha) * self.mu_N_ema

        # Compute shifting direction d_t = μ^S_N - μ_N(t) (Eq. 8)
        mu_S_N = self.source_stats["mean"][-1].to(e0_N.device)  # (d,)
        d_t = mu_S_N - self.mu_N_ema  # (d,)

        # Apply shift: ê^0_N = e^0_N + γ · d_t (Eq. 7)
        e0_N_shifted = e0_N + self.gamma * d_t.unsqueeze(0)  # (B, d)
        return e0_N_shifted

    @torch.no_grad()
    def _compute_fitness(
        self,
        logits: torch.Tensor,
        cls_features: List[torch.Tensor],
    ) -> float:
        """
        Compute the FOA fitness function (Eq. 5).

        L = Σ_{x∈X_t} Σ_c -ŷ_c log ŷ_c
            + λ Σ_{i=1}^{N} [||μ_i(X_t) - μ^S_i||_2 + ||σ_i(X_t) - σ^S_i||_2]

        Args:
            logits: Predicted logits of shape (B, num_classes).
            cls_features: List of N tensors, each (B, d) — CLS features per layer.

        Returns:
            Scalar fitness value (lower is better).
        """
        from .fitness import foa_fitness
        return foa_fitness(
            logits=logits,
            cls_features=cls_features,
            source_means=self.source_stats["mean"],
            source_stds=self.source_stats["std"],
            lam=self.lam,
        )


def run_foa(
    model: nn.Module,
    test_loader: torch.utils.data.DataLoader,
    source_stats: Dict[str, List[torch.Tensor]],
    Np: int = 3,
    K: int = 28,
    lam: float = 0.4,
    gamma: float = 1.0,
    alpha: float = 0.1,
    device: torch.device = torch.device("cuda"),
) -> List[torch.Tensor]:
    """
    Run FOA over entire test set (online, one-pass).

    Args:
        model: Frozen ViT model.
        test_loader: DataLoader over test batches {X_t}.
        source_stats: Precomputed source statistics.
        Np: Number of prompt embeddings.
        K: CMA population size.
        lam: Trade-off parameter λ.
        gamma: Activation shift step size.
        alpha: EMA factor for shift direction.
        device: Computation device.

    Returns:
        List of prediction tensors {Ŷ_t} for all batches.
    """
    adapter = FOAAdapter(
        model=model,
        source_stats=source_stats,
        Np=Np,
        K=K,
        lam=lam,
        gamma=gamma,
        alpha=alpha,
    )

    all_predictions = []
    for X_t, _ in test_loader:
        Y_hat_t = adapter.adapt_batch(X_t, device=device)
        all_predictions.append(Y_hat_t)

    return all_predictions
