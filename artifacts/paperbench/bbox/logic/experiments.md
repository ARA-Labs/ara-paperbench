# Experiments

## E01: Main Performance Evaluation on GPT-3.5-turbo
- **Verifies**: C01, C06
- **Setup**:
  - Model: gpt-3.5-turbo (via Microsoft Azure OpenAI API); Adapter: deberta-v3-base (86M) and deberta-v3-large (304M) for StrategyQA/GSM8K/ScienceQA; bert-base-cased (110M) for TruthfulQA
  - Hardware: NVIDIA A100-SXM4-80GB GPU; AMD EPYC 7702 64-Core CPU
  - Dataset: StrategyQA (229 test), GSM8K (1319 test), TruthfulQA (100 test), ScienceQA (500 test)
  - System: Azure OpenAI API for GPT-3.5-turbo; HuggingFace transformers for adapter
- **Procedure**:
  1. Run CoT baseline: prompt gpt-3.5-turbo with dataset-specific few-shot CoT prompts (2-shot for StrategyQA, 4-shot for GSM8K, 1-shot for ScienceQA, instruction-only for TruthfulQA); record accuracy/True+Info
  2. Run Azure-SFT: upload training data to Azure OpenAI fine-tuning API with 3 epochs; evaluate fine-tuned model on test sets
  3. Train BBOX-ADAPTER (Ground-Truth): initialize adapter randomly; run T=3 online adaptation iterations; each iteration samples M candidates, selects best via ground-truth answer match, trains adapter with NCE loss (lr=5e-6, batch=64, 6000 steps, AdamW wd=0.01); evaluate on test sets with beam size k=3
  4. Train BBOX-ADAPTER (AI Feedback): same as above but positive sample selection uses GPT-4 as judge based on coherency, reasonability, correctness, and format criteria; no ground-truth labels used
  5. Train BBOX-ADAPTER (Combined): augment ground-truth positives with AI-feedback-selected candidates
  6. Evaluate all variants; compute accuracy (StrategyQA, GSM8K, ScienceQA) and True+Info (TruthfulQA)
  7. Report best performance across 0.1B and 0.3B adapter sizes
- **Metrics**: Accuracy (%) for StrategyQA, GSM8K, ScienceQA; True+Info (%) for TruthfulQA; delta (%) over base CoT
- **Expected outcome**:
  - BBOX-ADAPTER (all settings) outperforms the CoT baseline on all four datasets
  - Combined > Ground-Truth ≈ AI Feedback in overall performance
  - AI Feedback achieves competitive performance with Ground-Truth despite having no access to labels
  - Azure-SFT serves as upper bound and outperforms BBOX-ADAPTER on most tasks
- **Baselines**: gpt-3.5-turbo CoT, Azure-SFT
- **Dependencies**: none

## E02: Plug-and-Play Transfer Evaluation
- **Verifies**: C05
- **Setup**:
  - Model: davinci-002 (OpenAI API) and Mixtral-8×7B (HuggingFace `mistralai/Mixtral-8x7B-v0.1`, half-precision); Plugger: BBOX-ADAPTER trained on gpt-3.5-turbo (from E01)
  - Hardware: NVIDIA A100-SXM4-80GB GPU (for Mixtral-8×7B)
  - Dataset: StrategyQA (229 test), GSM8K (1319 test), TruthfulQA (100 test)
  - System: No retraining of adapter; direct plug-in from E01
- **Procedure**:
  1. Load the BBOX-ADAPTER trained for gpt-3.5-turbo adaptation (E01, Combined setting)
  2. Evaluate unadapted davinci-002 on StrategyQA, GSM8K, TruthfulQA with CoT prompts; record base accuracy
  3. Apply the gpt-3.5-turbo adapter to davinci-002 generation using adapted inference (beam search, k=3); record adapted accuracy
  4. Evaluate unadapted Mixtral-8×7B on the same three datasets; record base accuracy
  5. Apply the gpt-3.5-turbo adapter to Mixtral-8×7B generation; record adapted accuracy
  6. Compute per-dataset delta and average improvement
