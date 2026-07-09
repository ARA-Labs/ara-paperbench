"""
Adaptor Module for TAN — Parameter-Efficient U-Net Layer Extension

Implements the bottleneck adaptor layer ψ^l described in §4.2 of the paper:
    x^l_t = θ^l(x^{l-1}) + ψ^l(x^{l-1})
    ψ^l(x^{l-1}) = f(x^{l-1} W_down) W_up

Key design: initialized to zero output so the pre-trained backbone is
preserved at the start of fine-tuning.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional


class AdaptorLayer(nn.Module):
    """
    Single adaptor layer inserted in parallel with a frozen U-Net layer.

    Architecture (§5.2):
        Input:     x ∈ ℝ^{w × h × r}  (or equivalently (B, r, h, w) in PyTorch)
        W_down:    projects to bottleneck  ℝ^{w/c × h/c × d}
        f(·):      non-linear activation (GELU)
        W_up:      projects back to ℝ^{w × h × r}
        Init:      W_up = 0  (so output is 0 at initialization)

    DDPM config: c=4, d=8  (1.3% parameter rate)
    LDM config:  c=2, d=8  (1.6% parameter rate)
    """

    def __init__(
        self,
        in_channels: int,   # r: number of input channels
        bottleneck_dim: int = 8,   # d: bottleneck dimension
        spatial_downsample: int = 4,  # c: spatial downscale factor
    ):
        """
        Args:
            in_channels:        Number of channels in input feature map (r)
            bottleneck_dim:     Bottleneck channel dimension d (default: 8)
            spatial_downsample: Spatial downscale factor c (default: 4 for DDPM,
                                2 for LDM per paper §5.2)
        """
        super().__init__()
        self.in_channels = in_channels
        self.bottleneck_dim = bottleneck_dim
        self.spatial_downsample = spatial_downsample

        # W_down: in_channels → bottleneck_dim with spatial downsampling via stride
        self.down = nn.Conv2d(
            in_channels,
            bottleneck_dim,
            kernel_size=spatial_downsample,
            stride=spatial_downsample,
            padding=0,
        )

        # W_up: bottleneck_dim → in_channels with spatial upsampling via transposed conv
        self.up = nn.ConvTranspose2d(
            bottleneck_dim,
            in_channels,
            kernel_size=spatial_downsample,
            stride=spatial_downsample,
            padding=0,
        )

        # Activation f(·)
        self.act = nn.GELU()

        # Initialize W_up to zero so the adaptor outputs zero at initialization
        nn.init.zeros_(self.up.weight)
        if self.up.bias is not None:
            nn.init.zeros_(self.up.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass: ψ^l(x) = f(x W_down) W_up

        Args:
            x: Input feature map (B, in_channels, H, W)

        Returns:
            Adaptor output (B, in_channels, H, W), zero at initialization.
        """
        h = self.act(self.down(x))
        return self.up(h)


class AdaptedUNetLayer(nn.Module):
    """
    Wrapper combining a frozen backbone U-Net layer θ^l with its adaptor ψ^l.

    Implements: x^l_t = θ^l(x^{l-1}) + ψ^l(x^{l-1})
    Only ψ^l parameters are trainable; θ^l is frozen.
    """

    def __init__(
        self,
        backbone_layer: nn.Module,  # θ^l: frozen pre-trained U-Net layer
        adaptor: AdaptorLayer,      # ψ^l: trainable adaptor
    ):
        super().__init__()
        self.backbone_layer = backbone_layer
        self.adaptor = adaptor

        # Freeze backbone layer
        for param in self.backbone_layer.parameters():
            param.requires_grad = False

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Combined forward: backbone output + adaptor output.

        Args:
            x: Input feature map (B, C, H, W)

        Returns:
            Combined output (B, C, H, W)
        """
        return self.backbone_layer(x) + self.adaptor(x)


def build_adapted_unet(
    backbone: nn.Module,
    layer_channels: list,  # list of channel sizes for each U-Net layer to adapt
    bottleneck_dim: int = 8,
    spatial_downsample: int = 4,
) -> tuple:
    """
    Attach adaptor layers to each specified U-Net layer in the backbone.
    Returns (backbone with frozen params, list of adaptor modules to train).

    Args:
        backbone:          Pre-trained U-Net (will be frozen)
        layer_channels:    List of channel dimensions for layers receiving adaptors
        bottleneck_dim:    Bottleneck dim d (DDPM: 8, LDM: 8)
        spatial_downsample: Spatial factor c (DDPM: 4, LDM: 2)

    Returns:
        (backbone, adaptors): backbone with all params frozen,
                               list of AdaptorLayer instances to optimize.
    """
    # Freeze all backbone parameters
    for param in backbone.parameters():
        param.requires_grad = False

    # Create adaptors for each specified layer
    adaptors = nn.ModuleList([
        AdaptorLayer(
            in_channels=ch,
            bottleneck_dim=bottleneck_dim,
            spatial_downsample=spatial_downsample,
        )
        for ch in layer_channels
    ])

    return backbone, adaptors
