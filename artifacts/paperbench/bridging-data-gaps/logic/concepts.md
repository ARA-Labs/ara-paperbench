---
# Concepts

## Diffusion Probabilistic Model (DPM / DDPM)
- **Notation**: $\epsilon_\theta(x_t, t)$, $q(x_t|x_0)$, $p_\theta(x_0)$
- **Definition**: A latent variable generative model that defines a forward diffusion process $q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t}x_0, (1-\bar{\alpha}_t)I)$ and learns a reverse denoising process via a U-Net $\epsilon_\theta$ trained to minimize $\mathcal{L}_{sample}(\theta) := \mathbb{E}_{t,x_0,\epsilon}\|\epsilon - \epsilon_\theta(x_t, t)\|^2$, where $x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon$ and $\epsilon \sim \mathcal{N}(0,I)$.
- **Boundary conditions**: Requires large datasets for training from scratch. $\alpha_t := 1-\beta_t$, $\bar{\alpha}_t := \prod_{i=0}^{t}(1-\beta_i)$ with variance schedule $\beta_t \in (0,1)$.
- **Related concepts**: Adversarial Noise Selection, Similarity-Guided Training, Adaptor Module, DDIM

## Similarity-Guided Training
- **Notation**: $\mathcal{L}(\psi) = \mathbb{E}_{t,x_0,\epsilon}\|\epsilon_t - \epsilon_{\theta,\psi}(x_t, t) - \hat{\sigma}_t^2 \gamma \nabla_{x_t} \log p_\phi(y=T|x_t)\|^2$, Equation (6)/(9)
- **Definition**: A modified DPM training loss that appends a similarity guidance term $\hat{\sigma}_t^2 \gamma \nabla_{x_t} \log p_\phi(y=T|x_t)$ to the noise prediction target, where $p_\phi$ is a binary classifier distinguishing source vs. target domain images at timestep $t$, and $\hat{\sigma}_t = (1-\bar{\alpha}_{t-1})\sqrt{\frac{1}{1-\bar{\alpha}_t}}$. This indirectly measures the domain gap via classifier gradients on noised images, avoiding any clean image comparison.
- **Boundary conditions**: Applicable only during fine-tuning (target domain transfer); the source-domain gradient term $\nabla_{x_t}\log p_\phi(y=S|x_t)$ is dropped because $p_\phi(y=S|x_t^T) \approx 0$ for target images. $\gamma$ is a hyperparameter (set to 5 in experiments).
- **Related concepts**: Binary Classifier, KL Divergence Domain Distance, Adversarial Noise Selection

## Adversarial Noise Selection
- **Notation**: $\epsilon^* = \arg\max_\epsilon \|\epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon, t)\|^2$, Equations (7)-(8)/(10)
- **Definition**: A min-max training strategy that finds the "worst-case" Gaussian noise (the noise the current pre-trained model most fails to denoise on target samples) via projected gradient descent (PGD). The inner maximization over $\epsilon$ is solved iteratively: $\epsilon^{j+1} = \text{Norm}(\epsilon^j + \omega \nabla_{\epsilon^j}\|\epsilon^j - \epsilon_\theta(x_t^j, t)\|^2)$, for $j=0,\ldots,J-1$, where $\text{Norm}$ normalizes to maintain $\epsilon^{j+1}_{mean}=0$, $\epsilon^{j+1}_{std}=I$. The outer minimization then trains the adaptor parameters on this worst-case noise.
- **Boundary conditions**: $\epsilon^0 \sim \mathcal{N}(0,I)$; $\omega$ is the PGD step size (set to 0.02); $J$ is number of PGD steps (set to 10). The similarity-guidance term is excluded from the inner maximization (too costly to differentiate). Minimizing worst-case noise subsumes minimizing all "easier" noise variants.
- **Related concepts**: Similarity-Guided Training, Adaptor Module, PGD

## Adaptor Module
- **Notation**: $\psi_l$, $x_t^l = \theta_l(x^{l-1}) + \psi_l(x^{l-1})$, where $\psi_l(x^{l-1}) = f(x^{l-1}W_{down})W_{up}$
- **Definition**: A lightweight parallel branch added to each layer of the pre-trained U-Net. The input is projected down via $W_{down}: \mathbb{R}^{w \times h \times r} \to \mathbb{R}^{c/c \times h/c \times d}$ (bottleneck), passed through a nonlinear activation $f(\cdot)$, then projected back up via $W_{up}$. The pre-trained U-Net parameters $\theta_l$ are frozen; only $\psi_l$ is updated. All adaptor parameters are initialized to zero so the initial output matches the frozen pre-trained model.
- **Boundary conditions**: For DDPM: $c=4$, $d=8$; for LDM: $c=2$, $d=8$. Results in 1.3% trainable parameters (DDPM-TAN) and 1.6% (LDM-TAN). Based on Houlsby et al. [10] (NLP adaptor), applied here to U-Net layers.
- **Related concepts**: Diffusion Probabilistic Model, Similarity-Guided Training, Adversarial Noise Selection

## KL Divergence Domain Distance
- **Notation**: $D_{KL}(p_{\theta_S,\phi}(x_{t-1}^S|x_t), p_{\theta_T,\phi}(x_{t-1}^T|x_t))$, Equation (5)
- **Definition**: The KL divergence between the source model $\theta_S$ and target model $\theta_T$ reverse process outputs given the same noised input $x_t$. Derived as: $\mathbb{E}_{t,x_0,\epsilon}\left[C_1 \|\nabla_{x_t}\log p_\phi(y=S|x_t) - \nabla_{x_t}\log p_\phi(y=T|x_t)\|^2\right]$ where $C_1 = \gamma/2$. This derivation uses the Gaussian form of the conditional reverse process (Eq. 4) and standard KL formula for Gaussians.
- **Boundary conditions**: Requires a joint model $\theta_{(S,T)}$ capable of generating both domains via classifier guidance. The source gradient term is discarded in practice.
- **Related concepts**: Similarity-Guided Training, Binary Classifier

