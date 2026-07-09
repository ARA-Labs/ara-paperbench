# CFG Impact on Chain-of-Thought Prompting (GSM8K)
- **Source**: Figure 3, Section 3.2
- **Caption**: "CFG impact on chain-of-thought prompting with respect to GSM8K dataset. For small CFG values, using CFG increases the percentage of chains which end in a valid answer structure while increasing the model accuracy. For large values the invalid percentage remains small but the accuracy drop."
- **Axis labels**: x-axis: CFG strength γ; y-axis: percentage (% invalid chains, % accuracy)
- **Models**: WizardLM-30B, Guanaco-65B
- **Dataset**: GSM8K

## Qualitative Pattern (exact values not provided in paper text; figure is a line plot)

| γ | Pattern for % Invalid Chains | Pattern for Accuracy |
|---|------------------------------|----------------------|
| 1.0 (baseline) | Higher invalid % | Baseline accuracy |
| 1.1 | Decreasing invalid % | Increasing accuracy |
| 1.25 | Further decreasing invalid % | Near-peak accuracy |
| 1.5 | Near-minimum invalid % | Peak or near-peak accuracy |
| 1.75 | Still low invalid % | Accuracy begins declining |
| 2.0 | Low invalid % (remains small) | Significant accuracy drop |

**Note**: Exact numerical values for each γ are not reported in the paper text for this figure; the figure is a line chart described qualitatively. The key directional findings are: (1) low γ reduces invalid chains AND increases accuracy; (2) high γ maintains low invalids but hurts accuracy. See Tables 14 and 15 for qualitative CoT comparison examples.

## Additional Context: AQuA Dataset (Figure 15/Appendix C.4)
- Similar pattern observed on AQuA with both WizardLM-30B and Guanaco-65B
- The paper notes these results "support our finding that using CFG increases the percentage of CoT which results in a valid answer and boost the model performances" at low γ
