"""
Inpainting coupling implementation for stochastic interpolants.

Implements the inpainting-specific data-dependent coupling from §4.1 of
Albergo et al., 2024 (ICML): "Stochastic Interpolants with Data-Dependent Couplings"

Coupling: ρ(x₀, x₁|ξ) = ρ₁(x₁)ρ₀(x₀|x₁, ξ)
Base:     x₀ = ξ ∘ x₁ + (1-ξ) ∘ ζ,  ζ ~ N(0, I)
where ξ ∈ {0,1}^{C×W×H} is a binary mask.
"""

import torch
import torch.nn as nn
from typing import Tuple


def generate_mask(
    image_shape: Tuple[int, int, int, int],  # (B, C, H, W)
    tile_prob: float = 0.3,
    device: torch.device = None,
) -> torch.Tensor:
    """
    Generate a random binary mask by tiling the image into 64 equal-sized tiles.
    Each tile is selected to enter the mask with probability p=0.3.

    §4.1: "the mask is drawn randomly by tiling the image into 64 tiles;
           each tile is selected to enter the mask with probability p = 0.3"
    §4.1: "For simplicity, the mask takes the same value for all channels
           in a given spatial location in the image."

    The mask is single-channel (B, 1, H, W) so it broadcasts uniformly across
    all C channels — same spatial mask value for every channel.

    Used identically at both training time (random masking over training set)
    and sampling/evaluation time (same 64-tile, p=0.3 procedure).

    Args:
        image_shape: (B, C, H, W) shape of the image batch.
        tile_prob: Probability of a tile being masked (default 0.3).
        device: Target device.

    Returns:
        mask: Binary mask, shape (B, 1, H, W), broadcast to all channels.
               mask[b,0,h,w] = 0 means pixel is masked (noise); = 1 means known.
    """
    B, C, H, W = image_shape
    # 64 tiles: 8x8 grid
    n_tiles = 64
    tiles_per_side = int(n_tiles ** 0.5)  # 8
    tile_h = H // tiles_per_side
    tile_w = W // tiles_per_side

    # Sample which tiles are masked (0 = in mask, 1 = known)
    tile_mask = (torch.rand(B, 1, tiles_per_side, tiles_per_side, device=device) > tile_prob).float()

    # Upsample tile_mask to image resolution (nearest-neighbor)
    mask = tile_mask.repeat_interleave(tile_h, dim=2).repeat_interleave(tile_w, dim=3)
    # mask: (B, 1, H, W); apply to all channels via broadcasting

    return mask  # 1 = keep (known), 0 = mask (noise)


def construct_base_inpainting(
    x1: torch.Tensor,    # (B, C, H, W) clean target image
    mask: torch.Tensor,  # (B, 1, H, W) binary mask: 1=known, 0=masked
) -> torch.Tensor:
    """
    Construct the base sample x₀ for inpainting coupling.

    §4.1: x₀ = ξ ∘ x₁ + (1-ξ) ∘ ζ
    where ξ is the mask, ζ ~ N(0, I) (separate noise per channel).

    Args:
        x1: Clean target image, shape (B, C, H, W).
        mask: Binary mask (1=keep, 0=mask), shape (B, 1, H, W).

    Returns:
        x0: Base sample with known pixels from x₁ and masked pixels as Gaussian noise.
            Shape: (B, C, H, W).
    """
    # Independent noise for each channel (separate noise per channel as per §4.1)
    zeta = torch.randn_like(x1)  # ζ ~ N(0, I), shape (B, C, H, W)

    # x₀ = ξ ∘ x₁ + (1-ξ) ∘ ζ  (Hadamard product with mask broadcast over C)
    x0 = mask * x1 + (1.0 - mask) * zeta
    return x0


def add_class_channel(
    image: torch.Tensor,        # (B, C, H, W) image tensor
    class_label: torch.Tensor,  # (B,) integer class labels in [0, 999]
) -> torch.Tensor:
    """
    Append a channel uniformly filled with the integer class label value.

    Rubric: "a channel is added which is uniformly filled with the sample's class value"
    This applies during both training and sampling for inpainting and super-resolution.

    Args:
        image: Image or interpolant, shape (B, C, H, W).
        class_label: Integer class indices per sample, shape (B,).

    Returns:
        image_with_class: Image with class channel appended, shape (B, C+1, H, W).
    """
    B, C, H, W = image.shape
    # Create a channel filled uniformly with class value (broadcast over H, W)
    class_channel = class_label.float().view(B, 1, 1, 1).expand(B, 1, H, W)
    return torch.cat([image, class_channel], dim=1)  # (B, C+1, H, W)


