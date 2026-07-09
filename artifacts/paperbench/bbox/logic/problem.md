# Problem Specification

## Observations

### O1: Black-box LLMs lack parameter and probability access
- **Statement**: State-of-the-art LLMs (GPT-3.5-turbo, GPT-4, PaLM-2, Gemini) expose neither internal model parameters nor output token probability distributions over the full vocabulary. The OpenAI `logprobs` API returns at most top-5 token probabilities; the `echo` probability feature was deprecated after October 5, 2023.
- **Evidence**: Appendix C; Table 1 comparison of white/grey/black-box methods
- **Implication**: All white-box fine-tuning (LoRA, prefix-tuning, adapters) and grey-box adaptation methods (CombLM, Proxy-Tuning, kNN-Adapter, IPA) requiring token probabilities or model weights are inapplicable.

### O2: Fine-tuning APIs are opaque, privacy-risky, and expensive
- **Statement**: OpenAI's GPT-3.5-turbo fine-tuning API only exposes 3 adjustable hyperparameters (epochs, batch size, learning rate multiplier). Azure-SFT costs $153.00–$216.50 training and $7.50–$28.30 per 1k questions inference on StrategyQA/GSM8K respectively. Uploading training data to external APIs introduces privacy risks for sensitive domains (e.g., healthcare).
- **Evidence**: Table 4 (cost analysis); §1 Introduction; Appendix F.3
- **Implication**: Fine-tuning APIs are impractical for privacy-sensitive applications and hyperparameter search is prohibitively expensive.

### O3: General-purpose pre-trained LLMs underperform on specialized tasks
- **Statement**: gpt-3.5-turbo achieves only 66.59% accuracy on StrategyQA, 67.51% on GSM8K, 77.00% True+Info on TruthfulQA, and 72.90% on ScienceQA under CoT prompting, leaving significant room for domain adaptation.
- **Evidence**: Table 2 (base model row); §4.2
- **Implication**: Task-specific adaptation is needed to unlock full LLM utility.

### O4: Grey-box methods require token probabilities unavailable in modern LLMs
- **Statement**: Methods such as kNN-Adapter (Huang et al., 2023), CombLM (Ormazabal et al., 2023), Proxy-Tuning (Liu et al., 2024), and IPA (Lu et al., 2023) all require access to output token probabilities, which are only available in models predating GPT-3 or in open-source LLMs like LLaMA-2.
- **Evidence**: §2 Grey-Box LLM Adaptation; §1 Introduction footnote 1
- **Implication**: A genuinely black-box adaptation method must operate solely on text outputs.

## Gaps

### G1: No black-box adaptation method without APIs
- **Statement**: There exists no method to adapt black-box LLMs without using their fine-tuning APIs and without accessing model parameters or output probabilities.
- **Caused by**: O1, O4
- **Existing attempts**: Fine-tuning APIs (Peng et al., 2023), grey-box methods (Sun et al., 2022; Huang et al., 2023; Ormazabal et al., 2023; Lu et al., 2023; Liu et al., 2024)
- **Why they fail**: Fine-tuning APIs violate transparency/privacy; grey-box methods require token probabilities unavailable in GPT-3.5+ and PaLM-2.

### G2: Lack of cost-efficient adaptation for black-box LLMs
- **Statement**: Fine-tuning APIs cost 31.30× more in training and 1.84× more in inference than the proposed approach, making frequent or iterative adaptation economically infeasible.
- **Caused by**: O2
- **Existing attempts**: Azure-SFT
- **Why they fail**: API pricing is fixed and opaque; no control over training efficiency.

### G3: Ground-truth dependency limits adaptation scope
- **Statement**: Existing adaptation methods require labeled ground-truth data, limiting applicability to domains where such labels are scarce or expensive.
- **Caused by**: O2, O3
- **Existing attempts**: Standard SFT with supervised labels
- **Why they fail**: Assumes full availability of ground-truth solutions.

## Key Insight

- **Insight**: A small auxiliary language model (0.1B–0.3B parameters) can be trained as an energy-based scoring function purely from text outputs of the black-box LLM, using a ranking-based NCE objective that pushes target-domain text higher than source-domain text—without ever querying model weights or probabilities. The black-box LLM then acts as a proposal generator during inference, and the adapter as a reranker via sentence-level beam search.
- **Derived from**: O1, O4 (only text outputs are available) + O3 (adaptation is needed)
- **Enables**: Full black-box LLM adaptation using only API text generation calls, with online self-improvement through iterative sampling and AI/human feedback.

## Assumptions

- A1: The black-box LLM's text generation API is accessible (text-in, text-out).
- A2: A small white-box model (e.g., DeBERTa-v3-base) can be fine-tuned locally.
- A3: Target domain text can be distinguished from source domain text in meaning and quality.
- A4: Sentence-level decomposition of the generation provides a useful granularity for beam search.
- A5: AI feedback from an advanced LLM (GPT-4) can approximate human preference labels.
