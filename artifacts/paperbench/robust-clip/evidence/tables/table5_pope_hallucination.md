# Table 5: Hallucination Evaluation Using POPE (F1-score)
- **Source**: Table 5, Section 4.4
- **Caption**: "Supervised fine-tuning via TeCoA causes LLaVA to hallucinate much more than unsupervised fine-tuning with FARE."
- **Conditions**: LLaVA-1.5 7B; POPE benchmark (Li et al., 2023b); COCO validation set; three evaluation splits: adversarial, popular, random; F1-score metric; clean images (no adversarial perturbations).

| Visual Encoder | POPE Adversarial | POPE Popular | POPE Random | Mean |
|----------------|-----------------|-------------|------------|------|
| CLIP | 82.6 | 85.1 | 85.9 | 84.5 |
| TeCoA2-CLIP | 74.0 | 76.5 | 77.3 | 75.9 |
| FARE2-CLIP | 78.6 | 81.5 | 82.2 | 80.8 |
| TeCoA4-CLIP | 70.2 | 73.0 | 73.3 | 72.2 |
| FARE4-CLIP | 74.0 | 77.0 | 77.8 | 76.3 |
