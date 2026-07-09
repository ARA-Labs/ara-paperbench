# Figure 5 / Figure 11: Adapter Usage Visualization on VTAB
- **Source**: Figure 5, Section 4.3 (same as Figure 11, Appendix C.3)
- **Caption**: "Visualization of adapter usage on VTAB. Adapters 1, 2, and 3 are added and trained on Tasks 1, 2, and 3, respectively. Tasks 4 and 5 primarily reuse Adapters 1 and 3 due to similar feature distributions with Tasks 1 and 3."
- **Dataset**: VTAB (5 tasks); self-expansion restricted to last transformer layer only
- **Axes**: X = Adapter ID (1, 2, 3); Y = Task ID (1–5)
- **Values**: Normalized average adapter usage (routing weight) per task; values sum to 1 per task
- **Note**: Exact values are approximate readings from heatmap figure

| Task ID | Adapter #1 Weight (≈) | Adapter #2 Weight (≈) | Adapter #3 Weight (≈) |
|---------|-----------------------|-----------------------|-----------------------|
| Task 1 | ≈0.70 | N/A | N/A |
| Task 2 | ≈0.15 | ≈0.70 | N/A |
| Task 3 | ≈0.10 | ≈0.10 | ≈0.65 |
| Task 4 | ≈0.60 | ≈0.15 | ≈0.25 |
| Task 5 | ≈0.15 | ≈0.20 | ≈0.55 |

**Key finding**: Each task predominantly uses the adapter trained on its own distribution. Task 4 (land cover, similar to Task 1 remote sensing) reuses Adapter 1. Task 5 (flowers, similar to Task 3 pets) reuses Adapter 3. This demonstrates effective cross-task knowledge reuse via the learned router.

**VTAB domain order** (from reproduction rubric):
- Task 1: resisc45 (classes 10-19) — remote sensing
- Task 2: dtd (classes 20-29) — texture
- Task 3: pets (classes 30-39) — natural images (animals)
- Task 4: eurosat (classes 40-49) — land cover/satellite
- Task 5: flowers (classes 50-59) — natural images (flowers)
