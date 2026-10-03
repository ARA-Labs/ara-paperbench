---
title: 'MMD-FUSE: Learning and Combining Kernels for Two-Sample Testing Without Data Splitting'
authors:
- Felix Biggs
- Antonin Schrab
- Arthur Gretton
year: 2023
venue: NeurIPS
doi: arXiv:2306.08777
ara_version: '1.0'
domain: Statistics and kernel two-sample testing
keywords:
- MMD
- permutation testing
- kernel selection
- normalization
- power
- source correspondence
claims_summary:
- Permutation-invariant parameter selection can reuse the pooled observations without sacrificing the
  null calibration of a permutation test.
- A soft maximum over kernel discrepancies corresponds to optimizing kernel weights subject to a divergence
  penalty from a prior.
- A positive pooled permutation-invariant normalizer lets kernel discrepancies share a scale without recomputing
  the normalizer for each label permutation.
- The paper proposes sufficient-power guarantees whose adaptation penalty depends on divergence from a
  fixed kernel prior.
- Signal spread across candidate kernels can reduce the divergence penalty in the paper’s sufficient condition
  compared with concentrating all weight on one kernel.
- Combining discrepancies into one statistic avoids the additional resampling stage used to calibrate
  an aggregation of separate tests.
- A global median distance can miss the local scale distinguishing well-separated mixture components.
- Competitive adaptive-kernel performance across selected datasets does not imply dominance over learned
  representations in every regime.
- Adding bandwidths can retain power once useful scales are represented in the particular reported perturbation
  experiment.
- The reported image-collection test detects a difference between the specified image collections under
  its selected protocol.
- Agreement with an aggregate result can coexist with a mismatch between executed code and a stated mathematical
  statistic.
abstract: 'Compiled summary: the paper combines permutation-invariant kernel selection with soft fusion
  of kernel discrepancies. This artifact represents its mathematical and empirical evidence, the pinned
  released implementation, and one completed local implementation reproduction. Paper/code temperature
  and other provenance gaps remain explicit.'
source_commit: 558e3999db1a2f6e3668b7539b48ef5ee3f09538
source_conflict_status: unresolved; paper and released implementation separately attributed
admission_status: T-MF1 admitted for registered generator1 and generator2 only
local_reproduction_scope: one pinned author-code mixture point; no source correction or new run during
  compilation
---

# MMD-FUSE research artifact

