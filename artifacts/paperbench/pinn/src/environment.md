---
# Environment

- **Python**: 3.10.12
- **Framework**: PyTorch 2.0.0
- **Hardware**: Single NVIDIA Titan V GPU, CUDA 11.8
- **Key dependencies**:
  - PyTorch 2.0.0 (for autograd, Hessian-vector products)
  - PyHessian (for Hessian spectral density estimation via SLQ; Yao et al. 2020)
  - NumPy (numerical operations)
  - SciPy (optional, for reference implementations)
- **Random seeds**: 5 seeds per configuration; exact seed values not specified in paper
- **Code repository**: https://github.com/pratikrathore8/opt_for_pinns
- **Evaluation grid**: Full 255×100 interior grid plus 257 IC and 101 BC points per boundary
