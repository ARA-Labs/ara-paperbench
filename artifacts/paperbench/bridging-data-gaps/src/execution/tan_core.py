"""
TAN (Transfer via Adversarial Noise) — Core Implementation Stubs
Paper: "Efficient Transfer Learning in Diffusion Models via Adversarial Noise"
Wang et al., arXiv:2308.11948v1

Implements:
  - AdaptorLayer: Parameter-efficient U-Net adaptor module (Eq. in §4.2)
  - augmented_forward: Frozen U-Net + adaptor residual (xl_t = θl(x^(l-1)) + ψl(x^(l-1)))
  - adversarial_noise_selection: PGD inner maximization (Eq. 8 / Algorithm 1 lines 7-12)
  - similarity_guided_loss: Outer minimization loss (Eq. 9)
  - tan_training_step: Single TAN training step (Algorithm 1)
  - train_binary_classifier: Fine-tune ImageNet classifier for source/target discrimination
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Callable, Tuple


class AdaptorLayer(nn.Module):
    """
    Adaptor module ψl for a single U-Net layer (§4.2, Eq. in §5.2).

    Architecture:
        ψl(x) = f(x @ Wdown) @ Wup
    where x ∈ R^(B × C × H × W) is projected down, activated, projected up.
    All parameters initialized to zero so initial output = 0.

    The augmented layer output is:
        xl_t = θl(x^(l-1)) + ψl(x^(l-1))   (frozen θl + trainable ψl)
    """

    def __init__(
        self,
        in_channels: int,    # r: input channel dimension
        spatial_factor: int, # c: spatial downscale factor (DDPM: 4, LDM: 2)
        bottleneck_dim: int, # d: bottleneck channel dimension (DDPM/LDM: 8)
    ) -> None:
        super().__init__()
        self.spatial_factor = spatial_factor
        self.bottleneck_dim = bottleneck_dim

        # Wdown: projects R^(C×H×W) -> R^(bottleneck_dim × H/c × W/c)
        self.W_down = nn.Conv2d(
            in_channels=in_channels,
            out_channels=bottleneck_dim,
            kernel_size=spatial_factor,
            stride=spatial_factor,
            bias=True,
        )
        # Wup: projects R^(bottleneck_dim × H/c × W/c) -> R^(C × H × W)
        self.W_up = nn.ConvTranspose2d(
            in_channels=bottleneck_dim,
            out_channels=in_channels,
            kernel_size=spatial_factor,
            stride=spatial_factor,
            bias=True,
        )
        # Initialize all parameters to zero (§5.2: "set all the extra layer parameters to zero")
        self._zero_init()

    def _zero_init(self) -> None:
        """Initialize all adaptor parameters to zero."""
        for p in self.parameters():
            nn.init.zeros_(p)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input activations from previous layer, shape (B, C, H, W)
        Returns:
            Residual correction, shape (B, C, H, W)
            (All zeros at initialization; gradually updated during training)
        """
        h = self.W_down(x)         # (B, d, H/c, W/c)
        h = F.silu(h)              # nonlinear activation f(·)
        h = self.W_up(h)           # (B, C, H, W)
        return h


def augmented_forward(
    frozen_layer: nn.Module,
    adaptor: AdaptorLayer,
    x_prev: torch.Tensor,
) -> torch.Tensor:
    """
    Augmented U-Net forward pass for one layer (§4.2):
        xl_t = θl(x^(l-1)) + ψl(x^(l-1))

    Args:
        frozen_layer: Pre-trained frozen U-Net layer θl
        adaptor: Trainable adaptor module ψl
        x_prev: Input activations x^(l-1), shape (B, C, H, W)
    Returns:
        Output activations xl_t, shape (B, C, H, W)
    """
    with torch.no_grad():
        frozen_out = frozen_layer(x_prev)   # θl(x^(l-1)), no gradient
    adaptor_out = adaptor(x_prev)            # ψl(x^(l-1)), gradient flows
    return frozen_out + adaptor_out


