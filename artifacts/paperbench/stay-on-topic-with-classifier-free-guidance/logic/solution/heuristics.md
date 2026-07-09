---
# Heuristics

## H01: Start Unconditional Prompt at Last Prompt Token
- **Rationale**: The last token of the user's prompt is in-distribution as a generation start point; it provides minimal context (essentially unconditional) while staying within the model's training distribution. Using a BOS token or random token may cause distribution mismatch.
- **Sensitivity**: high
- **Bounds**: Must be exactly one token (the last token of the prompt); do not use a full stop or special padding token unless that is naturally the last prompt token.
- **Code ref**: [src/execution/cfg_decoding.py]
- **Source**: Section 3.1, "we implement CFG by starting the unconditional prompt at the last token of the initial prompt"

## H02: Gamma of 1.5 for Zero-Shot / Short Benchmarks
- **Rationale**: γ=1.5 provides a good balance between prompt adherence and output quality for zero-shot NLP benchmarks with 1-2 token expected answers. Smaller values show less improvement; larger values risk over-constraining diversity.
- **Sensitivity**: medium
- **Bounds**: γ∈[1.1, 1.5] for zero-shot tasks; do not exceed 2.0 for short-answer benchmarks.
- **Code ref**: [src/execution/cfg_decoding.py]
- **Source**: Section 3.1; Figure 2; benchmark results comparing γ=1 vs γ=1.5

## H03: Low Gamma for CoT and Long-Form Generation
- **Rationale**: Chain-of-Thought and code generation require long, creative continuations. High γ over-constrains the search space, reducing the quality of multi-step reasoning chains while still keeping invalid-answer rate low.
- **Sensitivity**: high
- **Bounds**: γ∈[1.1, 1.5] for CoT; γ∈[1.0, 1.25] for machine translation; degrade rapidly above 1.5.
- **Code ref**: [src/execution/cfg_decoding.py]
- **Source**: Section 3.2 (CoT results), Section 3.3 (HumanEval), Appendix D.1 (machine translation)

## H04: Apply CFG Only to Prompt (Not CoT Chain)
- **Rationale**: In CoT prompting, applying CFG to the entire continuation (including the reasoning chain $w_{cot}$) would over-constrain the chain. The insight is that only the initial task prompt $w_p$ should be upweighted; the CoT chain should be allowed to develop more freely.
- **Sensitivity**: high
- **Bounds**: In CoT: CFG applied only during generation of $w_p$'s continuation up-weighting; $w_{cot}$ and $w_a$ are generated with the same prompt context but the CFG target is only $w_p$.
- **Code ref**: [src/execution/cfg_decoding.py]
- **Source**: Section 3.2, end of section: "instead of upweighting just wp, we might upweight wp, wcot, or other variations"

## H05: Negative Prompt = Default System Prompt for Chatbots
- **Rationale**: For chatbot/assistant tasks, the most effective negative prompt is the model's own default system prompt. This explicitly emphasizes the difference between the user's modified system prompt and the model's default behavior, rather than contrasting against an arbitrary unconditional distribution.
- **Sensitivity**: medium
- **Bounds**: Negative prompt should be semantically related to but distinct from the positive prompt; using completely unrelated text as negative prompt may produce unpredictable results. Optimal γ for chatbots is around 3; degrade at γ≥4.
- **Code ref**: [src/execution/cfg_decoding.py]
- **Source**: Section 3.4; Figure 5 showing peak at γ=3 with 75% preference
