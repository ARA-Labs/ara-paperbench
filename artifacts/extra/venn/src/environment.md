# Environment

- **Python**: Not specified in paper
- **Framework**: Not specified in paper (CL system implementation; simulator + real CL deployment)
- **Hardware (simulation)**: Event-driven simulator; hardware not specified
- **Hardware (real testbed)**: Not specified in paper (small-scale real CL deployment)
- **Key dependencies**:
  - FedScale (Lai et al., 2021a) — device availability and hardware traces
  - AI Benchmark (Ignatov et al., 2019) — device hardware profile data
  - FEMNIST dataset (Cohen et al., 2017)
  - Standard ML frameworks for ResNet-18 and MobileNet-V2 training (not specified)
- **Random seeds**: Not specified in paper
- **Code repository**: https://github.com/SymbioticLab/Venn
- **Simulation type**: Event-driven (replays client and job traces)
