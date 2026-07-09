# Figure 4c: Pyloric Experiment — % Valid Summary Statistics vs Simulation Budget

- **Source**: Figure 4c, Section 5.3
- **Caption**: "Percentage of valid summary statistics from the pyloric simulator against simulation budget for 3 different methods, SNPSE (ours, blue), TSNPE (orange), SNVI (pink)."
- **Experimental conditions**:
  - Task: Pyloric network simulator; 31 parameters, 18 summary statistics
  - Invalid = simulator returns NaN in ≥1 summary statistic dimension
  - SNPSE uses VP SDE; 9 rounds; 30000 initial + 20000 per round (total ≈ 190000)
  - Budget axis (×10³ simulations): 0 to ~200k

## Data Points (Read from Plot)

All values are approximate (≈) as the paper presents visual plots without exact numbers.

| Budget (×10³) | SNPSE (ours, VP) | TSNPE | SNVI |
|---------------|------------------|-------|------|
| 30 (round 1) | ≈2% | ≈2% | ≈2% |
| 50 | ≈15% | ≈5% | ≈5% |
| 70 (round 3) | ≈35% | ≈10% | ≈8% |
| 90 | ≈50% | ≈18% | ≈12% |
| 110 (round 5) | ≈62% | ≈28% | ≈18% |
| 130 | ≈68% | ≈38% | ≈25% |
| 150 (round 7) | ≈73% | ≈45% | ≈32% |
| 170 | ≈77% | ≈52% | ≈38% |
| 190 (round 9) | ≈81% | ≈58% | ≈45% |

## Key Takeaways
- **Final round result (stated explicitly in paper)**: SNPSE achieves 81% valid summary statistics.
- SNPSE outperforms TSNPE and SNVI at all simulation budget levels shown.
- The advantage is consistent and growing across rounds, indicating effective sequential focusing.
- Starting point (~2%) reflects that >99% of prior samples yield invalid statistics.
