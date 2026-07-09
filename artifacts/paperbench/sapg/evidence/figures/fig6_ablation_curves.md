---
# Figure 6: Ablation Study Performance Curves

- **Source**: Figure 6, Section 6.3
- **Caption**: "Performance curves for ablations of our method. The variants of our method with a symmetric aggregation scheme or without an off-policy combination perform significantly worse. Entropy regularization affects performance across environments, giving a benefit in reorientation. Using a high off-policy ratio without subsampling data leads to worse performance on ShadowHand and AllegroHand."
- **X-axis**: Number of environment steps (0 to 2×10¹⁰)
- **Y-axis**: Episode successes (AllegroKuka tasks) or episode rewards (ShadowHand, AllegroHand)
- **Curves**: 6 SAPG variants per panel

## Ablation Variants Compared

| Variant | Description |
|---------|-------------|
| Ours | Standard SAPG (λ_ent=0, leader-follower, 50/50 data split) |
| Ours (entropy coef = 0.005) | SAPG with σ=0.005 for followers |
| Ours (entropy coef = 0.003) | SAPG with σ=0.003 for followers |
| Ours (high off-policy ratio) | No subsampling; full off-policy dataset used |
| Ours (w/o off-policy) | No off-policy aggregation; policies train independently |
| Ours (symmetric off-policy) | Symmetric scheme: each policy updated with all others' data |

## Qualitative Findings per Task

### Allegro Kuka Regrasping
| Variant | Qualitative behavior |
|---------|---------------------|
| Ours (standard) | Best performer (final: 35.7 ± 1.46) |
| Ours (entropy 0.005) | Similar or slightly below standard |
| Ours (entropy 0.003) | Similar to standard |
| Ours (high off-policy) | Marginally worse than standard |
| Ours (symmetric) | Significantly worse |
| Ours (w/o off-policy) | Worst performer |

### Allegro Kuka Throw
| Variant | Qualitative behavior |
|---------|---------------------|
| Ours (standard) | Best performer (final: 23.7 ± 0.74) |
| Ours (entropy 0.003) | Similar to standard |
| Ours (high off-policy) | Marginally worse |
| Ours (symmetric) | Worse than standard |
| Ours (w/o off-policy) | Worst performer |

### Allegro Kuka Reorientation
| Variant | Qualitative behavior |
|---------|---------------------|
| Ours (entropy 0.005) | Best performer (final: 38.6 ± 0.63); ~16.5% better than standard |
| Ours (standard) | Second best (final: 33.2 ± 4.20) |
| Ours (high off-policy) | Initially sample-efficient but lower asymptote than entropy=0.005 |
| Ours (entropy 0.003) | Between standard and 0.005 |
| Ours (symmetric) | Significantly worse |
| Ours (w/o off-policy) | Worst performer |

### Allegro Hand
| Variant | Qualitative behavior |
|---------|---------------------|
| Ours (standard) | Best performer (final: 1.23e4 ± 3.29e2) |
| Ours (entropy 0.003) | Similar to standard |
| Ours (high off-policy) | Significantly worse than standard |
| Ours (symmetric) | Worse |
| Ours (w/o off-policy) | Worst performer |

### Shadow Hand
| Variant | Qualitative behavior |
|---------|---------------------|
| Ours (entropy 0.005) | Best performer (final: 1.28e4 ± 2.80e2) |
| Ours (standard) | Near top (final with λ=0: 1.17e4 ± 2.64e2) |
| Ours (entropy 0.003) | High performance, near top |
| Ours (high off-policy) | Significantly worse than standard on ShadowHand |
| Ours (w/o off-policy) | Significantly worse |
| Ours (symmetric) | Worst performer on ShadowHand |
