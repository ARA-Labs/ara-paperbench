# CodeGen HumanEval Results — Temperature = 0.2

- **Source**: Table 2, Section 3.3.2
- **Caption**: "CodeGen results with temperature=0.2. CFG in nearly all cases increases performance, but the optimal γ value varies."
- **Conditions**: HumanEval benchmark (164 Python tasks); pass@k metric; sampling temperature = 0.2; CFG strengths γ ∈ {1.0, 1.1, 1.25, 1.5, 1.75, 2.0}

| γ | CodeGen-350M k=1 | CodeGen-350M k=10 | CodeGen-350M k=100 | CodeGen-2B k=1 | CodeGen-2B k=10 | CodeGen-2B k=100 | CodeGen-6B k=1 | CodeGen-6B k=10 | CodeGen-6B k=100 |
|---|-----------------|------------------|--------------------|----------------|-----------------|------------------|----------------|-----------------|------------------|
| 1.0 | 11.0% | 17.0% | 22.0% | 19.5% | 25.5% | 29.8% | 19.5% | 25.5% | 29.8% |
| 1.1 | 11.8% | 18.1% | 20.1% | 20.4% | 25.4% | 28.0% | 20.4% | 25.4% | 28.0% |
| 1.25 | 11.4% | 17.3% | 18.9% | 19.7% | 25.4% | 28.0% | 19.7% | 25.4% | 28.0% |
| 1.5 | 10.9% | 16.7% | 18.3% | 20.9% | 26.7% | 29.2% | 20.9% | 26.7% | 29.2% |
| 1.75 | 10.3% | 16.0% | 18.2% | 20.4% | 26.2% | 28.6% | 20.4% | 26.2% | 28.6% |
| 2.0 | 8.6% | 14.6% | 17.6% | 16.5% | 22.4% | 24.4% | 16.5% | 22.4% | 24.4% |

## Notes
- CodeGen-16B-mono omitted due to compute constraints (Footnote 1)
- pass@k definition per Chen et al. (2021): k samples per problem, solved if any passes unit tests
- Note: CodeGen-2B and CodeGen-6B results at some γ values are identical in the paper (apparent duplicate data in Tables 6 and 7)