- **Metrics**: Accuracy (%) and True+Info (%) per dataset; delta (%) over unadapted base; average delta across 3 datasets
- **Expected outcome**:
  - Plugged davinci-002 outperforms unadapted davinci-002 on all three datasets
  - Plugged Mixtral-8×7B outperforms unadapted Mixtral-8×7B on all three datasets
  - Improvements demonstrate that adapter is portable without retraining
- **Baselines**: davinci-002 (unadapted), Mixtral-8×7B (unadapted)
- **Dependencies**: E01

## E03: Cost Analysis
- **Verifies**: C02, C03
- **Setup**:
  - Model: gpt-3.5-turbo; Adapter: deberta-v3-base (0.1B) and deberta-v3-large (0.3B)
  - Hardware: Azure OpenAI API; NVIDIA A100-SXM4-80GB (adapter training)
  - Dataset: StrategyQA (229 test), GSM8K (1319 test)
  - System: Azure OpenAI API with gpt-3.5-turbo-1106 pricing; cost tracked via API token consumption statistics
- **Procedure**:
  1. Record Azure-SFT training cost ($) for StrategyQA and GSM8K
  2. Record Azure-SFT inference cost ($/1k questions) for StrategyQA and GSM8K
  3. Record BBOX-ADAPTER (single-step) training cost ($) and inference cost ($/1k questions)
  4. Record BBOX-ADAPTER (full-step, k=3) training cost ($) and inference cost ($/1k questions)
  5. Aggregate total token consumption from Azure API; apply per-token cost (gpt-3.5-turbo-1106 pricing)
  6. Compute cost ratios (SFT / BBOX-ADAPTER) for training and inference
  7. Record accuracy under each regime
- **Metrics**: Training cost ($); inference cost ($/1k questions); accuracy (%); training cost ratio; inference cost ratio
- **Expected outcome**:
  - BBOX-ADAPTER full-step reduces training cost substantially compared to Azure-SFT
  - BBOX-ADAPTER single-step reduces inference cost more than full-step (due to no beam search)
  - Full-step variant achieves higher performance than single-step but at higher inference cost
  - Performance improvement per dollar heavily favors BBOX-ADAPTER
- **Baselines**: Azure-SFT (Peng et al., 2023), gpt-3.5-turbo CoT
- **Dependencies**: E01

## E04: White-Box Extension (Mixtral-8×7B)
- **Verifies**: C01 (generalizability)
- **Setup**:
  - Model: Mixtral-8×7B (HuggingFace `mistralai/Mixtral-8x7B-v0.1`, half-precision); Adapter: BERT-0.1B as backend; Baseline: SFT-LoRA (r=128 for 0.1B, r=384 for 0.3B; α=2r)
  - Hardware: 4× NVIDIA A100-SXM4-80GB GPUs (for LoRA training)
  - Dataset: StrategyQA (229 test)
  - System: HuggingFace peft + transformers; Mixtral treated as black-box (output-only access)
- **Procedure**:
  1. Evaluate base Mixtral-8×7B (no adaptation) on StrategyQA; record accuracy and VRAM
  2. Fine-tune Mixtral-8×7B with SFT-LoRA (r=128, 3 epochs, lr=2e-4, wd=0.001, batch=8/GPU, Paged AdamW 32bit, cosine LR, max gradient norm=0.3); record accuracy and VRAM
  3. Train BBOX-ADAPTER on Mixtral-8×7B (treating it as black-box, text-output only); record accuracy and VRAM
  4. Compare accuracy and VRAM usage across all three conditions
- **Metrics**: Accuracy (%); VRAM usage (GiB) for training and inference
- **Expected outcome**:
  - BBOX-ADAPTER surpasses base Mixtral-8×7B by a meaningful margin
  - SFT-LoRA achieves higher accuracy than BBOX-ADAPTER (white-box advantage)
  - BBOX-ADAPTER uses less VRAM during training than SFT-LoRA
