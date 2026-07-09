# Figure 7: RoboticSequence Per-Stage Success Rates throughout Training
- **Source**: Figure 7, Section 5
- **Caption**: "Success rate for each stage of RoboticSequence. The fine-tuning experiments start from a pre-trained policy π* that performs well on peg-unplug-side and push-wall."
- **Axis labels**: X = training steps (up to ~2e6); Y = success rate per stage
- **Conditions**: SAC; 4 stages; pre-trained on last two stages; 20 seeds; 90% CI

## hammer Stage (CLOSE — new task)

| Steps | From Scratch | Vanilla FT | FT + EWC | FT + EM | FT + BC |
|-------|-------------|-----------|---------|--------|--------|
| 0 | ≈0 | ≈0 | ≈0 | ≈0 | ≈0 |
| 200K | ≈0.5 | ≈0.6 | ≈0.7 | ≈0.7 | ≈0.9 |
| 500K | ≈0.7 | ≈0.8 | ≈0.85 | ≈0.85 | ≈0.95 |
| 1M+ | ≈0.9 | ≈0.92 | ≈0.92 | ≈0.92 | ≈0.95 |

## push Stage (CLOSE — new task)

| Steps | From Scratch | Vanilla FT | FT + EWC | FT + EM | FT + BC |
|-------|-------------|-----------|---------|--------|--------|
| 0 | ≈0 | ≈0 | ≈0 | ≈0 | ≈0 |
| 500K | ≈0.3 | ≈0.5 | ≈0.6 | ≈0.6 | ≈0.8 |
| 1M | ≈0.6 | ≈0.7 | ≈0.75 | ≈0.75 | ≈0.85 |
| 2M | ≈0.8 | ≈0.82 | ≈0.83 | ≈0.83 | ≈0.85 |

## peg-unplug-side Stage (FAR — pre-trained task)

| Steps | Pre-trained π* | Vanilla FT | FT + EWC | FT + EM | FT + BC |
|-------|---------------|-----------|---------|--------|--------|
| 0 | ≈1.0 | ≈1.0 | ≈1.0 | ≈1.0 | ≈1.0 |
| 100K | ≈1.0 | ≈0.1 | ≈0.5 | ≈0.1 | ≈1.0 |
| 500K | ≈1.0 | ≈0.3 | ≈0.7 | ≈0.5 | ≈0.95 |
| 1M | ≈1.0 | ≈0.6 | ≈0.85 | ≈0.85 | ≈0.95 |
| 2M | ≈1.0 | ≈0.8 | ≈0.90 | ≈0.90 | ≈0.95 |

## push-wall Stage (FAR — pre-trained task)

| Steps | Pre-trained π* | Vanilla FT | FT + EWC | FT + EM | FT + BC |
|-------|---------------|-----------|---------|--------|--------|
| 0 | ≈1.0 | ≈1.0 | ≈1.0 | ≈1.0 | ≈1.0 |
| 100K | ≈1.0 | ≈0.0 | ≈0.3 | ≈0.05 | ≈0.95 |
| 500K | ≈1.0 | ≈0.1 | ≈0.4 | ≈0.3 | ≈0.95 |
| 1M | ≈1.0 | ≈0.4 | ≈0.55 | ≈0.75 | ≈0.95 |
| 2M | ≈1.0 | ≈0.7 | ≈0.65 | ≈0.85 | ≈0.95 |

**Key findings**:
- BC maintains near-100% success on both FAR stages throughout training
- Vanilla FT: peg-unplug-side drops to ~10% and push-wall drops to 0% at ~100K steps (catastrophic forgetting)
- EM: initial drop in FAR stages, but recovers to ~90% by end
- EWC: partial forgetting of FAR stages, recovers but lower than BC/EM
- All methods learn CLOSE (hammer, push) successfully; BC is fastest
