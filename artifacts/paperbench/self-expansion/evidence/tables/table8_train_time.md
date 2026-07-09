# Table 8: Average Per-Batch Training Time
- **Source**: Table 8, Appendix C.4
- **Caption**: "Average per-batch train time of each method on each task measured in seconds. SEMA (overall) denotes the training time used when adapter and representation descriptor (RD) are trained sequentially."
- **Hardware**: Single NVIDIA GeForce RTX 3090 GPU
- **Note**: ImageNet-R here is 20-task split (10 classes/task)

| Method | CIFAR-100 (s) | ImageNet-R (s) | ImageNet-A (s) | VTAB (s) |
|--------|--------------|---------------|---------------|---------|
| L2P | 0.27 | 0.27 | 0.29 | 0.28 |
| DualPrompt | 0.25 | 0.25 | 0.27 | 0.29 |
| CODA-P | 0.31 | 0.32 | 0.35 | 0.36 |
| SEMA (Overall) | 0.25 | 0.11 | 0.15 | 0.31 |
| SEMA - Adapter | 0.13 | 0.10 | 0.12 | 0.20 |
| SEMA - RD | 0.12 | 0.01 | 0.03 | 0.11 |
