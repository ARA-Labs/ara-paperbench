---
# Related Work

## RW01: Weilbach et al., 2023
- **DOI**: ICML 2023, PMLR 202, pp. 36887–36909
- **Type**: imports
- **Delta**:
  - What changed: Simformer applies graphically structured diffusion models specifically to SBI, extending to amortized inference across arbitrary conditionals, function-valued parameters, and guided interval conditioning.
  - Why: Weilbach et al. established the foundation of using attention masks to encode graphical model structure in diffusion score models.
- **Claims affected**: C02, C03
- **Adopted elements**: Attention mask encoding of dependency structure; learnable identifier and condition-state embeddings; dynamic mask update algorithm for directed graphs.

## RW02: Papamakarios & Murray, 2016
- **DOI**: NeurIPS 2016
- **Type**: baseline
- **Delta**:
  - What changed: Simformer trains on the joint p(θ,x) rather than targeting only the posterior p(θ|x); uses diffusion instead of normalizing flows.
  - Why: NPE is the primary baseline to beat; it represents the state-of-the-art in amortized posterior estimation.
- **Claims affected**: C01, C02
- **Adopted elements**: Amortization concept; simulation-based training paradigm.

## RW03: Song et al., 2021b
- **DOI**: ICLR 2021
- **Type**: imports
- **Delta**:
  - What changed: Simformer uses the score model within a transformer for SBI, adding conditional sampling via condition masks.
  - Why: Score-based generative modeling through SDEs provides the mathematical framework for the Simformer's generative model.
- **Claims affected**: C01, C03, C05
- **Adopted elements**: VESDE and VPSDE formulations; denoising score-matching objective; reverse SDE sampling; probability flow ODE for log-probability evaluation.

## RW04: Peebles & Xie, 2022
- **DOI**: arXiv:2212.09748
- **Type**: imports
- **Delta**:
  - What changed: Simformer adapts the DiT (diffusion transformer) architecture for SBI on general variable sets rather than image patches.
  - Why: Demonstrates that transformers can serve as effective score networks in diffusion models.
- **Claims affected**: C01
- **Adopted elements**: Transformer-as-score-network architecture design.

## RW05: Simons et al., 2023
- **DOI**: Fifth Symposium on Advances in Approximate Bayesian Inference, 2023
- **Type**: extends
- **Delta**:
  - What changed: Simformer extends NPSE by replacing the conditional MLP score network with a transformer that learns all conditionals simultaneously.
  - Why: NPSE demonstrated that diffusion models improve SBI inference, but only for posterior estimation.
- **Claims affected**: C01, C06
- **Adopted elements**: Using diffusion score models for SBI; NPSE serves as a direct ablation baseline ("Simformer posterior only" ≈ NPSE up to architecture).

## RW06: Geffner et al., 2023
- **DOI**: ICML 2023, pp. 11098–11116
- **Type**: extends
- **Delta**:
  - What changed: Simformer inherits the score decomposition for i.i.d. data from Geffner et al. but generalizes to non-i.i.d. and arbitrary conditional settings.
  - Why: Score decomposition enables handling i.i.d. observations without retraining.
- **Claims affected**: C03, C04
- **Adopted elements**: Combining scores for i.i.d. inference; compositional score modeling concept.

## RW07: Lueckmann et al., 2021
- **DOI**: AISTATS 2021, pp. 343–351
- **Type**: baseline
- **Delta**:
  - What changed: Simformer evaluated on the same SBIBM benchmark suite but achieves superior performance with fewer simulations; handles full time series without summary statistics (vs. summary-based SBI in the benchmark).
  - Why: Provides standardized benchmark tasks and evaluation protocol (C2ST metric, 10 reference posteriors).
- **Claims affected**: C01, C02
- **Adopted elements**: SBIBM benchmark tasks (Linear Gaussian, Gaussian Mixture, Two Moons, SLCP); C2ST evaluation protocol.

