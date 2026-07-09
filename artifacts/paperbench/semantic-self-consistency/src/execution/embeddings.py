"""
Semantic Self-Consistency — Featurizer Utilities

Provides dataset-appropriate featurizer selection and batch embedding extraction
for reasoning paths using BERT-variant models (SciBERT, RoBERTa).

Per paper:
- SciBERT 110M → AQuA-RAT, SVAMP (mathematical/scientific reasoning)
- RoBERTa 125M → StrategyQA (commonsense reasoning)
"""

import numpy as np
from typing import List


FEATURIZER_MAP = {
    "aqua_rat": "allenai/scibert_scivocab_uncased",
    "svamp": "allenai/scibert_scivocab_uncased",
    "strategyqa": "roberta-base",
}


def load_featurizer(dataset_name: str):
    """
    Load the appropriate BERT-variant featurizer for a given dataset.

    Featurizer selection per Section 3.2:
    - SciBERT (allenai/scibert_scivocab_uncased, ~110M params) for AQuA-RAT and SVAMP
    - RoBERTa base (roberta-base, ~125M params) for StrategyQA

    Args:
        dataset_name: One of "aqua_rat", "svamp", "strategyqa".

    Returns:
        Tuple of (model, tokenizer) in eval mode.
    """
    from transformers import AutoModel, AutoTokenizer
    import torch

    if dataset_name not in FEATURIZER_MAP:
        raise ValueError(
            f"Unknown dataset '{dataset_name}'. "
            f"Choose from: {list(FEATURIZER_MAP.keys())}"
        )

    model_name = FEATURIZER_MAP[dataset_name]
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model.eval()

    return model, tokenizer


def embed_reasoning_path(
    reasoning_path: str,
    model,
    tokenizer,
    max_length: int = 512
) -> np.ndarray:
    """
    Embed a single reasoning path using the [CLS] token of a BERT-variant model.

    The [CLS] token (index 0 of last_hidden_state) provides a single vector
    representation capturing the overall semantic content of the full reasoning path.

    Args:
        reasoning_path: Full chain-of-thought response text string to embed.
        model: Loaded BERT-variant model (AutoModel) in eval mode.
        tokenizer: Corresponding AutoTokenizer.
        max_length: Maximum token length for truncation (default 512).

    Returns:
        Embedding vector of shape (hidden_size,) = (768,) for BERT-base variants.
    """
    import torch

    inputs = tokenizer(
        reasoning_path,
        return_tensors="pt",
        truncation=True,
        max_length=max_length,
        padding=True
    )
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract [CLS] token embedding from last hidden state
    cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze(0).cpu().numpy()
    return cls_embedding  # shape: (768,)


def embed_batch(
    reasoning_paths: List[str],
    model,
    tokenizer,
    max_length: int = 512,
    batch_size: int = 32
) -> np.ndarray:
    """
    Embed a batch of reasoning paths efficiently.

    Args:
        reasoning_paths: List of k reasoning path strings.
        model: Loaded BERT-variant model in eval mode.
        tokenizer: Corresponding AutoTokenizer.
        max_length: Maximum token length (default 512).
        batch_size: Number of sequences to process at once (default 32).

    Returns:
        Embedding matrix of shape (k, hidden_size).
    """
    import torch

    all_embeddings = []

    for i in range(0, len(reasoning_paths), batch_size):
        batch = reasoning_paths[i:i + batch_size]
        inputs = tokenizer(
            batch,
            return_tensors="pt",
            truncation=True,
            max_length=max_length,
            padding=True
        )
        with torch.no_grad():
            outputs = model(**inputs)

        # [CLS] tokens: shape (batch_size, hidden_size)
        cls_embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
        all_embeddings.append(cls_embeddings)

    return np.vstack(all_embeddings)  # shape: (k, hidden_size)


def get_embeddings_for_dataset(
    reasoning_paths: List[str],
    dataset_name: str,
    max_length: int = 512
) -> np.ndarray:
    """
    Convenience function: load the appropriate featurizer for a dataset and
    embed all reasoning paths.

    Args:
        reasoning_paths: List of k reasoning path strings.
        dataset_name: One of "aqua_rat", "svamp", "strategyqa".
        max_length: Max token length for truncation.

    Returns:
        Embedding matrix of shape (k, 768).
    """
    model, tokenizer = load_featurizer(dataset_name)
    return embed_batch(reasoning_paths, model, tokenizer, max_length=max_length)
