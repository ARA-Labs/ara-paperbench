---
# Figure 3: Main Performance Results

**Source**: Figure 3, §4
**Claims**: C01, C03, C04, C05

## Description
Learning curves comparing fine-tuning methods across all three environments. Each subplot shows performance vs training steps for: Pre-trained π* (frozen), Training from scratch, Vanilla fine-tuning, Fine-tuning + EWC, Fine-tuning + BC, Fine-tuning + KS (NetHack only).

## Figure 3a: NetHack (Human Monk)
- **X-axis**: Environment steps (up to ~2.5B)
- **Y-axis**: Average return (in-game score)
- **FPC type**: Imperfect cloning gap

| Method | Final Score (approx.) | Notes |
|--------|----------------------|-------|
| Pre-trained π* (frozen) | ~4500–5000 | Horizontal baseline; from Tuyls et al., 2023 |
| From scratch | 776 | Lowest; see Table 4 for exact value |
| Vanilla fine-tuning | 647 | Deteriorates; see Table 4 for exact value |
| Fine-tuning + EWC | 3976 | Slightly above vanilla FT; see Table 4 |
| Fine-tuning + BC | 7610 | New SOTA above pre-trained; see Table 4 |
| Fine-tuning + KS | 10588 | Highest; 2× pre-trained; see Table 4/5 |

## Figure 3b: Montezuma's Revenge
- **X-axis**: Environment steps (up to ~1e8)
- **Y-axis**: Average return
- **FPC type**: State coverage gap
- KS not shown (underperforms in state coverage gap)

| Method | Final Return (approx.) | Notes |
|--------|------------------------|-------|
| Training from scratch | lowest | Baseline |
| Vanilla fine-tuning | intermediate | Improves after ~20M steps when agent enters Room 7 |
| Fine-tuning + EWC | intermediate-high | Saturates lower than BC; converges ~5e7 steps |
| Fine-tuning + BC | ~6000 | Highest; diverges from vanilla FT at ~20M steps |

## Figure 3c: RoboticSequence
- **X-axis**: Environment steps (up to ~3e6)
- **Y-axis**: Overall success rate (0 to 1)
- **FPC type**: State coverage gap
- KS not shown (underperforms)

| Method | Final Success Rate (approx.) | Notes |
|--------|------------------------------|-------|
| Training from scratch | ~0.15 | Near zero early; slow improvement |
| Vanilla fine-tuning | ~0.15 | Indistinguishable from scratch |
| Fine-tuning + EWC | ~0.55 | Outperforms vanilla FT |
| Fine-tuning + EM | ~0.70 | Close second to BC |
| Fine-tuning + BC | ~0.80 | Highest; ~80% by ~1e6 steps then plateau |
