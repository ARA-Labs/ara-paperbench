---
source: "Table 2, Section 3.3 of arXiv:2506.22419"
claims_verified: [C07]
---

# Table 2: Search Scaffold Configurations

Configuration parameters for the five search scaffolds evaluated in the agent benchmark.

| Scaffold | N_0 (initial roots) | N (branch factor) | p_debug | D_max | M (total nodes) | Iteration? | Debug? |
|----------|-------|---|---------|-------|-----|------|--------|
| Tree | 1 | 3 | 0 | -- | 20 | Yes | No |
| Forest | 3 | 3 | 0 | -- | 20 | Yes | No |
| AIDE | 5 | 1 | 0.5 | 3 | 20 | Yes | Yes |
| Multi-AIDE | 3 | 3 | 0.5 | 3 | 20 | Yes | Yes |
| Flat | 20 | 0 | 0 | -- | 20 | No | No |

## Scaffold Design Rationale

- **Tree**: Single-root exploration with 3-way branching. Pure best-first search without debugging. Tests whether iterative refinement from one starting point suffices.
- **Forest**: Multi-root (3 diverse starting points) with same branching. Tests whether initialization diversity helps.
- **AIDE**: Sequential search with debugging. 5 independent roots, single-branch iteration, 50% debug probability. Matches the original AIDE paper design.
- **Multi-AIDE**: Combines Forest's multi-root branching with AIDE's debug capability. 3 roots, 3-way branching, 50% debug. The best overall performer.
- **Flat**: All 20 nodes generated independently from the root. No iteration, no debugging. Pure best-of-M sampling baseline.

## Key Takeaway

All scaffolds use the same total budget (M=20 nodes). Multi-AIDE combines the benefits of Forest (multiple roots, branching) with AIDE (debugging). Flat search serves as a surprisingly strong baseline that makes 20 independent attempts.
