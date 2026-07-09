---
# Table 5: NetHack Score vs Prior Work

**Source**: Table 5, Appendix D
**Caption**: Score comparison of methods from prior work and our best performing method (denoted as Fine-tuning + KS in the main text, here as "Scaled-BC + Fine-tuning + KS" to differentiate the pre-trained model).

## Offline Only

| Models | Human Monk Score |
|--------|-----------------|
| DQN-Offline (Hambro et al., 2022c) | 0.0 ± 0.0 |
| CQL (Hambro et al., 2022c) | 366 ± 35 |
| IQL (Hambro et al., 2022c) | 267 ± 28 |
| BC (CDGPT5) (Hambro et al., 2022c;a) | 1059 ± 159 |
| Scaled-BC (Tuyls et al., 2023) | 5218 ± — |

## Offline + Online

| Models | Human Monk Score |
|--------|-----------------|
| From Scratch + KS (Hambro et al., 2022c) | 2090 ± 123 |
| From Scratch + BC (Hambro et al., 2022c) | 2809 ± 103 |
| LDD* (Mu et al., 2022) | 2100 ± — |
| **Scaled-BC + Fine-tuning + KS (ours)** | **10588 ± 672** |

## Notes
- Previous neural model SOTA: Scaled-BC at 5218 points
- Our result: 10588 ± 672 (fine-tuning + KS applied to Scaled-BC pre-trained model)
- 2× improvement over previous SOTA (10588 / 5218 ≈ 2.03×)
- LDD* uses large language model guidance; our method uses only PPO + kickstarting
