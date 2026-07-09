# Table 11: Training and Testing Accuracy with Enlarged fmask
- **Source**: Table 11, Appendix D.3
- **Caption**: "Training and Testing Accuracy with Enlarged fmask (using EuroSAT, ResNet-18)"
- **Experimental conditions**: EuroSAT dataset; ResNet-18 as pretrained backbone; architecture of fmask kept the same (5-layer structure) but number of intermediate channels doubled progressively; default "MEDIUM" = 26,499 parameters (the one used in all main experiments)

| fmask SIZE | PARAMETERS | TRAINING ACCURACY (%) | TESTING ACCURACY (%) |
|-----------|------------|----------------------|---------------------|
| SMALL | 7,203 | 94.9 | 91.7 |
| MEDIUM (OURS) | 26,499 | 96.2 | 92.2 |
| LARGE | 101,379 | 96.4 | 92.2 |
| X-LARGE | 396,291 | 97.3 | 93.1 |
| XX-LARGE | 1,566,723 | 97.7 | 93.5 |
| XXX-LARGE | 6,230,019 | 98.1 | 93.2 |