- **Baselines**: Base Mixtral-8×7B, SFT-LoRA (Hu et al., 2021)
- **Dependencies**: none

## E05: Ablation — NCE Loss vs MLM Loss
- **Verifies**: C04
- **Setup**:
  - Model: gpt-3.5-turbo; Adapter: deberta-v3-base (0.1B) and deberta-v3-large (0.3B)
  - Hardware: NVIDIA A100-SXM4-80GB
  - Dataset: StrategyQA (229 test), GSM8K (1319 test)
  - System: MLM baseline: randomly mask words in ground-truth text, train adapter on masked word prediction; score beam search candidates by probability of a randomly masked word
- **Procedure**:
  1. Train BBOX-ADAPTER with NCE loss (full-step, k=3, standard settings)
  2. Train BBOX-ADAPTER with MLM loss: generate text chunks from ground-truth, mask random words, train on masked word prediction; during inference, mask random word in each beam candidate and score by masked word probability
  3. Evaluate both variants on StrategyQA and GSM8K test sets
  4. Report accuracy for 0.1B and 0.3B adapter sizes under both loss functions
- **Metrics**: Accuracy (%) for StrategyQA and GSM8K; 0.1B and 0.3B adapter sizes separately
- **Expected outcome**:
  - NCE loss outperforms MLM loss on both datasets for both adapter sizes
  - NCE advantage is larger on StrategyQA than GSM8K
  - The ranking-based NCE more effectively captures the distributional gap between source and target domains
- **Baselines**: MLM loss variant
- **Dependencies**: none

## E06: Scale Analysis — Beam Size
- **Verifies**: C07
- **Setup**:
  - Model: gpt-3.5-turbo; Adapter: deberta-v3-base (0.1B) and deberta-v3-large (0.3B)
  - Hardware: NVIDIA A100-SXM4-80GB
  - Dataset: StrategyQA (229 test)
  - System: 2-shot prompting; beam sizes k ∈ {1, 3, 5}
- **Procedure**:
  1. Train BBOX-ADAPTER with default settings; evaluate with beam sizes k=1, 3, 5
  2. Record accuracy for each beam size and each adapter size (0.1B and 0.3B)
  3. Compute average improvement across adapter sizes from k=1 to k=5
- **Metrics**: Accuracy (%) for each (k, adapter_size) combination; average delta across adapter sizes from k=1 to k=5
- **Expected outcome**:
  - Performance increases as beam size increases from 1 to 5 for both adapter sizes
  - Average improvement from k=1 to k=5 is approximately 2.41% across adapter sizes
  - Larger beam retains more candidate sequences, enabling better exploration
- **Baselines**: Base model (no adapter), k=1 (single beam)
- **Dependencies**: E01

## E07: Scale Analysis — Online Adaptation Iterations
- **Verifies**: C08
- **Setup**:
  - Model: gpt-3.5-turbo; Adapter: deberta-v3-base (0.1B) and deberta-v3-large (0.3B)
  - Hardware: NVIDIA A100-SXM4-80GB
  - Dataset: StrategyQA (229 test)
  - System: 2-shot prompting; T ∈ {0, 1, 2, 3, 4} iterations
- **Procedure**:
  1. At T=0: evaluate randomly initialized (unfinetuned) adapter with beam search; record accuracy
  2. At T=1,2,3,4: run online adaptation for T iterations; evaluate after each iteration
  3. Record accuracy for each T and each adapter size (0.1B, 0.3B)
  4. Compare all T values against base model (no adapter)
- **Metrics**: Accuracy (%) for each (T, adapter_size) combination
- **Expected outcome**:
  - T=0 (unfinetuned adapter) performs below the base model without adapter (inaccurate scoring misguides beam search)
  - T=1 surpasses base model performance
  - Performance improves consistently from T=1 to T=3
  - T=4 shows marginal or similar improvement to T=3
- **Baselines**: Base model (CoT, no adapter)
- **Dependencies**: E01
