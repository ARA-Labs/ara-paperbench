# Concepts

## Residual Stream
- **Notation**: $x_i^\ell \in \mathbb{R}^d$, where $d=1024$ for GPT2-medium
- **Definition**: The intermediate hidden state for token $i$ at layer $\ell$ in a transformer. Updated additively by attention heads and MLP blocks: $x_i^{\ell+1} = x_i^\ell + \text{MLP}^\ell(x_i^\ell + \text{Att}^\ell(x_i^\ell))$.
- **Boundary conditions**: Defined for layers $\ell = 0, \ldots, L-1$ where $L=24$ in GPT2-medium. The intermediate stream after attention but before MLP is denoted $x_i^{\ell\text{mid}}$.
- **Related concepts**: MLP Key-Value Decomposition, Residual Stream Shift

## MLP Key-Value Decomposition
- **Notation**: $\text{MLP}^\ell(x^\ell) = \sum_{i=1}^{d_\text{mlp}} m_i^\ell v_i^\ell$, where $m_i^\ell = \sigma(x^\ell \cdot k_i^\ell)$
- **Definition**: Each MLP block decomposes into $d_\text{mlp}$ sub-updates. $W_K^\ell \in \mathbb{R}^{d_\text{mlp} \times d}$ contains key vectors $k_i^\ell$ (rows); $W_V^\ell \in \mathbb{R}^{d_\text{mlp} \times d}$ contains value vectors $v_i^\ell$ (columns). The coefficient $m_i^\ell$ determines how strongly value vector $v_i^\ell$ is written to the residual stream.
- **Boundary conditions**: Applies to GPT-style transformer MLPs; $d_\text{mlp}=4096$ for GPT2-medium. Borrowed from Geva et al. (2022).
- **Related concepts**: Residual Stream, Toxic Value Vectors, MLP Activation Region

## Toxic Probe Vector (WToxic)
- **Notation**: $W_\text{Toxic} \in \mathbb{R}^d$, $P(\text{Toxic} | \bar{x}^{L-1}) = \text{softmax}(W_\text{Toxic} \bar{x}^{L-1})$
- **Definition**: A linear probe trained on the Jigsaw toxic comment classification dataset (561,808 comments, 90:10 train/validation split) using the averaged residual stream at the last layer $\bar{x}^{L-1}$. Achieves 94% validation accuracy. Represents an aggregate of all relevant toxicity signals in the model.
- **Boundary conditions**: Trained on GPT2-medium representations only; generalization to other architectures not validated.
- **Related concepts**: Toxic Value Vectors, SVD Toxic Vectors

## Toxic Value Vectors (MLP.vToxic)
- **Notation**: $\text{MLP.v}_\text{Toxic} = \{v_i^\ell : \cos(v_i^\ell, W_\text{Toxic}) \text{ is among top-}N\}$, $N=128$
- **Definition**: The set of $N=128$ MLP value vectors with highest cosine similarity to WToxic, selected across all layers. Their corresponding key vectors are $\text{MLP.k}_\text{Toxic}$. When activated, these vectors promote toxic tokens (verified via vocabulary projection).
- **Boundary conditions**: $N=128$ selected experimentally; similar results for other values of $N$. Only vectors that promote toxicity are selected; suppression vectors are not.
- **Related concepts**: Toxic Probe Vector, SVD Toxic Vectors, MLP Key-Value Decomposition

## SVD Toxic Vectors (SVD.UToxic)
- **Notation**: $\text{MLP.v}_\text{Toxic} = U \Sigma V^T$; $\text{SVD.U}_\text{Toxic}[i]$ = $i$-th left singular vector
- **Definition**: Obtained by stacking the $N=128$ toxic value vectors into an $N \times d$ matrix and applying SVD. The left singular vectors $\text{SVD.U}_\text{Toxic}$ form basis vectors spanning the toxicity representation subspace, with each vector capturing a different dimension (e.g., profanity, insults, sexual content).
- **Boundary conditions**: Three main singular vectors identified (indices 0, 1, 2) with interpretable token projections. Effectiveness decreases for higher-index vectors.
- **Related concepts**: Toxic Value Vectors, Vocabulary Projection