def adversarial_noise_selection(
    x0: torch.Tensor,                       # Target image, shape (B, C, H, W)
    t: torch.Tensor,                         # Timestep, shape (B,)
    alpha_bar_t: torch.Tensor,               # ᾱt, shape (B, 1, 1, 1)
    frozen_eps_theta: Callable,              # Frozen pre-trained model εθ(xt, t)
    J: int = 10,                             # Number of PGD steps (default: 10)
    omega: float = 0.02,                     # PGD step size ω (default: 0.02)
) -> torch.Tensor:
    """
    Inner maximization via PGD to find worst-case Gaussian noise ε* (Eq. 8 / Alg. 1).

    Solves:
        ε* = argmax_ε ||ε - εθ(√ᾱt·x0 + √(1-ᾱt)·ε, t)||²
        subject to: ε*_mean = 0, ε*_std = I

    Args:
        x0: Target image batch
        t: Timestep indices
        alpha_bar_t: Cumulative noise schedule ᾱt, broadcast-compatible with x0
        frozen_eps_theta: Frozen pre-trained denoising network εθ
        J: Number of PGD gradient ascent steps
        omega: PGD step size
    Returns:
        eps_star: Worst-case noise ε*, shape same as x0, normalized to mean=0, std=I
    """
    # Initialize with standard Gaussian noise (ε0 ~ N(0,I))
    eps = torch.randn_like(x0)

    for j in range(J):
        eps = eps.detach().requires_grad_(True)

        # Form noised image: xt = √ᾱt·x0 + √(1-ᾱt)·εj
        sqrt_alpha_bar = alpha_bar_t.sqrt()
        sqrt_one_minus_alpha_bar = (1.0 - alpha_bar_t).sqrt()
        xt = sqrt_alpha_bar * x0 + sqrt_one_minus_alpha_bar * eps

        # Compute denoising loss (no gradient to frozen model)
        with torch.no_grad():
            eps_pred = frozen_eps_theta(xt, t)
        # Recompute for gradient w.r.t. eps
        xt_grad = sqrt_alpha_bar * x0 + sqrt_one_minus_alpha_bar * eps
        eps_pred_grad = frozen_eps_theta(xt_grad, t)
        loss = ((eps - eps_pred_grad) ** 2).mean()

        # Gradient ascent step
        loss.backward()
        with torch.no_grad():
            eps_new = eps + omega * eps.grad.sign()  # gradient ascent
            # Norm: normalize to maintain Gaussian statistics (mean=0, std=I)
            eps_new = eps_new - eps_new.mean(dim=[1, 2, 3], keepdim=True)
            eps_new = eps_new / (eps_new.std(dim=[1, 2, 3], keepdim=True) + 1e-8)
        eps = eps_new.detach()

    return eps  # ε* = εJ


def similarity_guided_loss(
    eps_star: torch.Tensor,                   # Worst-case noise ε*, shape (B, C, H, W)
    x_star_t: torch.Tensor,                   # Worst-case noised image x*t, shape (B, C, H, W)
    t: torch.Tensor,                           # Timestep, shape (B,)
    sigma_hat_sq_t: torch.Tensor,             # σ̂²t = (1-ᾱ_{t-1}) / √(1-ᾱt), shape (B,1,1,1)
    gamma: float,                              # Similarity guidance scale γ (default: 5)
    eps_theta_psi: Callable,                   # Augmented model εθ,ψ (frozen θ + trainable ψ)
    classifier_log_grad: torch.Tensor,         # ∇x*t log pϕ(y=T|x*t), shape (B, C, H, W)
) -> torch.Tensor:
    """
    Compute outer similarity-guided loss L(ψ) (Eq. 9).

    L(ψ) = ||ε* - εθ,ψ(x*t, t) - σ̂²t·γ·∇x*t log pϕ(y=T|x*t)||²

    Args:
        eps_star: Worst-case noise from adversarial_noise_selection
        x_star_t: Noised image formed from ε* and x0
        t: Timestep
        sigma_hat_sq_t: σ̂²t = (1-ᾱ_{t-1})·(1/(1-ᾱt))^0.5  [shape broadcastable to (B,C,H,W)]
        gamma: Similarity guidance hyperparameter (set to 5)
        eps_theta_psi: Augmented model (frozen pre-trained + trainable adaptor)
        classifier_log_grad: Gradient of log pϕ(y=T|x*t) w.r.t. x*t (from frozen binary classifier)
    Returns:
        Scalar loss L(ψ)
    """
    # Predicted noise from augmented model
    eps_pred = eps_theta_psi(x_star_t, t)  # shape (B, C, H, W)

    # Corrected noise target: ε* - σ̂²t·γ·∇ log pϕ(y=T|x*t)
    correction = sigma_hat_sq_t * gamma * classifier_log_grad
    target = eps_star - correction

    # Mean squared error loss
    loss = ((target - eps_pred) ** 2).mean()
    return loss


