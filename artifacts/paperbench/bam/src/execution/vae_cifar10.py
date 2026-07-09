"""
VAE (Variational Autoencoder) for CIFAR-10 experiment (Section 5.3, Appendix E.6).

Architecture:
  - Encoder: 5-layer convolutional network → factorized Gaussian q(z|x)
  - Decoder: 5-layer convolutional network Ω(z, θ̂): ℝ²⁵⁶ → ℝ³⁰⁷²
  - Latent dimension: D = 256
  - Image dimension: 3072 (32×32×3 CIFAR-10)
  - Likelihood: N(Ω(z, θ̂), 0.1·I₃₀₇₂)

Training procedure (Appendix E.6):
  - Variational EM: maximize marginal likelihood over θ
  - Factorized Gaussian approximation q(z_n|x_n) = N(μ(x_n), diag(σ²(x_n)))
  - 100 epochs; ELBO converges (Figure E.8)
  - Optimizer: Standard VAE training (Adam)

Posterior inference (test time):
  - Draw test image x' from CIFAR-10 test split
  - Initialize: z ~ N(0, I₂₅₆)
  - Pilot run: T=100 iterations for learning rate selection
  - Main run: T=1000 iterations (BaM/ADVI/GSM)
  - Evaluate MSE = ||Ω(E[z'|x']) - x'||² / 3072
"""
import numpy as np
from typing import Callable, Tuple


# Model configuration (Section 5.3)
VAE_CONFIG = {
    "latent_dim": 256,           # D = 256
    "image_dim": 3072,           # 32 × 32 × 3
    "image_channels": 3,
    "image_height": 32,
    "image_width": 32,
    "encoder_layers": 5,         # 5-layer convolutional network
    "decoder_layers": 5,         # 5-layer convolutional network
    "sigma2": 0.1,               # Likelihood noise σ² = 0.1 (eq. 29)
    "training_epochs": 100,      # pre-training epochs
    "posterior_inference": {
        "pilot_iters": 100,      # T=100 pilot run for LR selection
        "main_iters": 1000,      # T=1000 main run
    },
    "dataset": "CIFAR-10",
    "batch_sizes_vi": [10, 100, 300],  # B values for posterior inference
}

# ADVI and BaM learning rates (Appendix E.6)
DEEP_GEN_LR = {
    "advi": {
        "selected": 0.02,
        "search_range": [0.001, 0.01, 0.02, 0.05],
    },
    "bam": {
        "B=10": {
            "selected": 0.1,
            "search_range": [0.01, 0.1, 0.2, 10],
        },
        "B=100": {
            "selected": 50,
            "search_range": [2, 20, 50, 100, 200],
        },
        "B=300": {
            "selected": 7500,
            "search_range": [1000, 5000, 7500, 10000],
        },
    },
}


def reconstruction_mse(
    z_posterior_mean: np.ndarray,  # (D=256,) — posterior mean E[z'|x']
    decoder_fn: Callable,          # Ω(·, θ̂): ℝ²⁵⁶ → ℝ³⁰⁷²
    x_prime: np.ndarray,           # (3072,) — original test image
) -> float:
    """
    Compute MSE between reconstructed image and original test image.

    MSE = ||Ω(E[z'|x'], θ̂) - x'||² / 3072

    Used in Figure 5.4 (iterations vs. MSE) and Figure E.7 (wallclock vs. MSE).

    Args:
        z_posterior_mean: Estimated posterior mean from VI
        decoder_fn: Pre-trained decoder network
        x_prime: Original CIFAR-10 test image

    Returns:
        MSE (scalar)
    """
    x_recon = decoder_fn(z_posterior_mean)  # (3072,)
    return float(np.mean((x_recon - x_prime) ** 2))


def vae_posterior_score(
    z: np.ndarray,         # (D,) latent vector
    decoder_fn: Callable,  # Ω(·, θ̂)
    x_prime: np.ndarray,   # (3072,) observed image
    sigma2: float = 0.1,
) -> np.ndarray:
    """
    Score of VAE posterior p(z'|x') ∝ p(z') p(x'|z').

    ∇_z log p(z'|x') = ∇_z log p(z') + ∇_z log p(x'|z')
                      = -z + (1/σ²) J_Ω(z)⊤ (x' - Ω(z, θ̂))

    where J_Ω is the Jacobian of the decoder.

    In practice, computed via:
        jax.grad(lambda z: log_prior(z) + log_likelihood(z, x, decoder, sigma2))(z)

    Args:
        z: Latent vector, shape (D=256,)
        decoder_fn: Pre-trained decoder Ω(·, θ̂)
        x_prime: Observed test image, shape (3072,)
        sigma2: Likelihood noise σ²

    Returns:
        score: ∇_z log p(z'|x'), shape (D,)
    """
    # Prior score: ∇_z log N(z; 0, I) = -z
    prior_score = -z  # (D,)

    # Likelihood score: ∇_z log N(x'; Ω(z), σ²I) = (1/σ²) J_Ω^T (x' - Ω(z))
    # In JAX: jax.grad(lambda z: -0.5/sigma2 * jnp.sum((x_prime - decoder_fn(z))**2))(z)
    raise NotImplementedError(
        "Requires JAX autodiff for Jacobian computation. "
        "Use: jax.grad(log_likelihood, argnums=0)(z) in JAX."
    )


def load_cifar10(split: str = "train"):
    """
    Load CIFAR-10 dataset.

    Dataset: CIFAR-10 (Krizhevsky, 2009)
    - 50,000 training images, 10,000 test images
    - 32×32 RGB images
    - Images modeled as continuous: x ∈ ℝ³⁰⁷²
    - Normalized to [0, 1] range

    Args:
        split: "train" or "test"

    Returns:
        images: Array of shape (N, 3072), dtype float32
    """
    # Requires: torchvision or tensorflow_datasets
    # from torchvision.datasets import CIFAR10
    # import torchvision.transforms as transforms
    # ...
    raise NotImplementedError("Requires torchvision or tensorflow_datasets for CIFAR-10.")


def sample_test_image(seed: int = 0) -> np.ndarray:
    """
    Sample a single test image x' from CIFAR-10 test split.
    Used for posterior inference evaluation in Section 5.3.

    Args:
        seed: Random seed for reproducibility

    Returns:
        x_prime: Single test image, shape (3072,)
    """
    # Load test set and sample one image
    rng = np.random.default_rng(seed)
    # test_images = load_cifar10("test")
    # idx = rng.integers(len(test_images))
    # return test_images[idx]
    raise NotImplementedError("Requires CIFAR-10 dataset.")
