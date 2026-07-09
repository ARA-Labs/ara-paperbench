---
# Experiment Plans

## E01: Zero-Shot NLP Benchmark Evaluation with CFG
- **Verifies**: C01, C02
- **Setup**:
  - Model: GPT-2 (small/medium/large/xl), Pythia (160M/410M/1B/1.4B/2.8B/6.9B/12B), LLaMA (7B/13B/30B/65B)
  - Hardware: High-memory GPU cluster (CoreWeave / Stability AI infrastructure)
  - Dataset: ARC-c, ARC-e, BoolQ, HellaSwag, PIQA, SciQ, TriviaQA, WinoGrande, Lambada (OpenAI) — all implemented in EleutherAI Language Model Evaluation Harness [33]
  - System: EleutherAI LM Evaluation Harness (github.com/EleutherAI/lm-evaluation-harness)
- **Procedure**:
  1. Load each model from its respective checkpoint (HuggingFace).
  2. For each model, implement CFG decoding (Eq. 7): at each step compute logits with full prompt (conditional) and with only the last prompt token (unconditional); combine as: `logits_cfg = logits_uncond + γ * (logits_cond - logits_uncond)`.
  3. Run evaluation with γ=1 (baseline, no guidance) and γ=1.5 (CFG) on all 9 benchmark datasets in zero-shot mode.
  4. For TriviaQA, use substring match (not exact match) to handle answer formatting variations.
  5. Record accuracy (or exact match, depending on dataset) for each model × γ × dataset combination.
  6. Compare γ=1 vs γ=1.5 per model per dataset.
- **Metrics**: Accuracy (%) per benchmark task; for Lambada specifically compare against PaLM-540B zero-shot SOTA
- **Expected outcome**:
  - CFG (γ=1.5) outperforms baseline (γ=1) on the majority of benchmarks across all model families
  - LLaMA-7B with CFG outperforms vanilla PaLM-540B on Lambada
  - ARC-challenge and WinoGrande may not show consistent improvements
  - Improvements are more pronounced on tasks with longer continuations
- **Baselines**: γ=1 (vanilla sampling), PaLM-540B zero-shot (external reference for Lambada)
- **Dependencies**: none

## E02: Chain-of-Thought Reasoning with CFG
- **Verifies**: C03
- **Setup**:
  - Model: WizardLM-30B, Guanaco-65B
  - Hardware: High-memory GPU cluster
  - Dataset: GSM8K (openai/gsm8k on HuggingFace), AQuA (nguyen-brat/aqua on HuggingFace)
  - System: Few-shot CoT prompts from Wang et al. 2023 (Self-Consistency paper); LM Evaluation Harness or equivalent
- **Procedure**:
  1. Load WizardLM-30B and Guanaco-65B models.
  2. Implement CFG decoding with CFG applied only to the initial task prompt $w_p$ (not the CoT chain $w_{cot}$ or answer $w_a$).
  3. Use few-shot prompt and parsing settings from Wang et al. 2023 [80] for both GSM8K and AQuA.
  4. Evaluate with guidance strengths γ ∈ {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}.
  5. For each generated chain, determine: (a) whether the chain ends with a valid parseable answer format ("The answer is ..."), (b) whether that answer is correct.
  6. Compute: % chains with valid answers, % accurate answers, % invalid chains.
  7. Plot % invalid, % valid-incorrect, % valid-correct as stacked bar per γ value.
- **Metrics**: % chains ending in valid answer (parseable), final answer accuracy on GSM8K and AQuA
- **Expected outcome**:
  - Low γ (≤1.5) increases % of chains with valid parseable answers and improves accuracy
  - High γ (>1.5) maintains low invalid rate but accuracy degrades
  - Effect consistent across WizardLM-30B and Guanaco-65B
- **Baselines**: γ=1 (no CFG, standard CoT)
- **Dependencies**: none

## E03: Code Generation (HumanEval) with CFG
- **Verifies**: C04
- **Setup**:
  - Model: CodeGen-350M-mono, CodeGen-2B-mono, CodeGen-6B-mono (Nijkamp et al. [54])
  - Hardware: GPU cluster; CodeGen-16B-mono omitted due to compute constraints
  - Dataset: HumanEval (Chen et al. [16]; 164 Python coding tasks with unit tests; openai/human-eval on GitHub)
  - System: Standard HumanEval evaluation framework
- **Procedure**:
  1. Load each CodeGen model variant.
  2. Implement CFG decoding (Eq. 7) with mutable γ parameter; unconditional prompt starts at last token of function signature + docstring prompt.
  3. Evaluate with γ ∈ {1.0, 1.1, 1.25, 1.5, 1.75, 2.0} × temperatures ∈ {0.2, 0.6, 0.8}.
  4. For each (model, γ, temperature) combination, generate k=100 samples per HumanEval problem.
  5. Compute pass@1, pass@10, pass@100 using the standard unbiased estimator.
  6. For CodeGen-350M-mono, perform task-by-task breakdown comparing γ=1 vs γ=1.25 to count wins/ties/losses.