def compute_classifier_gradient(
    classifier: nn.Module,                    # Frozen binary classifier pϕ
    x_star_t: torch.Tensor,                   # Noised image, shape (B, C, H, W)
    target_class_idx: int = 1,                # Index for target domain class T
) -> torch.Tensor:
    """
    Compute ∇x*t log pϕ(y=T|x*t) for similarity guidance.

    Args:
        classifier: Frozen binary classifier distinguishing source (y=0) vs. target (y=1)
        x_star_t: Worst-case noised image x*t
        target_class_idx: Class index for target domain (default: 1)
    Returns:
        Gradient ∇x*t log pϕ(y=T|x*t), shape same as x_star_t
    """
    x_input = x_star_t.detach().requires_grad_(True)
    logits = classifier(x_input)                              # (B, 2)
    log_probs = F.log_softmax(logits, dim=-1)                 # (B, 2)
    log_p_target = log_probs[:, target_class_idx].sum()       # scalar
    log_p_target.backward()
    return x_input.grad.detach()                              # (B, C, H, W)


def tan_training_step(
    x0: torch.Tensor,                         # Target image batch (B, C, H, W)
    adaptor_params: nn.ParameterList,          # Trainable adaptor parameters
    frozen_eps_theta: Callable,                # Frozen pre-trained εθ
    eps_theta_psi: Callable,                   # Augmented model εθ,ψ
    frozen_classifier: nn.Module,             # Frozen binary classifier pϕ
    noise_schedule: dict,                     # Dict with 'alpha_bar' (T,), 'sigma_hat_sq' (T,)
    optimizer: torch.optim.Optimizer,
    T_max: int = 1000,                        # Max timestep
    J: int = 10,                              # PGD steps
    omega: float = 0.02,                      # PGD step size
    gamma: float = 5.0,                       # Similarity guidance scale
) -> float:
    """
    Single TAN training step following Algorithm 1.

    Steps:
      1. Sample t ~ Uniform({1,...,T})
      2. Adversarial noise selection: find ε* via J-step PGD (Eq. 8)
      3. Compute similarity-guided loss L(ψ) (Eq. 9)
      4. Backprop through ψ only; update adaptor parameters

    Args:
        x0: Batch of target domain images
        adaptor_params: Trainable adaptor module parameters (all others frozen)
        frozen_eps_theta: Frozen pre-trained DDPM/LDM denoising network
        eps_theta_psi: Full augmented network (frozen θ + trainable ψ)
        frozen_classifier: Frozen binary classifier for similarity guidance
        noise_schedule: Precomputed ᾱt and σ̂²t for all timesteps
        optimizer: Optimizer over adaptor parameters only
        T_max: Maximum DDPM timestep
        J: PGD inner loop steps
        omega: PGD step size ω
        gamma: Similarity guidance scale γ
    Returns:
        Scalar loss value (float)
    """
    B = x0.shape[0]
    device = x0.device

    # Sample random timestep t ~ Uniform({1,...,T})
    t = torch.randint(1, T_max + 1, (B,), device=device)

    # Get noise schedule values for timestep t
    alpha_bar_t = noise_schedule['alpha_bar'][t].view(B, 1, 1, 1).to(device)   # (B,1,1,1)
    sigma_hat_sq_t = noise_schedule['sigma_hat_sq'][t].view(B, 1, 1, 1).to(device)

    # Step 1: Find worst-case noise ε* via PGD (inner maximization, Eq. 8)
    with torch.no_grad():
        eps_star = adversarial_noise_selection(
            x0=x0,
            t=t,
            alpha_bar_t=alpha_bar_t,
            frozen_eps_theta=frozen_eps_theta,
            J=J,
            omega=omega,
        )

    # Step 2: Form worst-case noised image x*t = √ᾱt·x0 + √(1-ᾱt)·ε*
    x_star_t = alpha_bar_t.sqrt() * x0 + (1.0 - alpha_bar_t).sqrt() * eps_star

    # Step 3: Compute classifier gradient ∇x*t log pϕ(y=T|x*t)
    classifier_grad = compute_classifier_gradient(
        classifier=frozen_classifier,
        x_star_t=x_star_t,
        target_class_idx=1,
    )

    # Step 4: Compute similarity-guided loss L(ψ) (Eq. 9)
    optimizer.zero_grad()
    loss = similarity_guided_loss(
        eps_star=eps_star,
        x_star_t=x_star_t,
        t=t,
        sigma_hat_sq_t=sigma_hat_sq_t,
        gamma=gamma,
        eps_theta_psi=eps_theta_psi,
        classifier_log_grad=classifier_grad,
    )

    # Step 5: Update only adaptor parameters ψ
    loss.backward()
    optimizer.step()

    return loss.item()


