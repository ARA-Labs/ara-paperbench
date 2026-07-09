---
# Claims

## C01: TAN achieves superior or competitive image generation diversity (Intra-LPIPS) compared to all baselines
- **Statement**: DDPM-TAN and LDM-TAN achieve higher Intra-LPIPS scores than all GAN-based and DDPM-based baselines on the majority of 10-shot adaptation tasks from FFHQ and LSUN Church source domains.
- **Status**: supported
- **Falsification criteria**: Any of TGAN, TGAN+ADA, EWC, CDC, DCL, or DDPM-PA achieve equal or higher Intra-LPIPS than both DDPM-TAN and LDM-TAN on the majority of the 5 tested adaptation tasks.
- **Proof**: [E01, E02]
- **Dependencies**: none
- **Tags**: diversity, Intra-LPIPS, few-shot, image generation, transfer learning

## C02: TAN achieves significantly better image quality (FID) than all baselines on FFHQ→Sunglasses and FFHQ→Babies
- **Statement**: DDPM-TAN/LDM-TAN achieve lower FID scores than TGAN, TGAN+ADA, EWC, CDC, DCL, and DDPM-PA on FFHQ→10-shot Sunglasses and FFHQ→10-shot Babies.
- **Status**: supported
- **Falsification criteria**: Any baseline achieves FID ≤ TAN on either Sunglasses or Babies.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: FID, image quality, few-shot, FFHQ, Sunglasses, Babies

## C03: TAN is parameter-efficient and computationally efficient compared to full fine-tuning and prior methods
- **Statement**: DDPM-TAN fine-tunes only 1.3% of parameters and converges in ~300 iterations (3 GPU hours, 9 GB memory), versus ~5000 iterations (7.5 GPU hours, 20 GB memory) for full fine-tuning baselines with 100% parameter rate.
- **Status**: supported
- **Falsification criteria**: TAN requires comparable GPU memory (≥15 GB) or comparable wall-clock time (≥6 GPU hours) to achieve equivalent or better quality as full fine-tuning baseline.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: efficiency, parameter rate, GPU memory, iterations, adaptor

## C04: Adversarial noise selection corrects the noisy gradient direction in few-shot settings, improving transfer speed and coverage
- **Statement**: On 2D toy data, the gradient direction of DDPM-TAN (with adversarial noise selection) is closer to the reference gradient (computed with 10,000 samples) than the baseline DDPM or similarity-guided training alone; and DDPM-TAN generates samples with higher concentration near the target distribution mode.
- **Status**: supported
- **Falsification criteria**: The angular deviation of DDPM-TAN gradient from the reference is not smaller than that of vanilla DDPM or similarity-guided-only variant in the toy experiment.
- **Proof**: [E04]
- **Dependencies**: none
- **Tags**: adversarial noise, gradient direction, toy experiment, convergence, worst-case noise

## C05: Each component of TAN (similarity guidance, adversarial noise) contributes incrementally to final FID improvement
- **Statement**: On FFHQ→10-shot Sunglasses at 300 iterations: Baseline FID 38.65 → Adaptor only FID 41.88 → DPMs-TAN w/o adversarial noise FID 26.41 → DPMs-TAN full FID 20.06, showing that similarity-guided training and adversarial noise selection each provide independent improvement.
- **Status**: supported
- **Falsification criteria**: DPMs-TAN w/o adversarial noise does not improve over the adaptor-only baseline, or DPMs-TAN full does not improve over DPMs-TAN w/o adversarial noise.
- **Proof**: [E05]
- **Dependencies**: C02
- **Tags**: ablation, similarity-guided training, adversarial noise, FID, component analysis
