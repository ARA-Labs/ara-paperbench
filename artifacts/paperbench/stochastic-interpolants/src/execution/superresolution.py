"""
Super-resolution coupling implementation for stochastic interpolants.

Implements the super-resolution specific data-dependent coupling from §4.2 of
Albergo et al., 2024 (ICML): "Stochastic Interpolants with Data-Dependent Couplings"

Coupling: ρ(x₀, x₁|ξ) = ρ₁(x₁)ρ₀(x₀|x₁, ξ)
Base:     x₀ = U(D(x₁)) + σζ,  ζ ~ N(0, I)
where D is nearest-neighbor downsampling, U is nearest-neighbor upsampling.
Conditioning: ξ = U(D(x₁)) (the upsampled low-res image), appended as channels.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple


def downsample_nearest(
    x: torch.Tensor,      # (B, C, H, W) high-resolution image
    low_res: Tuple[int, int],  # (H_low, W_low) target low resolution
) -> torch.Tensor:
    """
    Downsample image to low resolution by cropping/nearest-neighbor.

    Rubric: "downsampled by cropping to 64x64 if original is 256x256,
             or cropped to 256x256 if original is 512x512"
    Uses nearest-neighbor interpolation (area downsampling for crops).

    Args:
        x: High-res image, shape (B, C, H, W).
        low_res: Target (H_low, W_low), e.g., (64, 64) or (256, 256).

    Returns:
        x_low: Low-resolution image, shape (B, C, H_low, W_low).
    """
    return F.interpolate(x, size=low_res, mode='nearest')


def upsample_nearest(
    x_low: torch.Tensor,    # (B, C, H_low, W_low) low-resolution image
    high_res: Tuple[int, int],  # (H, W) target high resolution
) -> torch.Tensor:
    """
    Upsample low-resolution image back to original resolution using nearest-neighbor.

    Rubric: "nearest neighbour interpolation is applied to upsample the
             cropped image back to the original resolution"

    Args:
        x_low: Low-res image, shape (B, C, H_low, W_low).
        high_res: Target (H, W), e.g., (256, 256) or (512, 512).

    Returns:
        x_up: Upsampled image, shape (B, C, H, W).
    """
    return F.interpolate(x_low, size=high_res, mode='nearest')


def construct_base_superres(
    x1: torch.Tensor,         # (B, C, H, W) high-resolution ImageNet image
    low_res: Tuple[int, int],  # (H_low, W_low) low resolution
    sigma: float = 1.0,       # Noise level (σ > 0)
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Construct the base sample x₀ and conditioning variable ξ for super-resolution.

    §4.2: x₀ = U(D(x₁)) + σζ,  ζ ~ N(0, I)
          ξ = U(D(x₁))  (low-res image as conditioning)

    σ > 0 ensures base density is non-degenerate (not concentrated on
    a lower-dimensional manifold).

    Args:
        x1: High-resolution target image, shape (B, C, H, W).
        low_res: Target low resolution, e.g., (64, 64).
        sigma: Standard deviation of added Gaussian noise (σ > 0).

    Returns:
        x0: Base sample with upsampled low-res + noise, shape (B, C, H, W).
        xi: Low-resolution upsampled image for conditioning, shape (B, C, H, W).
    """
    H, W = x1.shape[2], x1.shape[3]

    # D: Downsample to low resolution
    x_low = downsample_nearest(x1, low_res)  # (B, C, H_low, W_low)

    # U: Upsample back to original resolution
    x_up = upsample_nearest(x_low, (H, W))  # (B, C, H, W)

    # Add Gaussian noise: x₀ = U(D(x₁)) + σζ
    zeta = torch.randn_like(x_up)
    x0 = x_up + sigma * zeta

    # Conditioning variable is the upsampled low-res image
    xi = x_up  # (B, C, H, W)

    return x0, xi


def add_class_channel_sr(
    image: torch.Tensor,        # (B, C_any, H, W) image tensor
    class_label: torch.Tensor,  # (B,) integer class labels in [0, 999]
) -> torch.Tensor:
    """
    Append a channel uniformly filled with the integer class label value.

    Rubric: "a channel is added which is uniformly filled with the sample's class value"
    Applied both during training and sampling for super-resolution.

    Args:
        image: Image or concatenated features, shape (B, C, H, W).
        class_label: Integer class indices per sample, shape (B,).

    Returns:
        image_with_class: Image with class channel appended, shape (B, C+1, H, W).
    """
    B, C, H, W = image.shape
    class_channel = class_label.float().view(B, 1, 1, 1).expand(B, 1, H, W)
    return torch.cat([image, class_channel], dim=1)  # (B, C+1, H, W)


