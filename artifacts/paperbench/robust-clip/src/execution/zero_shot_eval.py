"""
Zero-shot classification evaluation for CLIP and robust variants (FARE, TeCoA).

Reference: Schlarmann et al. (2024) - §4.3, Appendix B.10
Evaluation protocol: CLIP benchmark + OpenCLIP (Cherti et al., 2023)
14 datasets: ImageNet + 13 zero-shot datasets (CalTech101, StanfordCars, CIFAR10,
CIFAR100, DTD, EuroSAT, FGVC, Flowers102, ImageNet-R, ImageNet-Sketch, PCAM,
OxfordPets, STL-10)
"""

import torch
import torch.nn.functional as F
from typing import List, Optional
import numpy as np


def build_class_text_embeddings(
    text_encoder,
    class_names: List[str],
    prompt_templates: List[str],
    device: torch.device,
) -> torch.Tensor:
    """
    Build zero-shot classification text embeddings by averaging over prompt templates.
    One embedding per class (averaged and normalized).

    From §4.3: "class names are combined with a predefined set of prompt templates.
    The resulting prompts are encoded with the CLIP text-encoder and averaged for each class"

    Args:
        text_encoder: CLIP text encoder (frozen)
        class_names: List of K class names
        prompt_templates: List of prompt template strings (e.g., ["a photo of a {}", ...])
        device: torch.device

    Returns:
        class_embeddings: L2-normalized class embeddings (K, D)
    """
    class_embeddings = []

    with torch.no_grad():
        for class_name in class_names:
            # Fill in templates and encode
            prompts = [template.format(class_name) for template in prompt_templates]
            # Tokenize and encode (implementation depends on CLIP library)
            tokens = clip_tokenize(prompts).to(device)
            embeddings = text_encoder(tokens)  # (num_templates, D)
            # Average and normalize
            mean_embedding = embeddings.mean(dim=0)
            mean_embedding = F.normalize(mean_embedding, dim=-1)
            class_embeddings.append(mean_embedding)

    return torch.stack(class_embeddings, dim=0)  # (K, D)


def zero_shot_classify(
    image_encoder,
    images: torch.Tensor,
    class_embeddings: torch.Tensor,
) -> torch.Tensor:
    """
    Zero-shot classification via cosine similarity (§3.1).

    ŷ = argmax_k cos(phi(x), psi(t_k))

    Args:
        image_encoder: CLIP vision encoder (phi, may be FARE/TeCoA fine-tuned)
        images: Input images (B, 3, H, W), values in [0, 1]
        class_embeddings: L2-normalized class text embeddings (K, D)

    Returns:
        predictions: Predicted class indices (B,)
    """
    with torch.no_grad():
        img_features = image_encoder.encode_image(images)  # (B, D), unnormalized
        img_features = F.normalize(img_features, dim=-1)   # (B, D), normalized

    logits = img_features @ class_embeddings.T  # (B, K)
    predictions = logits.argmax(dim=-1)  # (B,)
    return predictions


def evaluate_zero_shot_clean(
    image_encoder,
    dataloader,
    class_embeddings: torch.Tensor,
    device: torch.device,
) -> float:
    """
    Evaluate clean zero-shot classification accuracy.

    Args:
        image_encoder: CLIP vision encoder variant
        dataloader: Dataset dataloader returning (images, labels)
        class_embeddings: L2-normalized class embeddings (K, D)
        device: torch.device

    Returns:
        accuracy: Top-1 accuracy in [0, 100]
    """
    correct = 0
    total = 0

    image_encoder.eval()
    for images, labels in dataloader:
        images, labels = images.to(device), labels.to(device)
        predictions = zero_shot_classify(image_encoder, images, class_embeddings)
        correct += (predictions == labels).sum().item()
        total += labels.shape[0]

    return 100.0 * correct / max(total, 1)


def evaluate_zero_shot_robust(
    image_encoder,
    dataloader,
    class_embeddings: torch.Tensor,
    epsilon: float,
    attack_fn,
    device: torch.device,
    num_eval_samples: int = 1000,
) -> float:
    """
    Evaluate adversarial zero-shot classification accuracy using AutoAttack
    (APGD-CE + APGD-DLR targeted, 100 iterations each; §4.3, Appendix B.10).

    Robustness evaluation on 1000 samples per dataset.

    Args:
        image_encoder: CLIP vision encoder variant
        dataloader: Dataset dataloader
        class_embeddings: L2-normalized class embeddings (K, D)
        epsilon: ℓ∞ radius (2/255 or 4/255)
        attack_fn: AutoAttack or APGD attack function
        device: torch.device
        num_eval_samples: Number of samples for robustness eval (1000)

    Returns:
        robust_accuracy: Robust top-1 accuracy in [0, 100]
    """
    correct = 0
    total = 0

    image_encoder.eval()
    for images, labels in dataloader:
        if total >= num_eval_samples:
            break
        images, labels = images.to(device), labels.to(device)

        # Adversarial examples via attack_fn
        images_adv = attack_fn(images, labels)

        predictions = zero_shot_classify(image_encoder, images_adv, class_embeddings)
        correct += (predictions == labels).sum().item()
        total += labels.shape[0]

    return 100.0 * correct / max(total, 1)


def clip_tokenize(texts: List[str]) -> torch.Tensor:
    """
    Tokenize text prompts for CLIP text encoder.
    Implementation depends on CLIP library (OpenCLIP or OpenAI CLIP).
    """
    raise NotImplementedError("Use clip.tokenize() from OpenAI CLIP or open_clip.tokenize()")
