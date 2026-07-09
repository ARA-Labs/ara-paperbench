# Figure 6: Montezuma's Revenge Room 7 Success Rate throughout Fine-tuning
- **Source**: Figure 6, Section 5
- **Caption**: "Montezuma's Revenge, success rate in Room 7 which represents a part of the FAR states."
- **Axis labels**: X = training steps (environment steps, up to ~5e7); Y = Room 7 success rate
- **Conditions**: PPO+RND; Room 7 = transition point between CLOSE (Rooms 1–6) and FAR (Room 7+); success = earn coin OR acquire item OR exit via different passage; evaluated every 5M steps; 5 seeds

## Data Points (approximate, read from Figure 6)

| Training Steps | Pre-trained π* | Vanilla Fine-tuning | Fine-tuning + EWC | Fine-tuning + BC |
|----------------|---------------|---------------------|------------------|-----------------|
| 0 | ≈0.80 | ≈0.80 | ≈0.80 | ≈0.80 |
| 5M | ≈0.80 | ≈0.72 | ≈0.78 | ≈0.78 |
| 10M | ≈0.80 | ≈0.65 | ≈0.76 | ≈0.77 |
| 15M | ≈0.80 | ≈0.60 | ≈0.75 | ≈0.76 |
| 20M | ≈0.80 | ≈0.55 | ≈0.74 | ≈0.75 |
| 25M | ≈0.80 | ≈0.58 | ≈0.74 | ≈0.75 |
| 30M | ≈0.80 | ≈0.62 | ≈0.75 | ≈0.76 |
| 40M | ≈0.80 | ≈0.65 | ≈0.75 | ≈0.76 |
| 50M | ≈0.80 | ≈0.65 | ≈0.75 | ≈0.75 |

**Key findings**:
- Vanilla FT Room 7 success rate drops from ~0.80 to ~0.55 by ~20M steps (catastrophic forgetting)
- After ~20M steps, vanilla FT slowly recovers as agent reaches Room 7 during training
- BC and EWC maintain stable success rate ~0.75–0.78 throughout training, close to π* level
- Vanilla FT never fully recovers to pre-trained π* level (~0.80) by end of training
