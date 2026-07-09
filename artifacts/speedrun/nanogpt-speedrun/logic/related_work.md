---
type: related_work
paper: nanogpt-speedrun
---

# Related Work

## Dependencies

- **[Muon Optimizer (Jordan et al.)]** — type: imports — Muon is the core optimizer innovation enabling Records 3-6. ARA provides implementation stub.
- **[FlexAttention (PyTorch team)]** — type: imports — FlexAttention API is critical for Records 11-12. External doc provided as knowledge hint.
- **[NanoGPT (Karpathy)]** — type: baseline — The original NanoGPT codebase and training recipe that Record 1 starts from.
- **[FineWeb-Edu (HuggingFace)]** — type: imports — Fixed training dataset for all records.
- **[AIDE (Weco AI)]** — type: baseline — Linear experimentation strategy used as baseline search method for agent evaluation.
- **[PaperBench (OpenAI)]** — type: bounds — Rubric-based evaluation methodology. LLM Speedrunner uses analogous per-record success criteria.
- **[MLPerf (MLCommons)]** — type: baseline — Hardware-focused training benchmarks. NanoGPT speedrun differs by focusing on algorithmic/software optimizations on fixed hardware.
- **[DAWNBench (Stanford)]** — type: baseline — Cost-aware training benchmarks. Conceptual predecessor to speedrun-style competitions.
- **[SWE-Bench (Princeton)]** — type: bounds — Code-level agent evaluation benchmark. LLM Speedrunner extends to distributed ML systems engineering.
- **[Aider]** — type: imports — Diff-based code editing tool used as the Coder backend in the agent framework.
