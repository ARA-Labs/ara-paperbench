---
source: "Figure 7, Section 4.8 of arXiv:2506.22419"
claims_verified: [C08]
---

# Figure 7: Cumulative FSR Degradation

FSR in cumulative mode (building on own output) vs. non-cumulative (ground-truth starting points).

## Data

| Transition | Non-Cumulative FSR | Cumulative FSR |
|------------|-------------------|----------------|
| R1 -> R2 | 0.60 | 0.60 |
| R2 -> R3 | 0.45 | 0.20 |
| R3 -> R4 | 0.35 | 0.05 |
| R4 -> R5 | 0.30 | 0.00 |

Configuration: o3-mini + Multi-AIDE + L1 hints.

## Key Observations

- **Non-cumulative FSR stays relatively stable** across transitions (~0.30-0.60)
- **Cumulative FSR degrades sharply**: ~60% at R1->R2, ~20% at R2->R3, ~5% at R3->R4, ~0% at R4->R5
- **Error compounding**: Imperfect agent solutions create progressively harder starting points. Non-standard code patterns, subtle bugs, and missing optimizations from prior steps accumulate.
- **This is the most concerning finding for autonomous research**: Agents cannot reliably chain innovations. Even moderate per-step success (~50%) leads to near-zero cumulative success within 3-4 steps.

## Visualization Type

Paired bar chart. X-axis: transition index. Two bars per transition (cumulative in red, non-cumulative in blue). Y-axis: FSR.
