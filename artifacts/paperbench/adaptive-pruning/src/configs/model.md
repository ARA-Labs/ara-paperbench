# Model Configurations

## RoBERTa-base Architecture
- **Value**: Hidden dim d_m = 768; 12 attention heads (n_h = 12, d_h = 64); 12 transformer layers (n_L = 12); FFN dim n_f = 3072; total ~125M parameters
- **Rationale**: Standard RoBERTa-base from Liu et al., 2019; used for GLUE and SQuAD experiments.
- **Search range**: Not applicable (pre-trained model)
- **Sensitivity**: Not applicable
- **Source**: §5.1, Appendix C

## T5-base Model
- **Value**: t5-lm-adapt variant (pre-trained on C4 corpus only, no downstream task pre-training); ~250M parameters; encoder-decoder architecture; gated FFN (up/gate/down projections)
- **Rationale**: t5-lm-adapt ensures fair comparison by guaranteeing the model has not observed downstream tasks in pre-training.
- **Search range**: Not applicable
- **Sensitivity**: Not applicable
- **Source**: §5.1 footnote 4

## LLaMA2-7B Architecture
- **Value**: 7 billion parameters; decoder-only; gated FFN; query/value MHA projections as APT adapter targets
- **Rationale**: Large-scale evaluation; represents consumer-accessible large LM (target: <24 GB for pruning).
- **Search range**: Not applicable
- **Sensitivity**: Not applicable
- **Source**: §5.1, §5.4

## LLaMA2-13B Architecture
- **Value**: 13 billion parameters; decoder-only; gated FFN; same APT configuration as 7B
- **Rationale**: Tests scalability of APT to larger models; evaluated in Appendix D.
- **Search range**: Not applicable
- **Sensitivity**: Not applicable
- **Source**: Appendix D.3

## BERT-base Architecture
- **Value**: ~110M parameters; 12 layers, 12 heads, hidden dim 768; evaluated in Appendix D for PST/LRP comparison
- **Rationale**: Legacy baseline comparison with existing PEFT+pruning methods.
- **Search range**: Not applicable
- **Sensitivity**: Not applicable
- **Source**: §5.2, Appendix D.1

## APT Adapter Placement — RoBERTa / T5 (Small Models)
- **Value**: Q projection (MHA), V projection (MHA), up-projection (FFN) in all transformer layers
- **Rationale**: Including FFN adapters for smaller models enables faster convergence; feasible given smaller total parameter count.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §4.1

## APT Adapter Placement — LLaMA (Large Models)
- **Value**: Q projection (MHA), V projection (MHA) only; no FFN adapters
- **Rationale**: Omitting FFN adapters reduces training memory overhead for large models; tradeoff in performance recovery.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §4.1

## Target Sparsity (Main Results)
- **Value**: γ_T = 0.6 for RoBERTa and T5 (60% pruned, 40% remain); γ_T = 0.3 for LLaMA2-7B and 13B (30% pruned, 70% remain)
- **Rationale**: 60% sparsity for small models provides a good efficiency-performance tradeoff; 30% for LLaMA is more conservative given distillation-free setting.
- **Search range**: Analyzed: 40%–95% for RoBERTa (Figure 3); 40%–90% for T5 (Figure 3); 30% and 50% for LLaMA (Table 5)
- **Sensitivity**: high
- **Source**: §5.4, Table 2, Table 3

## RoBERTa-base Block Counts (Example)
- **Value**: C_head = 4 × 768 × 768 / 12 = 196,608 params/head; C_neuron = 2 × 768 = 1,536 params/neuron; C_dimension = 12 × (4×768 + 2×3072) = 110,592 params/dimension-unit
- **Rationale**: Used in salience density computation and binary search parameter counting.
- **Search range**: Not applicable (architectural constants)
- **Sensitivity**: Not applicable
- **Source**: Appendix C, Equations 10–12
