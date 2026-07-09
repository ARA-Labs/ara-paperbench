---
# Table 5: Ablation of FOA Components
- **Source**: Table 5, Section 4.3
- **Caption**: "Ablations of components in our FOA. Entropy and Activation (Act.) Discrepancy are the left/right item in Fitness Function (Eqn. 5) used for CMA-based prompt adaptation. Act. Shifting is the method proposed in Section 3.2. We report the average results over 15 corruptions on ImageNet-C (level 5) with ViT-Base."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64; ImageNet-C severity level 5; average over 15 corruption types

| Entropy | Act. Discrepancy | Act. Shifting | Acc. (%, ↑) | ECE (%, ↓) |
|---------|-----------------|---------------|-------------|------------|
| — | — | — | 55.5 | 10.5 |
| ✓ | — | — | 44.9 | 36.8 |
| — | ✓ | — | 63.4 | 9.4 |
| — | — | ✓ | 59.1 | 12.7 |
| ✓ | ✓ | — | 63.8 | 9.9 |
| — | ✓ | ✓ | 65.4 | 3.3 |
| ✓ | ✓ | ✓ | **66.3** | **3.2** |

**Row 1**: NoAdapt baseline (no adaptation)
**Row 2**: CMA + entropy fitness only — performs WORSE than NoAdapt
**Row 3**: CMA + activation discrepancy fitness only — large improvement (+7.9%)
**Row 4**: Activation shifting only (no CMA prompt adaptation) — +3.6% improvement
**Row 5**: CMA + full fitness (entropy + discrepancy) without shifting
**Row 6**: CMA + discrepancy fitness + activation shifting — 65.4% accuracy, 3.3% ECE
**Row 7**: Full FOA — best accuracy (66.3%) and best ECE (3.2%)
