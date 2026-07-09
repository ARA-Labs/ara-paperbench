# Training Configuration

## Learning Rate (η)
- **Value**: 5e-6
- **Rationale**: Prevents catastrophic forgetting of pretrained DeBERTa/BERT representations; allows stable convergence of the NCE objective without destabilizing the energy function
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix H.2

## Batch Size
- **Value**: 64
- **Rationale**: Provides sufficient gradient signal across positive and negative samples per update step; balances compute utilization and training stability
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix H.2

## Number of Training Steps
- **Value**: 6,000
- **Rationale**: Sufficient for convergence on datasets ranging from 229 to 7,473 training samples; empirically determined as default
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix H.2

## Optimizer
- **Value**: AdamW
- **Rationale**: Standard optimizer with decoupled weight decay; well-suited for fine-tuning pretrained transformers
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Appendix H.2

## Weight Decay
- **Value**: 0.01
- **Rationale**: Light regularization to prevent overfitting the small adapter to the limited NCE training signal
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix H.2

## Number of Online Adaptation Iterations (T)
- **Value**: Default not explicitly stated; experiments evaluated T ∈ {0, 1, 2, 3, 4}; T=3 appears to be the practical default based on Figure 3(b)
- **Rationale**: More iterations enable self-improvement via dynamic positive/negative sets; performance plateaus around T=3–4
- **Search range**: {0, 1, 2, 3, 4}
- **Sensitivity**: medium
- **Source**: §4.6, Figure 3(b)

## Beam Size (k)
- **Value**: 3 (default)
- **Rationale**: Balances exploration quality (+2.41% vs k=1) against API cost (3× more LLM calls per step vs k=1)
- **Search range**: {1, 3, 5}
- **Sensitivity**: medium
- **Source**: §4.1, §4.6, Figure 3(a)

## Maximum Generation Length
- **Value**: 512 tokens
- **Rationale**: Sufficient for multi-step reasoning chains in all four evaluated tasks
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix H.2

## LLM Generation Temperature
- **Value**: 1.0 (for black-box LLM candidate generation during training and inference)
- **Rationale**: Maintains diversity in generated candidates for effective beam search and varied negative samples
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix H.2

## SFT Evaluation Temperature
- **Value**: 0 (for Azure-SFT baseline evaluation)
- **Rationale**: Greedy decoding for deterministic, reproducible evaluation of fine-tuned models
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Appendix H.2

## Azure-SFT Fine-Tuning Epochs
- **Value**: 3 epochs (for Azure-SFT baseline) / 5 epochs (for gpt-3.5-turbo fine-tuning via Azure API as mentioned in §4.1)
- **Rationale**: Limited by Azure API's 3 adjustable hyperparameters; 3 used as default for all Azure-SFT experiments
- **Search range**: {default} for batch size and LR multiplier; epochs varied in grid search (see Table 9)
- **Sensitivity**: medium
- **Source**: Appendix F.2, H.2

## LoRA Rank (r) — SFT-LoRA Baseline
- **Value**: r=128 (for 0.1B adapter size comparison); r=384 (for 0.3B adapter size comparison)
- **Rationale**: Chosen to match the parameter count of the corresponding BBOX-ADAPTER variant for fair comparison
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Appendix F.2

## LoRA Alpha — SFT-LoRA Baseline
- **Value**: α=2r (i.e., 256 for r=128; 768 for r=384)
- **Rationale**: Follows recommended setting from original LoRA paper (Hu et al., 2021)
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix F.2

## LoRA Dropout — SFT-LoRA Baseline
- **Value**: 0.1
- **Rationale**: Standard dropout for regularization during LoRA fine-tuning
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 8

## LoRA Learning Rate — SFT-LoRA Baseline
- **Value**: 2e-4
- **Rationale**: Standard learning rate for LoRA fine-tuning of large MoE models
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Table 8

## LoRA Weight Decay — SFT-LoRA Baseline
- **Value**: 0.001
- **Rationale**: Light regularization for LoRA fine-tuning
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 8

## LoRA Batch Size per GPU — SFT-LoRA Baseline
- **Value**: 8 per GPU (4 GPUs = 32 effective)
- **Rationale**: Memory-constrained batch size for Mixtral-8×7B on A100-80GB
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Table 8

## LoRA Max Gradient Norm — SFT-LoRA Baseline
- **Value**: 0.3
- **Rationale**: Gradient clipping for training stability with large MoE model
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Table 8

## LoRA Optimizer — SFT-LoRA Baseline
- **Value**: Paged AdamW 32bit
- **Rationale**: Memory-efficient optimizer for large model fine-tuning on multi-GPU setup
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Table 8

## LoRA LR Scheduler — SFT-LoRA Baseline
- **Value**: Cosine
- **Rationale**: Smooth learning rate decay for fine-tuning convergence
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Table 8
