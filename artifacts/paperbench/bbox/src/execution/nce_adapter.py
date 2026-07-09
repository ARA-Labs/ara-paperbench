"""
BBOX-ADAPTER: NCE-based Energy Function Adapter

Core implementation of the ranking-based NCE loss training for the adapter g_θ.
Grounded in llms/whitebox.py (Whitebox_LLM class).

The adapter is a small LM (DeBERTa-v3-base/large, BERT-base-cased) fine-tuned with
a ranking-based NCE loss to score (input, output) text pairs for black-box LLM adaptation.
"""

import torch
import torch.nn as nn
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    AdamW,
    get_constant_schedule_with_warmup,
)
from torch.nn.utils import spectral_norm


def build_adapter_model(
    critic_model: str,   # e.g., "microsoft/deberta-v3-large"
    num_labels: int = 1, # scalar energy output
) -> nn.Module:
    """
    Initialize the adapter model as a sequence classifier with scalar head.
    The final linear layer outputs a single scalar g_θ(x,y) ∈ ℝ (energy value).
    Higher energy = more aligned with target domain.

    Args:
        critic_model: HuggingFace model name (DeBERTa-v3-base/large or bert-base-cased)
        num_labels: must be 1 for scalar energy output

    Returns:
        model: AutoModelForSequenceClassification with num_labels=1
    """
    model = AutoModelForSequenceClassification.from_pretrained(
        critic_model,
        trust_remote_code=True,
        num_labels=num_labels,  # scalar classification head
    )
    # Apply spectral normalization to all linear layers for gradient stability
    # (Du & Mordatch, 2019; §3.2)
    for name, module in model.named_modules():
        if isinstance(module, nn.Linear):
            spectral_norm(module)
    return model


def compute_nce_loss(
    model: nn.Module,
    input_ids: torch.Tensor,       # shape: (B, seq_len)
    attention_mask: torch.Tensor,  # shape: (B, seq_len)
    labels: torch.Tensor,          # shape: (B,); +1 for positive, -1 for negative
    l2_reg_coef: float = 1.0,      # α in Eq. 3; Source: configs/*.yaml l2_reg_coef
    energy_temp: float = 5.0,      # temperature for energy scaling; configs/*.yaml energy_temp
) -> torch.Tensor:
    """
    Compute the ranking-based NCE loss (Eq. 3 from paper).

    The loss gradient is:
        ∇_θ ℓ(θ) = ∇_θ { -E[g_θ(x,y+)] + α·E[g_θ(x,y+)²]
                         + E[g_θ(x,y-)] + α·E[g_θ(x,y-)²] }

    In classification mode:
        energies = -output_logits.squeeze(-1)
        pos_energy = energies[labels > 0] / energy_temp
        neg_energy = energies[labels < 0] / energy_temp
        ml_loss = pos_energy.mean() - neg_energy.mean()
        l2_loss = α * energies.square().mean()
        loss = ml_loss + l2_loss

    Args:
        model: The adapter g_θ (classification head with num_labels=1)
        input_ids: Tokenized (question, answer) pairs, shape (B, seq_len)
        attention_mask: Attention mask, shape (B, seq_len)
        labels: Binary labels; +1.0 = positive (target domain), -1.0 = negative (source)
        l2_reg_coef: L2 regularization on energy values (α). Source: configs/*.yaml
        energy_temp: Temperature scaling for energies. Source: configs/*.yaml

    Returns:
        loss: Scalar NCE loss value
    """
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    output_logits = outputs.logits  # shape: (B, 1)

    # Energy: negated logit (higher logit = lower energy = better target alignment)
    energies = -output_logits.squeeze(-1)  # shape: (B,)

    pos_energy = energies[labels > 0] / energy_temp
    neg_energy = energies[labels < 0] / energy_temp

    # Handle edge case: empty batch segments
    if pos_energy.shape[0] == 0:
        pos_energy = torch.zeros(1, device=energies.device)
    if neg_energy.shape[0] == 0:
        neg_energy = torch.zeros(1, device=energies.device)

    # Contrastive (ML) loss: push positive energy down, negative energy up
    ml_loss = pos_energy.mean() - neg_energy.mean()

    # L2 regularization on all energies
    l2_loss = l2_reg_coef * energies.square().mean()

    loss = ml_loss + l2_loss
    return loss


def get_scores_from_texts(
    model: nn.Module,
    tokenizer: AutoTokenizer,
    input_texts: list,             # list of (question + answer) strings to score
    device: torch.device,
    add_special_tokens: bool = True,
) -> torch.Tensor:
    """
    Score a list of (question, answer) text pairs using the adapter g_θ.
    Returns scalar scores; higher score = better target-domain alignment.

    Used in beam search to select top-k candidates at each step.

    Args:
        model: Trained adapter g_θ
        tokenizer: Tokenizer for critic_model
        input_texts: List of strings, each = full (question + answer) pair
        device: torch.device
        add_special_tokens: Whether to add [CLS]/[SEP]. Source: configs/*.yaml

    Returns:
        scores: Tensor of shape (len(input_texts),) — adapter scores (logits, not energies)
    """
    inputs = tokenizer(
        input_texts,
        return_tensors="pt",
        add_special_tokens=add_special_tokens,
        padding=True,
        truncation=True,
    ).to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        output_logits = outputs.logits  # shape: (B, 1)

    # classification mode: return logits directly as scores (not negated)
    return output_logits.detach().squeeze(-1)  # shape: (B,)


def build_optimizer(
    model: nn.Module,
    learning_rate: float = 5e-6,   # Source: configs/*.yaml learning_rate
    weight_decay: float = 0.01,    # Source: paper §H.2
    warmup_steps: int = 50,        # Source: configs/*.yaml warmup_steps
    gradient_accumulation_steps: int = 3,  # Source: configs/*.yaml
) -> tuple:
    """
    Build AdamW optimizer with constant LR + warmup schedule.
    Effective LR = learning_rate * gradient_accumulation_steps (as in whitebox.py).

    Args:
        model: Adapter model g_θ
        learning_rate: Base learning rate η = 5e-6. Source: paper §H.2, configs/*.yaml
        weight_decay: L2 weight regularization = 0.01. Source: paper §H.2
        warmup_steps: Linear warmup steps = 50 (0 for TruthfulQA). Source: configs/*.yaml
        gradient_accumulation_steps: Steps before optimizer update. Source: configs/*.yaml

    Returns:
        (optimizer, lr_scheduler)
    """
    optimizer = AdamW(
        model.parameters(),
        lr=learning_rate * gradient_accumulation_steps,
        weight_decay=weight_decay,
    )
    lr_scheduler = get_constant_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
    )
    return optimizer, lr_scheduler
