# Table 12: SMM on StanfordCars (VR Failure Case)
- **Source**: Table 12, Appendix D.4
- **Caption**: "An Ineffective Case of Input Reprogramming - StanfordCars (Mean % ± Std %)"
- **Experimental conditions**: StanfordCars dataset (196 fine-grained car categories); ResNet-18, ResNet-50, ViT-B32 pretrained on ImageNet-1K; same training setup as main experiments

| METHOD | PAD | NARROW | MEDIUM | FULL | OURS |
|--------|-----|--------|--------|------|------|
| RESNET-18 | 4.5 ±0.1 | 3.6 ±0.1 | 3.6 ±0.1 | 3.4 ±0.1 | 2.9 ±0.2 |
| RESNET-50 | 4.7 ±0.2 | 4.7 ±0.1 | 4.7 ±0.2 | 4.6 ±0.1 | 3.0 ±0.6 |
| VIT-B32 | 4.7 ±0.6 | 7.7 ±0.2 | 8.3 ±0.3 | 5.0 ±0.0 | 4.8 ±0.9 |

**Note**: All VR methods fail on StanfordCars (196 classes); accuracy is below 10% for all methods, close to random chance (1/196 ≈ 0.5%). Adding SMM does not improve performance when VR itself is ineffective for fine-grained recognition.
