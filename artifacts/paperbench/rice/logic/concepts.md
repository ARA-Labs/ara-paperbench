# Concepts

## Markov Decision Process (MDP)
- **Notation**: $\langle \mathcal{S}, \mathcal{A}, P, \rho, R, \gamma \rangle$
- **Definition**: A tuple where $\mathcal{S}$ is the state set, $\mathcal{A}$ the action set, $P: \mathcal{S} \times \mathcal{A} \rightarrow \Delta(\mathcal{S})$ the transition function, $\rho$ the initial state distribution, $R: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$ the reward function, and $\gamma \in (0,1)$ the discount factor.
- **Boundary conditions**: Assumes Markovian rewards and transitions. Non-Markovian reward designs (identified as a flaw in the Malware Mutation environment, Appendix D) violate this.
- **Related concepts**: State Occupancy Distribution, Advantage Function, Sub-Optimality Gap

## State Occupancy Distribution
- **Notation**: $d^\pi_\rho(s) = (1 - \gamma) \sum_{t=0}^{\infty} \gamma^t \Pr^\pi(s_t = s \mid s_0 \sim \rho)$
- **Definition**: The (1-γ)-discounted visitation frequency of state s under policy π starting from initial distribution ρ.
- **Boundary conditions**: Defined for γ ∈ (0,1). In the limit γ→1 this approaches the stationary distribution.
- **Related concepts**: Markov Decision Process, Distribution Mismatch Coefficient

## Advantage Function
- **Notation**: $A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$
- **Definition**: The advantage of taking action a at state s over following policy π, where $Q^\pi(s,a) = \mathbb{E}_\pi[\sum_{t=0}^\infty \gamma^t R(s_t,a_t) | s_0=s, a_0=a]$ and $V^\pi(s) = \mathbb{E}_\pi[\sum_{t=0}^\infty \gamma^t R(s_t,a_t) | s_0=s]$.
- **Boundary conditions**: $\mathbb{E}_{a \sim \pi(\cdot|s)}[A^\pi(s,a)] = 0$ by definition.
- **Related concepts**: Sub-Optimality Gap, State Occupancy Distribution

## Sub-Optimality Gap
- **Notation**: $\text{SubOpt} := V^{\pi^*}(\rho) - V^{\pi'}(\rho)$
- **Definition**: The difference in expected discounted return between the optimal policy π* and the refined policy π', both evaluated from the default initial distribution ρ.
- **Boundary conditions**: Upper-bounded in Theorem 3.6 as $O\left(\frac{\varepsilon}{(1-\gamma)^2} \left\| \frac{d^{\pi^*}}{d^{\hat\pi}_\rho} \right\|_\infty\right)$ where ε bounds the one-step improvement $\mathbb{E}_{s \sim d^{\pi'}}[\max_a A^{\pi'}(s,a)] < \varepsilon$.
- **Related concepts**: Distribution Mismatch Coefficient, Advantage Function

## Distribution Mismatch Coefficient
- **Notation**: $\left\| \frac{d^{\pi^*}}{d^\pi_\rho} \right\|_\infty = \sup_s \frac{d^{\pi^*}_\rho(s)}{d^\pi_\rho(s)}$
- **Definition**: The worst-case ratio between the optimal policy's state visitation and that of policy π, measuring how well π covers the states important for π*.
- **Boundary conditions**: Requires $d^\pi_\rho(s) > 0$ whenever $d^{\pi^*}_\rho(s) > 0$ (Assumption 3.2, warm-start). Unbounded if the pre-trained policy has zero coverage of good states.
- **Related concepts**: Sub-Optimality Gap, State Occupancy Distribution

## StateMask (Original)
- **Notation**: $\tilde\pi_\theta$, mask network with binary action $a^m_t \in \{0, 1\}$
- **Definition**: A neural network policy that "blinds" the target agent at non-critical steps by replacing its action with a random action. The perturbed policy is $\bar\pi(a|s) = \tilde\pi(a^m=0|s)\pi(a|s) + \tilde\pi(a^m=1|s)\pi_r(a|s)$. Original objective: $J(\theta) = \min |\eta(\pi) - \eta(\bar\pi)|$, optimized with primal-dual methods.
- **Boundary conditions**: Assumes Assumption 3.1 (pre-trained policy better than random). A step with $a^m_t=0$ is critical (mask outputs 0 → action preserved); $a^m_t=1$ is non-critical (action randomized).
- **Related concepts**: Optimized StateMask, Critical State, MDP

## Optimized StateMask (RICE's Explanation Module)
- **Notation**: $\tilde\pi_\theta$, trained with PPO; modified reward $R'(s_t, a_t) = R(s_t, a_t) + \alpha \cdot a^m_t$
- **Definition**: Simplified StateMask using objective $J(\theta) = \max \eta(\bar\pi)$ (valid by Theorem 3.3 since $\eta(\bar\pi) \leq \eta(\pi)$ under Assumption 3.1). Adds blinding bonus α·am_t to prevent trivial solution (always outputting 0). Trained with vanilla PPO.
- **Boundary conditions**: Same assumptions as StateMask. α is a sensitivity-low hyperparameter (values 0.01, 0.001, 0.0001 yield similar fidelity). Equivalent to StateMask in fidelity per Lemma 3.5.
- **Related concepts**: StateMask (Original), Critical State, RICE Refining Algorithm

## Critical State
- **Notation**: $s^* = \arg\max_{s_t \in \tau} \tilde\pi_\theta(a^m=0 | s_t)$
- **Definition**: The state in trajectory τ where the mask network assigns highest importance score (probability of outputting 0, i.e., preserving the original action). Used as exploration frontier in RICE.
- **Boundary conditions**: Only meaningful when the pre-trained policy satisfies Assumption 3.2 (good state coverage). In "cold start" scenarios (e.g., Mountain Car), no meaningful critical states exist.
- **Related concepts**: Optimized StateMask, Mixed Initial State Distribution

## Mixed Initial State Distribution
- **Notation**: $\mu(s) = \beta \cdot d^{\hat\pi}_\rho(s) + (1-\beta)\rho(s)$; in code parameterized by reset probability $p$
- **Definition**: The mixture of the default initial distribution ρ and the critical-state distribution $d^{\hat\pi}_\rho(s)$ from the MaskNet-based sampling. With probability p, the refining episode starts from a critical state; with probability (1-p) from the default initial state.
- **Boundary conditions**: p=0 reduces to standard PPO fine-tuning; p=1 reduces to StateMask-R (overfits). Best performance at p ∈ {0.25, 0.5}.
- **Related concepts**: Critical State, Sub-Optimality Gap, RICE Refining Algorithm

## Random Network Distillation (RND) Exploration Bonus
- **Notation**: $R^{RND}(s_{t+1}) = |f(s_{t+1}) - \hat{f}(s_{t+1})|^2$; total reward $R'(s_t,a_t) = R(s_t,a_t) + \lambda \cdot R^{RND}(s_{t+1})$
- **Definition**: Intrinsic exploration reward based on the prediction error of a randomly initialized target network f by a trained predictor network $\hat{f}$. Novel states produce higher prediction error, encouraging exploration of unseen states.
- **Boundary conditions**: As state coverage increases, RND bonus decays to zero and the task-reward-optimal policy is recovered. Count-based bonuses are impractical in large/continuous state spaces where RND is preferred. λ controls exploration-exploitation trade-off.
- **Related concepts**: Mixed Initial State Distribution, RICE Refining Algorithm
