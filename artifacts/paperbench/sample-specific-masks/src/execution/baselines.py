"""
Baseline Visual Reprogramming Methods:
  - Pad: Padding-based VR (Chen et al., 2023)
  - Narrow/Medium/Full: Watermarking-based VR (Bahng et al., 2022)

Reference: Section 2.2, Section 5 (Baselines)
Paper: "Sample-specific Masks for Visual Reprogramming-based Prompting", ICML 2024
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple


class PadVR(nn.Module):
    """
    Padding-based Visual Reprogramming (Pad baseline).
    Centers the target image and adds learnable pattern in the border region.
    
    fin(xi) = [zeros(border) | xi | zeros(border)] + M_pad ⊙ delta
    where M_pad = 1 in the border, 0 in the image center.
    
    Args:
        target_size:  (H_target, W_target) — pre-trained model input size (e.g., 224×224)
        source_size:  (H_source, W_source) — target domain image size (e.g., 32×32)
    """

    def __init__(self, target_size: Tuple[int, int], source_size: Tuple[int, int]) -> None:
        super().__init__()
        H_t, W_t = target_size
        H_s, W_s = source_size

        # Shared learnable pattern delta (shape = target size)
        self.delta = nn.Parameter(torch.zeros(1, 3, H_t, W_t), requires_grad=True)

        # Binary mask: 0 at image center, 1 in border
        mask = torch.ones(1, 3, H_t, W_t)
        pad_h = (H_t - H_s) // 2
        pad_w = (W_t - W_s) // 2
        mask[:, :, pad_h:pad_h + H_s, pad_w:pad_w + W_s] = 0.0
        self.register_buffer('mask', mask)

        self.target_size = target_size
        self.source_size = source_size

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, 3, H_s, W_s) — original target images (NOT yet resized)
        Returns:
            fin: (B, 3, H_t, W_t) — padded reprogrammed images
        """
        H_t, W_t = self.target_size
        H_s, W_s = self.source_size
        pad_h = (H_t - H_s) // 2
        pad_w = (W_t - W_s) // 2

        # Create canvas and place image in center
        canvas = torch.zeros(x.shape[0], 3, H_t, W_t, device=x.device)
        canvas[:, :, pad_h:pad_h + H_s, pad_w:pad_w + W_s] = x

        # Add masked pattern
        fin = canvas + self.mask * self.delta
        return fin


class WatermarkingVR(nn.Module):
    """
    Watermarking-based Visual Reprogramming (Narrow/Medium/Full baselines).
    Upsamples image to target size and adds learnable pattern in masked region.
    
    fin(xi) = r(xi) + M_wm ⊙ delta
    
    where M_wm is:
      - Full:   all-ones (224×224 for ResNet)
      - Medium: border mask with width=56 (quarter of image)
      - Narrow: border mask with width=28 (1/8 of image)
    
    Args:
        target_size:   (H, W) — pre-trained model input size
        mask_type:     'full', 'medium', or 'narrow'
    """

    MASK_WIDTHS = {
        'full': None,    # All-ones mask
        'medium': 56,    # Width = 56 (quarter of 224)
        'narrow': 28,    # Width = 28 (1/8 of 224)
    }

    def __init__(self, target_size: Tuple[int, int], mask_type: str = 'full') -> None:
        super().__init__()
        assert mask_type in self.MASK_WIDTHS, f"mask_type must be one of {list(self.MASK_WIDTHS.keys())}"
        H, W = target_size
        self.target_size = target_size
        self.mask_type = mask_type

        # Shared learnable pattern delta (initialized to zero, Algorithm 1)
        self.delta = nn.Parameter(torch.zeros(1, 3, H, W), requires_grad=True)

        # Binary mask construction
        width = self.MASK_WIDTHS[mask_type]
        if width is None:
            # Full watermark: mask = all ones
            mask = torch.ones(1, 3, H, W)
        else:
            # Border mask: ones in border of given width, zeros in center
            mask = torch.ones(1, 3, H, W)
            mask[:, :, width:H - width, width:W - width] = 0.0

        self.register_buffer('mask', mask)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, 3, H_s, W_s) — target images (any size; will be resized)
        Returns:
            fin: (B, 3, H, W) — reprogrammed images at target_size
        """
        H, W = self.target_size
        # Bilinear upsampling to target size (r function)
        x_resized = F.interpolate(x, size=(H, W), mode='bilinear', align_corners=False)

        # Add masked pattern: r(xi) + M ⊙ delta
        fin = x_resized + self.mask * self.delta
        return fin
