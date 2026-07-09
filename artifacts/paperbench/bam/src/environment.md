# Environment

- **Python**: Not explicitly specified in paper (JAX ecosystem implies Python 3.7+)
- **Framework**: JAX (Bradbury et al., 2018) for automatic differentiation and JIT compilation; supports both CPU and GPU
- **Hardware**: CPU and GPU; wallclock timings reported in Figure E.1; all experiments fit in lower-dimensional regime or low-rank regime except deep generative model
- **Key dependencies**:
  - JAX (composable transformations of Python+NumPy programs)
  - PosteriorDB (Magnusson et al., 2022) for hierarchical model benchmarks: https://github.com/stan-dev/posteriordb
  - BridgeStan (Roualdes et al., 2023) for efficient access to Stan programs: https://github.com/roualdes/bridgestan
  - Stan (Carpenter et al., 2017) for model definitions
  - NumPy (implicit via JAX)
- **Random seeds**: 10 seeds for Gaussian/non-Gaussian experiments; 5 seeds for PosteriorDB experiments; not specified for deep generative
- **Code repository**: https://github.com/modichirag/GSM-VI/
- **Note on wallclock**: For D ≤ 64, all methods have similar timings. For D ≥ 128, low-rank BaM has similar timing to other methods. Gradient evaluations dominate cost in lower-dimensional settings.