def train_binary_classifier(
    source_images: torch.Tensor,   # Source domain images, shape (N_s, C, H, W)
    target_images: torch.Tensor,   # Target domain images (10-shot), shape (10, C, H, W)
    backbone: nn.Module,           # Pre-trained ImageNet backbone
    num_classes: int = 2,          # Binary: source (0) vs. target (1)
    num_epochs: int = 100,         # Training epochs (not specified in paper)
    lr: float = 1e-4,              # Classifier learning rate (not specified in paper)
) -> nn.Module:
    """
    Fine-tune an ImageNet pre-trained model with a binary classification head
    to distinguish source domain (y=0) from target domain (y=1) images at
    various noised timesteps.

    Per §5.2: "we establish a fixed pre-trained binary classifier that differentiates
    between source and target images at time step t"

    Args:
        source_images: Images from source domain S (FFHQ or LSUN Church)
        target_images: 10-shot images from target domain T
        backbone: Pre-trained ImageNet model (e.g., ResNet, ViT)
        num_classes: 2 (binary: source vs. target)
        num_epochs: Number of fine-tuning epochs
        lr: Learning rate for classifier fine-tuning
    Returns:
        Trained binary classifier pϕ (to be frozen during DPM fine-tuning)
    """
    classifier = nn.Sequential(
        backbone,
        nn.Linear(backbone.out_features, num_classes),  # type: ignore
    )
    optimizer = torch.optim.Adam(classifier.parameters(), lr=lr)

    # Labels: 0 for source, 1 for target
    source_labels = torch.zeros(len(source_images), dtype=torch.long)
    target_labels = torch.ones(len(target_images), dtype=torch.long)
    all_images = torch.cat([source_images, target_images], dim=0)
    all_labels = torch.cat([source_labels, target_labels], dim=0)

    for epoch in range(num_epochs):
        logits = classifier(all_images)
        loss = F.cross_entropy(logits, all_labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Freeze classifier for use in TAN training
    for p in classifier.parameters():
        p.requires_grad_(False)

    return classifier
