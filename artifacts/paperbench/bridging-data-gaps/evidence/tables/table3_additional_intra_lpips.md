---
# Table 3: Additional Intra-LPIPS Results (Appendix)

**Source**: Table 3, Appendix A.1
**Metric**: Intra-LPIPS (↑ higher = more diverse)
**Task**: 10-shot FFHQ → Sketches and FFHQ → Amedeo Modigliani's paintings
**Supporting claims**: C01

## Notes
- LDM-TAN not reported for these tasks (DDPM-TAN only)
- Bold values = best result per column (as marked in paper)
- Values reported as mean ± std

## Table

| Methods | FFHQ→Sketches | FFHQ→Amedeo's paintings |
|---------|---------------|-------------------------|
| TGAN | 0.394±0.023 | 0.548±0.026 |
| TGAN+ADA | 0.427±0.022 | 0.560±0.019 |
| EWC | 0.430±0.018 | 0.594±0.028 |
| CDC | 0.454±0.017 | 0.620±0.029 |
| DCL | 0.461±0.021 | 0.616±0.043 |
| DDPM-PA | 0.495±0.024 | 0.626±0.022 |
| DDPM-TAN (Ours) | **0.544±0.025** | 0.620±0.021 |

## Key Observations
- DDPM-TAN achieves best Intra-LPIPS on FFHQ→Sketches (0.544±0.025), significantly above DDPM-PA (0.495)
- On FFHQ→Amedeo's paintings, DDPM-TAN (0.620) matches CDC (0.620) but does not exceed DDPM-PA (0.626)
- Paper highlights the Sketches result as particularly strong ("far more better than other methods")
