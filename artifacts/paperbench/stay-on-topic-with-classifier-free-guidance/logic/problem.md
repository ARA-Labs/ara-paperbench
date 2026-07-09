---
# Problem Specification

## Observations

### O1: Language Model Prompt Drift
- **Statement**: Standard autoregressive generation does not differentiate between prompt tokens w₁...wₚ and continuation tokens wₚ₊₁...wₜ₋₁, leading to generations that lose adherence to the prompt over time.
- **Evidence**: Qualitative examples in Table 1 (main paper) show GPT4All ignoring system-level directives in vanilla sampling; Figure 17/18/19/20 show GPT-2 continuations diverging from the prompt.
- **Implication**: Models treat all context equally at generation time, causing meandering and hallucination especially in longer generations.

### O2: Smaller Models Struggle with Prompt Adherence
- **Statement**: Smaller language models (GPT-2, Pythia <1B) exhibit more severe prompt drift, hallucination, and degradation problems than larger models.
- **Evidence**: Zero-shot benchmark results (Figure 2, Table 2a/2b) show smaller models perform considerably worse; referenced issues of hallucination [49], degradation [38], and meandering [76].
- **Implication**: Compute-constrained users are most harmed by prompt drift.

### O3: Existing Solutions Are Compute- and Data-Expensive
- **Statement**: Instruction fine-tuning and reinforcement learning from human feedback (RLHF) are the dominant mitigation strategies but require significant compute, data, and expertise.
- **Evidence**: Referenced works [81, 70, 56, 4, 6] on instruction tuning and RLHF; these approaches are noted as not accessible to all users.
- **Implication**: There is a gap for lightweight, inference-time-only interventions accessible without model retraining.

### O4: CFG Works in Text-to-Image Without Architecture Changes
- **Statement**: Classifier-Free Guidance in diffusion models requires conditioning dropout training but significantly improves prompt adherence in text-to-image generation.
- **Evidence**: Ho & Salimans [37], Saharia et al. [68] demonstrate CFG effectiveness; conditioning dropout needed for diffusion.
- **Implication**: If LMs can support CFG without special training, they offer a superior application domain.

### O5: Language Models Naturally Handle Unconditional Generation
- **Statement**: Autoregressive language models trained on finite context windows naturally produce both conditional P(w|c) and unconditional P(w) distributions, since dropping the prefix c is a natural feature.
- **Evidence**: Equation 6 in Section 2.2 shows the factorization holds for autoregressive models; described in §2.2.
- **Implication**: Language models can apply CFG out-of-the-box without conditioning dropout training, unlike diffusion models.

## Gaps

### G1: No Inference-Time Prompt-Adherence Method for LMs
- **Statement**: No existing inference-time-only technique specifically targets prompt adherence across diverse prompting paradigms (zero-shot, CoT, long-form, chatbot) in autoregressive LMs.
- **Caused by**: O1, O3
- **Existing attempts**: Temperature scaling, nucleus sampling, repetition penalties (improve fluency but not prompt adherence); PPLM, FUDGE, GeDi (require auxiliary classifiers); instruction tuning (retraining required).
- **Why they fail**: Classifier-guided approaches require separate trained classifiers; instruction tuning requires full retraining and labeled data.

### G2: CFG Has Not Been Applied to Pure Language Modeling
- **Statement**: CFG has only been studied in the text-to-image domain with diffusion models; its application to decoder-only language models is unexplored.
- **Caused by**: O4, O5
- **Existing attempts**: None directly — the closest is contrastive decoding [45] which uses two models of different sizes.
- **Why they fail**: Contrastive decoding changes the model pair, not a single model's self-conditioning.

## Key Insight

- **Insight**: In autoregressive language models, the prompt c naturally serves as the conditioning, and the last token of the prompt can initiate the unconditional generation, making CFG applicable out-of-the-box at the logit level. The logit-space arithmetic log P̂(wᵢ|w<ᵢ, c) = log P(wᵢ|w<ᵢ) + γ(log P(wᵢ|w<ᵢ, c) − log P(wᵢ|w<ᵢ)) provides a guidance mechanism without any auxiliary model or retraining.
- **Derived from**: O4, O5
- **Enables**: Architecture-agnostic, training-free CFG applied to any decoder-only language model across arbitrary tasks.

## Assumptions

- A1: The logit distribution of a language model is linearly related to the last hidden layer, making logit-space arithmetic meaningful.
- A2: The unconditional distribution P(w) can be approximated by starting generation from the last token of the prompt (rather than a fixed start token).
- A3: Higher guidance strength γ > 1 improves prompt adherence at the cost of reduced diversity, consistent with behavior observed in text-to-image models.
- A4: The optimal γ value is task-dependent and must be tuned per setting.
