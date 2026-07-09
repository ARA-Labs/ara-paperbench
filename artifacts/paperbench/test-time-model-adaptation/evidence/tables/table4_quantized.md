# Table 4: Effectiveness on Quantized ViT Models — Accuracy (%) and ECE (%)
- **Source**: Table 4, Section 4.2
- **Caption**: "Effectiveness of our FOA on Quantized ViT models. We report the corruption Accuracy (%) and average ECE (%, ↓) on ImageNet-C (severity level 5). The bold number indicates the best result and see Appendix D for the detailed ECEs of each corruption."
- **Model**: ViT-Base quantized to 8-bit and 6-bit via PTQ4ViT
- **Batch size**: 64

## 8-bit Quantized ViT — Accuracy (%)

| Model | Method | Gauss. | Shot | Impul. | Defoc. | Glass | Motion | Zoom | Snow | Frost | Fog | Brit. | Contr. | Elas. | Pix. | JPEG | Avg Acc. | Avg ECE |
|-------|--------|--------|------|--------|--------|-------|--------|------|------|-------|-----|-------|--------|-------|------|------|----------|---------|
| 8-bit | NoAdapt | 55.8 | 55.8 | 56.5 | 46.7 | 34.7 | 52.1 | 42.5 | 60.8 | 61.4 | 66.7 | 76.9 | 24.6 | 44.7 | 65.8 | 66.7 | 54.1 | 10.8 |
| 8-bit | T3A | 55.6 | 55.7 | 55.7 | 45.8 | 34.4 | 51.1 | 41.2 | 59.5 | 61.9 | 66.8 | 76.4 | 45.5 | 43.4 | 65.6 | 67.5 | 55.1 | 25.9 |
| 8-bit | FOA (ours) | 60.7 | 61.4 | 61.3 | 57.2 | 51.5 | 59.4 | 51.3 | 68.0 | 67.3 | 72.4 | 80.3 | 63.2 | 57.0 | 72.0 | 69.8 | 63.5 | 3.8 |

## 6-bit Quantized ViT — Accuracy (%)

| Model | Method | Gauss. | Shot | Impul. | Defoc. | Glass | Motion | Zoom | Snow | Frost | Fog | Brit. | Contr. | Elas. | Pix. | JPEG | Avg Acc. | Avg ECE |
|-------|--------|--------|------|--------|--------|-------|--------|------|------|-------|-----|-------|--------|-------|------|------|----------|---------|
| 6-bit | NoAdapt | 44.2 | 42.0 | 44.8 | 39.8 | 28.9 | 43.4 | 34.7 | 53.2 | 59.8 | 59.0 | 75.1 | 27.4 | 39.0 | 59.1 | 65.3 | 47.7 | 9.9 |
| 6-bit | T3A | 43.3 | 41.3 | 42.7 | 29.1 | 23.4 | 38.9 | 30.0 | 49.4 | 58.3 | 60.2 | 73.8 | 31.0 | 36.3 | 58.0 | 65.2 | 45.4 | 30.1 |
| 6-bit | FOA (ours) | 53.2 | 51.8 | 54.6 | 49.6 | 38.8 | 51.0 | 44.8 | 60.3 | 65.0 | 68.8 | 76.7 | 39.5 | 46.6 | 67.3 | 68.6 | 55.8 | 5.5 |
