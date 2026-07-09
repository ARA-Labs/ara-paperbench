---
# Claims

## C01: SCW outperforms self-consistency baseline
- **Statement**: Semantic Consensus Weighting (SCW), which weights responses by summed cosine similarity of reasoning-path embeddings, achieves higher accuracy than standard self-consistency majority vote on the majority of model-dataset combinations tested.
- **Status**: supported
- **Falsification criteria**: SCW accuracy is equal to or below SC baseline for more than half of the 15 model-dataset pairs in Table 1.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: SCW, cosine similarity, self-consistency, accuracy, reasoning

## C02: CPW improves over self-consistency on arithmetic but not commonsense
- **Statement**: Centroid Proximity Weighting (CPW) improves accuracy over the SC baseline averaged across models on AQuA-RAT (+3.14%) and SVAMP (+0.97%), but decreases performance on StrategyQA (−1.63%).
- **Status**: supported
- **Falsification criteria**: CPW average delta is negative for AQuA-RAT or SVAMP, or positive for StrategyQA.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: CPW, centroid, arithmetic, commonsense, self-consistency

## C03: Embedding-based outlier removal improves or matches SC baseline
- **Statement**: Isolation Forest, KNN, and One-class SVM applied to reasoning-path embeddings before majority voting produce best-configuration accuracy that exceeds the SC baseline in the majority of model-dataset conditions, with consistent gains remaining at reduced sample sizes.
- **Status**: supported
- **Falsification criteria**: Outlier removal best-configuration accuracy falls below SC baseline for more than half of all model-dataset-method triples in Table 2.
- **Proof**: [E02]
- **Dependencies**: none
- **Tags**: outlier detection, isolation forest, KNN, SVM, robustness

## C04: Domain-aligned featurizers produce tighter embedding clusters for reasoning tasks
- **Statement**: SciBERT (avg distance 45.281) and MathBERT (avg distance 45.892) produce significantly lower average inter-embedding distances than RoBERTa (avg distance 48.697) on arithmetic reasoning tasks, indicating denser clustering.
- **Status**: supported
- **Falsification criteria**: RoBERTa average distance is ≤ SciBERT or MathBERT average distance on the same arithmetic tasks.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: featurizer, SciBERT, RoBERTa, embedding, clustering

## C05: Sequence length positively correlates with accuracy improvement from semantic methods
- **Statement**: Models producing longer reasoning chains (higher average sequence length) tend to show greater accuracy improvement from semantic weighting methods, as longer chains provide more discriminative semantic signal.
- **Status**: supported
- **Falsification criteria**: No positive correlation is observed between average sequence length and average accuracy increase in Table 3.
- **Proof**: [E04]
- **Dependencies**: C01
- **Tags**: sequence length, chain-of-thought, accuracy, correlation

## C06: BLEU score does not correlate with accuracy improvement
- **Statement**: Higher BLEU scores for generated reasoning paths do not predict higher accuracy gains from semantic self-consistency methods, indicating text generation quality and reasoning accuracy are orthogonal.
- **Status**: supported
- **Falsification criteria**: A statistically significant positive correlation is found between average BLEU score and accuracy improvement across model-dataset pairs in Table 3.
- **Proof**: [E04]
- **Dependencies**: C05
- **Tags**: BLEU, sequence quality, accuracy, reasoning
