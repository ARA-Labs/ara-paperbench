"""
SMM: Sample-specific Multi-channel Masks for Visual Reprogramming
Core implementation: MaskGenerator CNN + PatchWiseInterpolation + SMMTransform

Architecture reference: Section 3, Appendix A.2
Paper: "Sample-specific Masks for Visual Reprogramming-based Prompting", ICML 2024
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple, Optional


class MaskGeneratorResNet(nn.Module):
    """
    5-layer lightweight CNN mask generator for ResNet backbones (224×224 input).
    
    Input:  Tensor of shape (B, 3, 224, 224) — resized target images r(xi)
    Output: Tensor of shape (B, 3, 28, 28)  — 3-channel masks at H/8 × W/8
    
    Architecture (Appendix A.2, Figure 8):
      Conv(3→8)+BN+ReLU+MaxPool → Conv(8→16)+BN+ReLU+MaxPool →
      Conv(16→32)+BN+ReLU+MaxPool → Conv(32→64)+BN+ReLU → Conv(64→3)
    All convolutions: kernel=3, padding=1, stride=1
    All max-pooling: kernel=2, stride=2
    Total parameters: 26,499
    """

    def __init__(self) -> None:
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 8, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(8),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(8, 16, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer3 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer4 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )
        self.layer5 = nn.Conv2d(64, 3, kernel_size=3, padding=1, stride=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, 3, 224, 224) — resized target images
        Returns:
            mask: (B, 3, 28, 28) — low-resolution 3-channel mask
        """
        x = self.layer1(x)   # → (B, 8, 112, 112)
        x = self.layer2(x)   # → (B, 16, 56, 56)
        x = self.layer3(x)   # → (B, 32, 28, 28)
        x = self.layer4(x)   # → (B, 64, 28, 28)
        x = self.layer5(x)   # → (B, 3, 28, 28)
        return x


class MaskGeneratorViT(nn.Module):
    """
    6-layer lightweight CNN mask generator for ViT-B32 (384×384 input).
    
    Input:  Tensor of shape (B, 3, 384, 384) — resized target images r(xi)
    Output: Tensor of shape (B, 3, 48, 48)   — 3-channel masks at H/8 × W/8
    
    Architecture (Appendix A.2, Figure 9):
      Conv(3→8)+BN+ReLU+MaxPool → Conv(8→16)+BN+ReLU+MaxPool →
      Conv(16→32)+BN+ReLU+MaxPool → Conv(32→64)+BN+ReLU →
      Conv(64→128)+BN+ReLU → Conv(128→3)
    Total parameters: 102,339
    """

    def __init__(self) -> None:
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 8, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(8),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(8, 16, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer3 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer4 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )
        self.layer5 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
        )
        self.layer6 = nn.Conv2d(128, 3, kernel_size=3, padding=1, stride=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, 3, 384, 384) — resized target images
        Returns:
            mask: (B, 3, 48, 48) — low-resolution 3-channel mask
        """
        x = self.layer1(x)   # → (B, 8, 192, 192)
        x = self.layer2(x)   # → (B, 16, 96, 96)
        x = self.layer3(x)   # → (B, 32, 48, 48)
        x = self.layer4(x)   # → (B, 64, 48, 48)
        x = self.layer5(x)   # → (B, 128, 48, 48)
        x = self.layer6(x)   # → (B, 3, 48, 48)
        return x


def patch_wise_interpolate(
    mask: torch.Tensor,
    target_h: int,
    target_w: int,
    l: int
) -> torch.Tensor:
    """
    Patch-wise interpolation: upscales mask from H/2^l × W/2^l to H × W.
    Each low-resolution pixel is replicated to fill a 2^l × 2^l patch.
    Non-divisible boundary cases use nearest-patch mirroring.
    
    No floating-point arithmetic; no backpropagation required through this op.
    
    Args:
        mask:     (B, C, H_small, W_small) — CNN output mask
        target_h: H — target height (= H_small * 2^l, possibly with rounding)
        target_w: W — target width  (= W_small * 2^l, possibly with rounding)
        l:        number of MaxPool layers (patch size = 2^l)
    
    Returns:
        upsampled: (B, C, target_h, target_w) — patch-replicated mask
    
    Reference: Section 3.3, Appendix A.3
    """
    patch_size = 2 ** l
    # Nearest-neighbor upsampling implements patch-wise replication exactly
    # (each value copied to patch_size × patch_size block)
    with torch.no_grad():
        upsampled = F.interpolate(
            mask,
            size=(target_h, target_w),
            mode='nearest'
        )
    return upsampled


class SMMTransform(nn.Module):
    """
    Full SMM input transformation: fin(xi|phi, delta) = r(xi) + delta ⊙ fmask(r(xi)|phi)
    
    Implements Algorithm 1 forward pass (Steps 1 and 2).
    
    Args:
        backbone_type: 'resnet' (5-layer CNN, 224×224) or 'vit' (6-layer CNN, 384×384)
        num_pool_layers: l — number of MaxPool layers (default=3, patch_size=8)
    """

    def __init__(self, backbone_type: str = 'resnet', num_pool_layers: int = 3) -> None:
        super().__init__()
        self.backbone_type = backbone_type
        self.l = num_pool_layers

        if backbone_type == 'resnet':
            self.input_h = self.input_w = 224
            self.fmask = MaskGeneratorResNet()
        elif backbone_type == 'vit':
            self.input_h = self.input_w = 384
            self.fmask = MaskGeneratorViT()
        else:
            raise ValueError(f"Unknown backbone_type: {backbone_type}")

        # Shared learnable pattern delta, initialized to zeros (Algorithm 1, line 3)
        self.delta = nn.Parameter(
            torch.zeros(1, 3, self.input_h, self.input_w),
            requires_grad=True
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply SMM input transformation.
        
        Args:
            x: (B, 3, input_h, input_w) — resized target images r(xi)
               (bilinear upsampling to model input size should be applied before calling)
        
        Returns:
            fin: (B, 3, input_h, input_w) — reprogrammed images
                 = r(xi) + delta ⊙ fmask(r(xi)|phi) (after patch interpolation)
        """
        # Step 1: Generate sample-specific masks via CNN
        # mask_small: (B, 3, H/2^l, W/2^l)
        mask_small = self.fmask(x)

        # Step 2: Patch-wise interpolation to match input size
        if self.l > 0:
            mask = patch_wise_interpolate(
                mask_small, self.input_h, self.input_w, self.l
            )  # (B, 3, input_h, input_w)
        else:
            mask = mask_small  # no upsampling needed when l=0

        # Step 3: Apply masked pattern: r(xi) + delta ⊙ mask
        fin = x + self.delta * mask  # broadcast delta over batch
        return fin


