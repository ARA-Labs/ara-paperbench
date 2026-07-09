# Figure 3: SAC Agent Refining Performance in Hopper Game
- **Source**: Figure 3, Section 4.3
- **Caption**: "SAC Agent Refining Performance in Hopper Game—In the left part, we show the training curve of obtaining a pre-trained policy through the SAC algorithm. In the right part, we show the refining curves of different methods."
- **Axis labels**: X: Training Step (1e6 units, total 2M steps shown: 1M pretrain + 1M refine); Y: Reward
- **Conditions**: Hopper-v3 dense reward; SAC pre-trained for 1M steps; refining for 1M steps; 3 seeds

## Left Panel: SAC Pre-training (0 to 1M steps)
| Checkpoint | Approx. Reward |
|-----------|----------------|
| 0 steps | ≈0 |
| 500K steps | ≈2000 |
| 1M steps | ≈3200-3500 (reaches bottleneck) |

## Right Panel: Refining (1M to 2M steps)
| Method | Approx. Final Reward (at 2M steps) | Qualitative description |
|--------|-------------------------------------|------------------------|
| Ours (RICE) | ≈3800-4000 | Highest final reward; breaks through SAC bottleneck |
| PPO fine-tuning | ≈3500-3700 | Moderate improvement; better than SAC fine-tuning |
| StateMask-R | ≈3300-3500 | Limited improvement; near pre-training level |
| JSRL | ≈3400-3600 | Moderate improvement |
| SAC fine-tuning | ≈3200-3400 | Stays at bottleneck; minimal improvement |

**Note**: All values are approximate visual readings from Figure 3 (line plot). Exact values not given in paper. Paper states: "RICE achieves higher rewards than the other refining methods when refining a pretrained SAC agent"; "fine-tuning the DRL agent with the SAC algorithm still suffers from the training bottleneck while switching to the PPO algorithm provides an opportunity to break through the bottleneck." Mark all as ≈.
