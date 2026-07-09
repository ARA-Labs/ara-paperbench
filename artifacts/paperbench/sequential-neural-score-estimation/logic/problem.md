# Problem Specification

## Observations

### O1: Simulator-based models have intractable likelihoods
- **Statement**: Many scientific models generate synthetic data via stochastic simulators, making the likelihood p(x|θ) analytically unavailable or computationally intractable to evaluate.
- **Evidence**: Acknowledged across neuroscience (Gonçalves et al., 2020), evolutionary biology (Beaumont et al., 2002), ecology (Wood, 2010), epidemiology (Corander et al., 2017), climate science (Holden et al., 2018), cosmology, high-energy physics, and econometrics.
- **Implication**: Standard likelihood-based Bayesian methods (MCMC, VI) cannot be applied directly.

### O2: Normalizing-flow-based SBI methods impose architectural constraints
- **Statement**: Existing state-of-the-art SBI methods (SNPE, SNLE) rely on normalizing flows, which require invertible architectures and thus restrict model design.
- **Evidence**: Section 1, comparison to SNPE (Greenberg et al., 2019), SNLE (Papamakarios et al., 2019).
- **Implication**: Architectural inflexibility may limit expressiveness, especially in high-dimensional parameter spaces.

### O3: Score-based diffusion models achieve state-of-the-art generative quality
- **Statement**: Score-based generative models (Song et al., 2021; Ho et al., 2020) achieve high-quality sample generation without adversarial training and with greater architectural flexibility than normalizing flows.
- **Evidence**: Cited state-of-the-art results in image, audio, and video generation.
- **Implication**: Score-based methods are a natural alternative backbone for SBI.

### O4: Naive amortised inference wastes simulation budget for a specific observation
- **Statement**: When only a single observation x_obs is of interest, training an amortised posterior estimator over all of R^p wastes simulations on regions far from p(x|x_obs).
- **Evidence**: Section 3, motivation for sequential training.
- **Implication**: A sequential approach that concentrates simulations near x_obs can reduce the total simulation budget required for accurate inference.

### O5: Alternative sequential corrections suffer from variance or approximation errors
- **Statement**: SNPE-A uses post-hoc SIR (high variance), SNPE-B uses importance-weighted loss (high-variance gradients), and SNPE-C requires complex reparameterisation; empirically TSNPE outperforms these.
- **Evidence**: Section 3.2, Appendix C, Figure 6.
- **Implication**: A truncated-proposal approach that avoids explicit correction is preferable.

## Gaps

### G1: No principled score-based approach for SBI existed
- **Statement**: The use of conditional score-based diffusion models for simulation-based inference had not been systematically studied prior to this work.
- **Caused by**: O1, O3
- **Existing attempts**: Batzolis et al. (2021) applied conditional diffusion for image generation; Geffner et al. (2023) studied multiple-observation SBI in parallel.
- **Why they fail**: These works either address different settings (known likelihood) or lack sequential variants that reduce simulation cost.

### G2: Sequential SBI methods require correction mechanisms that degrade performance
- **Statement**: Sequential variants of flow-based SBI require either post-hoc importance weighting (SNPE-A), weighted loss (SNPE-B), or complex score decompositions (SNPE-C), all of which introduce approximation errors or variance.
- **Caused by**: O4, O5
- **Existing attempts**: SNPE-A/B/C (Papamakarios & Murray, 2016; Lueckmann et al., 2017; Greenberg et al., 2019), TSNPE (Deistler et al., 2022a).
- **Why they fail**: Importance weights are high-variance; the SNPE-C correction assumes known proposal structure; only TSNPE avoids correction but is restricted to normalizing flows.

### G3: Score-based SBI lacks sequential efficiency
- **Statement**: NPSE in its amortised form does not guide simulations toward x_obs, requiring large simulation budgets for accurate inference at a specific observation.
- **Caused by**: O4
- **Existing attempts**: None prior to this work for diffusion-based SBI.
- **Why they fail**: No sequential mechanism existed for score-based SBI.

## Key Insight

- **Insight**: The denoising posterior score matching (DSM) objective is minimised by the true posterior score even when the training distribution uses a proposal prior `˜p(θ)` that is proportional to the true prior `p(θ)` within the support of the posterior. Therefore, truncated priors as proposals require no correction.
- **Derived from**: O4, O5, and Proposition 3.1 (Appendix C.1).
- **Enables**: TSNPSE — a sequential algorithm that concentrates simulations near x_obs via truncated proposals without any importance weight correction, combining simulation efficiency with theoretical correctness.

## Assumptions

- A1: The simulator is a well-defined stochastic function mapping parameters θ to data x.
- A2: The forward SDE admits a unique stationary distribution π (e.g., standard Gaussian) from which it is easy to sample.
- A3: The truncated region does not exclude any mass from the true posterior: Θ_obs ⊆ HPR_ε(p^s_ψ(θ|x_obs)) for all rounds s ≥ 1.
- A4: An L2 bound on the score approximation error holds (Assumption A1 / A1' in Appendix A.2).
- A5: The prior p(θ) is known in closed form or can be sampled.
