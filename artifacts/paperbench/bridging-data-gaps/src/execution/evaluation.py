"""
Evaluation Metrics for TAN: Intra-LPIPS and FID

Implements the evaluation protocol described in §5.2 of the paper:
  - Intra-LPIPS: diversity metric (↑ higher = more diverse)
  - FID: quality metric (↓ lower = better)

Intra-LPIPS computation:
  1. Generate 1,000 images
  2. Assign each image to the training sample with smallest LPIPS distance (nearest-neighbor)
  3. Average pairwise LPIPS within each cluster
  4. Average across all clusters

FID evaluation uses larger held-out datasets:
  - Babies: 2,700 reference images
  - Sunglasses: 2,500 reference images
"""

import torch
import torch.nn as nn
from typing import List, Optional
import numpy as np


class IntraLPIPS:
    """
    Intra-LPIPS diversity metric for few-shot image generation (from CDC [19]).

    Protocol (§5.2):
      1. Generate 1,000 images from the model
      2. For each generated image, find the training image with minimum LPIPS distance
         (nearest-neighbor cluster assignment)
      3. Within each cluster, compute mean pairwise LPIPS distance
      4. Average these within-cluster scores across all clusters

    Higher Intra-LPIPS = more diverse generated images within each mode.
    """

    def __init__(self, lpips_net: str = "alex"):
        """
        Args:
            lpips_net: LPIPS backbone network ('alex', 'vgg', or 'squeeze')
        """
        try:
            import lpips
            self.lpips_fn = lpips.LPIPS(net=lpips_net)
        except ImportError:
            raise ImportError("Install lpips: pip install lpips")

    def assign_clusters(
        self,
        generated: torch.Tensor,   # (N_gen, C, H, W) — generated images
        training: torch.Tensor,     # (N_train, C, H, W) — training images (N_train=10)
    ) -> List[List[int]]:
        """
        Assign each generated image to the training image with minimum LPIPS distance.

        Args:
            generated: Generated images (N_gen=1000, C, H, W)
            training:  Training images (N_train=10, C, H, W)

        Returns:
            clusters: List of N_train lists, each containing indices into `generated`
        """
        N_gen = generated.shape[0]
        N_train = training.shape[0]
        clusters = [[] for _ in range(N_train)]

        for i in range(N_gen):
            min_dist = float("inf")
            min_k = 0
            for k in range(N_train):
                dist = self.lpips_fn(
                    generated[i:i+1], training[k:k+1]
                ).item()
                if dist < min_dist:
                    min_dist = dist
                    min_k = k
            clusters[min_k].append(i)

        return clusters

    def compute(
        self,
        generated: torch.Tensor,   # (N_gen, C, H, W) — N_gen=1000 generated images
        training: torch.Tensor,     # (N_train, C, H, W) — N_train=10 training images
    ) -> float:
        """
        Compute Intra-LPIPS score.

        Args:
            generated: 1,000 generated images (N_gen=1000, C, H, W)
            training:  10-shot training images (N_train=10, C, H, W)

        Returns:
            intra_lpips: Mean within-cluster pairwise LPIPS distance (higher=more diverse)
        """
        clusters = self.assign_clusters(generated, training)

        cluster_scores = []
        for cluster_indices in clusters:
            if len(cluster_indices) < 2:
                continue  # Skip clusters with fewer than 2 generated images
            cluster_imgs = generated[cluster_indices]  # (K, C, H, W)
            pairwise_dists = []
            for i in range(len(cluster_indices)):
                for j in range(i + 1, len(cluster_indices)):
                    d = self.lpips_fn(
                        cluster_imgs[i:i+1], cluster_imgs[j:j+1]
                    ).item()
                    pairwise_dists.append(d)
            cluster_scores.append(float(np.mean(pairwise_dists)))

        return float(np.mean(cluster_scores)) if cluster_scores else 0.0


def generate_samples(
    model_fn,           # callable: noise → image (DPM sampler)
    n_samples: int,     # number of images to generate (1000 for Intra-LPIPS, 10000 for FID)
    image_shape: tuple, # (C, H, W)
    device: str = "cuda",
    batch_size: int = 50,
) -> torch.Tensor:
    """
    Generate N images from the adapted DPM model.

    Used for:
    - Intra-LPIPS evaluation: n_samples=1,000 (§5.2)
    - FID evaluation: n_samples=10,000 (Appendix A.2)
    - Toy 2D experiment: n_samples=20,000 (§5.1, Figure 2b/c)

    Args:
        model_fn:    DPM sampling function returning images given initial noise
        n_samples:   Number of images to generate
        image_shape: Shape of each image (C, H, W)
        device:      Compute device
        batch_size:  Batch size for generation

    Returns:
        images: Tensor of shape (n_samples, C, H, W) in [-1, 1]
    """
    all_images = []
    remaining = n_samples

    while remaining > 0:
        current_batch = min(batch_size, remaining)
        noise = torch.randn(current_batch, *image_shape, device=device)
        with torch.no_grad():
            imgs = model_fn(noise)  # DPM reverse process
        all_images.append(imgs.cpu())
        remaining -= current_batch

    return torch.cat(all_images, dim=0)[:n_samples]


def compute_fid(
    generated_images: torch.Tensor,     # (N, C, H, W) — generated images
    reference_images_path: str,         # path to reference dataset (e.g., Babies 2700, Sunglasses 2500)
    device: str = "cuda",
) -> float:
    """
    Compute FID between generated images and a reference dataset.

    Reference dataset sizes (§5.2):
    - Babies: 2,700 images
    - Sunglasses: 2,500 images

    Note: FID is unstable with 10-shot datasets, so larger reference sets are used.

    Args:
        generated_images:      Generated image tensor (N, C, H, W)
        reference_images_path: Path to reference dataset directory
        device:                Compute device

    Returns:
        fid_score: FID value (lower = better quality)
    """
    try:
        from pytorch_fid import fid_score
        # Standard FID computation via pytorch-fid or torchmetrics
        raise NotImplementedError(
            "Use pytorch-fid library: pip install pytorch-fid\n"
            "torchrun -m pytorch_fid <generated_path> <reference_path>"
        )
    except ImportError:
        raise ImportError("Install pytorch-fid: pip install pytorch-fid")
