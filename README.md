# Agent-Native Research Artifacts (ARA) — Benchmark Collection

This repository collects **32 Agent-Native Research Artifacts (ARAs)**: a machine-readable, reproducibility-first alternative to the PDF paper. Each ARA decomposes a research paper into four grounded layers so that both humans and agents can read the claims, run the code, inspect the evidence, and replay how the research was actually explored (dead ends included).

## Anatomy of an ARA

Every artifact lives at `artifacts/<benchmark>/<name>/` and contains:

| Layer | Path | What it holds |
|-------|------|---------------|
| Summary | `PAPER.md` | Human-readable overview of the paper. |
| Cognitive | `logic/` | `claims.md`, `concepts.md`, `experiments.md`, `problem.md`, `related_work.md`, and `solution/` (`algorithm.md`, `architecture.md`, `constraints.md`, `heuristics.md`). Claims carry falsification criteria and proof pointers. |
| Artifact | `src/` | Runnable code, configs, and `environment.md`. |
| Evidence | `evidence/` | `figures/` and `tables/`, each tied back to the claims it supports. |
| Trajectory | `trajectory.html` | Self-contained interactive viewer: a clickable process map (left) plus a per-step drill-down (right) linking each step to its claim, grounded result, and code. Open in a browser. |
| Trace | `trace/` | `exploration_tree.yaml` (the research DAG source) and `exploration_tree.html` (a tree-only view). |

## How to browse

- Read any `artifacts/<benchmark>/<name>/PAPER.md` for the overview, then drill into `logic/` and `evidence/`.
- Open an artifact's `trajectory.html` in a browser to replay the research process step by step: a process map on the left (dead-end branches included) and a per-step drill-down on the right (what the step did, its linked claim, the grounded result, and the code pointer). (GitHub shows the HTML source inline; clone the repo or download the file to view it rendered.)

## Artifacts

### Paperbench (23)

| Artifact | Title | Trajectory |
|----------|-------|-------|
| [adaptive-pruning](artifacts/paperbench/adaptive-pruning/) | APT: Adaptive Pruning and Tuning of Pretrained Language Models for Efficient Training and Inference | [view](artifacts/paperbench/adaptive-pruning/trajectory.html) |
| [all-in-one](artifacts/paperbench/all-in-one/) | All-in-one Simulation-Based Inference (Simformer) | [view](artifacts/paperbench/all-in-one/trajectory.html) |
| [bam](artifacts/paperbench/bam/) | Batch and Match: Black-Box Variational Inference with a Score-Based Divergence | [view](artifacts/paperbench/bam/trajectory.html) |
| [bbox](artifacts/paperbench/bbox/) | BBox-Adapter: Lightweight Adapting for Black-Box Large Language Models | [view](artifacts/paperbench/bbox/trajectory.html) |
| [bridging-data-gaps](artifacts/paperbench/bridging-data-gaps/) | Efficient Transfer Learning in Diffusion Models via Adversarial Noise | [view](artifacts/paperbench/bridging-data-gaps/trajectory.html) |
| [fre](artifacts/paperbench/fre/) | Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings | [view](artifacts/paperbench/fre/trajectory.html) |
| [ftrl](artifacts/paperbench/ftrl/) | Fine-Tuning RL Models is Secretly a Forgetting Mitigation Problem | [view](artifacts/paperbench/ftrl/trajectory.html) |
| [lbcs](artifacts/paperbench/lbcs/) | Refined Coreset Selection: Minimal Coreset Size under Model Performance Constraints | [view](artifacts/paperbench/lbcs/trajectory.html) |
| [lca-on-the-line](artifacts/paperbench/lca-on-the-line/) | LCA-on-the-Line: Benchmarking Out-of-Distribution Generalization with Class Taxonomies | [view](artifacts/paperbench/lca-on-the-line/trajectory.html) |
| [mechanistic-understanding](artifacts/paperbench/mechanistic-understanding/) | A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO | [view](artifacts/paperbench/mechanistic-understanding/trajectory.html) |
| [pinn](artifacts/paperbench/pinn/) | Challenges in Training PINNs: A Loss Landscape Perspective | [view](artifacts/paperbench/pinn/trajectory.html) |
| [rice](artifacts/paperbench/rice/) | RICE: Breaking Through the Training Bottlenecks of Reinforcement Learning with Explanation | [view](artifacts/paperbench/rice/trajectory.html) |
| [robust-clip](artifacts/paperbench/robust-clip/) | Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Vision-Language Models | [view](artifacts/paperbench/robust-clip/trajectory.html) |
| [sample-specific-masks](artifacts/paperbench/sample-specific-masks/) | Sample-specific Masks for Visual Reprogramming-based Prompting | [view](artifacts/paperbench/sample-specific-masks/trajectory.html) |
| [sapg](artifacts/paperbench/sapg/) | SAPG: Split and Aggregate Policy Gradients | [view](artifacts/paperbench/sapg/trajectory.html) |
| [self-composing-policies](artifacts/paperbench/self-composing-policies/) | Self-Composing Policies for Scalable Continual Reinforcement Learning | [view](artifacts/paperbench/self-composing-policies/trajectory.html) |
| [self-expansion](artifacts/paperbench/self-expansion/) | Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning | [view](artifacts/paperbench/self-expansion/trajectory.html) |
| [semantic-self-consistency](artifacts/paperbench/semantic-self-consistency/) | Semantic Self-Consistency: Enhancing Language Model Reasoning via Semantic Weighting | [view](artifacts/paperbench/semantic-self-consistency/trajectory.html) |
| [sequential-neural-score-estimation](artifacts/paperbench/sequential-neural-score-estimation/) | Sequential Neural Posterior Score Estimation (NPSE) | [view](artifacts/paperbench/sequential-neural-score-estimation/trajectory.html) |
| [stay-on-topic-with-classifier-free-guidance](artifacts/paperbench/stay-on-topic-with-classifier-free-guidance/) | Stay on Topic with Classifier-Free Guidance | [view](artifacts/paperbench/stay-on-topic-with-classifier-free-guidance/trajectory.html) |
| [stochastic-interpolants](artifacts/paperbench/stochastic-interpolants/) | Stochastic Interpolants with Data-Dependent Couplings | [view](artifacts/paperbench/stochastic-interpolants/trajectory.html) |
| [test-time-model-adaptation](artifacts/paperbench/test-time-model-adaptation/) | Test-Time Model Adaptation with Only Forward Passes (FOA) | [view](artifacts/paperbench/test-time-model-adaptation/trajectory.html) |
| [what-will-my-model-forget](artifacts/paperbench/what-will-my-model-forget/) | What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement | [view](artifacts/paperbench/what-will-my-model-forget/trajectory.html) |

