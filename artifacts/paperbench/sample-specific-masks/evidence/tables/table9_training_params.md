# Table 9: Detailed Model Training Parameter Settings
- **Source**: Table 9, Appendix C
- **Caption**: "Detailed Model Training Parameter Settings of Our Mask Generator (where b, α and γ denote batch size, initial learning rate and learning rate decay, respectively)"
- **Experimental conditions**: Settings for the SMM mask generator training; milestones = epoch numbers at which LR decay is applied

| DATASET | MILESTONES | 5-LAYER b | 5-LAYER α | 5-LAYER γ | 6-LAYER b | 6-LAYER α | 6-LAYER γ |
|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| CIFAR10 | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| CIFAR100 | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| SVHN | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| GTSRB | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| FLOWERS102 | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| DTD | [0, 100, 145] | 64 | 0.01 | 0.1 | 64 | 0.001 | 1 |
| UCF101 | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| FOOD101 | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| SUN397 | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| EUROSAT | [0, 100, 145] | 256 | 0.01 | 0.1 | 256 | 0.001 | 1 |
| OXFORDPETS | [0, 100, 145] | 64 | 0.01 | 0.1 | 64 | 0.001 | 1 |

**Notes**:
- 5-layer CNN used for ResNet-18 and ResNet-50 backends
- 6-layer CNN used for ViT-B32 backend
- Milestones list [0, 100, 145] means LR decay applied at epochs 100 and 145 (epoch 0 is initial; γ=1.0 means no decay when γ column shows 1)
- For ViT-B32 with UCF101, using specific params α=0.01, γ=0.1 achieves 49.9% vs 42.6% with defaults (Table 8)
