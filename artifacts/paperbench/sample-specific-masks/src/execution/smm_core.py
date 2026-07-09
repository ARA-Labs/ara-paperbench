"""
SMM Core: AttributeNet (mask generator) + InstancewiseVisualPrompt
Source: instance_model.py from https://github.com/tmlr-group/SMM
"""

import torch
import torch.nn as nn


class AttributeNet(nn.Module):
    """
    Lightweight CNN mask generator (fmask) for SMM.

    Produces a sample-specific 3-channel mask from a resized input image.
    Spatial downsampling is controlled by patch_size (number of MaxPool layers
    determines how many times spatial dims are halved).

    Args:
        layers (int): Number of CNN layers; 5 for ResNet backbones, 6 for ViT
        patch_size (int): Size of spatial patches in output; must be in
                          {1, 2, 4, 8, 16, 32}. Equals 2^(number of MaxPool layers used).
        channels (int): Output channels; 3 for RGB-specific masks, 1 for shared mask

    Input shape:  (B, 3, H, W)   — resized target image, H=W=224 (ResNet) or 384 (ViT)
    Output shape: (B, channels, H/patch_size, W/patch_size)
    """

    def __init__(self, layers: int = 5, patch_size: int = 8, channels: int = 3):
        super(AttributeNet, self).__init__()
        self.layers = layers
        self.patch_size = patch_size
        self.channels = channels

        self.pooling = nn.MaxPool2d(2, 2)

        # Layer 1: 3 → 8
        self.conv1 = nn.Conv2d(3, 8, 3, 1, 1)
        self.bn1 = nn.BatchNorm2d(8)
        self.relu1 = nn.ReLU(inplace=True)

        # Layer 2: 8 → 16
        self.conv2 = nn.Conv2d(8, 16, 3, 1, 1)
        self.bn2 = nn.BatchNorm2d(16)
        self.relu2 = nn.ReLU(inplace=True)

        # Layer 3: 16 → 32
        self.conv3 = nn.Conv2d(16, 32, 3, 1, 1)
        self.bn3 = nn.BatchNorm2d(32)
        self.relu3 = nn.ReLU(inplace=True)

        # Layer 4: 32 → 64
        self.conv4 = nn.Conv2d(32, 64, 3, 1, 1)
        self.bn4 = nn.BatchNorm2d(64)
        self.relu4 = nn.ReLU(inplace=True)

        # Layer 5 (final for 5-layer) OR intermediate for 6-layer
        if self.layers == 5 and self.channels == 3:
            self.conv6 = nn.Conv2d(64, 3, 3, 1, 1)  # output layer
        elif self.layers == 6:
            self.conv5 = nn.Conv2d(64, 128, 3, 1, 1)
            self.bn5 = nn.BatchNorm2d(128)
            self.relu5 = nn.ReLU(inplace=True)
            if self.channels == 3:
                self.conv6 = nn.Conv2d(128, 3, 3, 1, 1)  # output layer

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, 3, H, W) — resized input image

        Returns:
            y: (B, channels, H/patch_size, W/patch_size)
               Each spatial location encodes a mask value for a patch_size×patch_size block.
        """
        # Conv block 1: pool if patch_size >= 2
        y = self.relu1(self.bn1(self.conv1(x)))
        if self.patch_size in [2, 4, 8, 16, 32]:
            y = self.pooling(y)   # H/2

        # Conv block 2: pool if patch_size >= 4
        y = self.relu2(self.bn2(self.conv2(y)))
        if self.patch_size in [4, 8, 16, 32]:
            y = self.pooling(y)   # H/4

        # Conv block 3: pool if patch_size >= 8
        y = self.relu3(self.bn3(self.conv3(y)))
        if self.patch_size in [8, 16, 32]:
            y = self.pooling(y)   # H/8

        # Conv block 4: pool if patch_size >= 16
        y = self.relu4(self.bn4(self.conv4(y)))
        if self.patch_size in [16, 32]:
            y = self.pooling(y)   # H/16

        # Optional 6th layer (ViT)
        if self.layers == 6:
            y = self.relu5(self.bn5(self.conv5(y)))
            if self.patch_size == 32:
                y = self.pooling(y)  # H/32

        # Output projection to 3 (or 1) channels
        if self.channels == 3:
            y = self.conv6(y)
        elif self.channels == 1:
            y = torch.mean(y, dim=1)  # average channels → single channel mask

        return y


class InstancewiseVisualPrompt(nn.Module):
    """
    SMM visual prompt: combines sample-specific mask from AttributeNet with
    shared learnable pattern delta.

    Forward: x_reprog = x + delta * patchwise_upsample(fmask(x))

    Args:
        size (int): Input image size (H=W); 224 for ResNet, 384 for ViT
        layers (int): AttributeNet depth; 5 (ResNet) or 6 (ViT)
        patch_size (int): Upsampling block size; default 8
        channels (int): Mask channels; 3 (default) or 1

    Input shape:  (B, 3, size, size)
    Output shape: (B, 3, size, size) — reprogrammed image
    """

    def __init__(self, size: int, layers: int = 5, patch_size: int = 8, channels: int = 3):
        super(InstancewiseVisualPrompt, self).__init__()

        if layers not in [5, 6]:
            raise ValueError("layers must be 5 or 6")
        if patch_size not in [1, 2, 4, 8, 16, 32]:
            raise ValueError("patch_size must be in {1,2,4,8,16,32}")
        if channels not in [1, 3]:
            raise ValueError("channels must be 1 or 3")
        if patch_size == 32 and layers != 6:
            raise ValueError("patch_size=32 requires layers=6")

        self.patch_num = int(size / patch_size)   # number of patches per spatial dim
        self.imagesize = size
        self.patch_size = patch_size
        self.channels = channels

        # Mask generator (fmask)
        self.priority = AttributeNet(layers, patch_size, channels)

        # Shared learnable pattern delta — initialized to zeros (key heuristic)
        self.program = nn.Parameter(data=torch.zeros(3, size, size))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, 3, H, W) — resized target-domain image (ImageNet-normalized)

        Returns:
            (B, 3, H, W) — reprogrammed image: x + delta * mask
        """
        # Step 1: Generate small mask via AttributeNet
        # attention shape: (B, channels, patch_num, patch_num)
        attention = self.priority(x)

        # Step 2: Patch-wise interpolation (expand each value to patch_size×patch_size block)
        # Reshape: (B, channels, patch_num^2, 1) → expand to (B, 3, patch_num^2, patch_size^2)
        # → view to (B, 3, patch_num, patch_num, patch_size, patch_size)
        # → transpose → reshape to (B, 3, H, W)
        attention = (
            attention
            .view(-1, self.channels, self.patch_num * self.patch_num, 1)
            .expand(-1, 3, -1, self.patch_size * self.patch_size)
            .view(-1, 3, self.patch_num, self.patch_num, self.patch_size, self.patch_size)
            .transpose(3, 4)
            .reshape(-1, 3, self.imagesize, self.imagesize)
        )

        # Step 3: Add masked pattern to image
        x = x + self.program * attention
        return x
