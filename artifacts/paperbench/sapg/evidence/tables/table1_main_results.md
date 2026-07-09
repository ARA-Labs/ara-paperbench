---
# Table 1: Main Performance Results After 2×10¹⁰ Samples

- **Source**: Table 1, Section 6
- **Caption**: "Performance after 2e10 samples for different methods with standard error. This is measured by successes for the AllegroKuka tasks and by episode rewards for in-hand reorientation tasks. Across environments, we find that our method performs better than baselines."
- **Experimental conditions**: N=24,576 parallel environments; M=6 policies for SAPG and DexPBT; 5 seeds per method; reported as mean ± standard error.
- **Metric**: Episode successes (AllegroKuka tasks) or episode rewards (AllegroHand, ShadowHand tasks)

| TASK | PPO [27] | PBT [24] | PQL [15] | SAPG (λ_ENT = 0) | SAPG (λ_ENT = 0.005) |
|------|----------|----------|----------|------------------|----------------------|
| ALLEGROHAND | 1.01e4 ± 6.31e2 | 7.28e3 ± 1.24e3 | 1.01e4 ± 5.28e2 | 1.23e4 ± 3.29e2 | 9.14e3 ± 8.38e2 |
| SHADOWHAND | 1.07e4 ± 4.90e2 | 1.01e4 ± 1.80e2 | 1.28e4 ± 1.25e2 | 1.17e4 ± 2.64e2 | 1.28e4 ± 2.80e2 |
| REGRASPING | 1.25 ± 1.15 | 31.9 ± 2.26 | 2.73 ± 0.02 | 35.7 ± 1.46 | 33.4 ± 2.25 |
| THROW | 16.8 ± 0.48 | 19.2 ± 1.07 | 2.62 ± 0.08 | 23.7 ± 0.74 | 18.7 ± 0.43 |
| REORIENTATION | 2.85 ± 0.05 | 23.2 ± 4.86 | 1.66 ± 0.11 | 33.2 ± 4.20 | 38.6 ± 0.63 |
| TWO ARMS REORIENTATION | 1.73 ± 0.51 | 14.46 ± 2.91 | - | - | 28.58 ± 1.55 |

**Notes**:
- "-" entries (PQL and SAPG λ=0 for Two Arms Reorientation) indicate results not reported in the paper.
- Bold in original paper indicates best-performing method per row.
- Best methods per task: AllegroHand → SAPG(λ=0); ShadowHand → SAPG(λ=0.005) tied with PQL; Regrasping → SAPG(λ=0); Throw → SAPG(λ=0); Reorientation → SAPG(λ=0.005); Two Arms → SAPG(λ=0.005).
- DexPBT directly optimizes success rate by mutating reward scales; SAPG uses a fixed reward function.
- SAPG improvement over DexPBT: Regrasping ~12%, Throw ~23%, Reorientation ~66%, Two Arms Reorientation >2×.
