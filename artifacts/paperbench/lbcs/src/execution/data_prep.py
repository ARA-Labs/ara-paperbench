"""
Data preparation utilities for LBCS experiments.
Handles: MNIST-S, noisy F-MNIST (symmetric label noise), class-imbalanced F-MNIST.
"""

import torch
import numpy as np
from typing import Tuple
from torch.utils.data import Dataset, Subset


def make_mnist_s(
    mnist_dataset,
    n_samples: int = 1000,
    seed: int = 42,
) -> Subset:
    """
    Construct MNIST-S: a random subset of n_samples examples from MNIST.
    Paper §5.1: "MNIST-S which is constructed by random sampling 1,000 examples
    from original MNIST."

    Args:
        mnist_dataset: torchvision MNIST dataset (train split)
        n_samples: Number of examples to sample (default 1000)
        seed: Random seed for reproducibility

    Returns:
        subset: A Subset of mnist_dataset with n_samples examples
    """
    rng = np.random.RandomState(seed)
    indices = rng.choice(len(mnist_dataset), size=n_samples, replace=False)
    return Subset(mnist_dataset, indices.tolist())


def apply_symmetric_label_noise(
    labels: torch.Tensor,
    noise_rate: float,
    n_classes: int = 10,
    seed: int = 42,
) -> torch.Tensor:
    """
    Apply symmetric label noise: randomly flip noise_rate fraction of labels
    to a uniformly random class (different from original).

    Paper §5.3: "30% symmetric label noise" and "50% symmetric label noise."
    Symmetric noise: the noisy label is drawn uniformly from all classes
    (including the original class, depending on convention; here we use
    any random class with equal probability, consistent with Ma et al., 2020).

    Args:
        labels: Original integer labels, shape (n,)
        noise_rate: Fraction of labels to corrupt (e.g., 0.30 or 0.50)
        n_classes: Number of classes (default 10)
        seed: Random seed

    Returns:
        noisy_labels: Corrupted labels, shape (n,)
    """
    rng = np.random.RandomState(seed)
    noisy_labels = labels.clone()
    n = len(labels)
    n_noisy = int(noise_rate * n)
    noisy_indices = rng.choice(n, size=n_noisy, replace=False)
    for idx in noisy_indices:
        # Flip to a uniformly random class (symmetric noise)
        noisy_labels[idx] = rng.randint(0, n_classes)
    return noisy_labels


def make_class_imbalanced_fmnist(
    fmnist_dataset,
    imbalance_ratio: float = 0.01,
    n_classes: int = 10,
    seed: int = 42,
) -> Subset:
    """
    Construct exponentially class-imbalanced F-MNIST training set.

    Paper §5.3: "exponential type of class imbalance (Cao et al., 2019),
    imbalanced ratio is set to 0.01."

    Exponential imbalance: class c has N_c = N_max * (imbalance_ratio)^{c/(n_classes-1)}
    examples, where c=0 is the majority class.

    Args:
        fmnist_dataset: torchvision FashionMNIST dataset (train split)
        imbalance_ratio: Ratio of min to max class size (default 0.01)
        n_classes: Number of classes (default 10)
        seed: Random seed

    Returns:
        imbalanced_subset: Subset of fmnist_dataset with exponential class imbalance
    """
    rng = np.random.RandomState(seed)
    targets = np.array(fmnist_dataset.targets)

    # Find samples per class
    class_indices = [np.where(targets == c)[0] for c in range(n_classes)]
    n_max = len(class_indices[0])  # assume class 0 is majority

    selected_indices = []
    for c in range(n_classes):
        # Exponential schedule
        n_c = int(n_max * (imbalance_ratio ** (c / (n_classes - 1))))
        n_c = max(1, min(n_c, len(class_indices[c])))
        chosen = rng.choice(class_indices[c], size=n_c, replace=False)
        selected_indices.extend(chosen.tolist())

    return Subset(fmnist_dataset, selected_indices)
