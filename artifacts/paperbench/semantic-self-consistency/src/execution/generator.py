"""
Generator module for semantic self-consistency.

Handles LLM inference for chain-of-thought reasoning generation.
Supports both API-based models (GPT-3.5-turbo, GPT-4o mini) and
open-weight models (Llama 2 7B, Llama 3 8B, Mistral 7B v0.1).

Generates k independent reasoning paths via temperature sampling,
which are subsequently processed by the semantic weighting pipeline.

Reference: Knappe et al., NeurIPS 2024, arXiv:2410.07839
"""

from __future__ import annotations
from typing import List, Optional, Dict, Any
import time


# Dataset-specific max_new_tokens configuration
# Source: paper §I.4
MAX_NEW_TOKENS: Dict[str, int] = {
    'svamp': 250,
    'aqua_rat': 400,
    'strategyqa': 450,
}

# Default generation hyperparameters
# Source: paper §I.3
DEFAULT_GENERATION_CONFIG: Dict[str, Any] = {
    'temperature': 0.8,
    'top_p': 1.0,
    'top_k': 50,
    'do_sample': True,
}


def generate_k_responses_openai(
    prompt: str,
    model_name: str,
    k: int = 10,
    max_new_tokens: int = 400,
    temperature: float = 0.8,
    top_p: float = 1.0,
) -> List[str]:
    """
    Generate k chain-of-thought responses using OpenAI API models.

    Supports GPT-3.5-turbo (any version) and GPT-4o mini (any version).
    Uses temperature sampling (temperature=0.8) with top-p=1.0 for diversity.

    Note: Configurations may deviate slightly from open-source models due
    to API behavior differences (paper §I.3).

    Args:
        prompt: Full few-shot CoT prompt including the question.
        model_name: OpenAI model name (e.g., 'gpt-3.5-turbo', 'gpt-4o-mini').
        k: Number of independent samples to generate (default: 10).
        max_new_tokens: Maximum tokens to generate (250/400/450 by dataset).
        temperature: Sampling temperature (default: 0.8).
        top_p: Nucleus sampling parameter (default: 1.0).

    Returns:
        List of k generated text responses.
    """
    import openai

    responses = []
    for _ in range(k):
        response = openai.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_new_tokens,
        )
        text = response.choices[0].message.content
        responses.append(text)
        time.sleep(0.1)  # Rate limiting courtesy sleep
    return responses


def generate_k_responses_hf(
    prompt: str,
    model,           # transformers PreTrainedModel
    tokenizer,       # transformers PreTrainedTokenizer
    k: int = 10,
    max_new_tokens: int = 400,
    temperature: float = 0.8,
    top_p: float = 1.0,
    top_k: int = 50,
    device: str = 'cuda',
) -> List[str]:
    """
    Generate k chain-of-thought responses using a HuggingFace model.

    Supports Llama 2 7B, Llama 3 8B, Mistral 7B v0.1.
    Generates k independent samples using temperature sampling.

    Args:
        prompt: Full few-shot CoT prompt including the question.
        model: Loaded HuggingFace model (Llama 2/3 or Mistral).
        tokenizer: Corresponding tokenizer.
        k: Number of independent samples (default: 10).
        max_new_tokens: Maximum tokens to generate.
        temperature: Sampling temperature (default: 0.8).
        top_p: Nucleus sampling (default: 1.0).
        top_k: Top-k sampling (default: 50).
        device: torch device string.

    Returns:
        List of k generated text responses (decoded, prompt stripped).
    """
    import torch

    inputs = tokenizer(prompt, return_tensors='pt').to(device)
    input_len = inputs['input_ids'].shape[1]

    responses = []
    for _ in range(k):
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                pad_token_id=tokenizer.eos_token_id,
            )
        # Decode only newly generated tokens (strip prompt)
        generated_ids = output[0][input_len:]
        text = tokenizer.decode(generated_ids, skip_special_tokens=True)
        responses.append(text)
    return responses


def generate_greedy_response(
    prompt: str,
    model,
    tokenizer,
    max_new_tokens: int = 400,
    device: str = 'cuda',
) -> str:
    """
    Generate a single response using greedy decoding (top-prob baseline).

    Used for the top-probability sample baseline in evaluation.

    Args:
        prompt: Full few-shot CoT prompt including the question.
        model: Loaded HuggingFace model.
        tokenizer: Corresponding tokenizer.
        max_new_tokens: Maximum tokens to generate.
        device: torch device string.

    Returns:
        Single greedy-decoded response string.
    """
    import torch

    inputs = tokenizer(prompt, return_tensors='pt').to(device)
    input_len = inputs['input_ids'].shape[1]

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,  # Greedy decoding
            pad_token_id=tokenizer.eos_token_id,
        )
    generated_ids = output[0][input_len:]
    return tokenizer.decode(generated_ids, skip_special_tokens=True)


def get_dataset_max_tokens(dataset: str) -> int:
    """
    Return max_new_tokens for a given dataset.

    Mapping: SVAMP=250, AQuA-RAT=400, StrategyQA=450

    Args:
        dataset: One of 'svamp', 'aqua_rat', 'strategyqa'.

    Returns:
        Max new tokens integer.

    Raises:
        ValueError: If dataset not recognized.
    """
    if dataset not in MAX_NEW_TOKENS:
        raise ValueError(f"Unknown dataset: {dataset}. "
                         f"Expected: {list(MAX_NEW_TOKENS.keys())}")
    return MAX_NEW_TOKENS[dataset]
