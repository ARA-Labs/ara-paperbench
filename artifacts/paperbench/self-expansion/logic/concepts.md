# Concepts

## Modular Adapter (Paired Unit)
- **Notation**: $(f_{\phi_k^l}, g_{\varphi_k^l})$
- **Definition**: A paired unit consisting of a functional adapter $f_{\phi_k^l}(\cdot)$ and a representation descriptor $g_{\varphi_k^l}(\cdot)$ added at the $k$-th position in the $l$-th transformer layer. Together they enable SEMA to represent and detect a specific feature distribution at that layer.
- **Boundary conditions**: Each modular adapter is associated with exactly one task that triggered its creation. After training, both components are frozen. At most one new modular adapter is added per layer per task.
- **Related concepts**: Functional Adapter, Representation Descriptor, Expandable Weighting Router

## Functional Adapter
- **Notation**: $f_{\phi_k^l}(\mathbf{x}^l) = \text{ReLU}(\mathbf{x}^l \cdot \mathbf{W}^l_{\text{down},k}) \cdot \mathbf{W}^l_{\text{up},k}$
- **Definition**: A lightweight bottleneck module inserted as a side branch of the MLP in a ViT transformer block. Parameters $\phi_k^l \equiv \{\mathbf{W}^l_{\text{up},k}, \mathbf{W}^l_{\text{down},k}\}$ with $\mathbf{W}^l_{\text{down},k} \in \mathbb{R}^{d \times r}$ (down-projection) and $\mathbf{W}^l_{\text{up},k} \in \mathbb{R}^{r \times d}$ (up-projection), where $r$ is the hidden (bottleneck) dimension.
- **Boundary conditions**: Hidden dimension $r=16$ as stated in paper §4.1. Reproduction rubric specifies $r=48$ for SEMA and ADAM adapter configurations — practitioners should verify against official code. The adapter operates on the feature $\mathbf{x}^l \in \mathbb{R}^d$ output of the second LayerNorm in the transformer block (before the MLP output residual).
- **Related concepts**: Modular Adapter, Expandable Weighting Router, LoRA, Convpass

## Representation Descriptor (RD)
- **Notation**: $g_{\varphi_k^l}(\cdot)$; reconstruction loss $\mathcal{L}^l_{\text{RD},k}(\mathbf{x}) = \sum_{\mathbf{x} \in \mathcal{X}_k^l} \|\mathbf{x} - g_{\varphi_k^l}(\mathbf{x})\|_2^2$
- **Definition**: An autoencoder that captures the feature distribution of the inputs seen during the training of its paired functional adapter. Architecture: encoder = Linear($d \to 128$) + LeakyReLU; decoder = Linear($128 \to d$). Trained exclusively with the reconstruction loss $\mathcal{L}_{\text{RD}}$, receiving no gradient from the classification loss.
- **Boundary conditions**: RD is paired 1-to-1 with a functional adapter. The running statistics (mean $\mu_k^l$, std $\sigma_k^l$) are maintained over a fixed buffer of the 500 most recent training samples for that adapter. After its task is trained, the RD is frozen.
- **Related concepts**: Modular Adapter, Z-Score Expansion Signal, Running Statistics Buffer

## Expandable Weighting Router
- **Notation**: $h_{\psi^l}(\cdot): \mathbb{R}^d \to \mathbb{R}^{K^l}$; $\mathbf{w}^l = \text{softmax}(\mathbf{x}^l \cdot \mathbf{W}^l_{\text{mix}})$; $\mathbf{W}^l_{\text{mix}} \in \mathbb{R}^{d \times K^l}$
- **Definition**: A layer-wise linear + softmax router that produces mixture weights $\mathbf{w}^l$ over the $K^l$ adapters at layer $l$. The output representation is $\mathbf{x}^l_{\text{out}} = \text{MLP}(\mathbf{x}^l) + \sum_{k=1}^{K^l} w_k^l \cdot f_{\phi_k^l}(\mathbf{x}^l)$. When a new adapter is added, $\mathbf{W}^l_{\text{mix}}$ is expanded by one column; existing columns are frozen, only the new column is trained.
- **Boundary conditions**: The router is always updated during expansion events. At $K^l=1$ (Task 1), the router reduces to a dummy scalar weight. The soft mixture is shown to outperform hard selection variants (Table 2).
- **Related concepts**: Functional Adapter, Modular Adapter

