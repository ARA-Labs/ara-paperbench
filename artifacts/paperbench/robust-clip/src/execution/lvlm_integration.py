"""
Downstream LVLM Integration — Plug-In Replacement of CLIP Vision Encoder
Demonstrates how to swap the original CLIP encoder with FARE-CLIP in LVLMs.

Paper: "Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings
        for Robust Large Vision-Language Models" (Schlarmann et al., ICML 2024)

Key insight: Because FARE preserves the original CLIP embedding distribution,
the fine-tuned encoder can directly replace the frozen original CLIP encoder
in any downstream LVLM without retraining the connector or LLM.
"""

import torch
import torch.nn as nn
from typing import Optional


def load_fare_clip_encoder(
    checkpoint_path: str,
    architecture: str = "ViT-L/14",
    device: str = "cuda",
) -> nn.Module:
    """
    Loads a FARE fine-tuned CLIP vision encoder from a checkpoint.

    The FARE encoder has the same architecture as the original OpenAI CLIP
    ViT-L/14 encoder but with adversarially fine-tuned weights. It can be
    used as a drop-in replacement in any LVLM that uses frozen CLIP ViT-L/14.

    Args:
        checkpoint_path: Path to FARE-CLIP checkpoint (e.g., FARE2 or FARE4 weights)
        architecture:    CLIP ViT architecture string (default: "ViT-L/14")
        device:          Device to load to ("cuda" or "cpu")

    Returns:
        FARE-fine-tuned CLIP vision encoder (nn.Module), ready for inference
    """
    import clip  # OpenAI CLIP
    # Load original CLIP architecture
    model, preprocess = clip.load(architecture, device=device)
    visual_encoder = model.visual

    # Load FARE fine-tuned weights
    state_dict = torch.load(checkpoint_path, map_location=device)
    visual_encoder.load_state_dict(state_dict)
    visual_encoder.eval()
    return visual_encoder


def replace_clip_in_llava(
    llava_model: nn.Module,
    fare_clip_encoder: nn.Module,
) -> nn.Module:
    """
    Replaces the frozen CLIP vision encoder in LLaVA-1.5 with a FARE-CLIP encoder.

    LLaVA-1.5 uses the second-to-last layer outputs of CLIP ViT-L/14@224.
    No retraining of the MLP projection or Vicuna LLM is needed because
    FARE preserves the original embedding distribution on clean inputs.

    Args:
        llava_model:       LLaVA-1.5 model (loaded via HuggingFace / LLaVA repo)
        fare_clip_encoder: FARE fine-tuned CLIP visual encoder

    Returns:
        LLaVA model with FARE-CLIP encoder installed
    """
    # Freeze FARE encoder (same as original frozen CLIP in LLaVA)
    for param in fare_clip_encoder.parameters():
        param.requires_grad_(False)
    fare_clip_encoder.eval()

    # Replace vision tower — exact attribute name depends on LLaVA implementation
    # LLaVA uses model.model.vision_tower or model.vision_tower
    if hasattr(llava_model, "model") and hasattr(llava_model.model, "vision_tower"):
        llava_model.model.vision_tower.vision_tower.vision_model = fare_clip_encoder
    elif hasattr(llava_model, "vision_tower"):
        llava_model.vision_tower.vision_tower.vision_model = fare_clip_encoder
    else:
        raise AttributeError(
            "Cannot find vision_tower in LLaVA model. "
            "Check LLaVA model structure for correct attribute path."
        )
    return llava_model


def replace_clip_in_openflamingo(
    of_model: nn.Module,
    fare_clip_encoder: nn.Module,
) -> nn.Module:
    """
    Replaces the frozen CLIP vision encoder in OpenFlamingo 9B with a FARE-CLIP encoder.

    OpenFlamingo uses cross-attention to connect CLIP visual features with MPT-7B LLM.
    No retraining of cross-attention layers or MPT-7B is required.

    Args:
        of_model:          OpenFlamingo 9B model
        fare_clip_encoder: FARE fine-tuned CLIP visual encoder

    Returns:
        OpenFlamingo model with FARE-CLIP encoder installed
    """
    for param in fare_clip_encoder.parameters():
        param.requires_grad_(False)
    fare_clip_encoder.eval()

    # OpenFlamingo stores vision encoder at model.vision_encoder
    # Exact attribute depends on OpenFlamingo implementation version
    if hasattr(of_model, "vision_encoder"):
        of_model.vision_encoder = fare_clip_encoder
    else:
        raise AttributeError(
            "Cannot find vision_encoder in OpenFlamingo model. "
            "Check OpenFlamingo model structure for correct attribute path."
        )
    return of_model
