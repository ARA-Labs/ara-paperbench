---
# Figure 8: MLP Reconstruction Error — State Diversity Analysis
- **Source**: Figure 8, §6.4
- **Caption**: "Curves comparing reconstruction error for states visited during training using MLPs with varying hidden layer dimensions for SAPG (Ours), PPO and a randomly initialized policy"

## Axis Information
- **X-axis**: Hidden layer size of reconstruction MLP (approximately {8, 16, 32, 64} neurons)
- **Y-axis**: L2 reconstruction error (training error on state batches)
- **Methods**: SAPG (Ours), PPO, Random policy

## Metric Definition
- A small feedforward network (2 layers, ReLU activation, Adam optimizer) is trained to reconstruct state inputs
- Higher reconstruction error = harder-to-compress distribution = higher state diversity
- If a batch has diverse states, a small network cannot fit all states well → high error

## Network Architecture (from rubric §Logging #17)
- 2 layers
- Hidden layer sizes: {8, 16, 32, 64} neurons
- Activation: ReLU
- Optimizer: Adam
- Loss: L2 reconstruction error of predicted state transitions

## Relative Reconstruction Error Rankings (from §6.4)

| Hidden Layer Size | SAPG Error | PPO Error | Random Policy Error | Winner (highest diversity) |
|-------------------|-----------|-----------|---------------------|---------------------------|
| 8 neurons | Highest | Middle | Lowest | SAPG |
| 16 neurons | Highest | Middle | Lowest | SAPG |
| 32 neurons | Highest | Middle | Lowest | SAPG |
| 64 neurons | Highest | Middle | Lowest | SAPG |

**Note**: Exact values not reported in paper. Rankings are ≈ (best-effort from §6.4 text: "training error is consistently higher for our method compared to PPO across different hidden layer sizes"). In some variants, SAPG and PPO show similar reconstruction errors while both significantly exceed the random policy.

## Summary Across Experiment Variants

| Variant | SAPG vs PPO | SAPG vs Random | PPO vs Random |
|---------|-------------|----------------|---------------|
| Primary (Fig 8a) | SAPG > PPO | SAPG > Random | PPO > Random |
| Secondary (Fig 8b) | SAPG ≈ PPO | SAPG >> Random | PPO >> Random |
| Tertiary (Fig 8c) | SAPG ≈ PPO | SAPG >> Random | PPO >> Random |

## Qualitative Findings (from §6.4)

- "Training error is consistently higher for our method [SAPG] compared to PPO across different hidden layer sizes"
- SAPG: highest reconstruction error across all tested hidden layer sizes
- PPO: middle; lower than SAPG but higher than random
- Random policy: lowest reconstruction error (less structured state distribution → easier to reconstruct)
- Pattern is consistent: SAPG > PPO > Random for all network sizes in primary experiment