def smm_train_step(
    smm_transform: SMMTransform,
    pretrained_model: nn.Module,
    images: torch.Tensor,
    labels: torch.Tensor,
    label_mapping: dict,
    optimizer_delta: torch.optim.Optimizer,
    optimizer_phi: torch.optim.Optimizer,
    criterion: nn.Module,
) -> torch.Tensor:
    """
    Single training step for SMM (Algorithm 1, inner loop body).
    
    Args:
        smm_transform:    SMMTransform instance (contains delta and fmask)
        pretrained_model: Frozen pre-trained classifier fP
        images:           (B, 3, H, W) — resized target images r(xi)
        labels:           (B,) — target domain labels
        label_mapping:    dict mapping source class index → target class index (ILM)
        optimizer_delta:  Optimizer for delta parameter
        optimizer_phi:    Optimizer for fmask parameters (phi)
        criterion:        Loss function (cross-entropy)
    
    Returns:
        loss: scalar training loss
    """
    optimizer_delta.zero_grad()
    optimizer_phi.zero_grad()

    # Apply SMM transformation: fin(xi) = r(xi) + delta ⊙ fmask(r(xi)|phi)
    reprogrammed = smm_transform(images)  # (B, 3, H, W)

    # Forward pass through frozen pre-trained model
    with torch.no_grad():
        source_logits = pretrained_model(reprogrammed)  # (B, |YP|)

    # Extract logits for the mapped subset Y^P_sub and map to target labels
    # (Assumes label_mapping is applied externally to get target predictions)
    # ... label mapping application omitted here; see label_mapping.py

    loss = criterion(source_logits, labels)
    loss.backward()
    optimizer_delta.step()
    optimizer_phi.step()

    return loss


class SingleChannelSMM(nn.Module):
    """
    Ablation variant: Single-channel SMM (f^s_mask).
    Averages the penultimate-layer output of the mask generator to produce a 1-channel mask,
    then broadcasts to 3 channels.
    
    Used in ablation study (Table 3, column 'Single-Channel f^s_mask').
    fin(xi) = r(xi) + delta ⊙ f^s_mask(r(xi))
    """

    def __init__(self, backbone_type: str = 'resnet', num_pool_layers: int = 3) -> None:
        super().__init__()
        self.l = num_pool_layers
        if backbone_type == 'resnet':
            self.input_h = self.input_w = 224
        else:
            self.input_h = self.input_w = 384
        # Use same architecture but keep track of penultimate layer
        self.smm_base = SMMTransform(backbone_type, num_pool_layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Average the 3-channel mask to single channel, then apply."""
        mask_small = self.smm_base.fmask(x)           # (B, 3, H_s, W_s)
        mask_single = mask_small.mean(dim=1, keepdim=True)  # (B, 1, H_s, W_s)
        mask_3ch = mask_single.expand(-1, 3, -1, -1)        # (B, 3, H_s, W_s)
        if self.l > 0:
            mask = patch_wise_interpolate(mask_3ch, self.input_h, self.input_w, self.l)
        else:
            mask = mask_3ch
        return x + self.smm_base.delta * mask
