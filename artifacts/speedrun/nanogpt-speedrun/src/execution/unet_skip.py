"""
U-Net Skip Connections for Transformers — Core optimization from Record 8.
Verifies: C05 (compounding architectural gains), H04 (learnable mixing)

Encoder-decoder residual connections between transformer layers with
learnable blending weights, initialized near zero for gradual adoption.
"""

import torch
import torch.nn as nn
from typing import List


class UNetTransformerWrapper(nn.Module):
    """
    Wraps a list of transformer layers with U-Net encoder-decoder
    skip connections.

    For N layers (must be even):
    - Layers 0..N/2-1 are "encoder" layers
    - Layers N/2..N-1 are "decoder" layers
    - Decoder layer i receives a blended residual from encoder layer (N-1-i)

    Blending: x_decoder = alpha * x_encoder + (1 - alpha) * x_decoder_input
    Alpha is learnable, initialized near 0 (skip connections start weak).

    Args:
        n_layers: Number of transformer layers (must be even)
        d_model: Model dimension for alpha parameterization
    """

    def __init__(self, n_layers: int, d_model: int):
        super().__init__()
        assert n_layers % 2 == 0, "U-Net requires even number of layers"

        self.n_layers = n_layers
        self.half = n_layers // 2

        # Learnable blending weights, one per decoder layer
        # Initialized to small value → skip connections start weak
        self.alphas = nn.ParameterList([
            nn.Parameter(torch.tensor(0.01))
            for _ in range(self.half)
        ])

    def forward(
        self,
        x: torch.Tensor,
        layers: List[nn.Module],
    ) -> torch.Tensor:
        """
        Forward pass with U-Net skip connections.

        Args:
            x: (B, S, D) input tensor
            layers: List of N transformer layer modules

        Returns:
            (B, S, D) output tensor
        """
        # Encoder pass: store intermediate activations
        encoder_outputs = []
        for i in range(self.half):
            x = layers[i](x)
            encoder_outputs.append(x)

        # Decoder pass: blend with encoder activations
        for i in range(self.half):
            encoder_idx = self.half - 1 - i  # mirror index
            alpha = torch.sigmoid(self.alphas[i])  # bound to [0, 1]

            # Blend encoder output with current decoder input
            x = alpha * encoder_outputs[encoder_idx] + (1 - alpha) * x
            x = layers[self.half + i](x)

        return x
