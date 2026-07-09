# Table 2: Main Results on Pre-trained ViT
- **Source**: Table 2, Section 5
- **Caption**: "Performance Comparison of Different Input Reprogramming Methods on Pre-trained ViT (Mean %, the average results are highlighted in grey)"
- **Experimental conditions**: ViT-B32 pretrained on ImageNet-1K; ILM output mapping; 200 epochs; initial LR 0.001; LR decay = 1 (no decay); batch size 256 (DTD/OxfordPets: 64); 3 seeds; single A100 GPU. Note: UCF101 result reported with unified LR=0.001, not dataset-specific LR.

| DATASET | PAD | NARROW | MEDIUM | FULL | OURS |
|---------|-----|--------|--------|------|------|
| CIFAR10 | 62.4 | 96.6 | 96.5 | 95.8 | 97.4 |
| CIFAR100 | 31.6 | 74.4 | 75.3 | 75.0 | 82.6 |
| SVHN | 80.2 | 85.0 | 87.4 | 87.8 | 89.7 |
| GTSRB | 62.3 | 57.8 | 68.6 | 75.5 | 80.5 |
| FLOWERS102 | 57.3 | 55.3 | 56.6 | 55.9 | 79.1 |
| DTD | 43.7 | 37.3 | 38.5 | 37.7 | 45.6 |
| UCF101 | 33.6 | 44.5 | 44.8 | 40.9 | 42.6 |
| FOOD101 | 37.4 | 47.3 | 48.6 | 49.4 | 64.8 |
| SUN397 | 21.8 | 29.0 | 29.4 | 28.8 | 36.7 |
| EUROSAT | 95.9 | 90.9 | 90.9 | 89.1 | 93.5 |
| OXFORDPETS | 57.6 | 82.5 | 81.0 | 75.3 | 83.8 |
| **AVERAGE** | **53.1** | **63.7** | **65.2** | **64.7** | **72.4** |
