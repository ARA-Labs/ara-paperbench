---
type: evidence_index
paper: nanogpt-speedrun
---

# Evidence Index

## Tables

| File | Description | Claims |
|------|-------------|--------|
| `tables/table1_speedrun_progression.md` | All 21 records with timing, val_loss, key optimization, and phase classification | C01, C03, C05, C10 |
| `tables/table2_scaffold_configs.md` | Search scaffold configuration parameters (Tree, Forest, AIDE, Multi-AIDE, Flat) | C07 |
| `tables/table3_main_fsr_results.md` | Main FSR results: 4 models x 5 scaffolds x 6 hint regimes | C02, C06, C07, C09 |
| `tables/table4_cumulative_degradation.md` | Cumulative vs. non-cumulative FSR degradation over chained transitions | C08 |
| `tables/table5_external_knowledge.md` | FSR with and without FlexAttention API docs on Record 12 | C09 |
| `tables/table6_per_record_fsr.md` | Per-record FSR by model showing monotonic difficulty increase | C02, C06, C08 |

## Figures

| File | Description | Claims |
|------|-------------|--------|
| `figures/fig1_timeline.md` | NanoGPT speedrun timeline and training time reduction | C01 |
| `figures/fig3_fsr_distributions.md` | FSR distributions across models and hint levels (violin/box plots) | C02, C06 |
| `figures/fig4_hint_ablation.md` | FSR vs. hint level for each model | C09 |
| `figures/fig5_scaffold_comparison.md` | IQM FSR across scaffolds per model | C07 |
| `figures/fig6_per_record_fsr.md` | FSR vs. record index showing difficulty scaling | C02, C08 |
| `figures/fig7_cumulative_degradation.md` | Cumulative FSR degradation over chained transitions | C08 |
| `figures/fig8_search_dynamics.md` | Node-type fractions over search steps per model | C02 |
| `figures/fig9_code_similarity.md` | Code embedding similarity vs. FSR scatter plot | C02 |
