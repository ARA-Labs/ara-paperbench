# Training / Evaluation Run Configuration

## Agent Timeout
- **Value**: 40 minutes (soft limit)
- **Rationale**: Provides sufficient time for most experiments while bounding compute cost; IA models frequently consume the full timeout, OH models often stop early
- **Search range**: Not searched; fixed operational constraint
- **Sensitivity**: high (IA agents are particularly sensitive; OH models often terminate before timeout)
- **Source**: §4.1

## GPU Allocation per Agent Run
- **Value**: 4× NVIDIA A40
- **Rationale**: Sufficient for most deep learning inference/training tasks in the benchmark; matches hardware available in a standard research cluster node
- **Search range**: Not varied
- **Sensitivity**: medium (tasks with very large models may fail due to memory constraints)
- **Source**: §4.1

## Container Image
- **Value**: Ubuntu 24.04 Docker container
- **Rationale**: Clean, reproducible environment ensures no state leakage between agent runs; standard Linux environment compatible with most ML codebases
- **Search range**: Not varied
- **Sensitivity**: medium (some tasks have environment-specific dependencies that may conflict)
- **Source**: §4.1

## LLM Judge Model
- **Value**: o3-mini-2025-01-01-preview
- **Rationale**: Top-performing reasoning model at evaluation time; used for monitor, design/conclusion, and implementation evaluation
- **Search range**: Not varied
- **Sensitivity**: high (judge quality directly impacts metric reliability)
- **Source**: §4.1

## Extraction LLM (Main Task)
- **Value**: o3-mini-2025-01-01-preview
- **Rationale**: Used for multi-modal task extraction from PDFs
- **Search range**: Not varied
- **Sensitivity**: high
- **Source**: App. F

## Extraction LLM (Implementation)
- **Value**: claude-3-7-sonnet-20250219-v1:0
- **Rationale**: Strong code understanding and tool-use capability for codebase search
- **Search range**: Not varied
- **Sensitivity**: high
- **Source**: App. F

## Average Curation Cost per Paper
- **Value**: ~$60 USD (LLM API costs only; primarily input tokens from full paper + codebase)
- **Rationale**: Dominated by input token costs for full paper + codebase ingestion in extraction stage
- **Search range**: Not applicable
- **Sensitivity**: medium (varies with paper and codebase length)
- **Source**: App. F

## Manual Validation Time per Paper (Post-Pipeline)
- **Value**: ~20 minutes
- **Rationale**: After pipeline finalization, human review is limited to lightweight consistency checks; pre-pipeline manual time was ~2 hours/paper
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: App. F
