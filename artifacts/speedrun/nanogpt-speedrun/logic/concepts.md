---
type: concepts
paper: nanogpt-speedrun
---

# Concepts

## Muon Optimizer
- **Definition**: A hybrid optimizer combining OrthogonalNesterov momentum for 2D+ weight matrices (using Newton-Schulz orthogonalization) with standard AdamW for 1D parameters (biases, norms, embeddings). Applies Nesterov momentum in the orthogonal group to accelerate convergence on matrix-valued parameters.
- **Notation**: `Muon(lr_muon, lr_adam, momentum, nesterov=True)`
- **Boundary**: Only applicable to parameters with ≥2 dimensions. 1D parameters fall back to AdamW. Requires distributed orthogonalization for multi-GPU efficiency.
- **Related**: [AdamW, Nesterov Momentum, Newton-Schulz Iteration, SOAP]

## FlexAttention
- **Definition**: PyTorch's flexible attention API (`torch.nn.attention.flex_attention`) enabling custom attention masks compiled into efficient CUDA kernels via `create_block_mask`. Supports document-aware causal masking (prevents cross-document attention) and sliding window patterns.
- **Notation**: `flex_attention(Q, K, V, block_mask=mask)`
- **Boundary**: Requires PyTorch 2.5+ and CUDA 12.5+. Block mask granularity is 128 tokens. Sliding window must align to block boundaries.
- **Related**: [Flash Attention, Block Sparse Attention, Ring Attention]

## NanoGPT Speedrun
- **Definition**: A community benchmark where participants optimize GPT-2 (124M parameter) training to reach val_loss ≤ 3.28 on FineWeb-Edu 10B tokens as fast as possible on 8×H100 GPUs. Each "record" is a new submission that improves upon the previous best time.
- **Notation**: Record N (R_N), train_time in milliseconds, val_loss threshold 3.28
- **Boundary**: Fixed hardware (8×H100 80GB NVLink), fixed dataset, fixed evaluation (HellaSwag via val_loss proxy).
- **Related**: [MLPerf, DAWNBench, Stanford NanoGPT]

## Best-of-N (BoN) Search
- **Definition**: Tree-structured experimentation strategy where N candidate modifications are evaluated in parallel from the current best version, the best performer is selected, and the process repeats. Generalizes linear search by allowing branching exploration.
- **Notation**: `BoN(branch_factor=N, iterations=T, debug_prob=p)`
- **Boundary**: Requires N× compute per iteration vs. linear search. Effective when optimization landscape has multiple viable paths.
- **Related**: [AIDE, Monte Carlo Tree Search, Evolutionary Search]

## Newton-Schulz Iteration
- **Definition**: An iterative method to approximate the matrix square root inverse (orthogonalization) without explicit SVD. Used in Muon to project gradient updates onto the orthogonal group: `X_{k+1} = aX_k + bX_k^3 + cX_k^5` with specific coefficients for cubic convergence.
- **Notation**: `newton_schulz_5(G, steps=5, eps=1e-7)`
- **Boundary**: Requires input matrix spectral norm < 1.86 for convergence. Number of iterations (typically 5) trades off accuracy vs. compute.
- **Related**: [SVD, Polar Decomposition, Matrix Square Root]

## U-Net Skip Connections
- **Definition**: Encoder-decoder style residual connections between transformer layers, inspired by U-Net architecture. Layer i's output is blended with layer (N-1-i)'s input using learnable mixing weights, enabling gradient shortcuts and feature reuse across depth.
- **Notation**: `x = α * x_encoder[i] + (1-α) * x_decoder[i]`
- **Boundary**: Only applicable when number of layers is even (symmetric encoder-decoder). Mixing weights require careful initialization.
- **Related**: [ResNet, DenseNet, Highway Networks]

## Gap Recovered
- **Definition**: The evaluation metric for agent performance. Measures what fraction of the human-authored speedup an agent achieves: `gap_recovered = (T_baseline - T_agent) / (T_baseline - T_target)` where T_baseline is the starting record's time and T_target is the next record's time.
- **Notation**: `GR ∈ [0, 1]` (0 = no improvement, 1 = fully matched human record)
- **Boundary**: Can exceed 1 if agent finds a faster path than the human record. Negative if agent's code is slower than baseline.
- **Related**: [Interquartile Mean, Normalized Score]

## Hint Levels
- **Definition**: Four abstraction levels for providing optimization knowledge to agents:
  - Level 0 (diff): Raw code diff between records
  - Level 1 (pseudo): Pseudocode description of the change
  - Level 2 (description): Natural language explanation
  - Level 3 (paper): Academic paper describing the technique
  - Level z: Zero knowledge (no hints)
- **Boundary**: Level 0 is not used in benchmarks as it trivializes the task. Combinations (e.g., [1,2], [1,2,5]) test cumulative knowledge.
- **Related**: [Curriculum Learning, Scaffolded Learning]
