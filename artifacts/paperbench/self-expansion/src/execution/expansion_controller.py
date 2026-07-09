"""
SEMA Expansion Controller: Z-score based self-expansion strategy.

Implements the task-oriented, shallow-to-deep scanning procedure described
in Section 3.6 of Wang et al. (arXiv:2403.18886v3).

Key algorithm:
1. For each new task, scan expansion-eligible layers shallow → deep
2. At each layer, compute z-scores from all existing RDs
3. If ALL z-scores > threshold τ: trigger expansion (add new modular adapter)
4. If no layer triggers: skip task (reuse frozen adapters, no training)
"""
import torch
import torch.nn as nn
from typing import List, Dict, Optional, Tuple
from src.execution.sema_model import SEMALayer, RepresentationDescriptor


def compute_layer_zscore(
    rd: RepresentationDescriptor,
    x_features: torch.Tensor
) -> float:
    """
    Compute z-score for a single representation descriptor given input features.

    z = (r - mu) / sigma  (Section 3.6)

    Args:
        rd: Frozen representation descriptor
        x_features: Pre-MLP features [B, N, d_model]
    Returns:
        Mean z-score (scalar float)
    """
    with torch.no_grad():
        z = rd.compute_zscore(x_features)
    return z


def detect_expansion_signal(
    sema_layer: SEMALayer,
    x_features: torch.Tensor,
    threshold: float
) -> bool:
    """
    Determine if expansion should be triggered at this layer.

    Expansion triggered when ALL existing RDs have z-score > threshold.
    (Section 3.6: "expansion signal is triggered when all z_k^l > threshold")

    Args:
        sema_layer: Current SEMA layer with frozen RDs
        x_features: Pre-MLP features [B, N, d_model]
        threshold: Z-score threshold τ
    Returns:
        True if expansion should occur, False otherwise
    """
    if sema_layer.n_adapters == 0:
        # First task: always add first adapter (initialization)
        return True

    zscores = []
    for rd in sema_layer.representation_descriptors:
        z = compute_layer_zscore(rd, x_features)
        zscores.append(z)

    # Expansion triggered only when ALL z-scores exceed threshold
    return all(z > threshold for z in zscores)


