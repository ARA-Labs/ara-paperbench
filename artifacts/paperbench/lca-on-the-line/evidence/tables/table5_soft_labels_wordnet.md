# Table 5: Soft Labeling with WordNet for Linear Probing
- **Source**: Table 5, Section 4.3.2
- **Caption**: "Soft labeling with WordNet for Linear Probing. Baseline: Trained with Cross Entropy only; Ours: Trained with Cross Entropy + LCA soft loss + weight linear interpolation of (CE, CE + soft loss) (Wortsman et al., 2022). Results show that integrating soft loss consistently improves model OOD performance, without compromising ID accuracy. Note that in Table 9 of ablation study in pro-OOD setting, we demonstrate that it's possible to further enhance OOD performance at the cost of a slight ID accuracy drop."
- **Conditions**: Linear probing with frozen backbone; lambda=0.03, temperature=25, CE mode; alpha selected to maximize ID val Top-1; WordNet hierarchy used for soft labels (D^P_LCA); Single NVIDIA GeForce GTX 1080 Ti

| Backbone Models | ImgNet Baseline | ImgNet Ours | ImgNet-V2 Baseline | ImgNet-V2 Ours | ImgNet-S Baseline | ImgNet-S Ours | ImgNet-R Baseline | ImgNet-R Ours | ImgNet-A Baseline | ImgNet-A Ours | ObjectNet Baseline | ObjectNet Ours |
|-----------------|----------------|------------|-------------------|---------------|------------------|--------------|------------------|--------------|------------------|--------------|-------------------|---------------|
| ResNet 18 | 69.4 | 69.4 (+0.0) | 56.4 | 56.9 (+0.5) | 19.7 | 20.7 (+1.0) | 31.9 | 33.8 (+1.8) | 1.1 | 1.2 (+0.1) | 27.0 | 28.0 (+1.0) |
| ResNet 50 | 79.5 | 79.8 (+0.3) | 67.9 | 68.6 (+0.7) | 25.5 | 27.7 (+2.2) | 36.5 | 42.5 (+6.0) | 10.3 | 16.2 (+5.9) | 43.2 | 45.5 (+2.3) |
| VIT-B | 75.8 | 75.9 (+0.1) | 62.9 | 62.8 (-0.1) | 27.0 | 27.6 (+0.6) | 40.5 | 41.5 (+1.0) | 8.0 | 8.6 (+0.6) | 27.6 | 28.1 (+0.5) |
| VIT-L | 76.8 | 76.8 (+0.0) | 63.9 | 63.8 (-0.1) | 28.4 | 29.2 (+0.8) | 42.2 | 43.6 (+1.4) | 10.6 | 11.5 (+0.9) | 28.7 | 29.0 (+0.3) |
| ConvNext | 82.0 | 82.1 (+0.1) | 70.6 | 71.0 (+0.4) | 28.7 | 30.0 (+1.3) | 42.4 | 44.3 (+1.9) | 21.8 | 25.3 (+3.5) | 44.4 | 45.5 (+1.1) |
| Swin Transformer | 83.1 | 83.2 (+0.1) | 72.0 | 71.9 (-0.1) | 30.3 | 31.4 (+1.1) | 43.5 | 45.3 (+1.8) | 29.5 | 32.7 (+3.2) | 48.3 | 49.5 (+1.2) |
