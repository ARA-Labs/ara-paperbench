# Table 2: Comparisons on ImageNet-C (Severity Level 5) — Accuracy (%)
- **Source**: Table 2, Section 4.1
- **Caption**: "Comparisons with SOTA methods on ImageNet-C (severity level 5) with ViT regarding Accuracy (%). BP is short for backward propagation and the bold number indicates the best result. We only report average ECE (%,↓) here and put detailed ECEs in Appendix D."
- **Model**: ViT-Base, full precision 32-bit
- **Batch size**: 64
- **Metric**: Classification Accuracy (%, ↑) per corruption and average; Average ECE (%, ↓)

| Method | BP | Gauss. | Shot | Impul. | Defoc. | Glass | Motion | Zoom | Snow | Frost | Fog | Brit. | Contr. | Elas. | Pix. | JPEG | Avg Acc. | Avg ECE |
|--------|-----|--------|------|--------|--------|-------|--------|------|------|-------|-----|-------|--------|-------|------|------|----------|---------|
| NoAdapt | ✗ | 56.8 | 56.8 | 57.5 | 46.9 | 35.6 | 53.1 | 44.8 | 62.2 | 62.5 | 65.7 | 77.7 | 32.6 | 46.0 | 67.0 | 67.6 | 55.5 | 10.5 |
| LAME | ✗ | 56.5 | 56.5 | 57.2 | 46.4 | 34.7 | 52.7 | 44.2 | 58.4 | 61.5 | 63.1 | 77.4 | 24.7 | 44.6 | 66.6 | 67.2 | 54.1 | 11.0 |
| T3A | ✗ | 56.4 | 56.9 | 57.3 | 47.9 | 37.8 | 54.3 | 46.9 | 63.6 | 60.8 | 68.5 | 78.1 | 38.3 | 50.0 | 67.6 | 69.1 | 56.9 | 26.8 |
| TENT | ✓ | 60.3 | 61.6 | 61.8 | 59.2 | 56.5 | 63.5 | 59.2 | 54.3 | 64.5 | 2.3 | 79.1 | 67.4 | 61.5 | 72.5 | 70.6 | 59.6 | 18.5 |
| CoTTA | ✓ | 63.6 | 63.8 | 64.1 | 55.5 | 51.1 | 63.6 | 55.5 | 70.0 | 69.4 | 71.5 | 78.5 | 9.7 | 64.5 | 73.4 | 71.2 | 61.7 | 6.5 |
| SAR | ✓ | 59.2 | 60.5 | 60.7 | 57.5 | 55.6 | 61.8 | 57.6 | 65.9 | 63.5 | 69.1 | 78.7 | 45.7 | 62.4 | 71.9 | 70.3 | 62.7 | 7.0 |
| FOA (ours) | ✗ | 61.5 | 63.2 | 63.3 | 59.3 | 56.7 | 61.4 | 57.7 | 69.4 | 69.6 | 73.4 | 81.1 | 67.7 | 62.7 | 73.9 | 73.0 | 66.3 | 3.2 |
