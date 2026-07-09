# Environment

- **Python**: Not specified in paper (standard for PyTorch deep learning; ~3.8+)
- **Framework**: PyTorch (version not specified in paper)
- **Key dependencies**:
  - `sbibm` — Python toolkit for SBI benchmarks, C2ST computation, and baseline results (NPE, SNPE-C, TSNPE); version not specified in paper
  - `tsnpe_neurips` — GitHub repo https://github.com/mackelab/tsnpe_neurips for TSNPE baseline
  - `scipy` — for RK45 ODE solver (`scipy.integrate.solve_ivp`)
  - `torch` — neural network training
  - `numpy` — numerical utilities
- **Hardware**: Not specified in paper
- **Random seeds**: Not specified in paper
- **Code repository**: https://github.com/jacksimons15327/snpse_icml (for reproducing paper results)
- **Pyloric simulator**: Data from Haddad & Marder (2021), Zenodo: https://zenodo.org/records/5139650; simulator from Prinz et al. (2003, 2004)
