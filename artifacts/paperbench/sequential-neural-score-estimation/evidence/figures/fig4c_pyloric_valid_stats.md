# Figure 4c: Pyloric Valid Summary Statistics vs Simulation Budget
- **Source**: Figure 4c, Section 5.3
- **Caption**: "Percentage of valid summary statistics from the pyloric simulator against simulation budget for 3 different methods, SNPSE (ours, blue), TSNPE (orange), SNVI (pink)."
- **Experimental conditions**: TSNPSE-VP, 9 rounds, 30000 initial simulations + 20000 per subsequent round. Invalid = NaN output from pyloric simulator. 31 parameters, 18 summary statistics.
- **Axes**: x-axis = Simulation Budget (×10³); y-axis = Percentage of Valid Summary Statistics (%)

Note: Values read approximately from line plot; ≈ indicates approximate visual readings.

| Simulation Budget (×10³) | TSNPSE/SNPSE (ours) % valid | TSNPE % valid | SNVI % valid |
|--------------------------|-------------------------------|----------------|--------------|
| 30 | ≈5 | ≈5 | ≈5 |
| 50 | ≈15 | ≈8 | ≈8 |
| 70 | ≈30 | ≈12 | ≈10 |
| 90 | ≈45 | ≈18 | ≈15 |
| 110 | ≈55 | ≈25 | ≈22 |
| 130 | ≈63 | ≈32 | ≈28 |
| 150 | ≈70 | ≈40 | ≈35 |
| 170 | ≈77 | ≈50 | ≈45 |
| 190 | ≈81 | ≈60 | ≈55 |

**Key reported facts (exact, from §5.3 text)**:
- Final round (round 9, ~190k total simulations): TSNPSE achieves **81%** valid summary statistics
- TSNPSE outperforms TSNPE and SNVI for all simulation budgets below 200×10³
- Previous work (Gonçalves et al. 2020) using NPE required **several million simulations**
- Recent sequential methods (Glöckler et al. 2022; Deistler et al. 2022a) reduced required simulations by **25× or more**
