# Environment

- **Python**: Not specified in paper or code
- **Framework**: PyTorch (version not specified); Lightning Fabric for parallelism
- **ODE Solver**: torchdiffeq (Chen, 2018) — Dopri solver
- **Hardware**: Not specified in paper (multi-GPU assumed given Lightning Fabric use)
- **Key dependencies**:
  - `torch` (PyTorch) — core deep learning framework
  - `lightning` / `lightning-fabric` — multi-GPU parallelism
  - `torchdiffeq` — Dopri ODE solver (Chen, 2018; https://github.com/rtqichen/torchdiffeq)
  - `denoising-diffusion-pytorch` (luciddrains) — U-Net architecture implementation
  - ImageNet dataset (ILSVRC 2012) — training and validation sets
- **Random seeds**: Not specified in paper or code
- **Repository**: https://github.com/interpolants/couplings (code to be uploaded at ICML 2024 conference)
