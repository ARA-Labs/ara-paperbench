# Heuristics

## H01: Positive-Pair Reweighting (α=0.1)
- **Rationale**: Forgotten examples constitute only 1-10% of D̂PT, creating severe class imbalance. Without reweighting, the model would predict no forgetting on all examples and achieve near-zero F1. The weight α=0.1 assigned to positive pairs compensates for this.
- **Sensitivity**: high
- **Bounds**: α ∈ (0, 1]; paper uses α=0.1 for all experiments
- **Code ref**: [src/execution/forecasting.py]
- **Source**: Appendix B, "Training Details of the Forecasting Models"

## H02: Frequency Prior Bias Term (bj)
- **Rationale**: Some upstream examples are intrinsically more forgettable than others (independent of which online example is learned). Adding the log-odds prior as a bias term to the representation model allows it to focus on learning residual interaction effects rather than global forgettability.
- **Sensitivity**: medium
- **Bounds**: Computed from D^Train_R; fixed at inference time; removing it consistently reduces F1 (Table 1, "w/o Prior" rows)
- **Code ref**: [src/execution/forecasting.py]
- **Source**: Section 3.3, "Forecasting with Frequency Priors"

## H03: Caching Top-k Logits (k=100)
- **Rationale**: Storing all TV logit values for each upstream example is prohibitively expensive in memory. Caching only the top-100 logits per output token provides sufficient coverage for margin-based prediction while reducing storage by a factor of V/100 ≈ 300-500×.
- **Sensitivity**: low
- **Bounds**: k=100; increasing k improves accuracy marginally but increases storage
- **Code ref**: [src/execution/forecasting.py]
- **Source**: Section 3.2, "Efficient Inference"

## H04: Replay Interval (every 10 steps for BART0/FLAN-T5Large; every 5 for FLAN-T53B)
- **Rationale**: Replaying every step wastes compute; replaying too infrequently fails to counteract forgetting. The paper fixes 3 mini-batches over 30 fine-tuning steps (every 10 steps). Larger models (FLAN-T53B) use a denser schedule (every 5 steps over 30 steps = 6 mini-batches of size 4).
- **Sensitivity**: medium
- **Bounds**: Paper uses 3 batches for BART0/FLAN-T5Large; 4-15 batches increases forgetting prevention but risks overfitting (Table 10)
- **Code ref**: [src/execution/model_refinement.py]
- **Source**: Section 4.2, "Model Refinement"; Appendix D.2, Table 10

## H05: Distillation Loss for Replay
- **Rationale**: Standard cross-entropy replay forces exact match to ground truth; distillation against the base model f0 is softer and preserves the full output distribution including uncertainties, leading to better performance than standard CE replay (following Buzzega et al., 2020a).
- **Sensitivity**: medium
- **Bounds**: Applied to all replay variants; target distribution is f0's output probabilities
- **Code ref**: [src/execution/model_refinement.py]
- **Source**: Section 4.2, "Model Refinement"; Buzzega et al. (2020a) citation

## H06: Smaller Learning Rate for Sequential Error Fixing
- **Rationale**: In sequential refinement, using the same learning rate as single-error fixing leads to rapid accumulation of forgetting across multiple updates. The paper uses 10× lower learning rates for sequential settings (10^-6 for BART0, 10^-5 for FLAN-T5 vs. 10^-5 and 10^-4 for single-error). Table 9 shows that 1e-4 leads to 24.9% EM Drop vs. 3.3% at 1e-5.
- **Sensitivity**: high
- **Bounds**: Single error: 10^-5 (BART0), 10^-4 (FLAN-T5); Sequential: 10^-6 (BART0), 10^-5 (FLAN-T5)
- **Code ref**: [src/execution/model_refinement.py]
- **Source**: Section 4.1, "Hyperparameters"; Appendix D.1, Table 9
