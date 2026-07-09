---
# Model Configuration

## Generator: GPT-3.5 (gpt-3.5-turbo)
- **Type**: Closed-source, large-scale transformer (OpenAI)
- **Access**: Public API (https://openai.com/blog/openai-api)
- **Notes**: Chat fine-tuned; some deviation from few-shot prompt formatting expected. Configurations may deviate slightly due to API.
- **Source**: Section 3.1

## Generator: GPT-4o mini
- **Type**: Closed-source, lower-parameter variant of GPT-4o (OpenAI)
- **Access**: Public API
- **Notes**: Chat fine-tuned; include explicit formatting instructions to maintain consistent output structure.
- **Source**: Section 3.1

## Generator: Llama 2 7B
- **Parameters**: 7B
- **Type**: Open-weight, Meta
- **Access**: Restricted; requires Meta license (https://ai.meta.com/llama/)
- **Notes**: No built-in content moderation; external safeguards recommended.
- **Source**: Section 3.1, [32]

## Generator: Llama 3 8B
- **Parameters**: 8B
- **Type**: Open-weight, Meta
- **Access**: Restricted; requires Meta license (https://ai.meta.com/llama/)
- **Notes**: No built-in content moderation.
- **Source**: Section 3.1, [8]

## Generator: Mistral 7B v0.1
- **Parameters**: 7B
- **Type**: Open-weight
- **Access**: Apache 2.0 license (https://github.com/Mistralai/Mistral-src)
- **Notes**: No built-in content moderation.
- **Source**: Section 3.1, [13]

## Featurizer: SciBERT 110M
- **Parameters**: 110M
- **Architecture**: BERT-base, fine-tuned on scientific text (Beltagy et al., 2019)
- **Usage**: AQuA-RAT and SVAMP datasets
- **License**: Apache 2.0
- **Pooling**: [CLS] token representation
- **Source**: Section 3.2, [2]

## Featurizer: RoBERTa 125M
- **Parameters**: 125M
- **Architecture**: Robustly optimized BERT pretraining (Liu et al., 2019)
- **Usage**: StrategyQA dataset
- **License**: MIT
- **Pooling**: [CLS] token representation
- **Source**: Section 3.2, [19]

## Featurizer: MathBERT (ablation only)
- **Parameters**: Not specified in paper
- **Architecture**: BERT-base, fine-tuned on mathematical text (Shen et al., 2023)
- **Usage**: Ablation study only (Appendix G.2); not used in main experiments
- **Avg distance**: 45.892 (vs SciBERT 45.281, RoBERTa 48.697)
- **Source**: Appendix G.2, Table 6, [29]
