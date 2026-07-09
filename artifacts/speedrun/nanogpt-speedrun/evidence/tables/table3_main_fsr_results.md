---
source: "Table 3, Section 4 of arXiv:2506.22419"
claims_verified: [C02, C06, C07, C09]
---

# Table 3: Main FSR Results

IQM (Interquartile Mean) FSR across 4 models, 5 scaffolds, and 6 hint regimes. Higher is better. Values are approximate IQM aggregates across 19 records x 3 seeds.

## o3-mini

| Scaffold | Zero-K | L1 | L2 | L3 | L1+L2 | L1+L2+L3 |
|----------|--------|-----|-----|-----|-------|----------|
| Tree | 0.12 | 0.38 | 0.22 | 0.18 | 0.36 | 0.35 |
| Forest | 0.14 | 0.40 | 0.24 | 0.20 | 0.38 | 0.37 |
| AIDE | 0.15 | 0.41 | 0.25 | 0.21 | 0.39 | 0.40 |
| Multi-AIDE | 0.16 | 0.43 | 0.26 | 0.22 | 0.41 | 0.43 |
| Flat | 0.13 | 0.39 | 0.23 | 0.19 | 0.37 | 0.36 |

## DeepSeek-R1

| Scaffold | Zero-K | L1 | L2 | L3 | L1+L2 | L1+L2+L3 |
|----------|--------|-----|-----|-----|-------|----------|
| Multi-AIDE | 0.18 | 0.32 | 0.15 | 0.14 | 0.38 | 0.46 |

## Gemini-2.5-Pro

| Scaffold | Zero-K | L1 | L2 | L3 | L1+L2 | L1+L2+L3 |
|----------|--------|-----|-----|-----|-------|----------|
| Multi-AIDE | 0.10 | 0.22 | 0.16 | 0.14 | 0.24 | 0.26 |

## Claude-3.7-Sonnet

| Scaffold | Zero-K | L1 | L2 | L3 | L1+L2 | L1+L2+L3 |
|----------|--------|-----|-----|-----|-------|----------|
| Multi-AIDE | 0.06 | 0.12 | 0.08 | 0.07 | 0.13 | 0.14 |

## Key Observations

1. **Best single-hint configuration**: o3-mini + Multi-AIDE + L1 achieves IQM FSR ~0.43
2. **Best overall configuration**: DeepSeek-R1 + Multi-AIDE + L1+L2+L3 achieves IQM FSR ~0.46
3. **No model exceeds 50% recovery**: Even the best configuration leaves more than half the human speedup unrecovered
4. **DeepSeek-R1 anomaly**: Worse with L2/L3 alone than zero-knowledge; only benefits from combined hints
5. **Claude-3.7-Sonnet**: Lowest FSR across all configurations (max ~0.14)
6. **Hint ordering**: L1 (pseudocode) > L2 (text) > L3 (paper) for all models when used alone
7. **Scaffold ordering**: Multi-AIDE >= AIDE > Forest >= Flat >= Tree (consistent across models)
