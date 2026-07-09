# Training Hyperparameters

## Learning Rate (GLUE small tasks: MRPC, CoLA, RTE, STSB)
- **Value**: 2e-4
- **Rationale**: Follows CoFi (Xia et al., 2022) hyperparameter settings for small GLUE tasks.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Learning Rate (GLUE big tasks: MNLI, SST2, QNLI, QQP)
- **Value**: 2e-4
- **Rationale**: Follows CoFi (Xia et al., 2022) hyperparameter settings for big GLUE tasks.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Learning Rate (SQuAD)
- **Value**: 2e-4
- **Rationale**: Consistent with GLUE settings; follows CoFi.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Learning Rate (CNN/DM)
- **Value**: 1e-4
- **Rationale**: Lower LR for generation tasks with T5; prevents overfitting on summarization.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Learning Rate (Alpaca / LLaMA instruction tuning)
- **Value**: 1e-4
- **Rationale**: Lower LR appropriate for large model fine-tuning; avoids destabilizing the pre-pruned model.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Batch Size (GLUE small and big, SQuAD)
- **Value**: 32
- **Rationale**: Standard batch size for encoder-only model fine-tuning; follows CoFi.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: Table 6, §A (Appendix A)

## Batch Size (CNN/DM)
- **Value**: 16
- **Rationale**: Smaller batch for generation tasks due to longer sequence lengths.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: Table 6, §A (Appendix A)

## Batch Size (Alpaca)
- **Value**: Not specified in paper (Table 6 columns for Alpaca are not fully filled in the text)
- **Rationale**: Not specified in paper
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Total Epochs (GLUE, SQuAD) — Non-FT Methods
- **Value**: 40 (20 distillation + 20 fine-tuning recovery)
- **Rationale**: Follows CoFi two-phase training; 20 epochs for pruning with distillation, 20 for recovery.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Total Epochs (CNN/DM) — Non-FT Methods
- **Value**: 16 (6 distillation + 10 fine-tuning recovery)
- **Rationale**: Fewer epochs for generation tasks; 6 distillation, 10 recovery.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: Table 6, §A (Appendix A)

## Total Epochs (Fine-Tuning Baseline)
- **Value**: 10
- **Rationale**: Standard fine-tuning epochs; no pruning or distillation required.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: §A (Appendix A)

## Total Epochs (Alpaca / LLaMA)
- **Value**: 15 (after pre-tuning pruning; can be reduced in practice)
- **Rationale**: Ensures convergence after pre-tuning pruning; note the paper states these can be reduced.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §A (Appendix A)

## Distillation Loss Weight μ
- **Value**: Linear from 0 to 1 during the distillation (pruning) phase
- **Rationale**: Starts at 0 (pure task loss) to allow initial adaptation, ends at 1 (pure distillation) to encourage knowledge transfer as pruning stabilizes.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §4.4 (Equation 7)

## Layer Distillation Weight (GLUE)
- **Value**: L_distill = L_pred + 0.9 × L_layer
- **Rationale**: Layer distillation weighted at 0.9 dominates; prediction distillation at 1.0 weight.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §4.4, Appendix

## Layer Distillation Weight (SQuAD, CNN/DM)
- **Value**: L_distill = 0.1 × L_pred + 0.9 × L_layer
- **Rationale**: Reduced prediction distillation weight for generation/QA tasks; layer distillation remains dominant.
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §4.4, Appendix

## Mask Decay Rate (α)
- **Value**: 0.01
- **Rationale**: Gradual mask decay prevents abrupt parameter removal that destabilizes training.
- **Search range**: Not searched
- **Sensitivity**: high
- **Source**: §C (Appendix C)

## EMA Decay for Salience (β)
- **Value**: 0.85
- **Rationale**: Smooths noisy single-batch salience estimates across recent steps; adopted from AdaLoRA (Zhang et al., 2023b).
- **Search range**: Not searched
- **Sensitivity**: medium
- **Source**: §A (Appendix A)

## Initial Adapter Rank (r_apt initial)
- **Value**: 8
- **Rationale**: Moderate initial capacity; grows adaptively. Starting ranks > 64 degrade performance (Figure 5a).
- **Search range**: Analyzed: {8, 16, 32, 64, 128, 256} in Figure 5a
- **Sensitivity**: medium
- **Source**: §A (Appendix A), Figure 5a

## LoRA Scaling Factor (s)
- **Value**: 2 (static)
- **Rationale**: Follows LoRA's implementation; set statically.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: §4.1, §A (Appendix A)

## Time-to-Accuracy Threshold (TTA)
- **Value**: 97% of fully fine-tuned model's performance
- **Rationale**: Captures training efficiency at high performance rather than final performance; standard training benchmark metric.
- **Search range**: Not applicable
- **Sensitivity**: medium
- **Source**: §5.3

## Inference Batch Size (Small Models)
- **Value**: 128
- **Rationale**: Large batch for throughput measurement on smaller models.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: §5.3

## Inference Batch Size (LLaMA 7B)
- **Value**: 32
- **Rationale**: Reduced batch size due to large model memory footprint.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: §5.3

## Inference Batch Size (LLaMA 13B)
- **Value**: 4
- **Rationale**: Very small batch due to 13B model size.
- **Search range**: Not searched
- **Sensitivity**: low
- **Source**: §5.3