## RW08: Webb et al., 2018
- **DOI**: NeurIPS 2018
- **Type**: imports
- **Delta**:
  - What changed: Simformer uses Webb et al.'s algorithm to dynamically update directed attention masks when conditioning changes the dependency structure.
  - Why: Directed attention masks must be augmented with additional edges to faithfully represent conditional dependencies under specific M_C configurations.
- **Claims affected**: C02
- **Adopted elements**: Algorithm for minimal edge addition to directed graph to represent conditional dependencies.

## RW09: Vaswani et al., 2017
- **DOI**: NeurIPS 2017
- **Type**: imports
- **Delta**:
  - What changed: Standard encoder-only transformer with modifications: output head is a single linear layer producing one scalar per token; diffusion time injected into each feed-forward block.
  - Why: Transformer attention mechanism enables variable-length input processing and dependency encoding via attention masks.
- **Claims affected**: C01, C04
- **Adopted elements**: Multi-head attention, feed-forward blocks, layer normalization; attention mechanism formulation attention(Q,K,V) = softmax(QK^T/√d)V.

## RW10: Bansal et al., 2023
- **DOI**: CVPR Workshop 2023, pp. 843–852
- **Type**: imports
- **Delta**:
  - What changed: Simformer applies universal guidance to SBI for interval conditioning on arbitrary constraint functions.
  - Why: Bansal et al. demonstrated diffusion models can be guided by arbitrary differentiable functions.
- **Claims affected**: C05
- **Adopted elements**: General guidance formulation; constraint score modification via sigmoid function.

## RW11: Gonçalves et al., 2020
- **DOI**: eLife 9:e56261
- **Type**: baseline
- **Delta**:
  - What changed: Simformer applied to the same Hodgkin-Huxley simulator and confirms wide/narrow marginal pattern; adds energy constraint conditioning.
  - Why: Establishes reference for HH inference and provides summary statistics implementation.
- **Claims affected**: C04, C05
- **Adopted elements**: Hodgkin-Huxley simulator setup; summary statistics definition.

## RW12: Hermans et al., 2020
- **DOI**: ICML 2020, pp. 4239–4248
- **Type**: baseline
- **Delta**:
  - What changed: Simformer does not require MCMC post-hoc; estimates posterior directly via reverse SDE.
  - Why**: NRE is included as a baseline in extended benchmark comparisons.
- **Claims affected**: C01
- **Adopted elements**: Expected coverage calibration test; C2ST evaluation methodology.

## RW13: Chen et al., 2020
- **DOI**: IEEE Trans. Network Science and Engineering 7(4), 2020
- **Type**: extends
- **Delta**:
  - What changed: Simformer handles time-varying contact rate without fixed grid discretization; evaluates at arbitrary time points.
  - Why: Chen et al. motivate time-dependent SIR parameters for COVID-19 modeling.
- **Claims affected**: C04
- **Adopted elements**: SIRD model structure; time-dependent contact rate motivation.

## RW14: Papamakarios et al., 2019
- **DOI**: AISTATS 2019, pp. 837–848
- **Type**: baseline
- **Delta**:
  - What changed: Simformer trains on joint and samples posterior; NLE trains on likelihood and requires MCMC for posterior. Simformer avoids MCMC post-hoc.
  - Why: NLE is included as an extended baseline; demonstrates trade-off between methods.
- **Claims affected**: C01
- **Adopted elements**: SLCP benchmark task definition; NLE methodology.

## RW15: Tejero-Cantero et al., 2020
- **DOI**: JOSS 5(52):2505, 2020
- **Type**: imports
- **Delta**:
  - What changed: sbi library used for NPE, NLE, NRE baseline implementations with default parameters (except neural spline flow for NPE and NLE).
  - Why: Provides standardized, reproducible baseline implementations.
- **Claims affected**: C01
- **Adopted elements**: sbi library; default training loops, Adam optimizer, early stopping; neural spline flow for NPE/NLE.
