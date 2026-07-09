# Constraints and Limitations

## Boundary Conditions

### BC1: Text-only API access required
- **Condition**: The black-box LLM must expose a text generation API (text-in, text-out). Output token probabilities, logits, and model weights must be completely inaccessible.
- **Implication**: Applicable to GPT-3.5-turbo, GPT-4, PaLM-2, Gemini, davinci-002. Not applicable to models that fully expose logprobs (grey-box) or weights (white-box).
- **Failure mode**: If logprobs become available, grey-box methods may outperform BBOX-ADAPTER.

### BC2: Requires local compute for adapter training
- **Condition**: A local GPU capable of training a 0.1B–0.3B parameter model is needed. Minimum: single GPU with ~4–8 GiB VRAM for adapter (deberta-v3-base or bert-base-cased). Mixtral-8×7B as base requires ~90+ GiB VRAM for inference.
- **Implication**: Not zero-cost; requires local hardware investment.
- **Failure mode**: Without GPU, adapter training at batch size 64 for 6000 steps is too slow.

### BC3: Sentence-level decomposition assumes sentence-structured reasoning
- **Condition**: The beam search assumes outputs can be meaningfully decomposed into sentence-level steps $[s_1, \ldots, s_L]$ with a recognizable stop signal (e.g., "####" for GSM8K).
- **Implication**: Works well for chain-of-thought style outputs. May degrade for single-sentence responses or highly structured outputs (e.g., code, tables).
- **Failure mode**: Tasks without multi-step reasoning structure may not benefit from beam search; single-step variant is then preferred.

### BC4: Positive sample quality determines adaptation ceiling
- **Condition**: The quality of positive samples (ground-truth, human feedback, or AI feedback) bounds the maximum achievable performance improvement.
- **Implication**: Azure-SFT upper-bounds BBOX-ADAPTER because SFT directly optimizes the LLM's own parameters with perfect supervision.
- **Failure mode**: If ground-truth is noisy or AI feedback is inaccurate, the adapter may learn incorrect preferences.

### BC5: Performance gains vary across task types
- **Condition**: The method was evaluated on four QA tasks (StrategyQA, GSM8K, TruthfulQA, ScienceQA). Performance gains range from +2.70% (TruthfulQA, Ground-Truth) to +6.77% (GSM8K, Combined).
- **Implication**: Tasks requiring implicit reasoning (StrategyQA) or factual truthfulness (TruthfulQA) may see smaller gains than mathematical reasoning tasks.
- **Failure mode**: Tasks with very long outputs or code generation may require different stop-signal handling.

## Known Limitations

### L1: Higher API cost than direct prompting
The full-step beam search requires $k \times n \times L$ LLM API calls per question vs. 1 call for direct CoT. Inference cost is $12.46/1k Q for GSM8K vs. $1.22/1k Q for base CoT.

### L2: Adapter is task-specific
While plug-and-play transfer to other LLMs is supported, the adapter is task-specific. Switching to a completely new task domain requires re-training the adapter. No zero-shot task generalization.

### L3: AI feedback depends on an advanced LLM
The AI Feedback setting uses GPT-4 as the judge, which itself incurs API costs and is not infinitely reliable. GPT-4 feedback quality degrades on highly technical or domain-specific tasks.

### L4: Gap to white-box SFT
For Mixtral-8×7B on StrategyQA: BBOX-ADAPTER (66.08%) vs SFT-LoRA (73.80%–75.98%) — a 7.72%–9.90% gap. Direct parameter access confers a significant advantage.

### L5: Security/misuse risks
The adapter can potentially be used to "jailbreak" black-box LLMs by engineering toxic target domains. Additionally, gradient information from the adapter combined with LLM logit biases could facilitate adversarial attacks.
