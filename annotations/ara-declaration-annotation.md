# Annotating ARAs with declarations

**Date:** 2026-10-07

Status: maintained annotation guidance. [Batch 1](batch-1-track1-reviewed.md) added specs for `paperbench/self-expansion` C01 and `paperbench/stay-on-topic-with-classifier-free-guidance` C04. [Batch 2](batch-2-subjects.md) added `subjects/mmdfuse` C12. These are exposed historical/development outputs, not new RQ1 extraction successes or independently adjudicated source-fidelity labels.

## TL;DR

`aratest` reads reported numbers from an ARA's existing evidence files. Its `aratest/spec.yaml` format version 7 supplies metric and axis meaning, canonical labels, and the properties each claim asserts, without copying evidence values. Specs already exist in the three artifacts listed above. New authoring must preserve the full assertion before selecting relations, keep unsupported claims in the selected-claim ledger, and separate executable checks from independent fidelity review. Collection, corpus regeneration, and fresh experiment families require separate authorization and resource caps.

## What `aratest` parses from the ARA

The ARA schema (`skills/compiler/references/ara-schema.md` in `ARA-Labs/Agent-Native-Research-Artifact`) records reported numbers in four places. `aratest` reads them where they are.

| Source | ARA location | Historical parser census, not a current acceptance gate |
|---|---|---|
| Tables | `evidence/tables/*.md` | 291 of 311 files parse with `aratest.evidence.parse_table_md`; 10,629 numeric cells |
| Figures | `evidence/figures/*.md` data tables | 145 of 183 data tables parse; 2,627 numeric cells, 1,828 of them approximate |
| Text | each claim's `Sources` field in `logic/claims.md` | Absent: the corpus predates the field |
| Runs | `evidence/results/*.md` run tables | Absent |

The historical census recorded 1,299 table cells and 402 figure cells with digits that did not parse, plus 20 rejected tables. Those counts describe the earlier parser and input snapshot; do not present them as the current runtime's behavior. Parse the actual pinned inputs before authoring, retaining any current failures.

Parsed cells carry table-local coordinates. 84% of table cells sit on an axis the parser can only name `column`, valued by header text. The metric may be a header, a caption, a `measure` axis, or a section heading. Axis names vary across files (`Method`, `Model`, `model`). The map in `spec.yaml` supplies this meaning. It never repeats a number.

Prose-only results need a source record that the installed parser can read. Preserve their exact quotation, units, scope, and source anchor in ordinary claim/evidence records. If the installed runtime cannot read or faithfully express them, retain the obligation with its reason rather than inventing evidence.

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

Write new files at format version 7. Legacy format support is a runtime compatibility detail, not permission to reuse a historical declaration under a different claim or source version.

## Inputs

