# Figure 11: CDF of QoE, TTFT, and TDS on BurstGPT Trace
- **Source**: Figure 11, Section 6.2
- **Caption**: "QoE, TTFT, and TDS CDFs of requests in BurstGPT."
- **Conditions**: Phi-3.5-MoE 16×3.8B, 8× A100 SXM4 40 GB, one-hour BurstGPT slice, Multi-Round ShareGPT dataset. Systems: Andes vs. vLLM (FCFS).

## Figure 11a: CDF of QoE
| QoE Threshold | Andes CDF (fraction of requests ≤ threshold) | vLLM CDF | Notes |
|---------------|---------------------------------------------|---------|-------|
| 0.95 | ≈0.03 (3% below 0.95) | ≈0.25 (25% below 0.95) | Derived from stated: 97% Andes ≥0.95; 75% vLLM ≥0.95 |

**Key stated values**:
- Andes average QoE: 0.99
- vLLM average QoE: 0.88
- Andes: 97% of requests achieve QoE ≥ 0.95
- vLLM: 75% of requests achieve QoE ≥ 0.95

## Figure 11b: CDF of TTFT
**Key stated values**:
- Andes average TTFT: 1.8 s
- vLLM average TTFT: 10.5 s

## Figure 11c: CDF of TDS
**Key stated values**:
- Andes average TDS: 10.9 tokens/s
- vLLM average TDS: 11.2 tokens/s

**Note**: CDF curves are not tabulated in the paper; only the key scalar statistics above are explicitly stated in Section 6.2. Exact CDF shapes require reading from the figure image.
