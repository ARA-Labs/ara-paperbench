---
# Table 9: Design Choices — Learnable Parameters × Optimizer × Loss Function
- **Source**: Table 9, Section 4.4
- **Caption**: "Empirical studies of design choices w.r.t. learnable parameters, optimizer and loss function. We report the average results over 15 corruptions on ImageNet-C (level 5) with ViT-Base."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64; ImageNet-C severity level 5; average over 15 corruptions

| Row | Learnable Params | Optimizer | Loss | Acc. (%, ↑) | ECE (%, ↓) |
|-----|-----------------|-----------|------|-------------|------------|
| NoAdapt | — | — | — | 55.5 | 10.5 |
| TENT | norm layers | SGD | entropy | 59.6 | 18.5 |
| exp1 | prompts | SGD | entropy | 50.7 | 18.4 |
| exp2 | norm layers | SGD | Eqn. (5) | 70.5 | 7.9 |
| exp3 | prompts | SGD | Eqn. (5) | 64.6 | 3.7 |
| exp4 | norm layers | CMA | Eqn. (5) | 0.1 | 5.8 |
| exp5 | norm layers | CMA | entropy | 0.1 | 99.0 |
| exp6 | prompts | CMA | entropy | 44.9 | 36.8 |
| FOA (ours) | prompts | CMA | Eqn. (5) | 65.4 | 3.3 |

**Key observations**:
- exp4, exp5: CMA on norm layers (high-dim) → catastrophic collapse to 0.1% accuracy
- exp6: CMA on prompts with entropy → 44.9% (worse than NoAdapt 55.5%)
- exp2: Proposed Eq.5 fitness with SGD on norm layers → 70.5% (best accuracy, but requires BP)
- exp3: Proposed Eq.5 fitness with SGD on prompts → 64.6% (good, requires BP)
- FOA: Proposed Eq.5 fitness with CMA on prompts → 65.4% (best BP-free performance)
- Note: FOA in Table 9 (65.4%) differs slightly from Table 2 (66.3%) as Table 9 does not include activation shifting
