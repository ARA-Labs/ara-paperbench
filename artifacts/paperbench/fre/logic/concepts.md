# Concepts

## Functional Reward Encoding (FRE)
- **Notation**: $z \sim p_\theta(z \mid s_1^e, \eta(s_1^e), \ldots, s_K^e, \eta(s_K^e))$
- **Definition**: A latent representation $z \in \mathbb{R}^d$ of a reward function $\eta: \mathcal{S} \to \mathbb{R}$, obtained by passing $K$ state-reward samples through a permutation-invariant transformer encoder with a variational information bottleneck. The encoding is trained to predict reward values on held-out states via a feedforward decoder.
- **Boundary conditions**: Requires an offline dataset $\mathcal{D}$ to sample encoding states from. Assumes reward functions are pure functions of state (or state-action). Fixed $K=32$ encoder samples; not designed for variable-length context like neural processes.
- **Related concepts**: Information Bottleneck, Transformer Encoder, Implicit Q-Learning, Prior Reward Distribution

## Information Bottleneck Objective
- **Notation**: $\max_\theta \; I(L^d_\eta; Z) - \beta \, I(L^e_\eta; Z)$
- **Definition**: The training objective for FRE, derived from the information bottleneck principle (Tishby et al., 2000). $L^e_\eta = \{(s_k^e, \eta(s_k^e))\}_{k=1}^K$ is the encoding context set; $L^d_\eta = \{(s_k^d, \eta(s_k^d))\}_{k=1}^{K'}$ is the decoding target set; $Z$ is the latent variable; $\beta=0.01$ is the compression weight. Maximized via a variational lower bound using ELBO-style objectives.
- **Boundary conditions**: Mutual information is intractable; approximated via KL penalty to unit Gaussian prior $u(z)$. Encoding and decoding states must be disjoint samples from $\mathcal{D}$.
- **Related concepts**: Functional Reward Encoding, Variational Autoencoder, KL Divergence

## Variational Lower Bound (FRE ELBO)
- **Notation**: $\mathcal{L} = \mathbb{E}_{\eta, L^e_\eta, L^d_\eta, z \sim p_\theta(z|L^e_\eta)}\!\left[\sum_{k=1}^{K'} \log q_\theta(\eta(s_k^d) \mid s_k^d, z) - \beta \, D_\text{KL}(p_\theta(z \mid L^e_\eta) \,\|\, u(z))\right]$
- **Definition**: The tractable surrogate for the information bottleneck objective. The reconstruction term $\log q_\theta(\eta(s^d) \mid s^d, z)$ is implemented as mean-squared error between predicted and true rewards. The KL term $D_\text{KL}(p_\theta(z|L^e_\eta) \| \mathcal{N}(0,I))$ regularizes the latent distribution toward a unit Gaussian.
- **Boundary conditions**: Assumes decoder is a Gaussian likelihood over scalar rewards. MSE reconstruction assumes constant variance.
- **Related concepts**: Information Bottleneck Objective, Functional Reward Encoding, KL Divergence

## Prior Reward Distribution
- **Notation**: $p(\eta)$
- **Definition**: The training-time distribution over reward functions used to pre-train FRE. Implemented as a uniform mixture of three families: (1) singleton goal-reaching rewards ($\eta(s) = -\mathbf{1}[\text{dist}(s, g) > \epsilon]$ with HER-style goal sampling), (2) random linear functions ($\eta(s) = w^\top s$ with sparse binary mask), (3) random 2-layer MLPs ($\eta(s) = \text{clip}(\text{MLP}(s), -1, 1)$).
- **Boundary conditions**: Each family contributes 1/3 probability in FRE-all. For AntMaze, XY positions are excluded from linear reward generation due to scale instability. Random MLPs use architecture (state_dim → 32 → 1) with tanh activation and normal init scaled by average layer dimension.
- **Related concepts**: Goal-Reaching Reward, Random Linear Function, Random MLP, FRE-hint

## Permutation-Invariant Transformer Encoder
- **Notation**: $p_\theta(z \mid \{(s_k^e, \eta(s_k^e))\}_{k=1}^K)$
- **Definition**: A transformer with 4 layers of hidden size 256, no causal masking, no positional encodings, treating K input tokens as an unordered set. Scalar rewards are first discretized into one of 32 bins and embedded via a learned embedding table; state features are projected via a linear layer; the two embeddings are concatenated per token. The average of final-layer representations is projected to mean and log-std of a Gaussian over $z$.
- **Boundary conditions**: Permutation invariance ensures the encoding is independent of token ordering. K is fixed at 32. No positional encoding by design.
- **Related concepts**: Functional Reward Encoding, Reward Discretization, FRE ELBO

## Implicit Q-Learning (IQL)
- **Notation**: $\pi(a \mid s, z)$, $Q(s, a, z)$, $V(s, z)$
- **Definition**: An offline RL algorithm (Kostrikov et al., 2021) that avoids out-of-distribution action queries by learning a value function via expectile regression and updating the actor via advantage-weighted regression (AWR). Critic update: $Q(s,a,z) \leftarrow \eta(s) + \gamma \cdot \text{mask} \cdot V(s', z)$. Value update: expectile regression on $Q(s,a,z)$ with $\tau=0.8$. Actor update: AWR with temperature $\beta_\text{AWR}=3.0$.
- **Boundary conditions**: Policy is conditioned on frozen latent $z$ (encoder frozen during policy training). Discount factor $\gamma=0.88$.
- **Related concepts**: Functional Reward Encoding, Strided Training, AWR Temperature

## Strided Training
- **Notation**: Phase 1: train $p_\theta(z|\cdot), q_\theta(\eta|\cdot)$ only. Phase 2: freeze $p_\theta$, train $\pi, Q, V$.
- **Definition**: A two-phase training procedure where the FRE encoder-decoder is trained to convergence first (150K steps for AntMaze, 1M for ExORL/Kitchen), then the encoder is frozen and the IQL policy is trained using the fixed encoder's outputs (850K steps for AntMaze, 1M for ExORL/Kitchen). This ensures a stationary mapping from $\eta$ to $z$ during TD learning.
- **Boundary conditions**: Required for stable multi-task Q-value estimation. If encoder changes during policy training, TD targets become non-stationary.
- **Related concepts**: Implicit Q-Learning, Functional Reward Encoding, Information Bottleneck Objective

## Reward Discretization
- **Notation**: $r_\text{disc} = \lfloor \text{clip}((r + 1) / 2, 0, 1) \times 32 \rfloor$
- **Definition**: Scalar reward values are mapped to integers in $\{0, \ldots, 31\}$ (32 bins) by rescaling to $[0,1]$ and flooring. Each bin index is then mapped to a continuous vector via a learned embedding table of size $32 \times d_\text{emb}$.
- **Boundary conditions**: Assumes rewards are normalized to approximately $[-1, 1]$. Number of embeddings = 32; embedding dimension not specified in paper.
- **Related concepts**: Permutation-Invariant Transformer Encoder, Prior Reward Distribution

## Zero-Shot RL Problem
- **Notation**: Phase 1: unsupervised pre-training from $\mathcal{D}$; Phase 2: zero-shot evaluation with no fine-tuning.
- **Definition**: A two-phase RL setting (Touati et al., 2022) where an agent is pre-trained from unlabeled offline data, then at test time must solve a new downstream reward function $\eta: \mathcal{S} \to \mathbb{R}$ specified only via a small set of $(s, \eta(s))$ tuples, without any further gradient updates to the policy.
- **Boundary conditions**: No online interaction during pre-training. Tasks share the same environment dynamics. FRE uses K=32 evaluation samples.
- **Related concepts**: Functional Reward Encoding, Strided Training, Prior Reward Distribution

## Advantage-Weighted Regression (AWR)
- **Notation**: $\mathcal{L}_\pi = -\mathbb{E}_{(s,a) \sim \mathcal{D}} \left[ \exp\!\left(\frac{Q(s,a,z) - V(s,z)}{\beta_\text{AWR}}\right) \log \pi(a \mid s, z) \right]$
- **Definition**: The actor update rule in IQL, where actions from the dataset are re-weighted by their exponentiated advantage with temperature $\beta_\text{AWR}=3.0$. Higher-advantage actions receive larger gradient weight.
- **Boundary conditions**: Large $\beta_\text{AWR}$ reduces to behavioral cloning; small $\beta_\text{AWR}$ reduces to policy gradient. Set to 3.0 in all experiments.
- **Related concepts**: Implicit Q-Learning, Functional Reward Encoding
