# Concepts

## APT Adapter
- **Notation**: $H_{apt}(X) = m_o \circ (W + s \cdot W_B W_A) X \circ m_i$
- **Definition**: A modified LoRA adapter that adds two binary pruning masks ($m_i \in \mathbb{R}^{d_i}$ for input, $m_o \in \mathbb{R}^{d_o}$ for output) and a dynamic rank $r_{apt}$ to the standard LoRA decomposition. The Hadamard product $\circ$ applies the masks element-wise. When a mask entry is 0, the corresponding parameter block is pruned; when 1, it is retained. The scaling factor $s$ follows LoRA's implementation and is set to 2.
- **Boundary conditions**: Applied to query and value projections in MHA layers always; also applied to FFN up-projection layers for smaller models (RoBERTa, T5). Not applied for inference (adapter weights merged into frozen parameters after training). $m_i$ prunes hidden dimensions; $m_o$ prunes attention heads (MHA) or FFN neurons (FFN).
- **Related concepts**: LoRA, Binary Pruning Mask, Dynamic Rank, Structured Pruning

## Binary Pruning Mask
- **Notation**: $m_i \in \mathbb{R}^{d_i}$, $m_o \in \mathbb{R}^{d_o}$; entries $\in \{0, 1\}$
- **Definition**: Learnable binary vectors that gate parameter blocks. A mask entry of 0 effectively removes the corresponding block from computation; a value of 1 retains it. To avoid training instability, masks of pruned blocks are decreased gradually by $\alpha = 0.01$ per step (not set to 0 instantly).
- **Boundary conditions**: Masks are applied at the block level (head, neuron, or hidden dimension granularity), not at the scalar parameter level. Pruning masks for pruned blocks decrease by $\alpha = 0.01$ per step; masks for retained blocks increase by $\alpha = 0.01$.
- **Related concepts**: APT Adapter, Structured Pruning, Outlier-Aware Salience Score

## Outlier-Aware Salience Score
- **Notation**: $\hat{S}(W_{:,j}) = \tilde{S}(W_{:,j}) + \text{Kurt}(O_{j,:})^{1/2}$, where $\tilde{S}(W_{:,j}) = \sum_{(x,y) \in D_t} \left|\frac{\partial L}{\partial H_{j,i}} \cdot H_{j,i}\right|$ and $O_{:,j} = W_{:,j} \circ X_{j,:}^T$
- **Definition**: A per-block importance score combining two terms: (1) the activation-gradient product (proxy for weight-gradient product when frozen weights have no accessible gradients in PEFT settings), summed over batches; and (2) the square root of the kurtosis of the block's activation to preserve outlier parameters. Updated via exponential moving average: $\bar{S}^{(t)}(m) = \beta \bar{S}^{(t-1)}(m) + (1-\beta)\hat{S}(m)$ with $\beta = 0.85$.
- **Boundary conditions**: Activation and gradient tensors are summed along the batch dimension before multiplication to reduce memory overhead. For APT adapter layers, the salience combines frozen weight salience and tuning weight salience (Equation 9 in paper). Applicable only during pruning training steps, not during inference.
- **Related concepts**: APT Adapter, Binary Pruning Mask, Kurtosis, EMA Salience

## Salience Density
- **Notation**: $\rho(b) = \hat{S}(b) / \mathcal{C}(b)$
- **Definition**: The outlier-aware salience score of a parameter block divided by the number of parameters in that block. Used to rank blocks for pruning: blocks with lower salience density are pruned first. Re-computed after every parameter size change.
- **Boundary conditions**: Only computed for blocks that have an APT adapter applied. Three block types have different parameter counts: MHA head ($4 d_m d_m / n_h$), FFN neuron ($2 d_m$), hidden dimension ($n_L (4 d_m + 2 n_f)$).
- **Related concepts**: Outlier-Aware Salience Score, Binary Search Block Selection, Structured Pruning

