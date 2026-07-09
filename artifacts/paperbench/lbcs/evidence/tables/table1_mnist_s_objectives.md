# Table 1: MNIST-S Optimization Objectives (§5.1)
- **Source**: Table 1, Section 5.1
- **Caption**: "Results (mean±std.) to illustrate the utility of our method in optimizing the objectives f1(m) and f2(m)."
- **Conditions**: Dataset=MNIST-S (1000 random samples from MNIST); CNN with two blocks (Conv→Dropout→MaxPool→ReLU); 20 repetitions on NVIDIA GTX3090 with PyTorch; Adam inner loop lr=0.001; ε∈{0.2,0.3,0.4}; k∈{200,400}.

| Predefined k | Objectives | Initial | ε=0.2 | ε=0.3 | ε=0.4 |
|-------------|-----------|---------|--------|--------|--------|
| 200 | f1(m) | 3.21 | 1.92±0.33 | 2.26±0.35 | 2.48±0.30 |
| 200 | f2(m) | 190.7±3.9 | (not shown as initial) | 185.0±4.6 | 175.5±7.7 |
| 400 | f1(m) | 2.16 | 1.05±0.26 | 1.29±0.33 | 1.82±0.41 |
| 400 | f2(m) | 384.1±4.4 | (not shown as initial) | 373.0±6.0 | 366.2±8.1 |

**Note**: The initial f2(m) values represent the initialization near k (200 or 400); for ε=0.2 the f2 values are 190.7±3.9 (k=200) and 384.1±4.4 (k=400) before optimization. The table as presented in the paper shows initial f1 and then the three ε conditions for both objectives simultaneously. From the paper: "compared with initialized f1(m) and f2(m), both achieved f1(m) and f2(m) after lexicographic bilevel coreset selection are lower."
