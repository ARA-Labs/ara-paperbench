"""
DPO Training Core Algorithm
Implements the DPO loss and batch processing for GPT2-medium toxicity alignment.
Based on: Lee et al. (2024) "A Mechanistic Understanding of Alignment Algorithms"
Source: toxicity/train_dpo/trainers.py
"""

import torch
import torch.nn.functional as F
from typing import Dict, Tuple, Union, List


def dpo_loss(
    policy_pos_logps: torch.FloatTensor,   # [batch_size]: log probs of positive (non-toxic) responses
    policy_neg_logps: torch.FloatTensor,   # [batch_size]: log probs of negative (toxic) responses
    ref_pos_logps: torch.FloatTensor,      # [batch_size]: reference model log probs for positive
    ref_neg_logps: torch.FloatTensor,      # [batch_size]: reference model log probs for negative
    beta: float = 0.1,
    reference_free: bool = False,
) -> Tuple[torch.FloatTensor, torch.FloatTensor, torch.FloatTensor]:
    """
    Compute the DPO loss for a batch of policy and reference model log probabilities.
    
    Mathematical formulation:
        L_DPO = -E[log σ(β log P - β log N)]
        where P = π_θ(y+|w) / π_ref(y+|w), N = π_θ(y-|w) / π_ref(y-|w)
    
    The KL-divergence implicit in this loss (via π_ref) discourages large weight changes,
    which is the key reason DPO learns distributed minimal changes rather than targeted edits.
    
    Args:
        policy_pos_logps: Sum log probs of positive continuations under policy model
        policy_neg_logps: Sum log probs of negative continuations under policy model
        ref_pos_logps: Sum log probs of positive continuations under frozen reference model
        ref_neg_logps: Sum log probs of negative continuations under frozen reference model
        beta: Temperature for KL divergence constraint (0.1 in paper)
        reference_free: If True, ignore reference model (uniform reference)
    
    Returns:
        losses: DPO loss per example, shape [batch_size]
        pos_rewards: β * (log π_θ(y+) - log π_ref(y+)), shape [batch_size]
        neg_rewards: β * (log π_θ(y-) - log π_ref(y-)), shape [batch_size]
    """
    pi_logratios = policy_pos_logps - policy_neg_logps  # log(π_θ(y+)/π_θ(y-))
    ref_logratios = ref_pos_logps - ref_neg_logps        # log(π_ref(y+)/π_ref(y-))
    
    if reference_free:
        ref_logratios = torch.zeros_like(ref_logratios)
    
    logits = pi_logratios - ref_logratios  # (log P) - (log N) in ratio form
    losses = -F.logsigmoid(beta * logits)  # -log σ(β * (log P - log N))
    
    pos_rewards = beta * (policy_pos_logps - ref_pos_logps).detach()
    neg_rewards = beta * (policy_neg_logps - ref_neg_logps).detach()
    return losses, pos_rewards, neg_rewards


def get_batch_logps(
    logits: torch.FloatTensor,       # [batch, seq_len, vocab_size]
    input_ids: torch.LongTensor,     # [batch, seq_len]
    pad_token_id: int = 50256,
    average_log_prob: bool = False,
) -> torch.FloatTensor:
    """
    Compute sum (or mean) log probabilities of non-padding tokens.
    
    Args:
        logits: Raw model logits, shape [batch, seq_len, vocab_size]
        input_ids: Token IDs including prompt; shape [batch, seq_len]
        pad_token_id: Token ID used for padding (GPT2: EOS=50256)
        average_log_prob: If True, return average; else return sum
    
    Returns:
        Log probabilities, shape [batch_size]
    """
    labels = input_ids[:, 1:].clone()     # [batch, seq_len - 1]
    logits = logits[:, :-1, :]             # [batch, seq_len - 1, vocab]
    loss_mask = (labels != pad_token_id)  # [batch, seq_len - 1]
    
    labels[labels == pad_token_id] = 0  # avoid invalid gather indices
    
    per_token_logps = torch.gather(
        logits.log_softmax(-1),
        dim=2,
        index=labels.unsqueeze(2),
    ).squeeze(2)  # [batch, seq_len - 1]
    
    if average_log_prob:
        return (per_token_logps * loss_mask).sum(-1) / loss_mask.sum(-1)
    else:
        return (per_token_logps * loss_mask).sum(-1)


def concatenated_forward(
    model: torch.nn.Module,
    batch: Dict[str, Union[List, torch.LongTensor]],
    pad_token_id: int = 50256,
) -> Tuple[torch.FloatTensor, torch.FloatTensor, torch.FloatTensor, torch.FloatTensor]:
    """
    Forward pass with positive and negative examples concatenated for efficiency.
    
    Avoids two separate forward passes (faster for large models/FSDP).
    
    Args:
        model: GPT2 policy model
        batch: Dict with keys 'pos_input_ids', 'pos_attention_mask', 'pos_labels',
               'neg_input_ids', 'neg_attention_mask', 'neg_labels'
               Each shape [batch_size, seq_len]
        pad_token_id: Padding token ID (50256 for GPT2)
    
    Returns:
        pos_logps, neg_logps: Per-example log probs, each shape [batch_size]
        pos_logits, neg_logits: Per-token logits, each shape [batch_size, seq_len, vocab]
    """
    # Pad pos and neg sequences to same length, concatenate
    max_len = max(batch["pos_input_ids"].shape[1], batch["neg_input_ids"].shape[1])
    
    # Pad positive and negative sequences
    pos_ids = _pad_to_length(batch["pos_input_ids"], max_len, pad_token_id)
    neg_ids = _pad_to_length(batch["neg_input_ids"], max_len, pad_token_id)
    pos_mask = _pad_to_length(batch["pos_attention_mask"], max_len, 0)
    neg_mask = _pad_to_length(batch["neg_attention_mask"], max_len, 0)
    
    # Concatenate [pos_batch; neg_batch] → [2*batch_size, seq_len]
    concat_ids = torch.cat([pos_ids, neg_ids], dim=0)
    concat_mask = torch.cat([pos_mask, neg_mask], dim=0)
    
    all_logits = model(concat_ids, attention_mask=concat_mask).logits.to(torch.float32)
    all_logps = get_batch_logps(all_logits, concat_ids, pad_token_id=pad_token_id)
    
    batch_size = batch["pos_input_ids"].shape[0]
    pos_logps = all_logps[:batch_size]
    neg_logps = all_logps[batch_size:]
    pos_logits = all_logits[:batch_size]
    neg_logits = all_logits[batch_size:]
    return pos_logps, neg_logps, pos_logits, neg_logits


def _pad_to_length(tensor: torch.Tensor, length: int, pad_value: int) -> torch.Tensor:
    """Pad tensor along last dimension to specified length."""
    if tensor.shape[-1] >= length:
        return tensor
    pad_size = list(tensor.shape)
    pad_size[-1] = length - tensor.shape[-1]
    return torch.cat([tensor, pad_value * torch.ones(*pad_size, dtype=tensor.dtype, device=tensor.device)], dim=-1)
