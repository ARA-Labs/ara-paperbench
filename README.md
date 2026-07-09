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
| Trace | `trace/` | `exploration_tree.yaml` and `exploration_tree.html`: the research DAG, including branches that failed. |

## How to browse

- Read any `artifacts/<benchmark>/<name>/PAPER.md` for the overview, then drill into `logic/` and `evidence/`.
- Open a `trace/exploration_tree.html` in a browser to replay the research trajectory step by step; dead-end branches are rendered distinctly from the chosen path. (GitHub shows the HTML source inline; clone the repo or download the file to view it rendered.)

## Artifacts

### Paperbench (23)

| Artifact | Title | Trace |
|----------|-------|-------|
| [adaptive-pruning](artifacts/paperbench/adaptive-pruning/) | APT: Adaptive Pruning and Tuning of Pretrained Language Models for Efficient Training and Inference | [tree](artifacts/paperbench/adaptive-pruning/trace/exploration_tree.html) |
| [all-in-one](artifacts/paperbench/all-in-one/) | All-in-one Simulation-Based Inference (Simformer) | [tree](artifacts/paperbench/all-in-one/trace/exploration_tree.html) |
| [bam](artifacts/paperbench/bam/) | Batch and Match: Black-Box Variational Inference with a Score-Based Divergence | [tree](artifacts/paperbench/bam/trace/exploration_tree.html) |
| [bbox](artifacts/paperbench/bbox/) | BBox-Adapter: Lightweight Adapting for Black-Box Large Language Models | [tree](artifacts/paperbench/bbox/trace/exploration_tree.html) |
| [bridging-data-gaps](artifacts/paperbench/bridging-data-gaps/) | Efficient Transfer Learning in Diffusion Models via Adversarial Noise | [tree](artifacts/paperbench/bridging-data-gaps/trace/exploration_tree.html) |
| [fre](artifacts/paperbench/fre/) | Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings | [tree](artifacts/paperbench/fre/trace/exploration_tree.html) |
| [ftrl](artifacts/paperbench/ftrl/) | Fine-Tuning RL Models is Secretly a Forgetting Mitigation Problem | [tree](artifacts/paperbench/ftrl/trace/exploration_tree.html) |
| [lbcs](artifacts/paperbench/lbcs/) | Refined Coreset Selection: Minimal Coreset Size under Model Performance Constraints | [tree](artifacts/paperbench/lbcs/trace/exploration_tree.html) |
| [lca-on-the-line](artifacts/paperbench/lca-on-the-line/) | LCA-on-the-Line: Benchmarking Out-of-Distribution Generalization with Class Taxonomies | [tree](artifacts/paperbench/lca-on-the-line/trace/exploration_tree.html) |
| [mechanistic-understanding](artifacts/paperbench/mechanistic-understanding/) | A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO | [tree](artifacts/paperbench/mechanistic-understanding/trace/exploration_tree.html) |
| [pinn](artifacts/paperbench/pinn/) | Challenges in Training PINNs: A Loss Landscape Perspective | [tree](artifacts/paperbench/pinn/trace/exploration_tree.html) |
| [rice](artifacts/paperbench/rice/) | RICE: Breaking Through the Training Bottlenecks of Reinforcement Learning with Explanation | [tree](artifacts/paperbench/rice/trace/exploration_tree.html) |
| [robust-clip](artifacts/paperbench/robust-clip/) | Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Vision-Language Models | [tree](artifacts/paperbench/robust-clip/trace/exploration_tree.html) |
| [sample-specific-masks](artifacts/paperbench/sample-specific-masks/) | Sample-specific Masks for Visual Reprogramming-based Prompting | [tree](artifacts/paperbench/sample-specific-masks/trace/exploration_tree.html) |
| [sapg](artifacts/paperbench/sapg/) | SAPG: Split and Aggregate Policy Gradients | [tree](artifacts/paperbench/sapg/trace/exploration_tree.html) |
| [self-composing-policies](artifacts/paperbench/self-composing-policies/) | Self-Composing Policies for Scalable Continual Reinforcement Learning | [tree](artifacts/paperbench/self-composing-policies/trace/exploration_tree.html) |
| [self-expansion](artifacts/paperbench/self-expansion/) | Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning | [tree](artifacts/paperbench/self-expansion/trace/exploration_tree.html) |
| [semantic-self-consistency](artifacts/paperbench/semantic-self-consistency/) | Semantic Self-Consistency: Enhancing Language Model Reasoning via Semantic Weighting | [tree](artifacts/paperbench/semantic-self-consistency/trace/exploration_tree.html) |
| [sequential-neural-score-estimation](artifacts/paperbench/sequential-neural-score-estimation/) | Sequential Neural Posterior Score Estimation (NPSE) | [tree](artifacts/paperbench/sequential-neural-score-estimation/trace/exploration_tree.html) |
| [stay-on-topic-with-classifier-free-guidance](artifacts/paperbench/stay-on-topic-with-classifier-free-guidance/) | Stay on Topic with Classifier-Free Guidance | [tree](artifacts/paperbench/stay-on-topic-with-classifier-free-guidance/trace/exploration_tree.html) |
| [stochastic-interpolants](artifacts/paperbench/stochastic-interpolants/) | Stochastic Interpolants with Data-Dependent Couplings | [tree](artifacts/paperbench/stochastic-interpolants/trace/exploration_tree.html) |
| [test-time-model-adaptation](artifacts/paperbench/test-time-model-adaptation/) | Test-Time Model Adaptation with Only Forward Passes (FOA) | [tree](artifacts/paperbench/test-time-model-adaptation/trace/exploration_tree.html) |
| [what-will-my-model-forget](artifacts/paperbench/what-will-my-model-forget/) | What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement | [tree](artifacts/paperbench/what-will-my-model-forget/trace/exploration_tree.html) |

