---
# Environment

- **Python**: Not specified in paper
- **Framework**: JAX (Bradbury et al., 2018); Hydra (Yadan, 2019) for configuration management
- **Baseline library**: sbi (Tejero-Cantero et al., 2020) for NPE, NLE, NRE implementations
- **Hardware**: Not specified in paper (multiple institutions; compute support from Digital Research Alliance of Canada, UBC ARC, Amazon, Oracle mentioned in acknowledgements)
- **Key dependencies**:
  - JAX (composable transformations of Python+NumPy programs)
  - Hydra (framework for configuring complex applications)
  - sbi toolkit (simulation-based inference baselines)
  - NumPy / SciPy (for ODE solvers in simulators)
- **Random seeds**: Not specified in paper
- **Code repository**: https://github.com/mackelab/simformer
- **Notes**: VESDE is the primary SDE for all main paper experiments; VPSDE results in Appendix A3. Extended benchmark (Figure A5) includes NSPE, NLE, NRE in addition to NPE baseline.
