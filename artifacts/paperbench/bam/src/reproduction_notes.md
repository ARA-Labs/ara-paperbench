# Reproduction Notes

Common pitfalls and critical details for reproducing the experiments in this paper.

## General

1. **Seeds**: Gaussian and non-Gaussian experiments use **10 seeds**. PosteriorDB uses **5 seeds**. Deep generative uses a single test image. Do not confuse these — using fewer seeds than specified will fail the reproduction criteria.

2. **All baselines must be run for every experiment**: Each experiment requires running ALL specified baselines (BaM, ADVI, GSM) under the SAME conditions. Do not skip ADVI or GSM for any experiment — the comparisons are central to the paper's claims. In particular:
   - PosteriorDB (E03) requires BaM, ADVI, AND GSM for all three models (arK, gp-pois-regr, eight-schools)
   - Non-Gaussian (E02) requires ALL methods for BOTH configurations: (a) varying skew s ∈ {0.2, 1.0, 1.8} with τ=1, AND (b) varying tails τ ∈ {0.1, 0.9, 1.7} with s=0

3. **Non-Gaussian has TWO experiment configurations**: The sinh-arcsinh experiment (E02) has two independent panels:
   - Panel 1: Fix τ=1, vary s ∈ {0.2, 1.0, 1.8} — tests skew sensitivity
   - Panel 2: Fix s=0, vary τ ∈ {0.1, 0.9, 1.7} — tests tail sensitivity
   Both panels must be reproduced. Missing either one is incomplete.

4. **KL divergence should be measured frequently**: Compute forward and reverse KL at regular intervals (ideally every iteration, or at minimum every 10-50 iterations) to generate meaningful convergence curves.

## PosteriorDB (E03) Specifics

5. **Use PosteriorDB Python package + BridgeStan**: The cleanest approach is to install the `posteriordb` Python package and use `BridgeStan` for computing score functions from Stan models. This avoids manual reimplementation of the log-posterior. Install: `pip install posteriordb bridgestan`.

6. **Three models required**: arK (D=7), gp-pois-regr (D=13), eight-schools (D=10). All three must be run with both B=8 and B=32.

7. **Reference samples**: Use HMC reference samples from PosteriorDB to compute relative mean and SD errors.

## Deep Generative (E04) Specifics

8. **VAE architecture**: 5-layer convolutional encoder/decoder, D=256 latent dimensions, Gaussian likelihood with σ²=0.1. Train for 100 epochs on CIFAR-10 training split before running VI.

9. **BaM batch size matters critically**: B=10 should perform poorly (MSE stays high), B=100 is borderline, B=300 ≈ D converges fast. This is the key result — showing BaM needs B comparable to D.

10. **GSM implementation**: GSM (Algorithm 3 in paper) computes per-sample rank-1 updates. The key step is solving a quadratic equation for ρ_b, then averaging the per-sample covariance updates. Make sure the final averaging step is correct.