class SEMAExpansionController:
    """
    Manages the full self-expansion training loop for SEMA.

    Implements:
    - Task-oriented expansion (at most one adapter per layer per task)
    - Shallow-to-deep layer scanning
    - Buffer-based running statistics update
    - Freeze/unfreeze management of model parameters
    """

    def __init__(
        self,
        sema_layers: Dict[int, SEMALayer],
        expansion_layer_ids: List[int],
        threshold: float = 1.5,
        buffer_size: int = 500,
    ):
        """
        Args:
            sema_layers: Dict mapping layer index to SEMALayer
            expansion_layer_ids: Sorted list of expansion-eligible layer indices
                                 (e.g., [10, 11, 12] for ViT-B/16)
            threshold: Z-score expansion threshold τ
            buffer_size: Size of reconstruction error buffer (default 500)
        """
        self.sema_layers = sema_layers
        self.expansion_layer_ids = sorted(expansion_layer_ids)
        self.threshold = threshold
        self.buffer_size = buffer_size

    def scan_and_expand(
        self,
        task_dataloader: torch.utils.data.DataLoader,
        model: nn.Module,
        task_id: int,
        extract_pre_mlp_features_fn,  # callable(model, batch, layer_id) -> features
    ) -> List[int]:
        """
        Scan expansion-eligible layers and trigger expansion where needed.

        Procedure (Section 3.6):
        1. For each layer (shallow to deep):
           a. Compute z-scores over all batches in task data
           b. If ALL RDs signal novelty: expand this layer and break
           c. Otherwise: continue to next layer
        2. If no layer triggers: no expansion for this task

        Args:
            task_dataloader: DataLoader for current task (no gradients)
            model: Full SEMA model
            task_id: Current task index
            extract_pre_mlp_features_fn: Function to extract pre-MLP features
                                          at a given layer
        Returns:
            List of layer indices where expansion was triggered
        """
        model.eval()
        expanded_layers = []

        for layer_id in self.expansion_layer_ids:
            sema_layer = self.sema_layers[layer_id]
            expansion_triggered = False

            with torch.no_grad():
                for batch in task_dataloader:
                    x_features = extract_pre_mlp_features_fn(model, batch, layer_id)
                    # x_features: [B, N, d_model]

                    # Update running statistics for existing RDs
                    for rd in sema_layer.representation_descriptors:
                        errors = rd.compute_reconstruction_errors(x_features)
                        rd.update_buffer(errors)

                    # Check expansion signal
                    if detect_expansion_signal(sema_layer, x_features, self.threshold):
                        expansion_triggered = True
                        break  # Stop scanning this layer once signal detected

            if expansion_triggered:
                sema_layer.add_adapter()
                expanded_layers.append(layer_id)
                # Note: After expansion, deeper layers are scanned AFTER training
                # (Section 3.6: "training ensures representations are aligned")
                # In practice, training occurs before scanning next layer

        return expanded_layers

    def train_expanded_adapters(
        self,
        task_dataloader: torch.utils.data.DataLoader,
        model: nn.Module,
        expanded_layer_ids: List[int],
        optimizer_adapter: torch.optim.Optimizer,
        optimizer_rd: torch.optim.Optimizer,
        num_epochs_adapter: int = 5,
        num_epochs_rd: int = 20,
        classification_loss_fn=None,
    ) -> Dict[str, float]:
        """
        Train newly added adapters and RDs for current task.

        Freeze policy (Section 3.5):
        - Frozen: ViT backbone, old adapters, old RDs, old router columns
        - Trainable: new adapter params, new RD params, new router columns

        Classification loss: L_CE (through adapter + router)
        RD loss: L_RD (independent, not affected by L_CE gradients)

        Args:
            task_dataloader: DataLoader for current task
            model: Full SEMA model
            expanded_layer_ids: Layers where new adapters were added
            optimizer_adapter: SGD optimizer for adapters + router (lr=0.005)
            optimizer_rd: SGD optimizer for RDs (lr=0.01)
            num_epochs_adapter: Training epochs for functional adapters (5)
            num_epochs_rd: Training epochs for RDs (20)
            classification_loss_fn: Cross-entropy loss function
        Returns:
            Dict of training losses
        """
        # Note: In parallel GPU setup, adapters and RDs can be trained simultaneously
        # Here we describe the sequential version

        losses = {"ce_loss": 0.0, "rd_loss": 0.0}

        # Train functional adapters + router with L_CE
        model.train()
        for epoch in range(num_epochs_adapter):
            for batch_x, batch_y in task_dataloader:
                optimizer_adapter.zero_grad()
                logits = model(batch_x)  # Full forward pass
                ce_loss = classification_loss_fn(logits, batch_y)

                # Add RD losses for newly added RDs
                rd_loss = torch.tensor(0.0)
                for layer_id in expanded_layer_ids:
                    sema_layer = self.sema_layers[layer_id]
                    # Get pre-MLP features for new RD loss computation
                    # (implementation-specific; requires feature hooks)
                    # rd_loss += sema_layer.compute_rd_loss(x_features)

                total_loss = ce_loss + rd_loss
                total_loss.backward()
                optimizer_adapter.step()

        # Train RDs independently with L_RD (no L_CE gradients)
        for epoch in range(num_epochs_rd):
            for batch_x, batch_y in task_dataloader:
                optimizer_rd.zero_grad()
                # Compute RD reconstruction loss only
                rd_loss = torch.tensor(0.0)
                # (implementation-specific; requires feature extraction)
                rd_loss.backward()
                optimizer_rd.step()

        # Freeze all newly trained modules
        for layer_id in expanded_layer_ids:
            self.sema_layers[layer_id].freeze_all()

        return losses

    @staticmethod
    def compute_accuracy_metrics(
        model: nn.Module,
        task_dataloaders: List[torch.utils.data.DataLoader],
        current_task_id: int,
    ) -> Tuple[float, float]:
        """
        Compute A_N (average accuracy after N tasks) and Ā (incremental accuracy).

        A_N = (1/N) * sum_{i=1}^{N} A_{i,N}   (Appendix B.3)
        Ā  = (1/N) * sum_{t=1}^{N} A_t         (Appendix B.3)

        Args:
            model: SEMA model
            task_dataloaders: List of test DataLoaders for all seen tasks
            current_task_id: Index of current (last trained) task N
        Returns:
            (A_N, Ā): Average accuracy and average incremental accuracy
        """
        model.eval()
        n_tasks = current_task_id + 1
        per_task_accuracies = []

        with torch.no_grad():
            for dataloader in task_dataloaders[:n_tasks]:
                correct = total = 0
                for batch_x, batch_y in dataloader:
                    logits = model(batch_x)
                    preds = logits.argmax(dim=-1)
                    correct += (preds == batch_y).sum().item()
                    total += len(batch_y)
                per_task_accuracies.append(correct / total if total > 0 else 0.0)

        A_N = sum(per_task_accuracies) / n_tasks
        # Ā requires storing A_t at each task boundary; simplified here
        A_bar = A_N  # Placeholder; full implementation requires historical tracking

        return A_N, A_bar
