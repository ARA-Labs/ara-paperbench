# Training Configuration

## Inner Loop Optimizer (F-MNIST, SVHN, CIFAR-10)
- **Value**: Adam optimizer, lr=0.001
- **Rationale**: Adam is robust to noisy gradients and requires minimal tuning; consistent across proxy models.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: §5.2 ("An Adam optimizer (Kingma & Ba, 2015) is used with a learning rate of 0.001 for the inner loop")

## Inner Loop Optimizer (Figure 1 Experiments — Trivial Solution Demonstration)
- **Value**: SGD, lr=0.1, momentum=0.9, 100 epochs
- **Rationale**: Matches Zhou et al. (2022) baseline for fair comparison in Figure 1.
- **Search range**: Not specified.
- **Sensitivity**: medium
- **Source**: Appendix C.3

## Outer Loop Optimizer (Figure 1 Experiments)
- **Value**: Adam optimizer, lr=2.5, cosine rate scheduler
- **Rationale**: Used for the probabilistic outer-loop optimization of the trivial solution (Eq. 3, Eq. 4), matching Zhou et al. (2022).
- **Search range**: Not specified.
- **Sensitivity**: high
- **Source**: Appendix C.3

## Outer Loop Iterations T
- **Value**: T=500 (main experiments §5.2, §5.3); T∈{100,200,300,500,800,1500,2000} (ablation)
- **Rationale**: T=500 provides empirical convergence in the ablation study (Table 7 appendix); practitioners can choose T based on budget.
- **Search range**: T∈{100,200,300,500,800,1500,2000} explored in §6.
- **Sensitivity**: medium — below T≈500, performance improves; above T≈500, diminishing returns.
- **Source**: §5.2 ("The parameters ε and T are set to 0.2 and 500"); §6 (ablation)

## Voluntary Performance Compromise ε
- **Value**: ε=0.2 (main experiments); ε∈{0.2,0.3,0.4} explored in §5.1
- **Rationale**: Balances f1 relaxation (enabling size reduction) against performance degradation. ε=0.2 chosen as default for all main experiments.
- **Search range**: ε∈{0.2,0.3,0.4} in §5.1.
- **Sensitivity**: medium — larger ε enables smaller coresets but potentially higher f1(m).
- **Source**: §5.1, §5.2

## Post-Selection Training: F-MNIST and SVHN
- **Value**: Adam optimizer, lr=0.001, 100 epochs
- **Rationale**: Standard setting for these benchmarks.
- **Search range**: Not specified.
- **Sensitivity**: low
- **Source**: §5.2 ("for F-MNIST and SVHN, an Adam optimizer (Kingma & Ba, 2015) is used with a learning rate of 0.001 and 100 epochs")

## Post-Selection Training: CIFAR-10
- **Value**: SGD optimizer, initial lr=0.1, cosine rate scheduler, 200 epochs
- **Rationale**: Standard CIFAR-10 training protocol for ResNet-18.
- **Search range**: Not specified.
- **Sensitivity**: low
- **Source**: §5.2 ("For CIFAR-10, an SGD optimizer is exploited with an initial learning rate of 0.1 and a cosine rate scheduler. 200 epochs are set totally")

## Post-Selection Training: ImageNet-1k
- **Value**: SGD optimizer, base lr=0.01, batch size=256, momentum=0.9, weight decay=0.001, 100 epochs
- **Rationale**: Standard large-scale ImageNet training protocol using VISSL library.
- **Search range**: Not specified.
- **Sensitivity**: low
- **Source**: §5.4

## Predefined Coreset Size k (Experiments)
- **Value**: k∈{200,400} for MNIST-S (§5.1); k∈{1000,2000,3000,4000} for F-MNIST/SVHN/CIFAR-10 (§5.2); k/n∈{70%,80%} for ImageNet-1k (§5.4)
- **Rationale**: Standard range covering small to large subsets; allows comparison at practical sizes.
- **Search range**: Not specified beyond tested values.
- **Sensitivity**: high — defines the initialization point for LBCS search.
- **Source**: §5.1, §5.2, §5.4

## Continual Learning (Appendix E.6)
- **Value**: Memory size=100, weight for previous memory=0.01; PermMNIST with 10 tasks; 10% symmetric label noise for noisy version
- **Rationale**: Follows Borsos et al. (2020) setup.
- **Sensitivity**: Not specified.
- **Source**: Appendix E.6

## Streaming (Appendix E.7)
- **Value**: Batch size=125, replay memory=100, slots=0.0005, Adam step size=0.0005, 40 gradient steps per batch
- **Rationale**: Follows Borsos et al. (2020) setup.
- **Sensitivity**: Not specified.
- **Source**: Appendix E.7
