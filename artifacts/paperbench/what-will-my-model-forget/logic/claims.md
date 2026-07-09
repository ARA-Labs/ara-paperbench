# Claims

## C01: Representation-Based Forecasting Achieves Best Overall Forecasting Performance
- **Statement**: A black-box forecasting model based on inner products of learned example representations (with frequency prior) achieves the highest binary F1 score for predicting forgotten upstream examples across all three PTLMs and nearly all fine-tuning configurations (7 of 8 model/dataset/tuning settings in Table 1).
- **Status**: supported
- **Falsification criteria**: A different method (threshold, fixed logit, or trainable logit) achieves higher average F1 than representation-based forecasting across the Table 1 configurations.
- **Proof**: [E01]
- **Dependencies**: C02, C03
- **Tags**: representation learning, forecasting, catastrophic forgetting, F1

## C02: Frequency Prior Improves Representation-Based Forecasting
- **Statement**: Adding a frequency prior bias term bj = log(forgetting odds) to the representation-based forecasting model consistently improves F1 compared to the same model without the prior (w/o Prior), for all 8 configurations in Table 1.
- **Status**: supported
- **Falsification criteria**: Removing the frequency prior does not consistently reduce F1, or improves it on some configurations.
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: frequency prior, ablation, class imbalance

## C03: Logit-Change Transfer Enables Partially Interpretable Forecasting on BART0 but Fails on FLAN-T5
- **Statement**: A trainable logit-based forecasting model that approximates NTK-based logit-change transfer achieves higher F1 than threshold-based forecasting on BART0Large (57.15 vs. 55.75 F1 under Full FT), but fails to outperform threshold on FLAN-T5Large under LoRA or Full FT (36.54 vs. 43.93, 40.91 vs. 48.43).
- **Status**: supported
- **Falsification criteria**: Trainable logit-based forecasting outperforms threshold on FLAN-T5 under LoRA or Full FT fine-tuning.
- **Proof**: [E01, E02]
- **Dependencies**: none
- **Tags**: logit-change transfer, NTK, BART0, FLAN-T5, interpretability

## C04: Replaying Forecasted-Forgotten Examples Reduces Catastrophic Forgetting vs. Random Replay
- **Statement**: Replaying examples predicted to be forgotten by the representation-based forecasting model achieves lower EM Drop Ratio than replaying random examples across all model/tuning configurations in sequential error-fixing (Table 3), achieving 1.634% vs. 5.769% on BART0Large Full FT and 0.301% vs. 3.267% on FLAN-T5Large LoRA.
- **Status**: supported
- **Falsification criteria**: Random replay achieves lower or equal EM Drop Ratio compared to forecasting-guided replay in any primary configuration.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: replay, model refinement, EM drop, catastrophic forgetting

## C05: Representation-Based Forecasting Generalizes to Out-of-Domain Tasks
- **Statement**: Only the representation-based forecasting model with frequency prior improves OOD F1 compared to threshold-based forecasting (50.12 vs. 46.24 on P3-TestOOD), while trainable logit-based forecasting and representation without prior fail to generalize (30.61 and 34.85 respectively, both below 46.24).
- **Status**: supported
- **Falsification criteria**: Another method achieves higher OOD F1 than representation with prior on P3-TestOOD.
- **Proof**: [E04]
- **Dependencies**: C01, C02
- **Tags**: out-of-domain generalization, P3, OOD

## C06: Forecasting-Guided Replay is Computationally Efficient Compared to Ground-Truth Forgetting
- **Statement**: Representation-based forecasting requires 1/6700 of the FLOPs needed to compute ground-truth forgetting by running inference on all upstream examples (1.35×10^10 vs. 9.04×10^14 FLOPs for 3,600 upstream examples under FLAN-T5Large Full FT), while achieving EM Drop comparable to ground-truth replay.
- **Status**: supported
- **Falsification criteria**: The FLOPs of representation-based forecasting exceed 1% of ground-truth inference FLOPs, or the EM Drop ratio of forecasting-guided replay is not within 2× of ground-truth replay EM Drop.
- **Proof**: [E05]
- **Dependencies**: C04
- **Tags**: computational efficiency, FLOPs, scalability
