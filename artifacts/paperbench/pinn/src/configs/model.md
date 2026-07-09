---
# Model Configuration

## Architecture
- **Value**: Multi-Layer Perceptron (MLP), 3 hidden layers
- **Rationale**: Standard PINN architecture; tanh activations enable smooth derivatives needed for PDE residual computation via automatic differentiation.
- **Search range**: Number of layers not varied; widths varied
- **Sensitivity**: medium
- **Source**: Section 2.2

## Hidden Layer Width
- **Value**: Tested widths ∈ {50, 100, 200, 400} (all hidden layers equal width)
- **Rationale**: Increasing width generally improves expressive power; study examines performance across sizes.
- **Search range**: {50, 100, 200, 400}
- **Sensitivity**: medium
- **Source**: Section 2.2

## Activation Function
- **Value**: tanh (hyperbolic tangent)
- **Rationale**: Smooth, differentiable, and enables computation of higher-order derivatives for PDE residual terms.
- **Search range**: Not varied
- **Sensitivity**: medium (smooth activations preferred for PINNs)
- **Source**: Section 2.2

## Weight Initialization
- **Value**: Xavier normal: W ~ N(0, 2/(fan_in + fan_out)) where fan_in and fan_out are input and output units
- **Rationale**: Maintains variance across layers; standard initialization for tanh networks.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 2.2; Glorot & Bengio 2010

## Bias Initialization
- **Value**: 0 (all biases initialized to zero)
- **Rationale**: Standard practice; ensures symmetric initialization.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 2.2

## Input Dimension
- **Value**: 2 (x, t) for all studied PDEs (1D spatial + 1D temporal)
- **Rationale**: All three benchmark PDEs are 1D+time.
- **Search range**: Not varied
- **Sensitivity**: N/A (problem-defined)
- **Source**: Appendix A.1-A.3

## Output Dimension
- **Value**: 1 (scalar u(x,t))
- **Rationale**: All studied PDEs have scalar solutions.
- **Search range**: Not varied
- **Sensitivity**: N/A (problem-defined)
- **Source**: Appendix A.1-A.3

## Total Parameters (approximate)
- **Value**: Width 50: ~7650; Width 100: ~30300; Width 200: ~120800; Width 400: ~483200 (for 2-input, 3 hidden layers, 1 output)
- **Rationale**: Paper requires p ≥ n_res + n_bc for interpolation assumption in theory.
- **Search range**: Determined by width choice
- **Sensitivity**: low (accuracy improves with width up to a point)
- **Source**: Section 2.1 (interpolation discussion)