## Binary Search Block Selection
- **Notation**: Given sorted blocks $B = \{b_1, \ldots, b_N\}$ and sparsity constraint $\gamma_t$, find maximum $i$ such that $C_{\text{top-}i} \leq (1-\gamma_t) \cdot C(\Theta_0, M_0)$
- **Definition**: A fast algorithm that leverages the monotonic relationship between the number of retained blocks and total parameter count. Blocks are sorted by salience density (descending). Given any index $i$, the total parameter count of the LM with the top-$i$ blocks is computed as $C_{\text{top-}i} = (4 d_h' \cdot n_h' + 2 n_f') \cdot d_m'$, where $n_h', n_f', d_m'$ are counts of heads, neurons, and dimension-steps in the top-$i$ blocks. Binary search over $i$ identifies which blocks to retain given the sparsity constraint.
- **Boundary conditions**: For T5 and LLaMA-like models, FFN layers are gated (up/gate/down projections), so the FFN neuron count formula uses 3 layers instead of 2. Encoder-decoder LMs (T5) also count cross-attention layers.
- **Related concepts**: Salience Density, Binary Pruning Mask, Cubic Sparsity Schedule

## Cubic Sparsity Schedule
- **Notation**: $\gamma_t = \gamma_T + (1 - \gamma_T)(1 - t/T)^3$
- **Definition**: A cubic decay schedule for the target sparsity at training step $t$, where $\gamma_T$ is the final target sparsity and $T$ is the total number of pruning training steps. The schedule starts at $\gamma_0 = 1$ (no pruning) and progressively increases sparsity toward $\gamma_T$ with a cubic rate, front-loading the pruning during early training.
- **Boundary conditions**: Used only during the pruning (distillation) phase, not during the fine-tuning recovery phase. The schedule is pre-determined; no dynamic adjustment based on task performance.
- **Related concepts**: Binary Search Block Selection, Binary Pruning Mask, APT Adapter

## Dynamic Rank (Adaptive Tuning)
- **Notation**: $r_{apt}' = \lfloor r_{apt} \cdot \Delta_{t'} / \Delta_t \rfloor$
- **Definition**: The rank of the APT adapter's LoRA matrices ($W_A \in \mathbb{R}^{r_{apt} \times d_i}$, $W_B \in \mathbb{R}^{d_o \times r_{apt}}$) is dynamically increased during training. APT adapters are ranked by their importance score $\mathcal{I}(H_{apt}) = \sum_{i,j} S(W_{B_{i,j}})$; the top-half most important adapters have their rank linearly scaled from $r_{apt}$ to $r_{apt}'$ as the tuning budget $\Delta_t$ increases. New $W_A$ rows are initialized from $\mathcal{N}(0, \sigma^2)$; new $W_B$ columns are initialized to 0 (preserving layer output unchanged at initialization).
- **Boundary conditions**: Adapter ranks start at 8 (initial value). The optimizer state is reset after each parameter size change to avoid instability. Only the top-half salient adapters gain new parameters; the bottom-half remain at their current rank.
- **Related concepts**: APT Adapter, Outlier-Aware Salience Score, Adaptive Tuning

## Self-Knowledge Distillation
- **Notation**: $\mathcal{L} = \mu \mathcal{L}_{\text{distill}} + (1-\mu) \mathcal{L}_{\text{ft}}$; $\mathcal{L}_{\text{layer}} = \sum_{i=1}^{4} \text{MSE}(\text{Tr}(H_s^{\phi(i)}), H_t^i)$
- **Definition**: A distillation strategy that avoids requiring a separately trained teacher model by duplicating tuning student layers as teachers during fine-tuning and sharing frozen parameters between teacher and student. Teacher layers are randomly sampled per epoch (4 layers from quarter-slices of the network). $\mu$ linearly scales from 0 to 1 during the distillation phase; $\text{Tr}$ is a tunable LoRA transformation layer initialized as the identity matrix; $\phi(\cdot)$ is the teacher-student layer mapping (argmin MSE over non-pruned student layers).
- **Boundary conditions**: For GLUE tasks: $\mathcal{L}_{\text{distill}} = \mathcal{L}_{\text{pred}} + 0.9 \mathcal{L}_{\text{layer}}$. For SQuAD/CNN/DM: $\mathcal{L}_{\text{distill}} = 0.1 \mathcal{L}_{\text{pred}} + 0.9 \mathcal{L}_{\text{layer}}$. $\mathcal{L}_{\text{pred}} = D_{\text{KL}}(p_s \| p_t)$. The layer mapping $\phi(i) = \arg\min_{j: z_{\text{FFN}}^{(j)} > 0} \text{MSE}(W_{\text{layer}} H_s^j, H_t^i)$ is re-computed every training step.
- **Related concepts**: APT Adapter, Dynamic Rank, Cubic Sparsity Schedule

## Structured Pruning
- **Notation**: Pruning MHA heads ($n_h^i$), FFN neurons ($n_f^i$), and hidden dimension ($d_m$) simultaneously across transformer layers.
- **Definition**: The removal of consistent, contiguous blocks of parameters from transformer layers such that the resulting model has fewer total parameters and runs faster on standard hardware without sparse matrix libraries. In APT, structured pruning is controlled via binary masks applied at the head, neuron, and hidden-dimension granularity.
- **Boundary conditions**: More hardware-friendly than unstructured (sparse) pruning; actual speedup depends on GPU architecture (Ampere: dimensions divisible by 8 for FP16, by 16 for Int8 for maximum efficiency). For encoder-decoder models, cross-attention layers are also counted.
- **Related concepts**: Binary Pruning Mask, Binary Search Block Selection, APT Adapter

## Target Sparsity
- **Notation**: $\gamma_T$; defined as ratio of pruned parameter count to original parameter count.
- **Definition**: The fraction of parameters removed from the LM after the full pruning schedule completes. At sparsity $\gamma_T$, the remaining parameter fraction is $(1 - \gamma_T)$. E.g., $\gamma_T = 0.6$ means 60% of parameters are pruned, 40% remain. APT experiments use $\gamma_T \in \{0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95\}$.
- **Boundary conditions**: Higher sparsity improves inference efficiency but may degrade task performance. The constraint $C(\Theta_t, M_t) / C(\Theta_0, M_0) \geq 1 - \gamma_t$ must hold at every training step $t$.
- **Related concepts**: Cubic Sparsity Schedule, Binary Search Block Selection, Structured Pruning
