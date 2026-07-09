# Constraints and Boundary Conditions

## Applicability Constraints

### BC1: FPC requires an RL feedback loop
- **Condition**: FPC only occurs when the agent's actions determine future state visitation. In i.i.d. supervised learning, the data distribution is fixed; forgetting of non-training-distribution examples does not affect downstream performance.
- **Implication**: The paper's findings are specific to RL; the supervised learning conventional wisdom (forgetting doesn't matter for downstream performance) does not apply.

### BC2: FAR states must be reachable only through CLOSE
- **Condition**: The CLOSE/FAR partition is meaningful only when FAR states are not directly accessible at training start. If FAR states are visited from the beginning (e.g., when pre-trained skills are needed from step 1), no forgetting occurs and vanilla fine-tuning works.
- **Evidence**: Figure 24 (RoboticSequence with known tasks at the start) shows no FPC when FAR = first tasks in sequence.

### BC3: Episodic Memory (EM) requires an off-policy replay buffer
- **Condition**: EM can only be trivially applied with off-policy algorithms (SAC, DQN). PPO and APPO (on-policy) cannot use EM without significant instability.
- **Implication**: EM is reported only for RoboticSequence (SAC); not reported for Montezuma (PPO) or NetHack (APPO).

### BC4: KS fails for State Coverage Gap
- **Condition**: Kickstarting applies the KL divergence on states visited by the current online policy. When state coverage gap is present, the online policy initially visits CLOSE states on which π* was never trained, making KL(π*(s) ‖ πθ(s)) undefined or harmful.
- **Implication**: KS is not reported for Montezuma's Revenge or RoboticSequence.

### BC5: Knowledge retention is applied only to the actor, not the critic
- **Condition**: All retention methods (EWC, BC, KS) are applied only to the policy (actor) network parameters. The critic is not regularized.
- **Rationale**: Only actor behavior on FAR states matters for downstream performance; critic forgetting doesn't directly impact policy rollouts.

## Known Limitations

### L1: Simple retention methods used
- The paper uses standard first-generation retention methods. More sophisticated continual learning methods (parameter isolation, modular networks, memory-aware synapses) may achieve better results.

### L2: Knowledge retention can harm if pre-trained policy is suboptimal on FAR
- If the pre-trained policy is actually suboptimal on FAR states (or if FAR state behavior should be unlearned), retention methods will prevent the policy from improving there. No mechanism to selectively preserve only beneficial pre-trained behaviors is studied.

### L3: No study of very large models
- The paper focuses on models up to 33M parameters. Parameter-efficient fine-tuning (LoRA, adapter layers) for models >1B parameters is out of scope.

### L4: Focus on two specific FPC scenarios
- Only SCG and ICG are studied. Real-world settings may exhibit other forms of distribution shift not covered.

### L5: Single-task fine-tuning only
- The paper studies fine-tuning to a single stationary downstream task. Multi-task fine-tuning and generalization to unseen goals are not the primary focus.

### L6: NetHack experiments limited to Human Monk character
- Due to computational constraints, only the Human Monk scenario is studied. Generalization to other NetHack roles is untested.

### L7: Network size effects are complex in RL
- Unlike supervised continual learning where larger networks forget less, no clear correlation between network size and forgetting is found for RL (Appendix F, Figure 27). EWC tends to fail with very small (2-layer) networks.

## Assumptions for FPC to be Severe

1. The size of CLOSE (amount of time before FAR is reached) is large enough that significant gradient interference accumulates
2. FAR and CLOSE states share enough representational overlap that CLOSE-gradient updates interfere with FAR representations
3. The distribution gap between FAR and CLOSE states is in the intermediate range (Lee et al., 2021: intermediate similarity causes most forgetting)
