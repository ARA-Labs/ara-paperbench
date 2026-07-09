---
# Table 16: Detailed ECE (%) for Full-Precision ViT on ImageNet-C
- **Source**: Table 16, Appendix D
- **Caption**: "Comparisons with state-of-the-art methods on ImageNet-C (severity level 5) with ViT-Base regarding ECE (%, ↓). BP is short for backward propagation and the bold number indicates the best result."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64; ImageNet-C severity level 5

| Method | BP | Gauss. | Shot | Impul. | Defoc. | Glass | Motion | Zoom | Snow | Frost | Fog | Brit. | Contr. | Elas. | Pix. | JPEG | Avg. ECE |
|--------|-----|--------|------|--------|--------|-------|--------|------|------|-------|-----|-------|--------|-------|------|------|----------|
| NoAdapt | ✗ | 7.5 | 4.6 | 6.6 | 6.5 | 6.2 | 2.6 | 5.0 | 4.7 | 19.7 | 49.2 | 8.6 | 19.3 | 6.0 | 5.0 | 6.2 | 10.5 |
| LAME | ✗ | 6.5 | 3.6 | 5.6 | 5.1 | 9.4 | 2.2 | 6.2 | 5.6 | 18.1 | 46.3 | 7.7 | 29.0 | 10.6 | 3.9 | 5.0 | 11.0 |
| T3A | ✗ | 29.6 | 30.0 | 29.6 | 31.1 | 42.0 | 32.1 | 37.1 | 25.7 | 26.2 | 14.7 | 16.6 | 6.1 | 35.0 | 24.4 | 22.5 | 26.8 |
| TENT | ✓ | 13.7 | 13.0 | 12.9 | 14.7 | 15.9 | 12.7 | 15.3 | 24.9 | 12.1 | 93.5 | 6.0 | 10.7 | 14.4 | 8.7 | 9.3 | 18.5 |
| CoTTA | ✓ | 4.2 | 2.9 | 4.4 | 7.2 | 12.8 | 7.1 | 11.6 | 4.1 | 0.9 | 5.1 | 3.2 | 15.9 | 8.1 | 5.1 | 5.4 | 6.5 |
| SAR | ✓ | 7.9 | 7.4 | 7.3 | 9.0 | 9.5 | 7.7 | 9.7 | 6.1 | 6.0 | 9.2 | 2.3 | 7.5 | 7.0 | 4.3 | 4.4 | 7.0 |
| FOA (ours) | ✗ | 2.5 | 2.4 | 2.5 | 3.4 | 3.3 | 3.0 | 4.0 | 3.2 | 3.3 | 4.8 | 3.0 | 3.4 | 3.2 | 3.0 | 2.8 | **3.2** |

**Notes**:
- Bold indicates best result per column
- TENT shows ECE of 93.5% on Fog corruption — catastrophic calibration failure
- FOA achieves best ECE on nearly all corruptions
- FOA's low ECE benefits from activation discrepancy regularization in Eq. 5
