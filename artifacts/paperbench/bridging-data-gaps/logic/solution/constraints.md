---
# Constraints and Limitations

## Boundary Conditions

### BC1: 10-shot target domain size
- **Description**: TAN is specifically designed and evaluated for the 10-shot regime (exactly 10 training images in the target domain). Performance may degrade differently outside this range.
- **Source**: §5.1, entire experimental setup uses 10-shot setting

### BC2: Pre-trained source DPM required
- **Description**: TAN requires a well-trained source DPM (DDPM or LDM) pre-trained on a large source dataset. The method adapts this model; it cannot train from scratch on 10 images.
- **Source**: §1, §4

### BC3: Binary classifier requires fine-tuning on target images
- **Description**: The classifier pϕ must be fine-tuned on the 10 target images before TAN training begins. The classifier uses an ImageNet pre-trained backbone. If the target domain is highly dissimilar from ImageNet, classifier quality may degrade.
- **Source**: §5.2 configurations

### BC4: DPM-specific — not applicable to GANs
- **Description**: TAN's similarity-guided loss is derived from the DPM variational lower bound and conditional reverse process formulation. The adaptor architecture is specific to the U-Net in DPMs. GAN architectures are not directly supported.
- **Source**: §1, §2, §4

### BC5: Adaptor parameters c and d must be chosen per backbone
- **Description**: For DDPM: c=4, d=8. For LDM: c=2, d=8. Other DPM backbones may require separate hyperparameter search for these bottleneck dimensions.
- **Source**: §5.2 configurations

### BC6: γ, J, ω are sensitivity-dependent hyperparameters
- **Description**: γ=5 is optimal for FFHQ→Sunglasses; too large (>5) causes overfitting. ω=0.02 is optimal; relatively stable in [0.01, 0.03]. J=10 PGD steps used uniformly. These values may need re-tuning for other source/target pairs.
- **Source**: Appendix A.2, Tables 4-5

### BC7: 300 training iterations is empirically optimal for tested tasks
- **Description**: For FFHQ→Sunglasses, FID reaches minimum at 300 iterations and increases thereafter (overfitting). This may vary for other domain pairs. Below 300 iterations may underfit.
- **Source**: Appendix A.2, Table 6

## Assumptions Made

- The similarity-guidance term $\nabla_{x_t}\log p_\phi(y=S|x_t^T) \approx 0$ for target images (discarded from loss).
- Worst-case noise normalization (mean=0, std=I) sufficiently preserves Gaussian statistics for meaningful PGD adversarial perturbation.
- Minimizing loss under worst-case noise subsumes minimizing under all "easier" (standard Gaussian) noise.

## Known Limitations (from paper Appendix)

### L1: Privacy leakage risk in generated images
- **Description**: Images synthesized by TAN may contain characteristics specific to the target domain training images. For example, sunglasses reflections in generated images may closely resemble those in the target training images, potentially revealing sensitive information about the target images.
- **Source**: Appendix (Limitation section)

### L2: Generated images tied to target domain style
- **Description**: Since the goal is target-domain transfer, generated images necessarily have target-domain characteristics. This can lead to inconsistency in generated images — they are constrained to adopt the target style.
- **Source**: Appendix (Limitation section)

### L3: Only parameter rate, not absolute parameter count, reported
- **Description**: The 1.3%/1.6% parameter rate is relative to the pre-trained model; the absolute number of adaptor parameters depends on the backbone architecture.
- **Source**: Table 1

### L4: FID unreliable for very small datasets
- **Description**: FID is not evaluated on the 10-shot datasets themselves (too few samples for reliable FID); it uses separate larger reference datasets (Sunglasses 2,500 images, Babies 2,700 images). Other target domains (Raphael, Haunted Houses, etc.) are evaluated only with Intra-LPIPS.
- **Source**: §5.2
