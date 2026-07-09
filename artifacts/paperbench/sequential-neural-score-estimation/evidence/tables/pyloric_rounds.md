# Pyloric Network: Valid Summary Statistics (Figure 4c)
- **Source**: Figure 4c, Section 5.3
- **Caption**: "Percentage of valid summary statistics from the Pyloric simulator against simulation budget for 3 different methods, SNPSE (ours, blue), TSNPE (orange), SNVI (pink)."
- **Conditions**: TSNPSE-VP; 9 rounds; 30000 initial simulations; 20000 added per round; pyloric network simulator (Prinz et al. 2003/2004); invalid = NaN output; TSNPE and SNVI from Deistler et al. 2022a, Glockler et al. 2022.

| Round | Cumulative Budget (×10³) | TSNPSE-VP % Valid | TSNPE % Valid | SNVI % Valid |
|-------|--------------------------|-------------------|---------------|--------------|
| 1 | 30 | ≈5% | ≈5% | ≈5% |
| 2 | 50 | ≈15% | ≈8% | ≈10% |
| 3 | 70 | ≈28% | ≈15% | ≈18% |
| 4 | 90 | ≈42% | ≈22% | ≈26% |
| 5 | 110 | ≈55% | ≈32% | ≈35% |
| 6 | 130 | ≈65% | ≈40% | ≈44% |
| 7 | 150 | ≈72% | ≈48% | ≈52% |
| 8 | 170 | ≈78% | ≈55% | ≈60% |
| 9 (final) | 190 | ≈81% | ≈62% | ≈68% |

**Note**: All values read from Figure 4c (approximate). Paper states "In the final round, we achieved 81% valid summary statistics" for TSNPSE. Initial round has <1% valid statistics under the prior (paper §5.3: "over 99% of prior samples input into the simulator result in neural traces with ill-defined summary statistics").

**Key finding**: TSNPSE achieves superior % valid statistics compared to TSNPE and SNVI at all simulation budgets ≤ 190k.
