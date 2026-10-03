# Annotation batch 2: the MMD-FUSE research subject

Batch 2 of the annotation plan (`annotations/ara-declaration-annotation.md`), as scoped by DissClaimer issue #405 (item B1): the MMD-FUSE ARA only. It adds the ARA under `artifacts/subjects/mmdfuse/`, unpacked unchanged from DissClaimer's retained archive `ara/evidence/track2_joint_admission_2026-09-13/mmdfuse/mmdfuse-derived-candidate.zip` (sha256 `3c9f292d489670f8cc11a90d91d7e79a05fa32d0e04e8bb372823e4514f31e4b`), and declares claim C12 in `aratest/spec.yaml` format version 7. The declaration was translated by hand, with Claude (`claude-opus-5-5`), from the frozen T-MF1 protocol; no model wrote it from the ARA's prose.

## ARAs touched

| ARA | Evidence entries | Claims declared | Properties | Families |
|---|---|---|---|---|
| `subjects/mmdfuse` | none | C12 | 1 | 1 |

Two commits: one imports the ARA unchanged, one adds only `aratest/spec.yaml`.

## Claims declared

**C12** ("Attributed experimental target T-MF1"): the mixture-cell rejection proportion (n=m=500, released code at `558e399`, reference `jax_seed` 42, reported 0.18) stays in the engineering band when only the seed changes.

- Property: `invariant` on `rejection_proportion`, statistic `mean` over the reference and treatment runs, band [0.13, 0.23] (the protocol's predeclared absolute tolerance of 0.05). A `paired_shift` control `labels` must decrease by at least 0.05 and land in [0, 0.10], with the reference in [0.13, 0.23]. These are the frozen `control-rule.json` values (`maximum_control` 0.10, `minimum_drop` 0.05, `reference_band`), and the same declaration as DissClaimer's saved-result parity domain for T-MF1.
- Family: `seed_resampling` version 1, `n_seeds: 2` (the reference and one other setting, as T-MF1's generator 1 ran seeds 42 and 43), `repetitions: 1`, and one negative control `labels` (a label permutation at the reference seed).
- Provenance: the T-MF1 record (`mmdfuse.T-MF1-engineering-band.v1`), model `claude-opus-5-5`.

## Claims skipped

- **C01** ("Pooled invariance permits reuse of all observations"). The plan names "MMD-FUSE C01 (from the shared-property spec)". That spec declares a different claim under the same ID: a narrowed power ordering, MMD-FUSE above MMD-Median at n=500. This ARA's C01 is a mathematical statement proved in E01, with no number in the evidence that a catalog relation could check. Declaring the ordering under this C01 would test something the claim does not say, so nothing is written for it.
- **C02–C11**: left for batch 3; not assessed here.
- **Simformer** (C07, matching T-SF1): part of the plan's batch 2, but outside #405's B1; not added.

## Evidence files that failed to parse

None mapped. The spec maps no evidence: `invariant` reads experiment cases, not reported numbers.

## Checks

Run with `aratest` and `dissclaimer` 1.0.3:

- `spec.yaml` loads at format version 7; `check_spec` reports no problem.
- C12 exists in `logic/claims.md`; `invariant` routes to the catalog relation; the domain validates.
- The continuous service's binding plan lists the C12 `seed_resampling` binding as runnable, with nothing unschedulable, skipped, or without families.
- `aratest test artifacts/subjects/mmdfuse --no-records` exits 4: C12 is undecided (`missing_evidence`) before any experiment; C01–C11 are undeclared.
- `ara check` was not run: the `ara` CLI is not installed on the annotation host. The fork has no `_seal_tests.py`.

## Demonstration run

`aratest continuous start artifacts/subjects/mmdfuse --agent openhands --run-usd 1.0 --max-runs 1 --run-timeout 7200`, with model `gpt-6-luna`, in a clean environment holding only the `aratest` and `dissclaimer` 1.0.3 wheels. The agent installed the ARA's pinned environment (Python 3.9.23, JAX and jaxlib 0.4.6), ran the three arms, and published a complete report: seed 42 gave 0.18, seed 43 gave 0.235, and the label control gave 0.075, the retained T-MF1 generator-1 values. It cost $0.067 over 44 minutes. With only `aratest` installed, `aratest test --claim C12 --results report.json` reports C12 holds (mean 0.2075).
