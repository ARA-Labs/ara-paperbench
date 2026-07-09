# Table 8: Extended Failure Type Analysis
- **Source**: Table 8, Appendix G
- **Caption**: "Agents fail in diverse ways across different phases of experimentation, measured across all agent and model evaluations."
- **Conditions**: 3,238 raw insights distilled to 361 unique failure types across all 7 agent configurations; some overlap between categories possible (LLM-based classification); only a subset shown here (full list in appendix)

| Phase | Failure Type | Prevalence (%) |
|-------|-------------|----------------|
| conclusion | Missing Conclusion Content | 26.18 |
| conclusion | Incorrect Conclusion Interpretation | 19.66 |
| conclusion | Incomplete Conclusion Outcome Statement | 14.43 |
| conclusion | Extraneous Details | 7.77 |
| conclusion | Missing Conclusion Analysis | 4.35 |
| conclusion | Missing Comparative Conclusion Analysis | 4.03 |
| conclusion | Minor Omission of Specific Details | 3.47 |
| conclusion | Incorrect Numeric Conclusion | 3.21 |
| conclusion | Mismatched Conclusion Format | 2.7 |
| conclusion | Error Message Output | 2.67 |
| conclusion | Incomplete Conclusion with Missing Exp. Findings | 2.14 |
| conclusion | Conclusion Diverges from Expected Emphasis | 1.6 |
| conclusion | Missing Comparative Analysis | 0.8 |
| conclusion | Missing Quantitative Performance Metrics | 0.8 |
| conclusion | Missing Visualization Details | 0.56 |
| conclusion | Incomplete Performance Evaluation | 0.53 |
| conclusion | Missing Numerical Equivalence Verification | 0.53 |
| conclusion | Missing Trend Analysis | 0.53 |
| conclusion | Naming Inconsistency Output | 0.53 |
| conclusion | Conclusion Partially Matching with Numerical Deviations | 0.27 |
| conclusion | Deviation in Saturation Point Conclusion | 0.27 |
| conclusion | Inconsistent ASR Reporting | 0.27 |
| conclusion | Missing Conclusion Analysis on Attack Budget Effects | 0.27 |
| conclusion | Missing Diminishing Returns Analysis | 0.27 |
| conclusion | Missing Methodological Innovation Discussion | 0.27 |
| conclusion | Missing Performance Evaluation Metrics | 0.27 |
| conclusion | Missing Submission Format Specification | 0.27 |
| design | Incomplete or Misclassified Design Variables | 16.05 |
| design | Omission of Required Design Variables | 19.84 |
| design | Complete Omission of Exp. Design Variables | 13.1 |
| design | Incorrect Design Specification Details | 8.32 |
| design | Incomplete Exp. Design Details | 7.67 |
| design | Irrelevant Procedural Additions | 7.62 |
| design | Missing Design Variable Information | 3.83 |
| design | Inclusion of Extraneous Factors | 3.64 |
| design | Incorrect Parameter Details | 3.18 |
| design | Partial Omission of Constant Variables | 2.75 |
| design | Incomplete Constant Variable Specification | 3.61 |
| design | Partial Fulfillment of DV | 1.93 |
| design | Error Message Returned Instead of Design Information | 1.27 |
| design | Incomplete Differentiation of Constant and Ind. Variables | 1.27 |
| design | Missing Dependent Variable Tracking | 1.06 |
| design | Incomplete Exp. Design Specification | 0.64 |
| design | Incomplete Specification of Design Variables | 0.64 |
| design | Missing Hyperparameter Design Details | 0.64 |
| design | Partially Complete Design Variable Specification | 0.64 |
| design | Missing Design Formatting Details | 0.42 |
| design | Missing Design Variables Details | 0.42 |
| design | Missing Explicit Variable Labeling | 0.42 |
| design | Missing Configuration File Variable | 0.21 |
| design | Missing Input Format Details | 0.21 |
| design | Omission of Exp. Configuration Details | 0.21 |
| design | Omission of Fixed Block Partition | 0.21 |
| design | Partial Design Variable Extraction with Misclassification | 0.21 |
| exec | Environment/Dependency Configuration Errors | 29.38 |
| exec | Execution Script and File Errors | 23.84 |
| exec | Missing Dependency Error | 11.9 |
| exec | Missing Setup Script File | 6.95 |
| exec | Tensor Operation Execution Error | 3.22 |
| exec | Syntax Error in Execution Environment | 2.86 |
| exec | Missing Input Data File | 2.27 |
| exec | Missing Required Attribute in Execution | 2.27 |
| exec | Missing Evaluation Output Files | 1.82 |
| exec | Missing Requirements File | 1.82 |
| exec | Runtime Indexing Error During Generation | 1.82 |
| exec | Insufficient Shared Memory in DataLoader Execution | 1.41 |
| exec | Execution Environment Warning: Root Privilege Usage | 1.36 |
| exec | Incorrect Dependency Import in Execution | 1.36 |
| exec | Dependency Version Conflict | 0.91 |
| exec | Docker Execution Failure | 0.91 |
| exec | Incomplete Results Saving Impl. | 0.91 |
| exec | Incorrect Dataset Loading | 0.91 |
| exec | Incorrect Function Argument Handling | 0.91 |
| exec | Missing Hugging Face API Token Authentication | 0.91 |
| exec | Missing Performance Metrics and Argument Parsing | 0.91 |
| exec | Missing Trust Remote Code Flag in Execution Environment | 0.91 |
| exec | Missing Setup Script File (duplicate) | 0.45 |
| setup | Missing Essential Impl. Components | 39.71 |
| setup | Incomplete Evaluation Metric Impl. | 2.15 |
| setup | Missing Critical Exp. Setup Details | 1.88 |
| setup | Incomplete Data and Preprocessing Setup | 1.83 |
| setup | Missing Command Line Argument Parsing | 1.58 |
| setup | Incomplete Exp. Setup Impl. | 1.49 |
| setup | Incomplete Training Regimen Impl. | 1.47 |
| setup | Incomplete Comparative Setup Features | 1.25 |
| setup | Missing Modular Helper Functions | 1.13 |
| setup | Incomplete Dataset Splitting Setup | 1.04 |
| setup | Missing Comparative Evaluation Methods | 1.02 |
| setup | Naming Inconsistencies Components | 1.02 |
| setup | Missing Detailed Architectural Parameters | 0.91 |
| setup | Incorrect Model Initialization | 0.9 |
| setup | Missing Optimizer Configuration | 0.9 |
| setup | Incomplete Evaluation Procedure | 0.79 |
| setup | Missing Critical Import Statements | 0.79 |
| setup | Missing Essential Library Imports | 0.56 |
| setup | Incomplete Results Saving Impl. | 0.45 |
| setup | Incomplete or Misplaced Setup Impls. | 0.45 |
| setup | Incorrect Dependency Import | 0.45 |
| setup | Misconfigured Exp. Infrastructure | 0.45 |
| setup | Missing C++ Acceleration Integration | 0.45 |
| setup | Missing Distributed Training Parameters | 0.45 |
| setup | Missing Hardware/Device Configuration | 0.45 |
| setup | Missing Training Pipeline Configuration | 0.45 |

**Notes**: Full list contains 361 unique failure types; only representative subset shown. "setup" phase corresponds to implementation phase in main paper (Table 2).
