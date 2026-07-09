# Figure 2: Data-dependent couplings vs conditioning

**Source**: Figure 2, §3 (page 3)
**Caption**: Data-dependent couplings are different than conditioning. Delineating between constructing couplings versus conditioning the velocity field, and their implications for the corresponding probability flow Xₜ. The transport problem is flowing from a Gaussian Mixture Model (GMM) with 3 modes to another GMM with 3 modes.
**Claims**: C05
**Type**: Qualitative visualization (no numerical data points)

## Description

Three side-by-side panels showing probability flow trajectories for 2D GMM→GMM transport:

### Left Panel: Data-dependent coupling ρ(x₀, x₁) = ρ₁(x₁)ρ₀(x₀|x₁)
- **Observation**: All samples follow simple, non-crossing trajectories from source to target modes.
- **Key feature**: No auxiliary modes form in the intermediate density ρₜ.
- **Transport simplicity**: Trajectories are approximately straight lines connecting paired modes.

### Center Panel: Conditional velocity bₜ(x, ξ) with ξ ∈ {0, 1, 2}
- **Observation**: The transport factorizes into three separate probability flows, one per class/mode.
- **Key feature**: Each sub-flow Xₜ^{ξ=0,1,2} is simple and non-crossing within its class.
- **Note**: This requires knowledge of the class label ξ at inference time, unlike the coupling approach.

### Right Panel: Unconditional velocity bₜ(x) with independent coupling ρ₀(x₀)ρ₁(x₁)
- **Observation**: Complex probability flow with many crossing trajectories.
- **Key feature**: Auxiliary modes form in the intermediate density ρₜ (particles pass through unintended regions).
- **Transport complexity**: Motivates using data-dependent couplings to simplify transport.

## Qualitative comparison summary

| Panel | Coupling type | Trajectory complexity | Auxiliary intermediate modes |
|-------|--------------|----------------------|------------------------------|
| Left | Data-dependent: ρ(x₀,x₁)=ρ₁(x₁)ρ₀(x₀\|x₁) | Simple, non-crossing | None |
| Center | Independent + conditional velocity bₜ(x,ξ), ξ∈{0,1,2} | Simple per class | None (factorized) |
| Right | Independent: ρ₀(x₀)ρ₁(x₁), unconditional bₜ(x) | Complex, crossing | Yes (auxiliary modes) |

Note: This figure is a 2D qualitative illustration; no numerical data points are extracted.
