---
# Claims

## C01: CFG Improves Zero-Shot Benchmark Performance
- **Statement**: Applying CFG with γ=1.5 to GPT-2, Pythia, and LLaMA family models improves zero-shot accuracy on 7 out of 9 standard NLP benchmarks (excluding ARC-challenge and WinoGrande), with LLaMA-7B achieving 81% on Lambada (OpenAI), surpassing PaLM-540B's 77.9% SOTA.
- **Status**: supported
- **Falsification criteria**: CFG with γ=1.5 fails to improve ≥5/9 benchmarks for GPT-2 or Pythia models; or LLaMA-7B with CFG scores below 77.9% on Lambada.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: zero-shot, benchmarking, prompt-adherence, LLaMA, GPT-2, Pythia, Lambada, SOTA

## C02: CFG Matches 2× Model Size at Same Inference FLOPs
- **Statement**: Across 5 out of 9 benchmark tasks, there is a statistically insignificant difference (ANCOVA at p=0.01) between using a model with CFG (doubling inference FLOPs) and using a vanilla model twice as large; 2 tasks favor CFG and 2 favor vanilla among significant cases.
- **Status**: supported
- **Falsification criteria**: Fewer than 5/9 tasks show insignificant ANCOVA difference; or the significant-difference tasks do not split evenly.
- **Proof**: [E01, E04]
- **Dependencies**: C01
- **Tags**: compute-efficiency, FLOPs, ANCOVA, model-scaling, inference-cost

## C03: CFG Improves CoT Validity and Accuracy at Low γ
- **Statement**: At low guidance strengths (γ ≤ 1.5), CFG increases the percentage of Chain-of-Thought continuations ending in a valid parseable answer and improves overall accuracy on GSM8K and AQuA; at high γ (> 1.5), invalid chains remain rare but accuracy degrades.
- **Status**: supported
- **Falsification criteria**: CFG at γ=1.1 or γ=1.25 fails to increase valid-answer rate on GSM8K or AQuA relative to γ=1; or accuracy at γ=1.1 is lower than at γ=1.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: chain-of-thought, CoT, GSM8K, AQuA, reasoning, WizardLM, Guanaco

## C04: CFG Improves Code Generation at Low γ
- **Statement**: Low CFG (γ ≤ 1.5) uniformly increases the pass@1 rate on HumanEval for CodeGen models at temperature=0.2; high CFG (γ ≥ 1.5) leads to deterioration; improvement diminishes or harms performance at pass@k for large k.
- **Status**: supported
- **Falsification criteria**: pass@1 for CodeGen-350M-mono at γ=1.1 is not higher than at γ=1.0; or CFG outperforms baseline at pass@100.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: code-generation, HumanEval, CodeGen, pass@k, program-synthesis

## C05: CFG with Negative Prompting Improves Assistant System-Prompt Following
- **Statement**: CFG with negative prompting (negative prompt = default system prompt, positive = edited system prompt) on GPT4All-J achieves 75% human preference for system-prompt following over baseline at γ=3, without degrading user-prompt relevance (52% preference, ≈ random).
- **Status**: supported
- **Falsification criteria**: Human evaluators do not prefer CFG over baseline at ≥60% rate; or user-prompt relevance drops significantly below 50% at optimal γ.
- **Proof**: [E05]
- **Dependencies**: none
- **Tags**: negative-prompting, assistant, chatbot, human-evaluation, GPT4All, system-prompt

## C06: CFG Reduces Sampling Entropy but Differs from Instruction Tuning
- **Statement**: CFG at γ=1.5 reduces logit entropy (mean 4.7 vs 5.4 for vanilla) to a level similar to instruction-tuned models, but CFG and instruction-tuned models share less than 30% vocabulary overlap in top-p=0.9; they are not equivalent in their effect on logit distributions.
- **Status**: supported
- **Falsification criteria**: CFG entropy is not significantly lower than vanilla; or CFG and instruction-tuned models share >50% top-p vocabulary overlap.
- **Proof**: [E04]
- **Dependencies**: C01
- **Tags**: entropy, instruction-tuning, logit-analysis, vocabulary-distribution, Falcon
