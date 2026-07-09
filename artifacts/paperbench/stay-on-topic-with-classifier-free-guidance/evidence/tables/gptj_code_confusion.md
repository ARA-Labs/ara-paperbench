# GPT-J Code Generation Language Confusion Matrix

- **Source**: Table 12, Appendix D.2
- **Caption**: "Confusion matrix for generating code tests with GPT-J. We prompt it to generate code in some programming language (rows) and compare with the generated programming language (columns). The overall accuracy results for γ=1, 1.25, 1.5, 1.75 are 73%, 86%, 81%, 77%, respectively."
- **Conditions**: 100 samples total (5 runs × 5 prompts) per guidance strength; GPT-J-6B; γ ∈ {1.0, 1.25, 1.5, 1.75}

## Overall Accuracy by γ

| γ | Overall Accuracy |
|---|-----------------|
| 1.0 | 73% |
| 1.25 | 86% |
| 1.5 | 81% |
| 1.75 | 77% |

## Confusion Matrix (Qualitative — exact cell counts not provided in paper)

Rows = prompted language, Columns = generated language. Matrix shown for γ=1 and γ=1.25 side by side:

| Prompted \ Generated | not code | Java | Python |
|---------------------|----------|------|--------|
| Unspecified (γ=1) | — | — | — |
| Java (γ=1) | — | — | — |
| Python (γ=1) | — | — | — |
| Unspecified (γ=1.25) | — | — | — |
| Java (γ=1.25) | — | — | — |
| Python (γ=1.25) | — | — | — |

Note: Exact cell counts were not reported numerically in the paper; only the overall accuracy values are extractable. The confusion matrix (Table 12) is presented as a visual diagram showing classification paths.

## Statistical Note
- Accuracy improvement from γ=1 to γ=1.25: 73% → 86%, p-value = 0.01 (reported in Appendix D.2)
