# Constraints

## Boundary Conditions

### BC1: Model Type Determines Logit-Based Method Viability
- The trainable logit-based forecasting model performs well on BART0Large but fails on FLAN-T5 models.
- Reason: FLAN-T5's instruction tuning creates more complex logit dynamics that the simplified kernel Θ̃ = h(xj,yj)h(xi,yi)^T cannot approximate.
- Implication: Only representation-based forecasting generalizes across model families.

### BC2: Fine-Tuning Scope Limits NTK Approximation Quality
- Fixed logit-based forecasting (using frozen f0 representations as h) is exact only when tuning LM heads only.
- Under LoRA or Full FT, the kernel requires TV backward passes, which is computationally prohibitive.
- The trainable approximation can partially recover under Full FT for BART0 but not for FLAN-T5.

### BC3: Sequential Refinement Degrades Forecasting Over Time
- Forecasting models are trained assuming the base model is f0; as the model is sequentially updated, predictions degrade.
- Precision remains approximately stable but recall drops over time as more examples are forgotten.
- Future work: update forecasting models alongside the language model.

### BC4: Forecasting Requires Access to Upstream Training Data
- D̂PT must be accessible for both training forecasting models and for replay.
- The method is not applicable when upstream pretraining data is private or inaccessible.

### BC5: LoRA Configuration
- LoRA is applied to query and value (but NOT key) matrices in all self-attention layers.
- This is a fixed design choice; different LoRA configurations may affect forgetting patterns.

### BC6: Positive Examples Are Rare (1-10%)
- Class imbalance means naive training without weighting or frequency priors leads to poor F1.
- The frequency prior and positive-pair weight α=0.1 are essential design choices.

## Known Limitations

### L1: Model-Specific Failure
- Logit-based forecasting works for BART0 but not FLAN-T5; the paper cannot explain why the simplified kernel is insufficient for FLAN-T5's architecture.

### L2: Distributional Shift in Sequential Settings
- In long sequential streams, the base model f0 used for training diverges from the current model ft, causing forecasting accuracy to degrade.
- Table 12 shows representation-based F1 drops from 49.3 to 23.4 over 5 time steps on FLAN-T5Large.

### L3: Task Distribution Effects Not Fully Analyzed
- The paper does not comprehensively analyze how task similarity between online and upstream examples affects forgetting probability.

### L4: Edit Success Rate vs. Forgetting Trade-off
- All replay methods reduce forgetting but may also cause forgetting of the newly learned online example (lower edit success rate in sequential settings).
- This tension is noted but not fully resolved.

### L5: Replay Overfitting in Single-Error Setting
- Replaying more examples per online example causes *increased* forgetting in the single-error setting (Table 10), suggesting replay overfitting to the replayed examples at the expense of the online example.
