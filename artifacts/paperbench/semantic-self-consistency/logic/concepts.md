---
# Concepts

## Self-Consistency
- **Notation**: SC; majority vote over $\{a_1, a_2, \ldots, a_k\}$
- **Definition**: A decoding strategy that generates $k$ independent chain-of-thought responses to the same question using temperature sampling, then selects the final answer as the mode (most frequent) of the extracted answers $\{a_1, \ldots, a_k\}$.
- **Boundary conditions**: Requires closed-answer tasks (the answer space must be finite and parsable). Performance degrades below k ≈ 7–10 samples. Originally proposed by Wang et al. (2023).
- **Related concepts**: Chain-of-Thought Prompting, Centroid Proximity Weighting, Semantic Consensus Weighting

## Chain-of-Thought Prompting (CoT)
- **Notation**: CoT; few-shot exemplars with step-by-step reasoning
- **Definition**: A prompting strategy where each few-shot example includes an explicit step-by-step reasoning path before the final answer, eliciting similar reasoning from the model at inference time.
- **Boundary conditions**: Requires a sufficiently capable model; performance degrades for very short output sequences. The paper uses 4-shot for AQuA-RAT, 6-shot for StrategyQA, 8-shot for SVAMP.
- **Related concepts**: Self-Consistency, Semantic Consensus Weighting

## Reasoning-Path Embedding
- **Notation**: $e_i = \text{featurizer}(r_i) \in \mathbb{R}^d$; uses [CLS] token representation
- **Definition**: A dense vector representation of an entire chain-of-thought reasoning path $r_i$, produced by passing the full text through a BERT-based encoder and extracting the hidden state at the [CLS] token position.
- **Boundary conditions**: Quality depends on domain alignment of the featurizer. Short sequences yield less discriminative embeddings. Does not capture fine-grained numeric details.
- **Related concepts**: Centroid Proximity Weighting, Semantic Consensus Weighting, Featurizer

## Featurizer
- **Notation**: $f: \text{string} \rightarrow \mathbb{R}^d$
- **Definition**: A pre-trained, fine-tuned BERT-based model that converts a text string (reasoning path) into a fixed-dimensional embedding vector. SciBERT 110M is used for AQuA-RAT and SVAMP; RoBERTa 125M is used for StrategyQA.
- **Boundary conditions**: Must be domain-aligned to the reasoning task. BERT-based featurizers are trained on English corpora and may yield inconsistent results in other languages.
- **Related concepts**: Reasoning-Path Embedding, SciBERT, RoBERTa

## Centroid Proximity Weighting (CPW)
- **Notation**: $w_i = 1 / \tilde{d}_i$; $\tilde{d}_i = d_i / \sum_j d_j$; $d_i = \|e_i - \bar{e}\|$; $\text{sum\_weights}[u] = \sum_{i \in I(u)} w_i$
- **Definition**: A weighting scheme that computes the centroid $\bar{e} = \frac{1}{k}\sum_i e_i$ of all k reasoning-path embeddings, then assigns weight to each response inversely proportional to its normalized Euclidean distance from the centroid. Responses with the same final answer have their weights summed; the answer with the highest total weight is selected.
- **Boundary conditions**: Effective when reasoning-path embeddings cluster meaningfully (arithmetic tasks). Less effective when reasoning paths are highly diverse (commonsense tasks with limited reasoning context).
- **Related concepts**: Reasoning-Path Embedding, Semantic Consensus Weighting, Self-Consistency

## Semantic Consensus Weighting (SCW)
- **Notation**: $S_{n_e} = \sum_{n_i \in N} \text{cosine\_similarity}(n_e, n_i)$; $\text{cosine\_similarity}(n_a, n_b) = \frac{n_a \cdot n_b}{\|n_a\|_2 \|n_b\|_2}$
- **Definition**: A weighting scheme that computes, for each reasoning-path embedding $n_e$, the sum of its cosine similarities with all other embeddings in the response set $N$. Scores are aggregated by final answer; the answer with the highest total score is selected.
- **Boundary conditions**: Generally outperforms CPW; most effective when correct reasoning paths are more mutually similar than incorrect ones. Performance can degrade if all responses are overly similar (degenerate generation).
- **Related concepts**: Reasoning-Path Embedding, Centroid Proximity Weighting, Self-Consistency

## Isolation Forest
- **Notation**: $s(x, n) = 2^{-E(h(x))/c(n)}$; $h(x)$ = path length, $c(n)$ = normalization
- **Definition**: An unsupervised anomaly detection algorithm that isolates data points by recursively partitioning the feature space with random cuts. Points requiring fewer cuts to isolate (shorter path lengths) receive lower anomaly scores. Applied to reasoning-path embeddings to remove outlier rationales before majority voting.
- **Boundary conditions**: Paper configuration: n_estimators=200, contamination=auto, max_samples=auto (sklearn defaults). Effective on moderate-to-large embedding sets.
- **Related concepts**: Reasoning-Path Embedding, K-Nearest Neighbor Outlier Removal, One-Class SVM

## K-Nearest Neighbor Outlier Removal (KNN)
- **Notation**: $d_{\text{knn}}(x) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$; threshold at 90th percentile
- **Definition**: An outlier detection approach that computes the average Euclidean distance from each embedding to its k nearest neighbors; points above the 90th percentile threshold are filtered as outliers. Paper configuration: n_neighbors=5, euclidean metric, ball_tree algorithm.
- **Boundary conditions**: Requires sufficient samples for meaningful distance estimates (k ≥ 7 recommended). Threshold of 90% retains 90% of the distribution.
- **Related concepts**: Reasoning-Path Embedding, Isolation Forest, One-Class SVM

## One-Class SVM (OCSVM)
- **Notation**: $\min_{\omega, \xi} \frac{1}{2}\omega^T\omega + C\sum_i \xi_i$
- **Definition**: A support vector machine trained on one class of data (inliers) that learns a decision boundary to identify points deviating from the nominal distribution. Applied to reasoning-path embeddings to filter outlier rationales. Paper configuration: linear kernel, nu=0.01, gamma=scale.
- **Boundary conditions**: Most effective when inlier distribution is compact. Performance varies by dataset; performs best on StrategyQA in the paper.
- **Related concepts**: Reasoning-Path Embedding, Isolation Forest, K-Nearest Neighbor Outlier Removal

## SciBERT
- **Notation**: SciBERT 110M; BERT-base architecture fine-tuned on scientific text
- **Definition**: A BERT-based language model (110M parameters) pre-trained on scientific corpora (Beltagy et al., 2019), used as the featurizer for AQuA-RAT and SVAMP datasets because its training distribution aligns with mathematical and scientific reasoning language.
- **Boundary conditions**: Produces lower avg inter-embedding distance (45.281) than general RoBERTa (48.697) on arithmetic tasks, confirming domain alignment benefit.
- **Related concepts**: Featurizer, Reasoning-Path Embedding, RoBERTa