- **Metrics**: pass@k for k=1, 10, 100 per model, guidance strength, and temperature; win/tie/loss counts per task
- **Expected outcome**:
  - Low CFG (γ ≤ 1.5) uniformly increases pass@1 compared to baseline
  - High CFG (γ ≥ 1.5) leads to deterioration
  - CFG improvement diminishes or reverses for pass@k at large k (e.g. pass@100)
  - Task-by-task: more tasks where CFG outperforms than underperforms
- **Baselines**: γ=1.0 (no CFG), temperature={0.2, 0.6, 0.8}
- **Dependencies**: none

## E04: Entropy, FLOPs, and Instruction-Tuning Comparison
- **Verifies**: C02, C06
- **Setup**:
  - Model: Falcon-7b-Base, Falcon-7b-Instruct (for analysis); GPT-2/Pythia/LLaMA families (for FLOPs)
  - Hardware: GPU cluster
  - Dataset: P3 dataset (bigscience/P3 on HuggingFace; 32,902 sampled datapoints); benchmark results from E01 (for FLOPs)
  - System: Custom analysis scripts; ANCOVA regression (log-transformed FLOP vs accuracy)
- **Procedure**:
  1. **Entropy Analysis**: Run Falcon-7b-Base with γ=1 (vanilla), γ=1.5 (CFG), and unconditional on P3 samples. Run Falcon-7b-Instruct with γ=1. At each generation step, compute entropy H(p) = -Σₖ pₖ log pₖ over vocabulary. Compare mean entropy distributions.
  2. **Top-p overlap**: For each sample, compute the set of tokens in top-p=0.9 for CFG and instruction-tuned outputs; measure overlap (inner product of indicator vectors).
  3. **Perplexity correlation**: Compute generation perplexity for P(y|x), CFG, and Instruct on P3; compute pairwise Spearman correlation. Test correlation between perplexity and top-p overlap.
  4. **FLOPs analysis**: Calculate inference FLOPs per token for each model from E01 (using electra FLOP computation formula); with CFG, FLOPs double. Pair FLOP count with benchmark accuracy from E01.
  5. **ANCOVA**: Run ANCOVA regression on log-FLOP vs accuracy for CFG group vs vanilla group; determine significance at p=0.01.
- **Metrics**: Mean logit entropy per condition; top-p=0.9 vocabulary overlap fraction; Spearman correlation (rs) and p-value; ANCOVA p-value per benchmark task
- **Expected outcome**:
  - CFG entropy is significantly lower than vanilla and comparable to instruction-tuned
  - CFG and instruction-tuned top-p distributions overlap less than 30%
  - CFG matches the performance of a 2x-sized vanilla model on majority of tasks
  - Perplexity correlation between CFG and instruction-tuned models is low overall but higher for longer prompts
- **Baselines**: Vanilla P(y|x), unconditional P(y), instruction-tuned Pinstruct(y|x)
- **Dependencies**: E01

## E05: Negative Prompting for Assistant Task Human Evaluation
- **Verifies**: C05
- **Setup**:
  - Model: GPT4All-J v1.3-jazzy
  - Hardware: CPU/GPU (GPT4All is designed for consumer hardware)
  - Dataset: 25 system prompts × 46 user prompts = 1,740 sampled combinations (Appendix G)
  - System: Custom platform built by Guillaume Sanchez; blind pairwise human preference evaluation
- **Procedure**:
  1. For each of 1,740 (system-prompt, user-prompt) combinations: generate one completion with vanilla sampling (γ=1) and one with CFG, using a guidance strength randomly chosen from {1, 2, 3, 4, 5, 6}.
  2. For CFG: set negative prompt $\bar{c}$ = default system prompt ("The prompt below is a question to answer..."); set positive prompt $c$ = modified system prompt (e.g., "...write a sad response").
  3. Present both completions blindly to human evaluators; ask two questions: (A) which better follows system prompt, (B) which better follows user prompt.
  4. Collect votes; analyze preference rate as function of γ.
  5. Find peak system-prompt preference γ and check user-prompt preference degradation.
- **Metrics**: % preference for CFG over vanilla on (A) system-prompt following and (B) user-prompt relevance, per γ value; total vote count; unique voter count
- **Expected outcome**:
  - CFG significantly preferred for system-prompt following (>60% preference) at optimal γ
  - User-prompt relevance not significantly degraded at optimal γ (preference ≈ 50%)
  - Clear peak in system-prompt preference at intermediate γ value
- **Baselines**: Vanilla sampling (γ=1)
- **Dependencies**: none
