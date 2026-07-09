---
# Related Work

## RW01: Wang et al., 2023
- **DOI**: arXiv:2203.11171
- **Type**: extends
- **Delta**:
  - What changed: This paper adds a semantic re-weighting and filtering step on top of self-consistency's majority vote, utilizing reasoning-path embeddings instead of only final answers.
  - Why: Standard majority vote discards semantic information in reasoning paths.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Self-consistency framework (generate k samples, majority vote); chain-of-thought prompting; benchmark datasets and evaluation protocol.

## RW02: Wei et al., 2022
- **DOI**: arXiv:2201.11903
- **Type**: imports
- **Delta**:
  - What changed: Chain-of-thought prompting is used as the generation strategy for all experiments without modification.
  - Why: CoT produces structured, step-by-step reasoning paths suitable for semantic embedding.
- **Claims affected**: C01, C02, C05
- **Adopted elements**: 8-shot math prompt (SVAMP), 4-shot AQuA-RAT prompt, 6-shot StrategyQA prompt; CoT as the prompting strategy.

## RW03: Devlin et al., 2019
- **DOI**: arXiv:1810.04805
- **Type**: imports
- **Delta**:
  - What changed: BERT architecture is used as the backbone for all featurizer models (SciBERT, RoBERTa, MathBERT).
  - Why: BERT's bidirectional representations and [CLS] token provide dense, contextual embeddings of full text sequences.
- **Claims affected**: C04
- **Adopted elements**: BERT-base architecture; [CLS] token pooling for sentence-level embeddings.

## RW04: Beltagy et al., 2019
- **DOI**: arXiv:1903.10676
- **Type**: imports
- **Delta**:
  - What changed: SciBERT is used as the featurizer for mathematical reasoning tasks (AQuA-RAT, SVAMP).
  - Why: SciBERT's scientific text pre-training aligns with mathematical language.
- **Claims affected**: C04
- **Adopted elements**: SciBERT 110M model weights.

## RW05: Liu et al., 2019
- **DOI**: arXiv:1907.11692
- **Type**: imports
- **Delta**:
  - What changed: RoBERTa is used as the featurizer for StrategyQA commonsense reasoning.
  - Why: RoBERTa's robust general training suits commonsense reasoning text.
- **Claims affected**: C04
- **Adopted elements**: RoBERTa 125M model weights.

## RW06: Liu et al., 2008 (Isolation Forest)
- **DOI**: 10.1109/ICDM.2008.17
- **Type**: imports
- **Delta**:
  - What changed: Isolation Forest is applied to reasoning-path embeddings for outlier removal instead of general tabular data.
  - Why: Efficient, parameter-light anomaly detection suitable for embedding-space outlier removal.
- **Claims affected**: C03
- **Adopted elements**: Isolation Forest algorithm; sklearn implementation with n_estimators=200, contamination=auto.

## RW07: Huang et al., 2022
- **DOI**: arXiv:2210.11610
- **Type**: baseline
- **Delta**:
  - What changed: Self-improvement requires an extra training phase; semantic self-consistency operates purely at inference time without re-training.
  - Why: Post-generation weighting avoids expensive pre-training.
- **Claims affected**: C01, C02
- **Adopted elements**: Concept of using model outputs to improve model predictions.

## RW08: Yoran et al., 2023
- **DOI**: arXiv:2304.13007
- **Type**: baseline
- **Delta**:
  - What changed: Meta-reasoning over CoT uses qualitative information between chains; semantic self-consistency uses embedding geometry instead, which is more robust on arithmetic operations.
  - Why: Meta-reasoning shares the same limitations as baseline self-consistency on arithmetic.
- **Claims affected**: C01, C03
- **Adopted elements**: Motivation for utilizing reasoning path content beyond final answers.
