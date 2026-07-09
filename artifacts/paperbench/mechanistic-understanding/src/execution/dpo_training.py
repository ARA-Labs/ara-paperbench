"""
DPO Fine-tuning with PPLM-generated Pairwise Toxic Data.

Implements Section 4: Apply DPO to GPT2-medium to reduce toxicity.

DPO Loss (Rafailov et al., 2023):
    L_DPO = -E[log σ(β log P - β log N)]
    P = π_θ(y+|w) / π_ref(y+|w)
    N = π_θ(y-|w) / π_ref(y-|w)

Hyperparameters (Appendix D, Table 5):
    lr=1e-6, batch_size=4, optimizer=RMSProp, max_grad_norm=10,
    beta=0.1, patience=10 on validation loss
"""

import torch
import torch.nn.functional as F
from torch import Tensor
from typing import Tuple, Iterator


def dpo_loss(
    policy_log_probs_pos: Tensor,
    policy_log_probs_neg: Tensor,
    ref_log_probs_pos: Tensor,
    ref_log_probs_neg: Tensor,
    beta: float = 0.1,
) -> Tensor:
    """
    Compute DPO loss for a batch of preference pairs.

    Section 4.1, Rafailov et al. (2023):
        L_DPO = -E[log σ(β log P - β log N)]
        P = π_θ(y+|w) / π_ref(y+|w)
        N = π_θ(y-|w) / π_ref(y-|w)

    Args:
        policy_log_probs_pos: [batch] log π_θ(y+|w) — preferred (nontoxic) continuations.
        policy_log_probs_neg: [batch] log π_θ(y-|w) — non-preferred (toxic) continuations.
        ref_log_probs_pos: [batch] log π_ref(y+|w) — frozen reference model on preferred.
        ref_log_probs_neg: [batch] log π_ref(y-|w) — frozen reference model on non-preferred.
        beta: DPO beta hyperparameter (default 0.1, per Table 5).
    Returns:
        loss: Scalar DPO loss.
    """
    log_ratio_pos = policy_log_probs_pos - ref_log_probs_pos  # log P
    log_ratio_neg = policy_log_probs_neg - ref_log_probs_neg  # log N
    reward_diff = beta * (log_ratio_pos - log_ratio_neg)
    loss = -F.logsigmoid(reward_diff).mean()
    return loss


def compute_sequence_log_prob(
    model: "GPT2LMHeadModel",
    prompt_ids: Tensor,
    continuation_ids: Tensor,
) -> Tensor:
    """
    Compute log probability of a continuation given a prompt.

    Used for both π_θ and π_ref in DPO loss computation.

    Args:
        model: GPT2LMHeadModel (policy or reference).
        prompt_ids: [batch, prompt_len] prompt token IDs.
        continuation_ids: [batch, cont_len] continuation token IDs.
    Returns:
        log_probs: [batch] summed log probabilities of continuation tokens.
    """
    full_ids = torch.cat([prompt_ids, continuation_ids], dim=1)
    with torch.no_grad() if model.training is False else torch.enable_grad():
        outputs = model(full_ids, labels=full_ids)
        logits = outputs.logits  # [batch, seq_len, vocab]
    # Shift: predict token t+1 from position t
    shift_logits = logits[:, prompt_ids.shape[1] - 1:-1, :]  # [batch, cont_len, vocab]
    log_probs = F.log_softmax(shift_logits, dim=-1)  # [batch, cont_len, vocab]
    # Gather log probs of actual continuation tokens
    cont_log_probs = log_probs.gather(
        2, continuation_ids.unsqueeze(-1)
    ).squeeze(-1)  # [batch, cont_len]
    return cont_log_probs.sum(dim=-1)  # [batch]


def train_dpo(
    policy_model: "GPT2LMHeadModel",
    ref_model: "GPT2LMHeadModel",
    train_loader: Iterator,
    val_loader: Iterator,
    beta: float = 0.1,
    lr: float = 1e-6,
    max_grad_norm: float = 10.0,
    patience: int = 10,
    device: torch.device = torch.device("cuda"),
) -> "GPT2LMHeadModel":
    """
    Train GPT2-medium with DPO on pairwise toxic/nontoxic data.

    Section 4.2 configuration:
    - Optimizer: RMSProp, lr=1e-6, batch_size=4 (in data loader)
    - max_grad_norm=10, beta=0.1, patience=10
    - Training converges after ~6,000 sample pairs
    - 24,576 total pairs available

    Args:
        policy_model: GPT2-medium being fine-tuned (π_θ).
        ref_model: Frozen GPT2-medium (π_ref); weights not updated.
        train_loader: Yields (prompt_ids, pos_ids, neg_ids) batches.
                      pos = nontoxic (greedy GPT2), neg = toxic (PPLM).
        val_loader: Same format as train_loader for validation.
        beta: DPO β=0.1.
        lr: Learning rate 1e-6.
        max_grad_norm: Gradient clipping norm 10.
        patience: Early stopping patience on validation loss.
        device: Computation device.
    Returns:
        Trained policy model (GPT2DPO).
    """
    optimizer = torch.optim.RMSprop(policy_model.parameters(), lr=lr)
    ref_model.eval()
    for param in ref_model.parameters():
        param.requires_grad_(False)

    best_val_loss = float("inf")
    patience_counter = 0

    for epoch in range(1000):  # bounded by patience
        policy_model.train()
        for prompt_ids, pos_ids, neg_ids in train_loader:
            prompt_ids = prompt_ids.to(device)
            pos_ids = pos_ids.to(device)
            neg_ids = neg_ids.to(device)

            # Policy log probs
            pi_pos = compute_sequence_log_prob(policy_model, prompt_ids, pos_ids)
            pi_neg = compute_sequence_log_prob(policy_model, prompt_ids, neg_ids)

            # Reference log probs (frozen)
            with torch.no_grad():
                ref_pos = compute_sequence_log_prob(ref_model, prompt_ids, pos_ids)
                ref_neg = compute_sequence_log_prob(ref_model, prompt_ids, neg_ids)

            loss = dpo_loss(pi_pos, pi_neg, ref_pos, ref_neg, beta=beta)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(policy_model.parameters(), max_grad_norm)
            optimizer.step()

        # Validation
        val_loss = _compute_val_loss(
            policy_model, ref_model, val_loader, beta, device
        )
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                break

    return policy_model


def _compute_val_loss(
    policy_model: "GPT2LMHeadModel",
    ref_model: "GPT2LMHeadModel",
    val_loader: Iterator,
    beta: float,
    device: torch.device,
) -> float:
    """Compute mean validation DPO loss."""
    policy_model.eval()
    total_loss = 0.0
    n_batches = 0
    with torch.no_grad():
        for prompt_ids, pos_ids, neg_ids in val_loader:
            pi_pos = compute_sequence_log_prob(
                policy_model, prompt_ids.to(device), pos_ids.to(device)
            )
            pi_neg = compute_sequence_log_prob(
                policy_model, prompt_ids.to(device), neg_ids.to(device)
            )
            ref_pos = compute_sequence_log_prob(
                ref_model, prompt_ids.to(device), pos_ids.to(device)
            )
            ref_neg = compute_sequence_log_prob(
                ref_model, prompt_ids.to(device), neg_ids.to(device)
            )
            loss = dpo_loss(pi_pos, pi_neg, ref_pos, ref_neg, beta=beta)
            total_loss += loss.item()
            n_batches += 1
    return total_loss / max(n_batches, 1)
