---
source: "Section 4.8 and Figure 7 of arXiv:2506.22419"
claims_verified: [C08]
---

# Table 4: Cumulative Speedrun FSR Degradation

FSR when agents must build on their own previous output (cumulative) vs. starting from ground-truth records (non-cumulative). Configuration: o3-mini + Multi-AIDE + L1 hints.

| Transition | Non-Cumulative FSR | Cumulative FSR | Delta |
|------------|-------------------|----------------|-------|
| R1 -> R2 | ~0.60 | ~0.60 | 0.00 |
| R2 -> R3 | ~0.45 | ~0.20 | -0.25 |
| R3 -> R4 | ~0.35 | ~0.05 | -0.30 |
| R4 -> R5 | ~0.30 | ~0.00 | -0.30 |

## Analysis

- **Error compounding**: Agent's own imperfect solutions create a progressively harder starting point. Each suboptimal implementation introduces code patterns that make the next optimization harder to integrate.
- **Failure cascade**: By the 4th transition (R4->R5), cumulative FSR drops to ~0%. The agent cannot make meaningful progress when building on its own prior work.
- **Non-cumulative stability**: Non-cumulative FSR (starting from ground-truth) stays relatively stable across transitions, confirming that the degradation is caused by compounding agent errors, not inherent task difficulty.
- **Implication for autonomous research**: This is the most concerning finding -- agents cannot reliably chain innovations even when each individual step has moderate success probability. Autonomous multi-step research requires near-perfect per-step execution to avoid cascading failures.