def build_model_input_inpainting(
    I_t: torch.Tensor,      # (B, C, H, W) interpolant at time t
    mask: torch.Tensor,     # (B, 1, H, W) binary mask
    class_label: torch.Tensor,  # (B,) integer class labels in [0, 999]
    num_classes: int = 1000,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Build the full input to the velocity U-Net for inpainting.

    Appendix B: "ξ is given to the model as appended channels of the image x"
    Additional: a channel uniformly filled with the integer class label value is appended.
    Rubric: "a channel is added which is uniformly filled with the sample's class value"

    Input layout: [I_t | mask | class_channel], shape (B, C+2, H, W).
    Class labels are also passed to U-Net's class embedding mechanism.
    Velocity model acts only on first C image channels; mask and class channels are input-only.

    Args:
        I_t: Interpolant image, shape (B, C, H, W).
        mask: Binary mask, shape (B, 1, H, W).
        class_label: Integer class indices, shape (B,).
        num_classes: Number of ImageNet classes (1000).

    Returns:
        model_input: Concatenated input, shape (B, C+2, H, W).
        class_tensor: Class labels for U-Net embedding, shape (B,).
    """
    # Append mask as extra channel, then class-value channel
    I_with_mask = torch.cat([I_t, mask], dim=1)  # (B, C+1, H, W)
    model_input = add_class_channel(I_with_mask, class_label)  # (B, C+2, H, W)
    return model_input, class_label


def apply_velocity_mask(
    b_hat: torch.Tensor,  # (B, C, H, W) raw velocity output
    mask: torch.Tensor,   # (B, 1, H, W) binary mask: 1=known, 0=masked
) -> torch.Tensor:
    """
    Mask the velocity output so unmasked (known) pixels have zero velocity.

    §4.1: "we can build this property into our neural network model, and
           mask the output of the approximate velocity field to enforce that
           the unmasked pixels remain fixed"

    Since İₜ = x₁ - x₀ = 0 on known pixels (where x₀=x₁), the true velocity
    is zero there. Masking enforces this structural constraint.

    Args:
        b_hat: Raw velocity prediction, shape (B, C, H, W).
        mask: 1=known (should be zero velocity), 0=masked (free to predict).

    Returns:
        b_hat_masked: Velocity with known-pixel regions zeroed out.
    """
    # Invert mask: act only on masked (unknown) regions
    return b_hat * (1.0 - mask)


def sample_inpainting(
    model: nn.Module,      # Trained velocity U-Net
    x1_test: torch.Tensor, # (B, C, H, W) test image from ImageNet val
    mask: torch.Tensor,    # (B, 1, H, W) binary mask for evaluation
    class_label: torch.Tensor,  # (B,) integer class labels
    N: int = 100,          # Number of Forward Euler steps
) -> torch.Tensor:
    """
    Sample from the inpainting model using Algorithm 2 (Forward Euler).

    In practice, the Dopri solver from torchdiffeq is used (Appendix B),
    but Forward Euler is shown here for clarity.

    §4.1: "Sampling an x₀ can be performed by ... using the assumption that
           one directly observes x₀ ~ ρ₀(x₀) at inference time"

    Args:
        model: Trained velocity model b̂_θ.
        x1_test: Test image (used to construct x₀ via mask).
        mask: Inpainting mask (same structure as training).
        class_label: Class labels for conditioning.
        N: Number of integration steps.

    Returns:
        X_hat_N: In-painted sample, shape (B, C, H, W).
    """
    model.eval()
    with torch.no_grad():
        # Construct initial condition: x₀ = ξ ∘ x₁ + (1-ξ) ∘ ζ
        x0 = construct_base_inpainting(x1_test, mask)
        X_hat = x0.clone()

        dt = 1.0 / N
        for n in range(N):
            t_val = n / N
            t = torch.full((x0.shape[0],), t_val, device=x0.device)

            # Build model input
            model_input, cls = build_model_input_inpainting(X_hat, mask, class_label)

            # Predict velocity
            b_hat = model(model_input, t, cls)

            # Apply output mask (zero velocity on known pixels)
            b_hat = apply_velocity_mask(b_hat, mask)

            # Forward Euler step: X̂_{n+1} = X̂_n + N⁻¹ · b̂_{n/N}(X̂_n)
            X_hat = X_hat + dt * b_hat

    return X_hat
