# Experiment Plans

## E01: Main Results — RoBERTa and T5 Pruning at 60% Sparsity
- **Verifies**: C01, C02, C03
- **Setup**:
  - Model: RoBERTa-base (125M params), T5-base (250M params, t5-lm-adapt variant)
  - Hardware: Single A100 GPU
  - Dataset: MNLI and SST2 from GLUE benchmark (dev set accuracy); SQuAD v2.0 (dev set F1) for RoBERTa; CNN/DM (ROUGE 1/2/L) for T5
  - System: APT with self-distillation, cubic sparsity schedule to 60% target sparsity; inference batch size 128
- **Procedure**:
  1. Load RoBERTa-base (or T5-base, t5-lm-adapt) and insert APT adapters in query/value MHA layers and FFN up-projection layers; initialize adapter ranks to 8.
  2. Run the pruning phase (20 epochs) with self-distillation objective; apply cubic sparsity schedule targeting γ_T=0.6; adaptively grow ranks in top-half salient adapters; update masks with α=0.01.
  3. Run the fine-tuning phase (20 epochs) without distillation on the task objective.
  4. Measure 97% TTA (seconds) for training speed; measure peak GPU memory (MB) during training.
  5. Merge APT adapter weights into frozen parameters; run inference at batch size 128; measure throughput (samples/second) and peak GPU memory.
  6. Repeat for baselines: FT (10 epochs), LoRA (40 epochs), LoRA+Prune (LoRA fine-tune then Mask Tuning + retrain), Prune+Distill (CoFi, RoBERTa only), LoRA+Prune+Distill (CoFi with LoRA-only tunable params).
  7. Normalize all training and inference metrics relative to FT baseline.
- **Metrics**: Dev accuracy (MNLI, SST2), dev F1 (SQuAD v2), ROUGE 1/2/L (CNN/DM); 97% TTA (seconds); peak training memory (MB); inference throughput (samples/sec); peak inference memory (MB); all efficiency metrics normalized to FT.
- **Expected outcome**:
  - APT should achieve substantially higher accuracy than LoRA+Prune at the same 60% sparsity
  - APT should converge much faster (by roughly an order of magnitude) than LoRA+Prune
  - APT should achieve comparable accuracy to Prune+Distill while using dramatically less training memory and time
  - APT's inference efficiency should be similar to or better than LoRA+Prune (both achieve similar parameter reduction)
- **Baselines**: FT, LoRA, LoRA+Prune, Prune+Distill (RoBERTa only), LoRA+Prune+Distill (RoBERTa only)
- **Dependencies**: none

## E02: LLaMA2-7B Pruning at 30% Sparsity
- **Verifies**: C06, C07
- **Setup**:
  - Model: LLaMA2 7B (7 billion parameters)
  - Hardware: Single A100 GPU; APT costs <24 GB for pruning; LLMPruner costs ~80 GB
  - Dataset: GPT-4 generated Alpaca dataset (instruction following); evaluation on Open LLM Leaderboard tasks: 25-shot ARC, 10-shot HellaSwag, 5-shot MMLU, 0-shot TruthfulQA
  - System: APT without distillation (distillation-free for large LMs to reduce memory); fine-tune pruned model for 15 epochs; inference batch size 32
- **Procedure**:
  1. Load LLaMA2-7B; insert APT adapters on query/value MHA layers; initialize adapter ranks to 8.
  2. Run pre-tuning pruning to target sparsity γ_T=0.3 (30% pruned, 70% remaining) using outlier-aware salience with kurtosis.
  3. Fine-tune the pruned model on Alpaca for 15 epochs with LR=1e-4, batch size=Not specified in Table 6 for Alpaca.
  4. Measure training time per step (seconds) and peak training memory (MB) relative to LoRA baseline.
  5. Evaluate on ARC, HellaSwag, MMLU, TruthfulQA using lm-eval-harness; report individual and average scores.
  6. Measure inference time (ms) and peak inference memory (MB) relative to LoRA baseline.
  7. Repeat for baselines: LoRA (no pruning), LoRA+Prune (LoRA fine-tune + Mask Tuning), LLMPruner (task-agnostic pruning + LoRA recovery).
