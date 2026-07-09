"""
Baseline Method Wrappers for TAN Comparison

Documents the baseline implementations used in TAN experiments (§5.2).
All GAN-based baselines are implemented by adapting the StyleGAN2 codebase [12].

Baselines compared:
  - TGAN [29]:       Fine-tune all parameters; no regularization; 100% param rate
  - TGAN+ADA [11]:   TGAN with adaptive data augmentation; 100% param rate
  - EWC [15]:        Elastic Weight Consolidation regularization; 100% param rate
  - CDC [19]:        Cross-Domain Consistency with patch discrimination; 100% param rate
  - DCL [33]:        Contrastive learning for source-target distance; 100% param rate
  - DDPM-PA [34]:    DPM-based pairwise adaptation (blurry image proxy); 100% param rate

All methods use the same 10-shot setup as TAN for fair comparison.
"""

import torch
import torch.nn as nn
from typing import Optional


class FullFineTuneWrapper(nn.Module):
    """
    Wrapper for full-parameter fine-tuning baselines (TGAN, TGAN+ADA, EWC, CDC, DCL).

    These methods update 100% of model parameters during fine-tuning,
    compared to TAN's 1.3–1.6% parameter rate via adaptor.

    All GAN-based baselines are implemented on the StyleGAN2 codebase [12]
    as described in §5.2.
    """

    def __init__(self, backbone: nn.Module):
        """
        Args:
            backbone: Pre-trained model (StyleGAN2 generator for GAN-based methods,
                      or DDPM U-Net for DDPM-PA)
        """
        super().__init__()
        self.backbone = backbone
        # All parameters enabled for full fine-tuning
        for param in self.backbone.parameters():
            param.requires_grad = True

    def forward(self, *args, **kwargs):
        return self.backbone(*args, **kwargs)

    @staticmethod
    def parameter_rate() -> float:
        """Returns 1.0 (100% of parameters fine-tuned)."""
        return 1.0


class DDPMPAWrapper(nn.Module):
    """
    DDPM Pairwise Adaptation (DDPM-PA) baseline [34].

    Approach: Substitutes the blurry predicted clean image at intermediate
    timestep t as a proxy for the final clean image, then applies CDC-like
    pairwise adaptation on DPMs.

    Limitation (identified in §1): The blurry predicted image does not
    accurately represent the generated image domain, leading to fuzzy and
    distorted outputs.

    All parameters are fine-tuned (100% parameter rate).
    Source: Zhu et al. (2022) arXiv:2211.03264
    """

    def __init__(self, ddpm_model: nn.Module):
        super().__init__()
        self.ddpm_model = ddpm_model
        for param in self.ddpm_model.parameters():
            param.requires_grad = True

    def predict_blurry_x0(
        self,
        x_t: torch.Tensor,
        t: torch.Tensor,
        alpha_bar_t: torch.Tensor,
    ) -> torch.Tensor:
        """
        Predict blurry x0 from intermediate timestep (DDPM-PA proxy).

        x0_pred = (x_t - sqrt(1-ᾱ_t) * ε_θ(x_t, t)) / sqrt(ᾱ_t)

        This blurry prediction is used as proxy for the clean target image
        in the pairwise adaptation loss — the main weakness identified in §1.

        Args:
            x_t:         Noisy image at timestep t
            t:           Timestep
            alpha_bar_t: ᾱ_t noise schedule values

        Returns:
            x0_pred: Blurry predicted clean image (used as target proxy in DDPM-PA)
        """
        eps_pred = self.ddpm_model(x_t, t)
        x0_pred = (x_t - (1 - alpha_bar_t).sqrt() * eps_pred) / alpha_bar_t.sqrt()
        return x0_pred

    def forward(self, x_t: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        return self.ddpm_model(x_t, t)

    @staticmethod
    def parameter_rate() -> float:
        return 1.0


# ─── Training Configuration Summary ──────────────────────────────────────────

BASELINE_CONFIGS = {
    "TGAN": {
        "parameter_rate": 1.0,          # 100% params updated
        "codebase": "StyleGAN2",         # implemented on StyleGAN2 [12]
        "iterations": 5000,              # approx. iterations (paper context)
        "reference": "[29] Wang et al., ECCV 2018",
    },
    "TGAN+ADA": {
        "parameter_rate": 1.0,
        "codebase": "StyleGAN2",
        "iterations": 5000,
        "reference": "[11] Karras et al., NeurIPS 2020",
    },
    "EWC": {
        "parameter_rate": 1.0,
        "codebase": "StyleGAN2",
        "iterations": 5000,
        "reference": "[15] Li et al., arXiv 2020",
    },
    "CDC": {
        "parameter_rate": 1.0,
        "codebase": "StyleGAN2",
        "iterations": 5000,
        "reference": "[19] Ojha et al., CVPR 2021",
    },
    "DCL": {
        "parameter_rate": 1.0,
        "codebase": "StyleGAN2",
        "iterations": 5000,
        "reference": "[33] Zhao et al., CVPR 2022",
    },
    "DDPM-PA": {
        "parameter_rate": 1.0,
        "codebase": "DDPM",
        "iterations": 5000,
        "reference": "[34] Zhu et al., arXiv 2022",
    },
    "DDPM-TAN": {
        "parameter_rate": 0.013,         # 1.3% params updated (adaptor only)
        "codebase": "DDPM",
        "iterations": 300,
        "reference": "This paper",
    },
    "LDM-TAN": {
        "parameter_rate": 0.016,         # 1.6% params updated (adaptor only)
        "codebase": "LDM",
        "iterations": 300,
        "reference": "This paper",
    },
}
