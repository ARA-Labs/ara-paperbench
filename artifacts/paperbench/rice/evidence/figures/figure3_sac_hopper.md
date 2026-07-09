# Figure 3: SAC Agent Refining Performance in Hopper Game
- **Source**: Figure 3, Section 4.3
- **Caption**: "SAC Agent Refining Performance in Hopper Game—In the left part, we show the training curve of obtaining a pre-trained policy through the SAC algorithm. In the right part, we show the refining curves of different methods."
- **Axes**: X = Training Step (1e6), Y = Reward; Left part: 0–1M steps (pre-training); Right part: 0–1M steps (refining)

## Pre-training Phase (Left — SAC, 0 to 1M steps)
| Training Step | SAC Agent Reward |
|---------------|-----------------|
| 0 | ≈0 |
| 200K | ≈1000 |
| 500K | ≈2500 |
| 750K | ≈3200 |
| 1M | ≈3300 (plateau/bottleneck) |

## Refining Phase (Right — 0 to 1M additional steps)
| Method | ~0 steps | ~250K steps | ~500K steps | ~1M steps (final) |
|--------|----------|-------------|-------------|-------------------|
| Ours (RICE) | ≈3300 | ≈3500 | ≈3700 | ≈3900 |
| PPO fine-tuning | ≈3300 | ≈3450 | ≈3550 | ≈3650 |
| StateMask-R | ≈3300 | ≈3400 | ≈3450 | ≈3500 |
| JSRL | ≈3300 | ≈3350 | ≈3400 | ≈3450 |
| SAC fine-tuning | ≈3300 | ≈3250 | ≈3200 | ≈3200 (bottleneck) |