- **Metrics**: ARC (25-shot), HellaSwag (10-shot), MMLU (5-shot), TruthfulQA (0-shot) accuracy; average across four tasks; training time per step (s); peak training memory (MB); inference time (ms); peak inference memory (MB); all normalized to LoRA.
- **Expected outcome**:
  - APT should substantially outperform LLMPruner on average accuracy despite using far less training memory
  - APT should use less training memory than LoRA while LoRA+Prune uses similar or more memory than LoRA
  - APT should achieve better TruthfulQA scores than all baselines
  - Without distillation, APT's performance gap vs LoRA should be larger than for smaller models
- **Baselines**: LoRA, LoRA+Prune, LLMPruner
- **Dependencies**: none

## E03: Ablation Study — Components of APT
- **Verifies**: C04, C05
- **Setup**:
  - Model: RoBERTa-base (for AP, AT, DS ablations), LLaMA2-7B (for kurtosis and AT ablations)
  - Hardware: Single A100 GPU
  - Dataset: MNLI and SST2 (RoBERTa); ARC, HellaSwag, MMLU, TruthfulQA (LLaMA)
  - System: Ablations: (a) w/o AP — remove adaptive pruning, use only adaptive tuning; (b) w/o AT — static LoRA ranks instead of dynamic growth; (c) w/o DS — remove self-distillation loss; (d) w/o kurtosis — use activation-gradient salience only without kurtosis term; (e) w/o salience — use uniform pruning instead of salience-based allocation
- **Procedure**:
  1. Train full APT with 60% sparsity target on RoBERTa (MNLI, SST2) as the reference.
  2. Train APT w/o AP: use only adaptive tuning (no pruning masks); inference efficiency same as FT/LoRA.
  3. Train APT w/o AT: fix LoRA ranks at initial value (8) throughout training; no rank growth in salient layers.
  4. Train APT w/o DS: remove the self-distillation loss (L_ft only); keep adaptive pruning and tuning.
  5. Train APT w/o salience: use uniform pruning allocation instead of salience-based ranking.
  6. Train APT w/o kurtosis: use activation-gradient salience only, omit the kurtosis term.
  7. For LLaMA2-7B: test APT w/o AP (no pruning) and APT w/o kurtosis at 30% sparsity; APT w/o AT at 30% and 50% sparsity.
  8. Measure SST2/MNLI accuracy, TTA, peak training memory for RoBERTa ablations; measure ARC/HellaSwag/MMLU/TruthfulQA/avg for LLaMA ablations.
- **Metrics**: Task accuracy (MNLI, SST2 for RoBERTa; 4 tasks + avg for LLaMA); 97% TTA relative to FT (RoBERTa); peak training memory relative to FT (RoBERTa); relative training memory to LoRA (LLaMA).
- **Expected outcome**:
  - Removing adaptive pruning (w/o AP) should preserve accuracy but eliminate inference efficiency benefit; training should be faster but higher memory for large LMs
  - Removing adaptive tuning (w/o AT) should substantially degrade accuracy (comparable to LoRA+Prune baseline) and slow convergence
  - Removing self-distillation (w/o DS) should degrade accuracy and speed up training with slightly lower memory
  - Removing kurtosis should severely degrade LLaMA performance but have smaller impact on smaller models
  - Removing salience-based allocation should degrade accuracy compared to full APT
- **Baselines**: Full APT
- **Dependencies**: E01, E02

## E04: Distillation Strategy Comparison
- **Verifies**: C03
- **Setup**:
  - Model: RoBERTa-base
  - Hardware: Single A100 GPU
  - Dataset: SST2
  - System: Comparison of APT's self-distillation vs traditional knowledge distillation strategies
- **Procedure**:
  1. Train APT with full self-distillation (reference).
  2. Train APT w/o layer distillation (ablate L_layer, keep L_pred).
  3. Train APT without any distillation objective (L_ft only).
  4. Train APT with FT teacher: use a separately converged full fine-tuning model as teacher; combine teacher time + student time for total training time.
  5. Train APT with LoRA teacher: use a separately converged LoRA-tuned model as teacher.
  6. Report SST2 accuracy, relative training speed (vs FT), relative training memory (vs FT).
