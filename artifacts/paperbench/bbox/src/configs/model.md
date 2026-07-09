# Model Configuration

## BBOX-ADAPTER Backbone — StrategyQA, GSM8K, ScienceQA
- **Value**: microsoft/deberta-v3-base (86M parameters) and microsoft/deberta-v3-large (304M parameters)
- **Rationale**: DeBERTa-v3 provides strong discriminative text understanding; two sizes allow cost-performance tradeoff analysis
- **Search range**: {deberta-v3-base, deberta-v3-large}
- **Sensitivity**: medium
- **Source**: §4.1, Appendix H.2

## BBOX-ADAPTER Backbone — TruthfulQA
- **Value**: bert-base-cased (110M parameters)
- **Rationale**: BERT-base-cased chosen for TruthfulQA task (different from other tasks); task-specific backbone selection
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Appendix H.2

## Adapter Output Head
- **Value**: Linear layer mapping [CLS] representation → scalar (output_dim=1)
- **Rationale**: Scalar output required for energy-based scoring of (question, answer) pairs; [CLS] token captures full sequence representation
- **Search range**: Not applicable
- **Sensitivity**: medium
- **Source**: §3.1, §3.2

## Spectral Normalization
- **Value**: Applied to final linear classification layer of adapter
- **Rationale**: Prevents sharp gradients during EBM training; ensures Lipschitz continuity of energy function
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: §3.2, Du & Mordatch (2019)

## Black-Box LLM — Primary Experiments
- **Value**: gpt-3.5-turbo (via Microsoft Azure OpenAI API); temperature=1.0; max_length=512
- **Rationale**: State-of-the-art black-box LLM; represents the target adaptation model class
- **Search range**: Not applicable (fixed baseline)
- **Sensitivity**: N/A
- **Source**: §4.1, Appendix H.2

## Black-Box LLM — White-Box Extension
- **Value**: mistralai/Mixtral-8x7B-v0.1 (loaded in half-precision fp16 from HuggingFace); temperature=1.0; max_length=512
- **Rationale**: Open-source alternative that can also be treated as black-box for fair evaluation
- **Search range**: Not applicable
- **Sensitivity**: N/A
- **Source**: §4.7, Appendix H.2

## Plug-and-Play Target Models
- **Value**: davinci-002 (OpenAI API) and Mixtral-8×7B (HuggingFace)
- **Rationale**: Diverse set of black-box LLMs for testing plug-and-play adapter transfer without retraining
- **Search range**: Not applicable
- **Sensitivity**: N/A
- **Source**: §4.3, Table 3

## AI Feedback Judge
- **Value**: GPT-4 (via OpenAI API)
- **Rationale**: Advanced LLM used to simulate human preference in the AI Feedback setting; evaluates candidates on coherency, reasonability, correctness, and format
- **Search range**: Not applicable
- **Sensitivity**: medium
- **Source**: §3.4, §4.1, Appendix G

## ToxiGen Adapter Backbone
- **Value**: deberta-v3-base (86M parameters)
- **Rationale**: Standard backbone for ToxiGen evaluation (Appendix E)
- **Search range**: Not specified
- **Sensitivity**: Not specified
- **Source**: Appendix E

## ToxiGen Base Model
- **Value**: Mixtral-8x7B-v0.1; temperature=0.7
- **Rationale**: Used for toxicity reduction evaluation; temperature 0.7 for ToxiGen specific to that evaluation
- **Search range**: Not specified
- **Sensitivity**: Not specified
- **Source**: Appendix E
