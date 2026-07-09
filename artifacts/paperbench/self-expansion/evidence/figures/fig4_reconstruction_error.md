# Figure 4: Reconstruction Error During Training (Dynamic Expansion Process)
- **Source**: Figure 4, Section 4.3
- **Caption**: "Reconstruction error during training to show the dynamic expansion process. Expansion occurs for Tasks 1, 2, and 3, while no expansion is triggered for Tasks 4 and 5 due to no detected distribution shift."
- **Dataset**: VTAB (first 5 tasks); self-expansion restricted to last transformer layer only
- **Axes**: X = training progress across 5 tasks (with detection phase markers); Y = reconstruction error of RDs
- **Series**: RD (AE) #1, RD (AE) #2, RD (AE) #3

## Key Data Points (Qualitative — exact pixel values not extractable from text description)

| Task | Phase | RD #1 Error | RD #2 Error | RD #3 Error | Expansion Triggered? |
|------|-------|------------|------------|------------|----------------------|
| Task 1 | Training | Decreases and converges | N/A (not yet added) | N/A | Yes — RD #1 added |
| Task 2 | Detection | High (novel input) | N/A | N/A | Yes — RD #2 added |
| Task 2 | Training | Low (after training) | Decreases and converges | N/A | — |
| Task 3 | Detection | High (novel input) | High (novel input) | N/A | Yes — RD #3 added |
| Task 3 | Training | Low | Low | Decreases and converges | — |
| Task 4 | Detection | ≈Low (at least one RD handles input) | ≈Low | ≈Low | No |
| Task 4 | (No training) | — | — | — | — |
| Task 5 | Detection | ≈Low (at least one RD handles input) | ≈Low | ≈Low | No |
| Task 5 | (No training) | — | — | — | — |

**Key finding**: After training on its task, each RD's reconstruction error decreases and stabilizes. During detection phases for new tasks, existing RDs show high errors for genuinely novel distributions (Tasks 2, 3) but low errors when existing patterns suffice (Tasks 4, 5).
