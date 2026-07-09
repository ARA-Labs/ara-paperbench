# Problem Specification

## Observations

### O1: Fine-tuning RL models frequently fails to leverage pre-trained knowledge
- **Statement**: Unlike supervised learning where fine-tuning reliably transfers knowledge, vanilla fine-tuning in RL often results in performance equal to or worse than training from scratch. In NetHack, vanilla fine-tuning achieves only ~1K average return by end of training versus ~5K for the frozen pre-trained model.
- **Evidence**: Figure 3a (NetHack performance curves), Table 4 (Fine-tuning score 7756 vs. From scratch 6696 at last checkpoint, but training curves show early collapse below the pre-trained baseline)
- **Implication**: RL fine-tuning has a structural problem not present in supervised learning; the standard recommendation to "just fine-tune" does not transfer from NLP/CV.

### O2: The RL feedback loop creates non-stationary state visitation during fine-tuning
- **Statement**: In RL, the states visited by the agent depend on its current policy. When fine-tuning on a downstream task, the agent initially visits only easy "CLOSE" states. States in "FAR" (reachable only after mastering CLOSE) are not visited early, even if the pre-trained policy was competent there.
- **Evidence**: Figure 4 (density plots showing pre-trained policy π* rarely leaves Level 1 of NetHack, while AutoAscend expert visits many levels); Section 2, conceptual analysis
- **Implication**: Gradient updates on CLOSE states interfere with the function approximator's representation for FAR states, causing forgetting even though the downstream task's stationary distribution includes FAR.

### O3: Forgetting of FAR-state behavior is rapid and often catastrophic
- **Statement**: In RoboticSequence, the success rate on FAR stages (peg-unplug-side, push-wall) collapses to 0% within the first 100K fine-tuning steps. In Montezuma's Revenge, Room 7 success rate drops significantly within the first 20M steps of vanilla fine-tuning.
- **Evidence**: Figure 7 (RoboticSequence per-stage success rates), Figure 6 (Montezuma Room 7 success rate), Figure 8 (log-likelihood collapse on push-wall trajectories)
- **Implication**: The forgetting is not gradual degradation but catastrophic collapse, making recovery difficult.

### O4: Even after re-learning, the final policy differs from the pre-trained one
- **Statement**: Log-likelihood of expert trajectories under the fine-tuned policy on push-wall does not recover to original values even after the policy re-learns the task. This indicates the agent learned a qualitatively different policy rather than recovering the pre-trained one.
- **Evidence**: Figure 8 (log-likelihood PCA projections at 0, 100K, 500K steps), Appendix F analysis
- **Implication**: FPC is irreversible under vanilla fine-tuning; transfer benefits are permanently lost.

### O5: FPC occurs even in simple 2-state MDPs
- **Statement**: Toy 2-state MDPs with specific parameterizations exhibit both state coverage gap and imperfect cloning gap, showing FPC is a fundamental property of gradient-based optimization on parametric policies, not an artifact of deep networks.
- **Evidence**: Figure 9 (toy MDP analysis), Appendix A (APPLERETRIEVAL gridworld experiments)
- **Implication**: The problem has a theoretical basis rooted in function approximator interference, independent of scale.

## Gaps

### G1: Lack of conceptualization of FPC in the RL fine-tuning literature
- **Statement**: Prior work on RL fine-tuning (Baker et al. 2022, Kumar et al. 2022, Seo et al. 2022) implicitly uses knowledge retention but does not identify FPC as the root cause, nor systematically study it.
- **Caused by**: O1, O2
- **Existing attempts**: Baker et al. (2022) adds a regularization term; Kumar et al. (2022) mixes old and new data; Seo et al. (2022) uses modularity
- **Why they fail**: These are ad-hoc solutions not informed by the underlying mechanism; practitioners don't know when or why to apply them.

### G2: No systematic evaluation of knowledge retention methods for RL fine-tuning
- **Statement**: No prior work comprehensively compares EWC, BC, KS, and EM specifically for the fine-tuning transfer scenario across multiple RL environments.
- **Caused by**: O1, G1
- **Existing attempts**: Individual continual RL papers test methods for multi-task sequences, not single-task fine-tuning
- **Why they fail**: Continual RL assumes we care about all tasks; fine-tuning only cares about the downstream task—different objective.

## Key Insight

- **Insight**: The interplay between actions and observations in RL creates a non-stationary data distribution during fine-tuning that mimics the task-sequence non-stationarity studied in continual learning. Therefore, continual learning's knowledge retention methods directly address the root cause of poor RL fine-tuning.
- **Derived from**: O1, O2, O3
- **Enables**: Directly applying EWC, behavioral cloning loss, kickstarting, and episodic memory from the continual learning literature to RL fine-tuning, achieving SOTA results with minimal implementation overhead.

## Assumptions

- A1: The downstream task's state space can be approximately partitioned into CLOSE (reachable early) and FAR (reachable only after mastering CLOSE) subsets.
- A2: The pre-trained policy has meaningful competence on FAR states that would be beneficial for the downstream task.
- A3: Knowledge retention methods are applied only to the actor (policy network), not the critic.
- A4: The downstream task is a single stationary MDP (not a sequence of tasks).
- A5: Models are not extremely large (>1B parameters); parameter-efficient fine-tuning methods like LoRA are out of scope.
