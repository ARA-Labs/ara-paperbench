# Experiments

## E01: Fidelity and Efficiency of Optimized StateMask vs Original StateMask
- **Verifies**: C03
- **Setup**:
  - Model: Pre-trained PPO policy for each of the 8 environments
  - Hardware: 8 NVIDIA A100 GPUs
  - Dataset: 500 trajectories per environment, 3 random seeds
  - System: Fixed number of training samples per environment (see Table 4: 3×10^5 for MuJoCo games, 1.5×10^6 for Selfish Mining, 1×10^7 for CAGE, 2,443,260 for Auto Driving, 32,349 for Malware)
- **Procedure**:
  1. Train original StateMask mask network using primal-dual optimization on each environment's pre-trained policy.
  2. Train RICE's optimized mask network using PPO with reward R′ = R + α·am_t (α from Table 3; default α=0.0001).
  3. For each trained mask network, run 500 trajectories from each environment.
  4. Apply sliding window of width l over each trajectory (K = 10%, 20%, 30%, 40% of trajectory length L).
  5. Select the window with highest average importance score; randomize actions at those steps.
  6. Measure average reward change d and maximum possible reward change d_max.
  7. Compute fidelity score: log(d/d_max) − log(l/L).
  8. Report mean and standard deviation over 3 seeds.
  9. Record wall-clock training time for a fixed sample budget (Table 4 values).
- **Metrics**: Fidelity score (higher = better); training time in seconds for fixed sample budget.
- **Expected outcome**:
  - Optimized StateMask fidelity scores are comparable to original StateMask (not significantly lower or higher).
  - Both methods significantly outperform Random explanation baseline in fidelity.
  - Optimized StateMask trains noticeably faster than original StateMask across all environments (reduction in wall-clock time).
- **Baselines**: Original StateMask (primal-dual), Random explanation (random state selection)
- **Dependencies**: none

## E02: Effectiveness of RICE Refining vs Baseline Refining Methods (Dense Reward Environments)
- **Verifies**: C02
- **Setup**:
  - Model: Pre-trained PPO policy for each of 8 environments; PPO refining agent
  - Hardware: 8 NVIDIA A100 GPUs
  - Dataset: 8 environments (Hopper-v3, Walker2d-v3, Reacher-v2, HalfCheetah-v3, Selfish Mining, CAGE Challenge 2, MetaDrive Macro-v1, MalConv Malware)
  - System: Default hyperparameters from Table 3; all methods use the same RICE explanation for critical state identification (fair comparison)
- **Procedure**:
  1. Pre-train policy π on each environment using PPO (Stable-Baselines3).
  2. Train optimized StateMask mask network (Algorithm 1) to identify critical states.
  3. Implement four refining methods: (a) PPO fine-tuning (reduced learning rate, continue PPO), (b) StateMask-R (reset exclusively to critical states, continue training), (c) JSRL (initialize πe = πg, curriculum-guided), (d) RICE/Ours (Algorithm 2: mixed distribution with p, RND with λ).
  4. For each method, refine the pre-trained policy from the same checkpoint.
  5. Measure final reward after refining; report mean and standard deviation over 3 seeds.
  6. For Malware Mutation, report evasion probability (%) as the metric.
  7. For CAGE Challenge 2, report sum of average rewards across 3 episode lengths (30, 50, 100).
- **Metrics**: Final episode reward (mean ± std over 3 seeds); higher is better except CAGE Challenge 2 (less negative is better) and Reacher (less negative is better).
- **Expected outcome**:
  - RICE (Ours) achieves the highest final reward among all refining methods for each environment.
  - PPO fine-tuning shows only marginal improvements (trapped in local optima).
  - StateMask-R sometimes degrades performance relative to no-refine baseline (overfitting).
  - JSRL underperforms RICE substantially.
- **Baselines**: PPO fine-tuning, StateMask-R, JSRL, No Refine (baseline)
- **Dependencies**: E01

## E03: Impact of Explanation Quality on Refining Performance
- **Verifies**: C01, C02
- **Setup**:
  - Model: Same as E02, fixed refining method = RICE/Ours
  - Hardware: 8 NVIDIA A100 GPUs
  - Dataset: All 8 environments
  - System: Fixed refining method (RICE Algorithm 2) with hyperparameters from Table 3; vary explanation method