### ReBench (5)

| Artifact | Title | Trajectory |
|----------|-------|-------|
| [rebench-fix_embedding](artifacts/rebench/rebench-fix_embedding/) | Fix Embedding (RE-Bench task) | [view](artifacts/rebench/rebench-fix_embedding/trajectory.html) |
| [rebench-nanogpt_chat_rl](artifacts/rebench/rebench-nanogpt_chat_rl/) | nanoGPT Chat RL (RE-Bench task) | [view](artifacts/rebench/rebench-nanogpt_chat_rl/trajectory.html) |
| [rebench-restricted_mlm](artifacts/rebench/rebench-restricted_mlm/) | Restricted-Architecture MLM (RE-Bench task) | [view](artifacts/rebench/rebench-restricted_mlm/trajectory.html) |
| [rebench-rust_codecontests](artifacts/rebench/rebench-rust_codecontests/) | Rust CodeContests Inference (RE-Bench task) | [view](artifacts/rebench/rebench-rust_codecontests/trajectory.html) |
| [rebench-triton_cumsum](artifacts/rebench/rebench-triton_cumsum/) | Triton Cumsum Kernel (RE-Bench task) | [view](artifacts/rebench/rebench-triton_cumsum/trajectory.html) |

### Speedrun (1)

| Artifact | Title | Trajectory |
|----------|-------|-------|
| [nanogpt-speedrun](artifacts/speedrun/nanogpt-speedrun/) | NanoGPT Speedrun | [view](artifacts/speedrun/nanogpt-speedrun/trajectory.html) |

### Extra (3)

| Artifact | Title | Trajectory |
|----------|-------|-------|
| [andes](artifacts/extra/andes/) | Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services | [view](artifacts/extra/andes/trajectory.html) |
| [venn](artifacts/extra/venn/) | Venn: Resource Management for Collaborative Learning Jobs | [view](artifacts/extra/venn/trajectory.html) |
| [expbench](artifacts/extra/expbench/) | EXP-Bench: Can AI Conduct AI Research Experiments? | [view](artifacts/extra/expbench/trajectory.html) |

## Provenance & quality

Each ARA was compiled from a source paper and its accompanying code; the content is grounded to the source paper (claims, figures, and tables trace back to the original). A subset additionally passed SEAL structural and cross-layer validation. These artifacts are reconstructions for research and evaluation purposes; consult the original papers and their licenses for authoritative results.

## Benchmarks

The `paperbench`, `rebench`, and `speedrun` artifacts correspond to the ARA evaluation benchmark. The `extra` artifacts are additional complete ARAs beyond the benchmark set.

## License

Content is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
