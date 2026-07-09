# Experiments

## E01: Forecasting Forgetting Performance (Table 1)
- **Verifies**: C01, C02, C03
- **Setup**:
  - Model: BART0Large (400M), FLAN-T5Large (780M), FLAN-T53B (3B)
  - Hardware: Not specified in paper (GPU with sufficient memory for each model)
  - Dataset: DPT = 36 P3 tasks (train split), 100 examples per task; DR = P3-Test (8 tasks) for BART0, MMLU validation (57 tasks) for FLAN-T5; DR split 60/40 train/test
  - System: Each online example is fine-tuned separately; 30 steps for LoRA/Full FT, 100 steps for head-only
- **Procedure**:
  1. Evaluate base model f0 on DPT and DR using Exact Match; collect mispredicted examples to form DR; filter DPT to D̂PT (only correctly predicted upstream examples)
  2. Split DR into D^Train_R (60%) and D^Test_R (40%)
  3. For each (xi, yi) ∈ D^Train_R, fine-tune f0 to obtain fi; evaluate fi on D̂PT to get ground-truth forgetting indicators zij
  4. Train each forecasting model (threshold, fixed logit, trainable logit, representation, representation w/o prior) using (D^Train_R, D̂PT, zij)
  5. For each (xi, yi) ∈ D^Test_R, fine-tune f0 to obtain fi; evaluate fi on D̂PT for ground-truth z^test_ij
  6. Run each forecasting model to produce predicted ẑ^test_ij for all (xi, xj) pairs in D^Test_R × D̂PT
  7. Compute binary F1 between ẑ^test_ij and z^test_ij for each method and configuration
- **Metrics**: Binary F1 score for forgetting prediction; evaluated per (model, dataset, fine-tuning setup) combination
- **Expected outcome**:
  - Representation-based forecasting should outperform threshold-based forecasting across most configurations
  - Adding frequency prior should consistently improve representation-based forecasting F1
  - Fixed logit-based forecasting should be competitive when only LM heads are fine-tuned (since the ground-truth kernel is then exact), but degrade under LoRA/Full FT
  - Trainable logit-based forecasting should improve over threshold on BART0 but fail to do so on FLAN-T5 under LoRA/Full FT
- **Baselines**: Threshold-based forecasting (frequency threshold γ tuned on D^Train_R)
- **Dependencies**: none

## E02: Logit-Change Transfer Visualization
- **Verifies**: C03
- **Setup**:
  - Model: FLAN-T5Large
  - Hardware: Not specified
  - Dataset: A specific pair of examples: online example about public relations (FLAN-T5 prediction error) and upstream example about paraphrase detection from P3
  - System: Single gradient step or 100-step head fine-tuning
- **Procedure**:
  1. Select an online learning example (xi, yi) for which f0(xi) ≠ yi
  2. Select an upstream example (xj, yj) ∈ D̂PT
  3. Record logit scores of output tokens for both examples before fine-tuning (f̂0(xi) and f̂0(xj))
  4. Fine-tune f0 on (xi, yi) to obtain fi
  5. Record updated logit scores f̂i(xi) and f̂i(xj)
  6. Compute logit changes Δf̂i(xi) = f̂i(xi) - f̂0(xi) and Δf̂i(xj) = f̂i(xj) - f̂0(xj)
  7. Examine whether tokens that change most in xi also change substantially in xj
- **Metrics**: Absolute logit change per output token for both xi and xj; whether prediction of xj flips (forgetting indicator)
- **Expected outcome**:
  - Tokens with large logit changes in xi should also show measurable (though smaller) changes in xj
  - The logit change transfer should be sufficient to flip the prediction of xj from correct to incorrect
- **Baselines**: none
- **Dependencies**: none

## E03: Practical Utility via Targeted Replay (Tables 3 and 4)
- **Verifies**: C04
- **Setup**:
  - Model: BART0Large (Full FT), FLAN-T5Large (Full FT and LoRA), FLAN-T53B (LoRA)
  - Hardware: Not specified
  - Dataset: Same as E01; sequential fixing of all examples in D^Test_R for Table 3; single-error fixing for Table 4
  - System: Replay mini-batches from D̂PT every 10 steps (every 5 for FLAN-T53B)