## Vocabulary Projection
- **Notation**: $r_i^\ell = E v_i^\ell \in \mathbb{R}^{|V|}$
- **Definition**: Projecting a value vector onto vocabulary space by multiplying by the embedding matrix $E \in \mathbb{R}^{|V| \times d}$. The resulting ranking of tokens (by $e_w \cdot v_i^\ell$) reveals which tokens are most promoted by that value vector. Promotion occurs when $e_w \cdot m_i^\ell v_i^\ell > 0$.
- **Boundary conditions**: Static component $e_w \cdot v_i^\ell$ does not depend on input; dynamic scale $m_i^\ell$ (determined by key vector and residual stream) modulates actual promotion.
- **Related concepts**: MLP Key-Value Decomposition, Toxic Value Vectors

## MLP Activation Region
- **Notation**: $\gamma(k_i^\ell) := \{g \mid g \in \mathbb{R}^d, \sigma(k_i^\ell \cdot g) > 0\}$
- **Definition**: The subspace in the model's hidden space in which a key vector $k_i^\ell$ has high dot product with the residual stream, thereby activating its corresponding value vector. If the residual stream lies in $\gamma(k_i^\ell)$, value vector $v_i^\ell$ is positively activated and contributes to the output.
- **Boundary conditions**: Depends on nonlinear activation $\sigma$ (GeLU for GPT2-medium). Regions are high-dimensional and not directly visualizable; analyzed through activation statistics.
- **Related concepts**: MLP Key-Value Decomposition, Residual Stream Shift

## Residual Stream Shift (δx)
- **Notation**: $\delta^{\ell\text{mid}} := x_{\text{DPO}}^{\ell\text{mid}} - x_{\text{GPT2}}^{\ell\text{mid}} \in \mathbb{R}^d$
- **Definition**: The vector difference between the residual streams of GPT2DPO and GPT2 at layer $\ell$ intermediate (after attention, before MLP). Interpreted as the offset that DPO learns to steer the residual stream away from toxic activation regions $\gamma(\text{MLP.k}_\text{Toxic})$.
- **Boundary conditions**: Computed per-prompt; mean shift $\bar{\delta}^\ell_x$ averaged over 1,199 RealToxicityPrompts. Key finding: δMLP.v and δx have high negative cosine similarity.
- **Related concepts**: MLP Activation Region, DPO Loss

## DPO Loss
- **Notation**: $\mathcal{L}_\text{DPO} = -\mathbb{E}[\log \sigma(\beta \log P - \beta \log N)]$, where $P = \pi_\theta(y^+|w)/\pi_\text{ref}(y^+|w)$, $N = \pi_\theta(y^-|w)/\pi_\text{ref}(y^-|w)$
- **Definition**: Direct Preference Optimization loss derived from pairwise preference data. $y^+$ is a preferred (non-toxic) continuation, $y^-$ is a non-preferred (toxic) continuation of prompt $w$. $\pi_\text{ref}$ is the frozen reference model; $\pi_\theta$ is the model being updated. $\beta=0.1$ used in this work.
- **Boundary conditions**: Requires paired preference data. KL-divergence regularization (implicit in $\pi_\text{ref}$ ratio) discourages large weight changes.
- **Related concepts**: Residual Stream Shift, Toxic Value Vectors

## Logit Lens
- **Notation**: $P(w | x^\ell) = \text{softmax}(E \cdot x^\ell)[w]$
- **Definition**: A technique (Nostalgebraist, 2020) that applies the unembedding layer $U$ to intermediate residual streams to visualize which tokens are being predicted at each layer. Used in this work to show which MLP layers most promote the toxic token "sh*t".
- **Boundary conditions**: Interpretive tool; does not represent the model's actual generation at intermediate layers. Applied to $x^{\ell\text{mid}}$ (after attention, before MLP) to isolate MLP contributions.
- **Related concepts**: Residual Stream, Vocabulary Projection

## PPLM (Plug and Play Language Model)
- **Notation**: $p(y|a) \propto p(y) p(a|y)$
- **Definition**: Attribute-controlled language generation technique (Dathathri et al., 2019) that attaches a linear attribute classifier $p(a|w)$ to a language model and uses its gradients to shift activations towards generating text with attribute $a$. Used in this paper to generate toxic negative samples for DPO training, using WToxic as the attribute classifier.
- **Boundary conditions**: Requires differentiable language model; quality degrades with strong steering. Hyperparameters: step size=0.4, decay=FALSE, GM scale=0.95, KL scale=0.1.
- **Related concepts**: DPO Loss, Toxic Probe Vector
