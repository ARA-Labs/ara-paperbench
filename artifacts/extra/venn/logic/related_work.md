# Related Work

## RW01: Bonawitz et al., 2019 (Google FL at Scale)
- **DOI**: MLSys 2019
- **Type**: baseline
- **Delta**:
  - What changed: Venn replaces Google's job-driven random client sampling with contention-aware IRS scheduling.
  - Why: Random matching fails under resource contention; scheduling delay is ignored.
- **Claims affected**: C01, C02
- **Adopted elements**: CL system model (check-in/dispatch/report lifecycle); overcommit design pattern delegated to jobs.

## RW02: Huba et al., 2022 (Meta Papaya)
- **DOI**: MLSys 2022
- **Type**: baseline
- **Delta**:
  - What changed: Venn replaces centralized random client-to-job matching with IRS + tier-based matching.
  - Why: Centralized random matching is suboptimal under contention.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Centralized resource manager architecture that sits above all CL jobs.

## RW03: Paulik et al., 2021 (Apple FL Infrastructure)
- **DOI**: arXiv:2102.08503
- **Type**: baseline
- **Delta**:
  - What changed: Venn uses a centralized scheduler vs. Apple's client-driven sampling from a job list.
  - Why: Client-driven sampling cannot implement contention-aware cross-job scheduling.
- **Claims affected**: C01
- **Adopted elements**: Concept of per-job device eligibility requirements.

## RW04: Lai et al., 2021b (Oort)
- **DOI**: OSDI 2021
- **Type**: bounds
- **Delta**:
  - What changed: Venn extends single-job client selection to multi-job resource scheduling; adds scheduling delay optimization.
  - Why: Oort assumes sufficient devices are always available for a single job; it does not model inter-job contention.
- **Claims affected**: C02, C03
- **Adopted elements**: FedScale device traces (Lai et al., 2021a) used for evaluation; participant selection based on system utility.

## RW05: Lai et al., 2021a (FedScale Benchmark)
- **DOI**: arXiv:2105.11367
- **Type**: imports
- **Delta**:
  - What changed: FedScale provides the 180M-item device availability and hardware trace used in Venn's evaluation.
  - Why: Real-world trace needed to emulate diurnal availability and hardware heterogeneity.
- **Claims affected**: C01, C04
- **Adopted elements**: Device availability trace; hardware profile data; simulation framework.

## RW06: Balakrishnan et al., 2022 (Diverse Client Selection)
- **DOI**: ICLR 2022
- **Type**: bounds
- **Delta**:
  - What changed: Venn addresses multi-job resource contention; Balakrishnan et al. optimize participant diversity for a single job.
  - Why: Submodular client selection ignores scheduling delay and inter-job competition.
- **Claims affected**: C02
- **Adopted elements**: Motivation for participant diversity in CL training.

## RW07: Even et al., 1975 (MCF Complexity)
- **DOI**: FOCS 1975
- **Type**: bounds
- **Delta**:
  - What changed: Venn acknowledges the NP-hardness of the exact IRS formulation and proposes a tractable heuristic.
  - Why: Exact integer MCF is computationally infeasible at CL scale.
- **Claims affected**: C04
- **Adopted elements**: Complexity lower bound justifying the heuristic approach.

## RW08: Garey et al., 1976 (Flowshop Scheduling)
- **DOI**: Mathematics of Operations Research, 1976
- **Type**: imports
- **Delta**:
  - What changed: Venn applies the SRPT-style insight (smallest remaining demand first) within job groups, citing Garey et al. as justification.
  - Why: Proven effectiveness of priority-based scheduling for minimizing average completion time.
- **Claims affected**: C02
- **Adopted elements**: Smallest-remaining-demand-first ordering principle for intra-group scheduling.

## RW09: Wang et al., 2023 (Flint)
- **DOI**: MLSys 2023
- **Type**: imports
- **Delta**:
  - What changed: Venn uses the log-normal device response time model from Wang et al. for tier speed-up factor computation.
  - Why: Empirically validated distribution model for CL device response times.
- **Claims affected**: C03
- **Adopted elements**: Log-normal response time distribution; 95th-percentile tail latency metric.

## RW10: He et al., 2023 (GlueFL)
- **DOI**: MLSys 2023
- **Type**: bounds
- **Delta**:
  - What changed: Venn manages scheduling delay at the multi-job level; GlueFL optimizes bandwidth for a single job via model masking and client sampling.
  - Why: Single-job response collection time optimization is insufficient at scale.
- **Claims affected**: C01, C03
- **Adopted elements**: Motivation for straggler mitigation in CL response collection.