- **Procedure**:
  1. For each environment, train three explanation methods: Random (random state selection), original StateMask, and optimized StateMask (Ours).
  2. For each explanation method, apply RICE refining (Algorithm 2) using the identified critical states.
  3. Measure final reward after refining for each (refining method = fixed Ours, explanation method varies).
  4. Report mean and standard deviation over 3 seeds.
- **Metrics**: Final episode reward (mean ± std); same as E02.
- **Expected outcome**:
  - Refining with Ours explanation achieves the highest final reward across all environments.
  - Refining with original StateMask explanation is close to Ours (comparable performance).
  - Refining with Random explanation significantly underperforms both StateMask and Ours.
  - This validates Claim 1: better explanation → smaller mismatch coefficient → better refining.
- **Baselines**: Random explanation, original StateMask explanation
- **Dependencies**: E01, E02

## E04: Generalization to Non-PPO Pretrained Agents (SAC + GAIL)
- **Verifies**: C06
- **Setup**:
  - Model: SAC agent pre-trained on Hopper-v3; GAIL policy network approximating the SAC agent
  - Hardware: 8 NVIDIA A100 GPUs
  - Dataset: MuJoCo Hopper-v3 (dense reward)
  - System: Pre-train SAC for 1M steps; apply GAIL to obtain PPO-compatible policy; refine for 1M steps
- **Procedure**:
  1. Pre-train a SAC agent on Hopper-v3 for 1M steps (pre-training phase).
  2. Apply GAIL (generative adversarial imitation learning) to learn an approximated PPO-compatible policy network from the SAC agent's demonstrations.
  3. Refine the GAIL-approximated policy using five methods: (a) RICE/Ours, (b) PPO fine-tuning, (c) JSRL, (d) StateMask-R, (e) SAC fine-tuning of the original SAC agent.
  4. Track reward curve over 1M refining steps.
  5. Compare final reward and convergence speed across methods.
- **Metrics**: Episode reward (mean) throughout refining; final reward at 1M refining steps.
- **Expected outcome**:
  - RICE (Ours) achieves the highest reward among all refining methods by the end of the refining phase.
  - PPO fine-tuning outperforms SAC fine-tuning (switching algorithm helps escape bottleneck).
  - SAC fine-tuning also shows training bottleneck behavior despite algorithm consistency.
- **Baselines**: PPO fine-tuning, JSRL, StateMask-R, SAC fine-tuning
- **Dependencies**: E02

## E05: Hyperparameter Sensitivity Analysis (p, λ, α)
- **Verifies**: C04, C05
- **Setup**:
  - Model: Pre-trained PPO policies for all 8 dense environments
  - Hardware: 8 NVIDIA A100 GPUs
  - Dataset: All 8 environments; also 3 sparse MuJoCo environments (SparseHopper, SparseWalker2d, SparseHalfCheetah)
  - System: RICE refining method; sweep over hyperparameter values
- **Procedure**:
  1. Vary p ∈ {0, 0.25, 0.5, 0.75, 1.0} while fixing λ at each environment's default value; measure final reward.
  2. Vary λ ∈ {0, 0.1, 0.01, 0.001} while fixing p at each environment's default value; measure final reward.
  3. Vary α ∈ {0.01, 0.001, 0.0001} for the mask network; measure fidelity scores and final reward after refining.
  4. For Hopper with SAC/GAIL pretrained agent, additionally report sensitivity curves of p and λ.
  5. Report final reward under each hyperparameter setting.
- **Metrics**: Final episode reward for p/λ sweep; fidelity score for α sweep.
- **Expected outcome**:
  - p=0 (pure default init) and p=1 (pure critical state init) produce lower performance than any intermediate p.
  - p ∈ {0.25, 0.5} tends to produce best performance across environments.
  - Any λ > 0 provides noticeable improvement over λ = 0; λ = 0.01 generally best.
  - α does not significantly affect fidelity score (low sensitivity).
- **Baselines**: p=0 (no critical states), λ=0 (no exploration)
- **Dependencies**: E02
