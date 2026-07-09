# Table 13: Clean LLaVA-13B Evaluations of Vision-Language Tasks
- **Source**: Table 13, Appendix C.3
- **Caption**: "We report clean scores of LLaVA-13B with different vision encoders. All FARE model consistently outperform TeCoA, while FARE2 suffers a very small degradation in performance in comparison to the clean CLIP."
- **Conditions**: LLaVA-1.5 13B; clean images (no adversarial perturbations); CIDEr for COCO and Flickr30k; VQA accuracy for TextVQA and VQAv2.

| LLaVA model | COCO | Flickr30k | TextVQA | VQAv2 |
|-------------|------|-----------|---------|-------|
| CLIP | 119.1 | 77.4 | 39.1 | 75.5 |
| TeCoA2 | 99.4 | 58.3 | 25.6 | 67.9 |
| FARE2 | 111.9 | 71.4 | 33.8 | 72.6 |
| TeCoA4 | 88.2 | 48.6 | 22.0 | 64.1 |
| FARE4 | 101.4 | 62.0 | 29.0 | 69.1 |
