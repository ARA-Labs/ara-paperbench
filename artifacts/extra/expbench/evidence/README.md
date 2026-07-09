# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_main_results.md](tables/table1_main_results.md) | Table 1, §4.1 | C01, C02 | Average benchmark scores (D, I, E, C, I·E, All✓, All·E✓) across all 461 tasks for 7 agent configurations, showing best All·E✓ of 0.5% for OH+o3-mini. |
| [tables/table2_failure_patterns.md](tables/table2_failure_patterns.md) | Table 2, §4.3 | C04, C05 | Simplified subset of common failure types with prevalence percentages across four experiment phases (design, implementation, execution, conclusion). |
| [tables/table3_category_results.md](tables/table3_category_results.md) | Table 3, §4.1 | C01 | Average benchmark scores broken down by task category (Applications, RL) for select agent-model pairs, showing RL agents reaching ~41% on I metric. |
| [tables/table4_iclr_papers.md](tables/table4_iclr_papers.md) | Table 4, App. B | — | Full list of ICLR 2024 source papers with GitHub stars, citation count, AI domain, key distinction, and hardware requirements. |
| [tables/table5_neurips_papers.md](tables/table5_neurips_papers.md) | Table 5, App. B | — | Full list of NeurIPS 2024 source papers with GitHub stars, citation count, AI domain, key distinction, and hardware requirements. |
| [tables/table6_full_category_results.md](tables/table6_full_category_results.md) | Table 6, App. D | C01, C03 | Complete per-category benchmark scores across all agents and all 17 AI subfields, including updated values for IA+3.5 Haiku. |
| [tables/table7_extraction_issues.md](tables/table7_extraction_issues.md) | Table 7, App. F | — | Examples of extraction pipeline failures identified and patched, covering task components: question, masked source, requirements, expected outcome, method/instruction. |
| [tables/table8_extended_failure_patterns.md](tables/table8_extended_failure_patterns.md) | Table 8, App. G | C04, C05 | Extended failure type analysis across all phases with 361 unique categories and prevalence percentages for each. |
| [tables/table9_cost_time.md](tables/table9_cost_time.md) | Table 9, App. I.2 | — | Full cost–time summary statistics (avg, median, Q1, Q3, std, min, max for both time in minutes and cost in USD) for all 7 agent configurations. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig6b_conjunctive_metrics.md](figures/fig6b_conjunctive_metrics.md) | Figure 6b, §4.2 | C03 | Average score (%) vs. progressive conjunctive metric strictness (M → M·C·D → M·C·D·I → M·C·D·I·E) for 4 OpenHands configurations, showing monotone score collapse from 20.6% to 0.2%. |
| [figures/fig5_metric_stability.md](figures/fig5_metric_stability.md) | Figure 5, §4.2 | C06 | Metric stability analysis comparing variance of individual metrics (C, E) vs. conjunctive metrics (C·D, I·E), demonstrating that conjunctive forms produce more stable evaluation signals. |
| [figures/fig6a_cost_time.md](figures/fig6a_cost_time.md) | Figure 6a, §4.2 | — | Average cost (USD) vs. average time (minutes) per task for all 7 agent configurations with performance rank annotations, showing OH+o3-mini achieves best cost-performance tradeoff. |
