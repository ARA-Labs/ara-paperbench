# Boundary Conditions and Limitations

## Hard Constraints (System Fails Without These)

### BC1: Pre-trained label space must dominate target label space
- **Condition**: |Y^T| ≤ |Y^P|
- **Reason**: Output label mapping is injective from Y^P_sub (|Y^P_sub| = |Y^T|) to Y^T; cannot map more target classes than source classes exist.
- **Impact**: SMM cannot be applied to target tasks with more classes than the pre-trained model.

### BC2: Input domain must support bilinear upsampling to pre-trained input size
- **Condition**: Target images must be upsamplable to the pre-trained model's input size (224×224 for ResNet, 384×384 for ViT)
- **Reason**: r(xi) must match the expected input shape of fP
- **Impact**: Downsampling (target images larger than pre-trained input) is not the focus of this paper.

### BC3: Mask generator output size must match pattern size (or patch-wise interpolation applied)
- **Condition**: If l > 0 (any Max-Pool layers), patch-wise interpolation must be applied to align mask size with dP
- **Reason**: Element-wise product δ ⊙ fmask(r(xi)|ϕ) requires both tensors to have shape dP
- **Impact**: Setting l=0 removes the interpolation requirement but also removes spatial abstraction.

## Soft Constraints (Degraded Performance Without These)

### SC1: Target task must not require fine-grained appearance discrimination
- **Condition**: VR methods (including SMM) fail when classification requires detecting subtle appearance differences at the object part level
- **Evidence**: StanfordCars (196 classes) achieves <10% accuracy for all VR methods including SMM
- **Impact**: SMM provides no benefit over baselines when the VR paradigm fundamentally fails.

### SC2: Patch size should be 8 (l=3 MaxPool layers) for the default configuration
- **Condition**: Patch size 2^l where l=3 provides the best balance between over-fitting (small patches, l=0,1) and information loss (large patches, l=4)
- **Evidence**: Figure 4 showing accuracy vs patch size across EuroSAT, Flowers102, CIFAR100, SVHN
- **Impact**: Using l=0 risks overfitting; l=4 causes accuracy plateau or decline.

### SC3: The mask generator should remain lightweight (< few ×10^4 parameters)
- **Condition**: Enlarging fmask increases estimation error; at ~1M parameters (same order as pre-trained model), overfitting becomes noticeable
- **Evidence**: Table 11 (EuroSAT/ResNet-18): test accuracy does not improve beyond ~92-93% even as training accuracy rises to 98%
- **Impact**: The theoretical advantage of lower approximation error may be offset by higher estimation error for large fmask.

### SC4: DTD (texture dataset) with ResNet-18 is an exception
- **Condition**: For texture classification tasks with relatively simple pre-trained models, watermark-style noise adversely affects texture features
- **Evidence**: Padding-based method achieves 35.3% vs SMM 33.6% for ResNet-18/DTD
- **Impact**: Resizing-based methods (including SMM) add noise over the entire image, interfering with texture patterns. Padding preserves original pixels.

### SC5: ViT/EuroSAT is an exception
- **Condition**: When target task is very simple (EuroSAT has limited task complexity) and pre-trained model is powerful (ViT), resizing-based methods overfit
- **Evidence**: ViT-B32/EuroSAT: Pad=95.9% vs SMM=93.5%
- **Impact**: Padding-based method preserves the overfit-resistant structure for simple satellite imagery tasks with ViT.

## Known Limitations

### L1: UCF101 with ViT requires dataset-specific learning rate
- The default unified LR=0.001 with γ=1 is suboptimal for ViT/UCF101; using LR=0.01 with γ=0.1 achieves 49.9% vs 42.6%
- Using unified hyperparameters for fairness sacrifices some performance on this dataset.

### L2: SMM does not improve VR when VR itself is fundamentally ineffective
- Adding SMM on top of a failing VR paradigm (StanfordCars) does not recover performance. SMM amplifies existing VR capacity; it cannot create capacity where none exists.

### L3: Orthogonality with finetuning is beneficial but untested at scale
- Combining SMM with LoRA or full FC-layer finetuning shows gains (Table 14), but optimal joint training strategies are not explored in depth.
