# Table 6: Number of Added Parameters at Model Deployment (Millions)
- **Source**: Table 6, Appendix C.2
- **Caption**: "Number of added parameters used in model deployment, measured in Millions. L2P uses a fixed size of prompts. DualPrompt and CODA-P incrementally add parameters (i.e., prompts) sequentially by task. SEMA adds a small number of parameters with its dynamic expansion strategy."
- **Experimental conditions**: ViT-B/16-IN1K; deployment-time parameters only (RDs not counted for SEMA). A_N values from Table 1.

| Type | Method | CIFAR-100 Params (M) | CIFAR-100 A_N | ImageNet-R Params (M) | ImageNet-R A_N | ImageNet-A Params (M) | ImageNet-A A_N | VTAB Params (M) | VTAB A_N |
|------|--------|---------------------|---------------|----------------------|----------------|----------------------|----------------|----------------|---------|
| Fixed Param Size | L2P | 0.123 | 77.87 | 0.200 | 62.90 | 0.200 | 38.48 | 0.085 | 80.83 |
| Expandable Param Size | DualPrompt | 1.022 | 80.43 | 1.098 | 61.97 | 1.098 | 50.23 | 0.983 | 79.79 |
| Expandable Param Size | CODA-P | 3.917 | 86.11 | 3.994 | 70.02 | 3.994 | 35.02 | 3.878 | 81.58 |
| Expandable Param Size | SEMA | 0.645 | 86.98 | 0.617 | 74.53 | 0.560 | 53.32 | 0.554 | 89.64 |
