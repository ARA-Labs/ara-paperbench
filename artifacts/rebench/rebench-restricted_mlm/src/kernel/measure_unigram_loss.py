import torch
import numpy as np
import os
from tqdm import tqdm
import time
import math
import torch.nn as nn
import torch.nn.functional as F

vocab_size = 50257
device = "cuda:7"
dataset = "openwebtext"
data_dir = os.path.join("data/data", dataset)

# estimate unigram loss
data = np.memmap(os.path.join(data_dir, "train.bin"), dtype=np.uint16, mode="r")
n_tokens_for_unigram = vocab_size * 200
data_section = torch.from_numpy(data[:n_tokens_for_unigram].astype(np.int32)).to(device)


def unigram_loss_efficient(sequence, vocab_size, smoothing=1e-5):
    """
    Compute the loss of a unigram model for a given sequence using an efficient weighted sum.

    Args:
    - sequence (torch.LongTensor): Input sequence of token indices
    - vocab_size (int): Size of the vocabulary
    - smoothing (float): Smoothing parameter for the unigram distribution

    Returns:
    - loss (torch.Tensor): Negative log-likelihood loss
    """
    # Compute token counts
    counts = torch.bincount(sequence, minlength=vocab_size).float()

    # Add smoothing
    smoothed_counts = counts + smoothing

    # Compute token probabilities
    probs = smoothed_counts / smoothed_counts.sum()
    torch.save(probs, "unigrams.pt")

    # Compute log probabilities
    log_probs = torch.log(probs)

    # Compute negative log-likelihood using indexing
    nll = -log_probs[sequence].sum()

    # Normalize by sequence length
    loss = nll / len(sequence)

    return loss


def bigram_loss(sequence, vocab_size, smoothing=1e-5, backward=False):
    """
    Compute the combined loss of a bigram and unigram model for a given sequence.

    Args:
    - sequence (torch.LongTensor): Input sequence of token indices
    - vocab_size (int): Size of the vocabulary
    - bigram_weight (float): Weight for the bigram component (1 - bigram_weight for unigram)
    - smoothing (float): Smoothing parameter for the distributions

    Returns:
    - loss (torch.Tensor): Combined negative log-likelihood loss
    """
    # Compute unigram counts

    # Compute bigram counts
    from_index = slice(0, -1) if not backward else slice(1, None)
    to_index = slice(1, None) if not backward else slice(0, -1)
    bigram_counts = torch.zeros(vocab_size, vocab_size, dtype=torch.float, device=sequence.device)
    bigram_indices = torch.stack([sequence[from_index], sequence[to_index]], dim=0)
    bigram_counts.index_put_(
        (bigram_indices[0], bigram_indices[1]),
        torch.ones(len(sequence) - 1, device=sequence.device),
        accumulate=True,
    )

    # Add smoothing
    smoothed_bigram_counts = bigram_counts + smoothing

    # Compute probabilities
    bigram_probs = smoothed_bigram_counts / smoothed_bigram_counts.sum(dim=1, keepdim=True)
    torch.save(bigram_probs, f'bigrams_{"backward" if backward else "forward"}.pt')

    # Compute log probabilities
    bigram_log_probs = torch.log(bigram_probs)

    # Compute bigram negative log-likelihood
    bigram_nll = -bigram_log_probs[sequence[from_index], sequence[to_index]].mean()
    return bigram_nll


print("bigram loss", bigram_loss(data_section, 50257).item())
print("backward bigram loss", bigram_loss(data_section, 50257, backward=True).item())
print("unigram loss", unigram_loss_efficient(data_section, 50257).item())
