# Pyloric Network: Valid Summary Statistics vs Simulation Budget (Figure 4c)
- **Source**: Figure 4c, Section 5.3
- **Caption**: "Percentage of valid summary statistics from the Pyloric simulator against simulation budget for 3 different methods, SNPSE (ours, blue), TSNPE (orange), SNVI (pink)."
- **Experimental conditions**: R=9 rounds; TSNPSE starts with 30,000 initial simulations and adds 20,000 per round; total budget ≈ 190,000. TSNPE and SNVI are compared at matching budgets. Invalid = NaN summary statistics.
- **Note**: Values read approximately from Figure 4c line plot. Marked ≈.

| Round | Total Budget (×10³) | TSNPSE (SNPSE-VP) % valid (≈) | TSNPE % valid (≈) | SNVI % valid (≈) |
|-------|--------------------|---------------------------------|--------------------|------------------|
| 1 | 30 | ≈20% | ≈20% | ≈20% |
| 2 | 50 | ≈35% | ≈28% | ≈25% |
| 3 | 70 | ≈50% | ≈35% | ≈30% |
| 4 | 90 | ≈60% | ≈42% | ≈38% |
| 5 | 110 | ≈68% | ≈48% | ≈43% |
| 6 | 130 | ≈73% | ≈55% | ≈48% |
| 7 | 150 | ≈77% | ≈60% | ≈53% |
| 8 | 170 | ≈79% | ≈65% | ≈58% |
| 9 | 190 | ≈81% | ≈70% | ≈62% |

**Key stated result (from §5.3)**: "In the final round, we achieved 81% valid summary statistics from the simulator (Figure 4c), superior to the percentage achieved by other methods for the same simulation budget."
