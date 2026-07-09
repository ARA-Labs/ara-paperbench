---
# Problem Specification

## Observations

### O1: DPMs require large-scale data and cannot easily leverage GAN-based transfer
- **Statement**: Modern DPMs heavily rely on extensive amounts of data to train large-scale network parameters; gathering sufficient data is not always feasible in certain situations.
- **Evidence**: Empirical observation from the field; cited in [3] (survey on generative diffusion models)
- **Implication**: Transfer learning from a large source domain to a small target domain is necessary for DPMs in low-data regimes.

### O2: DPMs cannot produce clean images during training — only noisy intermediate predictions
- **Statement**: GANs can directly compare generated clean images with target images during training; DPMs can only produce a blurry predicted final image at intermediate timestep t, not a high-quality final image.
- **Evidence**: DDPM-PA [34] uses predicted blurry final image at intermediate timestep as surrogate for clean image; described in §1 and §2
- **Implication**: Existing GAN-based transfer loss functions that compare clean generated images with target images (CDC, DCL) cannot be applied directly to DPMs.

### O3: Non-targeted Gaussian noise causes unbalanced per-sample transfer rates
- **Statement**: The diffusion/denoising process uses fully random Gaussian noise independent of the input image; this imposes unbalanced effects on different images during transfer, causing divergent training iteration requirements.
- **Evidence**: Figure 1 — at the same training iteration (e.g., 1000), one image (below) successfully transfers to Sunglasses domain while the other (above) has severely overfit; LPIPS values range from 0.394–0.589 within the same training run.
- **Implication**: A fixed number of training iterations cannot simultaneously avoid overfitting one image while successfully transferring another; targeted noise selection is required.

### O4: DDPM-PA produces fuzzy and distorted images due to blurry image comparison
- **Statement**: DDPM-PA substitutes the high-quality real final image with the predicted blurry final image at intermediate timestep, leading to inaccurate domain transfer direction estimation.
- **Evidence**: Qualitative comparison in Figure 3 (top and bottom rows) shows DDPM-PA images are fuzzy; DDPM-PA FID on Sunglasses = 34.75 vs. TAN = 20.06 (Table 2).
- **Implication**: A fundamentally different approach to domain gap estimation is needed — one that does not rely on comparing with blurry intermediate predictions.

## Gaps

### G1: No direct clean-image comparison available for diffusion model transfer
- **Statement**: GAN-based transfer methods rely on comparing generated clean images with target images (e.g., CDC cross-domain consistency loss, DCL contrastive loss), which is incompatible with the DPM training process.
- **Caused by**: O2 — DPMs only yield intermediate noisy predictions during training
- **Existing attempts**: DDPM-PA [34] uses predicted blurry intermediate image as proxy for clean target
- **Why they fail**: Blurry predicted image does not accurately represent the target domain distribution; comparing blurry predictions with sharp target images introduces inaccurate gradient direction, producing fuzzy/distorted outputs (O4)

### G2: Random Gaussian noise is inefficient and causes unbalanced transfer
- **Statement**: Standard DPM training samples noise uniformly from N(0,I), which is agnostic to the current model's capability and the input image, requiring extensive iterations with limited data.
- **Caused by**: O3 — non-targeted noise causes divergent per-sample transfer pace
- **Existing attempts**: Prior GAN-based and DDPM-based methods use standard Gaussian noise without adaptation
- **Why they fail**: Random noise may require thousands of iterations to cover all "hard" noise types for the current model state; with only 10 training samples, this leads to overfitting before all generated images are successfully transferred (Figure 1)

## Key Insight

- **Insight**: The domain gap between source and target can be measured entirely through the divergence of classifier gradient signals on noised images xt — without ever needing to compare clean generated images. Furthermore, the "worst-case" Gaussian noise (the noise the current model most fails to denoise on the target domain) can be found via PGD gradient ascent, and minimizing this worst-case noise implicitly minimizes all easier noise variants, dramatically accelerating transfer.
- **Derived from**: O2, O3 — avoiding clean image comparison; targeting only model-failing noise
- **Enables**: (1) Similarity-guided training using a binary classifier pϕ(y=T|xt) on noised images as domain divergence proxy; (2) Adversarial noise selection via min-max PGD to find and minimize worst-case noise

## Assumptions

- A1: A binary classifier can be trained on only 10 target-domain images (via ImageNet pre-trained model fine-tuning) to provide useful gradient signal for domain gap estimation.
- A2: The pre-trained source DPM has strong denoising capability for source-domain images; only a small parameter shift (adaptor) is needed for target-domain adaptation.
- A3: Minimizing the loss under worst-case noise (inner max) subsumes minimizing loss under all "easier" noise variants — i.e., worst-case noise convergence implies convergence on typical noise.
- A4: The similarity-guidance term ∇xt log pϕ(y=S|xt) is negligible during fine-tuning because xt pertains to target images, making pϕ(y=S|xT_t) near zero with large chaotic gradient.
