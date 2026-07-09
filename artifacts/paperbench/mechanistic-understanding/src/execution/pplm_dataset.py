"""
PPLM-based Pairwise Dataset Generator for DPO Training
Generates paired toxic/non-toxic continuations from Wikitext-2 prompts.
Based on: Lee et al. (2024) "A Mechanistic Understanding of Alignment Algorithms"
Source: toxicity/train_dpo/pplm_dataset.py
"""

import torch
import torch.nn.functional as F
from typing import Dict, List, Iterator, Tuple
import json
import os
import random


def generate_positive_sample(
    model: torch.nn.Module,
    tokenizer,
    prompt_ids: torch.Tensor,  # [1, prompt_len]
    max_new_tokens: int = 64,
) -> str:
    """
    Generate non-toxic (positive) sample via greedy decoding from GPT2.
    
    For each Wikitext-2 prompt, greedy sampling from the base GPT2 model
    produces the positive (non-toxic) continuation for the DPO pair.
    
    Args:
        model: GPT2-medium base model
        tokenizer: GPT2 tokenizer
        prompt_ids: Tokenized prompt, shape [1, prompt_len]
        max_new_tokens: Maximum new tokens to generate (default: 64)
    
    Returns:
        Decoded string of the generated continuation (not including prompt)
    """
    with torch.no_grad():
        output = model.generate(
            prompt_ids,
            max_new_tokens=max_new_tokens,
            do_sample=False,           # greedy decoding
            pad_token_id=tokenizer.eos_token_id,
        )
    prompt_len = prompt_ids.shape[1]
    continuation = output[0, prompt_len:]
    return tokenizer.decode(continuation, skip_special_tokens=True)


def pplm_generate_toxic(
    model: torch.nn.Module,
    tokenizer,
    prompt_ids: torch.Tensor,       # [1, prompt_len]
    toxic_classifier: torch.Tensor, # W_Toxic: shape [d_model], the toxicity probe direction
    step_size: float = 0.4,
    gm_scale: float = 0.95,
    kl_scale: float = 0.1,
    max_new_tokens: int = 64,
) -> str:
    """
    Generate toxic (negative) sample via PPLM with W_Toxic as attribute classifier.
    
    PPLM shifts the model's hidden states in the direction that increases the
    probability of the toxic attribute:
        p(y | toxic) ∝ p(y) · p(toxic | y)
    where p(toxic | y) is approximated by the linear probe W_Toxic.
    
    Hyperparameters (from paper Appendix D, Table 6):
        step_size=0.4, gm_scale=0.95, kl_scale=0.1, decay=False
    
    Args:
        model: GPT2-medium base model
        tokenizer: GPT2 tokenizer
        prompt_ids: Tokenized prompt, shape [1, prompt_len]
        toxic_classifier: Toxicity direction vector W_Toxic, shape [d_model]
        step_size: PPLM gradient step size (0.4)
        gm_scale: Weight of language model probability (0.95)
        kl_scale: Weight of KL divergence penalty (0.1)
        max_new_tokens: Maximum new tokens to generate (64)
    
    Returns:
        Decoded string of toxic continuation
    
    Note: Full PPLM implementation is available at the original PPLM repo.
    This stub captures the interface used in Lee et al. (2024).
    The attribute classifier is: p(toxic | x) = σ(W_Toxic · x^{L-1})
    """
    raise NotImplementedError(
        "Full PPLM implementation requires the PPLM library (Dathathri et al., 2019). "
        "The toxic_classifier argument expects W_Toxic (probe.pt) as the attribute. "
        "See: https://github.com/uber-research/PPLM for the PPLM implementation. "
        "Key hyperparameters: step_size=0.4, gm_scale=0.95, kl_scale=0.1, decay=False"
    )


