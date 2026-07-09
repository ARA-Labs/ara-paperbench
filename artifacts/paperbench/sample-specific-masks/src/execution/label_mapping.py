"""
Label Mapping Methods for Visual Reprogramming
Implements: ILM (Algorithm 4), FLM (Algorithm 3), RLM

Reference: Section 2.3, Appendix A.4
Paper: "Sample-specific Masks for Visual Reprogramming-based Prompting", ICML 2024
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Dict, Tuple


def compute_frequency_distribution(
    pretrained_model: nn.Module,
    fin_transform: nn.Module,
    dataloader: torch.utils.data.DataLoader,
    num_source_classes: int,
    num_target_classes: int,
    device: torch.device,
) -> torch.Tensor:
    """
    Algorithm 2: Compute frequency distribution of [fP(fin(xi|theta)), y^T].
    
    Args:
        pretrained_model: Frozen pre-trained model fP
        fin_transform:    Current input transformation fin(·|theta)
        dataloader:       Target domain training data loader
        num_source_classes: |Y^P| (e.g., 1000 for ImageNet)
        num_target_classes: |Y^T|
        device:           Computation device
    
    Returns:
        d: (|Y^P|, |Y^T|) frequency count matrix
           d[yP, yT] = count of times class yP was predicted when true label is yT
    """
    d = torch.zeros(num_source_classes, num_target_classes, dtype=torch.long)

    pretrained_model.eval()
    fin_transform.eval()

    with torch.no_grad():
        for images, target_labels in dataloader:
            images = images.to(device)
            target_labels = target_labels.to(device)

            # Apply input transformation
            reprogrammed = fin_transform(images)

            # Get source domain predictions
            source_logits = pretrained_model(reprogrammed)  # (B, |YP|)
            predicted_source = source_logits.argmax(dim=1)  # (B,)

            # Accumulate frequency counts (Algorithm 2, lines 5-7)
            for yP, yT in zip(predicted_source.cpu(), target_labels.cpu()):
                d[yP.item(), yT.item()] += 1

    return d


def compute_label_mapping_from_frequency(
    d: torch.Tensor,
    num_target_classes: int,
) -> Dict[int, int]:
    """
    Greedy label mapping from frequency distribution (used by both FLM and ILM).
    
    Implements the inner while-loop of Algorithm 3 (FLM) and Algorithm 4 (ILM).
    
    Args:
        d:                  (|YP|, |YT|) frequency matrix
        num_target_classes: |Y^T|
    
    Returns:
        mapping: dict {source_class_idx: target_class_idx} — injective mapping
                 (Y^P_sub → Y^T of size |Y^T|)
    """
    d_work = d.clone().float()
    mapping: Dict[int, int] = {}
    assigned_source: set = set()
    assigned_target: set = set()

    while len(mapping) < num_target_classes:
        # Find maximum in frequency matrix
        flat_idx = d_work.argmax().item()
        yP = flat_idx // d_work.shape[1]
        yT = flat_idx % d_work.shape[1]

        # Assign mapping: f_out(yP) = yT
        mapping[yP] = yT
        assigned_source.add(yP)
        assigned_target.add(yT)

        # Zero out row and column to prevent duplicate assignments (Algorithm 4, lines 12-13)
        d_work[yP, :] = 0.0
        d_work[:, yT] = 0.0

    return mapping


def random_label_mapping(
    num_source_classes: int,
    num_target_classes: int,
    seed: Optional[int] = None,
) -> Dict[int, int]:
    """
    Random Label Mapping (RLM): Randomly assigns source classes to target classes.
    
    Args:
        num_source_classes: |Y^P|
        num_target_classes: |Y^T|
        seed:               Optional random seed for reproducibility
    
    Returns:
        mapping: dict {source_class_idx: target_class_idx} — random injective mapping
    """
    rng = np.random.RandomState(seed)
    source_subset = rng.choice(num_source_classes, num_target_classes, replace=False)
    target_order = rng.permutation(num_target_classes)
    mapping = {int(s): int(t) for s, t in zip(source_subset, target_order)}
    return mapping


def apply_label_mapping(
    source_logits: torch.Tensor,
    mapping: Dict[int, int],
    num_target_classes: int,
    device: torch.device,
) -> torch.Tensor:
    """
    Apply label mapping to source logits to produce target predictions.
    
    For each target class yT, find the mapped source class yP and return
    the logit for yP as the score for yT. Creates a (B, |YT|) output tensor.
    
    Args:
        source_logits:      (B, |YP|) — logits from pre-trained model
        mapping:            {source_idx → target_idx}
        num_target_classes: |Y^T|
        device:             Computation device
    
    Returns:
        target_logits: (B, |YT|) — logits mapped to target classes
    """
    B = source_logits.shape[0]
    target_logits = torch.zeros(B, num_target_classes, device=device)

    # Reverse mapping: target → source
    target_to_source = {v: k for k, v in mapping.items()}

    for yT in range(num_target_classes):
        if yT in target_to_source:
            yP = target_to_source[yT]
            target_logits[:, yT] = source_logits[:, yP]

    return target_logits


from typing import Optional
