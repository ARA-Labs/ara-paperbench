---
# System Architecture

## Component Graph

```
Input (x, t) ──► MLP (tanh) ──► u(x,t;w)
                    │
                    ▼
              PINN Loss L(w)
                    │
          ┌─────────┼──────────┐
          ▼         ▼          ▼
     L_res(w)   L_ic(w)    L_bc(w)
     [diff op]  [IC]       [BC/periodic]
          └─────────┴──────────┘
                    │
              Optimizer Pipeline
                    │
          ┌─────────┼──────────┐
          ▼         ▼          ▼
        Adam   →  L-BFGS  →  NNCG
      (Phase I) (Phase II) (Phase III)
```

## Components

### MLP (Multi-Layer Perceptron)
- **Purpose**: Parameterize PDE solution u(x,t; w)
- **Inputs**: Spatial-temporal coordinates x ∈ ℝ^d (e.g., x∈(0,2π), t∈(0,1))
- **Outputs**: Scalar function value u ∈ ℝ
- **Architecture**: 3 hidden layers, widths ∈ {50, 100, 200, 400} (all equal), tanh activations
- **Initialization**: Xavier normal (W ~ N(0, 2/(fan_in+fan_out))), biases = 0
- **Interactions**: Input to PINN Loss via automatic differentiation

### PINN Loss
- **Purpose**: Measure how much u(x;w) violates PDE and BCs
- **Inputs**: Network weights w, collocation points {x_r^i}^{n_res}, boundary points {x_b^j}^{n_bc}
- **Outputs**: Scalar loss value L(w)
- **Formula**: L(w) = (1/2n_res)∑[D[u(x_r^i;w),x_r^i]]² + (1/2n_bc)∑[B[u(x_b^j;w),x_b^j]]²
- **Key design**: Points sampled once before training and fixed; n_res=10000 (from 255×100 grid), n_ic=257, n_bc=101 per side
- **Interactions**: Feeds gradients to optimizer; Hessian used for spectral analysis

### Adam Optimizer (Phase I)
- **Purpose**: Escape saddle points and reach vicinity of global minimum
- **Inputs**: Gradient ∇L(w)
- **Outputs**: Weight update
- **Key parameters**: lr ∈ {1e-5,...,1e-1} (grid searched), default β1=0.9, β2=0.999
- **Duration**: 1k, 11k, or 31k iterations (tuned)
- **Interactions**: Feeds final weights to L-BFGS phase

### L-BFGS Optimizer (Phase II)
- **Purpose**: Exploit second-order structure to improve conditioning and converge faster
- **Inputs**: Loss values and gradients; stores m=100 (s,y) pairs
- **Outputs**: Weight update via H_k∇L
- **Key parameters**: lr=1.0, memory m=100, strong Wolfe line search
- **Duration**: Remainder of 41000 total iterations after Adam phase
- **Known limitation**: Terminates early when strong Wolfe line search finds no valid step
- **Interactions**: Preconditions loss landscape; stores direction pairs for spectral analysis

### NNCG Optimizer (Phase III, optional)
- **Purpose**: Further reduce loss after L-BFGS stalls, using Nyström-preconditioned CG Newton steps
- **Inputs**: Hessian-vector products H_L(w)v, gradient ∇L(w)
- **Outputs**: Newton step d_k via NyströmPCG, then Armijo line search step size η_k
- **Key parameters**: η=1, K=2000, s=60 (sketch size), F=20 (preconditioner update freq), μ (damping, tuned), ε=1e-16, M=1000, α=0.1, β=0.5
- **Duration**: 2000 additional iterations
- **Interactions**: Takes weights from L-BFGS endpoint; uses Hessian-vector products for Newton step
