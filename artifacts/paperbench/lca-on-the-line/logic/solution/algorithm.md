# Algorithm Specification

## 1. Information Content Node Score

**Inputs**: Class hierarchy tree $\mathcal{H}$, set of $K$ leaf classes  
**Output**: Information content $I(v)$ for all nodes $v$

```
Algorithm: Compute Information Content
1. For each leaf node y: p(y) = 1/K  (uniform distribution)
2. For each internal node v (bottom-up):
     p(v) = sum of p(children of v)
3. For each node v:
     I(v) = -log2(p(v))
```

## 2. LCA Distance (Information Content Variant, D^I_LCA)

**Inputs**: Ground truth class $y$, predicted class $y'$, hierarchy $\mathcal{H}$ with information content scores  
**Output**: LCA distance (scalar ≥ 0)

$$D^I_{LCA}(y', y) := I(y) - I(N_{LCA}(y, y'))$$

where $N_{LCA}(y, y')$ is the lowest common ancestor of $y$ and $y'$ in $\mathcal{H}$.

**Average over dataset**:
$$D_{LCA}(\text{model}, \mathcal{M}) := \frac{1}{n}\sum_{i=1}^{n} D^I_{LCA}(\hat{y}_i, y_i) \Leftrightarrow y_i \neq \hat{y}_i$$

## 3. LCA Distance (Tree Depth Variant, D^P_LCA)

**Inputs**: Ground truth class $y$, predicted class $y'$, hierarchy $\mathcal{H}$ with depth function $P(\cdot)$  
**Output**: LCA distance (scalar ≥ 0)

$$D^P_{LCA}(y', y) := (P(y) - P(N_{LCA}(y', y))) + (P(y') - P(N_{LCA}(y', y)))$$

The second term compensates for tree imbalance.

## 4. ELCA Distance

**Inputs**: Predicted probability distribution $(\hat{p}_{1,i}, \ldots, \hat{p}_{K,i})$, ground truth $y_i$  
**Output**: Expected LCA distance

$$D_{ELCA}(\text{model}, \mathcal{M}) := \frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K} \hat{p}_{k,i} \cdot D_{LCA}(k, y_i)$$

## 5. K-means Latent Hierarchy Construction

```
Algorithm: Build Latent Hierarchy
Input: Pretrained model M, dataset (X, Y), K classes, n=9 levels
1. Compute per-class average features:
   kX[c] = mean(M.features(X[Y==c])) for c in 0..K-1
2. For i = 1 to 9:
   clusters[i] = KMeans(n_clusters=2^i).fit(kX)
3. For each class pair (c1, c2):
   lca_height[c1, c2] = min level i where clusters[i].label(c1) == clusters[i].label(c2)
   if no shared cluster found: lca_height[c1, c2] = 10  (base level)
4. Return lca_height as the latent hierarchy distance matrix
```

## 6. LCA Alignment Loss (Algorithm 1 from paper)

```python
def LCA_ALIGNMENT_LOSS(logits, targets, alignment_mode, LCA_matrix, lambda_weight=0.03):
    # Step 1: Compute reverse LCA matrix
    reverse_LCA_matrix = 1 - LCA_matrix

    # Step 2: Compute predicted probabilities
    probs = softmax(logits, dim=1)

    # Step 3: One-hot encode targets
    one_hot_targets = one_hot(targets, num_classes=K)

    # Step 4: Standard cross-entropy loss
    standard_loss = -sum(one_hot_targets * log(probs), dim=1)

    # Step 5-10: Soft loss based on alignment_mode
    if alignment_mode == 'BCE':
        soft_loss = mean(BCEWithLogitsLoss(logits, reverse_LCA_matrix[targets]), dim=1)
    elif alignment_mode == 'CE':
        soft_loss = -mean(reverse_LCA_matrix[targets] * log(probs), dim=1)

    # Step 11-12: Combine losses
    total_loss = lambda_weight * standard_loss + soft_loss

    return mean(total_loss)
```

**Soft label construction** (preprocessing, before training):
$$M_{LCA} = \text{MinMax}(M^T)$$
where $M[i,k] = D^P_{LCA}(i,k)$ and $T=25$.

## 7. Weight Interpolation for Linear Probes

$$W_{interp} = \alpha \cdot W_{CE} + (1-\alpha) \cdot W_{CE+soft}$$

where $\alpha \in \{0.0, 0.1, 0.2, \ldots, 1.0\}$ is selected to maximize Top-1 accuracy on ImageNet validation set.

## 8. Correlation Metrics

$$R^2 = 1 - \frac{\sum_i (y_i - f(x_i))^2}{\sum_i (y_i - \bar{y})^2}$$

$$r_{PEA} = \frac{\sum_i (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_i (x_i - \bar{x})^2} \sqrt{\sum_i (y_i - \bar{y})^2}}$$

$$\tau_{KEN} = \frac{\text{concordant pairs} - \text{discordant pairs}}{\frac{1}{2}n(n-1)}$$

$$\rho_{SPE} = 1 - \frac{6\sum_i d_i^2}{n(n^2 - 1)}$$

where $d_i$ = rank difference for observation $i$. All metrics apply min-max scaling to inputs.
