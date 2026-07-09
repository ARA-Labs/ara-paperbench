---
# Model Configuration

## Transformer Token Dimension
- **Value**: 50
- **Rationale**: Compact representation suitable for scalar variable tokens; balances expressiveness with memory.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix A2.1

## Number of Transformer Layers
- **Value**: 6 (benchmark tasks: Gaussian Linear, Gaussian Mixture, Two Moons, SLCP, Tree, HMM); 8 (Lotka-Volterra, SIRD, Hodgkin-Huxley)
- **Rationale**: More layers for complex physical simulators; 6 sufficient for synthetic benchmark tasks.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix A2.1

## Number of Attention Heads
- **Value**: 4
- **Rationale**: Standard multi-head attention; allows different attention patterns.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Appendix A2.1

## Attention Size (Key/Query/Value Dimension per Head)
- **Value**: 10
- **Rationale**: Per-head dimension = 10; total = 4 × 10 = 40 (projected within token dimension 50).
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix A2.1

## Feed-Forward Widening Factor
- **Value**: 3 (hidden dimension = 3 × 50 = 150)
- **Rationale**: Standard transformer FF expansion; 150-dim hidden layer per FF block.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Appendix A2.1

## Diffusion Time Embedding Dimension
- **Value**: 128-dim random Gaussian Fourier embedding
- **Rationale**: Fixed random Fourier features provide expressive encoding of continuous time t without learnable parameters.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Appendix A2.1

## Metadata Fourier Embedding Dimension (Index Set)
- **Value**: 128-dim random Gaussian Fourier embedding → learnable linear projection to token_dim
- **Rationale**: Same as diffusion time embedding; encodes time/space index for function-valued parameters.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Section 3.1, Appendix A2.1

## Identifier Embedding
- **Value**: Learnable vector embedding table; one vector per unique variable ID; dimension = token_dim = 50
- **Rationale**: Each variable (parameter or data dimension) has a unique, learnable identity vector.
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Section 3.1

## Condition State Embedding
- **Value**: Learnable vector for "observed" (True); zero vector for "unobserved" (False); dimension = token_dim = 50
- **Rationale**: Binary condition state embedded as learnable/zero to distinguish observed from latent variables.
- **Search range**: Not applicable
- **Sensitivity**: medium
- **Source**: Section 3.1

## Output Head
- **Value**: Single linear layer projecting each token (d_model=50) to 1 scalar (the score for that variable)
- **Rationale**: Each token corresponds to one variable; output is the score of that variable's dimension.
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Section 3, Figure 2

## Framework
- **Value**: JAX (Bradbury et al., 2018)
- **Rationale**: Authors' choice; XLA compilation for efficient training.
- **Source**: Software and Data section
