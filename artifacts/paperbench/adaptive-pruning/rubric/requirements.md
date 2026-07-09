# Rubric Requirements — adaptive-pruning
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 123

## Method Implementation

### R01: Code has been implemented such that RoBERTa can...
- **Rubric ID**: 9ad77547-04b6-4558-993b-f22d91203bf1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that RoBERTa can be loaded into memory
- **Parent context**: The required pre-trained models are available

### R02: LoRA is available to be applied to modules...
- **Rubric ID**: 48e1cbcb-4226-4f00-a456-7a8d2025263c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA is available to be applied to modules within transformers
- **Parent context**: LoRA has correctly been setup

### R03: After training a method using LoRA adapters, before...
- **Rubric ID**: d5ec9b1a-d8cb-4196-8cfc-2923638b8483
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: After training a method using LoRA adapters, before performing inference, the LoRA parameters are merged into the parameters of the model
- **Parent context**: LoRA has correctly been setup

### R04: The fine-tuning baseline is implemented by finetuning a...
- **Rubric ID**: 3ec70bbe-9d13-49f5-8145-1dc9682d27e6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The fine-tuning baseline is implemented by finetuning a pre-trained model on a dataset
- **Parent context**: The baselines have been implemented

### R05: The Mask Tuning baseline is implemented, using the...
- **Rubric ID**: 791e26f6-38ea-4e1a-89a9-b0bd251a48ea
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The Mask Tuning baseline is implemented, using the implementation at https://github.com/WoosukKwon/retraining-free-pruning
- **Parent context**: The baselines have been implemented

### R06: In LoRA+Prune, LoRA adapters are first added to...
- **Rubric ID**: c4790fad-070e-401b-bb6b-a163971ba23a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In LoRA+Prune, LoRA adapters are first added to modules of the given model
- **Parent context**: The LoRA+Prune baseline is implemented by first finetuning a model with LoRA adapters, then apply...

### R07: In LoRA+Prune, once the model with LoRA adapters...
- **Rubric ID**: 95d71d15-54a0-421b-b2af-9e6c65e5a004
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In LoRA+Prune, once the model with LoRA adapters has finished finetuning, Mask Tuning is applied to the model
- **Parent context**: The LoRA+Prune baseline is implemented by first finetuning a model with LoRA adapters, then apply...

### R08: The CoFi baseline (also named "Prune+Distill" in Section...
- **Rubric ID**: 1ad3cbb6-04ad-4947-88c9-f4461fa33596
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The CoFi baseline (also named "Prune+Distill" in Section 5.2) is implemented, using the implementation at https://github.com/princeton-nlp/CoFiPruning
- **Parent context**: The baselines have been implemented

### R09: In LoRA+Prune+Distill, LoRA adapters are first added to...
- **Rubric ID**: 92a96898-e039-4a9e-98a1-0b8143bab0d5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In LoRA+Prune+Distill, LoRA adapters are first added to modules of the given model
- **Parent context**: The LoRA+Prune+Distill baseline is implemented

### R10: In LoRA+Prune+Distill, CoFi pruning and distillation is used...
- **Rubric ID**: a7b5b5ae-5a7b-425c-b286-b753e36610d0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In LoRA+Prune+Distill, CoFi pruning and distillation is used but with LoRA parameters only; only the $L_0$ modules (the non-negative stochastic gates in CoFi which collectively determine which weights to set to zero) and LoRA parameters are tuneable
- **Parent context**: The LoRA+Prune+Distill baseline is implemented

### R11: The masked input to the APT adapter is...
- **Rubric ID**: b16c44c6-58e1-4660-a60b-f66b21d43437
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The masked input to the APT adapter is computed as $X \circ m_i$, where $X$ is the input to the adapter and is $m_i \in \mathbb{R}^d_i$ a learnable binary pruning mask
- **Parent context**: The masked input to the adapter is computed

### R12: When APT is applied to MHA layers, $m_i$...
- **Rubric ID**: a1686474-6def-4ed5-8b88-7a6af0659cab
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When APT is applied to MHA layers, $m_i$ prunes the transformers' hidden dimension
- **Parent context**: The masked input to the adapter is computed

### R13: When APT is applied to FFN layers, $m_i$...
- **Rubric ID**: 169a5eb2-e201-49be-bf7f-f977933291f1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When APT is applied to FFN layers, $m_i$ prunes the transformers' hidden dimension
- **Parent context**: The masked input to the adapter is computed

