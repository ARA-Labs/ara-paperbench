# System Architecture: SEMA

## Component Graph

```
Input Image x
     |
     v
[Frozen ViT Encoder]  (L=12 transformer blocks for ViT-B/16)
     |
     | For each transformer block l:
     |
     +--[LayerNorm 1]--[MHSA]--[Residual]--[LayerNorm 2]--> x^l (input to MLP)
                                                              |
     +--------------------------------------------------------+
     |
     | --> [Frozen MLP(x^l)] --> MLP output
     |
     | --> [Expandable Adapter Module at layer l]:
     |         |
     |         +-- [Functional Adapters]: f_{phi_1^l}, f_{phi_2^l}, ..., f_{phi_{K^l}^l}
     |         |       Each: down-proj -> ReLU -> up-proj (lightweight bottleneck)
     |         |
     |         +-- [Representation Descriptors]: g_{phi_1^l}, ..., g_{phi_{K^l}^l}
     |         |       Each: AE (Linear->LeakyReLU->Linear)
     |         |       Used during TRAINING for expansion signal detection
     |         |
     |         +-- [Expandable Weighting Router]: h_{psi^l}
     |                 Linear(d -> K^l) -> Softmax
     |                 Produces weights w^l = [w_1^l, ..., w_{K^l}^l]
     |
     +--> x^l_out = MLP(x^l) + sum_k(w_k^l * f_{phi_k^l}(x^l))
     |
     v
[Next transformer block l+1 ...]
     |
     v
[Classification Head]  (expandable linear layer, grows with new classes)
     |
     v
Output: class logits
```

## Component Descriptions

### Frozen ViT Backbone
- **Purpose**: Stable feature extraction. Never updated during CL.
- **Inputs**: Raw image $x \in \mathbb{R}^{H \times W \times C}$ (patched to sequence)
- **Outputs**: Intermediate features $\mathbf{x}^l \in \mathbb{R}^{N \times d}$ at each layer; final [CLS] token
- **Key design**: Pre-trained ViT-B/16 on ImageNet-1K (or IN-21K). All parameters frozen.

### Expandable Adapter Module (per layer)
- **Purpose**: Adapts frozen representations to downstream tasks; enables on-demand expansion.
- **Inputs**: Layer feature $\mathbf{x}^l \in \mathbb{R}^d$ (from the second LayerNorm output)
- **Outputs**: Adaptation residual to be added to MLP output
- **Interactions**: Receives features from frozen ViT; outputs are combined with MLP outputs.

### Functional Adapter $f_{\phi_k^l}$
- **Purpose**: Produce task-specific feature adaptations as a side branch of the MLP.
- **Inputs**: $\mathbf{x}^l \in \mathbb{R}^d$
- **Outputs**: $f_{\phi_k^l}(\mathbf{x}^l) \in \mathbb{R}^d$
- **Architecture**: Down-projection ($d \to r$) + ReLU + Up-projection ($r \to d$). $r=16$ per paper; reproduction rubric specifies $r=48$.
- **Key design choice**: Side branch of MLP (not inside attention), following AdaptFormer [9].

### Representation Descriptor $g_{\varphi_k^l}$
- **Purpose**: Capture feature distribution of the paired adapter's training data; detect novel patterns.
- **Inputs**: $\mathbf{x}^l \in \mathbb{R}^d$
- **Outputs**: Reconstruction $\hat{\mathbf{x}}^l \in \mathbb{R}^d$; reconstruction error $r_k^l$
- **Architecture**: AE with encoder Linear($d \to 128$) + LeakyReLU + decoder Linear($128 \to d$).
- **Key design choice**: Trained only with $\mathcal{L}_{\text{RD}}$; gradient from $\mathcal{L}_{\text{CE}}$ does not flow through RD.
- **Deployment**: RDs are NOT used at inference time; only functional adapters and router are active.

### Expandable Weighting Router $h_{\psi^l}$
- **Purpose**: Learn a soft weighted mixture over functional adapters to enable knowledge sharing.
- **Inputs**: $\mathbf{x}^l \in \mathbb{R}^d$
- **Outputs**: $\mathbf{w}^l \in \mathbb{R}^{K^l}$ (mixture weights, sum to 1)
- **Architecture**: Linear($d \to K^l$) + Softmax; $\mathbf{W}^l_{\text{mix}} \in \mathbb{R}^{d \times K^l}$.
- **Key design choice**: When a new adapter is added, only the new column of $\mathbf{W}^l_{\text{mix}}$ is learnable; existing columns frozen.

### Classification Head
- **Purpose**: Map [CLS] features to class logits.
- **Inputs**: Final ViT [CLS] token representation
- **Outputs**: Class probabilities
- **Key design choice**: Expanded when new tasks arrive (new columns added for new classes); existing columns frozen.

## Interaction Flow: Training Phase (New Task $t$)

1. **Scanning phase**: For each eligible layer $l$ (shallow to deep), pass all Task $t$ samples through frozen ViT + existing adapters; compute z-scores from all RDs at layer $l$.
2. **Expansion decision**: If all z-scores exceed threshold $\tau$ for any sample, trigger expansion at layer $l$.
3. **Module addition**: Add new $(f_{\phi_{K^l+1}^l}, g_{\varphi_{K^l+1}^l})$; expand router $\mathbf{W}^l_{\text{mix}}$ by one column.
4. **Training**: Train new adapter + RD + new router column for task $t$; freeze all other parameters.
5. **Post-task freeze**: Freeze all newly trained modules; proceed to check deeper layers or next task.

## Interaction Flow: Inference Phase

1. Pass input through frozen ViT layers.
2. At each layer $l$: compute router weights $\mathbf{w}^l = \text{softmax}(\mathbf{x}^l \cdot \mathbf{W}^l_{\text{mix}})$.
3. Compute $\mathbf{x}^l_{\text{out}} = \text{MLP}(\mathbf{x}^l) + \sum_k w_k^l \cdot f_{\phi_k^l}(\mathbf{x}^l)$.
4. Classify with expanded classification head (no RDs used at inference).
