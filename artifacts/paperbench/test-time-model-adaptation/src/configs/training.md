---
# Training / Adaptation Hyperparameters

## Batch Size (BS)
- **Value**: 64
- **Rationale**: Follows TENT and SAR for fair comparison; provides sufficient samples for batch statistics in fitness function; single-sample adaptation handled separately via FOA-I
- **Search range**: {1, 4, 8, 16, 32, 64} analyzed in Table 7 (memory) and Table 14 (EMA ablation)
- **Sensitivity**: medium — smaller BS affects batch statistics quality; EMA mitigates this for activation shifting
- **Source**: Section 4 (Implementation Details)

## Population Size K
- **Value**: 28 (= 4 + 3 × log(prompt_dim)); prompt_dim = 768 × 3 = 2304 for ViT-Base default
- **Rationale**: Follows CMA-ES convention (Hansen, 2016); balances exploration-exploitation; performance converges for K > 15
- **Search range**: {2, 3, ..., 28} analyzed in Figure 2(a)
- **Sensitivity**: low — FOA works for all K ∈ [2, 28]; K=2 already outperforms NoAdapt; K=6 surpasses TENT
- **Source**: Section 4 (Implementation Details); Section 4.3; Figure 2(a)

## Number of Prompt Embeddings (Np)
- **Value**: 3
- **Rationale**: Reduces optimization dimension to 3 × 768 = 2,304 (ViT-Base), making CMA tractable; not carefully tuned as test data for tuning is unavailable in practice
- **Search range**: {1, 2, ..., 10} analyzed in Figure 2(b)
- **Sensitivity**: low — only minor variation across Np values; Np=5/7 marginally better
- **Source**: Section 4 (Implementation Details); Section 4.3; Figure 2(b)

## Prompt Initialization
- **Value**: Uniform initialization
- **Rationale**: Neutral starting point; no prior information about test distribution
- **Search range**: Not specified in paper
- **Sensitivity**: Not analyzed in paper
- **Source**: Section 4 (Implementation Details); Appendix B.2

## Trade-off Parameter λ
- **Value**: 0.4 × BS/64 on ImageNet-C/V2/Sketch; 0.2 × BS/64 on ImageNet-R
- **Rationale**: Balances entropy and activation discrepancy terms in fitness function; BS/64 normalization accounts for batch size; ImageNet-R uses 0.2 due to less severe distribution shift
- **Search range**: {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0} analyzed in Table 13
- **Sensitivity**: low — accuracy varies from 61.1% to 61.8% across λ ∈ [0.1, 1.0]; ECE more sensitive (2.5% to 5.9%)
- **Source**: Section 4 (Implementation Details); Appendix C (Table 13)

## EMA Factor α (Activation Shifting)
- **Value**: 0.1
- **Rationale**: Smooths online estimates of OOD domain center; low α gives high stability at cost of slower adaptation; critical for BS=1 operation (without EMA, BS=1 gives 0.1% accuracy)
- **Search range**: Not explicitly analyzed
- **Sensitivity**: high — without EMA (α=1.0), batch statistics are noisy; α=0.1 gives stable performance from BS=1 to BS=64
- **Source**: Section 3.2; Section 4 (Implementation Details); Appendix C (Table 14)

## Step Size γ (Activation Shifting)
- **Value**: 1.0
- **Rationale**: γ=1.0 achieves exact center alignment — the shifted center of OOD test features equals the source domain center μ^S_N. This is the "back-to-source" principle.
- **Search range**: Not explicitly analyzed in paper
- **Sensitivity**: medium — too small under-corrects; too large over-corrects
- **Source**: Section 3.2; Section 4 (Implementation Details)

## Number of Source ID Samples Q
- **Value**: Full ImageNet-1K validation set (default); minimum effective Q = 32 for stable statistics
- **Rationale**: Q ≥ 32 provides stable source statistics on ImageNet; larger Q does not meaningfully improve performance (Figure 2c)
- **Search range**: {16, 32, 64, 100, 200, 400, 800, 1600} analyzed in Figure 2(c)
- **Sensitivity**: low for Q ≥ 32 — both accuracy and ECE stable; Q=16 shows instability
- **Source**: Section 3.1; Section 4.3; Figure 2(c)

## Interval I (FOA-I single-sample variant)
- **Value**: I ∈ {4, 8, 16, 32, 64} (analyzed); no fixed default — depends on latency requirements
- **Rationale**: For BS=1, buffer I samples before running CMA update; smaller I = more CMA steps = better performance; I=4 outperforms TENT (BS=64)
- **Search range**: {4, 8, 16, 32, 64}
- **Sensitivity**: medium — smaller I is better for accuracy (more adaptation steps); I=4: 62.1% acc; I=64: 61.5% acc
- **Source**: Section 4.4; Table 6

## SGD Hyperparameters (for baseline comparisons in Table 9)
- **Value (TENT baseline)**: SGD, momentum=0.9, lr=0.001, trainable = affine params of layer normalization
- **Value (prompt + SGD + entropy, exp1)**: SGD, lr=0.01, Np=3 prompts
- **Value (SGD + Eq.5 fitness)**: entropy divided by BS=64; λ=30 (to match magnitude of two losses)
- **Source**: Appendix B.2; Table 9 experiments
