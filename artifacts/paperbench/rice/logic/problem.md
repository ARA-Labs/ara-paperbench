# Problem Specification

## Observations

### O1: DRL Agents Converge to Training Bottlenecks
- **Statement**: DRL agents frequently become locally optimal and cease to improve further, making systematic errors or failing to complete final goals.
- **Evidence**: Motivating observation throughout §1; empirically demonstrated by pre-trained agents achieving plateaued rewards (Table 1, "No Refine" column).
- **Implication**: A refining strategy is needed — re-training from scratch is too costly for complex tasks.

### O2: Re-training from Scratch Is Prohibitively Expensive
- **Statement**: For complex DRL tasks (e.g., AlphaStar/StarCraft), re-training exceeds one month with TPUs and can cost millions of dollars.
- **Evidence**: Cited in §1 (Vinyals et al., 2019; Agarwal et al., 2022).
- **Implication**: Any practical refining method must reuse the pre-trained policy rather than discard it.

### O3: Fine-tuning Only from Critical States Causes Overfitting
- **Statement**: Initializing refining exclusively from critical states (StateMask-R) degrades performance on default initial states due to distribution shift.
- **Evidence**: Table 7 (Malware Mutation case study): StateMask-R achieves 50.8% evasion from critical states but only 36.2% from default initial states (vs. 33.8% no-refine baseline). Appendix D.
- **Implication**: Diversity in initial state distribution is necessary to prevent overfitting.

### O4: Random Exploration Frontiers Are Ineffective
- **Statement**: JSRL's random selection of exploration frontiers does not guarantee frontiers with positive returns, leading to poor performance on complex tasks.
- **Evidence**: Table 1: JSRL underperforms RICE across all 8 environments; Figure 2 shows JSRL diverges or stagnates in sparse MuJoCo tasks.
- **Implication**: Explanation-guided frontier selection is necessary for effective refining.

### O5: StateMask's Primal-Dual Optimization Is Computationally Costly
- **Statement**: The original StateMask requires estimating discounted accumulated rewards under both the perturbed and original policies, incurring extra computation.
- **Evidence**: Table 4: StateMask takes 15,393 sec vs. 12,426 sec for Ours on Hopper; 16.8% average time reduction.
- **Implication**: The objective can be simplified (via Theorem 3.3) without sacrificing guarantees.

## Gaps

### G1: No Principled Refining Strategy with Theoretical Guarantees
- **Statement**: Existing refining strategies (PPO fine-tuning, StateMask-R, JSRL) lack formal sub-optimality bounds.
- **Caused by**: O1, O2, O4
- **Existing attempts**: StateMask-R (critical state reset), JSRL (guided policy curriculum), PPO fine-tuning.
- **Why they fail**: StateMask-R overfits (O3); JSRL uses random frontiers (O4); PPO fine-tuning trapped in local optima (Table 1).

### G2: No Integration of Explanation Quality into Initial State Distribution
- **Statement**: PPO++ (Chang et al., 2023) mixes default and visited states but treats all visited states equally — not all are informative.
- **Caused by**: O4
- **Existing attempts**: PPO++ constructs mixed distribution with random visited states.
- **Why they fail**: Random states provide no guarantee of reducing distribution mismatch coefficient.

## Key Insight
- **Insight**: Selecting critical states via StateMask is equivalent to sampling from a better policy ˆπ (Lemma 3.5). Mixing these states with default initial states reduces the state distribution mismatch coefficient ||dπ*/dˆπρ||∞, which directly tightens the sub-optimality upper bound (Theorem 3.6). Combined with RND exploration from these frontiers, the agent escapes local optima.
- **Derived from**: O1, O3, O4
- **Enables**: A theoretically grounded mixed initial distribution that prevents overfitting while providing better exploration frontiers.

## Assumptions
- A1: The pre-trained policy π performs strictly better than a random policy (Assumption 3.1: E_{a~πr}[Aπ(s,a)] ≤ 0, ∀s).
- A2: The pre-trained policy π covers all states visited by the optimal policy π* (Assumption 3.2: ||dπ*/dπρ||∞ ≤ C — warm-start assumption).
- A3: A superior policy ˆπ (η(ˆπ) ≥ η(π)) has a smaller distribution mismatch coefficient (Assumption 3.4: ||dπ*/dˆπ||∞ ≤ ||dπ*/dπ||∞).
- A4: The environment is simulator-based (enabling state reset to arbitrary critical states).
