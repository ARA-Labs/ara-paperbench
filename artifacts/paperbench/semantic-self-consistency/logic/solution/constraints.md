---
# Constraints and Limitations

## Boundary Conditions

### BC1: Minimum sample size k
- **Constraint**: k ≥ 7–10 responses required for stable performance.
- **Consequence**: Below k ≈ 7, performance gains diminish and can produce completely random results (Appendix I.1).
- **Mitigation**: Always use k=10 as the default; expect diminishing returns at k < 7.

### BC2: Featurizer domain alignment
- **Constraint**: The featurizer must be aligned to the reasoning task domain.
- **Consequence**: Misaligned featurizers (e.g., using RoBERTa on math tasks) reduce embedding cluster density and degrade weighting quality.
- **Mitigation**: Use SciBERT for mathematical reasoning; RoBERTa for commonsense. Test multiple featurizers per task.

### BC3: Sequence length range
- **Constraint**: Both very short and very long sequences degrade performance.
- **Consequence**: Short sequences lack semantic discriminability; very long sequences increase noise.
- **Mitigation**: Use adequate max-new-tokens per dataset (SVAMP=250, AQuA-RAT=400, StrategyQA=450).

### BC4: Reasoning task type
- **Constraint**: SCW performs well on both arithmetic and commonsense tasks; CPW performs well only on arithmetic.
- **Consequence**: CPW decreases average accuracy on StrategyQA by −1.63%.
- **Mitigation**: Prefer SCW as the default method; use CPW only on arithmetic/algebraic datasets.

### BC5: Closed-answer task requirement
- **Constraint**: All methods require parsable final answers (the answer must follow "The answer is").
- **Consequence**: Open-ended generation tasks cannot be directly evaluated with majority voting.
- **Mitigation**: Ensure structured prompts elicit fixed-format answers; apply custom parsing for edge cases.

### BC6: Overly similar generations
- **Constraint**: If all k responses are near-identical (e.g., low temperature, instruction-tuned models), embedding-based methods cannot discriminate.
- **Consequence**: All methods reduce to approximately standard majority vote.
- **Mitigation**: Use temperature=0.8 for sufficient diversity; consider varied-temperature sampling (Appendix G.1).

## Known Limitations

1. **Subtle numerical variations**: Small changes in mathematical reasoning (e.g., one sign flip) produce very similar embedding vectors, making it hard to detect incorrect arithmetic within otherwise correct reasoning.
2. **Abstract reasoning/symbolic logic**: Embedding vectors may overlook subtle logical variations, reducing effectiveness on tasks requiring precise symbolic distinctions.
3. **English-only featurizers**: BERT-based models are trained on English; multilingual tasks are out of scope.
4. **No content moderation**: Mistral 7B, Llama 2 7B, and Llama 3 8B lack built-in content moderation.
5. **Hyperparameter sensitivity**: Outlier detection configurations vary in effectiveness; recommend grid search per deployment context.
6. **Additional compute overhead**: SCW adds O(k²·d) pairwise cosine computations; acceptable on modern GPUs but non-zero.
