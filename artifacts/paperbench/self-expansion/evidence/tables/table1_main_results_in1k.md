# Table 1: Comparison with ViT-based CL Methods in CIL (ViT-B/16-IN1K)
- **Source**: Table 1, Section 4.2
- **Caption**: "Comparison with ViT-based CL methods in CIL. All models adopt ViT-B/16-IN1K as the backbone."
- **Note**: Each cell contains two numbers: A_N (left, average accuracy after final task) / Ā (right, average incremental accuracy). Column headers: each dataset with two metrics.
- **Experimental conditions**: Class-incremental learning, no memory rehearsal, ViT-B/16 pre-trained on ImageNet-1K, same data shuffling as ADAM paper. Each task = 10 classes (except ImageNet-R splits).

| Method | CIFAR-100 A_N | CIFAR-100 Ā | 5-Task IN-R A_N | 5-Task IN-R Ā | 10-Task IN-R A_N | 10-Task IN-R Ā | 20-Task IN-R A_N | 20-Task IN-R Ā | ImageNet-A A_N | ImageNet-A Ā | VTAB A_N | VTAB Ā |
|--------|--------------|-------------|-----------------|---------------|------------------|----------------|------------------|----------------|----------------|-------------|---------|--------|
| FT Adapter | 47.88 | 30.9 | 53.91 | 41.23 | 45.31 | 30.93 | 38.51 | 24.22 | 29.78 | 17.64 | 59.98 | 43.50 |
| L2P | 84.77 | 77.87 | 77.40 | 73.59 | 66.97 | 62.72 | 70.67 | 62.90 | 47.16 | 38.48 | 81.19 | 80.83 |
| DualPrompt | 86.60 | 80.43 | 76.39 | 72.29 | 72.83 | 66.75 | 62.33 | 61.97 | 59.54 | 50.23 | 82.89 | 79.79 |
| CODA-P | 91.55 | 86.11 | 81.63 | 76.98 | 81.11 | 75.25 | 75.00 | 70.02 | 47.29 | 35.02 | 79.88 | 81.58 |
| SimpleCIL | 82.31 | 76.21 | 65.83 | 61.31 | 67.09 | 61.35 | 67.59 | 61.35 | 60.05 | 49.24 | 85.29 | 83.61 |
| ADAM | 90.55 | 85.62 | 79.91 | 74.25 | 79.11 | 73.15 | 75.84 | 69.10 | 60.15 | 49.24 | 85.29 | 83.61 |
| InfLoRA | 90.51 | 85.05 | 78.58 | 72.58 | 81.39 | 75.32 | 78.87 | 72.60 | 59.71 | 46.21 | 88.90 | 87.63 |
| SEMA | 91.37 | 86.98 | 84.75 | 79.78 | 83.56 | 78.00 | 81.75 | 74.53 | 64.53 | 53.32 | 91.26 | 89.64 |
