---
# Key Concepts

## Forward-Optimization Adaptation (FOA)
- **Notation**: FOA
- **Definition**: A test-time adaptation paradigm that adapts a model to OOD test data using only forward passes, combining CMA-ES-based prompt learning with back-to-source activation shifting. No backpropagation, no weight modification.
- **Boundary conditions**: Applicable to any model architecture that supports input prompt insertion; full benefit requires batch size ≥ 2 (for statistics); single-sample variant FOA-I uses interval buffering.
- **Related concepts**: CMA Evolution Strategy, Prompt Embedding, Back-to-Source Activation Shifting, Fitness Function

## CMA Evolution Strategy (CMA-ES)
- **Notation**: CMA-ES; sampling distribution: p(t)_k ~ m(t) + τ(t) N(0, Σ(t))
- **Definition**: A derivative-free black-box optimizer that maintains a multivariate normal distribution over the solution space. At each iteration t, it samples K candidate solutions (population), evaluates a fitness function for each, then updates the mean m(t), step size τ(t), and covariance matrix Σ(t) by maximizing the likelihood of successful candidates.
- **Boundary conditions**: Becomes intractable for very high-dimensional problems (e.g., full model weights); effective for low-dimensional prompt optimization (Np×d ~ 3×768 = 2,304 dimensions for ViT-Base).
- **Related concepts**: Forward-Optimization Adaptation, Prompt Embedding, Fitness Function, Population Size K

## Prompt Embedding
- **Notation**: p ∈ R^{d × Np}; inserted before the first transformer layer as [p; X_embeddings]
- **Definition**: Np learnable continuous vectors of dimension d (same as patch embedding dimension) prepended to the test batch's patch embeddings as additional model input tokens. Only the prompt is optimized; all model parameters remain frozen.
- **Boundary conditions**: Np=3 by default (low sensitivity to Np ∈ {1,...,10}); initialized with uniform distribution; effective for transformer architectures (ViT, VisionMamba); less effective for CNNs due to locality of convolutions.
- **Related concepts**: Forward-Optimization Adaptation, CMA Evolution Strategy, ViT CLS Token

## Fitness Function
- **Notation**: L(f_Θ(p; X_t)) = Σ_{x∈X_t} Σ_{c∈C} −ŷ_c log ŷ_c + λ Σ_{i=1}^{N} [||μ_i(X_t) − μ^S_i||_2 + ||σ_i(X_t) − σ^S_i||_2]
- **Definition**: The unsupervised objective used to score CMA candidate prompts. Combines prediction entropy (first term) with activation distribution discrepancy (second term) across all N transformer layers' CLS tokens. Lower fitness is better. λ balances the two terms.
- **Boundary conditions**: λ=0.4×BS/64 on ImageNet-C/V2/Sketch; λ=0.2×BS/64 on ImageNet-R; entropy alone leads to degenerate solutions; discrepancy alone already effective (63.4% accuracy); full combination is best (66.3%).
- **Related concepts**: CMA Evolution Strategy, Source In-Distribution Statistics, Prediction Entropy, Activation Discrepancy

## Back-to-Source Activation Shifting
- **Notation**: ê^0_N ← e^0_N + γ·d_t; d_t = μ^S_N − μ_N(t); μ_N(t) = α·μ_N(X_t) + (1−α)·μ_N(t−1)
- **Definition**: A forward-only mechanism that directly modifies the N-th (final) transformer layer's CLS token feature e^0_N by adding a direction vector d_t scaled by step size γ. The direction points from the estimated OOD test center toward the source domain center, updated online via exponential moving average.
- **Boundary conditions**: γ=1.0 (exact center alignment); α=0.1 (EMA factor); requires source statistics μ^S_N precomputed; initialization μ_N(0) = μ_N(X_1); works even at BS=1 with EMA, unlike batch-statistics-only variant.
- **Related concepts**: Source In-Distribution Statistics, ViT CLS Token, Exponential Moving Average

## Source In-Distribution Statistics
- **Notation**: {μ^S_i, σ^S_i}_{i=0}^{N}; computed over D_S = {x_q}_{q=1}^{Q}
- **Definition**: Mean and standard deviation of CLS token features {e^0_i}_{i=1}^{N} computed once before TTA over Q unlabeled source in-distribution samples. Used in both the fitness function (all layers) and activation shifting (final layer only).
- **Boundary conditions**: Q ≥ 32 samples sufficient for stable statistics on ImageNet; computed from ImageNet-1K validation set in experiments; computed without prompt insertion; one-time computation, not updated during TTA.
- **Related concepts**: Fitness Function, Back-to-Source Activation Shifting, CLS Token

## ViT CLS Token
- **Notation**: e^0_i ∈ R^d; classification token at layer i; output: ŷ = Head(e^0_N)
- **Definition**: A learnable [CLS] classification token prepended to patch embeddings. At each transformer layer i, e^0_i is updated alongside patch embeddings E_i = L_i(E_{i-1}). The final CLS token e^0_N is passed to the MLP head for classification.
- **Boundary conditions**: Specific to transformer architectures; acts as global representation aggregated from all patches; FOA uses CLS token statistics at all N layers for fitness and at layer N for shifting.
- **Related concepts**: Prompt Embedding, Back-to-Source Activation Shifting, Source In-Distribution Statistics

## Population Size K
- **Notation**: K = 4 + 3 × log(prompt_dim) ≈ 28 for default Np=3 ViT-Base configuration
- **Definition**: The number of candidate prompt solutions sampled per CMA iteration (per test batch). Each of the K prompts is evaluated separately via a forward pass, generating K fitness values used to update the CMA distribution.
- **Boundary conditions**: Default K=28; performance converges for K > 15; at K=2, FOA already outperforms NoAdapt and T3A; at K=6, FOA surpasses TENT; K is a performance-efficiency trade-off parameter.
- **Related concepts**: CMA Evolution Strategy, Forward-Optimization Adaptation

## Expected Calibration Error (ECE)
- **Notation**: ECE (%, ↓)
- **Definition**: Measures the difference between predicted confidence probabilities and empirical accuracy across probability bins. Lower ECE indicates better calibrated probability estimates.
- **Boundary conditions**: Evaluated alongside classification accuracy on all benchmarks; FOA achieves notably lower ECE (3.2%) than gradient-based methods (TENT: 18.5%, SAR: 7.0%) due to the activation discrepancy regularization reducing error accumulation.
- **Related concepts**: Fitness Function, Prediction Entropy

## Quantization (Post-Training Quantization)
- **Notation**: 8-bit ViT, 6-bit ViT; produced via PTQ4ViT
- **Definition**: Reducing the numerical precision of model weights and activations from 32-bit floating point to 8-bit or 6-bit integers. Non-differentiable discrete quantizers cause vanishing gradients, making backpropagation infeasible. Memory scales as 0.25× of 32-bit for 8-bit models.
- **Boundary conditions**: FOA is the only optimization-based TTA method compatible with quantized models; gradient-based methods (TENT, CoTTA, SAR) are inapplicable; T3A is applicable but shows substantially weaker performance.
- **Related concepts**: Forward-Optimization Adaptation, Back-to-Source Activation Shifting
