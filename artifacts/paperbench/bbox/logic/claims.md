# Claims

## C01: BBOX-ADAPTER significantly improves black-box LLM task performance
- **Statement**: BBOX-ADAPTER consistently improves gpt-3.5-turbo performance across diverse QA tasks by an average of 6.39% and up to 6.77% (Combined setting, GSM8K), while requiring no access to model parameters or output token probabilities.
- **Status**: supported
- **Falsification criteria**: BBOX-ADAPTER (any setting) fails to improve over the CoT baseline on all four datasets (StrategyQA, GSM8K, TruthfulQA, ScienceQA).
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: performance, black-box, QA, GPT-3.5

## C02: BBOX-ADAPTER reduces training cost by 31.30x over SFT
- **Statement**: The full-step variant of BBOX-ADAPTER requires $3.48 (StrategyQA) and $11.58 (GSM8K) training cost versus $153.00 and $216.50 for Azure-SFT, yielding approximately 31.30× reduction in training cost per thousand questions.
- **Status**: supported
- **Falsification criteria**: BBOX-ADAPTER full-step training cost exceeds or equals Azure-SFT training cost on StrategyQA or GSM8K.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: cost, training, efficiency, SFT

## C03: BBOX-ADAPTER reduces inference cost by 1.84x over SFT (full-step)
- **Statement**: The full-step BBOX-ADAPTER inference costs $5.37/1k Q (StrategyQA) and $12.46/1k Q (GSM8K) versus $7.50/1k Q and $28.30/1k Q for Azure-SFT, yielding approximately 1.84× reduction; the single-step variant achieves approximately 6.27× reduction.
- **Status**: supported
- **Falsification criteria**: BBOX-ADAPTER full-step inference cost equals or exceeds Azure-SFT inference cost.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: cost, inference, efficiency, beam search

## C04: Ranking-based NCE loss outperforms MLM loss by up to ~10%
- **Statement**: On StrategyQA with 0.1B adapter, NCE achieves 71.62% accuracy vs MLM's 61.52% (+10.10%); on GSM8K with 0.3B adapter, NCE achieves 73.86% vs MLM's 70.81% (+3.05%).
- **Status**: supported
- **Falsification criteria**: MLM loss achieves accuracy equal to or greater than NCE loss on both StrategyQA and GSM8K under any adapter size.
- **Proof**: [E05]
- **Dependencies**: none
- **Tags**: ablation, NCE, MLM, loss function

## C05: BBOX-ADAPTER supports plug-and-play transfer to other black-box LLMs
- **Statement**: An adapter trained on gpt-3.5-turbo can be directly applied without retraining to davinci-002 (+6.85% average) and Mixtral-8×7B (+4.50% average) across three datasets.
- **Status**: supported
- **Falsification criteria**: Applying the gpt-3.5-turbo adapter to davinci-002 or Mixtral-8×7B does not improve performance over the unadapted baseline on any dataset.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: plug-and-play, transfer, davinci, Mixtral

## C06: AI feedback is competitive with ground-truth labels
- **Statement**: BBOX-ADAPTER (AI Feedback, using GPT-4 to select positive samples) achieves competitive performance with BBOX-ADAPTER (Ground-Truth) across all four tasks, with differences of ≤1.77% accuracy on any single dataset.
- **Status**: supported
- **Falsification criteria**: AI Feedback performance falls more than 5% below Ground-Truth performance on any dataset in Table 2.
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: AI feedback, ground-truth, online adaptation, GPT-4

## C07: Increasing beam size improves performance by ~2.41% on average
- **Statement**: Increasing beam size from k=1 to k=5 on StrategyQA with gpt-3.5-turbo contributes to an average performance enhancement of 2.41% across 0.1B and 0.3B adapter sizes.
- **Status**: supported
- **Falsification criteria**: Performance does not increase monotonically from k=1 to k=5 for both adapter sizes on StrategyQA.
- **Proof**: [E06]
- **Dependencies**: C01
- **Tags**: beam search, scale, beam size, StrategyQA

## C08: Online adaptation iterations improve performance monotonically (T=1..3)
- **Statement**: An unfinetuned adapter (T=0) performs below the base model; after T=1 adaptation iteration the model surpasses the base; performance improves consistently through T=3 on StrategyQA.
- **Status**: supported
- **Falsification criteria**: At T=1, BBOX-ADAPTER performance is below or equal to the base model; or performance does not improve from T=1 to T=3.
- **Proof**: [E07]
- **Dependencies**: C01
- **Tags**: online adaptation, iterations, self-improvement, convergence
