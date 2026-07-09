# Constraints

## Boundary Conditions

### BC1: Warm-Start Requirement (Assumption 3.2)
- **Condition**: The pre-trained policy π must have sufficient state coverage such that $\|d^{\pi^*}/d^\pi_\rho\|_\infty \leq C$ for some finite constant C.
- **Implication**: RICE does not work in "cold-start" settings where the pre-trained agent has very poor coverage (e.g., MountainCar — Appendix E). In such cases, RICE degenerates to plain RND exploration.
- **Test**: Check whether the pre-trained agent can reliably reach a diverse set of environment states.

### BC2: Simulator-Based Environment Required
- **Condition**: The environment must support state reset to arbitrary previously visited states.
- **Implication**: Cannot be directly applied in real-world physical systems where deterministic state restoration is impossible. Workaround: goal/state-conditioned policy with sub-goals (Ecoffet et al., 2021).
- **Note**: All evaluated environments (MuJoCo, MetaDrive, CAGE, Malware RL, Selfish Mining) are simulator-based.

### BC3: Pre-Trained Policy Must Outperform Random (Assumption 3.1)
- **Condition**: $\mathbb{E}_{a \sim \pi_r}[A^\pi(s,a)] \leq 0, \forall s$
- **Implication**: RICE requires a reasonably good pre-trained policy. The explanation method is only meaningful when the policy has learned something useful.

### BC4: Unknown Training Algorithm of Pre-Trained Policy
- **Condition**: RICE does not require knowledge of the original training algorithm.
- **Implication**: The pre-trained policy may have been trained with SAC, PPO, or other algorithms. For non-PPO policies, GAIL is used to obtain a PPO-compatible approximation (Experiment IV).

## Known Limitations

### L1: Critical State Filtering Not Considered
- States identified as critical may already have converged to optimal behavior. Resetting to these states provides little additional learning benefit. Future work: filter by TD error or policy convergence metrics.

### L2: Single Critical State Per Trajectory
- Algorithm 2 selects only the single most critical state per trajectory. This may miss other important states in the same episode. Extension to top-K critical states is possible but not evaluated.

### L3: Non-Markovian Reward Designs
- Reward functions that depend on initial state s_0 rather than current state s_t (discovered in MalConv, Appendix D) violate MDP assumptions and reduce PPO-based refining effectiveness. Requires reward debugging before RICE can be applied.

### L4: Requires Simulator for Fidelity Evaluation
- The fidelity score metric requires the ability to fast-forward trajectories and randomize specific actions, which requires full environment access.
