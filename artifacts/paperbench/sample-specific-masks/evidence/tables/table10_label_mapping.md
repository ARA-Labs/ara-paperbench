# Table 10: Performance Improvement with Different Label Mapping Methods
- **Source**: Table 10, Appendix D.1
- **Caption**: "Performance Improvement When Applying Our Input Reprogramming on Different Label Mapping Methods (the average results are highlighted in grey)"
- **Experimental conditions**: ResNet-18 pretrained on ImageNet-1K; three output mapping methods: Iterative (Ilm), Frequent (Flm), Random (Rlm); W/O OURS = Full watermarking baseline; W OURS = SMM; IMPROVE = absolute accuracy difference

| DATASET | Ilm W/O OURS | Ilm W OURS | Ilm IMPROVE | Flm W/O OURS | Flm W OURS | Flm IMPROVE | Rlm W/O OURS | Rlm W OURS | Rlm IMPROVE |
|---------|--------------|------------|-------------|--------------|------------|-------------|--------------|------------|-------------|
| CIFAR10 | 68.90% | 72.80% | +3.90% | 71.79% | 72.75% | +0.96% | 65.68% | 69.71% | +4.03% |
| CIFAR100 | 33.80% | 39.40% | +5.60% | 29.79% | 32.35% | +2.56% | 16.99% | 23.47% | +6.48% |
| SVHN | 78.30% | 84.40% | +6.10% | 78.78% | 83.73% | +4.95% | 77.44% | 85.37% | +7.92% |
| GTSRB | 76.80% | 80.40% | +3.60% | 74.76% | 80.90% | +6.14% | 69.60% | 82.38% | +12.79% |
| FLOWERS102 | 23.20% | 38.70% | +15.50% | 17.78% | 32.16% | +14.37% | 12.34% | 37.68% | +25.33% |
| DTD | 29.00% | 33.60% | +4.60% | 30.14% | 34.28% | +4.14% | 14.60% | 19.74% | +5.14% |
| UCF101 | 24.40% | 28.70% | +4.30% | 22.71% | 25.72% | +3.01% | 9.04% | 16.71% | +7.67% |
| FOOD101 | 13.20% | 17.50% | +4.30% | 11.58% | 15.21% | +3.62% | 7.15% | 15.86% | +8.71% |
| SUN397 | 13.40% | 16.00% | +2.60% | 13.45% | 15.45% | +1.99% | 1.05% | 3.35% | +2.29% |
| EUROSAT | 84.30% | 92.20% | +7.90% | 86.00% | 92.67% | +6.67% | 84.49% | 94.47% | +9.98% |
| OXFORDPETS | 70.00% | 74.10% | +4.10% | 69.66% | 72.83% | +3.16% | 8.89% | 16.84% | +7.96% |
| **AVERAGE** | **46.85%** | **52.53%** | **+5.68%** | **46.04%** | **50.73%** | **+4.69%** | **33.39%** | **42.32%** | **+8.94%** |
