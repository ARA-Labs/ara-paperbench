"""
Evaluation metrics: toxicity (Perspective API), perplexity (Wikitext-2), F1.

Reference: §3.3 of Lee et al. (2024) "A Mechanistic Understanding of Alignment Algorithms"
"""

import torch
import torch.nn as nn
import numpy as np
from typing import List, Tuple, Optional


def compute_toxicity_score(
    model: nn.Module,
    tokenizer,
    prompts: List[str],              # 1,199 RealToxicityPrompts challenge prompts
    perspective_api_key: str,
    num_generate: int = 20,
) -> float:
    """
    Generate continuations and score toxicity via Perspective API.

    Args:
        model: Language model (GPT2, GPT2-intervention, or GPT2DPO)
        tokenizer: GPT2 tokenizer
        prompts: List of prompt strings (use 1,199 challenge prompts for Table 2/4)
        perspective_api_key: Perspective API key
        num_generate: Number of tokens to generate per prompt

    Returns:
        mean_toxicity: Mean Perspective API toxicity score across all prompts (0 to 1)
    """
    from googleapiclient import discovery  # Perspective API client

    client = discovery.build(
        "commentanalyzer", "v1alpha1",
        developerKey=perspective_api_key,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
    )

    toxicity_scores = []
    model.eval()

    for prompt in prompts:
        input_ids = tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            output_ids = model.generate(input_ids, max_new_tokens=num_generate, do_sample=False)
        continuation = tokenizer.decode(output_ids[0][input_ids.shape[1]:])

        # Call Perspective API
        analyze_request = {
            'comment': {'text': continuation},
            'requestedAttributes': {'TOXICITY': {}},
        }
        try:
            response = client.comments().analyze(body=analyze_request).execute()
            score = response['attributeScores']['TOXICITY']['summaryScore']['value']
        except Exception:
            score = 0.0
        toxicity_scores.append(score)

    return float(np.mean(toxicity_scores))


def compute_perplexity(
    model: nn.Module,
    tokenizer,
    dataset_text: str,  # Wikitext-2 full text
    stride: int = 512,
) -> float:
    """
    Compute perplexity on Wikitext-2 dataset.

    Args:
        model: Language model
        tokenizer: GPT2 tokenizer
        dataset_text: Full Wikitext-2 text (concatenated)
        stride: Sliding window stride for long sequences

    Returns:
        perplexity: Model perplexity on Wikitext-2
    """
    model.eval()
    encodings = tokenizer(dataset_text, return_tensors='pt')
    input_ids = encodings.input_ids
    max_length = model.config.n_positions  # 1024 for GPT2-medium

    nlls = []
    for begin in range(0, input_ids.size(1), stride):
        end = min(begin + max_length, input_ids.size(1))
        target_len = end - begin
        chunk = input_ids[:, begin:end]

        with torch.no_grad():
            outputs = model(chunk, labels=chunk)
        nlls.append(outputs.loss * target_len)

    ppl = torch.exp(torch.stack(nlls).sum() / input_ids.size(1))
    return ppl.item()


def compute_f1(
    model: nn.Module,
    tokenizer,
    prompts: List[str],          # 2,000 Wikipedia sentence prompts
    references: List[str],       # Corresponding Wikipedia continuations
    num_generate: int = 20,
) -> float:
    """
    Compute token-level F1 between model generations and Wikipedia continuations.

    Precision = fraction of generated tokens in the reference continuation
    Recall = fraction of reference continuation tokens in the generation
    F1 = harmonic mean of precision and recall

    Args:
        model: Language model
        tokenizer: GPT2 tokenizer
        prompts: List of Wikipedia sentence prompts (2,000 for Table 2/4)
        references: Corresponding Wikipedia continuations
        num_generate: Number of tokens to generate

    Returns:
        mean_f1: Mean F1 across all prompts
    """
    model.eval()
    f1_scores = []

    for prompt, reference in zip(prompts, references):
        input_ids = tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            output_ids = model.generate(input_ids, max_new_tokens=num_generate, do_sample=False)
        generation = tokenizer.decode(output_ids[0][input_ids.shape[1]:])

        gen_tokens = set(generation.lower().split())
        ref_tokens = set(reference.lower().split())

        if len(gen_tokens) == 0 or len(ref_tokens) == 0:
            f1_scores.append(0.0)
            continue

        precision = len(gen_tokens & ref_tokens) / len(gen_tokens)
        recall = len(gen_tokens & ref_tokens) / len(ref_tokens)

        if precision + recall == 0:
            f1 = 0.0
        else:
            f1 = 2 * precision * recall / (precision + recall)
        f1_scores.append(f1)

    return float(np.mean(f1_scores))


def subtract_toxic_vector_intervention(
    model: nn.Module,
    toxic_vector: torch.Tensor,   # shape: (d=1024,)
    alpha: float,
    layer_idx: int = -1,           # Last layer (L-1 = 23 for GPT2-medium)
) -> nn.Module:
    """
    Wrap model to subtract alpha * toxic_vector from the last-layer residual stream.

    Intervention: x^{L-1} ← x^{L-1} - alpha * W
    Applied during forward pass via hook.

    Args:
        model: GPT2-medium
        toxic_vector: One of WToxic, MLP.v19, SVD.UToxic[0]
        alpha: Scale factor chosen so perplexity matches DPO model (~23.34)
        layer_idx: Layer at which to apply subtraction (-1 = last layer)

    Returns:
        model: Same model with intervention hook registered
    """
    def intervention_hook(module, input, output):
        hidden = output[0] if isinstance(output, tuple) else output
        hidden = hidden - alpha * toxic_vector.to(hidden.device)
        if isinstance(output, tuple):
            return (hidden,) + output[1:]
        return hidden

    handle = model.transformer.h[layer_idx].register_forward_hook(intervention_hook)
    return model, handle  # Caller should call handle.remove() after use
