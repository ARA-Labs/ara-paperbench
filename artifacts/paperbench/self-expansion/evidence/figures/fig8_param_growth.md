# Figure 8 / Figure 10: Added Parameters Over Tasks on ImageNet-A
- **Source**: Figure 8, Section 4.3 (same as Figure 10, Appendix C.2)
- **Caption**: "Analysis on added parameters (in Millions) during model deployment on ImageNet-A. We compare with methods using fixed number of prompts like L2P, and methods like DualPrompt and CODA-P that incrementally expand like SEMA but with prompts and on a linear basis according to tasks. Expansion by task adds adapters for every incoming task, whilst SEMA executes expansion on demand, which increments parameters on a sub-linear basis."
- **Dataset**: ImageNet-A (20-task split, 10 classes per task)
- **Axes**: X = Number of tasks (1–20); Y = Added parameters (Millions)
- **Note**: "Specifically, SEMA added more parameters (with expansions at more layers) at Task 9 than other steps with expansion."

## Approximate Parameter Values at Key Task Points

| Method | Task 1 (≈M) | Task 5 (≈M) | Task 10 (≈M) | Task 15 (≈M) | Task 20 (≈M) | Growth Pattern |
|--------|------------|------------|-------------|-------------|-------------|----------------|
| L2P | ≈0.20 | ≈0.20 | ≈0.20 | ≈0.20 | ≈0.20 | Fixed (constant) |
| DualPrompt | ≈0.27 | ≈0.55 | ≈1.10 | ≈1.64 | ≈1.10 | Linear |
| CODA-P | ≈1.00 | ≈2.00 | ≈2.00 | ≈3.00 | ≈4.00 | Linear |
| SEMA | ≈0.03 | ≈0.20 | ≈0.45-0.56 | ≈0.56 | ≈0.560 | Sub-linear |
| Expansion by Task | ≈0.10 | ≈0.50 | ≈0.95 | ≈1.43 | ≈1.904 | Linear |

**Key findings**:
- L2P: constant parameter count (fixed prompt pool)
- DualPrompt and CODA-P: linear growth with task count
- SEMA: sub-linear growth; expands only when z-score signal triggers; notable expansion at Task 9
- Expansion-by-Task: linear growth but less than CODA-P; still less efficient than SEMA
- SEMA final: 0.560M (Table 5) vs Expansion-by-Task: 1.904M — SEMA achieves same or better accuracy with 3.4× fewer parameters