The paper, released code and local observation remain separately attributed. The scientific claim statuses are bounded by their Evidence basis and Conditions; no local result is promoted into paper-wide validation. The original compilation left the protocol/admission choice in issue [#281](https://github.com/ARA-Labs/DissClaimer/issues/281). This derived revision records its released-code choice below.

## Layer Index

### logic

| File |
| --- |
| [logic/claims.md](logic/claims.md) |
| [logic/concepts.md](logic/concepts.md) |
| [logic/experiments.md](logic/experiments.md) |
| [logic/problem.md](logic/problem.md) |
| [logic/related_work.md](logic/related_work.md) |
| [logic/solution/algorithm.md](logic/solution/algorithm.md) |
| [logic/solution/constraints.md](logic/solution/constraints.md) |
| [logic/solution/coverage.md](logic/solution/coverage.md) |

### src

| File |
| --- |
| [src/artifacts.md](src/artifacts.md) |
| [src/environment.md](src/environment.md) |
| [src/execution/grounding.md](src/execution/grounding.md) |
| [src/execution/p1_mixture_point.py](src/execution/p1_mixture_point.py) |
| [src/execution/transcription.json](src/execution/transcription.json) |

### data

| File |
| --- |
| [data/dataset.md](data/dataset.md) |

### trace

| File |
| --- |
| [trace/exploration_tree.yaml](trace/exploration_tree.yaml) |

### evidence

| File |
| --- |
| [evidence/README.md](evidence/README.md) |
| [evidence/author_arrays.json](evidence/author_arrays.json) |
| [evidence/definition1-normalizer-page6.png](evidence/definition1-normalizer-page6.png) |
| [evidence/distinct-pairs-definition-page3.png](evidence/distinct-pairs-definition-page3.png) |
| [evidence/experiment-lambda-page8.png](evidence/experiment-lambda-page8.png) |
| [evidence/figures/figure1.md](evidence/figures/figure1.md) |
| [evidence/figures/figure1.png](evidence/figures/figure1.png) |
| [evidence/figures/figure2.md](evidence/figures/figure2.md) |
| [evidence/figures/figure2.png](evidence/figures/figure2.png) |
| [evidence/figures/figure3.md](evidence/figures/figure3.md) |
| [evidence/figures/figure3.png](evidence/figures/figure3.png) |
| [evidence/figures/figure4.md](evidence/figures/figure4.md) |
| [evidence/figures/figure4.png](evidence/figures/figure4.png) |
| [evidence/figures/figure5.md](evidence/figures/figure5.md) |
| [evidence/figures/figure5.png](evidence/figures/figure5.png) |
| [evidence/figures/figure6.md](evidence/figures/figure6.md) |
| [evidence/figures/figure6.png](evidence/figures/figure6.png) |
| [evidence/figures/figure7.md](evidence/figures/figure7.md) |
| [evidence/figures/figure7.png](evidence/figures/figure7.png) |
| [evidence/figures/figure8.md](evidence/figures/figure8.md) |
| [evidence/figures/figure8.png](evidence/figures/figure8.png) |
| [evidence/logs/log_pointers.md](evidence/logs/log_pointers.md) |
| [evidence/logs/stderr.log](evidence/logs/stderr.log) |
| [evidence/logs/stdout.log](evidence/logs/stdout.log) |
| [evidence/paper.pdf](evidence/paper.pdf) |
| [evidence/proofs/calibration.md](evidence/proofs/calibration.md) |
| [evidence/proofs/fusion.md](evidence/proofs/fusion.md) |
| [evidence/proofs/page24.png](evidence/proofs/page24.png) |
| [evidence/proofs/page25.png](evidence/proofs/page25.png) |
| [evidence/proofs/page27.png](evidence/proofs/page27.png) |
| [evidence/proofs/page31.png](evidence/proofs/page31.png) |
| [evidence/proofs/page32.png](evidence/proofs/page32.png) |
| [evidence/proofs/page34.png](evidence/proofs/page34.png) |
| [evidence/proofs/page35.png](evidence/proofs/page35.png) |
| [evidence/proofs/page4.png](evidence/proofs/page4.png) |
| [evidence/proofs/page7.png](evidence/proofs/page7.png) |
| [evidence/proofs/page8.png](evidence/proofs/page8.png) |
| [evidence/proofs/power.md](evidence/proofs/power.md) |
| [evidence/proofs/theorem01.md](evidence/proofs/theorem01.md) |
| [evidence/proofs/theorem02.md](evidence/proofs/theorem02.md) |
| [evidence/proofs/theorem03.md](evidence/proofs/theorem03.md) |
| [evidence/proofs/theorem04.md](evidence/proofs/theorem04.md) |
| [evidence/proofs/theorem05.md](evidence/proofs/theorem05.md) |
| [evidence/proofs/theorem06.md](evidence/proofs/theorem06.md) |
| [evidence/proofs/theorem07.md](evidence/proofs/theorem07.md) |
| [evidence/proofs/theorem08.md](evidence/proofs/theorem08.md) |
| [evidence/proofs/theorem09.md](evidence/proofs/theorem09.md) |
| [evidence/proofs/theorem10.md](evidence/proofs/theorem10.md) |
| [evidence/proofs/theorem11.md](evidence/proofs/theorem11.md) |
| [evidence/proofs/theorem12.md](evidence/proofs/theorem12.md) |
| [evidence/proofs/theorem13.md](evidence/proofs/theorem13.md) |
| [evidence/proofs/theorem14.md](evidence/proofs/theorem14.md) |
| [evidence/proofs/theorem_index.md](evidence/proofs/theorem_index.md) |
| [evidence/results/author_result_index.md](evidence/results/author_result_index.md) |
| [evidence/results/environment.lock.txt](evidence/results/environment.lock.txt) |
| [evidence/results/final-result.json](evidence/results/final-result.json) |
| [evidence/results/local_run.md](evidence/results/local_run.md) |
| [evidence/results/preregistered-protocol.json](evidence/results/preregistered-protocol.json) |
| [evidence/results/repetitions.jsonl](evidence/results/repetitions.jsonl) |
| [evidence/results/result.json](evidence/results/result.json) |
| [evidence/source_bibliography.txt](evidence/source_bibliography.txt) |
| [evidence/source_conflicts.md](evidence/source_conflicts.md) |
| [evidence/source_manifest.json](evidence/source_manifest.json) |
| [evidence/tables/table1.md](evidence/tables/table1.md) |
| [evidence/tables/table1.png](evidence/tables/table1.png) |
| [evidence/upstream_tree.json](evidence/upstream_tree.json) |

| [level2_report.json](level2_report.json) |

## Derived released-code admission

This revision adds the separately attributed experimental target T-MF1. The original claim blocks remain source-attributed; admission does not certify their theory, comparisons, or paper temperature. See [the full retained report](evidence/admission/report.json) and [copied public runs](evidence/admission/public-runs.zip).

The seed-43 cell produced 47/200 rejections (0.235), exceeding the original band edge 0.23 by 0.005. The G1 `holds` verdict refers only to the preregistered finite two-treatment mean 0.2075. It does not say every seed reproduces or establish unrestricted seed robustness. The band and reducer were not widened. Seed-42 baseline reproduction, runtime and source exposure checks stand independently.

**Sources**: [result] [retained family report](evidence/admission/report.json) «"rejection_proportion":0.235» and «"value":0.2075»; [input] [frozen original band](evidence/admission/frozen-protocol.json).
