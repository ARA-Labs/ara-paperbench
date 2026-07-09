# Experiments

## E01: NetHack Fine-tuning with Knowledge Retention Methods
- **Verifies**: C01, C03, C04, C05
- **Setup**:
  - Model: 33M parameter LSTM (Tuyls et al., 2023), hidden_dim=1738, ReLU activations; pre-trained on 115B transitions from AutoAscend via behavioral cloning
  - Hardware: Single A100 NVIDIA GPU; >500M environment steps per 24 hours
  - Dataset: NLD-AA subset, ~8000 Human Monk games; pre-trained weights from https://drive.google.com/uc?id=1tWxA92qkat7Uee8SKMNsj-BV1K9ENExl
  - System: APPO via Sample Factory; Human Monk scenario; encoders frozen during fine-tuning
- **Procedure**:
  1. Load the pre-trained 33M LSTM checkpoint (Tuyls et al., 2023)
  2. Pre-train the critic head only for 500M environment steps (freeze all other parameters)
  3. Fine-tune the full model (with frozen encoders) using APPO with 5 seeds per method
  4. Evaluate all methods: (a) training from scratch, (b) vanilla fine-tuning, (c) Fine-tuning + EWC (coeff 2×10⁶), (d) Fine-tuning + BC (scale 2.0, no decay), (e) Fine-tuning + KS (scale 0.5, decay 0.99998/step)
  5. Log average return every N steps; at end of training generate 1000 trajectories from final checkpoint
  6. Record score, turns, steps, dungeon level, XP level, eating score, gold, scout, sokoban, staircase metrics
- **Metrics**: Average in-game score (primary); dungeon level, turns, Sokoban pit fills (secondary)
- **Expected outcome**:
  - Fine-tuning + KS achieves substantially higher final score than all other methods
  - Fine-tuning + BC is second best, both surpassing the frozen pre-trained model (SOTA ~5K)
  - Vanilla fine-tuning deteriorates significantly below the pre-trained baseline during training
  - EWC shows poor long-term performance (similar to or below pre-trained baseline)
  - Training from scratch achieves lower final score than Fine-tuning + KS and BC
- **Baselines**: Frozen pre-trained model (Tuyls et al. 2023, ~5K), training from scratch, prior work (BC CDGPT5, LDD, From Scratch + KS/BC from Hambro et al. 2022)
- **Dependencies**: none

## E02: Montezuma's Revenge Fine-tuning with Knowledge Retention
- **Verifies**: C01, C02, C04, C05
- **Setup**:
  - Model: PPO + RND architecture from jcwleo/random-network-distillation-pytorch; target and prediction networks outputting 512-dim vectors
  - Hardware: GPU; ~5e7 environment steps total
  - Dataset: Pre-train a PPO+RND agent from scratch until it achieves ~7000 episode reward; collect 500 trajectories for BC buffer
  - System: PPO with RND exploration; pre-train policy on Rooms 7+ only; fine-tune on full game from Room 1
- **Procedure**:
  1. Train a PPO+RND agent from scratch on Montezuma's Revenge until it achieves ~7000 cumulative reward; this is π*
  2. Collect 500 trajectories from π* for the BC replay buffer
  3. Pre-train a new policy on the game restricted to Room 7 onward; this is the policy to fine-tune
  4. Fine-tune on the full game (starting from Room 1) using: (a) scratch, (b) vanilla FT, (c) FT + BC, (d) FT + EWC
  5. Every 5M steps, evaluate Room 7 success rate (success = earn coin, acquire item, or exit via different passage)
  6. Record average return throughout training
- **Metrics**: Average episode return; Room 7 success rate (evaluated every 5M steps)
- **Expected outcome**:
  - Fine-tuning + BC achieves highest average return at end of training (~6000)
  - Fine-tuning + EWC converges faster than vanilla FT but saturates at a lower return
  - Vanilla FT's Room 7 success rate drops sharply in the first 20M steps, before recovering after the agent reaches Room 7
  - BC and EWC maintain stable Room 7 success rate throughout training, close to pre-trained performance
  - All fine-tuning methods achieve higher final return than training from scratch
  - BC diverges from vanilla FT at ~20M steps when the agent first enters Room 7
- **Baselines**: Training from scratch (PPO+RND), vanilla fine-tuning
- **Dependencies**: none

## E03: RoboticSequence Fine-tuning with Knowledge Retention
- **Verifies**: C01, C02, C04, C05
- **Setup**:
  - Model: SAC with 4-layer MLP, 256 neurons each, Leaky-ReLU, layer norm after first layer; separate output head per stage; entropy coefficient auto-tuned
  - Hardware: 8 CPU cores, 30GB RAM per experiment; ~48 hours per run
  - Dataset: Pre-trained policy (SAC trained to 100% success on peg-unplug-side + push-wall); 10K samples for EM; BC buffer from SAC replay buffer at end of each task
  - System: Meta-World; 4-stage sequence (hammer → push → peg-unplug-side → push-wall); T=200 steps max; β=1.5 success reward augmentation; 20 seeds per method, 90% confidence intervals
- **Procedure**:
  1. Pre-train SAC from scratch on the last two tasks (peg-unplug-side, push-wall) until 100% success rate; save as π*
  2. Sample 10K state-action-reward tuples from π* for the EM buffer
  3. Initialize fine-tuning from π* on full 4-stage sequence
  4. Train all methods: (a) from scratch, (b) vanilla FT, (c) FT + EWC (actor_coeff=100), (d) FT + BC (actor_coeff=1), (e) FT + EM (10K protected samples)
  5. Record per-stage success rates throughout training
  6. Compute forward transfer metric (AUC relative to scratch)
