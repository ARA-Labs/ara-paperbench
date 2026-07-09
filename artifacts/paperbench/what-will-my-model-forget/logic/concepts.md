# Concepts

## Model Refinement
- **Notation**: $f_i \leftarrow \text{FineTune}(f_0, \langle x_i, y_i \rangle, K \text{ steps})$
- **Definition**: The process of updating a deployed language model $f_0$ by performing $K$ gradient steps on a small set of mispredicted examples $D_R$ to correct their predictions, without full retraining from scratch.
- **Boundary conditions**: Applies when model is deployed and making errors; assumes the base model $f_0$ is accessible for further gradient updates. Distinct from model editing methods (e.g., MEND) which learn meta-gradients.
- **Related concepts**: Catastrophic Forgetting, Edit Success Rate, EM Drop Ratio

## Catastrophic Forgetting
- **Notation**: $\text{EMDrop}_{D_{PT}, f_i} = (\text{EM}_{D_{PT}, f_i} - \text{EM}_{D_{PT}, f_0}) / \text{EM}_{D_{PT}, f_0}$
- **Definition**: The phenomenon where fine-tuning a neural network on new data causes it to rapidly lose performance on previously learned tasks. Measured as EM Drop Ratio on upstream pretraining data $D_{PT}$ after model refinement.
- **Boundary conditions**: More severe with higher learning rates and more gradient steps; less severe with parameter-efficient methods (LoRA, head-only). Positive EM Drop means performance decreased; negative means increased.
- **Related concepts**: Model Refinement, Logit-Change Transfer, Replay-Based Methods

## Logit-Change Transfer
- **Notation**: $\Delta\hat{f}_i(x_j) = \hat{f}_i(x_j) - \hat{f}_0(x_j) \approx \Theta(x_j, x_i)\Theta^{-1}(x_i, x_i)[\hat{f}_i(x_i) - \hat{f}_0(x_i)]$
- **Definition**: The empirical observation that the change in pre-softmax logit scores of an online-learned example $x_i$ after a gradient step partially transfers to the logit change of an upstream pretraining example $x_j$, following the relationship derived from first-order Taylor expansion around the Neural Tangent Kernel.
- **Boundary conditions**: Derivation assumes a single gradient step and first-order Taylor approximation. More accurate when only LM heads are tuned (exact for head-only, approximate for LoRA/Full FT). Transfer occurs even for semantically unrelated example pairs.
- **Related concepts**: Neural Tangent Kernel, Logit-Based Forecasting, Forecasting Forgetting

## Neural Tangent Kernel (NTK)
- **Notation**: $\Theta(x_j, x_i) = \nabla_\theta \hat{f}_0(x_j) \nabla_\theta \hat{f}_0(x_i)^T \in \mathbb{R}^{TV \times TV}$
- **Definition**: A kernel function measuring the inner product of gradients of the model output with respect to parameters, evaluated at two different inputs. Controls how learning from one example affects the model's predictions on another. $T$ = output length, $V$ = vocabulary size.
- **Boundary conditions**: Computing the full NTK for large LMs is prohibitively expensive (requires $TV$ backward passes). Computationally tractable only when fine-tuning only the LM head (gradients are then just example representations). The paper approximates it with a trainable low-rank kernel.
- **Related concepts**: Logit-Change Transfer, Trainable Logit-Based Forecasting

## Trainable Logit-Based Forecasting Model
- **Notation**: $\tilde{\Theta}(x_j, x_i) = h(x_j, y_j) h(x_i, y_i)^T \in \mathbb{R}^{T \times T}$, where $h: (x, y) \mapsto \mathbb{R}^{T \times d}$
- **Definition**: An approximation of the NTK-based logit-change transfer, where the ground-truth kernel $\Theta(x_j, x_i)\Theta^{-1}(x_i, x_i)$ is replaced by a trainable low-rank kernel $h(x_j, y_j)h(x_i, y_i)^T$. The encoding function $h$ maps input-output pairs to low-dimensional representations of output tokens. Trained using a margin loss to predict whether $x_j$ will be forgotten.
- **Boundary conditions**: Effective on BART0 but fails to fit logit dynamics on FLAN-T5. Does not require inference with updated model $f_i$ at test time (logits of $x_i$ and $x_j$ from base model are cached).
- **Related concepts**: Logit-Change Transfer, NTK, Representation-Based Forecasting