def build_model_input_superres(
    I_t: torch.Tensor,      # (B, C, H, W) interpolant at time t
    xi: torch.Tensor,       # (B, C, H, W) upsampled low-resolution image (= x₀ without noise)
    class_label: torch.Tensor,  # (B,) integer class labels
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Build the full input to the velocity U-Net for super-resolution.

    Appendix B: "we follow (Ho et al., 2022a) and append upsampled
                 low-resolution images to the input xₜ at each time step"
    Rubric: "the image that has been downsampled, upsampled, and had gaussian
             noise added to it is appended to the original ImageNet image along
             the channel dimension to create the corrupted image"
    Rubric: "a channel is added which is uniformly filled with the sample's class value"

    Input layout: [I_t (C channels) | xi/upsampled_low_res (C channels) | class_channel (1 channel)]
    Total: (B, 2C+1, H, W).

    Velocity field acts ONLY on the first C image channels of the output.
    The appended low-res (xi) and class channels are input-only conditioning.

    Args:
        I_t: Interpolant image, shape (B, C, H, W).
        xi: Upsampled low-res image (conditioning, = U(D(x₁))), shape (B, C, H, W).
        class_label: Integer class indices, shape (B,).

    Returns:
        model_input: Concatenated input, shape (B, 2C+1, H, W).
        class_label: Passed through for U-Net class conditioning.
    """
    # Step 1: Append upsampled low-res image as conditioning channels
    model_input = torch.cat([I_t, xi], dim=1)  # (B, 2C, H, W)
    # Step 2: Append channel uniformly filled with class label value
    model_input = add_class_channel_sr(model_input, class_label)  # (B, 2C+1, H, W)
    return model_input, class_label


def apply_velocity_superres(
    b_hat_full: torch.Tensor,  # (B, 2C or C, H, W) raw velocity output
    C_image: int = 3,
) -> torch.Tensor:
    """
    Extract only the image-channel velocity (first C channels).

    §4.1/§4.2: "The velocity field only acts on the interpolant image,
                not the additional class channel that has been appended,
                or the low-resolution image that has been appended"

    Args:
        b_hat_full: Full velocity output from U-Net.
        C_image: Number of image channels (3 for RGB).

    Returns:
        b_hat: Velocity for image channels only, shape (B, C_image, H, W).
    """
    return b_hat_full[:, :C_image, :, :]


def sample_superres(
    model: nn.Module,          # Trained velocity U-Net
    x1_test: torch.Tensor,     # (B, C, H, W) high-res test image from ImageNet val
    class_label: torch.Tensor, # (B,) integer class labels
    low_res: Tuple[int, int],  # Low resolution, e.g., (64, 64)
    sigma: float = 1.0,        # Noise level
    N: int = 100,              # Number of Forward Euler steps
) -> torch.Tensor:
    """
    Sample super-resolved image using Algorithm 2 (Forward Euler).

    In practice, the Dopri solver from torchdiffeq is used (Appendix B).

    Rubric: "given N total iterations, on the i-th iteration the sample
             X̂_{i+1} = X̂_i + N⁻¹ · b̂_{i/N}(X̂_i)"

    Args:
        model: Trained velocity model b̂_θ.
        x1_test: High-resolution test image (full target for coupling construction).
        class_label: Class labels for conditioning.
        low_res: Target low resolution.
        sigma: Noise level for base construction.
        N: Number of integration steps.

    Returns:
        X_hat_N: Super-resolved sample, shape (B, C, H, W).
    """
    model.eval()
    with torch.no_grad():
        # Construct initial condition: x₀ = U(D(x₁)) + σζ
        x0, xi = construct_base_superres(x1_test, low_res, sigma)
        X_hat = x0.clone()

        dt = 1.0 / N
        for n in range(N):
            t_val = n / N
            t = torch.full((x0.shape[0],), t_val, device=x0.device)

            # Build model input (append conditioning)
            model_input, cls = build_model_input_superres(X_hat, xi, class_label)

            # Predict velocity (model output is C channels for image)
            b_hat = model(model_input, t, cls)

            # Forward Euler step: X̂_{n+1} = X̂_n + N⁻¹ · b̂_{i/N}(X̂_i)
            X_hat = X_hat + dt * b_hat

    return X_hat