- **Metrics**: Overall success rate (fraction of episodes completing all 4 stages); per-stage success rates; forward transfer metric
- **Expected outcome**:
  - Fine-tuning + BC achieves the highest success rate (~80% overall), followed by EM then EWC
  - Vanilla fine-tuning and training from scratch achieve indistinguishable performance, substantially below BC/EM/EWC
  - FAR stages (peg-unplug-side, push-wall) show catastrophic forgetting (success → 0%) within first 100K steps under vanilla FT
  - BC maintains near-100% success on FAR stages throughout training
  - EM recovers FAR stage performance after initial drop
  - KS is not competitive in this setting and is excluded from reporting
- **Baselines**: Training from scratch, vanilla fine-tuning; frozen pre-trained π*
- **Dependencies**: none

## E04: Per-Level Analysis of Forgetting in NetHack (FAR State Evaluation)
- **Verifies**: C03, C04
- **Setup**:
  - Model: Same as E01 (33M LSTM)
  - Hardware: A100 GPU
  - Dataset: 200 AutoAscend game saves per level (Level 4 and Sokoban level); saves generated by running AutoAscend until it reaches the target level
  - System: APPO; evaluate agent from AutoAscend-saved states; report score on top of AutoAscend's score
- **Procedure**:
  1. Use AutoAscend to generate 200 game saves at Level 4 and 200 at Sokoban level
  2. Every 25M training steps, load each of the 200 saves and run the agent from that point
  3. Record incremental score achieved (score above AutoAscend's score at save point)
  4. Compare all methods: scratch, vanilla FT, FT+EWC, FT+BC, FT+KS
- **Metrics**: Average incremental score from Level 4; average Sokoban pit fills (number of filled pits)
- **Expected outcome**:
  - Vanilla FT and training from scratch achieve lower Level 4 performance than pre-trained baseline
  - KS and BC achieve higher Level 4 performance than pre-trained baseline by end of training
  - EWC temporarily improves Level 4 performance but eventually declines
  - Vanilla FT quickly forgets Sokoban behavior (score → ~0); BC maintains Sokoban performance; KS struggles with Sokoban because Sokoban is only in deeper dungeon levels not visited online early in training
  - KS consistently shows highest Level 4 score but lower Sokoban score than BC
- **Baselines**: Pre-trained frozen model, training from scratch
- **Dependencies**: E01

## E05: Comparison of KS vs. BC for Different FPC Instance Types
- **Verifies**: C05
- **Setup**:
  - Model: All three environment models (NetHack LSTM, Montezuma PPO+RND, RoboticSequence SAC)
  - Hardware: As per E01, E02, E03
  - Dataset: As per E01, E02, E03
  - System: Run KS and BC in all three environments; analyze when each fails
- **Procedure**:
  1. Run all experiments from E01, E02, E03 including both KS and BC
  2. For Montezuma's Revenge: omit KS from final plots (pre-analysis shows failure)
  3. For RoboticSequence: omit KS from final plots (pre-analysis shows failure)
  4. Qualitatively analyze: KS applies KL on online data (matches pre-trained on states the online policy visits), BC applies KL on static pre-training data buffer
  5. Document when KS works (imperfect cloning gap: agent visits FAR eventually, matching there is beneficial) vs. fails (state coverage gap: agent visits CLOSE states that π* was never trained on, forcing KL on invalid states)
- **Metrics**: Final performance comparison between KS and BC; qualitative analysis of failure modes
- **Expected outcome**:
  - KS outperforms or matches BC in imperfect cloning gap settings (NetHack)
  - KS underperforms BC in state coverage gap settings (Montezuma's Revenge, RoboticSequence)
  - BC is the more robust default choice across both FPC types
- **Baselines**: Vanilla fine-tuning, EWC
- **Dependencies**: E01, E02, E03

## E06: Log-Likelihood and Representation Analysis of Forgetting in RoboticSequence
- **Verifies**: C06
- **Setup**:
  - Model: SAC policy for RoboticSequence (same as E03)
  - Hardware: 8 CPU cores, 30GB RAM
  - Dataset: Trajectories collected from π* (pre-trained on peg-unplug-side, push-wall)
  - System: Evaluate vanilla fine-tuned policy; compute log-likelihoods and CKA at checkpoints 0, 100K, 500K, and during re-learning
- **Procedure**:
  1. Collect expert trajectories (s, a*) with a* ~ π*(s) on push-wall before fine-tuning
  2. At each checkpoint (0, 100K, 500K steps, and after re-learning), compute log-likelihood log πθ(a*|s) for all expert trajectories
  3. Project state space to 2D via PCA and color-code by log-likelihood
  4. Compute CKA between activations at each layer of the pre-trained vs. fine-tuned policy at multiple checkpoints (collect activations on pre-training trajectories)
  5. Check whether log-likelihoods recover to pre-fine-tuning levels after the policy re-learns push-wall
- **Metrics**: Log-likelihood of expert trajectories under fine-tuned policy; CKA similarity per layer between pre-trained and fine-tuned activations
- **Expected outcome**:
  - Log-likelihoods collapse rapidly in the first 100K steps; success rate goes to 0%
  - Even after re-learning push-wall (~4M steps, success >80%), log-likelihoods do not recover to original values, indicating a qualitatively different policy was learned
  - CKA: later layers change more than early layers; policy network representations change more rapidly than Q-network representations
  - After re-visiting push-wall, early layer CKA recovers somewhat but later layers do not
- **Baselines**: Pre-trained policy (CKA = 1.0 baseline)
- **Dependencies**: E03