### R14: For the APT adapter implementation, a dynamic rank...
- **Rubric ID**: 3a628b4e-ba0c-457f-ac35-fdf18c8fd356
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, a dynamic rank $r_{apt}$ is defined for each weight matrix, which can vary
- **Parent context**: The new weight matrix is computed, using the original weight matrix $W \in \mathbb{R}^{d_o \times...

### R15: For the APT adapter implementation, a new learnable...
- **Rubric ID**: 18060c53-6871-4aa5-93d5-49f962f7187d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, a new learnable weight matrix $W_A \in \mathbb{R}^{r_{apt} \times d_i}$ is defined
- **Parent context**: The new weight matrix is computed, using the original weight matrix $W \in \mathbb{R}^{d_o \times...

### R16: For the APT adapter implementation, a new learnable...
- **Rubric ID**: ee70fcc6-17cf-490f-ba08-3f2dba12b190
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, a new learnable weight matrix $W_B \in \mathbb{R}^{d_o \times r_{apt}}$ is defined
- **Parent context**: The new weight matrix is computed, using the original weight matrix $W \in \mathbb{R}^{d_o \times...

### R17: For the APT adapter implementation, the new weight...
- **Rubric ID**: bf86efe4-a3cb-4ee3-8c7b-19ab0a3cdf49
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, the new weight matrix is computed as $W + 2 \cdot W_B W_A$
- **Parent context**: The new weight matrix is computed, using the original weight matrix $W \in \mathbb{R}^{d_o \times...

### R18: For the APT adapter implementation, the new weight...
- **Rubric ID**: bb7ec9df-02b9-43e0-92c9-dc1b5429ef23
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, the new weight matrix is multipled by the masked input
- **Parent context**: The APT adapter architecture has been implemented, following Section 4.1

### R19: For the APT adapter implementation, the output of...
- **Rubric ID**: 5f68b482-6b70-43d8-973b-da59eab1f6ee
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, the output of the multiplication between the updated weights and masked input is masked by a learnable binary pruning mask $m_o \mathbb{R}^d_o$
- **Parent context**: The output of the APT adapter is correctly computed

### R20: When the APT adapter is applied to MHA...
- **Rubric ID**: 9500d7e2-8f9a-446a-8da0-7f0e4621db39
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When the APT adapter is applied to MHA layers, $m_o$ prunes attention heads
- **Parent context**: The output of the APT adapter is correctly computed

### R21: When the APT adapter is applied to FFN...
- **Rubric ID**: 472390c9-f791-4705-ab68-92c155f904d1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When the APT adapter is applied to FFN layers, $m_o$ prunes internal neurons in the FFN layers
- **Parent context**: The output of the APT adapter is correctly computed

### R22: For a parameter $W_{i,j}$ that is not in...
- **Rubric ID**: 56fadbbe-1aab-4a95-9fd6-08accc31726b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For a parameter $W_{i,j}$ that is not in an APT adapter layer, the salience is computed as $S(W_{i,j}) = \left| W_{i,j} \cdot \frac{\partial \mathcal{L}}{\partial W_{i,j}} \right|$
- **Parent context**: Outlier-aware salience score is implemented, following equations 3 and 9

### R23: For an APT adapter layer, the salience is...
- **Rubric ID**: 67496368-0dd9-4422-b0f2-6fca77abe7a6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For an APT adapter layer, the salience is computed following equation 9 as the sum of the block-wise frozen weight salience and the corresponding tuning weight
- **Parent context**: Outlier-aware salience score is implemented, following equations 3 and 9

### R24: Outlier-aware salience for a block is computed as...
- **Rubric ID**: 7f8d2c8b-7078-4e1f-b6f2-7e2c92240b89
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Outlier-aware salience for a block is computed as $\hat{S}(W_{:,j}) = \tilde{S}(W_{:,j}) + \left( \text{Kurt}(O_{j,:}) \right)^{\frac{1}{2}}$, where $\tilde{S}$ is the salience score, $O_{:,j} = W_{:,j} \circ X_{j,:}^T$ represents the activation, and $\text{Kurt}(\cdot)$ stands for Kurtosis
- **Parent context**: Outlier-aware salience score is implemented, following equations 3 and 9

### R25: During training, the outlier-aware salience of each block...
- **Rubric ID**: 6c5119f5-f5ff-43bd-a2ce-3965c4befe2c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During training, the outlier-aware salience of each block is computed as an exponential moving-average $\overline{S}^{(t)}(m) \gets 0.85 \overline{S}^{(t-1)}(m) + 0.15 \hat{S}(m)$, where $\overline{S}^{(t)}(m)$ is the moving-average of block $m$ at time step $t$, and $\hat{S}(m)$ is the current outlier-aware salience score of block $m$
- **Parent context**: Outlier-aware salience score is implemented, following equations 3 and 9

### R26: Given a hidden dimensionality $d_m$ and number of...
- **Rubric ID**: 293d6fac-aff3-4b99-b709-e803ff9d11a4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a hidden dimensionality $d_m$ and number of attention heads $n_h$, the number of parameters of a MHA head is computed as $4 \times d_m \times d_m / n_h$
- **Parent context**: Computing the parameter count for different blocks is implemented correctly following equations 1...

### R27: Given a hidden dimensionality $d_m$, the number of...
- **Rubric ID**: 4a6f0dfe-c9c0-43b6-b910-7b7257b56fe6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a hidden dimensionality $d_m$, the number of parameters of a FFN neuron is computed as $2 \times d_m$
- **Parent context**: Computing the parameter count for different blocks is implemented correctly following equations 1...

### R28: Given a hidden dimensionality $d_m$, number of layers...
- **Rubric ID**: 87383bb6-5e78-4acd-a7fb-ce8cdcef77d1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a hidden dimensionality $d_m$, number of layers $n_L$, and number of neurons in the FFN layer $n_f$, the number of parameters associated with a transformers hidden dimension across all layers is computed as $n_L \times (4 d_m + 2 n_f)$
- **Parent context**: Computing the parameter count for different blocks is implemented correctly following equations 1...

### R29: For a block with salience $S$ and number...
- **Rubric ID**: 1d80f3a3-58f0-4419-976c-5786053c9b4c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For a block with salience $S$ and number of parameters $\mathcal{C}$, the salience density is computed as the salience divided by the parameter number $S / \mathcal{C}$
- **Parent context**: APT Blocks are sorted in descending order by salience density

### R30: The blocks are sorted by their salience density...
- **Rubric ID**: 4221dd78-0c29-416e-abd1-fa9b0a69d0ed
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The blocks are sorted by their salience density in descending order
- **Parent context**: APT Blocks are sorted in descending order by salience density

### R31: A function $f$ for identifying a block's category...
- **Rubric ID**: 50d7ad1a-8908-427c-9830-585bfd7086f4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A function $f$ for identifying a block's category is implemented, following equation 13. $f$ returns 0 when block $b_i$ is a head, 1 if $b_i$ is a neuron, and 2 if $b_i$ is a dimension
- **Parent context**: Low-cost Adaptive LM Pruning is implemented, as described in Section 4.2 and Appendix B

### R32: Following equation 14, given any index $i$ and...
- **Rubric ID**: c32d372a-826a-4bce-b9a0-5b5100afdd43
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Following equation 14, given any index $i$ and a sorted list of N blocks in descending order of salience density, the number of blocks in the top-$i$ blocks that are added to heads is computed as $n_h^\prime = \sum_{j=0}^{i-1} \delta (0, f(b_j))$, where $\delta (i, j)$ is the Kronecker delta function that returns 1 if $i=j$, and otherwise 0, and $f$ is the function that returns 0 when block $b_i$ is a head, 1 if $b_i$ is a neuron, and 2 if $b_i$ is a dimension
- **Parent context**: Following equation 14, given any index $i$, the parameter number of the LM consisting of the top-...

### R33: Following equation 14, given any index $i$ and...
- **Rubric ID**: 7de18cb9-893c-4faf-9fff-59347b183ec3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Following equation 14, given any index $i$ and a sorted list of N blocks in descending order of salience density, the number of blocks in the top-$i$ blocks that are added to neurons is computed as $n_f^\prime = \sum_{j=0}^{i-1} \delta (1, f(b_j))$, where $\delta (i, j)$ is the Kronecker delta function that returns 1 if $i=j$, and otherwise 0, and $f$ is the function that returns 0 when block $b_i$ is a head, 1 if $b_i$ is a neuron, and 2 if $b_i$ is a dimension
- **Parent context**: Following equation 14, given any index $i$, the parameter number of the LM consisting of the top-...

### R34: Following equation 14, given any index $i$ and...
- **Rubric ID**: 256c6f16-a3d6-46ce-a5b4-edc6c2a96653
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Following equation 14, given any index $i$ and a sorted list of N blocks in descending order of salience density, the number of blocks in the top-$i$ blocks that are added to dimensions is computed as $d_m^\prime = \sum_{j=0}^{i-1} \delta (2, f(b_j))$, where $\delta (i, j)$ is the Kronecker delta function that returns 1 if $i=j$, and otherwise 0, and $f$ is the function that returns 0 when block $b_i$ is a head, 1 if $b_i$ is a neuron, and 2 if $b_i$ is a dimension
- **Parent context**: Following equation 14, given any index $i$, the parameter number of the LM consisting of the top-...

### R35: Following equation 14, given any index $i$ and...
- **Rubric ID**: d3dcd793-2ff9-4ef2-89a2-0e38815a1637
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Following equation 14, given any index $i$ and a sorted list of N blocks in descending order of salience density, the parameter number is computed as $C_{\text{top}-i} = (4d_h^\prime \cdot n_h^\prime + 2n_f^\prime) \cdot d_m^\prime$, where $d_h^\prime$ is the number of heads in the model, $n_h^\prime$ is the number of the top-$i$ blocks that are added to heads, $n_f^\prime$ is the number of the top-$i$ blocks that are added to neurons, and $d_m^\prime$ is the number of the top-$i$ blocks that are added to dimensions
- **Parent context**: Following equation 14, given any index $i$, the parameter number of the LM consisting of the top-...

### R36: In Low-cost Adaptive LM Pruning, binary search is...
- **Rubric ID**: b424b0fc-5ca1-40d0-95c6-095dea897198
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Low-cost Adaptive LM Pruning, binary search is used to get the top-$i$ salient blocks
- **Parent context**: Low-cost Adaptive LM Pruning is implemented, as described in Section 4.2 and Appendix B

### R37: In Low-cost Adaptive LM Pruning, blocks that are...
- **Rubric ID**: 215e9429-279e-4fb5-9bce-7cbf69c1f76e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Low-cost Adaptive LM Pruning, blocks that are marked to be pruned have their corresponding masks decreased by 0.01
- **Parent context**: Low-cost Adaptive LM Pruning is implemented, as described in Section 4.2 and Appendix B

### R38: In Adaptive and Efficient LM Tuning, given an...
- **Rubric ID**: 664da958-cb9d-4efd-aec5-9c30d4e0c64f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Adaptive and Efficient LM Tuning, given an APT adapter $H_{apt}$, the importance score is computed as $\mathcal{I}(H_{apt}) = \sum_{i,j} S(W_{Bi,j})$, the summation of the parameter salience scores in $W_B$ (where $W_B \in \mathbb{R}^{d_o \times r_{apt}}$ is an APT tuning parameter)
- **Parent context**: Adaptive and Efficient LM Tuning is implemented, as described in Section 4.3

### R39: In Adaptive and Efficient LM Tuning, APT adapters...
- **Rubric ID**: 7fd4d11b-41d3-4036-b203-9bd71cc003b5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Adaptive and Efficient LM Tuning, APT adapters are sorted by their importance score
- **Parent context**: Adaptive and Efficient LM Tuning is implemented, as described in Section 4.3

### R40: When increasing tuning parameter from $\Delta t$ to...
- **Rubric ID**: 0e3baed9-9122-4c55-9326-29edf8f0b4c4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When increasing tuning parameter from $\Delta t$ to $Delta t^{\prime}$, the salient layer's rank is changed from $r_{apt}$ to $r_{apt}^\prime=\lfloor{r_{apt} \cdot \frac{\Delta_t^\prime}{\Delta_t }\rfloor$
- **Parent context**: The ranks of the top-half blocks (blocks with largest importance) is linearly increased

### R41: When adding parameters, random Gaussian initialized parameters $\mathcal{N}(0,...
- **Rubric ID**: 48d8285a-bcee-412a-995e-dea44e2fff2f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When adding parameters, random Gaussian initialized parameters $\mathcal{N}(0, \sigma^2)$ are concatenated to $W_A$, and zeros are concatenated to $W_B$, where $W_A \in \mathbb{R}^{r_{apt} \times d_i}$,  $W_B \in \mathbb{R}^{d_o \times r_{apt}}$ are both APT tuning parameters
- **Parent context**: The ranks of the top-half blocks (blocks with largest importance) is linearly increased

### R42: In Efficient Self-Knowledge Distillation, at each training epoch,...
- **Rubric ID**: 2b494437-89dd-4517-b9fb-634cbc20de15
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, at each training epoch, intermediate layers from the teacher model are randomly selected for distillation; 4 teacher layers are randomly sampled in each quarter slice of the layers (e.g. for a 12-layer network the slices would be: 0-2, 3-5, 6-8, 9-11)
- **Parent context**: Efficient Self-Knowledge Distillation is implemented, as described in Section 4.4

### R43: In Efficient Self-Knowledge Distillation, the teacher-student layer-mapping function...
- **Rubric ID**: 92744e38-5ae3-4873-8ed1-c0c431e77ad3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, the teacher-student layer-mapping function $m(\cdot)$ is implemented to match 4 teacher layers with the closest, non-pruned student layers, using the same method introduced in CoFi (Xia et al., 2022). For each of the 4 teacher layers, the layer mapping function dynamically determines which of the student layers is closest; $\mathop{\arg \min}\limits_{j:\mathbf{z}_{FFN}^{(j)}>0} \text{MSE} (W_{\text{layer}} H_s^j, H_t^i)$, where $H_s^j, H_t^i$ are hidden representations from the $j$-th student FFN layer and $i$-th teacher layer respectively, and $W_{\text{layer}} \in \mathbb{R}^{d\timesd}$ is a learnable linear transformation matrix, initialized as an identity matrix
- **Parent context**: In Efficient Self-Knowledge Distillation, the teacher-student layer-mapping function $m(\cdot)$ i...

### R44: In Efficient Self-Knowledge Distillation, the teacher-student layer-mapping function...
- **Rubric ID**: 39282784-429b-4b1f-97a1-729417989069
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, the teacher-student layer-mapping function $m(\cdot)$ is re-computed every training step
- **Parent context**: In Efficient Self-Knowledge Distillation, the teacher-student layer-mapping function $m(\cdot)$ i...

### R45: In Efficient Self-Knowledge Distillation, the hidden layer distillation...
- **Rubric ID**: 28658a50-5fa0-47d4-92c2-cdafb0d751aa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, the hidden layer distillation loss is defined as $\mathcal{L}_{\text{layer}} = \sum_{i=1}^4 \text{MSE}(\text{Tr}(H_s^{\phi(i)}), H_t^i)$, where $\text{Tr}$ denotes the tunable LoRA layer for layer transformation, initialized as an identical matrix $\mathcal{I}$, and $\phi(\cdot)$ is the teacher-student layer-mapping function
- **Parent context**: Efficient Self-Knowledge Distillation is implemented, as described in Section 4.4

### R46: In Efficient Self-Knowledge Distillation, cross-entropy loss between the...
- **Rubric ID**: 8f4b756f-947a-4194-929a-06e791900ec7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, cross-entropy loss between the pruned student's and teacher's output probability distributions $\mathbf{p}_s$ and $\mathbf{p}_t$ is computed as $\mathcal{L}_{\text{pred}} = D_{\text{KL}}(\mathbf{p}_s \,\|\, \mathbf{p}_t)$
- **Parent context**: The distillation loss $L_{\text{distil}}$ is implemented

### R47: In Efficient Self-Knowledge Distillation, when training on GLUE...
- **Rubric ID**: 1e6df51c-71c6-4712-95bd-c3ff8f9b8d69
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, when training on GLUE tasks, the layer distillation is combined with the prediction-layer distillation: $\mathcal{L}_{\text{distill}} = \mathcal{L}_{\text{pred}} + 0.9 \mathcal{L}_{\text{layer}}$
- **Parent context**: The distillation loss $L_{\text{distil}}$ is implemented

### R48: In Efficient Self-Knowledge Distillation, when training on SQuAD...
- **Rubric ID**: 16f88c2e-9b4d-44b0-8417-44d14a96f729
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, when training on SQuAD or CNN/DM, the layer distillation is combined with the prediction-layer distillation: $\mathcal{L}_{\text{distill}} = 0.1 \mathcal{L}_{\text{pred}} + 0.9 \mathcal{L}_{\text{layer}}$
- **Parent context**: The distillation loss $L_{\text{distil}}$ is implemented

### R49: Following equation 7, the distillation objective is defined...
- **Rubric ID**: 3f534396-e443-46f3-9ea8-a215dd653142
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Following equation 7, the distillation objective is defined as $\mathcal{L} = \mu \mathcal{L}_{\text{distill}} + (1 - \mu) \mathcal{L}_{\text{ft}}$, where $\mathcal{L}_{ft}$ is the supervised fine-tuning objective
- **Parent context**: Efficient Self-Knowledge Distillation is implemented, as described in Section 4.4

### R50: When pruning LMs with APT, given a pre-determined...
- **Rubric ID**: 50acfee7-499d-4b68-8205-a346d6aa16e1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When pruning LMs with APT, given a pre-determined target sparsity $\gamma_T$ and total number of pruning training steps $T$, the target sparsity at timestep $t$ is computed by $\gamma_t = \gamma_T + (1 - \gamma_T) \left(1 - \frac{t}{T}\right)^3$
- **Parent context**: APT has been implemented

### R51: After training a model using APT adapters, before...
- **Rubric ID**: ca6ea57b-3ed0-40ee-96e8-123036828dfb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: After training a model using APT adapters, before performing inference, the APT parameters are merged into the parameters of the model
- **Parent context**: APT has been implemented

### R52: LoRA and APT adapters are added to queries...
- **Rubric ID**: dde4b5f2-f505-4592-a0ca-2fa8b50ddf12
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA and APT adapters are added to queries and values of MHA layers in RoBERTa and T5
- **Parent context**: The LoRA and APT adapters are applied to the correct modules of RoBERTa and T5

### R53: LoRA and APT adapters are added to the...
- **Rubric ID**: 2a3669df-4e69-464a-b0c5-47b9001e2281
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA and APT adapters are added to the up layer in FFN layers in RoBERTa and T5
- **Parent context**: The LoRA and APT adapters are applied to the correct modules of RoBERTa and T5

## Data Processing & Preparation

### R54: Code for accessing the train and dev splits...
- **Rubric ID**: 5fef034a-5a8f-4ada-848c-336469238e68
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code for accessing the train and dev splits from the MNLI dataset from the GLUE benchmark has been implemented
- **Parent context**: The required pre-trained datasets have been setup

## Dataset & Model Acquisition

### R55: Code has been implemented such that T5, specifically...
- **Rubric ID**: fa5309a4-2d43-45ef-80f6-df26a5559be2
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been implemented such that T5, specifically t5-lm-adapt, can be loaded into memory
- **Parent context**: The required pre-trained models are available

### R56: Code for accessing the train and dev splits...
- **Rubric ID**: c9daa9ee-7667-4795-9c83-3f5c9c88a65f
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and dev splits from the SST2 dataset from the GLUE benchmark has been implemented
- **Parent context**: The required pre-trained datasets have been setup

### R57: Code for accessing the train and dev splits...
- **Rubric ID**: 8605df37-4a11-4c87-8eae-bfb10b6bf5b9
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and dev splits from the SQuAD 2.0 benchmark has been implemented
- **Parent context**: The required pre-trained datasets have been setup

### R58: Code for accessing the train and test sets...
- **Rubric ID**: 4e1da193-e3eb-4cc0-af44-74314ba83668
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test sets from the CNN Dailymail (CNN/DM) dataset has been implemented
- **Parent context**: The required pre-trained datasets have been setup

## Experimental Setup (Development)

### R59: In LoRA+Prune, the model with the LoRA adapters...
- **Rubric ID**: e2236b08-c76c-4236-b3d6-f4c2bcd3e9e5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In LoRA+Prune, the model with the LoRA adapters added is finetuned
- **Parent context**: The LoRA+Prune baseline is implemented by first finetuning a model with LoRA adapters, then apply...

### R60: For the APT adapter implementation, the original weight...
- **Rubric ID**: c99479b2-0e4e-435e-a574-53a7ae8d4c7f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the APT adapter implementation, the original weight matrix $W$ is kept frozen; it isn't updated during training
- **Parent context**: The new weight matrix is computed, using the original weight matrix $W \in \mathbb{R}^{d_o \times...

### R61: In Efficient Self-Knowledge Distillation, $\mu$ is a moving...
- **Rubric ID**: 4b5df1a0-8ade-4ffa-a0b6-07fe15c74174
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In Efficient Self-Knowledge Distillation, $\mu$ is a moving term that linearly scales from 0 to 1 during pruning
- **Parent context**: Efficient Self-Knowledge Distillation is implemented, as described in Section 4.4

### R62: When pruning LMs with APT, the LM is...
- **Rubric ID**: 43b7fa8c-b6d9-43fb-be02-91df6e3ac7ce
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When pruning LMs with APT, the LM is first pruned and trained with the self-distillation objective for some pre-defined number of epochs, then it is fine-tuned on the same dataset for some other pre-defined number of epochs
- **Parent context**: APT has been implemented

### R63: All models trained on GLUEuse a learning rate...
- **Rubric ID**: e193b120-5b15-442f-ad9c-8d817dea5c66
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models trained on GLUEuse a learning rate of 2e-4
- **Parent context**: The GLUEhyperparameters are configured

### R64: All models trained on GLUEuse a batch size...
- **Rubric ID**: 83a476b8-e3d9-4ce5-b956-e3cac8d8a499
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models trained on GLUEuse a batch size of 32
- **Parent context**: The GLUEhyperparameters are configured

### R65: For every method that isn't Finetune, models trained...
- **Rubric ID**: d441dc31-a89e-483a-996f-4a62517c47e5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For every method that isn't Finetune, models trained on GLUE use 40 epochs
- **Parent context**: The GLUEhyperparameters are configured

### R66: When training on the GLUE dataset using the...
- **Rubric ID**: fe34b5f1-93eb-4175-b53c-5b18b04b032d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training on the GLUE dataset using the Prune+Distill, LoRA+Prune+Distill, or APT methods, the first 20 epochs are used for distillation, and the remaining 20 are for training on the objective
- **Parent context**: The GLUEhyperparameters are configured

### R67: All models trained on SQuAD use a learning...
- **Rubric ID**: 9662eaea-80a1-42d8-969f-c6d3b051806d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models trained on SQuAD use a learning rate of 2e-4
- **Parent context**: The SQuAD hyperparameters are configured

### R68: All models trained on SQuAD use a batch...
- **Rubric ID**: 89b01087-4722-4de3-8e4e-8d75f82f6904
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models trained on SQuAD use a batch size of 32
- **Parent context**: The SQuAD hyperparameters are configured

### R69: For every method that isn't Finetune, models trained...
- **Rubric ID**: c99c524a-17bd-4f7d-93c1-2f4b2b2753d1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For every method that isn't Finetune, models trained on SQuAD use 40 epochs
- **Parent context**: The SQuAD hyperparameters are configured

### R70: When training on the SQuAD dataset using the...
- **Rubric ID**: a5c6d56b-c273-40cf-9ded-82a9267d9c42
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training on the SQuAD dataset using the Prune+Distill, LoRA+Prune+Distill, or APT methods, the first 20 epochs are used for distillation, and the remaining 20 are for training on the objective
- **Parent context**: The SQuAD hyperparameters are configured

### R71: All models trained on CNN/DM use a learning...
- **Rubric ID**: e32c3c58-2be6-4435-a181-9c46588f4945
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models trained on CNN/DM use a learning rate of 1e-4
- **Parent context**: The CNN/DM hyperparameters are configured

### R72: All models trained on CNN/DM use a batch...
- **Rubric ID**: 2fff2695-43e9-4392-ada2-77604e02babc
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models trained on CNN/DM use a batch size of 16
- **Parent context**: The CNN/DM hyperparameters are configured

### R73: For every method that isn't Finetune, models trained...
- **Rubric ID**: f0f7160e-44ba-49de-89eb-d581aed006ee
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For every method that isn't Finetune, models trained on CNN/DM use 16 epochs
- **Parent context**: The CNN/DM hyperparameters are configured

### R74: When training on the CNN/DM dataset using the...
- **Rubric ID**: 908deb8d-c35b-415f-9a18-0d086bab4a87
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training on the CNN/DM dataset using the Prune+Distill, LoRA+Prune+Distill, or APT methods, the first 6 epochs are used for distillation, and the remaining 10 are for training on the objective
- **Parent context**: The CNN/DM hyperparameters are configured

### R75: The adapter ranks $r_{apt}$ in all APT modules...
- **Rubric ID**: 6287838a-d855-40c2-ba76-b3057ecfc68e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The adapter ranks $r_{apt}$ in all APT modules are initialized to 8
- **Parent context**: The hyperparameters have been configured

### R76: The Finetune method is trained for 10 epochs
- **Rubric ID**: 452a6371-176b-4a01-b29b-e74f9278c08e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Finetune method is trained for 10 epochs
- **Parent context**: The hyperparameters have been configured

## Evaluation & Metrics Implementation

### R77: When evaluating models on SST2 and MNLI, the...
- **Rubric ID**: 1fdb66d7-04b9-479e-bcf4-32791841707f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When evaluating models on SST2 and MNLI, the dev set accuracy is reported
- **Parent context**: The required dataset-specific metrics have been implemented

### R78: When evaluating models on SQuAD, the dev set...
- **Rubric ID**: d43a1c9e-74f8-4725-91be-58a38063639a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When evaluating models on SQuAD, the dev set F1 score is reported
- **Parent context**: The required dataset-specific metrics have been implemented

### R79: When evaluating models on CNN/DM, the ROUGE 1/2/L...
- **Rubric ID**: 698b1e1c-4947-4365-a49f-10c6ab66e263
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When evaluating models on CNN/DM, the ROUGE 1/2/L scores on the test set are reported
- **Parent context**: The required dataset-specific metrics have been implemented

### R80: For each method trained on some dataset, the...
- **Rubric ID**: 3aeea066-bf35-4baa-a1e5-864de953d68f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each method trained on some dataset, the train time is measured as the time-to-accuracy of reaching 97% of the dev (/test) set performance of the finetuning baseline
- **Parent context**: Training and evaluation metrics have been implemented

### R81: For each method, when being trained on some...
- **Rubric ID**: 79a20612-83df-424a-9355-068dc18032d7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each method, when being trained on some dataset, code has been implemented to record the max GPU memory utilization, using torch.cuda.max_memory_allocated() (or equivalent)
- **Parent context**: Training and evaluation metrics have been implemented

### R82: For each method, when being evaluated on some...
- **Rubric ID**: 240b99e2-f34e-4a0c-86c2-4454e31b6517
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each method, when being evaluated on some dataset, the speed of inference is measured as the inference throughput (sampled processed per second)
- **Parent context**: Training and evaluation metrics have been implemented

### R83: For each method, when performing inference with some...
- **Rubric ID**: 1ff3dcb3-be14-4770-93a8-dcf721c4e3bd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each method, when performing inference with some dataset, code has been implemented to record the max GPU memory utilization, using torch.cuda.max_memory_allocated() (or equivalent)
- **Parent context**: Training and evaluation metrics have been implemented

### R84: The salience density is only calculated for blocks...
- **Rubric ID**: a3ae8772-f9aa-4f65-a8d2-7a1f94c9ae3c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The salience density is only calculated for blocks that have an APT adapter applied to them
- **Parent context**: APT Blocks are sorted in descending order by salience density

### R85: The salience density of each block is re-computed...
- **Rubric ID**: 8e4cb47d-9829-4357-b3c3-c44799d7f6f2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The salience density of each block is re-computed everytime the number of parameters of the model changes
- **Parent context**: APT Blocks are sorted in descending order by salience density

### R86: For Section 5
- **Rubric ID**: 0c47a836-4eec-478f-9be1-b7c9abd768f1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For Section 5.5, the relative accuracy for some model is computed as the accuracy such model achieves when compared to the accuracy the finetuning baseline achieves
- **Parent context**: The experiments required for Section 5.5 have been run

## Code Execution — Method

### R87: RoBERTa is trained using a modified version of...
- **Rubric ID**: 859bffed-bd82-43db-bed1-443bdf4b1ef0
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: RoBERTa is trained using a modified version of APT that doesn't use adaptive tuning (APT w/o $A_T$) using 60% sparsity
- **Parent context**: The experiments and results related to adaptive tuning in Section 5.6 have been replicated

## Code Execution — Experimental Setup

### R88: RoBERTa with the FT, LoRA, LoRA+Prune, and APT...
- **Rubric ID**: 01d90251-7fc3-4c86-9a5a-aab6ed12d987
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: RoBERTa with the FT, LoRA, LoRA+Prune, and APT methods is trained and evaluated on MNLI, SST2, and SQuAD v2 separately with 60% sparsity
- **Parent context**: RoBERTa is trained and evaluated using various pruning methods

### R89: RoBERTa with the Prune+Distill and LoRA+Prune+Distill methods is...
- **Rubric ID**: 8e9dce7a-d32e-4636-9da7-df9918647823
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: RoBERTa with the Prune+Distill and LoRA+Prune+Distill methods is trained and evaluated on MNLI and SST2 separately with 60% sparsity.
- **Parent context**: RoBERTa is trained and evaluated using various pruning methods

### R90: T5 with the FT, LoRA, LoRA+Prune, and APT...
- **Rubric ID**: dcc716d8-6f57-45be-b4d5-5c1b774b4b6b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: T5 with the FT, LoRA, LoRA+Prune, and APT methods is trained and evaluated on MNLI, SST2, and CNN/DM separately with 60% sparsity
- **Parent context**: The experiments required for Section 5.4 have been run

### R91: RoBERTa is trained and evaluated on SST2 and...
- **Rubric ID**: e9fa1766-f3bd-447a-918d-e6696bf20ecf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: RoBERTa is trained and evaluated on SST2 and MNLI separately with 60% sparsity using a modified version of APT that doesn't use adaptive pruning (APT w/o $A_P$)
- **Parent context**: The experiments and results related to adaptive pruning in Section 5.6 have been replicated

### R92: RoBERTa is trained using 60% sparsity and a...
- **Rubric ID**: e7ad0e1d-93d3-46c9-98c2-cff17945550d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: RoBERTa is trained using 60% sparsity and a modified version of APT that doesn't use self-distillation (APT w/o $D_S$)
- **Parent context**: The experiments and results related to self-distillation in Section 5.6 have been replicated

## Code Execution — Evaluation & Benchmarking

### R93: RoBERTa with the LoRA+Prune, LoRA+Prune+Distill, and Prune+Distill methods...
- **Rubric ID**: d406c635-3506-4ed8-bf4f-ed80d54bc7b2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: RoBERTa with the LoRA+Prune, LoRA+Prune+Distill, and Prune+Distill methods is trained and evaluated on SST2 and MNLI separately, and the relative performance is computed using the average on SST2 and MNLI
- **Parent context**: The experiments required for Section 5.5 have been run

### R94: T5 with the LoRA+Prune method is trained and...
- **Rubric ID**: 24223a79-763d-4cb8-9f73-27fdd358d543
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: T5 with the LoRA+Prune method is trained and evaluated on SST2 and MNLI separately, and the relative performance is computed using the average on SST2 and MNLI
- **Parent context**: The experiments required for Section 5.5 have been run

### R95: RoBERTa with the APT method is trained and...
- **Rubric ID**: 5a92263e-e824-4fe3-bc4f-661fc7ab5c1a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: RoBERTa with the APT method is trained and evaluated on SST2 and MNLI separately for sparsities 40%, 50%, 60%, 70%, 80%, 90%, 95%, and the relative is computed using the average on SST2 and MNLI
- **Parent context**: The experiments required for Section 5.5 have been run

### R96: T5 with the APT method is trained and...
- **Rubric ID**: 8df3184f-06b6-4df1-8234-055b81384970
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: T5 with the APT method is trained and evaluated on SST2 and MNLI separately for sparsities 40%, 50%, 60%, 70%, 80%, 90%, and the relative performance is computed using the average on SST2 and MNLI
- **Parent context**: The experiments required for Section 5.5 have been run

## Result Analysis — Evaluation & Benchmarking

### R97: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: d075f77c-9383-4f7c-8b35-dbb8ad9507a8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa to 60% sparsity, APT converged about 8x faster than the LoRA+Prune baseline
- **Parent context**: The results comparing training time and efficiency of APT compared to LoRA+Prune have been replic...

### R98: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: be593611-3cdd-4a6c-89c6-726831a9382c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa to 60% sparsity, APT used similar GPU memory during both training and inference compared to the LoRA+Prune baseline
- **Parent context**: The results comparing training time and efficiency of APT compared to LoRA+Prune have been replic...

### R99: The recorded metrics show that when pruning T5...
- **Rubric ID**: 7fb47445-dde2-4b4a-957a-777aedae4eae
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning T5 to 60% sparsity, APT converged about 8x faster than the LoRA+Prune baseline
- **Parent context**: The results comparing training time and efficiency of APT compared to LoRA+Prune have been replic...

### R100: The recorded metrics show that when pruning T5...
- **Rubric ID**: c6179a9c-02b7-428b-b019-16d2d490b271
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning T5 to 60% sparsity, APT used similar GPU memory during both training and inference compared to the LoRA+Prune baseline
- **Parent context**: The results comparing training time and efficiency of APT compared to LoRA+Prune have been replic...

### R101: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: cdcbff81-1647-42dd-85fa-851fc14037d7
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT achieves an equal or higher performance than LoRA+Prune across all evaluations
- **Parent context**: The results comparing performance of APT compared to LoRA+Prune have been replicated

### R102: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: fbdc9a9e-6d1a-44a4-972d-995e33e35234
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, the inference efficiency reached by APT is about the same as the LoRA+Prune baseline
- **Parent context**: The results comparing performance of APT compared to LoRA+Prune have been replicated

### R103: The recorded metrics show that when pruning T5...
- **Rubric ID**: de57690a-d1e9-4606-b8d7-dc198bc976da
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning T5 under 60% sparsity, APT has roughly 5% better end-task performance on average than the LoRA+Prune baseline
- **Parent context**: The results comparing performance of APT compared to LoRA+Prune have been replicated

### R104: The recorded metrics show that when pruning T5...
- **Rubric ID**: 737f8df7-95b8-42cb-9e59-8e05bae93052
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning T5 under 60% sparsity, the inference efficiency reached by APT is worse than the LoRA+Prune baseline
- **Parent context**: The results comparing performance of APT compared to LoRA+Prune have been replicated

### R105: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: ec378300-5912-40de-a90e-d5d28f7bea31
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT has similar task accuracy to Prune+Distill across MNLI and SST2
- **Parent context**: The results comparing performance of APT to Prune+Distill have been replicated

### R106: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 37612400-aa24-4650-9402-9b9c536b86a5
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT costs roughly 40% of training memory compared to Prune+Distill
- **Parent context**: The results comparing performance of APT to Prune+Distill have been replicated

### R107: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 9f477ec1-f090-482a-919d-c9050cac0802
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT converges 2.5x faster than Prune+Distill
- **Parent context**: The results comparing performance of APT to Prune+Distill have been replicated

### R108: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: e1fe1c33-bdce-4ee4-a5cb-7ec2b210f6a6
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT achieves better task performance than LoRA+Prune+Distill
- **Parent context**: The results comparing performance of APT to Prune+Distill have been replicated

### R109: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: dc200210-82d1-4f50-ae44-b30bd24cc22b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT requires less training time than LoRA+Prune+Distill
- **Parent context**: The results comparing performance of APT to Prune+Distill have been replicated

### R110: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 5a2b6715-3de9-4527-b9ae-86e28d4713b5
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa and T5 to 60% sparsity, APT requires less memory than LoRA+Prune+Distill
- **Parent context**: The results comparing performance of APT to Prune+Distill have been replicated

### R111: The recorded metrics indicate that APT is about...
- **Rubric ID**: 939d1034-157f-460e-8cf6-fb589ea1f417
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics indicate that APT is about 20% faster in inference than the LoRA+Prune baseline for RoBERTa, when comparing the APT model that achieved the closest accuracy to the LoRA+Prune baseline
- **Parent context**: The results from Section 5.5 have been replicated

### R112: The recorded metrics indicate that APT is about...
- **Rubric ID**: 00ce14bb-60bc-461a-8958-897ca6c75a3d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics indicate that APT is about 7% more memory efficient than the LoRA+Prune baseline for RoBERTa, when comparing the APT model that achieved the closest accuracy to the LoRA+Prune baseline
- **Parent context**: The results from Section 5.5 have been replicated

### R113: The recorded metrics indicate that APT is about...
- **Rubric ID**: 93cb26c7-4166-42c5-8718-8c27d892d682
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics indicate that APT is about 60% faster in inference than the LoRA+Prune baseline for T5, when comparing the APT model that achieved the closest accuracy to the LoRA+Prune baseline
- **Parent context**: The results from Section 5.5 have been replicated

### R114: The recorded metrics indicate that APT is about...
- **Rubric ID**: b7607af8-bc54-4840-9153-9a8b55409c84
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics indicate that APT is about 25% more memory efficient than the LoRA+Prune baseline for T5, when comparing the APT model that achieved the closest accuracy to the LoRA+Prune baseline
- **Parent context**: The results from Section 5.5 have been replicated

### R115: The recorded metrics show that when pruning with...
- **Rubric ID**: 7525718b-1307-426a-9c08-1d1505a08ade
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning with APT w/o $A_P$, the task performance of RoBERTa reaches roughly 94 for SST2 and 87.5 for MNLI
- **Parent context**: The results related to adaptive pruning have been replicated

### R116: The recorded metrics show that when pruning with...
- **Rubric ID**: 16db85a1-c6ea-4e23-86f7-5d538f4f438a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning with APT w/o $A_P$, the RoBERTA training speed with APT w/o $A_P$ is roughly 20% faster than full fine-tuning on the same datasets
- **Parent context**: The results related to adaptive pruning have been replicated

### R117: The recorded metrics show that when pruning with...
- **Rubric ID**: 66039c65-91df-4270-9216-1a31aab5756e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning with APT w/o $A_P$, the RoBERTA training using APT w/o $A_P$ requires roughly 60% of the memory compared to full fine-tuning on the same datasets
- **Parent context**: The results related to adaptive pruning have been replicated

### R118: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 011cf2f5-5a70-44ba-954c-0a3620075f08
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa with APT w/o $A_T$, it achieves roughly 93 on SST2
- **Parent context**: The results related to adaptive tuning have been replicated

### R119: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 1a57a576-01a5-42e4-bb42-cdcdaa3f45e2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa with APT w/o $A_T$, it achieves roughly 84 on MNLI
- **Parent context**: The results related to adaptive tuning have been replicated

### R120: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 26fbd16f-a67f-4464-be72-818898a86f41
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa with APT w/o $A_T$, it has a similar performance as the LoRA+Prune baseline
- **Parent context**: The results related to adaptive tuning have been replicated

### R121: The recorded metrics show that when pruning RoBERTa...
- **Rubric ID**: 70a1b6da-2a1f-475e-b61e-8dbbd1911766
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that when pruning RoBERTa with APT w/o $A_T$, it converged roughly 15% slower than full APT
- **Parent context**: The results related to adaptive tuning have been replicated

### R122: The recorded metrics show that pruning RoBERTa with...
- **Rubric ID**: 9c90df0a-aa9f-4c71-be71-69f5cac2ccc0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that pruning RoBERTa with APT w/o $D_S$ costs roughly 10% less training memory than full APT
- **Parent context**: The results related to self-distillation have been replicated

## Result Analysis — Logging & Presentation

### R123: The recorded metrics show that pruning RoBERTa with...
- **Rubric ID**: 10f451dd-7fac-4566-9e55-1d66c7beceb5
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The recorded metrics show that pruning RoBERTa with APT w/o $D_S$ has roughly 20% faster training time than full APT
- **Parent context**: The results related to self-distillation have been replicated
