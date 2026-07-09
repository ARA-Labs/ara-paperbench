---
# Concepts

## Split and Aggregate Policy Gradients (SAPG)
- **Notation**: SAPG; M policies π₁, …, πM over N environments
- **Definition**: An on-policy RL algorithm that divides N parallel environments into M blocks of N/M environments each. Each block runs a separate policy. One policy is designated the "leader" (i=1) and aggregates importance-sampled data from all M−1 "followers" in addition to its own on-policy data. Followers update only on their own block's data. The combined loss is L(πi) = Lon(πi) + λ·Loff(πi; X).
- **Boundary conditions**: Effective when N >> typical RL batch sizes (e.g., N ≥ 10,000); degenerates to standard PPO when M=1 or when off-policy term is removed.
- **Related concepts**: Leader Policy, Follower Policy, Off-policy Importance Sampling Correction, Latent Conditioning

## Leader Policy
- **Notation**: π₁; backbone parameters θ, ψ; hanging parameter ϕ₁
- **Definition**: The single policy in SAPG that receives both on-policy data from its own N/M environments AND importance-sampled off-policy data from all followers (X = {2, 3, …, M}). Updated with L(π₁) = Lon(π₁) + λ·Loff(π₁; {2,…,M}). Off-policy data is subsampled to match on-policy data size (equal 50/50 split per mini-batch).
- **Boundary conditions**: Exactly one leader exists; the leader does not have an entropy regularization term.
- **Related concepts**: Follower Policy, Off-policy Importance Sampling Correction, SAPG

## Follower Policy
- **Notation**: πj, j ∈ {2, …, M}; hanging parameter ϕj
- **Definition**: Each of the M−1 non-leader policies in SAPG. Each follower runs on its own block of N/M environments and is updated only with standard PPO on-policy loss: L(πj) = Lon(πj) + λent(j−1)·H(πj(a|s)). Followers do NOT receive off-policy data from other policies. Different followers have different entropy coefficients to encourage diverse exploration.
- **Boundary conditions**: M−1 followers exist in the leader-follower variant; in symmetric variant all policies are treated equally.
- **Related concepts**: Leader Policy, Entropy Regularization, Latent Conditioning

## Off-policy Importance Sampling Correction
- **Notation**: μ = πi,old(s,a) / πj(s,a); ratio rπi(s,a) = πi(s,a) / πj(s,a)
- **Definition**: When updating leader policy πi using data collected by follower policy πj, the importance weight corrects for the distributional mismatch. The off-policy actor loss is: Loff(πi; X) = (1/|X|) Σⱼ∈X E[(s,a)~πj][min(rπi, clip(rπi, μ(1−ε), μ(1+ε))) · Aπi,old(s,a)] where μ = πi,old(s,a)/πj(s,a) is the off-policy correction term. When i=j this reduces to the standard PPO on-policy update.
- **Boundary conditions**: Only applied to off-policy transitions; on-policy transitions use μ=1 (standard PPO clip). High off-policy ratios (no subsampling) degrade performance on simpler tasks.
- **Related concepts**: Leader Policy, SAPG, PPO Clipped Surrogate Objective

## PPO Clipped Surrogate Objective
- **Notation**: Lon(πθ); rt(πθ) = πθ(at|st)/πold(at|st); ε = clipping parameter
- **Definition**: Lon(πθ) = E_πold[min(rt(πθ), clip(rt(πθ), 1−ε, 1+ε)) · Aπold]. Restricts policy updates to an approximate trust region around πold by clipping the probability ratio. Used for each policy's on-policy update in SAPG.
- **Boundary conditions**: ε = 0.1 for AllegroKuka and ShadowHand; ε = 0.2 for AllegroHand. Requires on-policy data; degrades if applied naively to highly off-policy data without IS correction μ.
- **Related concepts**: Off-policy Importance Sampling Correction, SAPG

## Latent Conditioning (Hanging Parameters)
- **Notation**: ϕj ∈ R^d; shared backbone Bθ for actor, Cψ for critic; d=32 for AllegroKuka, d=16 for ShadowHand/AllegroHand
- **Definition**: All M policies share a common backbone network (Bθ for actor, Cψ for critic). Each policy πj is conditioned on its own learnable "hanging parameter" vector ϕj that is concatenated with or injected into the backbone. Parameters θ, ψ are updated by gradients from all policies; ϕj is updated only by gradients from policy j's objective. This encourages knowledge sharing while maintaining policy diversity.
- **Boundary conditions**: Hanging parameter dimension chosen based on task complexity (32 for complex LSTM tasks, 16 for simpler MLP tasks). Sigma (action std dev) is also per-policy learnable vector when entropy regularization is used.
- **Related concepts**: Follower Policy, Leader Policy, Entropy Regularization

## Entropy Regularization for Diversity
- **Notation**: λent(j−1)·H(πj(a|s)); H(π) = −E[log π(a|s)]
- **Definition**: An entropy bonus added to the loss of each follower policy j with coefficient λent(j−1) that scales with follower index. Followers with large entropy coefficients explore more aggressively (wider distribution); those with small coefficients stay close to optimal trajectories. The leader has no entropy term (λent = 0 for leader). Tuned from {0, 0.003, 0.005}.
- **Boundary conditions**: Best σ = 0 for AllegroHand, Regrasping, Throw. Best σ = 0.005 for ShadowHand and Reorientation. Per-block learnable sigma vector enables different entropy levels when entropy exploration is active.
- **Related concepts**: Follower Policy, SAPG

## n-step Return (On-policy Critic Target)
- **Notation**: V^target_on,πj(st) = Σ_{k=t}^{t+2} γ^{k−t} r_k + γ³ Vπj,old(st+3); n=3
- **Definition**: The critic value target for on-policy transitions uses 3-step bootstrapped returns to reduce variance while maintaining a reasonable bias-variance trade-off. Used only for the leader's on-policy data and each follower's own data.
- **Boundary conditions**: Only applicable to on-policy data where sequential step access is available. Off-policy data uses 1-step return instead (Eq 6).
- **Related concepts**: Off-policy 1-step Return, Combined Critic Loss

## Off-policy 1-step Return (Off-policy Critic Target)
- **Notation**: V^target_off,πj(s't) = r_t + γ Vπj,old(s't+1)
- **Definition**: For off-policy transitions (follower data used to update leader critic), only a 1-step bootstrapped return is used as the value target, because the temporal structure of the off-policy trajectory cannot be assumed to match the policy being updated. This avoids bias from multi-step off-policy corrections.
- **Boundary conditions**: Applied exclusively to off-policy transitions in the leader's critic update; n-step returns are used for on-policy data.
- **Related concepts**: n-step Return, Combined Critic Loss, Off-policy Importance Sampling Correction

## Symmetric Aggregation
- **Notation**: ∀i: X = {1, …, M} \ {i}; λ = 1 with equal-size subsampling
- **Definition**: An alternative SAPG variant where there is no privileged leader — each policy i is updated with off-policy data from ALL other policies X = {1, 2, …, i−1, i+1, …, M}. Each policy also uses its own on-policy data. Off-policy data is subsampled to match on-policy data size. This contrasts with the leader-follower scheme where only policy 1 (leader) receives off-policy data.
- **Boundary conditions**: Empirically inferior to leader-follower because it causes policies to converge in behavior, reducing data diversity and defeating the purpose of having separate policies.
- **Related concepts**: Leader Policy, Follower Policy, SAPG
