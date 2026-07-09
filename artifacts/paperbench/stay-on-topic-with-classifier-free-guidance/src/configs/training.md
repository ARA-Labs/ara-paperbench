---
# Training / Inference Configuration

## Guidance Strength (γ) — Zero-Shot Benchmarks
- **Value**: γ = 1.5
- **Rationale**: Empirically found to consistently improve performance across GPT-2, Pythia, and LLaMA on 7/9 zero-shot benchmarks; provides a good bias-variance tradeoff for short-continuation tasks
- **Search range**: Reported curves over γ = {1.0, 1.1, 1.25, 1.5, 1.75, 2.0} in appendix figures (Figures 8, 9, 10)
- **Sensitivity**: medium
- **Source**: Section 3.1; Figure 2

## Guidance Strength (γ) — Chain-of-Thought (CoT)
- **Value**: γ ∈ {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}
- **Rationale**: Low γ improves valid-answer rate and accuracy; high γ degrades accuracy. Optimal varies per model.
- **Search range**: {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}
- **Sensitivity**: high
- **Source**: Section 3.2; Figure 3

## Guidance Strength (γ) — HumanEval Code Generation
- **Value**: γ ∈ {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}
- **Rationale**: γ=1.1 typically maximizes pass@1 at temperature=0.2; optimal varies by model size and temperature
- **Search range**: {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}
- **Sensitivity**: high
- **Source**: Section 3.3, Table 2, Tables 5/6/7

## Sampling Temperature — HumanEval
- **Value**: {0.2, 0.6, 0.8}
- **Rationale**: Standard temperature values for pass@k evaluation; lower temperature favors pass@1, higher temperature needed for pass@100
- **Search range**: {0.2, 0.6, 0.8}
- **Sensitivity**: medium
- **Source**: Section 3.3.2, Footnote 3

## Guidance Strength (γ) — Machine Translation
- **Value**: γ ∈ {1.0, 1.05, 1.1, 1.25} (lower range than NLP benchmarks)
- **Rationale**: Translation is a structured task where even small guidance overshoots quickly; mT0 and 1-shot Bloom show degradation at γ=1.1
- **Search range**: 0-shot Bloom-3B: {1.0, 1.10, 1.25}; 1-shot Bloom-3B / mT0: {1.0, 1.05, 1.10}
- **Sensitivity**: high
- **Source**: Appendix D.1, Table 11

## Guidance Strength (γ) — Chatbot / Human Evaluation
- **Value**: Randomly chosen from {1, 2, 3, 4, 5, 6} during data collection; optimal found to be γ=3
- **Rationale**: Wider range tested for chatbot tasks since system-prompt following requires stronger emphasis; peak preference at γ=3
- **Search range**: {1, 2, 3, 4, 5, 6}
- **Sensitivity**: medium
- **Source**: Section 3.4, Figure 5

## Unconditional Prefix Construction
- **Value**: Last token of the initial prompt
- **Rationale**: In-distribution starting point that effectively drops the prompt prefix
- **Search range**: Not searched; architectural design choice
- **Sensitivity**: high
- **Source**: Section 3.1; reproduction rubric requirement

## CoT Few-Shot Prompt Format
- **Value**: Few-shot prompt and parsing setting from Wang et al. 2023 (Self-Consistency) [80]
- **Rationale**: Standard format for CoT evaluation on GSM8K and AQuA
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: Section 3.2

## Human Evaluation Sample Count
- **Value**: 25 system prompts × 46 user prompts = 1,740 combinations; 611 total votes; 71 unique voters
- **Rationale**: Broad coverage of system prompt types and user queries
- **Search range**: Fixed
- **Sensitivity**: low
- **Source**: Section 3.4, Figure 5

## P3 Dataset Sample Count
- **Value**: 32,902 datapoints
- **Rationale**: Large sample for statistical reliability of entropy and perplexity analysis
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 5
