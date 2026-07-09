# Figure 2: Agent Refining Performance in Two Sparse MuJoCo Games
- **Source**: Figure 2, Section 4.3
- **Caption**: "Agent Refining Performance in two Sparse MuJoCo Games—For Group (a), we fix the explanation method to our method (mask network) if needed while varying refining methods. For Group (b), we fix the refining method to our method while varying the explanation methods."
- **Axes**: X = Training steps (0 to ~500,000), Y = Reward (0 to ~1000)
- **Note**: Exact data points are read from line plots; values marked ≈ are best-effort estimates from the figures.

## Group (a): Fix Explanation (Ours); Vary Refining Methods

### SparseHopper
| Method | ~100K steps | ~250K steps | ~500K steps (final) |
|--------|-------------|-------------|---------------------|
| Ours | ≈0 | ≈400 | ≈900 |
| JSRL | ≈0 | ≈0 | ≈50 |
| StateMask-R | ≈0 | ≈100 | ≈200 |
| PPO fine-tuning | ≈0 | ≈0 | ≈0 |

### SparseHalfCheetah
| Method | ~50K steps | ~150K steps | ~250K steps (final) |
|--------|------------|-------------|---------------------|
| Ours | ≈0 | ≈500 | ≈900 |
| JSRL | ≈0 | ≈0 | ≈100 |
| StateMask-R | ≈0 | ≈0 | ≈150 |
| PPO fine-tuning | ≈0 | ≈0 | ≈0 |

## Group (b): Fix Refining Method (Ours); Vary Explanation Methods

### SparseHopper
| Explanation Method | ~100K steps | ~250K steps | ~500K steps (final) |
|-------------------|-------------|-------------|---------------------|
| Ours | ≈0 | ≈400 | ≈900 |
| StateMask | ≈0 | ≈350 | ≈850 |
| Random | ≈0 | ≈100 | ≈300 |

### SparseHalfCheetah
| Explanation Method | ~50K steps | ~150K steps | ~250K steps (final) |
|-------------------|------------|-------------|---------------------|
| Ours | ≈0 | ≈500 | ≈900 |
| StateMask | ≈0 | ≈400 | ≈850 |
| Random | ≈0 | ≈100 | ≈400 |
