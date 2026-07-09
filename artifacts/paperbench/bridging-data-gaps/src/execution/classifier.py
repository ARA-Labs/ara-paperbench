"""
Binary Domain Classifier for TAN Similarity-Guided Training

This module implements the binary domain classifier p_φ(y|x_t) described in §4.1.
The classifier is pre-trained on ImageNet and fine-tuned on 10 target-domain images
to distinguish source (y=S) from target (y=T) images at any noise level t.

During TAN training, only the gradient ∇_{x_t} log p_φ(y=T|x_t) is needed.
The classifier is frozen during DPM fine-tuning.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional


class BinaryDomainClassifier(nn.Module):
    """
    Binary classifier p_φ(y|x_t) to distinguish source and target domain images.

    Architecture:
        - ImageNet pre-trained backbone (e.g., ResNet-50 or similar)
        - Binary classification head (2 output classes: source=0, target=1)
        - Fine-tuned on 10 target-domain images (mixed with source images)
        - Frozen during DPM fine-tuning

    The classifier operates on noisy images x_t at arbitrary noise levels t,
    enabling domain-gap estimation without requiring clean generated images.
    """

    def __init__(self, backbone: nn.Module, feature_dim: int, num_classes: int = 2):
        """
        Args:
            backbone:     Pre-trained feature extractor (e.g., ImageNet-pretrained ResNet)
            feature_dim:  Dimension of backbone output features
            num_classes:  Number of output classes (2: source vs. target)
        """
        super().__init__()
        self.backbone = backbone
        self.head = nn.Linear(feature_dim, num_classes)

    def forward(self, x_t: torch.Tensor) -> torch.Tensor:
        """
        Compute log-probabilities for source/target domain.

        Args:
            x_t: Noisy image at timestep t, shape (B, C, H, W)

        Returns:
            Log-probabilities (B, 2): [:, 0] = log p(y=S|x_t),
                                       [:, 1] = log p(y=T|x_t)
        """
        features = self.backbone(x_t)
        logits = self.head(features)
        return F.log_softmax(logits, dim=-1)

    def get_target_grad(self, x_t: torch.Tensor) -> torch.Tensor:
        """
        Compute ∇_{x_t} log p_φ(y=T|x_t) — the similarity guidance signal.

        This gradient points in the direction that makes x_t more target-like.
        Used in the TAN training loss (Eq. 6 and Eq. 9).

        The source term p_φ(y=S|x_t) is discarded (near zero for target images;
        its gradient is large and chaotic — see §4.1).

        Args:
            x_t: Noisy image at timestep t, shape (B, C, H, W)

        Returns:
            Gradient tensor of shape (B, C, H, W): ∇_{x_t} log p_φ(y=T|x_t)
        """
        x_t_in = x_t.detach().requires_grad_(True)
        log_prob_target = self.forward(x_t_in)[:, 1].sum()  # sum over batch
        grad = torch.autograd.grad(log_prob_target, x_t_in)[0]
        return grad.detach()


def train_classifier(
    classifier: BinaryDomainClassifier,
    source_images: torch.Tensor,   # (N_s, C, H, W) — noisy source images at t
    target_images: torch.Tensor,   # (N_t, C, H, W) — noisy target images at t (10-shot)
    num_epochs: int = 100,
    lr: float = 1e-4,
) -> BinaryDomainClassifier:
    """
    Fine-tune the binary classifier on 10 target-domain images + source images.

    The classifier is trained to distinguish x_t from source domain (label=0)
    vs. target domain (label=1) at various noise levels.

    After training, the classifier is frozen for use as a guidance signal.

    Args:
        classifier:     BinaryDomainClassifier with ImageNet-pretrained backbone
        source_images:  Sample of source domain images
        target_images:  10-shot target domain images
        num_epochs:     Number of fine-tuning epochs
        lr:             Learning rate for fine-tuning

    Returns:
        Trained (and subsequently frozen) classifier.
    """
    optimizer = torch.optim.Adam(classifier.parameters(), lr=lr)

    source_labels = torch.zeros(len(source_images), dtype=torch.long)
    target_labels = torch.ones(len(target_images), dtype=torch.long)

    images = torch.cat([source_images, target_images], dim=0)
    labels = torch.cat([source_labels, target_labels], dim=0)

    for epoch in range(num_epochs):
        # Shuffle
        perm = torch.randperm(len(images))
        images_shuf, labels_shuf = images[perm], labels[perm]

        log_probs = classifier(images_shuf)
        loss = F.nll_loss(log_probs, labels_shuf)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Freeze classifier for use as guidance signal
    for param in classifier.parameters():
        param.requires_grad = False

    return classifier