## Binary Classifier
- **Notation**: $p_\phi(y|x_t)$, $y \in \{S, T\}$
- **Definition**: A pre-trained ImageNet model fine-tuned with a binary classification head to distinguish source domain (S) from target domain (T) images at noised timestep $t$. Fine-tuned on only 10 target-domain images. Used to compute the guidance gradient $\nabla_{x_t}\log p_\phi(y=T|x_t)$ directing the denoising toward the target domain.
- **Boundary conditions**: Classifier is kept fixed during the DPM fine-tuning phase; only the DPM adaptor parameters are updated. Fine-tuned on 10 target images for the few-shot setting.
- **Related concepts**: Similarity-Guided Training, KL Divergence Domain Distance

## Intra-LPIPS
- **Notation**: Intra-LPIPS $= \frac{1}{K}\sum_{k=1}^{K} \frac{1}{|C_k|^2} \sum_{i,j \in C_k} \text{LPIPS}(I_i, I_j)$
- **Definition**: A diversity metric for few-shot generation. Generate 1,000 images; assign each to the training sample with smallest LPIPS distance (forming $K$ clusters $C_k$); compute average pairwise LPIPS distance within each cluster; average across all clusters. Higher is better (more diversity within semantically similar groups).
- **Boundary conditions**: Requires LPIPS perceptual distance metric [32]. Designed for few-shot settings where standard FID may be unreliable due to insufficient reference samples. 1,000 generated images used per evaluation.
- **Related concepts**: FID

## FID (Fréchet Inception Distance)
- **Notation**: FID
- **Definition**: Standard metric for generative model quality; computes the Fréchet distance between Inception feature distributions of generated images and reference dataset images. Lower is better. For few-shot evaluation, FID requires a larger reference dataset; the paper uses Sunglasses (2,500 images) and Babies (2,700 images) reference sets, generating 10,000 images for FID evaluation.
- **Boundary conditions**: Unreliable/unstable when reference dataset is small (e.g., 10-shot). Therefore used only for larger target datasets (Sunglasses 2,500; Babies 2,700). For FID evaluation, 10,000 images are generated.
- **Related concepts**: Intra-LPIPS

## Source Domain / Target Domain
- **Notation**: $S$ (source), $T$ (target)
- **Definition**: Source domain $S$ is the large dataset used to pre-train the DPM (FFHQ or LSUN Church). Target domain $T$ is the small (10-shot) dataset the model is transferred to (e.g., Sunglasses, Babies, Landscape drawings).
- **Boundary conditions**: 10-shot setting — only 10 images from the target domain are used for fine-tuning and classifier training.
- **Related concepts**: Binary Classifier, KL Divergence Domain Distance

## DDIM (Denoising Diffusion Implicit Models)
- **Notation**: $\sigma_t = \eta\sqrt{\frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}}\sqrt{1 - \frac{\bar{\alpha}_t}{\bar{\alpha}_{t-1}}}$
- **Definition**: A deterministic (or semi-deterministic) variant of DDPM that "implicates" the reverse process, enabling much fewer inference steps. $\eta=0$ gives deterministic DDIM; $\eta=1$ gives standard DDPM; $\eta=\sqrt{(1-\bar{\alpha}_t)/(1-\bar{\alpha}_{t-1})}$ is another variant.
- **Boundary conditions**: Used for fast inference; TAN training follows standard DDPM loss but can use DDIM sampling at inference.
- **Related concepts**: Diffusion Probabilistic Model

## Latent Diffusion Model (LDM)
- **Notation**: LDM-TAN
- **Definition**: A diffusion model operating in a compressed latent space encoded by a pre-trained autoencoder, enabling high-resolution image synthesis more efficiently. In TAN, the LDM backbone and autoencoder are kept frozen; only the adaptor shift modules of the U-Net are fine-tuned.
- **Boundary conditions**: LDM adaptor uses $c=2$, $d=8$ (vs. DDPM: $c=4$, $d=8$); LDM-TAN tunes 1.6% of parameters; learning rate $1\times10^{-5}$.
- **Related concepts**: Adaptor Module, Diffusion Probabilistic Model

## PGD (Projected Gradient Descent)
- **Notation**: $\epsilon^{j+1} = \text{Norm}\left(\epsilon^j + \omega \nabla_{\epsilon^j}\|\epsilon^j - \epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon^j, t)\|^2\right)$, Equation (8)
- **Definition**: Multi-step gradient ascent with projection (normalization to maintain Gaussian statistics) used to solve the inner maximization of the min-max objective. Each step updates noise $\epsilon^j$ to increase the denoising loss, with step size $\omega$ and normalization $\text{Norm}(\cdot)$ enforcing $\epsilon^{j+1}_{mean}=0$, $\epsilon^{j+1}_{std}=I$.
- **Boundary conditions**: $J=10$ steps, $\omega=0.02$. The similarity-guidance term is excluded from the inner loop for computational tractability. Results are relatively stable for $\omega \in [0.01, 0.03]$.
- **Related concepts**: Adversarial Noise Selection
