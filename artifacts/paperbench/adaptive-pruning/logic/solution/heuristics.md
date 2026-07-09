# Heuristics

## H01: Gradual Mask Decay (α = 0.01)
- **Rationale**: Setting pruning masks directly from 1 to 0 causes training instability due to sudden parameter removal. Gradual decay allows the remaining parameters to adapt before the pruned block fully disappears.
- **Sensitivity**: high
- **Bounds**: α ∈ (0, 0.1]; α = 0.01 used in all experiments.
- **Code ref**: [src/execution/pruning.py]
- **Source**: §C (Appendix C), Algorithm 1

## H02: Exponential Moving Average for Salience (β = 0.85)
- **Rationale**: Single-batch salience estimates are noisy. EMA with β = 0.85 smooths the salience signal across recent training steps, following AdaLoRA (Zhang et al., 2023b).
- **Sensitivity**: medium
- **Bounds**: β ∈ [0.8, 0.95]; β = 0.85 used in all experiments. Equivalently: EMA = 0.85·prev + 0.15·current.
- **Code ref**: [src/execution/salience.py]
- **Source**: §A (Appendix A), following Zhang et al., 2023b

## H03: Initial Adapter Rank = 8
- **Rationale**: Starting all adapter ranks at 8 provides a moderate initial tuning capacity. The rank grows adaptively during training; starting too high wastes memory and may hurt convergence (Figure 5a shows ranks > 64 degrade accuracy).
- **Sensitivity**: medium
- **Bounds**: Initial rank ∈ [4, 64]; rank = 8 used in all experiments. Ranks > 256 degrade performance below fine-tuning baseline in some cases.
- **Code ref**: [src/execution/apt_adapter.py]
- **Source**: §A (Appendix A), Figure 5a

## H04: Scaling Factor s = 2 (Static)
- **Rationale**: Follows LoRA's scaling convention; set to 2 statically. This prevents tuning parameters from dominating the frozen weights during early training when ranks are small.
- **Sensitivity**: low
- **Bounds**: s = 2 fixed; not searched.
- **Code ref**: [src/execution/apt_adapter.py]
- **Source**: §4.1, §A (Appendix A)

## H05: Cubic Sparsity Schedule
- **Rationale**: The cubic schedule γ_t = γ_T + (1-γ_T)(1-t/T)^3 front-loads pruning in early training when the model is still adapting to the task, leaving later training steps for stable fine-tuning on the pruned structure. Linear or step schedules can cause instability when too many parameters are removed at once.
- **Sensitivity**: medium
- **Bounds**: Exponent = 3 (cubic); T_prune = 20 epochs for GLUE/SQuAD, 6 epochs for CNN/DM.
- **Code ref**: [src/execution/pruning.py]
- **Source**: §A (Appendix A)

## H06: Zero Initialization for New W_B Columns (Rank Expansion)
- **Rationale**: When expanding adapter rank, new W_B columns are initialized to zero and new W_A rows are initialized from N(0, σ²). This ensures the layer output is unchanged immediately after rank expansion, preventing training disruption.
- **Sensitivity**: high
- **Bounds**: W_B new columns = 0; W_A new rows ~ N(0, σ²). Alternative initializations that change the output will destabilize training.
- **Code ref**: [src/execution/apt_adapter.py]
- **Source**: §4.3

## H07: Random Layer Mapping for Self-Distillation (4 Layers, Quarter-Sliced)
- **Rationale**: Using 4 randomly sampled teacher layers (one per quarter of the network depth) per epoch provides coverage of the full network while avoiding the computational cost of matching all layers. Re-computing the mapping every step ensures the closest non-pruned student layer is always used.
- **Sensitivity**: medium
- **Bounds**: 4 teacher layers sampled from 4 equal-depth slices per epoch. Layer mapping updated every training step.
- **Code ref**: [src/execution/distillation.py]
- **Source**: §4.4, §B (Appendix B), following Haidar et al., 2022
