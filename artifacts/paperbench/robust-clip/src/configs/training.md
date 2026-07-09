# Training Configuration

## optimizer
- **Value**: AdamW (Loshchilov & Hutter, 2018)
- **Rationale**: Standard optimizer for transformer fine-tuning; decoupled weight decay
- **Search range**: Not ablated (fixed from Mao et al. 2023 guidance)
- **Sensitivity**: low
- **Source**: Appendix B.1

## beta1
- **Value**: 0.9
- **Rationale**: Standard AdamW first momentum coefficient
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix B.1

## beta2
- **Value**: 0.95
- **Rationale**: Slightly higher than default (0.999) for transformer fine-tuning stability
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix B.1

## peak_learning_rate
- **Value**: 1e-5
- **Rationale**: Smaller LR (1e-5 vs 1e-4) yields +4.2% clean zero-shot generalization at cost of ~5% lower ImageNet robustness. Since preserving generalization is the goal, 1e-5 is chosen.
- **Search range**: {1e-5, 1e-4}
- **Sensitivity**: high
- **Source**: Appendix B.3, Table 8

## lr_schedule
- **Value**: Cosine decay with linear warmup to peak LR at 7% of total training steps
- **Rationale**: Standard practice for transformer fine-tuning; warmup prevents instability
- **Search range**: Not ablated
- **Sensitivity**: low
- **Source**: Appendix B.1

## weight_decay
- **Value**: 1e-4
- **Rationale**: Ablation shows WD has no impact on clean or robust performance; 1e-4 chosen as default.
- **Search range**: {1e-4, 1e-3}
- **Sensitivity**: low
- **Source**: Appendix B.3, Table 8

## effective_batch_size
- **Value**: 128
- **Rationale**: Standard mini-batch size for adversarial training on ImageNet
- **Search range**: Not ablated
- **Sensitivity**: medium
- **Source**: Appendix B.1

## epochs
- **Value**: 2
- **Rationale**: 2 epochs ≈ 0.2% of original CLIP training cost (32 epochs × 400M images). Sufficient for non-trivial robustness in short fine-tuning regime.
- **Search range**: Not ablated (fixed at 2 for all ViT-L/14 models)
- **Sensitivity**: medium
- **Source**: §4 (Setting), Appendix B.1

## pgd_steps_training
- **Value**: 10
- **Rationale**: More steps compensate for shorter training time (2 epochs). In long training (300 epochs), 2–3 steps suffice; in short fine-tuning, 10 steps are necessary.
- **Search range**: Not ablated directly for ViT-L/14 (fixed at 10)
- **Sensitivity**: medium
- **Source**: §4 (Setting), Appendix B.3

## pgd_step_size
- **Value**: 1/255 (≈0.00392)
- **Rationale**: Standard step size for ℓ∞ adversarial training on ImageNet
- **Search range**: Not ablated
- **Sensitivity**: medium
- **Source**: Appendix B.1

## epsilon_fare2
- **Value**: 2/255 (≈0.00784)
- **Rationale**: Smaller radius yields better clean performance; perturbations are imperceptible
- **Search range**: {2/255, 4/255}
- **Sensitivity**: high
- **Source**: §4 (Controlling the clean vs robust accuracy trade-off)

## epsilon_fare4
- **Value**: 4/255 (≈0.01569)
- **Rationale**: Larger radius provides full robustness at both 2/255 and 4/255 test radii; slight clean performance cost
- **Search range**: {2/255, 4/255}
- **Sensitivity**: high
- **Source**: §4 (Controlling the clean vs robust accuracy trade-off)

## image_resolution
- **Value**: 224×224
- **Rationale**: ViT-L/14 operates at 224×224; matches LVLM configuration for OpenFlamingo and LLaVA
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: Appendix B.1

## pgd_momentum_factor
- **Value**: 0.9
- **Rationale**: Momentum PGD for inner maximization; standard practice
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1 (implied by PGD implementation)

## fare_loss_norm
- **Value**: Squared ℓ₂ norm (||·||²₂)
- **Rationale**: Connected to cosine similarity; preserves unnormalized embeddings. ℓ₁ performs comparably but has no theoretical motivation.
- **Search range**: {||·||²₂, ||·||₁}
- **Sensitivity**: low
- **Source**: §3.3, Appendix B.4, Table 9

## embedding_token
- **Value**: Class token only
- **Rationale**: Using all tokens requires more memory/compute without improving downstream LVLM results
- **Search range**: {class token, all tokens}
- **Sensitivity**: medium
- **Source**: Appendix B.1
