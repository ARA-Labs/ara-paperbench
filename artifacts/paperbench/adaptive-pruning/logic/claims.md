# Claims

## C01: APT Maintains ~98% Task Performance Under 60% Sparsity on RoBERTa and T5
- **Statement**: APT maintains up to 98% of the fully fine-tuned model's task performance when pruning 60% of parameters in RoBERTa-base and T5-base models across GLUE (MNLI, SST2) and CNN/DM tasks.
- **Status**: supported
- **Falsification criteria**: APT achieves less than 96% relative performance (compared to FT) at 60% sparsity on MNLI, SST2, or CNN/DM for RoBERTa or T5.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: task performance, sparsity, RoBERTa, T5, GLUE

## C02: APT Trains 8× Faster Than LoRA+Prune Baseline
- **Statement**: APT converges 8.4× faster than LoRA+Prune for RoBERTa and 8.2× faster for T5 at 60% sparsity, measured by 97% Time-to-Accuracy (TTA) on SST2.
- **Status**: supported
- **Falsification criteria**: The ratio of LoRA+Prune TTA to APT TTA is less than 6× for either RoBERTa or T5 at 60% sparsity.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: training efficiency, time-to-accuracy, RoBERTa, T5

## C03: APT Achieves On-Par Distillation Performance With 41.6% Training Memory
- **Statement**: APT reaches comparable task accuracy to the Prune+Distill (CoFi) baseline (within 0.9 points on MNLI, same on SST2) while using only 41.6% training memory and converging 2.5× faster.
- **Status**: supported
- **Falsification criteria**: APT's training memory exceeds 60% of Prune+Distill's, or APT's task accuracy is more than 2 points below Prune+Distill on MNLI or SST2.
- **Proof**: [E01, E04]
- **Dependencies**: C01
- **Tags**: self-distillation, training memory, RoBERTa

## C04: Outlier-Aware Salience (Kurtosis) Is Critical for Large LM Pruning
- **Statement**: Removing the kurtosis component from the outlier-aware salience score causes LLaMA2-7B average performance to drop from 50.0 to 38.1 (a 23.8% reduction) at 30% sparsity.
- **Status**: supported
- **Falsification criteria**: Removing kurtosis from salience causes less than 5% relative performance drop on LLaMA2-7B at 30% sparsity.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: salience scoring, kurtosis, outlier parameters, LLaMA

## C05: Adaptive Tuning (Dynamic Rank Growth) Substantially Improves Training Speed and Task Performance
- **Statement**: Ablating adaptive tuning (static ranks instead of dynamic rank growth in salient layers) degrades RoBERTa SST2 performance from 94.5 to 93.2 and MNLI from 86.4 to 84.5, and slows convergence by 16% relative to full APT.
- **Status**: supported
- **Falsification criteria**: Ablating adaptive tuning changes RoBERTa task performance by less than 0.5 points or does not slow convergence.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: adaptive tuning, rank growth, ablation, RoBERTa

## C06: APT Preserves 86.4% LLaMA Performance With 70% Parameters Remaining
- **Statement**: APT maintains 86.4% of LoRA-tuned LLaMA2-7B average performance (50.0 vs 57.9 on ARC/HellaSwag/MMLU/TruthfulQA average) at 30% sparsity with 75.8% training memory relative to LoRA.
- **Status**: supported
- **Falsification criteria**: APT achieves less than 80% relative performance of LoRA-tuned LLaMA2-7B at 30% sparsity, or training memory exceeds 90% of LoRA.
- **Proof**: [E02]
- **Dependencies**: C04
- **Tags**: LLaMA, large LM, inference efficiency, memory

## C07: APT Outperforms LLMPruner With 30% of Its Training Memory
- **Statement**: For LLaMA2-7B at 30% sparsity, APT outperforms LLMPruner (50.0 vs 42.9 average performance) while using only ~30% of LLMPruner's training memory (APT: <24 GB; LLMPruner: ~80 GB).
- **Status**: supported
- **Falsification criteria**: APT uses more than 40% of LLMPruner's training memory, or APT's average performance is within 2 points of LLMPruner's.
- **Proof**: [E02]
- **Dependencies**: C06
- **Tags**: LLaMA, LLMPruner, memory efficiency, task-specific pruning

## C08: APT Achieves Superior Inference Efficiency vs LoRA+Prune at Same Task Accuracy
- **Statement**: At the same target task performance on RoBERTa, APT achieves 21.8% faster inference and 7% more memory reduction than LoRA+Prune; for T5 at 97% dense model performance, APT achieves 62.7% more inference speedup and 24.8% more memory reduction.
- **Status**: supported
- **Falsification criteria**: APT's inference speedup at comparable task accuracy is not statistically significantly better than LoRA+Prune on both RoBERTa and T5.
- **Proof**: [E05]
- **Dependencies**: C01, C02
- **Tags**: inference efficiency, Pareto frontier, sparsity analysis
