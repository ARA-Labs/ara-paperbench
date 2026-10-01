# Annotating ARAs with declarations

**Date:** 2026-09-30

Status: draft instructions, nothing annotated yet. Companion to [the refactor plan](package-design-review.md) (decisions 19 and 20, D7, Phase 3) and [the package and API plan](refactored-packages-and-api.md). A copy of this file is committed to the `ara-paperbench` fork with the first annotation batch, next to the data it produces.

## TL;DR

`aratest` reads an ARA's reported numbers by parsing the evidence files the ARA already has. It does not ask for a second copy. What parsing cannot recover is meaning: which header is the metric, what an unnamed column axis is, and which spellings name the same method. Each annotated ARA therefore gains one file, `aratest/spec.yaml` (format version 7). It holds a short map that gives parsed evidence that meaning, plus the properties each claim asserts. No ARA in the `ara-paperbench` fork has one yet. This plan fixes what an offline agent writes into the fork, in which order, and how each commit is checked. Nothing is committed to the fork except by following it.

## What `aratest` parses from the ARA

The ARA schema (`skills/compiler/references/ara-schema.md` in `ARA-Labs/Agent-Native-Research-Artifact`) records reported numbers in four places. `aratest` reads them where they are.

| Source | ARA location | State in the pinned corpus (32 ARAs) |
|---|---|---|
| Tables | `evidence/tables/*.md` | 291 of 311 files parse with `aratest.evidence.parse_table_md`; 10,629 numeric cells |
| Figures | `evidence/figures/*.md` data tables | 145 of 183 data tables parse; 2,627 numeric cells, 1,828 of them approximate |
| Text | each claim's `Sources` field in `logic/claims.md` | Absent: the corpus predates the field |
| Runs | `evidence/results/*.md` run tables | Absent |

Parser gaps to close in `aratest`, not in the ARAs: 1,299 table cells and 402 figure cells contain digits but do not parse (for example `~0.05`, because `~` is not yet an approximate marker), and 20 tables are rejected, half of them for sub-tables with different axes.

Parsed cells carry table-local coordinates. 84% of table cells sit on an axis the parser can only name `column`, valued by header text. The metric may be a header, a caption, a `measure` axis, or a section heading. Axis names vary across files (`Method`, `Model`, `model`). The map in `spec.yaml` supplies this meaning. It never repeats a number.

Results stated only in prose cannot be checked on this corpus, because no file records them. ARAs written to the current schema record them in `Sources`. Their map format is settled when the first such ARA is annotated.

## What gets written

Each annotated ARA gains `aratest/spec.yaml`. Nothing else in the ARA changes, and standard ARA readers ignore the `aratest/` directory.

```yaml
format_version: 7

evidence:                          # how to read parsed evidence; one entry per file used
  evidence/tables/table1_main_results.md:
    metric: {axis: measure}        # the metric is a parsed axis; or {name: AN} for a constant
    axes: {Method: method, group: dataset}
  evidence/figures/figure3_accuracy_vs_budget.md:   # illustrative figure data table
    metric: {name: accuracy}
    axes: {Budget: budget, column: method}

labels:                            # spellings that name the same value
  method: {"SEMA (ours)": SEMA}

claims:
  - claim_id: C01                  # must exist in logic/claims.md
    properties:                    # one or more; the claim holds only if all hold
      - kind: consistency
        metric: AN
        treatment: {method: SEMA}
        baseline: {method: ADAM}
        comparator: gt                 # required; "higher is better" is not universal
        over: dataset
        in_scope: [CIFAR-100, 5-Task IN-R, ImageNet-A]
      - kind: consistency
        metric: AN
        treatment: {method: SEMA}
        baseline: {method: DualPrompt}
        comparator: gt
        over: dataset
        in_scope: [CIFAR-100, 5-Task IN-R, ImageNet-A]
    provenance:                    # optional in the schema, required by this plan
      author: annotation-agent
      model: <model id>
    families:                      # optional
      - family_id: seed_resampling
        version: "1"
        params: {n_seeds: 3}
```

- **`evidence`** lists only the files that some property uses. `metric` says where the metric comes from. `axes` renames parsed axes to names that are canonical across the ARA. A file without an entry contributes nothing.
- **`labels`** merges spellings of the same value across files. Leave it out when spellings already agree.
- **`properties`**: each item is one catalog relation. `kind` selects it, and its operands address numbers by `metric` and canonical coordinates, never by file. Several properties on one claim replace the old `conjunction` kind, and a failure names the specific property.
- **`families`** lists experiments that can generate fresh cases. A claim without `families` is checked on reported numbers only.
- The file holds no numbers copied from evidence, no orderings, results, verdicts, or execution settings. `aratest` computes any ordering it needs from the parsed numbers, and takes precision from the decimals shown and from approximate markers.

