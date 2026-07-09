# Key Concepts

## LCA Distance (D_LCA)
- **Notation**: $D_{LCA}(y', y) := f(y) - f(N_{LCA}(y, y'))$
- **Definition**: The taxonomic distance between a model's predicted class $y'$ and the ground-truth class $y$ in a predefined class hierarchy (e.g., WordNet). $N_{LCA}(y, y')$ is the lowest common ancestor node of $y$ and $y'$. $f(\cdot)$ is a node scoring function (either information content or tree depth). The average LCA distance over a dataset is computed only over incorrectly classified samples: $D_{LCA}(\text{model}, \mathcal{M}) := \frac{1}{n}\sum_{i=1}^{n} D_{LCA}(\hat{y}_i, y_i) \Leftrightarrow y_i \neq \hat{y}_i$.
- **Boundary conditions**: Requires a predefined class hierarchy. Only computed for misclassified samples (correct predictions contribute 0 by convention). Lower LCA distance indicates "better mistakes" (semantically closer predictions). Not comparable across modalities using ELCA (sensitive to logit temperature).
- **Related concepts**: Information Content, ELCA Distance, WordNet Hierarchy, K-means Latent Hierarchy

## Information Content (I)
- **Notation**: $I(\text{node}) := -\log_2(p(\text{node}))$
- **Definition**: The negative log-probability of a node in the class hierarchy, where leaf nodes receive uniform probability ($p(\text{leaf}) = 1/K$ for $K$ total classes) and internal nodes receive probability equal to the sum of their descendants' probabilities. Used as the scoring function $f(\cdot)$ in the primary LCA distance variant ($D^I_{LCA}$).
- **Boundary conditions**: Assigns more weight to specific (deep) nodes than general (shallow) ones. More robust to tree imbalance than depth-based scoring. Used for the main correlation experiments.
- **Related concepts**: LCA Distance, WordNet Hierarchy

## ELCA Distance (D_ELCA)
- **Notation**: $D_{ELCA}(\text{model}, \mathcal{M}) := \frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K} \hat{p}_{k,i} \cdot D_{LCA}(k, y_i)$
- **Definition**: The Expected LCA Distance, a generalization of LCA distance that considers the full predicted probability distribution over all $K$ classes (weighted by softmax probabilities). Extends cross-entropy to incorporate hierarchical class relationships.
- **Boundary conditions**: Should NOT be compared across modalities (sensitive to logit temperature calibration). Combines aspects of Top-1 accuracy, LCA distance, and cross-entropy. Computed using softmax probabilities.
- **Related concepts**: LCA Distance, Information Content

## LCA Tree Depth Distance (D^P_LCA)
- **Notation**: $D^P_{LCA}(y', y) := (P(y) - P(N_{LCA}(y', y))) + (P(y') - P(N_{LCA}(y', y)))$
- **Definition**: LCA distance computed using tree depth $P(\cdot)$ as the node scoring function, rather than information content. The additive term $(P(y') - P(N_{LCA}))$ is included to counter tree imbalance. Used in linear probing experiments (not the main correlation experiments).
- **Boundary conditions**: Susceptible to tree imbalance (unlike information content variant). Used for constructing soft labels in the linear probing experiments. Defined in Appendix D.2.1.
- **Related concepts**: LCA Distance, Information Content

## WordNet Hierarchy
- **Notation**: $\mathcal{H}_{WN}$
- **Definition**: A large-scale lexical database organized as a tree hierarchy encoding semantic relationships between English words/concepts. ImageNet classes are mapped to WordNet synsets, making WordNet the standard hierarchy for ImageNet-based LCA computation. Serves as the primary class taxonomy in this paper.
- **Boundary conditions**: Available for ImageNet and related datasets. Not available for arbitrary datasets (motivating K-means latent hierarchy). Encodes human semantic knowledge approximating invariant class relationships across environments.
- **Related concepts**: K-means Latent Hierarchy, LCA Distance

## K-means Latent Hierarchy
- **Notation**: $\mathcal{H}_{KM}$
- **Definition**: A class taxonomy constructed by applying K-means clustering hierarchically to per-class average feature representations extracted from a pretrained model. For ImageNet (1000 classes), 9 levels of clustering are performed with $2^i$ cluster centers ($i = 1, 2, \ldots, 9$, since $2^9 < 1000$). The LCA height for a class pair is determined by the deepest level at which both classes share a cluster.
- **Boundary conditions**: Applicable to any dataset with a pretrained model. Quality depends on the source model (VLMs produce better hierarchies). All classes share a base cluster level of 10 by convention. Results in mean PEA correlations slightly lower than WordNet but still substantial.
- **Related concepts**: WordNet Hierarchy, LCA Distance

## Effective Robustness
- **Notation**: Not formally defined; refers to excess OOD performance beyond what ID performance predicts via the linear fit from Accuracy-on-the-Line.
- **Definition**: The concept (from Taori et al., 2020) that OOD performance should be predictable from ID performance via a linear function. A model has high "effective robustness" if it exceeds the expected OOD performance given its ID performance. VLMs exhibit high effective robustness under Accuracy-on-the-Line (unexpectedly high OOD given their ID Top-1).
- **Boundary conditions**: VLMs appear to have high effective robustness under Top-1 based evaluation, but this is explained by LCA distance — VLMs have lower LCA distance which correctly predicts their higher OOD performance.
- **Related concepts**: LCA Distance, Accuracy-on-the-Line

## LCA Alignment Loss
- **Notation**: $L = \lambda \cdot L_{CE} + L_{soft\_lca}$
- **Definition**: A composite training loss combining standard cross-entropy ($L_{CE}$) with an auxiliary soft label loss ($L_{soft\_lca}$). The soft labels are derived from the reverse normalized LCA distance matrix: $M_{LCA} = \text{MinMax}(M^T)$, where $M[i,k] = D_{LCA}(i,k)$ and $T$ is the temperature. The reverse is $1 - M_{LCA}$. Loss can be BCE or CE mode. Lambda weights the standard CE loss.
- **Boundary conditions**: Requires precomputed LCA distance matrix (n×n, where n = number of classes). Temperature T controls smoothness of soft labels. Lambda balances ID accuracy preservation vs. OOD improvement. Used for linear probing experiments only (not full end-to-end training reported in main paper).
- **Related concepts**: LCA Distance, LCA Tree Depth Distance, K-means Latent Hierarchy

## OOD Correlation Metrics (R², PEA, KEN, SPE)
- **Notation**: $R^2$, $r$ (PEA), $\tau$ (KEN), $\rho$ (SPE)
- **Definition**: Four correlation metrics used to measure the relationship between ID metrics (LCA or Top-1) and OOD accuracy across 75 models. R² (coefficient of determination) measures predictability; PEA (Pearson) measures linear correlation; KEN (Kendall's $\tau$) and SPE (Spearman's $\rho$) measure rank correlations. All use min-max scaling for preprocessing.
- **Boundary conditions**: All metrics take absolute values for simplicity (direction not reported). Min-max scaling applied since LCA does not fall in [0,1]. Used to assess "on-the-line" behavior rather than just point correlations.
- **Related concepts**: LCA Distance, Effective Robustness
