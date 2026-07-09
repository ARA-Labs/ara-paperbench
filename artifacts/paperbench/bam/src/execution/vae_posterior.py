"""
VAE Posterior Inference with BaM/ADVI/GSM
Paper: "Batch and Match: BBVI with a Score-Based Divergence", Section 5.3

Deep generative model setup for CIFAR-10 experiment (Figure 5.4).

Generative model:
  z_n ~ N(0, I)           [prior in R^256]
  x_n | z_n ~ N(Ω(z_n, θ̂), σ²I)  [Gaussian likelihood; σ²=0.1]
  
  Ω: decoder network (5 conv layers), θ̂: trained weights
  
Posterior inference task:
  Given test image x', approximate p(z'|x') using full-covariance Gaussian q.
  Score: s(z) = ∇_z [log p(z) + log p(x'|z)] = -z + (1/σ²)J_Ω(z)^T (x' - Ω(z))
  
Evaluation metric:
  MSE = ||x' - Ω(E[z'|x'], θ̂)||²  / dim(x)
  
VAE training:
  - CIFAR-10 training split (50,000 images)
  - 100 epochs; standard VAE ELBO
  - Factorized Gaussian encoder q_φ(z|x) (amortized VI for training)
  - After training: use BaM/ADVI/GSM for exact full-covariance inference at test time

Pilot run for learning rate selection:
  - 100 iterations pilot run; select λ minimizing MSE
  - BaM grids: B=10→{0.01,0.1,0.2,10}; B=100→{2,20,50,100,200}; B=300→{1000,5000,7500,10000}
  - ADVI grid: {0.001, 0.01, 0.02, 0.05} → best=0.02 (consistent)
  - Selected BaM λ: B=10→0.1; B=100→50; B=300→7500
  
Main run: T=1000 iterations
Batch sizes tested: B=10, 100, 300
"""

import numpy as np
import jax
import jax.numpy as jnp
from jax import jit, grad, vmap
from typing import Callable, Tuple


# Model constants (from paper §5.3 and Appendix E.6)
LATENT_DIM = 256     # z ∈ R^256
IMAGE_DIM = 3072     # x ∈ R^{32×32×3}
SIGMA_SQ = 0.1       # Gaussian likelihood variance σ²=0.1
VAE_EPOCHS = 100     # Training epochs for VAE
IMAGE_DATASET = "CIFAR-10"


def make_vae_posterior_score(
    decoder_fn: Callable,  # Ω(z, θ̂): z (D,) -> x_mean (IMAGE_DIM,)
    x_prime: np.ndarray,   # (IMAGE_DIM,) test image x'
    sigma_sq: float = SIGMA_SQ,
) -> Callable:
    """
    Create score function for the VAE posterior p(z'|x').
    
    Score: s(z) = ∇_z [log p(z) + log p(x'|z)]
              = ∇_z [-0.5 ||z||² - (1/(2σ²)) ||x' - Ω(z)||²]
              = -z + (1/σ²) J_Ω(z)^T (x' - Ω(z))
    
    where J_Ω is the Jacobian of the decoder. Computed via JAX autodiff.
    
    Args:
        decoder_fn: Pre-trained decoder network Ω(z, θ̂)
        x_prime:    (IMAGE_DIM,) test image to reconstruct
        sigma_sq:   Gaussian likelihood variance (0.1 in paper)
    
    Returns:
        score_fn: lp_g(samples: (N, D)) -> (N, D) scores for posterior
    """
    x_prime = jnp.array(x_prime)

    def log_posterior_single(z: jnp.ndarray) -> jnp.ndarray:
        """log p(z) + log p(x'|z) for single z."""
        log_prior = -0.5 * jnp.dot(z, z)
        x_recon = decoder_fn(z)
        diff = x_prime - x_recon
        log_likelihood = -0.5 / sigma_sq * jnp.dot(diff, diff)
        return log_prior + log_likelihood

    @jit
    def score_fn(samples: jnp.ndarray) -> jnp.ndarray:
        """Score ∇ log p(z'|x') for batch: (N, D) -> (N, D)."""
        return vmap(grad(log_posterior_single))(samples)

    return score_fn


def reconstruction_mse(
    decoder_fn: Callable,  # Ω(z, θ̂): z (D,) -> x_mean (IMAGE_DIM,)
    mu_hat: np.ndarray,    # (D,) estimated posterior mean E[z'|x']
    x_prime: np.ndarray,   # (IMAGE_DIM,) test image
) -> float:
    """
    Compute image reconstruction MSE.
    
    MSE = ||x' - Ω(μ_hat, θ̂)||² / IMAGE_DIM
    
    Evaluation metric in Figure 5.4. Measures how well the posterior
    mean reconstructs the test image when fed to the decoder.
    
    Args:
        decoder_fn: Pre-trained decoder network
        mu_hat:     (D,) variational posterior mean estimate
        x_prime:    (IMAGE_DIM,) original test image
    Returns:
        mse: Mean squared error (scalar)
    """
    x_recon = np.array(decoder_fn(jnp.array(mu_hat)))
    return float(np.mean((x_prime - x_recon) ** 2))


def run_vae_experiment(
    decoder_fn: Callable,
    encoder_fn: Callable,   # AVI encoder: x -> (mu_z, log_var_z)
    x_prime: np.ndarray,    # (IMAGE_DIM,) test image from CIFAR-10 test split
    key,                    # jax.random.PRNGKey
    D: int = LATENT_DIM,
) -> dict:
    """
    Full VAE posterior inference experiment (Section 5.3, Figure 5.4).
    
    Runs BaM, ADVI, GSM, and AVI to approximate p(z'|x').
    Measures MSE at each iteration.
    
    Protocol:
      1. Sample test image x' from CIFAR-10 test set.
      2. For BaM and ADVI: pilot run of T=100 to select learning rate.
      3. Main run: T=1000 iterations.
      4. At each iteration: compute MSE = ||x' - Ω(μ_t)||² / IMAGE_DIM.
      5. AVI: single forward pass through encoder.
    
    Batch sizes: B = 10, 100, 300
    
    Optimal learning rates (from paper Appendix E.6):
      BaM: B=10→λ=0.1; B=100→λ=50; B=300→λ=7500
      ADVI: lr=0.02 (consistent across all batch sizes)
    
    Args:
        decoder_fn: Trained decoder network Ω(·, θ̂)
        encoder_fn: Trained encoder network q_φ(z|x)
        x_prime:    Test image
        key:        JAX random key
        D:          Latent dimension (256)
    
    Returns:
        results: dict with MSE trajectories for all methods and batch sizes
    
    Note: BaM MSE > 0.2 at B=10; MSE < 0.05 at B=100, 300.
          BaM at B=300 converges ≥10× faster than ADVI and GSM.
          Both BaM and ADVI eventually achieve lower MSE than AVI.
    """
    score_fn = make_vae_posterior_score(decoder_fn, x_prime)

    # Initialize all methods from standard Gaussian
    mu0 = np.zeros(D)
    cov0 = np.eye(D)

    results = {}

    # AVI baseline (single forward pass)
    mu_avi, _ = encoder_fn(x_prime)
    mse_avi = reconstruction_mse(decoder_fn, mu_avi, x_prime)
    results['avi'] = {'mse': mse_avi}

    # BaM / ADVI / GSM runs omitted here; see BaM.fit() / ADVI.fit() / GSM.fit()
    # Use KLMonitor-style callback to record MSE at each iteration.
    # Pilot run: T=100 iterations; grid search for λ (BaM) or lr (ADVI).
    # Main run: T=1000 iterations with selected hyperparameters.

    return results