## Z-Score Expansion Signal
- **Notation**: $z_k^l = (r_k^l - \mu_k^l) / \sigma_k^l$
- **Definition**: The normalized reconstruction error of the $k$-th RD at layer $l$ for a given input $\mathbf{x}^l$, where $r_k^l = \|\mathbf{x}^l - g_{\varphi_k^l}(\mathbf{x}^l)\|_2^2$ is the raw reconstruction error, and $\mu_k^l, \sigma_k^l$ are running mean and standard deviation maintained over a buffer of 500 recent samples. An expansion signal at layer $l$ is triggered when $z_k^l > \tau$ for all $k = 1, \ldots, K^l$, where $\tau$ is the expansion threshold hyperparameter.
- **Boundary conditions**: Computed only during the scanning (detection) phase at the start of each new task. No training occurs during scanning. The z-score normalises out scale and perturbation differences, making the method insensitive to $\tau$ within a wide range (§4.3, Fig. 6).
- **Related concepts**: Representation Descriptor, Running Statistics Buffer, Task-Oriented Expansion

## Task-Oriented Expansion
- **Notation**: At most 1 new adapter per layer per task.
- **Definition**: An expansion restriction specific to the CIL setting: when a new task $t$ arrives, SEMA scans all samples in the first epoch sequentially from shallow to deep layers to decide expansion. If an expansion signal is triggered at layer $l$, exactly one adapter is added and trained for the entire task $t$; subsequent deeper layers are then scanned. If no signal is triggered in any layer, no adapter is added and no training occurs.
- **Boundary conditions**: Requires knowledge of task boundaries (not applicable to fully online CL). Limits to CIL scenario. Does not apply to within-task or online expansion.
- **Related concepts**: Z-Score Expansion Signal, Multi-Layer Expansion

## Multi-Layer Expansion
- **Notation**: Expansion layers $\mathcal{L}_{\text{exp}} \subseteq \{1, \ldots, L\}$
- **Definition**: SEMA applies expansion decisions sequentially from the shallowest to deepest eligible layer. By default, only the last 3 transformer layers (layers 10, 11, 12 for ViT-B/16 with 12 layers) are eligible for expansion. Expansion at a shallow layer triggers training before checking deeper layers.
- **Boundary conditions**: Setting $|\mathcal{L}_{\text{exp}}| = 1$ reduces to single-layer expansion. Earlier layers (e.g., 9) expand less frequently. Expanding too many early layers can increase adapter count without proportional accuracy gains (Fig. 7).
- **Related concepts**: Task-Oriented Expansion, Z-Score Expansion Signal

## Running Statistics Buffer
- **Notation**: Buffer $\mathcal{B}_k^l$ of size 500; $\mu_k^l = \text{mean}(\mathcal{B}_k^l)$, $\sigma_k^l = \text{std}(\mathcal{B}_k^l)$
- **Definition**: A fixed-size FIFO stack of 500 reconstruction errors from the most recent training batches, maintained per representation descriptor. Used to compute running mean $\mu_k^l$ and std $\sigma_k^l$ for z-score calculation.
- **Boundary conditions**: Only the most recent 500 samples are retained (sliding window). Initialized at the start of training for each new RD.
- **Related concepts**: Representation Descriptor, Z-Score Expansion Signal

## Class-Incremental Learning (CIL)
- **Notation**: Task sequence $(D_1, D_2, \ldots, D_T)$; $D_t = \{(x_i^t, y_i^t)\}_{i=1}^{n_t}$; $\mathcal{Y}_t \cap \mathcal{Y}_{t'} = \emptyset$ for $t \neq t'$
- **Definition**: A continual learning scenario where the model must classify among all classes seen so far, with non-overlapping class sets per task. Only current task data $D_t$ is accessible during training of task $t$ (no rehearsal in SEMA). Objective: minimise $\mathbb{E}_{(x,y) \in D_t}[\mathcal{L}_{\text{CE}}(F_\theta(x), y)]$ for each $t$ sequentially while retaining performance on all previous tasks.
- **Boundary conditions**: SEMA assumes task boundaries are known (task-oriented expansion). Without task boundaries (online CL), the expansion protocol requires modification.
- **Related concepts**: Task-Oriented Expansion, Average Accuracy A_N, Average Incremental Accuracy Ā
