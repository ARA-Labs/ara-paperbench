---
# Training Configuration

## Learning Rate (DDPM)
- **Value**: 5 × 10^-5
- **Rationale**: Small learning rate for fine-tuning adaptor module from near-zero initialization; prevents overshooting with limited 10-shot data
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: §5.2 Configurations

## Learning Rate (LDM)
- **Value**: 1 × 10^-5
- **Rationale**: Even smaller learning rate for LDM, which operates in compressed latent space; prevents instability
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: §5.2 Configurations

## Number of Training Iterations
- **Value**: 300 (approximately)
- **Rationale**: Achieves minimum FID (18.13 on FFHQ→Sunglasses) before overfitting begins. FID stabilizes around 400 iterations. Much fewer than ~5,000 iterations needed by prior methods.
- **Search range**: Evaluated at multiple values; see Table 6 in evidence
- **Sensitivity**: medium
- **Source**: §5.2 Configurations; Appendix A.2 Table 6

## Batch Size
- **Value**: 40
- **Rationale**: Large batch size used to fully exploit the 10-shot training data by repeating samples; used across ×8 A100 GPUs
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.2 Configurations

## Similarity Guidance Scale (γ)
- **Value**: 5
- **Rationale**: Optimal trade-off between image quality (FID) and diversity (Intra-LPIPS) for FFHQ→Sunglasses. At γ=5, FID=18.13 (minimum). Higher γ causes overfitting (images too similar to target or degrade to noise).
- **Search range**: Multiple values evaluated; see Table 4 in evidence
- **Sensitivity**: high
- **Source**: §5.2 Configurations; Appendix A.2 Table 4

## Adversarial Noise PGD Steps (J)
- **Value**: 10
- **Rationale**: Practical trade-off between approximation quality of worst-case noise and computational cost; used for "most transfer learning tasks"
- **Search range**: Not specified in paper (no ablation over J)
- **Sensitivity**: medium
- **Source**: §5.2 Configurations

## Adversarial Noise PGD Step Size (ω)
- **Value**: 0.02
- **Rationale**: Optimal FID (18.13) on FFHQ→Sunglasses. Results relatively stable in range [0.01, 0.03]. Larger ω causes overfitting.
- **Search range**: [0.01, 0.05] evaluated; see Table 5 in evidence
- **Sensitivity**: medium
- **Source**: §5.2 Configurations; Appendix A.2 Table 5

## Number of GPUs
- **Value**: 8 × NVIDIA A100
- **Rationale**: Used to achieve batch size 40 with efficient training; baseline comparison uses 1 GPU with batch size 5
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §5.2 Configurations

## Target Dataset Size (Few-Shot)
- **Value**: 10 images
- **Rationale**: Few-shot setting matching DDPM-PA experimental protocol
- **Search range**: N/A
- **Sensitivity**: high (core setting of the work)
- **Source**: §5.1, §5.2

## Intra-LPIPS Evaluation Images
- **Value**: 1,000 generated images
- **Rationale**: Sufficient for stable Intra-LPIPS estimation per CDC [19] protocol
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §5.2 Measurements

## FID Evaluation Images
- **Value**: 10,000 generated images (implied from Appendix A.2)
- **Rationale**: Standard FID computation requires large sample count for stable estimates
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: Appendix A.2 ("we generate 10000 images for the FID")
