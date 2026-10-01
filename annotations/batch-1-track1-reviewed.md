# Annotation batch 1: the reviewed Track 1 bindings

Batch 1 of the annotation plan (`annotations/ara-declaration-annotation.md`). It ports the 14 reviewed `consistency` bindings of DissClaimer's Track 1 authority (`ara/src/eval3-track1-authority/`, pinned to corpus commit `62e9b54b`) into `aratest/spec.yaml` format version 7. No model was used: each binding was converted by hand from the parser coordinates it already uses.

## ARAs touched

| ARA | Evidence entry | Claims declared | Properties |
|---|---|---|---|
| `paperbench/self-expansion` | `evidence/tables/table1_main_results.md` | C01 | 6 |
| `paperbench/stay-on-topic-with-classifier-free-guidance` | `evidence/tables/table2_codegen_humaneval_temp02.md` | C04 | 8 |

Each commit adds only that ARA's `aratest/spec.yaml`.

## The evidence maps

- **`self-expansion`, Table 1.** The parser reads the axes `Method`, `group`, and `measure`. The metric is the `measure` axis (`AN` or `Ā`). `Method` is renamed `method` and `group` is renamed `dataset`.
- **`stay-on-topic-with-classifier-free-guidance`, Table 2.** The parser reads the axes `γ`, `group`, and `measure`. Every cell reports pass@k, so the metric is the constant `pass@k`. `γ` is renamed `gamma`, `group` is renamed `model`, and `measure` is renamed `k`, valued `k=1`, `k=10`, and `k=100`. The metric is not read from `measure`: a reviewed Track 1 control site on this table compares pass@10 with pass@1, and a `consistency` property compares one metric on both sides.
- No `labels`: each ARA maps one file, so no value is spelled two ways.

## Claims declared

- **`self-expansion` C01**: SEMA beats each of ADAM, DualPrompt, FT Adapter, InfLoRA, L2P, and SimpleCIL on `AN` (`gt`) at every dataset (CIFAR-100, 5-, 10-, and 20-Task IN-R, ImageNet-A, VTAB). One property per baseline, in the reviewed file's order.
- **`stay-on-topic-with-classifier-free-guidance` C04**: on pass@k at `k=1`, guidance 1.1, 1.25, and 1.5 each beat 1.0; at `k=100`, guidance 1.0 beats each of 1.1, 1.25, 1.5, 1.75, and 2.0 (`gt`), for every CodeGen model (2B, 350M, 6B). Shared pins sit in `where`.

Provenance names the authority (`author: eval3-track1-authority`) and no model.

## Claims skipped

Batch 1 declares only the two reviewed claims. Every other claim of these two ARAs, and every other ARA, is left for batch 3; none was assessed here.

## Evidence files that failed to parse

None. Both mapped tables parse with every numeric cell read (0 skipped digit cells).

## Checks

Run with `aratest` 0.5.23 (DissClaimer `origin/main` at `4ce78cb6`) on the local branch `annotation-batch-1`:

- Both files load with `load_spec` as format version 7.
- `AraArtifact.load` reads each ARA: every claim ID exists in `logic/claims.md`; each evidence path exists and parses; every renamed axis is a parsed axis. Self-expansion reads 96 measurements and stay-on-topic 54.
- `check_spec` reports 0 problems: every `kind` routes to the installed `consistency` relation, and every property binds, so all operands resolve to parsed numbers.
- No `families` are declared.
- `ara check` was not run: the `ara` CLI is not installed on the annotating machine. Neither ARA has a `_seal_tests.py`.
- The diff of each ARA commit touches only its `aratest/spec.yaml`.

The DissClaimer Track 1 parity gate (`dissclaimer-eval track1-parity`) checks the 14 declarations against an independent statement of their operands and against `audit_scope` on the same tables.
