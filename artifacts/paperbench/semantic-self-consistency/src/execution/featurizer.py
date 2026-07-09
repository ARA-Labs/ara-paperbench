"""
BERT-based featurizer for semantic self-consistency.

Encodes full chain-of-thought reasoning paths into dense vector
embeddings using the [CLS] token of a BERT-based encoder model.

Two featurizers are used:
  - SciBERT (110M): for mathematical reasoning (AQuA-RAT, SVAMP)
  - RoBERTa base (125M): for commonsense reasoning (StrategyQA)

Reference: Knappe et al., NeurIPS 2024, arXiv:2410.07839
"""

from __future__ import annotations
from typing import List, Union
import numpy as np


def get_cls_embedding(
    text: str,
    model,      # transformers PreTrainedModel (SciBERT or RoBERTa)
    tokenizer,  # transformers PreTrainedTokenizer
    device: str = 'cpu',
) -> np.ndarray:
    """
    Extract the [CLS] token embedding from a BERT-based encoder.

    Passes the input text through the encoder and returns the hidden state
    at position 0 (the [CLS] token), which serves as a sentence-level
    semantic representation of the entire reasoning path.

    Args:
        text: Full chain-of-thought reasoning path text.
        model: Loaded BERT-based encoder (SciBERT or RoBERTa).
        tokenizer: Corresponding tokenizer.
        device: torch device string (e.g., 'cpu', 'cuda').

    Returns:
        CLS token embedding as a numpy array of shape (d,) where d=768.
    """
    import torch

    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True,
        max_length=512,
        padding=True,
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    # Extract [CLS] token: hidden state at position 0
    cls_embedding = outputs.last_hidden_state[:, 0, :]  # shape: (1, d)
    return cls_embedding.squeeze(0).cpu().numpy()        # shape: (d,)


def embed_responses(
    responses: List[str],
    model,
    tokenizer,
    device: str = 'cpu',
) -> np.ndarray:
    """
    Embed a list of reasoning-path responses into a matrix of [CLS] embeddings.

    Args:
        responses: List of k chain-of-thought text responses.
        model: Loaded BERT-based encoder.
        tokenizer: Corresponding tokenizer.
        device: torch device string.

    Returns:
        Embedding matrix of shape (k, d).
    """
    embeddings = [
        get_cls_embedding(r, model, tokenizer, device) for r in responses
    ]
    return np.array(embeddings)  # (k, d)


def load_scibert(device: str = 'cpu'):
    """
    Load SciBERT (110M) for mathematical reasoning tasks (AQuA-RAT, SVAMP).

    Model: allenai/scibert_scivocab_uncased
    License: Apache 2.0

    Returns:
        Tuple of (model, tokenizer).
    """
    from transformers import AutoTokenizer, AutoModel

    model_name = 'allenai/scibert_scivocab_uncased'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)
    model.eval()
    return model, tokenizer


def load_roberta(device: str = 'cpu'):
    """
    Load RoBERTa base (125M) for commonsense reasoning tasks (StrategyQA).

    Model: roberta-base
    License: MIT

    Returns:
        Tuple of (model, tokenizer).
    """
    from transformers import AutoTokenizer, AutoModel

    model_name = 'roberta-base'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)
    model.eval()
    return model, tokenizer


def get_featurizer_for_dataset(dataset: str, device: str = 'cpu'):
    """
    Return the appropriate featurizer for a given dataset.

    Mapping:
        AQuA-RAT -> SciBERT (math)
        SVAMP    -> SciBERT (math)
        StrategyQA -> RoBERTa (commonsense)

    Args:
        dataset: One of 'aqua_rat', 'svamp', 'strategyqa'.
        device: torch device string.

    Returns:
        Tuple of (model, tokenizer).

    Raises:
        ValueError: If dataset is not recognized.
    """
    if dataset in ('aqua_rat', 'svamp'):
        return load_scibert(device)
    elif dataset == 'strategyqa':
        return load_roberta(device)
    else:
        raise ValueError(f"Unknown dataset: {dataset}. "
                         f"Expected one of: 'aqua_rat', 'svamp', 'strategyqa'")
