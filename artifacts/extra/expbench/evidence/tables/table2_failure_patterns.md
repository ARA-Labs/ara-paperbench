# Table 2: Agent Failure Patterns — Simplified Subset
- **Source**: Table 2, Section 4.3
- **Caption**: "Agents fail in diverse ways across different phases of experimentation; this table presents a simplified subset of common examples, measured across all agent and model evaluations."
- **Conditions**: Analysis across all 7 agent configurations on all 461 tasks; 3,238 raw insights distilled to 361 unique failure types; subset presented here; some overlap between categories possible (LLM-based classification)

| Phase | Failure Type | Prevalence (%) |
|-------|-------------|----------------|
| Design | Incomplete or Misclassified Design Variables | 16.05 |
| Design | Irrelevant Procedural Additions in Design | 7.62 |
| Implementation | Missing Essential implementation Components | 39.71 |
| Implementation | Incomplete Evaluation Metric Implementation | 2.15 |
| Implementation | Incomplete Data and Preprocessing Setup | 1.83 |
| Execution | Environment/Dependency Configuration Errors | 29.38 |
| Execution | Execution Script and File Errors | 23.84 |
| Execution | Missing Setup Script File | 6.95 |
| Execution | Tensor Operation Execution Error | 3.22 |
| Conclusion | Missing Conclusion Content | 26.18 |
| Conclusion | Incorrect Conclusion Interpretation | 19.66 |
| Conclusion | Extraneous Details in Conclusion | 7.77 |
| Conclusion | Incorrect Numeric Conclusion | 3.21 |

**Example failure instances cited in paper**:
- Missing essential components: semantic retrieval strategies (UniXcoder-H2L and UniXcoder-L2H), validation functions (GPT-3.5 filtering), Mixup/CutMix/Label Smoothing techniques
- Incomplete preprocessing: ETTh1 series preparation, ACF plotting, RevIN normalization
- Env/dependency errors: STORM not registered in jaxmarl; missing PyTorch and Flax
- Script errors: moganet_tiny not found in timm; missing checkpoint files
- Missing conclusions: omitting PPO vs. Q-Learning comparison details; neglecting 1.25% improvement across ARC-Challenge and OpenBookQA
- Incorrect interpretation: claiming Hadamard-enhanced INT4 inference improves performance without substantiating baseline comparison
