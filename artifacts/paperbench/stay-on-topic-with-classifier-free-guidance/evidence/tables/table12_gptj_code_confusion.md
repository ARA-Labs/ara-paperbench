---
# Table 12 (Appendix D.2): GPT-J Code Generation Language Confusion Matrix
- **Source**: Table 12, Appendix D.2
- **Caption**: "Confusion matrix for generating code tests with GPT-J. We prompt it to generate code in some programming language (rows) and compare with the generated programming language (columns). The overall accuracy results for γ=1, 1.25, 1.5, 1.75 are 73%, 86%, 81%, 77%, respectively."
- **Model**: GPT-J-6B
- **Setup**: 100 samples (5 runs × 5 prompts per γ value); γ ∈ {1, 1.25, 1.5, 1.75}
- **Metric**: Language match accuracy; confusion between prompted language (rows) vs generated language (columns)

**Confusion Matrices (qualitative — exact cell counts not given; overall accuracy stated):**

| γ value | Overall Accuracy |
|---------|-----------------|
| 1.0 | 73% |
| 1.25 | 86% |
| 1.5 | 81% |
| 1.75 | 77% |

**Languages tested (rows = prompted, columns = generated):**
- Unspecified
- Java
- Python

**Key finding**: Optimal accuracy at γ=1.25 (86% correct language generation vs 73% baseline); accuracy improves then decreases at higher γ, with p-value 0.01 for the jump from γ=1 to γ=1.25.
