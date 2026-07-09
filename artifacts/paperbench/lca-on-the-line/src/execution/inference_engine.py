"""
Inference Engine for LCA-on-the-Line evaluation framework.

Provides unified inference for both Vision Models (VMs) and Vision-Language Models (VLMs),
outputting per-sample predictions and logits/probabilities needed for LCA computation.

Architecture component: '2. Inference Engine' (logic/solution/architecture.md)
"""
from __future__ import annotations
import numpy as np
import torch
import torch.nn.functional as F
from typing import Dict, List, Optional, Tuple, Union


def get_vm_predictions(
    model: torch.nn.Module,
    dataloader,
    device: str = "cuda",
    return_probs: bool = False,
) -> Tuple[np.ndarray, np.ndarray, Optional[np.ndarray]]:
    """
    Run inference with a Vision Model (VM) on a dataset.

    VMs use standard forward pass (image → logits) with softmax classification.
    Supports all torchvision pretrained models (ResNet, ViT, ConvNext, etc.).

    Args:
        model: Pretrained VM (torchvision model in eval mode)
        dataloader: DataLoader yielding (images, labels) batches
        device: Computation device
        return_probs: If True, also return softmax probabilities [N, K]

    Returns:
        predictions: [N] int array of predicted class indices (argmax)
        labels: [N] int array of ground-truth class indices
        probs: [N, K] float array of softmax probabilities (if return_probs=True, else None)
    """
    all_preds: List[np.ndarray] = []
    all_labels: List[np.ndarray] = []
    all_probs: List[np.ndarray] = []

    model.eval()
    with torch.no_grad():
        for images, batch_labels in dataloader:
            images = images.to(device)
            logits = model(images)                    # [B, K]
            preds = logits.argmax(dim=1).cpu().numpy()
            all_preds.append(preds)
            all_labels.append(batch_labels.numpy())
            if return_probs:
                probs = F.softmax(logits, dim=1).cpu().numpy()
                all_probs.append(probs)

    predictions = np.concatenate(all_preds)
    labels = np.concatenate(all_labels)
    probs = np.concatenate(all_probs) if return_probs else None
    return predictions, labels, probs


def get_vlm_predictions(
    model,                       # CLIP or OpenCLIP model
    preprocess,                  # CLIP/OpenCLIP preprocessing transform
    tokenizer,                   # CLIP/OpenCLIP text tokenizer
    class_names: List[str],
    dataloader,
    device: str = "cuda",
    prompt_template: str = "a photo of a {}",
    return_probs: bool = False,
) -> Tuple[np.ndarray, np.ndarray, Optional[np.ndarray]]:
    """
    Run zero-shot inference with a Vision-Language Model (VLM) on a dataset.

    VLMs use cosine similarity between image embeddings and text class embeddings.
    Supports CLIP (openai/CLIP) and OpenCLIP (mlfoundations/open_clip) interfaces.

    Args:
        model: VLM with encode_image() and encode_text() methods
        preprocess: Image preprocessing transform from CLIP/OpenCLIP
        tokenizer: Text tokenizer (clip.tokenize or open_clip.tokenize)
        class_names: List of K class name strings (e.g., ImageNet class names)
        dataloader: DataLoader yielding (images, labels) batches
        device: Computation device
        prompt_template: Format string for text prompt, e.g. "a photo of a {}"
        return_probs: If True, also return softmax probabilities [N, K]

    Returns:
        predictions: [N] int array of predicted class indices
        labels: [N] int array of ground-truth class indices
        probs: [N, K] float array of softmax probabilities (if return_probs=True, else None)
    """
    # Pre-compute text embeddings for all classes
    text_prompts = [prompt_template.format(name) for name in class_names]
    with torch.no_grad():
        text_tokens = tokenizer(text_prompts).to(device)
        text_features = model.encode_text(text_tokens)   # [K, d]
        text_features = F.normalize(text_features, dim=-1)

    all_preds: List[np.ndarray] = []
    all_labels: List[np.ndarray] = []
    all_probs: List[np.ndarray] = []

    model.eval()
    with torch.no_grad():
        for images, batch_labels in dataloader:
            images = images.to(device)
            image_features = model.encode_image(images)          # [B, d]
            image_features = F.normalize(image_features, dim=-1)
            # Cosine similarity as logits [B, K]
            logits = (image_features @ text_features.T) * 100.0
            preds = logits.argmax(dim=1).cpu().numpy()
            all_preds.append(preds)
            all_labels.append(batch_labels.numpy())
            if return_probs:
                probs = F.softmax(logits, dim=1).cpu().numpy()
                all_probs.append(probs)

    predictions = np.concatenate(all_preds)
    labels = np.concatenate(all_labels)
    probs = np.concatenate(all_probs) if return_probs else None
    return predictions, labels, probs


def compute_topk_accuracy(
    predictions_topk: np.ndarray,   # [N, K] sorted logits indices (descending)
    labels: np.ndarray,             # [N]
    k: int = 1,
) -> float:
    """
    Compute Top-K accuracy.

    Args:
        predictions_topk: [N, K_total] array of class indices sorted by logit (descending)
        labels: [N] ground-truth class indices
        k: K for top-K accuracy

    Returns:
        float: Top-K accuracy in [0, 1]
    """
    top_k_preds = predictions_topk[:, :k]              # [N, k]
    correct = (top_k_preds == labels[:, None]).any(axis=1)
    return float(correct.mean())


def build_taxonomy_parent_prompts(
    class_name: str,
    parent_chain: List[str],
    mode: str = "taxonomy_parent",
) -> str:
    """
    Build taxonomy-aligned prompts for VLM zero-shot evaluation (Section 4.3.3).

    Args:
        class_name: Leaf class name (e.g., "dalmatian")
        parent_chain: List of parent class names from direct parent to root
                      (e.g., ["dog", "animal"])
        mode: One of:
              "baseline"        -> "<class_name>"
              "stack_parent"    -> "<class>, <parent1>, <parent2>"
              "taxonomy_parent" -> "<class>, which is a type of <parent1>, which is a type of <parent2>"
              "shuffle_parent"  -> "<class>, which is a type of <random1>, which is a type of <random2>"

    Returns:
        prompt string
    """
    if mode == "baseline":
        return class_name
    elif mode == "stack_parent":
        parts = [class_name] + parent_chain
        return ", ".join(parts)
    elif mode == "taxonomy_parent":
        prompt = class_name
        for parent in parent_chain:
            prompt += f", which is a type of {parent}"
        return prompt
    elif mode == "shuffle_parent":
        # Caller is responsible for passing shuffled (wrong) parent_chain
        prompt = class_name
        for parent in parent_chain:
            prompt += f", which is a type of {parent}"
        return prompt
    else:
        raise ValueError(f"Unknown prompt mode: {mode}")
