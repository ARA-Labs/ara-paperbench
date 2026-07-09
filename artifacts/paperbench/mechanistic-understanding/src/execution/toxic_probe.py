"""
Toxicity Probe Training for GPT2-medium.

Implements Section 3.1: Train a linear probe W_Toxic ∈ R^d to classify
residual streams as toxic or non-toxic using the Jigsaw dataset.

The probe operates on the averaged last-layer residual stream:
    P(Toxic | x_bar^{L-1}) = softmax(W_Toxic @ x_bar^{L-1})
"""

import torch
import torch.nn as nn
from torch import Tensor
from typing import Tuple, Iterator


class ToxicityProbe(nn.Module):
    """
    Linear probe for toxicity classification.

    Trains W_Toxic ∈ R^{d x 2} where the classifier maps
    averaged last-layer residual streams to binary toxic/non-toxic labels.

    Input: x_bar ∈ R^d (averaged residual stream at layer L-1)
    Output: logits ∈ R^2 (non-toxic, toxic)
    """

    def __init__(self, hidden_dim: int = 1024) -> None:
        """
        Args:
            hidden_dim: d=1024 for GPT2-medium.
        """
        super().__init__()
        # W_Toxic ∈ R^{d x 2}: columns are [non-toxic, toxic] directions
        self.linear = nn.Linear(hidden_dim, 2, bias=False)

    def forward(self, x_bar: Tensor) -> Tensor:
        """
        Args:
            x_bar: Tensor of shape [batch, d] — averaged last-layer residual stream.
        Returns:
            logits: Tensor of shape [batch, 2]
        """
        return self.linear(x_bar)

    @property
    def toxic_direction(self) -> Tensor:
        """
        Returns W_Toxic ∈ R^d — the toxic classification vector.
        This is the weight column corresponding to the toxic class.
        Shape: [d]
        """
        return self.linear.weight[1]  # toxic class direction


def extract_last_layer_residual(
    model: "GPT2Model",
    input_ids: Tensor,
    device: torch.device,
) -> Tensor:
    """
    Extract mean residual stream at layer L-1 for toxicity probe training.

    Args:
        model: GPT2-medium model with output_hidden_states=True.
        input_ids: Tensor of shape [batch, seq_len].
        device: Target device.
    Returns:
        x_bar: Tensor of shape [batch, d] — mean residual stream at last layer.
    """
    with torch.no_grad():
        outputs = model(input_ids.to(device), output_hidden_states=True)
    # hidden_states: tuple of (L+1) tensors, each [batch, seq_len, d]
    last_layer = outputs.hidden_states[-1]  # [batch, seq_len, d]
    x_bar = last_layer.mean(dim=1)  # average over timesteps → [batch, d]
    return x_bar


def train_probe(
    probe: ToxicityProbe,
    data_loader: Iterator,
    model: "GPT2Model",
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    num_epochs: int,
) -> Tuple[ToxicityProbe, float]:
    """
    Train the toxicity probe on Jigsaw dataset representations.

    Training procedure (Section 3.1):
    - 90:10 train/validation split of Jigsaw dataset (561,808 comments)
    - Train on averaged last-layer residual stream x_bar^{L-1}
    - Expected validation accuracy: ~94%

    Args:
        probe: ToxicityProbe model.
        data_loader: Yields (input_ids, labels) batches.
        model: Frozen GPT2-medium for representation extraction.
        optimizer: e.g., Adam or SGD.
        device: Computation device.
        num_epochs: Number of training epochs.
    Returns:
        Trained probe and final validation accuracy.
    """
    criterion = nn.CrossEntropyLoss()
    probe.train()

    for epoch in range(num_epochs):
        total_loss = 0.0
        for input_ids, labels in data_loader:
            x_bar = extract_last_layer_residual(model, input_ids, device)
            logits = probe(x_bar.to(device))
            loss = criterion(logits, labels.to(device))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

    # Return trained probe and placeholder accuracy (compute externally on val set)
    val_accuracy = evaluate_probe(probe, data_loader, model, device)
    return probe, val_accuracy


def evaluate_probe(
    probe: ToxicityProbe,
    val_loader: Iterator,
    model: "GPT2Model",
    device: torch.device,
) -> float:
    """
    Evaluate probe accuracy on validation split.

    Args:
        probe: Trained ToxicityProbe.
        val_loader: Validation data loader.
        model: Frozen GPT2-medium.
        device: Computation device.
    Returns:
        Accuracy (float in [0, 1]). Expected: ~0.94.
    """
    probe.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for input_ids, labels in val_loader:
            x_bar = extract_last_layer_residual(model, input_ids, device)
            logits = probe(x_bar.to(device))
            preds = logits.argmax(dim=-1)
            correct += (preds == labels.to(device)).sum().item()
            total += labels.size(0)
    return correct / total
