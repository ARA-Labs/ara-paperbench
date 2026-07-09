# Concepts

## Black-Box Large Language Model (LLM)
- **Notation**: $p_{LLM}(y|x)$
- **Definition**: A language model where the user has access only to text inputs and text outputs via an API. Internal model parameters, high-dimensional intermediate representations, and output token probability distributions over the vocabulary are all inaccessible. Examples: GPT-3.5-turbo, GPT-4, PaLM-2, Gemini.
- **Boundary conditions**: Applies when neither model weights nor logprobs can be queried. Distinct from grey-box (token probs available) and white-box (full parameter access). Post-October 2023 OpenAI API removes even the `echo` probabilities feature.
- **Related concepts**: Grey-Box LLM Adaptation, Energy-Based Model Adapter

## Energy-Based Model (EBM) Adapter
- **Notation**: $g_\theta(x, y) \in \mathbb{R}$; $p_\theta(y|x) = \frac{p_{LLM}(y|x)\exp(g_\theta(x,y))}{Z_\theta(x)}$
- **Definition**: A small trainable language model (0.1B–0.3B parameters, e.g., DeBERTa-v3) that outputs a scalar energy score for an input–output pair $(x, y)$. The adapted model distribution is the product of the black-box LLM's distribution and the exponentiated adapter score, normalized by the intractable partition function $Z_\theta(x) = \int p_{LLM}(y|x)\exp(g_\theta(x,y))dy$.
- **Boundary conditions**: Requires only text input/output pairs; does not access LLM internals. Trained with NCE to avoid computing $Z_\theta$. Spectral normalization is applied to prevent sharp gradients.
- **Related concepts**: Ranking-Based NCE Loss, Spectral Normalization, Online Adaptation

## Ranking-Based NCE Loss
- **Notation**: $\ell(\theta) = -\mathbb{E}_{p_{data}(x)}\left[g_\theta(x) - \log\sum_{k}\exp(g_\theta(x_k))\right]$
- **Definition**: A Noise Contrastive Estimation objective that avoids computing the intractable partition function. It treats the positive sample (target-domain data $y^+$) as the "real" sample and negative samples (source-domain/LLM-generated text $y^-$) as "noise," training the adapter to rank $y^+$ above $y^-$. The gradient is: $\nabla_\theta\ell(\theta) = \nabla_\theta\{-\mathbb{E}_{y^+\sim p_{data}}[g_\theta(x,y^+)] + \alpha\mathbb{E}[g_\theta(x,y^+)^2] + \mathbb{E}_{y^-\sim p_\theta}[g_\theta(x,y^-)] + \alpha\mathbb{E}[g_\theta(x,y^-)^2]\}$ where $\alpha$ is the spectral normalization regularization weight.
- **Boundary conditions**: Requires at least one positive and one negative sample per training step. Reduces to standard NCE when only binary real/noise distinction is used. Extended to ranking by minimizing KL divergence between the parameterized posterior and the data-to-noise ratio.
- **Related concepts**: Energy-Based Model Adapter, Spectral Normalization, Online Adaptation

## Spectral Normalization
- **Notation**: $\text{SN}(W) = W / \sigma(W)$ where $\sigma(W)$ is the spectral norm (largest singular value)
- **Definition**: A weight normalization technique applied to the energy model $g_\theta$ to control the Lipschitz constant of the network, preventing sharp gradients during EBM training. The gradient of the regularized loss includes terms $+\alpha\mathbb{E}[g_\theta(x,y^+)^2]$ and $+\alpha\mathbb{E}[g_\theta(x,y^-)^2]$ which enforce smoothness.
- **Boundary conditions**: Necessary for training stability of energy-based models. Applied per (Du & Mordatch, 2019). Without it, energy values may diverge.
- **Related concepts**: Ranking-Based NCE Loss, Energy-Based Model Adapter

## Online Adaptation Framework (Algorithm 1)
- **Notation**: $\{\theta_t\}_{t=0}^{T}$; $y^{(t)}_{i+} = \text{SEL}(y^{(t-1)}_{i+}, \{\hat{y}_{i,m}\}_{m=1}^M)$; $y^{(t)}_{i-} = \{\hat{y}_{i,m} | \hat{y}_{i,m} \neq y^{(t)}_{i+}\}$
- **Definition**: An iterative training procedure with $T$ rounds. At each iteration $t$: (1) sample $M$ candidates from the current adapted distribution $p_{\theta_t}(y|x_i)$; (2) update the positive set by selecting the best candidate (via ground-truth, human, or AI feedback); (3) use remaining candidates as negatives; (4) compute NCE loss gradient and update adapter parameters via SGD: $\theta_{t+1} = \theta_t - \eta\nabla_\theta\ell(\theta_t)$.
- **Boundary conditions**: Requires an accessible feedback signal (ground-truth labels, human preference, or an advanced AI judge). Performance degrades if $T=0$ (untuned adapter misguides beam search). Improvement saturates around $T=3$–$4$ iterations.
- **Related concepts**: Energy-Based Model Adapter, Ranking-Based NCE Loss, Adapted Inference (Beam Search)

