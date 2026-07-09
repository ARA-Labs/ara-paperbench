# Claims

## C01: LBCS achieves equal or better test accuracy with smaller coreset sizes than fixed-size baselines
- **Statement**: On F-MNIST, SVHN, and CIFAR-10, LBCS with predefined size k consistently produces coresets strictly smaller than k, while achieving test accuracy ≥ the best fixed-size baseline (Uniform, EL2N, GraNd, Influential, Moderate, CCS, Probabilistic) at the same k.
- **Status**: supported
- **Falsification criteria**: LBCS produces a coreset of size ≥ k, or achieves lower test accuracy than all 7 baselines at the same k, across all datasets and all tested k values.
- **Proof**: [E01, E02]
- **Dependencies**: none
- **Tags**: coreset-size, test-accuracy, comparison, F-MNIST, SVHN, CIFAR-10

## C02: When evaluated at LBCS-determined coreset sizes, LBCS outperforms all baselines on test accuracy
- **Statement**: Applying the coreset size found by LBCS to all baseline methods, LBCS still achieves the highest mean test accuracy on F-MNIST, SVHN, and CIFAR-10 for all k configurations.
- **Status**: supported
- **Falsification criteria**: Any baseline achieves higher mean test accuracy than LBCS at the LBCS-determined coreset size on any tested dataset/k combination.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: fixed-size comparison, test-accuracy, F-MNIST, SVHN, CIFAR-10

## C03: LBCS converges ε-optimally (ε-convergence theorem)
- **Statement**: Under Conditions 1 (Progressable) and 2 (Stable Moving), LBCS satisfies P_{t→∞}[f2(mt) ≤ f*_2] = 1, where f*_2 = min_{m: f1(m) ≤ f*_1·(1+ε)} f2(m). That is, LBCS converges to the minimum achievable coreset size under the ε-relaxed accuracy constraint.
- **Status**: supported
- **Falsification criteria**: A counterexample to Theorem 2 is produced (a setting where Conditions 1 and 2 hold but the algorithm does not converge).
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: convergence, theoretical, bilevel, lexicographic

## C04: LBCS reduces model overfitting during coreset selection under imperfect supervision
- **Statement**: On F-MNIST with 30% or 50% symmetric label noise, and with class-imbalanced data, LBCS achieves higher test accuracy than all 7 baselines across predefined coreset sizes k∈{1000,2000,3000,4000}. The ε-compromise prevents over-optimization of f1(m) and hence reduces the effect of label noise.
- **Status**: supported
- **Falsification criteria**: On noisy or imbalanced F-MNIST, at least one baseline achieves higher test accuracy than LBCS for some k.
- **Proof**: [E04]
- **Dependencies**: C03
- **Tags**: label-noise, class-imbalance, overfitting, generalization, robustness

## C05: LBCS scales to ImageNet-1k and reduces the effective selection ratio below the predefined ratio
- **Statement**: On ImageNet-1k, LBCS at predefined ratios 70% and 80% achieves the highest Top-5 test accuracy among all methods and produces optimized selection ratios of 68.53% and 77.82% respectively.
- **Status**: supported
- **Falsification criteria**: LBCS does not achieve the top Top-5 accuracy, or the optimized ratio is ≥ the predefined ratio.
- **Proof**: [E05]
- **Dependencies**: C01
- **Tags**: ImageNet, large-scale, scalability, Top-5, selection-ratio
