"""
Back-to-Source Activation Shifting — FOA Feature-Level Adaptation
Paper: "Test-Time Model Adaptation with Only Forward Passes" (ICML 2024)

Implements Equations (7), (8), (9) from the paper.
Can be used standalone (without CMA-ES prompt adaptation) as 'foa_shift'.
"""

import torch
import torch.nn as nn

from .prompt_vit import PromptViT


class ActivationShift(nn.Module):
    """Back-to-source activation shifting for test-time adaptation.
    
    Directly shifts the final-layer CLS features toward source distribution
    without any backpropagation. Used as standalone or combined with FOA.
    
    Algorithm:
        1. Pre-compute source statistics {μ_N^S} from source samples D_S
        2. For each test batch X_t:
           a. Forward pass to get CLS feature e^0_N (shape: (B, d=768))
           b. Update EMA: μ_N(t) = 0.9*μ_N(t-1) + 0.1*batch_mean(e^0_N)
           c. Shift direction: d_t = μ_N^S − μ_N(t)          [Eqn. 8]
           d. Shifted feature: ê^0_N = e^0_N + γ * d_t       [Eqn. 7]
           e. Predict: ŷ = Head(ê^0_N)
    
    Args:
        model: PromptViT (can have num_prompts=0 for shift-only mode)
    """

    def __init__(self, model: PromptViT):
        super().__init__()
        self.model = model
        self.hist_stat = None   # μ_N(t): EMA estimate of test domain mean
        self.train_info = None  # (std, mean) of source CLS features
        self.imagenet_mask = None

    def _update_hist(self, batch_mean: torch.Tensor) -> None:
        """EMA update of test domain feature mean (Eqn. 9).
        
        μ_N(t) = α * μ_N(X_t) + (1−α) * μ_N(t−1), α = 0.1
        
        Initialization: on first batch, hist_stat = batch_mean (no prior)
        """
        if self.hist_stat is None:
            self.hist_stat = batch_mean  # initialize on first batch
        else:
            self.hist_stat = 0.9 * self.hist_stat + 0.1 * batch_mean

    def _get_shift_vector(self):
        """Compute d_t = μ_N^S − μ_N(t) (Eqn. 8).
        
        Returns None if hist_stat not yet initialized (first batch gets no shift).
        """
        if self.hist_stat is None:
            return None
        return self.train_info[1][-768:] - self.hist_stat  # source_mean − running_mean

    @torch.no_grad()
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply activation shifting to test batch.
        
        Args:
            x: Test batch, shape (B, 3, H, W)
        Returns:
            Prediction logits after shifted CLS features, shape (B, C)
        """
        shift_vector = self._get_shift_vector()

        # Forward pass: get CLS features from all N layers, shape (B, N*d)
        features = self.model.layers_cls_features_with_prompts(x)
        _, batch_mean = torch.std_mean(features, dim=0)

        # Extract final-layer CLS features (last d=768 dims)
        cls_features = features[:, -768:]  # e^0_N, shape (B, 768)

        # Apply shift: ê^0_N = e^0_N + γ * d_t  (γ=1.0, Eqn. 7)
        if shift_vector is not None:
            cls_features = cls_features + 1.0 * shift_vector

        # Final prediction via classification head
        output = self.model.vit.head(cls_features)
        if self.imagenet_mask is not None:
            output = output[:, self.imagenet_mask]

        # Update EMA with current batch mean (Eqn. 9)
        self._update_hist(batch_mean[-768:])

        return output

    def obtain_origin_stat(self, train_loader) -> None:
        """Pre-compute source CLS statistics {μ_N^S, σ_N^S}.
        
        Same as FOA.obtain_origin_stat but used for shift-only mode.
        Computed WITHOUT prompts (standard forward pass).
        
        Args:
            train_loader: DataLoader over source ID samples (Q ≥ 32)
        """
        features_list = []
        with torch.no_grad():
            for dl in train_loader:
                images = dl[0].cuda()
                feature = self.model.layers_cls_features(images)
                features_list.append(feature)
        features = torch.cat(features_list, dim=0)
        self.train_info = torch.std_mean(features, dim=0)  # (std, mean)

    def reset(self) -> None:
        """Reset EMA statistics between adaptation domains."""
        self.hist_stat = None
