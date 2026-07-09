# Boundary Conditions and Limitations

## Boundary Conditions (Where LBCS Works)

### BC1: Discrete and binary mask space
- LBCS operates on binary masks m ∈ {0,1}^n. The LexiFlow randomized search is designed for continuous relaxations but converges with probability 1 under Conditions 1 and 2.
- Practical implementation perturbs mask continuously, then thresholds back to binary representation.

### BC2: Inner-loop convergence requirement
- LBCS evaluates f1(m) using θ(m) = argmin_θ L(m,θ). In practice, the inner loop must run long enough to produce a reliable approximation of θ(m).
- Acceleration: pre-train once with a random mask, then fine-tune for subsequent masks (reduces cost).

### BC3: ε must be non-negative
- ε ≥ 0 is required for the lexicographic structure to make sense. ε = 0 recovers exact first-objective optimization.

### BC4: Predefined k provides initialization only
- The predefined coreset size k initializes the mask but does not constrain the final coreset size. The final size is determined by lexicographic optimization.

### BC5: Applies to datasets with standard supervised learning setup
- Requires labeled data and cross-entropy (or similar) loss. Applied to image classification tasks in the paper; not evaluated on regression or generation tasks directly.

### BC6: Large-scale scalability via grouping
- For large datasets (ImageNet-1k), groups of G examples share the same mask entry, reducing dimensionality of the search space by a factor of G. This introduces a granularity constraint: the minimum selectable unit is a group, not an individual sample.

## Assumptions Made

- A1: The stable moving condition holds for LexiFlow on the given mask space and dataset. This is a standard assumption for local randomized search algorithms and cannot be verified a priori.
- A2: The inner-loop training provides a good approximation of the true θ(m) for evaluating f1(m).
- A3: f1(m) evaluated on the full dataset (not a held-out validation set) is a reliable proxy for generalization. In practice, this can lead to overfitting in the coreset selection loop — the ε compromise partially mitigates this.

## Known Limitations

### L1: Optimal convergence rate unknown
- Theorem 2 proves convergence in the limit but does not bound the rate. The number of outer iterations T needed for practical convergence is empirically determined (typically T=500).

### L2: Method is specific to bilevel optimization paradigm
- Other advanced coreset selection methods (e.g., score-based methods like EL2N, GraNd, Moderate) do not use bilevel optimization. The paper does not discuss how to incorporate size minimization into non-bilevel methods.

### L3: Computational overhead from inner-loop training
- Each mask evaluation requires (approximately) full inner-loop training. While acceleration tricks exist (pre-training + fine-tuning, model sparsity), the method is more expensive than score-based methods that require only a single training run.

### L4: Grouping trick introduces quantization
- Using groups of G=100 for ImageNet-1k means the minimum unit is 100 samples. Very small coreset sizes that are not multiples of G cannot be achieved exactly.

### L5: Convergence conditions not verifiable in closed form
- Conditions 1 and 2 hold by construction (C1) and assumption (C2). There is no practical test to verify whether C2 holds for a given dataset/architecture.

### L6: Does not compare to Borsos et al. (2020)
- The original bilevel coreset method (Borsos et al. 2020) is excluded from comparisons because its time complexity grows rapidly with coreset size. This limits the scope of comparison.
