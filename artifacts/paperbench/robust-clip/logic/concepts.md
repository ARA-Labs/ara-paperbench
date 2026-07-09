# Concepts

## FARE (Fine-tuning for Adversarially Robust Embeddings)
- **Notation**: $\mathcal{L}_{\text{FARE}}(\phi, x) = \max_{\|z - x\|_\infty \leq \varepsilon} \|\phi(z) - \phi_{\text{Org}}(x)\|_2^2$
- **Definition**: An unsupervised adversarial fine-tuning objective for CLIP's vision encoder that enforces the adversarially-perturbed embedding to remain close (in ℓ₂) to the original clean embedding. The fine-tuned encoder is obtained by $\phi_{\text{FT}} = \arg\min_\phi \sum_i \mathcal{L}_{\text{FARE}}(\phi, x_i)$.
- **Boundary conditions**: Applicable to any foundation model with an intermediate embedding layer linking modalities. Requires access to original encoder φ_Org (frozen). No labels required. Computed on class token only (sufficient for downstream quality).
- **Related concepts**: TeCoA, PGD Attack, CLIP Vision Encoder, ℓ∞ Threat Model

## TeCoA (Text-guided Contrastive Adversarial Training)
- **Notation**: $\mathcal{L}_{\text{TeCoA}}(y, f(\phi, x)) = -\log\frac{e^{f_y(\phi,x)}}{\sum_k e^{f_k(\phi,x)}}$; $\phi_{\text{FT}} = \arg\min_\phi \sum_i \max_{\|z-x_i\|_\infty \leq \varepsilon} \mathcal{L}_{\text{TeCoA}}(y_i, f(\phi, z))$
- **Definition**: Supervised adversarial fine-tuning of CLIP's vision encoder using cross-entropy loss on ImageNet zero-shot classification logits (cosine similarities to class text embeddings). Proposed by Mao et al. (2023).
- **Boundary conditions**: Requires ImageNet labels. Loss is cosine-similarity based, hence invariant to radial rescaling of embeddings — may introduce arbitrary radial distortions. Generalizes poorly to non-ImageNet classes.
- **Related concepts**: FARE, CLIP Vision Encoder, Zero-Shot Classification, ℓ∞ Threat Model

## CLIP Vision Encoder (φ)
- **Notation**: $\phi: \mathcal{I} \rightarrow \mathbb{R}^D$; architecture: ViT-L/14 with image resolution 224×224
- **Definition**: The image encoding component of CLIP (Radford et al., 2021) that maps images to D-dimensional feature vectors. In downstream LVLMs (LLaVA, OpenFlamingo), the encoder is frozen and all tokens (or the class token) are used. Fine-tuning in FARE updates only φ while keeping the text encoder ψ frozen.
- **Boundary conditions**: ViT-L/14 variant is the focus of this paper (used by OF and LLaVA-1.5). Training of downstream LVLMs need not be modified.
- **Related concepts**: FARE, Zero-Shot Classification, LVLM

## Zero-Shot Classification (CLIP)
- **Notation**: $\hat{y} = \arg\max_{k=1,\ldots,K} \cos(\phi(x), \psi(t_k))$ where $t_k = $ "A photo of <class k>"
- **Definition**: Classification by comparing image embedding cosine similarity to text embeddings of class name prompts. No training data for the target classes is used. The classifier logits are $f_k(\phi, x) = \cos(\phi(x), \psi(t_k))$.
- **Boundary conditions**: Requires a text encoder ψ. Performance depends on quality of class prompt templates. FARE preserves zero-shot performance by keeping embeddings close to φ_Org.
- **Related concepts**: CLIP Vision Encoder, TeCoA, FARE