## Representation-Based Forecasting Model
- **Notation**: $g(\langle x_i, y_i\rangle, \langle x_j, y_j\rangle) = \sigma(h(x_j, y_j) h(x_i, y_i)^T + b_j)$
- **Definition**: A black-box binary classifier that directly predicts whether $x_j$ will be forgotten upon learning $x_i$, based on the inner product of learned averaged token representations $h(\cdot) \in \mathbb{R}^d$ plus a frequency-prior bias term $b_j$. Trained with binary cross-entropy loss, with positive-pair weight $\alpha=0.1$.
- **Boundary conditions**: Does not interpret *how* forgetting occurs; only predicts *whether* it occurs. Generalizes across model types (BART0, FLAN-T5) and fine-tuning strategies. Computationally efficient: $O(N_{PT} H)$ at inference time.
- **Related concepts**: Trainable Logit-Based Forecasting, Frequency Prior

## Frequency Prior
- **Notation**: $b_j = \log\left(\frac{|\{⟨x_i,y_i⟩ \in D^{\text{train}}_R \mid z_{ij}=1\}|}{|D^{\text{train}}_R|}\right) - \log\left(\frac{|\{⟨x_i,y_i⟩ \in D^{\text{train}}_R \mid z_{ij}=0\}|}{|D^{\text{train}}_R|}\right)$
- **Definition**: The log odds that a specific upstream example $\langle x_j, y_j\rangle$ is forgotten (marginalizing over all online examples in the training set). Serves as a bias term in the representation-based forecasting model, capturing global forgettability of each upstream example independent of which online example is learned.
- **Boundary conditions**: Computed from training split $D^{\text{train}}_R$ and fixed at inference time. Beneficial especially for OOD generalization; without it, the model may fail to capture frequency-level patterns.
- **Related concepts**: Representation-Based Forecasting, Threshold-Based Forecasting

## Edit Success Rate
- **Notation**: $\text{EditSucc} = |\{⟨x_i, y_i⟩ \in D_R \mid f_i(x_i) = y_i\}| / |D_R|$
- **Definition**: The proportion of mispredicted examples in $D_R$ that are correctly predicted by the updated model $f_i$ after model refinement. Measures whether the refinement objective is met.
- **Boundary conditions**: Approaches 100% immediately after fine-tuning a single error (all methods achieve >95% right after fixing), but drops over time in sequential settings due to forgetting of online learned examples. High edit success rate may conflict with low forgetting.
- **Related concepts**: Model Refinement, EM Drop Ratio

## EM Drop Ratio
- **Notation**: $\text{EMDrop}(D_{PT}, f_i, f_0) = (\text{EM}_{D_{PT}, f_i} - \text{EM}_{D_{PT}, f_0}) / \text{EM}_{D_{PT}, f_0}$
- **Definition**: The relative change in Exact Match score on upstream pretraining data $D_{PT}$ between the updated model $f_i$ and the base model $f_0$. Negative values indicate improvement; positive values indicate forgetting.
- **Boundary conditions**: Computed after sequential error fixing on $D^{\text{test}}_R$ (Table 3) or single-error fixing (Table 4). Uses 100 examples per task across 36 P3 tasks as $D_{PT}$.
- **Related concepts**: Edit Success Rate, Catastrophic Forgetting

## Threshold-Based Forecasting
- **Notation**: $g(\langle x_i, y_i\rangle, \langle x_j, y_j\rangle) = \mathbf{1}\left[|\{j \in 1..J \mid z_{ij}=1\}| \geq \gamma\right]$
- **Definition**: A non-trainable baseline that predicts an upstream example $\langle x_j, y_j\rangle$ will be forgotten if it has been forgotten more than $\gamma$ times in the training set, regardless of the specific online example being learned. The threshold $\gamma$ is tuned to maximize F1 on $D^{\text{train}}_R$.
- **Boundary conditions**: Does not capture interactions between pairs of examples; treats forgettability as a property of $x_j$ only. Serves as a lower bound for methods that should capture interaction effects.
- **Related concepts**: Representation-Based Forecasting, Frequency Prior
