"""
Dataset Loading and Data Preparation for TAN Few-Shot Transfer Learning

This module handles loading source and target domain datasets (FFHQ, LSUN Church)
and preparing 10-shot target domain subsets for fine-tuning.
Implements the data processing described in §5.2 of the paper.
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from pathlib import Path
from typing import Optional, Tuple


# ─── Dataset Constants ─────────────────────────────────────────────────────────

FFHQ_SOURCE_TASKS = [
    "Babies",           # 10-shot target; FID eval uses 2,700 images
    "Sunglasses",       # 10-shot target; FID eval uses 2,500 images
    "Raphael_paintings",# 10-shot target (Raphael Peale style)
    "Amedeo_paintings", # 10-shot target (Amedeo Modigliani style)
    "Sketches",         # 10-shot target
]

LSUN_SOURCE_TASKS = [
    "Haunted_houses",    # 10-shot target
    "Landscape_drawings",# 10-shot target
]

NUM_SHOT = 10           # Number of target domain training images
BATCH_SIZE = 40         # Training batch size (§5.2)


class FewShotTargetDataset(Dataset):
    """
    Dataset wrapper for 10-shot target domain adaptation.

    Loads exactly N=10 target domain images from disk.
    Used as the target dataset for fine-tuning the DPM adaptor.

    Args:
        image_dir:  Path to directory containing target domain images
        transform:  Image transforms (resize, normalize, etc.)
        n_shot:     Number of images to use (default: 10)
    """

    def __init__(
        self,
        image_dir: str,
        transform: Optional[transforms.Compose] = None,
        n_shot: int = NUM_SHOT,
    ):
        self.image_dir = Path(image_dir)
        self.n_shot = n_shot
        self.transform = transform or self._default_transform()

        # Collect image paths (sorted for reproducibility)
        self.image_paths = sorted(self.image_dir.glob("*.jpg")) + \
                           sorted(self.image_dir.glob("*.png"))
        self.image_paths = self.image_paths[:n_shot]

        assert len(self.image_paths) >= n_shot, \
            f"Expected {n_shot} images, found {len(self.image_paths)} in {image_dir}"

    @staticmethod
    def _default_transform() -> transforms.Compose:
        """Standard preprocessing for 256×256 generation models."""
        return transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(256),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
        ])

    def __len__(self) -> int:
        return len(self.image_paths)

    def __getitem__(self, idx: int) -> torch.Tensor:
        from PIL import Image
        img = Image.open(self.image_paths[idx]).convert("RGB")
        return self.transform(img)


def get_target_dataloader(
    image_dir: str,
    batch_size: int = BATCH_SIZE,
    n_shot: int = NUM_SHOT,
    num_workers: int = 4,
) -> DataLoader:
    """
    Create DataLoader for few-shot target domain fine-tuning.

    Implements the data processing step from Algorithm 1 (line 2):
    "x_0 ~ q(x_0)" — sampling from the target dataset.

    Args:
        image_dir:   Path to 10-shot target images directory
        batch_size:  Training batch size (40, per §5.2)
        n_shot:      Number of target images (10)
        num_workers: DataLoader worker processes

    Returns:
        DataLoader that cycles over the n_shot images with batch_size
    """
    dataset = FewShotTargetDataset(image_dir=image_dir, n_shot=n_shot)
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        drop_last=True,
    )


def load_ffhq_target_task(
    ffhq_root: str,
    task_name: str,  # e.g., "Babies", "Sunglasses", "Raphael_paintings", etc.
    n_shot: int = NUM_SHOT,
    batch_size: int = BATCH_SIZE,
) -> DataLoader:
    """
    Load a 10-shot FFHQ-based target task for fine-tuning.

    Supported task names: Babies, Sunglasses, Raphael_paintings,
    Amedeo_paintings, Sketches.

    Args:
        ffhq_root:  Root directory containing FFHQ target sub-datasets
        task_name:  Name of the target task/domain
        n_shot:     Number of shots (default: 10)
        batch_size: Training batch size

    Returns:
        DataLoader for the specified target task
    """
    assert task_name in FFHQ_SOURCE_TASKS, \
        f"Task {task_name} not in FFHQ tasks: {FFHQ_SOURCE_TASKS}"
    image_dir = str(Path(ffhq_root) / task_name)
    return get_target_dataloader(image_dir, batch_size=batch_size, n_shot=n_shot)


def load_lsun_target_task(
    lsun_root: str,
    task_name: str,  # e.g., "Haunted_houses", "Landscape_drawings"
    n_shot: int = NUM_SHOT,
    batch_size: int = BATCH_SIZE,
) -> DataLoader:
    """
    Load a 10-shot LSUN Church-based target task for fine-tuning.

    Supported task names: Haunted_houses, Landscape_drawings.

    Args:
        lsun_root:  Root directory containing LSUN Church target sub-datasets
        task_name:  Name of the target task/domain
        n_shot:     Number of shots (default: 10)
        batch_size: Training batch size

    Returns:
        DataLoader for the specified LSUN target task
    """
    assert task_name in LSUN_SOURCE_TASKS, \
        f"Task {task_name} not in LSUN tasks: {LSUN_SOURCE_TASKS}"
    image_dir = str(Path(lsun_root) / task_name)
    return get_target_dataloader(image_dir, batch_size=batch_size, n_shot=n_shot)


def sample_training_batch(
    dataloader_iter,
    t_max: int = 1000,
    device: str = "cuda",
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Sample one training batch from the target dataset.
    Implements the first 3 lines of Algorithm 1:
        x_0 ~ q(x_0)
        t ~ Uniform({1, ..., T})
        ε ~ N(0, I)

    Args:
        dataloader_iter: Iterator over target dataloader
        t_max:           Maximum timestep T (default: 1000 for DDPM)
        device:          Target device

    Returns:
        (x0, t, eps): Clean images (B,C,H,W), timesteps (B,), initial noise (B,C,H,W)
    """
    x0 = next(dataloader_iter).to(device)
    B, C, H, W = x0.shape

    # Randomly sample timestep t ~ Uniform({1, ..., T})
    t = torch.randint(1, t_max + 1, (B,), device=device)

    # Sample standard Gaussian noise ε ~ N(0, I)
    eps = torch.randn_like(x0)

    return x0, t, eps
