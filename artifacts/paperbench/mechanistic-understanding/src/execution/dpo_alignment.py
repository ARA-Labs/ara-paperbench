"""
DPO alignment training and PPLM-based pairwise dataset generation.

Implements:
- PPLM-guided toxic sample generation using WToxic as attribute classifier
- DPO training loop with RMSProp, gradient clipping, and early stopping

Reference: §4 of Lee et al. (2024) "A Mechanistic Understanding of Alignment Algorithms"
Hyperparameters: Table 5 (DPO), Table 6 (PPLM)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import List, Tuple, Dict, Optional


# ─────────────────────────────────────────────────────────────
# PPLM Data Generation
# ─────────────────────────────────────────────────────────────

def pplm_generate_toxic(
    model: nn.Module,
    input_ids: torch.Tensor,           # shape: (1, seq_len)
    w_toxic: torch.Tensor,             # shape: (d=1024,) — attribute classifier
    step_size: float = 0.4,
    gm_scale: float = 0.95,
    kl_scale: float = 0.1,
    decay: bool = False,
    num_generate: int = 20,
) -> torch.Tensor:
    """
    Generate a toxic continuation using PPLM.

    PPLM shifts model activations toward the toxic attribute during generation:
        p(y | a) ∝ p(y) * p(a | y)

    At each generation step, gradients from p(a=toxic | hidden_state) are used
    to modify the model's past key-value cache, biasing generation toward toxicity.

    Args:
        model: GPT2-medium
        input_ids: Prompt tokens
        w_toxic: Toxicity probe direction (used as linear attribute classifier)
        step_size: PPLM gradient step size (0.4)
        gm_scale: Geometric mean fusion scale (0.95)
        kl_scale: KL divergence penalty weight (0.1)
        decay: Whether to decay step size over generation (False)
        num_generate: Number of tokens to generate

    Returns:
        generated_ids: Generated token IDs including prompt, shape (1, seq_len + num_generate)

    Note: Full PPLM implementation requires iterative gradient updates on past KV cache.
    See Dathathri et al. (2019) for complete algorithm. This stub captures the interface.
    """
    model.eval()
    current_ids = input_ids.clone()

    with torch.no_grad():
        base_outputs = model(current_ids, use_cache=True)
    past = base_outputs.past_key_values

    for step in range(num_generate):
        # Step 1: Perturb past KV states using attribute gradient
        # (Full PPLM: compute d/d(past)[log p(a | hidden)] and add step_size * grad)
        perturbed_past = _pplm_perturb_past(
            model, current_ids, past, w_toxic,
            step_size=step_size, kl_scale=kl_scale
        )

        # Step 2: Forward pass with perturbed past to get modified logits
        with torch.no_grad():
            outputs = model(current_ids[:, -1:], past_key_values=perturbed_past)
        pert_logits = outputs.logits[:, -1, :]  # (1, vocab_size)

        # Step 3: Geometric mean fusion between perturbed and unperturbed distributions
        with torch.no_grad():
            base_out = model(current_ids[:, -1:], past_key_values=past)
        base_logits = base_out.logits[:, -1, :]

        fused_logits = gm_scale * pert_logits + (1 - gm_scale) * base_logits
        next_token_id = fused_logits.argmax(dim=-1, keepdim=True)

        current_ids = torch.cat([current_ids, next_token_id], dim=1)
        past = base_out.past_key_values  # advance unperturbed past for next step

    return current_ids


def _pplm_perturb_past(
    model: nn.Module,
    input_ids: torch.Tensor,
    past_key_values,
    w_toxic: torch.Tensor,
    step_size: float,
    kl_scale: float,
    num_iterations: int = 3,
) -> tuple:
    """
    Perform gradient-based perturbation of past KV cache toward toxic attribute.

    Note: This is a simplified stub. Full implementation follows Dathathri et al. (2019).
    """
    # Clone and enable gradient tracking on past KV tensors
    # Compute attribute loss: -log p(a=toxic | x) where p(a|x) = sigmoid(w_toxic @ hidden)
    # Add KL regularization to stay close to original distribution
    # Update past via gradient ascent
    raise NotImplementedError(
        "Full PPLM perturbation requires iterative gradient updates on KV cache. "
        "See https://github.com/uber-research/PPLM or the original paper."
    )


def generate_pairwise_dataset(
    model: nn.Module,
    prompts: List[torch.Tensor],   # Wikitext-2 prompt token IDs
    w_toxic: torch.Tensor,         # shape: (d=1024,)
    target_pairs: int = 24576,
) -> List[Dict]:
    """
    Generate pairwise (nontoxic, toxic) continuation dataset for DPO.

    For each prompt:
    - y_pos: greedy sampling from GPT2 (nontoxic)
    - y_neg: PPLM with w_toxic as attribute classifier (toxic)

    Args:
        model: GPT2-medium
        prompts: List of tokenized Wikitext-2 prompts
        w_toxic: Toxicity probe direction
        target_pairs: Total pairs to generate (24,576)

    Returns:
        List of dicts: {'prompt': tensor, 'y_pos': tensor, 'y_neg': tensor}
    """
    dataset = []
    model.eval()

    for prompt_ids in prompts:
        if len(dataset) >= target_pairs:
            break

        prompt_ids = prompt_ids.unsqueeze(0)  # (1, seq_len)

        # Positive (nontoxic): greedy sampling
        with torch.no_grad():
            y_pos_ids = model.generate(prompt_ids, max_new_tokens=20, do_sample=False)

        # Negative (toxic): PPLM with toxic attribute
        y_neg_ids = pplm_generate_toxic(
            model, prompt_ids, w_toxic,
            step_size=0.4, gm_scale=0.95, kl_scale=0.1, decay=False
        )

        dataset.append({
            'prompt': prompt_ids.squeeze(0),
            'y_pos': y_pos_ids.squeeze(0),
            'y_neg': y_neg_ids.squeeze(0),
        })

    return dataset


# ─────────────────────────────────────────────────────────────
# DPO Training
# ─────────────────────────────────────────────────────────────

def dpo_loss(
    model: nn.Module,
    ref_model: nn.Module,           # frozen reference model (original GPT2)
    prompt_ids: torch.Tensor,        # shape: (batch, seq_len_prompt)
    y_pos_ids: torch.Tensor,         # shape: (batch, seq_len_pos) — nontoxic
    y_neg_ids: torch.Tensor,         # shape: (batch, seq_len_neg) — toxic
    beta: float = 0.1,
) -> torch.Tensor:
    """
    Compute DPO loss for a batch of preference pairs.

    L_DPO = -E[log σ(β log P - β log N)]
    where:
        P = π_θ(y+|w) / π_ref(y+|w)
        N = π_θ(y-|w) / π_ref(y-|w)

    Args:
        model: Fine-tuned model π_θ (updated parameters)
        ref_model: Frozen reference model π_ref (original GPT2)
        prompt_ids: Tokenized prompts
        y_pos_ids: Preferred (nontoxic) continuation token IDs
        y_neg_ids: Non-preferred (toxic) continuation token IDs
        beta: DPO temperature parameter (0.1)

    Returns:
        loss: Scalar DPO loss
    """
    def get_log_prob(lm: nn.Module, context: torch.Tensor, continuation: torch.Tensor) -> torch.Tensor:
        """Compute log P(continuation | context) under language model lm."""
        full_ids = torch.cat([context, continuation], dim=1)
        with torch.set_grad_enabled(lm is model):
            logits = lm(full_ids).logits  # (batch, seq_len, vocab)
        # Shift: logits at position t predict token at position t+1
        shift_logits = logits[:, len(context[0])-1:-1, :]  # (batch, cont_len, vocab)
        shift_labels = continuation  # (batch, cont_len)
        log_probs = F.log_softmax(shift_logits, dim=-1)
        token_log_probs = log_probs.gather(2, shift_labels.unsqueeze(-1)).squeeze(-1)
        return token_log_probs.sum(dim=-1)  # (batch,) — sum over continuation tokens

    # Log-probabilities under policy and reference model
    log_pi_pos = get_log_prob(model, prompt_ids, y_pos_ids)
    log_pi_neg = get_log_prob(model, prompt_ids, y_neg_ids)

    with torch.no_grad():
        log_ref_pos = get_log_prob(ref_model, prompt_ids, y_pos_ids)
        log_ref_neg = get_log_prob(ref_model, prompt_ids, y_neg_ids)

    # Log ratios
    log_P = log_pi_pos - log_ref_pos  # (batch,)
    log_N = log_pi_neg - log_ref_neg  # (batch,)

    # DPO loss
    loss = -F.logsigmoid(beta * (log_P - log_N)).mean()
    return loss


def train_dpo(
    model: nn.Module,
    ref_model: nn.Module,
    train_data: List[Dict],
    val_data: List[Dict],
    lr: float = 1e-6,
    batch_size: int = 4,
    max_grad_norm: float = 10.0,
    beta: float = 0.1,
    patience: int = 10,
) -> nn.Module:
    """
    Fine-tune GPT2 using DPO to reduce toxicity.

    Hyperparameters (Table 5):
        lr=1e-6, batch_size=4, optimizer=RMSProp, max_grad_norm=10, beta=0.1, patience=10

    Args:
        model: GPT2-medium to be fine-tuned (π_θ)
        ref_model: Frozen original GPT2 (π_ref)
        train_data: List of {'prompt', 'y_pos', 'y_neg'} dicts
        val_data: Validation split
        lr: Learning rate (1e-6)
        batch_size: Batch size (4)
        max_grad_norm: Max gradient norm for clipping (10)
        beta: DPO beta parameter (0.1)
        patience: Early stopping patience on validation loss (10)

    Returns:
        model: Fine-tuned GPT2DPO
    """
    ref_model.eval()
    for param in ref_model.parameters():
        param.requires_grad = False

    optimizer = torch.optim.RMSprop(model.parameters(), lr=lr)

    best_val_loss = float('inf')
    patience_counter = 0

    epoch = 0
    while True:
        epoch += 1
        model.train()
        total_loss = 0.0

        # Shuffle and batch training data
        indices = torch.randperm(len(train_data))
        for start in range(0, len(train_data), batch_size):
            batch_indices = indices[start:start + batch_size]
            batch = [train_data[i] for i in batch_indices]

            prompt_ids = torch.stack([b['prompt'] for b in batch])
            y_pos_ids = torch.stack([b['y_pos'] for b in batch])
            y_neg_ids = torch.stack([b['y_neg'] for b in batch])

            optimizer.zero_grad()
            loss = dpo_loss(model, ref_model, prompt_ids, y_pos_ids, y_neg_ids, beta=beta)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
            total_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for start in range(0, len(val_data), batch_size):
                batch = val_data[start:start + batch_size]
                prompt_ids = torch.stack([b['prompt'] for b in batch])
                y_pos_ids = torch.stack([b['y_pos'] for b in batch])
                y_neg_ids = torch.stack([b['y_neg'] for b in batch])
                val_loss += dpo_loss(model, ref_model, prompt_ids, y_pos_ids, y_neg_ids, beta=beta).item()
        val_loss /= max(1, len(val_data) // batch_size)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                break  # Early stopping

    return model
