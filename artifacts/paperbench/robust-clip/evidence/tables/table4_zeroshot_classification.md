# Table 4: Clean and Adversarial Evaluation on Image Classification Datasets
- **Source**: Table 4, Section 4.3
- **Caption**: "Clean and adversarial evaluation on image classification datasets of CLIP model. Models are trained on ImageNet, all other datasets are zero-shot."
- **Conditions**: Clean: all available samples. Adversarial: 1000 samples each. AutoAttack first two attacks (APGD-CE + APGD-DLR targeted, 100 iterations each). ℓ∞ at ε = 2/255 and ε = 4/255. Evaluated at 224×224 except CIFAR10, CIFAR100, STL-10 at native resolution. Average computed over zero-shot datasets (excludes ImageNet).

## Zero-shot Clean Accuracy (%)

| Eval | Vision encoder | ImageNet | CalTech | Cars | CIFAR10 | CIFAR100 | DTD | EuroSAT | FGVC | Flowers | ImageNet-R | ImageNet-S | PCAM | OxfordPets | STL-10 | Average |
|------|----------------|----------|---------|------|---------|---------|-----|---------|------|---------|-----------|-----------|------|-----------|--------|---------|
| clean | CLIP | 74.9 | 83.3 | 77.9 | 95.2 | 71.1 | 55.2 | 62.6 | 31.8 | 79.2 | 87.9 | 59.6 | 52.0 | 93.2 | 99.3 | 73.1 |
| clean | TeCoA2-CLIP | 80.2 | 80.7 | 50.1 | 87.5 | 60.7 | 44.4 | 26.1 | 14.0 | 51.8 | 80.1 | 58.4 | 49.9 | 80.0 | 96.1 | 60.0 |
| clean | FARE2-CLIP | 74.2 | 84.8 | 70.5 | 89.5 | 69.1 | 50.0 | 25.4 | 26.7 | 70.6 | 85.5 | 59.7 | 50.0 | 91.1 | 98.5 | 67.0 ↑7.0 |
| clean | TeCoA4-CLIP | 75.2 | 78.4 | 37.9 | 79.6 | 50.3 | 38.0 | 22.5 | 11.8 | 38.4 | 74.3 | 54.2 | 50.0 | 76.1 | 93.4 | 54.2 |
| clean | FARE4-CLIP | 70.4 | 84.7 | 63.8 | 77.7 | 56.5 | 43.8 | 18.3 | 22.0 | 58.1 | 80.2 | 56.7 | 50.0 | 87.1 | 96.0 | 61.1 ↑6.9 |

## Adversarial Accuracy at ℓ∞ = 2/255 (%)

| Eval | Vision encoder | ImageNet | CalTech | Cars | CIFAR10 | CIFAR100 | DTD | EuroSAT | FGVC | Flowers | ImageNet-R | ImageNet-S | PCAM | OxfordPets | STL-10 | Average |
|------|----------------|----------|---------|------|---------|---------|-----|---------|------|---------|-----------|-----------|------|-----------|--------|---------|
| ℓ∞=2/255 | CLIP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 |
| ℓ∞=2/255 | TeCoA2-CLIP | 62.3 | 70.2 | 22.2 | 63.7 | 35.0 | 27.0 | 12.8 | 5.8 | 27.6 | 58.8 | 45.2 | 40.0 | 69.7 | 88.7 | 43.6 |
| ℓ∞=2/255 | FARE2-CLIP | 46.1 | 73.0 | 26.0 | 60.3 | 35.6 | 26.7 | 6.2 | 5.9 | 31.2 | 56.5 | 38.3 | 41.9 | 68.3 | 90.1 | 43.1 ↓0.5 |
| ℓ∞=2/255 | TeCoA4-CLIP | 60.6 | 69.7 | 17.9 | 59.7 | 33.7 | 26.5 | 8.0 | 5.0 | 24.1 | 59.2 | 43.0 | 48.8 | 68.0 | 86.7 | 42.3 |
| ℓ∞=2/255 | FARE4-CLIP | 52.4 | 76.7 | 30.0 | 57.3 | 36.5 | 28.3 | 12.8 | 8.2 | 31.3 | 61.6 | 41.6 | 50.2 | 72.4 | 89.6 | 45.9 ↑3.6 |

## Adversarial Accuracy at ℓ∞ = 4/255 (%)

| Eval | Vision encoder | ImageNet | CalTech | Cars | CIFAR10 | CIFAR100 | DTD | EuroSAT | FGVC | Flowers | ImageNet-R | ImageNet-S | PCAM | OxfordPets | STL-10 | Average |
|------|----------------|----------|---------|------|---------|---------|-----|---------|------|---------|-----------|-----------|------|-----------|--------|---------|
| ℓ∞=4/255 | CLIP | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| ℓ∞=4/255 | TeCoA2-CLIP | 37.3 | 57.4 | 6.5 | 31.0 | 17.8 | 14.7 | 7.7 | 1.1 | 9.8 | 36.7 | 32.8 | 16.0 | 50.3 | 69.2 | 27.0 |
| ℓ∞=4/255 | FARE2-CLIP | 16.6 | 46.6 | 4.8 | 25.9 | 13.9 | 11.7 | 0.5 | 0.6 | 7.1 | 25.6 | 22.5 | 17.2 | 27.9 | 61.7 | 20.5 ↓6.5 |
| ℓ∞=4/255 | TeCoA4-CLIP | 44.3 | 60.9 | 8.4 | 37.1 | 21.5 | 16.4 | 6.6 | 2.1 | 12.4 | 41.9 | 34.2 | 44.0 | 55.2 | 74.3 | 31.9 |
| ℓ∞=4/255 | FARE4-CLIP | 33.3 | 64.1 | 12.7 | 34.6 | 20.2 | 17.3 | 11.1 | 2.6 | 12.5 | 40.6 | 30.9 | 50.2 | 50.7 | 74.4 | 32.4 ↑0.5 |