- **Procedure**:
  1. Evaluate each forecasting model on D^Test_R × D̂PT to produce predicted forgetting sets
  2. For sequential refinement (Table 3): process examples in D^Test_R one at a time; after each error fix, evaluate Edit Success Rate and EM Drop on DPT
  3. For each refinement step, replay a mini-batch of 8 (or 4 for FLAN-T53B) examples from D̂PT selected by the forecasting method (random / threshold / trainable logit / representation / GT), using distillation loss against base model f0
  4. Record final Edit Success Rate after processing all D^Test_R and EM Drop Ratio at the end of the stream
  5. Repeat for single-error fixing (Table 4): compute average EM Drop across all separate fine-tuning runs
- **Metrics**: Edit Success Rate (%), EM Drop Ratio (%); lower EM Drop is better while maintaining high edit success rate
- **Expected outcome**:
  - Forecasting-guided replay (any method) should achieve lower EM Drop than Vanilla FT
  - Representation-based replay should achieve lower EM Drop than random replay
  - Ground-truth replay should provide the best forgetting reduction as an oracle upper bound
  - Forecasting-guided replay should outperform or match MIR and OCS baselines
- **Baselines**: Vanilla FT (no replay), Random replay, MIR, OCS, GT Forget replay (oracle)
- **Dependencies**: E01

## E04: Out-of-Domain Generalization of Forecasting Models (Table 2)
- **Verifies**: C05
- **Setup**:
  - Model: BART0Large with Full FT
  - Hardware: Not specified
  - Dataset: P3-Test split into P3-TestID (SuperGlue-Cb, SuperGlue-RTE, SuperGLUE-wsc.fixed, SuperGlue-Copa, SuperGlue-wic) and P3-TestOOD (storycloze, hellaswag, anli, winograde-xl)
  - System: Same as E01 for BART0 Full FT setting
- **Procedure**:
  1. Use P3-TestID as D^Train_R and P3-TestOOD as D^Test_R (no overlap between ID and OOD tasks)
  2. Train forecasting models on ID data using same procedure as E01
  3. Evaluate forecasting models on OOD test data; compute binary F1 on both splits
- **Metrics**: Binary F1 on P3-TestID (in-domain) and P3-TestOOD (out-of-domain)
- **Expected outcome**:
  - Representation-based forecasting with frequency prior should be the only method to improve OOD F1 over threshold-based forecasting
  - Methods without the frequency prior or relying purely on logit-change dynamics should fail to generalize OOD
  - ID performance of all trainable methods should exceed threshold
- **Baselines**: Threshold-based forecasting (46.24 OOD F1 expected)
- **Dependencies**: E01

## E05: Computational Efficiency Analysis (Tables 5, 8)
- **Verifies**: C06
- **Setup**:
  - Model: FLAN-T5Large (Full FT as worst case)
  - Hardware: GPU with FLOP counting support
  - Dataset: 36 upstream tasks × 100 examples = 3,600 total upstream examples; 1 online learning example
  - System: Compare FLOP counts across methods
- **Procedure**:
  1. Profile actual FLOPs for representation-based forecasting on 3,600 upstream examples given one online example
  2. Profile FLOPs for trainable logit-based forecasting on same setup
  3. Profile FLOPs for obtaining ground-truth forgetting by running full LM inference on all 3,600 upstream examples with updated model fi
  4. Compare computational complexity formulas: Threshold O(NPT), Representation O(NPTH), Trainable Logit O(NPTT²(H+V)), GT Head O(NPTTV), GT Full FT O(Fw(N))
  5. Verify that representations/logits of upstream examples can be pre-computed and cached once, enabling amortization across multiple online examples
- **Metrics**: Total FLOPs per query (one online example vs. 3,600 upstream examples); ratio of forecasting FLOPs to GT inference FLOPs
- **Expected outcome**:
  - Representation-based forecasting should use substantially fewer FLOPs than ground-truth inference (expected ~1/6700 ratio)
  - Trainable logit-based forecasting should use more FLOPs than representation-based but still fewer than GT Full FT
  - All forecasting methods should show dramatically lower cost than GT Full FT
- **Baselines**: Ground-truth inference (GT Head and GT Full FT)
- **Dependencies**: E01
