# Chain-of-Thought CFG Impact on GSM8K

- **Source**: Figure 3, Section 3.2
- **Caption**: "CFG impact on chain-of-thought prompting with respect to GSM8K dataset. For small CFG values, using CFG increases the percentage of chains which end in a valid answer structure while increasing the model accuracy. For large values the invalid percentage remains small but the accuracy drop."
- **Conditions**: WizardLM-30B and Guanaco-65B; GSM8K dataset; self-consistency CoT following Wang et al. (2023) few-shot prompt and parsing settings; γ ∈ {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}

## Qualitative Data Points (from Figure 3)

Figure 3 is a line chart showing two metrics as a function of γ. Exact data point values are not reported numerically in the paper; the following are directional descriptions:

| γ | Valid Answer Rate | Accuracy | Notes |
|---|-----------------|----------|-------|
| 1.0 | Baseline | Baseline | Standard CoT |
| 1.1 | Higher than baseline | Higher than baseline | CFG improves both |
| 1.25 | Higher than baseline | Higher than baseline | Peak or near-peak |
| 1.5 | Peak or near-peak | Near peak | Transition zone |
| 1.75 | Low invalid % | Begins to decline | Accuracy degradation starts |
| 2.0 | Low invalid % | Below baseline | Reasoning quality degraded |

## Key Qualitative Finding
- Low γ (≤1.5): CFG increases valid-answer parsing rate AND accuracy
- High γ (>1.5): Invalid % remains small (chains produce parseable answers) BUT reasoning quality degrades and accuracy drops below γ=1 baseline
- This bifurcation demonstrates that CFG enforces structural adherence (valid format) even at high γ, but over-constrains the reasoning process

## Qualitative Examples (Tables 14-15 in paper)
- Table 14: Guanaco-65B on GSM8K — vanilla CoT diverges and gives wrong answer format; CFG (γ=1.5) produces correct answer in expected format
- Table 15: WizardLM-30B on GSM8K — vanilla CoT gives wrong answer; CFG (γ=1.1) gives correct answer $36 in correct format
