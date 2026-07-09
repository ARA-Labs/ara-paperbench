"""
Lightweight CNN Mask Generator for SMM Visual Reprogramming

Implements the 5-layer CNN (for ResNet-18/50) and 6-layer CNN (for ViT-B32)
as described in Section 3.2 and Appendix A.2 of:
    Cai et al., "Sample-specific Masks for Visual Reprogramming-based Prompting", ICML 2024

Architecture summary:
    - All conv layers: kernel=3, padding=1, stride=1 (size-preserving)
    - MaxPool layers: kernel=2, stride=2 (halving spatial dims)
    - Final layer outputs 3 channels (three-channel mask)
    - 5-layer CNN: 3 MaxPool layers -> output size = H/8 × W/8 × 3
    - 6-layer CNN: 3 MaxPool layers -> output size = H/8 × W/8 × 3

Parameter counts:
    - 5-layer (ResNet): 26,499 parameters
    - 6-layer (ViT): 102,339 parameters
"""

import torch
import torch.nn as nn
from typing import Optional


class MaskGeneratorResNet(nn.Module):
    """
    5-layer CNN mask generator for ResNet-18 and ResNet-50 backbones.
    
    Input:  (B, 3, 224, 224) — resized target images
    Output: (B, 3, 28, 28)   — 3-channel masks at 1/8 spatial resolution
    
    Architecture (Figure 8 in paper):
        Layer 1: Conv(3->8) + BN + ReLU + MaxPool(2x2)    -> (B, 8, 112, 112)
        Layer 2: Conv(8->16) + BN + ReLU + MaxPool(2x2)   -> (B, 16, 56, 56)
        Layer 3: Conv(16->32) + BN + ReLU + MaxPool(2x2)  -> (B, 32, 28, 28)
        Layer 4: Conv(32->64) + BN + ReLU                 -> (B, 64, 28, 28)
        Layer 5: Conv(64->3)                               -> (B, 3, 28, 28)
    
    Total trainable parameters: 26,499
    """
    
    def __init__(self):
        super().__init__()
        
        # Layer 1: Conv 3->8, BN, ReLU, MaxPool
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 8, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(8),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Layer 2: Conv 8->16, BN, ReLU, MaxPool
        self.layer2 = nn.Sequential(
            nn.Conv2d(8, 16, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Layer 3: Conv 16->32, BN, ReLU, MaxPool
        self.layer3 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Layer 4: Conv 32->64, BN, ReLU (NO MaxPool)
        self.layer4 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )
        
        # Layer 5: Conv 64->3 (final output, NO BN, NO activation)
        self.layer5 = nn.Conv2d(64, 3, kernel_size=3, padding=1, stride=1)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Resized target images, shape (B, 3, 224, 224)
        
        Returns:
            Three-channel mask at 1/8 resolution, shape (B, 3, 28, 28)
        """
        x = self.layer1(x)  # (B, 8, 112, 112)
        x = self.layer2(x)  # (B, 16, 56, 56)
        x = self.layer3(x)  # (B, 32, 28, 28)
        x = self.layer4(x)  # (B, 64, 28, 28)
        x = self.layer5(x)  # (B, 3, 28, 28)
        return x


class MaskGeneratorViT(nn.Module):
    """
    6-layer CNN mask generator for ViT-B32 backbone.
    
    Input:  (B, 3, 384, 384) — resized target images (ViT input size)
    Output: (B, 3, 48, 48)   — 3-channel masks at 1/8 spatial resolution
    
    Architecture (Figure 9 in paper):
        Layer 1: Conv(3->8) + BN + ReLU + MaxPool(2x2)     -> (B, 8, 192, 192)
        Layer 2: Conv(8->16) + BN + ReLU + MaxPool(2x2)    -> (B, 16, 96, 96)
        Layer 3: Conv(16->32) + BN + ReLU + MaxPool(2x2)   -> (B, 32, 48, 48)
        Layer 4: Conv(32->64) + BN + ReLU                  -> (B, 64, 48, 48)
        Layer 5: Conv(64->128) + BN + ReLU                 -> (B, 128, 48, 48)
        Layer 6: Conv(128->3)                               -> (B, 3, 48, 48)
    
    Total trainable parameters: 102,339
    """
    
    def __init__(self):
        super().__init__()
        
        # Layer 1: Conv 3->8, BN, ReLU, MaxPool
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 8, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(8),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Layer 2: Conv 8->16, BN, ReLU, MaxPool
        self.layer2 = nn.Sequential(
            nn.Conv2d(8, 16, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Layer 3: Conv 16->32, BN, ReLU, MaxPool
        self.layer3 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Layer 4: Conv 32->64, BN, ReLU (NO MaxPool)
        self.layer4 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )
        
        # Layer 5: Conv 64->128, BN, ReLU (NO MaxPool)
        self.layer5 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
        )
        
        # Layer 6: Conv 128->3 (final output, NO BN, NO activation)
        self.layer6 = nn.Conv2d(128, 3, kernel_size=3, padding=1, stride=1)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Resized target images, shape (B, 3, 384, 384)
        
        Returns:
            Three-channel mask at 1/8 resolution, shape (B, 3, 48, 48)
        """
        x = self.layer1(x)  # (B, 8, 192, 192)
        x = self.layer2(x)  # (B, 16, 96, 96)
        x = self.layer3(x)  # (B, 32, 48, 48)
        x = self.layer4(x)  # (B, 64, 48, 48)
        x = self.layer5(x)  # (B, 128, 48, 48)
        x = self.layer6(x)  # (B, 3, 48, 48)
        return x


def build_mask_generator(backbone: str) -> nn.Module:
    """
    Factory function: returns the appropriate mask generator for a given backbone.
    
    Args:
        backbone: One of 'resnet18', 'resnet50', 'vit_b32'
    
    Returns:
        Initialized mask generator CNN (with PyTorch default random initialization)
    """
    if backbone in ('resnet18', 'resnet50'):
        return MaskGeneratorResNet()
    elif backbone == 'vit_b32':
        return MaskGeneratorViT()
    else:
        raise ValueError(f"Unknown backbone: {backbone}. Use 'resnet18', 'resnet50', or 'vit_b32'")


def build_delta(backbone: str, device: str = 'cuda') -> torch.Tensor:
    """
    Build the shared pattern delta, initialized to zeros.
    
    Args:
        backbone: Determines input size — 224×224 for ResNet, 384×384 for ViT
        device: 'cuda' or 'cpu'
    
    Returns:
        Zero-initialized tensor of shape (1, 3, H_P, W_P) with requires_grad=True
    """
    if backbone in ('resnet18', 'resnet50'):
        shape = (1, 3, 224, 224)
    elif backbone == 'vit_b32':
        shape = (1, 3, 384, 384)
    else:
        raise ValueError(f"Unknown backbone: {backbone}")
    
    delta = torch.zeros(shape, device=device, requires_grad=True)
    return delta
