---
# Environment

## Python
- **Version**: Not specified in paper

## Framework
- **PyTorch**: Not specified in paper
- **HuggingFace Transformers**: Used for model loading (implied by model sources)

## Evaluation Framework
- **Language Model Evaluation Harness**: EleutherAI LM Evaluation Harness (github.com/EleutherAI/lm-evaluation-harness); Gao et al. 2021 [33]
- **HumanEval**: openai/human-eval (github.com/openai/human-eval)
- **FLOP Computation**: Based on google-research/electra FLOP computation script

## Hardware
- **Zero-shot benchmarks (GPT-2, Pythia, LLaMA)**: CoreWeave and Stability AI computing cluster (mentioned in Acknowledgements)
- **Human evaluation hosting**: Custom platform (built by Guillaume Sanchez)
- **Exact GPU specifications**: Not specified in paper

## Key Dependencies
- **lm-evaluation-harness**: EleutherAI, github.com/EleutherAI/lm-evaluation-harness (version not specified)
- **scipy**: Used for entropy computation (H(p) = -Σₖ pₖ log pₖ, equivalent to scipy implementation; mentioned in addendum)
- **ANCOVA**: Statistical analysis per Rutherford [67] ("ANOVA and ANCOVA: a GLM approach")

## Analysis Datasets
- **P3**: bigscience/P3 on HuggingFace; 32,902 datapoints sampled
- **Open-Assistant Dataset**: [42] (Köpf et al. 2023); used as secondary validation
- **Redpajama-3b**: Together.xyz Redpajama model family; used as secondary validation

## Random Seeds
- **Not specified in paper**

## Compute Credits
- Stability AI and CoreWeave provided compute for evaluations (per Acknowledgements)
- Bloomberg News PhD fellowship (Alexander Spangher)
