---
# Table 17: Detailed ECE (%) for Quantized ViT on ImageNet-C
- **Source**: Table 17, Appendix D
- **Caption**: "Effectiveness of our FOA on Quantized ViT-Base models. We report the corruption ECE (%, ↓) on ImageNet-C (severity level 5). The bold number indicates the best result."
- **Conditions**: Quantized ViT-Base (8-bit and 6-bit via PTQ4ViT); batch size 64; ImageNet-C severity level 5

## 8-bit ViT-Base ECE (%)

| Method | Gauss. | Shot | Impul. | Defoc. | Glass | Motion | Zoom | Snow | Frost | Fog | Brit. | Contr. | Elas. | Pix. | JPEG | Avg. |
|--------|--------|------|--------|--------|-------|--------|------|------|-------|-----|-------|--------|-------|------|------|------|
| NoAdapt | 8.3 | 5.7 | 7.5 | 7.9 | 4.9 | 3.0 | 4.4 | 5.5 | 20.7 | 50.0 | 10.4 | 14.1 | 5.2 | 6.2 | 8.3 | 10.8 |
| T3A | 30.0 | 26.0 | 25.7 | 28.7 | 41.9 | 31.2 | 40.1 | 27.2 | 21.6 | 9.6 | 15.8 | 5.7 | 40.7 | 23.1 | 21.0 | 25.9 |
| FOA (ours) | 2.8 | 3.4 | 2.9 | 3.5 | 3.5 | 3.1 | 4.3 | 3.6 | 3.9 | 5.6 | 3.9 | 5.0 | 3.6 | 3.9 | 3.1 | **3.8** |

## 6-bit ViT-Base ECE (%)

| Method | Gauss. | Shot | Impul. | Defoc. | Glass | Motion | Zoom | Snow | Frost | Fog | Brit. | Contr. | Elas. | Pix. | JPEG | Avg. |
|--------|--------|------|--------|--------|-------|--------|------|------|-------|-----|-------|--------|-------|------|------|------|
| NoAdapt | 10.1 | 7.0 | 10.5 | 5.8 | 4.2 | 4.2 | 4.5 | 2.8 | 18.0 | 32.5 | 12.4 | 17.3 | 4.2 | 6.6 | 7.8 | 9.9 |
| T3A | 31.3 | 27.3 | 26.2 | 43.2 | 50.4 | 35.6 | 49.3 | 33.9 | 22.8 | 14.6 | 16.9 | 7.7 | 44.2 | 26.6 | 22.2 | 30.1 |
| FOA (ours) | 5.6 | 4.9 | 6.7 | 3.1 | 2.4 | 5.0 | 3.5 | 6.6 | 7.1 | 7.0 | 6.0 | 7.7 | 3.3 | 5.8 | 7.7 | **5.5** |
