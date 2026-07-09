---
# Table 14: Accuracy on OOD Dataset by Enforcing Class Taxonomy (CLIP-ViT32)
- **Source**: Table 14, Section 4.3.3 (Appendix F)
- **Caption**: "Accuracy on OOD dataset by enforcing class taxonomy: Baseline: <dalmatian>; Stack Parent: <dalmatian, dog, animal>; Taxonomy Parent:<dalmatian, which is type of a dog, which is type of an animal>; Shuffle Parent: <dalmatian, which is type of an organism, which is type of a seabird>; The Taxonomy Parent method, which includes the full hierarchical relationship, yields the best performance."
- **Conditions**: Model = CLIP-ViT32; Baseline = class name only; Test CE = test-time Cross-Entropy

| Model | ImgN Top1 | ImgN Test CE | ImgN-v2 Top1 | ImgN-v2 Test CE | ImgN-S Top1 | ImgN-S Test CE | ImgN-R Top1 | ImgN-R Test CE | ImgN-A Top1 | ImgN-A Test CE | ObjNet Top1 | ObjNet Test CE |
|-------|----------|------------|-------------|----------------|-----------|--------------|-----------|--------------|-----------|--------------|-----------|--------------|
| Baseline | 0.589 | 9.322 | 0.517 | 9.384 | 0.379 | 9.378 | 0.667 | 8.790 | 0.294 | 9.358 | 0.394 | 8.576 |
| Stack Parent | 0.381 | 9.389 | 0.347 | 9.395 | 0.219 | 9.561 | 0.438 | 9.258 | 0.223 | 9.364 | 0.148 | 9.076 |
| Shuffle Parent | 0.483 | 9.679 | 0.432 | 9.696 | 0.329 | 9.718 | 0.557 | 9.281 | 0.236 | 9.586 | 0.329 | 8.785 |
| Taxonomy Parent | 0.626 | 9.102 | 0.553 | 9.165 | 0.419 | 9.319 | 0.685 | 8.658 | 0.319 | 9.171 | 0.431 | 8.515 |