Format versions 1–6 (one `property`, old kind names, label addressing) stay readable only so retained records replay. New files are written at version 7, which `aratest` defines in refactor plan Phase 3, so annotation batches wait for that reader.

## Inputs

| Input | Where | Use |
|---|---|---|
| The ARAs | `ara-paperbench` fork, branch `feat/aratest-dev`, `artifacts/{paperbench,rebench,speedrun,extra}/<id>/` (32 ARAs) | Annotation targets |
| Reviewed Track 1 authority | `ara/src/eval3-track1-authority/` in this repository: reviewed `consistency` bindings for `paperbench/self-expansion` C01 (6 baselines, `table1_main_results`) and `paperbench/stay-on-topic-with-classifier-free-guidance` C04 (8 baselines, `table2_codegen_humaneval_temp02`), pinned to corpus commit `62e9b54b` | Batch 1, converted without a model |
| MMD-FUSE and Simformer ARAs | Zip archives under `ara/evidence/track2_joint_admission_2026-09-13/` in this repository; not in the fork | Batch 2 |
| MMD-FUSE shared-property spec | `ara/evidence/shared_property_328/contract/spec.yaml` (format version 5, MMD-FUSE C01) | Batch 2 |
| Relation and family catalogs | `aratest.catalog` (refactor plan §6.3) | The allowed `kind` and `family_id` values and their schemas |

## Batches

Each batch is one set of commits on `feat/aratest-dev`, with a batch report.

1. **Port the reviewed Track 1 claims.** The reviewed bindings already use the parser's coordinates (`[["Method", "SEMA"], ["measure", "AN"]]`). For each of the two ARAs, write the `evidence` entry for the one table its bindings use, and write each binding as one `consistency` property. No model is involved. Check that `audit_scope` and the new relation give the same verdicts on the same table; this is the Phase 3 parity gate.
2. **Add the research subjects.** Unpack the MMD-FUSE and Simformer ARAs from their retained archives into the fork under `artifacts/subjects/<id>/`. Declare MMD-FUSE C01 (from the shared-property spec) and C12 with a `seed_resampling` binding matching retained record T-MF1, which Phase 5 demonstrates. Simformer C07 gets the same binding, matching T-SF1. Other subject claims follow batch 3.
3. **Annotate everything else**, following the instructions below.

## Instructions for the annotation agent

For each ARA:

1. Read `PAPER.md`, `logic/claims.md`, and `logic/experiments.md`.
2. For each claim, decide whether catalog relations express it over numbers the ARA's evidence files contain.
   - If not, because no relation fits or the numbers are only in prose, write nothing for that claim and record the reason in the batch report. Do not stretch a relation to fit.
   - If so, write the `evidence` entries for the files those numbers come from, using the parsed axes `aratest` reports for each file. Add `labels` only where the same value is spelled differently across those files. Then write the claim's `properties`.
3. Add `families` only when a catalog family would produce cases that a declared relation can check, and the ARA's code and data make that experiment plausible. Choose parameters from the family's schema; do not invent parameters.
4. Fill `provenance` for every claim.
5. Do not edit any file outside `aratest/`, and do not copy numbers into `spec.yaml`.

## Checks before each commit

- `spec.yaml` loads with `aratest`'s model at format version 7.
- Every `evidence` path exists and parses, and every axis it renames exists in the parsed file.
- Every `claim_id` exists in the ARA's `logic/claims.md`.
- Every `kind` routes to a catalog relation, every property's operands resolve to at least one parsed number, and every `family_id` names a catalog family with valid parameters.
- The ARA's own checks still pass: `ara check` and the fork's `_seal_tests.py`, if present, accept the added `aratest/` directory.
- The diff touches only the ARA's `aratest/spec.yaml`.

## Commits and reports

- One commit per ARA per batch, message `annotate(<ara-id>): <batch name>`.
- Each batch adds `annotations/<batch>.md` at the fork root: ARAs touched, claims declared, claims skipped with reasons, evidence files that failed to parse, the model and prompt used, and the check results.
- Commits are pushed only after the owner approves the batch.

## Open questions

1. **Review of agent annotations.** Provenance records the agent. Decide whether a researcher reviews batch 3 before its results are reported, and if so, record it as `provenance.reviewed_by`.
2. **Corpus pin.** This repository reads the corpus as the submodule `corpus/ara-paperbench`, which points at `github.com/AmberLJC/ara-paperbench` at commit `62e9b54b`. That is also the fork's current `main`. After batch 1, the submodule should point at the `ARA-Labs` fork's `feat/aratest-dev`, and the authority file's `corpus_commit` should be updated with it.
3. **Subject placement.** `artifacts/subjects/` is a new category in the fork. The alternative is `artifacts/extra/`.
4. **`research-manager` integration.** New ARAs should get `spec.yaml` while the research happens. The `research-manager` skill needs an instruction to write it; that change lives with the skill, not here.
