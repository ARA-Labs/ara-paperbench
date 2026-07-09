"""
Downstream Integration: Drop-in replacement of CLIP vision encoder in LVLMs.

This module shows how to substitute the original CLIP ViT-L/14 vision encoder
with a FARE fine-tuned encoder in OpenFlamingo 9B and LLaVA-1.5 7B,
enabling adversarial robustness without retraining the downstream LVLM.

Key property (Theorem 3.1): Because FARE drives phi_FT(x) → phi_Org(x) on
clean inputs, the downstream LVLM connector and LLM see an approximately
unchanged embedding distribution, preserving clean performance.

Reference: Schlarmann et al. (2024) - §3.3, §4, Appendix B.1
"""

import torch
import torch.nn as nn
from typing import Optional


def load_fare_clip_encoder(
    checkpoint_path: str,
    device: torch.device,
    clip_model_name: str = "ViT-L/14",
) -> nn.Module:
    """
    Load a FARE fine-tuned CLIP ViT-L/14 vision encoder from a checkpoint.

    The encoder is a drop-in replacement for the original CLIP encoder
    in any downstream LVLM (LLaVA-1.5, OpenFlamingo) without LVLM retraining.

    Args:
        checkpoint_path: Path to the FARE fine-tuned encoder state dict
        device: Target device
        clip_model_name: CLIP architecture name (default: "ViT-L/14" at 224×224)
            NOTE: Use ViT-L/14@224 (NOT ViT-L/14@336) to match LLaVA-1.5 and OF configs

    Returns:
        phi_ft: FARE fine-tuned CLIP vision encoder (eval mode, on device)
    """
    import open_clip  # Requires open_clip package (not HuggingFace CLIP)
    # NOTE: LLaVA requires OpenCLIP implementation rather than HuggingFace CLIP

    # Load base CLIP architecture
    model, _, preprocess = open_clip.create_model_and_transforms(
        clip_model_name,
        pretrained=None,
    )
    vision_encoder = model.visual

    # Load FARE fine-tuned weights
    state_dict = torch.load(checkpoint_path, map_location=device)
    vision_encoder.load_state_dict(state_dict, strict=True)

    vision_encoder = vision_encoder.to(device).eval()
    return vision_encoder


def replace_clip_in_llava(
    llava_model: nn.Module,
    fare_vision_encoder: nn.Module,
) -> nn.Module:
    """
    Replace the original CLIP vision encoder in LLaVA-1.5 7B with FARE-CLIP.

    LLaVA uses second-last layer outputs (all tokens) of ViT-L/14@224.
    No retraining of the projection layers or Vicuna-7B LLM is required.

    Args:
        llava_model: Loaded LLaVA-1.5 7B model
        fare_vision_encoder: FARE fine-tuned ViT-L/14 encoder

    Returns:
        llava_model: LLaVA model with FARE encoder substituted (in-place)
    """
    # Replace the vision tower's encoder with FARE-fine-tuned weights
    # LLaVA accesses vision encoder via model.model.vision_tower
    if hasattr(llava_model, 'model') and hasattr(llava_model.model, 'vision_tower'):
        llava_model.model.vision_tower.vision_model = fare_vision_encoder
    else:
        raise AttributeError(
            "Cannot find vision_tower in LLaVA model. "
            "Ensure LLaVA-1.5 7B is loaded correctly."
        )
    return llava_model


def replace_clip_in_openflamingo(
    of_model: nn.Module,
    fare_vision_encoder: nn.Module,
) -> nn.Module:
    """
    Replace the original CLIP vision encoder in OpenFlamingo 9B with FARE-CLIP.

    OpenFlamingo uses all token outputs (not second-last layer) of ViT-L/14@224.
    Only the vision encoder is replaced; MPT-7B LLM and cross-attention
    layers remain frozen and unchanged.

    Args:
        of_model: Loaded OpenFlamingo 9B model
        fare_vision_encoder: FARE fine-tuned ViT-L/14 encoder

    Returns:
        of_model: OpenFlamingo model with FARE encoder substituted (in-place)
    """
    if hasattr(of_model, 'vision_encoder'):
        of_model.vision_encoder = fare_vision_encoder
    else:
        raise AttributeError(
            "Cannot find vision_encoder in OpenFlamingo model. "
            "Ensure OpenFlamingo 9B is loaded correctly."
        )
    return of_model


def verify_embedding_preservation(
    phi_ft: nn.Module,
    phi_org: nn.Module,
    images: torch.Tensor,
    device: torch.device,
) -> dict:
    """
    Verify that FARE fine-tuning preserves clean embeddings (Appendix C.4, Table 14).

    Computes L_clean = ||phi_FT(x) - phi_Org(x)||²₂ on a set of images.
    Expected values from paper (mean over 500 ImageNet validation images):
      - FARE2: E[L_clean] = 32.7
      - FARE4: E[L_clean] = 47.6
      - TeCoA2: E[L_clean] = 236.9 (much higher distortion)
      - TeCoA4: E[L_clean] = 292.7

    Args:
        phi_ft: Fine-tuned CLIP vision encoder
        phi_org: Original frozen CLIP vision encoder
        images: Input images (B, 3, H, W), values in [0, 1]
        device: torch.device

    Returns:
        metrics: Dict with 'mean_clean_loss' scalar
    """
    phi_ft.eval()
    phi_org.eval()

    with torch.no_grad():
        images = images.to(device)
        ft_embeddings = phi_ft.encode_image(images)    # (B, D), unnormalized
        org_embeddings = phi_org.encode_image(images)  # (B, D), unnormalized
        clean_loss = ((ft_embeddings - org_embeddings) ** 2).sum(dim=-1)  # (B,)

    return {
        'mean_clean_loss': clean_loss.mean().item(),
        'max_clean_loss': clean_loss.max().item(),
        'per_sample_loss': clean_loss.cpu().numpy(),
    }
