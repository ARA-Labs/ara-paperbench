---
# Experiments

## E01: Semantic weighting methods vs. self-consistency baseline
- **Verifies**: C01, C02
- **Setup**:
  - Model: GPT-3.5 (turbo), GPT-4o mini, Llama 2 7B, Llama 3 8B, Mistral 7B v0.1
  - Hardware: NVIDIA V100 16GB, NVIDIA A100 40GB, NVIDIA TPU v2 32GB (see reproducibility statement)
  - Dataset: AQuA-RAT (254 test samples), SVAMP (1000 train+test samples), StrategyQA (687 test samples)
  - System: k=10 samples per question, temperature=0.8, top-p=1, top-k=50; featurizer=SciBERT for AQuA-RAT/SVAMP, RoBERTa 125M for StrategyQA
- **Procedure**:
  1. For each question, generate k=10 chain-of-thought responses using temperature=0.8 sampling (4-shot for AQuA-RAT, 8-shot for SVAMP, 6-shot for StrategyQA).
  2. Parse the final answer from each response by extracting the string after "The answer is", removing whitespace, fullstops, and parentheses.
  3. Compute a reasoning-path embedding for each response using the [CLS] token from the domain-specific featurizer.
  4. **SC Baseline**: Take majority vote over extracted answers.
  5. **CPW**: Compute centroid of all k embeddings; compute normalized Euclidean distance of each embedding from centroid; assign weights inversely proportional to normalized distances; sum weights by answer; select highest-weight answer.
  6. **SCW**: Compute pairwise cosine similarity for all k embeddings; aggregate scores by summing cosine similarities per embedding; sum scores by answer; select highest-score answer.
  7. Also compute Top-prob baseline (greedy decoding, single response).
  8. Report accuracy on each dataset for each method/model combination.
- **Metrics**: Accuracy (% correct answers), delta over SC baseline (percentage points)
- **Expected outcome**:
  - SCW should outperform the SC baseline for the majority of model-dataset pairs
  - CPW should outperform SC baseline on AQuA-RAT and SVAMP on average across models, but underperform on StrategyQA
  - SC baseline should consistently outperform Top-prob single-sample baseline
- **Baselines**: Top-prob sample (greedy), SC baseline (majority vote with k=10)
- **Dependencies**: none

## E02: Outlier removal methods vs. self-consistency baseline
- **Verifies**: C03
- **Setup**:
  - Model: GPT-3.5, GPT-4o mini, Llama 2 7B, Llama 3 8B, Mistral 7B v0.1
  - Hardware: Same as E01
  - Dataset: AQuA-RAT (254 test), SVAMP (1000 samples), StrategyQA (687 test)
  - System: k=10 samples, temperature=0.8; featurizer=SciBERT for AQuA-RAT/SVAMP, RoBERTa for StrategyQA; KNN: n_neighbors=5, ball_tree, euclidean, 90% threshold; Isolation Forest: n_estimators=200, contamination=auto, max_samples=auto; SVM: linear kernel, nu=0.01, gamma=scale
- **Procedure**:
  1. Generate k=10 chain-of-thought responses per question (same setup as E01).
  2. Compute reasoning-path embeddings using the domain-specific featurizer.
  3. **Isolation Forest**: Fit IsolationForest(n_estimators=200, contamination='auto', max_samples='auto') on embeddings; remove samples predicted as outliers; apply majority vote to remaining.
  4. **KNN**: Compute average distance to 5 nearest neighbors for each embedding using ball_tree algorithm; filter top-10% highest-distance embeddings; apply majority vote to remaining.
  5. **One-class SVM**: Fit OneClassSVM(kernel='linear', nu=0.01, gamma='scale') on embeddings; remove samples predicted as outliers; apply majority vote to remaining.
  6. Report best and average accuracy across parameter configurations for each method/model/dataset combination.
  7. Verify that gains persist at reduced sample sizes.
- **Metrics**: Best accuracy (%), average accuracy (%), delta over SC baseline
- **Expected outcome**:
  - Outlier removal methods should generally improve or match the SC baseline across most model-dataset pairs
  - Gains should remain consistent as sample size decreases
  - One-class SVM should perform best on StrategyQA
  - GPT-3.5 should show larger relative gains than GPT-4o mini across all methods and datasets
- **Baselines**: SC baseline (majority vote k=10)
- **Dependencies**: none

## E03: Featurizer embedding quality comparison
- **Verifies**: C04
- **Setup**:
  - Model: RoBERTa 125M, SciBERT 110M, MathBERT (as featurizers)
  - Hardware: Not specified for this ablation
  - Dataset: Arithmetic reasoning samples (subset, due to greater variability)
  - System: Apply each featurizer to same set of generated reasoning paths; compute average pairwise embedding distance
- **Procedure**:
  1. Generate a set of reasoning-path responses on arithmetic reasoning samples.
  2. Embed each response using RoBERTa, SciBERT, and MathBERT respectively.
  3. Compute the average Euclidean distance between all pairs of embeddings for each featurizer.
  4. Compare average distances: lower distance indicates tighter clustering (better domain alignment).
- **Metrics**: Average pairwise embedding distance (lower is better for clustering)
- **Expected outcome**:
  - SciBERT and MathBERT should produce lower average distances than RoBERTa, indicating tighter clustering
  - Domain-aligned featurizers should outperform general-purpose featurizers on task-specific embeddings
- **Baselines**: RoBERTa 125M (general-purpose BERT variant)
- **Dependencies**: none

## E04: Sequence length and BLEU score vs. accuracy improvement
- **Verifies**: C05, C06
- **Setup**:
  - Model: GPT-3.5, GPT-4o mini, Llama 2 7B, Llama 3 8B, Mistral 7B v0.1
  - Hardware: Same as E01
  - Dataset: AQuA-RAT, SVAMP, StrategyQA
  - System: Same semantic self-consistency setup as E01; additionally measure average sequence length and BLEU score of generated responses vs. reference answers
- **Procedure**:
  1. Run semantic self-consistency experiments (E01) and record all generated responses.
  2. Compute average sequence length (token count) of generated responses per model-dataset pair.
  3. Compute average BLEU score (ROUGE-N / n-gram overlap) of generated responses vs. dataset reference answers.
  4. Compute average accuracy increase (%) from semantic methods over SC baseline per model-dataset pair.
  5. Analyze correlations: sequence length vs. accuracy increase, BLEU score vs. accuracy increase.
- **Metrics**: Average sequence length (tokens), Average BLEU score, Average accuracy increase (%)
- **Expected outcome**:
  - Positive correlation between average sequence length and accuracy improvement
  - No significant correlation between BLEU score and accuracy improvement
  - Longer sequences should provide more discriminative semantic signal for embedding-based methods
- **Baselines**: SC baseline accuracy
- **Dependencies**: E01