- **Metrics**: SST2 accuracy; training speed relative to dense FT; training memory relative to dense FT.
- **Expected outcome**:
  - Self-distillation should be substantially faster than using separately trained teachers (FT teacher or LoRA teacher)
  - Self-distillation should use less memory than FT teacher approach (which roughly doubles GPU memory)
  - Removing distillation entirely should be faster and use less memory but degrade accuracy
  - Layer mapping ablation should moderately degrade accuracy with negligible efficiency impact
- **Baselines**: APT w/o L_layer, APT w/o distillation, FT teacher, LoRA teacher
- **Dependencies**: E01

## E05: Sparsity Analysis — Performance vs Inference Efficiency Pareto Curves
- **Verifies**: C08
- **Setup**:
  - Model: RoBERTa-base, T5-base, LLaMA2-7B
  - Hardware: Single A100 GPU
  - Dataset: MNLI and SST2 (RoBERTa, T5, averaged); Alpaca/Open LLM Leaderboard (LLaMA)
  - System: APT trained at multiple target sparsities; inference efficiency measured post-merge
- **Procedure**:
  1. Train APT on RoBERTa at sparsities: 40%, 50%, 60%, 70%, 80%, 90%, 95%; average MNLI/SST2 dev accuracy.
  2. Train APT on T5 at sparsities: 40%, 50%, 60%, 70%, 80%, 90%; average MNLI/SST2 dev accuracy.
  3. Train baselines (LoRA+Prune, Prune+Distill, LoRA+Prune+Distill for RoBERTa; LoRA+Prune for T5) at multiple sparsities.
  4. Measure inference speedup (relative to FT or LoRA) and inference memory reduction for each (model, method, sparsity) triple.
  5. Plot relative task accuracy vs inference speedup and vs inference memory reduction for all methods.
  6. Identify the APT sparsity setting closest to each baseline's task accuracy; compare inference efficiency at that accuracy level.
- **Metrics**: Relative task accuracy (normalized to FT dense model); inference speedup (×); inference memory reduction (relative to FT/LoRA); Pareto frontier area.
- **Expected outcome**:
  - APT should dominate the Pareto frontier: for the same task accuracy, APT should achieve higher inference speedup and lower memory than LoRA+Prune
  - For RoBERTa at same accuracy as LoRA+Prune, APT should be ~20% faster in inference and ~7% more memory-efficient
  - For T5 at 97% dense model accuracy, APT should achieve ~60% more inference speedup and ~25% more memory reduction vs LoRA+Prune
- **Baselines**: LoRA+Prune, Prune+Distill, LoRA+Prune+Distill
- **Dependencies**: E01

## E06: LLaMA2-13B Pruning and Additional BERT/GLUE Baselines
- **Verifies**: C06, C07
- **Setup**:
  - Model: LLaMA2-13B (13B parameters); BERT-base (110M, for PST/LRP comparison)
  - Hardware: Single A100 GPU
  - Dataset: Alpaca (LLaMA2-13B), full GLUE benchmark (BERT-base)
  - System: Same APT configuration as E02 for LLaMA; standard APT for BERT at 50% and 10% density settings
- **Procedure**:
  1. Apply APT to LLaMA2-13B at 30% sparsity; fine-tune on Alpaca; evaluate on ARC, HellaSwag, MMLU, TruthfulQA.
  2. Compare to LoRA, LoRA+Prune, LLMPruner on LLaMA2-13B.
  3. Apply APT to BERT-base at 50% and 10% parameter density; evaluate on 8 GLUE tasks (MNLI, QQP, QNLI, SST2, CoLA, STS-B, MRPC, RTE).
  4. Compare BERT-base results to PST (unstructured pruning + PEFT), LRP (structured pruning + PEFT), MaP, MvP baselines.
- **Metrics**: ARC, HellaSwag, MMLU, TruthfulQA, avg (LLaMA2-13B); MNLI, QQP, QNLI, SST2, CoLA, STS-B, MRPC, RTE, GLUE avg (BERT).
- **Expected outcome**:
  - APT should outperform LLMPruner on LLaMA2-13B on all four tasks
  - APT should achieve higher GLUE average than PST and LRP at both 50% and 10% density
  - Larger models (13B vs 7B) should recover better accuracy at the same sparsity
- **Baselines**: LoRA, LoRA+Prune, LLMPruner (LLaMA); MaP, MvP, PST, LRP (BERT)
- **Dependencies**: E02
