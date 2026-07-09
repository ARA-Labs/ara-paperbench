# Table 1: Efficiency Comparison of Existing Methods and APT
- **Source**: Table 1, Section 1 (Introduction)
- **Caption**: "Efficiency comparison of existing methods and APT. AP stands for adaptive pruning and AT for adaptive tuning, where the total and tuning parameter sizes are dynamically adjusted. We measure efficiency using training converge time, inference time (T), and peak memory (M). Symbols ⇑ and ⇓ indicate increased and decreased costs, respectively, while = signifies no change in cost. The terms 'low' and 'high' qualify the extent of cost variations."

| Category | Method | Train Time | Train Mem | Inf Time (T) | Inf Mem (M) |
|----------|--------|-----------|-----------|-------------|------------|
| PEFT | Adapter (Pfeiffer et al., 2021) | ⇑High | ⇓Low | ⇑Low | ⇑Low |
| PEFT | LoRA (Hu et al., 2022) | ⇑High | ⇓Low | = | = |
| PEFT | AdaLoRA (Zhang et al., 2023b) | ⇑High | ⇓Low | = | = |
| Pruning | MvP (Sanh et al., 2020) | ⇑High | ⇑Low | ⇓Low | ⇓Low |
| Pruning | BMP (Lagunas et al., 2021) | ⇑High | ⇑Low | ⇓High | ⇓Low |
| Pruning | CoFi (Xia et al., 2022) | ⇑High | ⇑Low | ⇓High | ⇓Low |
| Pruning | MT (Kwon et al., 2022) | ⇓High | = | ⇓Low | ⇓Low |
| Combined | SPA (Hedegaard et al., 2022) | ⇑High | ⇑Low | ⇓High | ⇓Low |
| Combined | LRP (Zhang et al., 2023a) | ⇑High | ⇓Low | ⇓High | ⇓Low |
| Combined | APT (ours) | ⇑Low | ⇓Low | ⇓High | ⇓Low |

*Note: The paper's Table 1 also includes AP (adaptive pruning) and AT (adaptive tuning) indicator columns; APT has both AP and AT checked while others do not.*
