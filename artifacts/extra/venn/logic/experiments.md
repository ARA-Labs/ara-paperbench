# Experiments

## E01: End-to-End JCT Improvement Across Five Workloads
- **Verifies**: C01
- **Setup**:
  - Model: ResNet-18 (He et al., 2016) and MobileNet-V2 (Sandler et al., 2018) for real experiments; simulation uses job demand traces from Figure 8b
  - Hardware: Event-driven simulator (large scale); real CL testbed (small scale)
  - Dataset: FEMNIST (Cohen et al., 2017) for real experiments; FedScale device traces (Lai et al., 2021a) + AI Benchmark (Ignatov et al., 2019) for simulation
  - System: 50 concurrent CL jobs (simulation); 20 concurrent jobs (real); Poisson arrivals with 30-min average inter-arrival; 5 workload types: Even (all jobs), Small (below-average demand), Large (above-average demand), Low (below-average per-round demand), High (above-average per-round demand); device eligibility stratified into 4 categories (General, Compute-Rich, Memory-Rich, High-Performance)
- **Procedure**:
  1. Deploy Venn, FIFO, SRSF, and optimized random matching as schedulers in the event-driven simulator.
  2. Load the FedScale + AI Benchmark device traces to emulate heterogeneous device check-in patterns.
  3. Sample CL jobs from the job demand trace according to each workload scenario (Even/Small/Large/Low/High).
  4. Run each scheduler over the full job trace and record per-job JCT (scheduling delay + response collection time).
  5. Compute average JCT speedup for each scheduler relative to the optimized random matching baseline.
  6. Report speedups as in Table 1.
- **Metrics**: Average JCT speedup (×) over optimized random matching; reported per workload scenario and per scheduler.
- **Expected outcome**:
  - Venn achieves the highest JCT speedup across all five workload scenarios; SRSF generally outperforms FIFO; all schedulers outperform random matching
- **Baselines**: Optimized random matching (baseline=1.0×), FIFO, SRSF
- **Dependencies**: none

## E02: Ablation — Component-Level JCT Improvement Breakdown
- **Verifies**: C02, C03
- **Setup**:
  - Model: Same as E01 (simulation)
  - Hardware: Event-driven simulator
  - Dataset: FedScale + AI Benchmark device traces
  - System: Low workload and High workload scenarios from E01; compare four variants: Random (baseline), FIFO, Venn w/o sched (only matching + FIFO), Venn w/o match (only IRS scheduling), Venn (full)
- **Procedure**:
  1. Run Low workload with all four variants and record average JCT improvement over random matching.
  2. Run High workload with all four variants and record average JCT improvement over random matching.
  3. Report results as in Figure 11 (two bar charts).
- **Metrics**: Average JCT improvement (×) over random matching, per variant, per workload.
- **Expected outcome**:
  - Full Venn (matching + scheduling) outperforms each component in isolation; the matching component provides larger gains in demand-diverse workloads
- **Baselines**: Optimized random matching
- **Dependencies**: E01

## E03: Scheduling Overhead Scalability
- **Verifies**: C04
- **Setup**:
  - Model: N/A (scheduling overhead only, no ML training)
  - Hardware: Not specified in paper
  - Dataset: Synthetic; vary number of jobs from 100 to 1000 and number of job groups from 10 to 100
  - System: Venn scheduler invoked once (one-time trigger); measure wall-clock latency
- **Procedure**:
  1. Instantiate Venn's scheduler with varying numbers of jobs (up to 1000) and varying numbers of job groups (up to 100).
  2. Trigger one scheduling invocation and measure end-to-end latency in milliseconds.
  3. Plot latency vs. number of jobs and vs. number of job groups as in Figure 10.
- **Metrics**: Scheduling latency (ms); qualitative shape (should be sub-linear relative to job count consistent with max(O(m log m), O(n²))).
- **Expected outcome**:
  - Scheduling latency scales sub-linearly with job count, remaining practical for realistic cluster sizes
- **Baselines**: none
- **Dependencies**: none

## E04: Model Accuracy — Venn Does Not Hurt Convergence
- **Verifies**: C05
- **Setup**:
  - Model: ResNet-18 (He et al., 2016) and MobileNet-V2 (Sandler et al., 2018)
  - Hardware: Real CL testbed (small scale)
  - Dataset: FEMNIST (Cohen et al., 2017)
  - System: 20 concurrent CL jobs; real CL system execution; compare FIFO, SRSF, Venn
- **Procedure**:
  1. Deploy real CL system with 20 concurrent jobs targeting FEMNIST.
  2. Run FIFO, SRSF, and Venn schedulers for the same number of training rounds.
  3. Record average test accuracy across all jobs at each wall-clock time point.
  4. Plot average test accuracy vs. wall-clock time (in seconds) as in Figure 9.
- **Metrics**: Average test accuracy (y-axis 0.60–0.75) vs. wall-clock time (seconds, x-axis 0–25000s).
- **Expected outcome**:
  - All schedulers converge to the same final accuracy; Venn reaches target accuracy fastest
- **Baselines**: FIFO, SRSF
- **Dependencies**: E01

## E05: Fairness Knob (ε) Tradeoff
- **Verifies**: C06
- **Setup**:
  - Model: Simulation
  - Hardware: Event-driven simulator
  - Dataset: FedScale + AI Benchmark device traces; Even workload
  - System: Vary ε from 0 to large values; measure average JCT speedup (Figure 14a) and percentage of jobs meeting fair-share JCT (Figure 14b)
- **Procedure**:
  1. Run Venn with varying values of ε (0, 1, 2, and larger).
  2. For each ε, compute average JCT speedup over random matching.
  3. For each ε, compute the percentage of jobs with actual JCT ≤ Ti = M × sdi (fair-share JCT).
  4. Plot both metrics against ε.
- **Metrics**: Average JCT improvement (×) and percentage of jobs meeting fair-share JCT (%).
- **Expected outcome**:
  - Increasing ε trades off average JCT for fairness; JCT speedup decreases monotonically while fair-share fraction increases monotonically
- **Baselines**: Random matching (ε=0 equivalent)
- **Dependencies**: E01
