"""
PromptViT — Vision Transformer with Learnable Input Prompt Injection
Paper: "Test-Time Model Adaptation with Only Forward Passes" (ICML 2024)
Source: models/vpt.py

Wraps a timm VisionTransformer by injecting Np learnable prompt embeddings
at the input sequence (after CLS token, before patch embeddings).
All original ViT weights are kept frozen during TTA.
"""

import math
import torch
import torch.nn as nn
from functools import reduce
from operator import mul

from timm.models.vision_transformer import VisionTransformer


class PromptViT(nn.Module):
    """ViT extended with learnable prompts at input layer.
    
    Prompt injection (after patch_embed + _pos_embed):
        Original: [CLS, patch_1, patch_2, ..., patch_m]
        With prompts: [CLS, p_1, ..., p_Np, patch_1, ..., patch_m]
    
    During TTA:
        - vit parameters: FROZEN (requires_grad=False)
        - prompts: updated by CMA-ES (no backprop needed)
    
    Args:
        vit: Pre-trained timm VisionTransformer instance
        num_prompts: Np, number of learnable prompt embeddings (default 3)
    """

    def __init__(self, vit: VisionTransformer, num_prompts: int = 3):
        super().__init__()
        self.vit = vit
        self.num_prompts = num_prompts
        self.prompt_dim = vit.embed_dim  # d = 768 for ViT-Base

        if num_prompts > 0:
            # Xavier uniform initialization (from VPT, Jia et al. 2022)
            # val = sqrt(6 / (3 * patch_size^2 + d))
            val = math.sqrt(6.0 / float(
                3 * reduce(mul, vit.patch_embed.patch_size, 1) + self.prompt_dim
            ))
            self.prompts = nn.Parameter(torch.zeros(1, num_prompts, self.prompt_dim))
            nn.init.uniform_(self.prompts.data, -val, val)

    def reset(self) -> None:
        """Re-initialize prompts with Xavier uniform (called between domains)."""
        val = math.sqrt(6.0 / float(
            3 * reduce(mul, self.vit.patch_embed.patch_size, 1) + self.prompt_dim
        ))
        nn.init.uniform_(self.prompts.data, -val, val)

    def prompt_injection(self, x: torch.Tensor) -> torch.Tensor:
        """Inject prompts into patch embedding sequence.
        
        Args:
            x: Patch embeddings with CLS, shape (B, 1+m, d)
        Returns:
            Extended sequence: (B, 1+Np+m, d)
        """
        if self.num_prompts > 0:
            # [CLS token | Np prompts | m patch embeddings]
            x = torch.cat((
                x[:, :1, :],                            # CLS token
                self.prompts.expand(x.shape[0], -1, -1),  # (B, Np, d)
                x[:, 1:, :]                             # patch embeddings
            ), dim=1)
        return x

    def forward_features(self, x: torch.Tensor) -> torch.Tensor:
        """Standard ViT forward with prompts injected.
        
        Args:
            x: Input images, shape (B, 3, H, W)
        Returns:
            Final layer output including CLS, shape (B, 1+Np+m, d)
        """
        x = self.vit.patch_embed(x)       # (B, m, d)
        x = self.vit._pos_embed(x)        # (B, 1+m, d) with CLS and positional embedding
        x = self.prompt_injection(x)      # (B, 1+Np+m, d) — key innovation
        x = self.vit.norm_pre(x)
        x = self.vit.blocks(x)
        x = self.vit.norm(x)
        return x

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Full forward pass with prompts.
        
        Args:
            x: Input images, shape (B, 3, H, W)
        Returns:
            Classification logits, shape (B, C)
        """
        x = self.forward_features(x)
        x = self.vit.forward_head(x)
        return x

    def _collect_layers_features(self, x: torch.Tensor) -> torch.Tensor:
        """Collect normalized CLS features from ALL N transformer layers.
        
        Used for computing source statistics and fitness function (Eqn. 5).
        
        Args:
            x: Token sequence after positional embedding, shape (B, seq_len, d)
        Returns:
            Concatenated per-layer CLS features, shape (B, N*d)
            where N=12 for ViT-Base, d=768
        """
        cls_features = []
        for i in range(len(self.vit.blocks)):
            x = self.vit.blocks[i](x)
            if i < len(self.vit.blocks) - 1:
                # Intermediate layers: apply next layer's norm1 to CLS
                cls_features.append(self.vit.blocks[i + 1].norm1(x[:, 0]))
            else:
                # Final layer: apply final layer norm
                cls_features.append(self.vit.norm(x[:, 0]))
        return torch.cat(cls_features, dim=1)  # (B, N*d)

    def layers_cls_features(self, x: torch.Tensor) -> torch.Tensor:
        """CLS features from all layers WITHOUT prompts (for source statistics).
        
        Used in obtain_origin_stat() to compute {μ_i^S, σ_i^S}_{i=0}^N.
        
        Args:
            x: Input images, shape (B, 3, H, W)
        Returns:
            Concatenated CLS features, shape (B, N*d)
        """
        x = self.vit.patch_embed(x)
        x = self.vit._pos_embed(x)
        x = self.vit.norm_pre(x)
        return self._collect_layers_features(x)

    def layers_cls_features_with_prompts(self, x: torch.Tensor) -> torch.Tensor:
        """CLS features from all layers WITH current prompts.
        
        Used during TTA: fitness evaluation and activation shifting.
        
        Args:
            x: Input images, shape (B, 3, H, W)
        Returns:
            Concatenated CLS features, shape (B, N*d)
        """
        x = self.vit.patch_embed(x)
        x = self.vit._pos_embed(x)
        x = self.prompt_injection(x)     # inject prompts
        x = self.vit.norm_pre(x)
        return self._collect_layers_features(x)
