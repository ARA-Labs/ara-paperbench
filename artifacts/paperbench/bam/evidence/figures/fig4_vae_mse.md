# Figure 5.4: VAE Image Reconstruction — MSE vs. Gradient Evaluations

**Source**: Figure 5.4 (§5.3), Figure E.7 (Appendix E.6, wallclock time)  
**Claims**: C06  
**Description**: Image reconstruction MSE vs. number of gradient evaluations for BaM, ADVI, GSM (batch sizes B=10, 100, 300), and AVI (single point, from encoder). Stars mark best outcome within 3000 gradient evaluations. Beige star = ADVI; purple star = BaM.

## Setup

- **Model**: VAE with 5-layer conv encoder+decoder; latent D=256; images in R^3072
- **Dataset**: CIFAR-10 test split (one sampled image x')
- **Posterior target**: p(z'|x') = N(0,I) × N(x'; Ω(z',θ̂), 0.1·I)
- **Metric**: MSE = ||x' - Ω(μ_t, θ̂)||²/3072

## Key Quantitative Observations from Paper (§5.3)

- **BaM at B=10**: Performs poorly — MSE greater than 0.2 (paper: "BaM performs poorly when the batch size is very small (B=10) relative to the dimension of the latent variable z'").
- **BaM at B=100 and B=300**: BaM becomes competitive — MSE less than 0.05.
- **BaM at B=300 vs ADVI and GSM**: BaM converges an order of magnitude (or more) faster than ADVI and GSM (in gradient evaluations).
- **Budget of 3000 gradient evaluations**:
  - ADVI: lowest MSE at B=10, T=300 (most evaluations sequential)
  - BaM: comparable result at B=300, T=10 (evaluations largely parallelizable)
- **AVI comparison**: Both BaM and ADVI eventually achieve lower MSE than AVI encoder (uses factorized Gaussian).
- **Wallclock time** (Figure E.7): BaM at B=300 converges fastest in wallclock time.

## Learning Rates Used (Appendix E.6)

| Method | Batch Size | Learning Rate |
|--------|------------|---------------|
| BaM | B=10 | λ=0.1 (grid: {0.01, 0.1, 0.2, 10}) |
| BaM | B=100 | λ=50 (grid: {2, 20, 50, 100, 200}) |
| BaM | B=300 | λ=7500 (grid: {1000, 5000, 7500, 10000}) |
| ADVI | B=10,100,300 | lr=0.02 (grid: {0.001, 0.01, 0.02, 0.05}) |
| GSM | all | N/A (no tuning needed) |
