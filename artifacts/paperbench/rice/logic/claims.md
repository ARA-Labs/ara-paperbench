# Claims

## C01: RICE Achieves a Tighter Sub-Optimality Bound via Explanation-Guided Mixed Distribution
- **Statement**: The RICE refining method, using MaskNet-identified critical states in a mixed initial distribution µ(s) = β·dˆπρ(s) + (1−β)ρ(s), achieves a tighter upper bound on the sub-optimality gap V^π*(ρ) − V^π′(ρ) than random-explanation-based mixed distribution.
- **Status**: supported
- **Falsification criteria**: If the distribution mismatch coefficient ||dπ*/dˆπρ||∞ is not smaller than ||dπ*/dπρ||∞, or if RICE's performance improvement over the random baseline is not statistically significant.
- **Proof**: [E01, E03]
- **Dependencies**: none
- **Tags**: theory, sub-optimality, mixed distribution, StateMask

## C02: RICE Outperforms All Baseline Refining Methods Across All 8 Environments
- **Statement**: RICE (using optimized StateMask + mixed distribution + RND) achieves higher final reward than PPO fine-tuning, StateMask-R, and JSRL in all 8 benchmark environments (Hopper, Walker2d, Reacher, HalfCheetah, Selfish Mining, CAGE Challenge 2, Autonomous Driving, Malware Mutation).
- **Status**: supported
- **Falsification criteria**: Any environment where RICE does not achieve the highest final reward (mean) among all refining methods.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: main result, refining, PPO, JSRL, StateMask-R, dense rewards

## C03: Optimized StateMask Has Comparable Fidelity to Original StateMask with ~16.8% Faster Training
- **Statement**: The simplified mask network (J(θ) = max η(π̄) + blinding bonus R′ = R + α·am_t, trained with vanilla PPO) achieves fidelity scores statistically comparable to original StateMask across all 8 environments and K ∈ {10%, 20%, 30%, 40%}, while reducing average mask network training time by 16.8%.
- **Status**: supported
- **Falsification criteria**: If fidelity scores differ significantly between the two methods, or if no time reduction is observed.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: explanation, fidelity, efficiency, StateMask, mask network

## C04: Mixed Initial State Distribution (0 < p < 1) Outperforms Extremes (p=0 and p=1)
- **Statement**: Setting p ∈ (0, 1) (mixing default initial states and critical states) achieves higher final reward than either p=0 (all default) or p=1 (all critical states), across all tested environments. Optimal p is 0.25 or 0.5 depending on the environment.
- **Status**: supported
- **Falsification criteria**: Any environment where p=0 or p=1 achieves performance comparable to or better than all intermediate p values.
- **Proof**: [E05]
- **Dependencies**: C01
- **Tags**: hyperparameter, mixed distribution, overfitting prevention

## C05: Exploration Bonus (λ > 0 via RND) Significantly Improves Refining
- **Statement**: Any λ > 0 provides a noticeable improvement over λ = 0 (no exploration). The specific value of λ has lower sensitivity; λ = 0.01 yields the best performance in most environments.
- **Status**: supported
- **Falsification criteria**: λ = 0 achieves performance comparable to λ > 0, indicating exploration adds no benefit.
- **Proof**: [E05]
- **Dependencies**: C02
- **Tags**: RND, exploration, hyperparameter, sensitivity

## C06: RICE Generalizes to Non-PPO Pretrained Agents via GAIL Transfer
- **Statement**: RICE can refine a pre-trained SAC agent (after GAIL imitation learning to obtain a PPO-compatible policy) and achieves higher reward than PPO fine-tuning, JSRL, StateMask-R, and SAC fine-tuning baselines in the Hopper environment.
- **Status**: supported
- **Falsification criteria**: RICE fails to outperform SAC fine-tuning or the other PPO-based baselines when applied to a GAIL-imitated SAC policy.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: generalization, SAC, GAIL, algorithm-agnostic
