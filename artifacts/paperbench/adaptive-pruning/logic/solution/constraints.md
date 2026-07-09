# Constraints and Limitations

## Boundary Conditions

### BC1: APT Adapters Must Be Placed Correctly
- APT adapters are required on Q and V projections of all MHA layers (for all model sizes).
- For smaller models (RoBERTa-base, T5-base), APT adapters should also be placed on FFN up-projections to achieve fast convergence.
- For large models (LLaMA 7B, 13B), APT adapters are placed only on Q and V projections to limit memory overhead.

### BC2: Distillation Is Used Only for Smaller Models
- Self-distillation is used for RoBERTa and T5 pruning; it is not used for LLaMA models due to excessive memory costs at scale.
- Without distillation, the performance gap for large LMs is larger (86.4% vs ~99% relative performance).

### BC3: Sparsity Constraints
- The constraint $1 - C(\Theta_t, M_t)/C(\Theta_0, M_0) \geq \gamma_t$ must hold at every training step.
- The constraint $\delta(\Theta_t, M_t, R_t) \leq \Delta_t$ (tuning parameter budget) must hold at every training step.
- Practical sparsity range tested: 40%–95% (RoBERTa), 40%–90% (T5), 30% (LLaMA 7B, 13B).

### BC4: Hardware Requirements
- All experiments conducted on a single A100 GPU.
- Inference batch size: 128 (small models), 32 (LLaMA 7B), 4 (LLaMA 13B).
- For maximum realistic speedup on Ampere GPUs: dimensions should be divisible by 8 (FP16) or 16 (Int8).

### BC5: Model Architecture Constraints
- For encoder-decoder models (T5): cross-attention layers in the decoder must also be counted in the parameter budget.
- For gated FFN models (T5, LLaMA): the FFN parameter count formula uses 3 projection layers (up/gate/down) instead of 2.
- Bias terms and layer norm parameters are excluded from the parameter count (< 1% of total).

### BC6: Optimizer Reset Requirement
- The optimizer state must be reset after each parameter shape change (mask update or rank growth) to avoid training instability.

## Known Limitations

### L1: Performance Gap Widened for Large LMs Without Distillation
- LLaMA 7B achieves only 86.4% relative performance (vs ~99% for RoBERTa) because distillation is disabled.
- Better memory-efficient distillation or parameter sharing strategies could close this gap.

### L2: Training Instability Due to Dynamic Shape Changes
- Newly initialized parameters are added and existing parameters are pruned dynamically; this can cause instability.
- The current mitigation (gradual mask decay with α = 0.01, optimizer reset) may not fully prevent instability.
- Teacher checkpoint selection timing significantly affects performance.

### L3: T5 Inference Efficiency Is Worse Than Expected
- APT prunes more decoder parameters (computationally cheaper for classification) than encoder parameters, leading to worse inference efficiency (1.3× speedup, 81.5% memory) than LoRA+Prune (2.1× speedup, 73.4% memory) for T5 at 60% sparsity on classification tasks.
- This is a side effect of the task-adaptive nature of APT.

### L4: Low-Rank Adapters May Limit Performance Recovery
- APT is built on LoRA (linear adapters), which does not increase model representation capacity.
- Non-linear adapters (HAdapters, Prefix-tuning, Parallel-adapters) may achieve better performance recovery but would add inference overhead (cannot be merged).

### L5: LLaMA 13B LoRA+Prune Slightly Outperforms APT
- APT (avg 55.6) is slightly behind LoRA+Prune (avg 57.1) for LLaMA2-13B, indicating room for improvement in pre-tuning pruning methods for very large models.

### L6: No Hyperparameter Search Conducted
- The paper explicitly states no hyperparameter search was conducted for any training; results may not be fully optimized.
