# Claims

## C01: NPSE matches or surpasses NPE on standard SBI benchmarks
- **Statement**: NPSE-VE and NPSE-VP achieve C2ST scores comparable to or lower than NPE (Papamakarios & Murray, 2016) on 8 standard sbibm benchmark tasks at simulation budgets of 1000, 10000, and 100000.
- **Status**: supported
- **Falsification criteria**: NPE achieves strictly lower C2ST than both NPSE-VE and NPSE-VP on the majority of tasks and budgets.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: C2ST, benchmark, non-sequential, NPE, NPSE

## C02: TSNPSE outperforms SNPE-C and TSNPE on high-dimensional benchmarks
- **Statement**: TSNPSE-VE and/or TSNPSE-VP achieve lower C2ST than both SNPE-C and TSNPE on the SLCP and Lotka Volterra benchmarks (the two most challenging tasks), demonstrating superior scaling to high dimensions.
- **Status**: supported
- **Falsification criteria**: SNPE-C or TSNPE achieves equal or lower C2ST than both TSNPSE variants on SLCP and Lotka Volterra at all tested budgets.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: C2ST, benchmark, sequential, TSNPSE, SNPE, TSNPE, high-dimensional

## C03: TSNPSE dominates all alternative sequential NPSE corrections
- **Statement**: TSNPSE achieves lower C2ST than SNPSE-A and SNPSE-B on tested benchmark tasks; SNPSE-C fails to produce meaningful results (C2ST ≈ 1).
- **Status**: supported
- **Falsification criteria**: SNPSE-A or SNPSE-B achieves equal or lower C2ST than TSNPSE on any tested task.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: sequential variants, SNPSE-A, SNPSE-B, SNPSE-C, ablation

## C04: TSNPSE achieves superior valid summary statistics on the Pyloric problem
- **Statement**: TSNPSE (using VP SDE, 9 rounds, 30000 initial + 20000 per round) achieves 81% valid summary statistics in the final round, higher than TSNPE and SNVI at the same simulation budget.
- **Status**: supported
- **Falsification criteria**: TSNPE or SNVI achieves ≥81% valid summary statistics at any matched simulation budget, or TSNPSE does not exceed both baselines across all budgets ≤ 200k.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: Pyloric, neuroscience, valid statistics, real-world

## C05: VE SDE is preferable for low-dimensional tasks; VP SDE for high-dimensional tasks
- **Statement**: Empirically, VE SDE yields better C2ST than VP SDE on low-dimensional benchmarks (SIR, Two Moons, Gaussian Mixture), while VP SDE performs comparably or better on high-dimensional tasks (SLCP, Lotka Volterra, Bernoulli GLM, Gaussian Linear Uniform).
- **Status**: supported
- **Falsification criteria**: Neither SDE type dominates across the dimension spectrum — performance is uncorrelated with parameter dimensionality.
- **Proof**: [E01, E02]
- **Dependencies**: C01
- **Tags**: VE SDE, VP SDE, dimensionality, ablation