### ReBench (5)

| Artifact | Title | Trace |
|----------|-------|-------|
| [rebench-fix_embedding](artifacts/rebench/rebench-fix_embedding/) | Fix Embedding (RE-Bench task) | [tree](artifacts/rebench/rebench-fix_embedding/trace/exploration_tree.html) |
| [rebench-nanogpt_chat_rl](artifacts/rebench/rebench-nanogpt_chat_rl/) | nanoGPT Chat RL (RE-Bench task) | [tree](artifacts/rebench/rebench-nanogpt_chat_rl/trace/exploration_tree.html) |
| [rebench-restricted_mlm](artifacts/rebench/rebench-restricted_mlm/) | Restricted-Architecture MLM (RE-Bench task) | [tree](artifacts/rebench/rebench-restricted_mlm/trace/exploration_tree.html) |
| [rebench-rust_codecontests](artifacts/rebench/rebench-rust_codecontests/) | Rust CodeContests Inference (RE-Bench task) | [tree](artifacts/rebench/rebench-rust_codecontests/trace/exploration_tree.html) |
| [rebench-triton_cumsum](artifacts/rebench/rebench-triton_cumsum/) | Triton Cumsum Kernel (RE-Bench task) | [tree](artifacts/rebench/rebench-triton_cumsum/trace/exploration_tree.html) |

### Speedrun (1)

| Artifact | Title | Trace |
|----------|-------|-------|
| [nanogpt-speedrun](artifacts/speedrun/nanogpt-speedrun/) | NanoGPT Speedrun | [tree](artifacts/speedrun/nanogpt-speedrun/trace/exploration_tree.html) |

### Extra (3)

| Artifact | Title | Trace |
|----------|-------|-------|
| [andes](artifacts/extra/andes/) | Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services | [tree](artifacts/extra/andes/trace/exploration_tree.html) |
| [venn](artifacts/extra/venn/) | Venn: Resource Management for Collaborative Learning Jobs | [tree](artifacts/extra/venn/trace/exploration_tree.html) |
| [expbench](artifacts/extra/expbench/) | EXP-Bench: Can AI Conduct AI Research Experiments? | [tree](artifacts/extra/expbench/trace/exploration_tree.html) |

## Provenance & quality

Each ARA was compiled from a source paper and its accompanying code; the content is grounded to the source paper (claims, figures, and tables trace back to the original). A subset additionally passed SEAL structural and cross-layer validation. These artifacts are reconstructions for research and evaluation purposes; consult the original papers and their licenses for authoritative results.

## Benchmarks

The `paperbench`, `rebench`, and `speedrun` artifacts correspond to the ARA evaluation benchmark. The `extra` artifacts are additional complete ARAs beyond the benchmark set.

## License

Content is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