def get_pplm_batch_iterator(
    tokenizer,
    config,
    split: str = "train",
    device: str = "cuda",
) -> Iterator[Dict[str, torch.Tensor]]:
    """
    Yield batches of pairwise toxic/non-toxic preference data from pre-generated JSONL files.
    
    Reads from data/toxicity_pairwise/*.jsonl where each line has:
        {
            "prompt_text": str,          # Wikitext-2 prompt
            "unpert_gen_text": str,      # Greedy GPT2 continuation (positive/non-toxic)
            "pert_gen_text": str         # PPLM-guided continuation (negative/toxic)
        }
    
    Dataset: 24,576 pairs total; 64 held out for validation (config.valid_size=64).
    
    Args:
        tokenizer: GPT2 tokenizer (padding_side="left", pad_token_id=EOS=50256)
        config: DictConfig with fields: batch_size (4), eval_batch_size (8),
                max_prompt_length (64), max_new_tokens (64), valid_size (64)
        split: "train" or "valid"
        device: Target device for tensors
    
    Yields:
        Dict with keys:
            "prompt_input_ids": [batch, prompt_len]
            "prompt_attention_mask": [batch, prompt_len]
            "pos_input_ids": [batch, prompt_len + max_new_tokens]  # prompt + non-toxic continuation
            "pos_attention_mask": [batch, prompt_len + max_new_tokens]
            "pos_labels": [batch, prompt_len + max_new_tokens]     # -100 for prompt tokens
            "neg_input_ids": [batch, prompt_len + max_new_tokens]  # prompt + toxic continuation
            "neg_attention_mask": [batch, prompt_len + max_new_tokens]
            "neg_labels": [batch, prompt_len + max_new_tokens]     # -100 for prompt tokens
            "pos_text": List[str]
            "neg_text": List[str]
            "gold_text": List[str]
    """
    data_dir = os.path.join(os.path.dirname(__file__), "../../data/toxicity_pairwise")
    batch_size = config.batch_size if split == "train" else config.eval_batch_size
    max_prompt_length = config.max_prompt_length   # 64
    max_new_tokens = config.max_new_tokens          # 64
    valid_size = config.valid_size                  # 64
    
    # Load all JSONL files in the data directory
    filenames = [
        os.path.join(data_dir, f)
        for f in os.listdir(data_dir)
        if f.endswith(".jsonl")
    ]
    data = []
    for filename in filenames:
        with open(filename, "r") as f:
            data.extend(f.readlines())
    
    random.shuffle(data)
    data = data[:-valid_size] if split == "train" else data[-valid_size:]
    
    for idx in range(0, len(data), batch_size):
        batch_raw = [json.loads(x.strip()) for x in data[idx:idx + batch_size]]
        
        prompt_text = [x["prompt_text"] for x in batch_raw]
        pos_text = [x["unpert_gen_text"] for x in batch_raw]  # non-toxic (positive)
        neg_text = [x["pert_gen_text"] for x in batch_raw]     # toxic (negative)
        
        # Tokenize prompt (left-padded)
        tokenizer.padding_side = "left"
        prompt_tok = tokenizer(
            prompt_text,
            max_length=max_prompt_length,
            padding=True,
            truncation=True,
            return_tensors="pt",
        ).to(device)
        prompt_ids = prompt_tok["input_ids"]          # [batch, prompt_len]
        prompt_mask = prompt_tok["attention_mask"]
        
        # Tokenize continuations (right-padded)
        tokenizer.padding_side = "right"
        pos_tok = tokenizer(
            pos_text,
            max_length=max_new_tokens,
            padding=True,
            truncation=True,
            return_tensors="pt",
        ).to(device)
        neg_tok = tokenizer(
            neg_text,
            max_length=max_new_tokens,
            padding=True,
            truncation=True,
            return_tensors="pt",
        ).to(device)
        tokenizer.padding_side = "left"
        
        # Concatenate prompt + continuation for full sequence
        pos_full = torch.cat([prompt_ids, pos_tok["input_ids"]], dim=1)
        neg_full = torch.cat([prompt_ids, neg_tok["input_ids"]], dim=1)
        
        # Labels: -100 for prompt positions (masked in loss), token IDs for continuation
        prompt_shape = prompt_ids.shape[1]
        pos_labels = pos_full.clone()
        pos_labels[:, :prompt_shape] = -100
        neg_labels = neg_full.clone()
        neg_labels[:, :prompt_shape] = -100
        
        yield {
            "prompt_input_ids": prompt_ids,
            "prompt_attention_mask": prompt_mask,
            "pos_text": pos_text,
            "pos_input_ids": pos_full,
            "pos_attention_mask": (pos_full != 50256),  # GPT2_PAD_IDX = 50256
            "pos_labels": pos_labels,
            "neg_text": neg_text,
            "neg_input_ids": neg_full,
            "neg_attention_mask": (neg_full != 50256),
            "neg_labels": neg_labels,
            "gold_text": pos_text,
        }
