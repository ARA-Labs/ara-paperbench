# Figure 19: QoE Gain Estimation Time Horizon (∆t) Sensitivity
- **Source**: Figure 19, Section 6.4
- **Caption**: "Varying ∆t."
- **Model**: Llama 3.1 70B; Multi-Round ShareGPT dataset; default cyclic burst load
- **Systems**: Andes (multiple ∆t values), vLLM, LQSF, Sarathi-Serve
- **X-axis**: ∆t values (specific values not enumerated in paper text)
- **Y-axis**: Average QoE

## Key Observation (§6.4)
"The average QoE remains roughly consistent for various ∆t values and significantly outperforms the baselines. The best value of ∆t depends on both the model and request input/output distribution, requiring fine-tuning prior to deployment."

| System | QoE behavior vs. ∆t |
|--------|---------------------|
| Andes | Roughly flat across tested ∆t values; consistently high |
| vLLM | Flat and low (∆t does not affect FCFS) |
| LQSF | Flat; slight improvement over vLLM |
| Sarathi-Serve | Flat; low |

**Note**: Exact ∆t values and corresponding QoE numbers are not reported in paper text; results shown as line plot.
