# Table 6: Soft Labeling with Latent Hierarchies for Linear Probing on ResNet-18
- **Source**: Table 6, Section 4.3.2
- **Caption**: "Soft Labeling with Latent Hierarchies for Linear Probing on ResNet-18. Instead of using WordNet to construct soft labels in Table 5, we adopted latent hierarchies constructed from pre-trained models using K-means clustering. Results show that using latent hierarchies also delivers a generalization boost compared to the baseline, although it is less significant than using WordNet. Experiments are listed here with the pro-OOD setting in Table 9."
- **Conditions**: ResNet-18 backbone; latent hierarchies from K-means on 4 source models + WordNet; lambda=0.03, temperature=25, CE mode; Interp = weight interpolation; values are Top-1 accuracy (%)

| Hierarchy Sources | ImgNet-S Baseline | ImgNet-S Interp | ImgNet-R Baseline | ImgNet-R Interp | ImgNet-A Baseline | ImgNet-A Interp | ObjectNet Baseline | ObjectNet Interp |
|-------------------|------------------|----------------|------------------|----------------|------------------|----------------|-------------------|----------------|
| MnasNet | 19.7 | 20.2 (+0.5) | 31.9 | 32.4 (+0.5) | 1.1 | 1.7 (+0.6) | 27.0 | 28.1 (+1.1) |
| ResNet 18 | 19.7 | 20.2 (+0.5) | 31.9 | 32.4 (+0.5) | 1.1 | 1.8 (+0.7) | 27.0 | 28.2 (+1.2) |
| vit-l-14 | 19.7 | 20.8 (+1.2) | 31.9 | 33.2 (+1.3) | 1.1 | 2.0 (+0.9) | 27.0 | 28.3 (+1.3) |
| OpenCLIP(vit-l-14) | 19.7 | 20.9 (+1.3) | 31.9 | 33.7 (+1.8) | 1.1 | 2.1 (+1.0) | 27.0 | 28.5 (+1.5) |
| WordNet | 19.7 | 21.2 (+1.5) | 31.9 | 35.1 (+3.2) | 1.1 | 1.4 (+0.4) | 27.0 | 28.6 (+1.6) |
