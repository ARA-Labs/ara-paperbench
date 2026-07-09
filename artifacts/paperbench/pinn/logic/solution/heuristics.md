---
# Heuristics and Convergence Tricks

## H01: Run Adam before L-BFGS to avoid saddle-point attraction
- **Rationale**: L-BFGS and quasi-Newton methods are attracted to saddle points (not global minima). First-order methods like Adam avoid saddle points almost surely. Running Adam first ensures L-BFGS starts from a region near a minimum rather than a saddle.
- **Sensitivity**: high
- **Bounds**: Switch after at least 1000 Adam iterations (empirically: 11k or 31k performs best); too early and Adam hasn't escaped saddles, too late and Adam wastes compute on the ill-conditioned landscape.
- **Code ref**: [src/execution/pinn_model.py]
- **Source**: Section 6.2, Section 8 (GDND theory)

## H02: Grid-search Adam learning rate from {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}
- **Rationale**: PINN loss landscapes vary significantly in curvature across PDEs; no single learning rate generalizes. The optimal lr differs by PDE and network width.
- **Sensitivity**: high
- **Bounds**: lr ∈ {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}; 5-point grid search.
- **Code ref**: [src/execution/pinn_model.py]
- **Source**: Section 2.2

## H03: L-BFGS memory size m=100
- **Rationale**: Larger memory allows better approximation of the inverse Hessian. m=100 is significantly larger than PyTorch default (m=20) and reflects the large number of curvature directions in the PINN Hessian.
- **Sensitivity**: medium
- **Bounds**: m=100 (default in paper); reducing m degrades preconditioner quality.
- **Code ref**: [src/execution/pinn_model.py]
- **Source**: Section 2.2, Appendix C

## H04: NNCG damping parameter μ tuned in [1e-5, 1e-1]
- **Rationale**: Damping (H_L + μI) ensures the Newton direction is a descent direction even when H_L has negative or near-zero eigenvalues. Too large μ → slow convergence (like GD); too small μ → unstable Newton steps.
- **Sensitivity**: high
- **Bounds**: μ ∈ {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}; empirically μ ∈ {1e-2, 1e-1} works best.
- **Code ref**: [src/execution/nncg.py]
- **Source**: Appendix E.2

## H05: NNCG preconditioner update frequency F=20
- **Rationale**: Recomputing the Nyström approximation every iteration is expensive; updating every F=20 iterations amortizes the sketch cost while maintaining good preconditioning since H_L changes slowly after Adam+L-BFGS.
- **Sensitivity**: medium
- **Bounds**: F=20; too large F → stale preconditioner; too small F → excessive sketch computation.
- **Code ref**: [src/execution/nncg.py]
- **Source**: Appendix E.2

## H06: Use 10000 residual points sampled from 255×100 grid, fixed throughout training
- **Rationale**: Sufficient coverage of the interior domain; fixed points (no re-sampling) ensures the loss function is deterministic, enabling L-BFGS and Newton methods (which require full-gradient information).
- **Sensitivity**: medium
- **Bounds**: n_res=10000 from 255×100=25500 grid; 257 IC points, 101 BC points per boundary. Sampling done once before training.
- **Code ref**: [src/execution/pinn_model.py]
- **Source**: Section 2.2