## ℓ∞ Threat Model
- **Notation**: $\|z - x\|_\infty \leq \varepsilon$, where $\varepsilon \in \{2/255, 4/255\}$; $z \in \mathcal{I}$
- **Definition**: The adversarial perturbation set constraining each pixel-wise change to at most ε in absolute value. The adversarial image z must also lie in the valid image domain I. FARE and TeCoA are trained with ε ∈ {2/255, 4/255}.
- **Boundary conditions**: ε = 2/255 produces imperceptible perturbations; ε = 4/255 may be noticed with close attention. Models trained at ε=2/255 provide some robustness when tested at ε=4/255.
- **Related concepts**: PGD Attack, FARE, TeCoA, APGD

## PGD Attack (Projected Gradient Descent)
- **Notation**: $z_{t+1} = \Pi_{\|z-x\|_\infty \leq \varepsilon}(z_t + \alpha \cdot \text{sign}(\nabla_z \mathcal{L}))$; momentum factor 0.9; step size α = 1/255; 10 steps for training
- **Definition**: Iterative first-order attack that maximizes a loss function subject to an ℓ∞ perturbation constraint. Used as the inner maximization solver in adversarial training (both FARE and TeCoA). Initialization: uniform random perturbation in ℓ∞ ball.
- **Boundary conditions**: 10 steps used during fine-tuning (sufficient for short fine-tuning regime). 100 steps used during evaluation (APGD). Step size set to 1/255. Gradient normalization with element-wise sign for ℓ∞.
- **Related concepts**: FARE, TeCoA, APGD, ℓ∞ Threat Model

## APGD (Auto Projected Gradient Descent)
- **Notation**: First two attacks of AutoAttack (Croce & Hein, 2020): APGD-CE (cross-entropy loss) and APGD-DLR (targeted DLR loss); 100 iterations each
- **Definition**: A parameter-free variant of PGD with adaptive step size, used for adversarial evaluation (not training). For LVLM evaluation, run at half precision (100 iterations) then single precision. For zero-shot classification, uses targeted DLR loss (stronger than untargeted used by Mao et al.).
- **Boundary conditions**: Initial step size set to ε. For targeted attacks on LVLMs: 10,000 iterations. Only APGD-CE used for binary classification (PCAM dataset).
- **Related concepts**: PGD Attack, ℓ∞ Threat Model, TeCoA, FARE

## LVLM (Large Vision-Language Model)
- **Notation**: LVLM = LLM + frozen CLIP vision encoder + learned connector (projection/cross-attention)
- **Definition**: A large multi-modal model combining a pre-trained LLM with a frozen CLIP vision encoder. The vision encoder output is connected to the LLM via learned projection layers or cross-attention. FARE targets LLaVA-1.5 7B (LLM: Vicuna-7B) and OpenFlamingo 9B (LLM: MPT-7B). Neither the LLM nor the connector needs retraining when substituting FARE-CLIP.
- **Boundary conditions**: Only applicable to LVLMs with frozen vision encoders. FARE does not address robustness of the text modality.
- **Related concepts**: CLIP Vision Encoder, FARE, Zero-Shot Classification

## Embedding Preservation (FARE Theoretical Guarantee)
- **Notation**: $|\cos(\phi_{\text{FT}}(x), \psi(t)) - \cos(\phi_{\text{Org}}(x), \psi(t))| \leq \min\left(\frac{1}{\|\phi_{\text{Org}}(x)\|_2}, \frac{1}{\|\phi_{\text{FT}}(x)\|_2}\right) \cdot \|\phi_{\text{FT}}(x) - \phi_{\text{Org}}(x)\|_2$
- **Definition**: Theorem 3.1: if the ℓ₂ distance between original and fine-tuned embeddings is small, then the cosine similarity between image and text embeddings is also approximately preserved. This guarantees zero-shot classification performance is maintained when FARE loss is small.
- **Boundary conditions**: Bound tightens when embeddings have large norm. The bound applies to any text embedding ψ(t).
- **Related concepts**: FARE, CLIP Vision Encoder, Zero-Shot Classification
