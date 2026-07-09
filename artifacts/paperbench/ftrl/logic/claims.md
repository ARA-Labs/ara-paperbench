# Claims

## C01: Vanilla RL fine-tuning fails to leverage pre-trained capabilities due to FPC
- **Statement**: Fine-tuning a pre-trained RL agent on a downstream task using standard RL (without knowledge retention) will, in most practical scenarios, result in performance comparable to or worse than training from scratch at the end of training, due to catastrophic forgetting of pre-trained capabilities on FAR states.
- **Status**: supported
- **Falsification criteria**: A majority of RL fine-tuning benchmarks show vanilla fine-tuning consistently outperforming training from scratch without any knowledge retention mechanism.
- **Proof**: [E01, E02, E03]
- **Dependencies**: none
- **Tags**: forgetting, fine-tuning, RL, catastrophic forgetting

## C02: State coverage gap is a common and catastrophic instance of FPC
- **Statement**: When a pre-trained agent is competent on FAR states but not on CLOSE states, fine-tuning will cause catastrophic forgetting of FAR-state behavior before the agent learns CLOSE. In RoboticSequence, the success rate on FAR stages collapses to 0% within 100K steps.
- **Status**: supported
- **Falsification criteria**: Pre-trained agents fine-tuned on tasks where they are initially incompetent on CLOSE states maintain their FAR-state performance during the early fine-tuning phase.
- **Proof**: [E03, E04]
- **Dependencies**: C01
- **Tags**: state coverage gap, RoboticSequence, Montezuma's Revenge, forgetting

## C03: Imperfect cloning gap is a common and catastrophic instance of FPC
- **Statement**: When the pre-trained agent is a perturbed version of an expert (e.g., trained by behavioral cloning from a superior rule-based agent), small policy imperfections cause distribution shift that prevents the agent from regularly visiting FAR states, leading to rapid forgetting. In NetHack, the pre-trained BC policy rarely visits levels beyond Level 1 despite the expert visiting many levels.
- **Status**: supported
- **Falsification criteria**: Pre-trained agents whose policies closely approximate an expert demonstrate no significant distribution shift from the expert and maintain FAR-state performance during fine-tuning.
- **Proof**: [E01, E04]
- **Dependencies**: C01
- **Tags**: imperfect cloning gap, NetHack, behavioral cloning, distribution shift

## C04: Knowledge retention methods (EWC, BC, KS, EM) mitigate FPC and improve fine-tuning performance
- **Statement**: Applying standard knowledge retention techniques (EWC, behavioral cloning loss, kickstarting, or episodic memory) to the actor network during RL fine-tuning prevents catastrophic forgetting of FAR-state behavior and leads to significantly better final performance. Fine-tuning + KS on NetHack achieves 10,588 ± 672 points versus ~1K for vanilla fine-tuning and ~5,218 for the frozen pre-trained model.
- **Status**: supported
- **Falsification criteria**: Knowledge retention methods fail to prevent the decline of FAR-state performance metrics (Room 7 success rate, per-stage RoboticSequence success, Level 4 NetHack score) compared to vanilla fine-tuning.
- **Proof**: [E01, E02, E03, E04]
- **Dependencies**: C01, C02, C03
- **Tags**: EWC, behavioral cloning, kickstarting, episodic memory, knowledge retention

## C05: The choice of knowledge retention method depends on the type of FPC instance
- **Statement**: Kickstarting (KS) is effective for imperfect cloning gap (NetHack) but fails for state coverage gap (Montezuma's Revenge, RoboticSequence) because it applies KL on online data and thus matches the pre-trained model on CLOSE states it was never trained on. Behavioral cloning (BC) succeeds for state coverage gap because it uses a static buffer from the pre-trained environment.
- **Status**: supported
- **Falsification criteria**: KS achieves competitive performance with BC on state coverage gap tasks (Montezuma's Revenge, RoboticSequence).
- **Proof**: [E02, E03, E05]
- **Dependencies**: C04
- **Tags**: kickstarting, behavioral cloning, state coverage gap, imperfect cloning gap, method selection

## C06: Forgetting is irreversible under vanilla fine-tuning — the re-learned policy is qualitatively different from the pre-trained one
- **Statement**: After the fine-tuned agent eventually revisits FAR states, the policy it re-learns is qualitatively different from the pre-trained policy (log-likelihoods of pre-trained expert trajectories under the fine-tuned policy do not recover to original values), indicating that transfer benefits are permanently lost under vanilla fine-tuning.
- **Status**: supported
- **Falsification criteria**: Log-likelihood of pre-trained expert trajectories under the fine-tuned policy recovers to within 10% of original values after re-visiting FAR states.
- **Proof**: [E06]
- **Dependencies**: C01, C02
- **Tags**: irreversibility, log-likelihood, representation shift, CKA
