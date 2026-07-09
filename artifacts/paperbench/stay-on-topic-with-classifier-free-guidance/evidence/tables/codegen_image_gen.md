# CodeGen Image Generation Task Results

- **Source**: Table 13, Appendix D.2
- **Caption**: Table comparing γ=1 and γ=2 for CodeGen-350M-mono on fixed image generation function completion task.
- **Conditions**: CodeGen-350M-mono; 1600 completions per CFG strength; prompt: `# Return a red square on a 32x32 picture in the form of numpy array with RGB channels\ndef draw() -> np.ndarray:`; γ ∈ {1.0, 2.0}

| Metric | γ=1 | γ=2 | Improvement |
|--------|-----|-----|-------------|
| Correct syntax | — | — | 137% |
| Correct return type | — | — | 189% |
| Correct shape | — | — | 189% |
| L2 distance to reference (red square) | 0.111 | 0.090 | 123% (lower is better) |

## Notes
- Absolute values for "correct syntax", "correct return type", "correct shape" were not provided numerically in the paper; only relative improvements (% increase) are reported.
- L2 distance: pixels normalized to [0, 1]; lower L2 = closer to reference pure-red image.
- "Improvement" column represents relative improvement of γ=2 over γ=1.
- "137%" syntax improvement means correct syntax rate increased by 37% relative to γ=1 (i.e., γ=2 rate = 1.37 × γ=1 rate).