## Adapted Inference (Sentence-Level Beam Search)
- **Notation**: $y = [s_1, s_2, \ldots, s_L]$; $p_\theta(y|x) = \exp(g_\theta(s_{1:L},x))\prod_l p_{LLM}(s_l|x,s_{1:l-1})$
- **Definition**: An inference procedure that decomposes the full generation $y$ into sentence-level steps $s_1,\ldots,s_L$. The black-box LLM generates $n$ candidate sentences at each step for each beam (producing $nk$ candidates), and the adapter scores each partial chain $s_{1:l}$ to retain the top-$k$ beams. Default beam size $k=3$; each beam generates multiple candidates per step.
- **Boundary conditions**: Requires multiple API calls to the black-box LLM (beam\_size × candidates per step × steps). The "single-step" variant collapses $L=1$, generating complete answers in one shot and reranking. Increases API cost compared to direct CoT inference.
- **Related concepts**: Energy-Based Model Adapter, Online Adaptation Framework

## Grey-Box LLM Adaptation
- **Notation**: Methods requiring $p_{LLM}(y_t|x,y_{<t})$ (token-level output probabilities)
- **Definition**: Adaptation methods that assume access to output token probabilities but not model parameters. Examples: LMaaS (Sun et al., 2022), kNN-Adapter (Huang et al., 2023), CombLM (Ormazabal et al., 2023), Proxy-Tuning (Liu et al., 2024), IPA (Lu et al., 2023). These methods are inapplicable to post-GPT-3 black-box APIs.
- **Boundary conditions**: Applicable only to models that expose logprobs (e.g., pre-GPT-3, LLaMA-2). Distinct from black-box adaptation (no probabilities) and white-box (full parameter access).
- **Related concepts**: Black-Box Large Language Model, Energy-Based Model Adapter

## Positive and Negative Samples
- **Notation**: $y^+ \sim p_{data}(y|x)$ (positive); $y^- \sim p_\theta(y|x)$ (negative)
- **Definition**: In BBOX-ADAPTER training, positive samples are target-domain outputs (from ground-truth solutions, human preference, or AI feedback via GPT-4). Negative samples are outputs generated by the current adapted model. The key distinction from standard supervised learning is that negatives are dynamically sampled from the adapter's own distribution at each iteration, enabling self-improvement.
- **Boundary conditions**: Initial positives are selected from K initial LLM samples using SEL(·) (best-of-K). Initial negatives are from a randomly-initialized adapter. At iteration $t$, previous positive is compared against new samples and updated via SEL(·).
- **Related concepts**: Online Adaptation Framework, Ranking-Based NCE Loss

## Plug-and-Play Adaptation
- **Notation**: Adapter $g_{\theta^*}$ trained on model $A$ applied to model $B$
- **Definition**: The property that a BBOX-ADAPTER trained to adapt one black-box LLM (e.g., gpt-3.5-turbo) can be directly applied as a scorer/reranker for a different black-box LLM (e.g., davinci-002, Mixtral-8×7B) without any retraining. This is enabled by the adapter's independence from internal LLM parameters—it operates purely on generated text.
- **Boundary conditions**: Requires that the adapted LLM produces text in a similar format/language as the original. Performance gains may be smaller when the target LLM distribution differs substantially from the source.
- **Related concepts**: Adapted Inference (Beam Search), Energy-Based Model Adapter

## Parameter-Efficient Fine-Tuning (PEFT)
- **Notation**: LoRA: $W + \Delta W = W + BA$ where $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, $r \ll \min(d,k)$
- **Definition**: Fine-tuning approaches that update only a small subset of model parameters rather than the full model. Examples: LoRA (Hu et al., 2021), adapters (Houlsby et al., 2019), prefix-tuning. For the LoRA baseline used in experiments, rank $r=128$ (for 0.1B comparison) or $r=384$ (for 0.3B comparison), with $\alpha=2r$.
- **Boundary conditions**: Requires access to internal model parameters and backward passes—inapplicable to black-box LLMs. Used as a white-box upper-bound baseline (SFT-LoRA with Mixtral-8×7B).
- **Related concepts**: Grey-Box LLM Adaptation, Energy-Based Model Adapter
