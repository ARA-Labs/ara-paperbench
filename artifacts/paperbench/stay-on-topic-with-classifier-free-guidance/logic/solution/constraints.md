---
# Constraints and Limitations

## Boundary Conditions

### BC1: Gamma Must Be Task-Tuned
- **Condition**: The optimal γ value varies significantly across tasks and prompting paradigms.
- **Evidence**: Zero-shot tasks work well with γ=1.5; CoT tasks degrade at γ>1.5; assistant tasks peak at γ=3; machine translation works best at γ∈[1.1, 1.25].
- **Implication**: CFG cannot be applied with a single fixed γ across all tasks; requires exploration/tuning per application.

### BC2: High Gamma Degrades Quality
- **Condition**: γ values too high (task-dependent) reduce output diversity and quality.
- **Evidence**: HumanEval pass@k degrades at γ≥1.5 for k=100; CoT accuracy drops at γ>1.5; assistant tasks degrade at γ≥4.
- **Implication**: There is an optimal γ range per task; overstepping it harms performance.

### BC3: Limited Benefit for Short-Continuation Tasks
- **Condition**: In zero-shot benchmarks where desired continuations are 1-2 tokens, the main benefit of CFG is variance reduction, not long-range coherence.
- **Evidence**: Section 3.1 acknowledges risks of meandering are low in short-answer settings; improvements are primarily in entropy reduction.
- **Implication**: For very short continuations, alternative methods may be equally effective with less overhead.

### BC4: Inconsistent on ARC-Challenge and WinoGrande
- **Condition**: CFG with γ=1.5 does not consistently improve ARC (challenge) and WinoGrande benchmarks.
- **Evidence**: Figure 2 / Tables 2a, 2b show mixed results on these two benchmarks; authors note "reasons for these discrepancies are still unknown."
- **Implication**: CFG may not universally benefit all reasoning task types; adversarially constructed datasets may resist CFG.

### BC5: Already-Tuned Models May Not Benefit
- **Condition**: Models that are already at the "pinnacle" of zero-shot performance (e.g., mT0 prompt-tuned model) show no significant CFG gains.
- **Evidence**: Table 11 shows mT0 does not benefit from CFG on machine translation; 1-shot Bloom-3B also shows no benefit.
- **Implication**: CFG's benefit is largest when there is a gap between prompt adherence and model's default behavior; already well-aligned models may not improve.

### BC6: 2× Inference Cost
- **Condition**: CFG requires two forward passes per token, approximately doubling compute.
- **Evidence**: Section 4 explicitly calculates FLOPs; this is the key trade-off analyzed.
- **Implication**: For compute-constrained (not VRAM-constrained) deployments, running a larger model may be preferable. VRAM advantage of CFG+small model is significant.

## Known Limitations (from paper)

- **Security risk**: CFG has not been tested against prompt injection attacks; increased prompt adherence could amplify malicious prompts.
- **Alignment risk**: CFG's effects on alignment-breaking prompts are unknown; potential for misuse as a tool to override safety guardrails.
- **Theoretical incompleteness**: The exact mechanism by which CFG affects generation quality is not fully understood; authors note this as future work.
- **No LLaMA-family CoT/Code evaluation**: LLaMA models are only evaluated zero-shot; CoT uses WizardLM/Guanaco, code uses CodeGen.
- **Human evaluation scope**: Only chatbot-style prompts with GPT4All; may not generalize to other assistant models.

## Assumptions

- The unconditional distribution P(w) is well-approximated by starting from the last prompt token.
- Token logits form a semantically structured space where arithmetic interpolation is meaningful.
- Prompt adherence is generally beneficial for downstream task performance.
