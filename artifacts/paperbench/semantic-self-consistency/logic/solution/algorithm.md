---
# Algorithm

## Mathematical Formulation

### Centroid Proximity Weighting (CPW)

Given $k$ reasoning-path embeddings $\{e_1, e_2, \ldots, e_k\} \subset \mathbb{R}^d$:

**Step 1: Centroid**
$$\bar{e} = \frac{1}{k} \sum_{i=1}^{k} e_i$$

**Step 2: Distances**
$$d_i = \|e_i - \bar{e}\|_2$$

**Step 3: Normalized distances**
$$\tilde{d}_i = \frac{d_i}{\sum_{j=1}^{k} d_j}$$

**Step 4: Weights**
$$w_i = \frac{1}{\tilde{d}_i}$$

**Step 5: Aggregate by answer**
$$\text{score}(u) = \sum_{i \in I(u)} w_i \quad \text{where } I(u) = \{i : a_i = u\}$$

**Step 6: Select answer**
$$\hat{a} = \arg\max_u \text{score}(u)$$

---

### Semantic Consensus Weighting (SCW)

Given $N = \{n_1, n_2, \ldots, n_k\}$ (embedding vectors of $k$ responses):

**Step 1: Cosine similarity**
$$\text{cosine\_similarity}(n_a, n_b) = \frac{n_a \cdot n_b}{\|n_a\|_2 \cdot \|n_b\|_2}$$

**Step 2: Aggregate score per embedding**
$$S_{n_e} = \sum_{n_i \in N} \text{cosine\_similarity}(n_e, n_i)$$

**Step 3: Aggregate by answer**
$$\text{score}(u) = \sum_{e \in E(u)} S_e \quad \text{where } E(u) = \{e_i : a_i = u\}$$

**Step 4: Select answer**
$$\hat{a} = \arg\max_u \text{score}(u)$$

---

### Outlier Removal (Isolation Forest)

$$s(x, n) = 2^{-\frac{E(h(x))}{c(n)}}$$

where $h(x)$ is the path length (number of edges) to isolate $x$, and $c(n) = 2H(n-1) - \frac{2(n-1)}{n}$ is the normalization factor ($H$ = harmonic number). Samples with $s(x,n)$ close to 1 are outliers.

Configuration: `n_estimators=200`, `contamination='auto'`, `max_samples='auto'`

---

### Outlier Removal (KNN)

$$d_{\text{knn}}(x) = \frac{1}{k}\sum_{y \in \text{kNN}(x)} \sqrt{\sum_j (x_j - y_j)^2}$$

Samples with $d_{\text{knn}}(x)$ above the 90th percentile threshold are removed.

Configuration: `n_neighbors=5`, `metric='euclidean'`, `algorithm='ball_tree'`, `threshold=90%`

---

### Outlier Removal (One-Class SVM)

$$\min_{\omega, \xi, \rho} \frac{1}{2}\omega^T\omega - \rho + \frac{1}{\nu n}\sum_{i=1}^n \xi_i$$

Samples predicted as negative by the trained SVM are removed as outliers.

Configuration: `kernel='linear'`, `nu=0.01`, `gamma='scale'`

---

## Pseudocode

### CPW
```
function CPW(embeddings, answers):
    centroid = mean(embeddings, axis=0)
    distances = [norm(e - centroid) for e in embeddings]
    norm_distances = distances / sum(distances)
    weights = [1.0 / d for d in norm_distances]
    score_by_answer = defaultdict(float)
    for i, answer in enumerate(answers):
        score_by_answer[answer] += weights[i]
    return argmax(score_by_answer)
```

### SCW
```
function SCW(embeddings, answers):
    scores = []
    for i, e_i in enumerate(embeddings):
        s = sum(cosine_similarity(e_i, e_j) for e_j in embeddings)
        scores.append(s)
    score_by_answer = defaultdict(float)
    for i, answer in enumerate(answers):
        score_by_answer[answer] += scores[i]
    return argmax(score_by_answer)
```

### Outlier Removal (Generic)
```
function outlier_filter_then_vote(embeddings, answers, detector):
    labels = detector.fit_predict(embeddings)   # -1 = outlier
    retained = [answers[i] for i in range(len(answers)) if labels[i] != -1]
    return majority_vote(retained)
```

## Complexity Analysis
- **Embedding generation**: O(k · L · d) where L = sequence length, d = hidden dim
- **CPW**: O(k · d) for centroid + O(k · d) for distances = O(k · d)
- **SCW**: O(k² · d) for pairwise cosine similarities
- **Isolation Forest**: O(k · n_estimators · log k) fit + O(k) predict
- **KNN**: O(k² · d) for distance matrix with ball_tree
- **One-class SVM**: O(k² · d) for kernel computation (linear kernel is O(k · d))

All methods add negligible overhead compared to LLM generation cost.