| Input | Where | Use |
|---|---|---|
| The ARAs | Pinned `ARA-Labs/ara-paperbench` revision; `artifacts/{paperbench,rebench,speedrun,extra,subjects}/<id>/` | Annotation inputs, with exact included files and exposure recorded |
| Batch 1 authority | [Batch 1 report](batch-1-track1-reviewed.md), including original authority and corpus pin | Historical conversion, not automatic extraction or independent source review |
| MMD-FUSE spec | [Batch 2 report](batch-2-subjects.md), `artifacts/subjects/mmdfuse/aratest/spec.yaml` | Historical engineering target C12; C01 was not substituted for a different assertion |
| Shared authoring contract | [Pinned maintained contract](https://github.com/ARA-Labs/Agent-Native-Research-Artifact/blob/ebae6b6c5ddd0424e3e9c2ba80db357b4bda415f/skills/shared/property-authoring.md), loaded by all four compiler/research-manager variants | Source preservation, staged obligations, semantic revisions, and isolated ARA-only inputs |
| Relation and family catalogs | Installed `aratest.catalog` and its schemas | Allowed relations, domains, and separately authorized fresh-case families |

## Batches

Each batch is one set of commits on `feat/aratest-dev`, with a batch report.

1. **Retain the completed conversions.** Batch 1 ported the two reviewed binding sets without a model. Their historical authority and checks remain in the batch report; they are not independently reviewed source-fidelity results.
2. **Retain the research subject's identity.** Batch 2 added MMD-FUSE C12. It explicitly rejected applying a different source claim under C01 and did not add Simformer. Do not mark the original broader batch proposal complete.
3. **Enroll later authoring before outcomes.** Record source/ARA identities, claim IDs, exposure, ordering and selection rules, screening and effort limits, attempt/repair allowance, and stopping rule. Unsupported, missing, ambiguous, and failed claims remain in that fixed denominator.

## Instructions for the annotation agent

For each ARA:

1. Pin the workflow, model, catalog, tools, attempts, and allowed input view. For ARA-only extraction, use a materialized allowlisted view and a fresh context: retain preserved assertions, conditions, source quotations, raw evidence and neutral axis/label meaning; exclude the original source packet, generated specs, relation choices, executable operand mappings, check/repair feedback, reviewer answers, and exclusions reachable through linked records. Source-informed compiler authoring is a different output, not an independent extraction arm.
2. Read `PAPER.md`, `logic/claims.md`, and neutral linked evidence/experiments within that allowed view. Capture each exact assertion and every conjunct before relation selection. Resolve metric, units, direction, exact variant and baseline, scope, quantifier, aggregation, statistical unit, uncertainty commitment, and evidence headers. Do not merge fixed and adaptive methods or swap average and final accuracy.
3. Compare the whole assertion with the pinned relation schemas. If no faithful relation or evidence is available, keep the claim in the batch ledger with separate reasons for unsupported relation, missing evidence, unresolved meaning, approximation, or absent variance. Missing variance is never zero. A useful narrowed subclaim gets its own identity and does not discharge the full assertion.
4. For executable candidates, write evidence maps from actual parsed axes and canonical labels only for equivalent spellings. Include every supported required conjunct as a property. Compare the candidate's meaning with the captured assertion before execution; a holding check cannot justify omitted conjuncts or changed meaning.
5. Add fresh-case `families` only with separate authorization and resource caps. Reported-evidence authoring does not launch them automatically.
6. Fill supported `provenance`; retain richer source, workflow, initial-output, feedback, repair, and human-help history in linked authoring/batch records. Do not invent spec fields or copy evidence numbers into it.
7. Preserve original ARAs. Existing-artifact annotation changes only `aratest/spec.yaml`, with the selected-claim ledger and attempt history in the batch report. Compiler regeneration and live recording create separately versioned artifacts under the shared contract; they do not edit historical evidence to make checks hold.
8. Save every candidate and semantic revision under immutable identities. Link checks to the exact obligation, declaration, evidence, relation, and decision-policy versions. A revised method or scope must not inherit the old check.

## Checks before each commit

- `spec.yaml` loads with `aratest`'s format version 7 model; keep schema acceptance separate from semantic fidelity.
- Every evidence path exists and parses, renamed axes exist, and operand references resolve using the pinned public APIs.
- Claim identities map back to the selected source obligations; splitting claims does not inflate coverage.
- Supported relations and separately authorized family schemas validate. Load, bind, check, save, and replay executable reported-evidence candidates, retaining holds, violations, inconclusive outcomes, and operational failures.
- Run `ara check` and the artifact's own checks when available; otherwise record exactly what was not run. These are engineering checks, not independent source review.
- Retain initial and repaired outputs separately. Report semantic mismatch even when execution holds; keep unsupported obligations visible.

## Commits and reports

- One commit per ARA per batch, message `annotate(<ara-id>): <batch name>`.
- Each batch adds `annotations/<batch>.md` at the fork root: ARAs touched, claims declared, claims skipped with reasons, evidence files that failed to parse, the model and prompt used, and the check results.
- Commits are pushed only after the owner approves the batch.

## Independent review before reporting fidelity

RQ1 requires two qualified human source reviewers working independently and a separate independent adjudicator. They must not be the system developer or protocol author. AI review, historical authority conversions, and the production checker cannot replace them. Record expertise, independence, permitted source access, and active review time.

Hide candidates, checker outcomes, and repair answers while reviewers annotate source assertions. Lock source annotations before reviewing neutral compiled assertions and evidence, then lock those annotations before candidate review. Review source-to-ARA, ARA-to-declaration, and source-to-final fidelity separately, preserving both reviewers' judgments before adjudication. Record wrong variants, headers, omitted conjuncts, changed scope/aggregation/uncertainty, and unresolved cases.

No independent reviewers or no recoverable historical input means the corresponding fidelity result is unperformed. Do not reconstruct missing accepted outputs from corrected diagnostics. Release only independently reviewed, eligible declarations to downstream tests, preserving initial scores and correction history.

## Live recording and regenerated artifacts

The compiler and research-manager workflows load one shared authoring contract in their maintained upstream skill sources. The research manager stages obligations at its first recording opportunity without forcing crystallization; an obligation written after evidence is not preregistered. Semantic and decision-policy changes preserve immutable before/after identities and require a new check of the new version.

Keep regenerated artifacts, sources, claim/evidence correspondence, and compiler configuration separate from the original unmodified-ARA cohort. Live integration receives engineering smoke validation only; compiler regeneration is not evidence of live research-manager effectiveness. New collection and effectiveness studies still require their own prospective enrollment, authorization, reviewers, and caps.
