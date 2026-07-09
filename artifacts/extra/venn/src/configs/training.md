# Training Configuration

## Number of Target Participants per Round
- **Value**: 80% of target number must respond within deadline
- **Rationale**: Standard synchronous CL protocol requirement; ensures statistically representative aggregation.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.1 (CL jobs setup)

## Round Deadline
- **Value**: 5 min – 15 min (range, depending on round demand)
- **Rationale**: Balances device participation window with training throughput; deadline varies with job's per-round demand.
- **Search range**: Not specified
- **Sensitivity**: high — shorter deadlines increase scheduling delay as fewer devices can participate
- **Source**: §5.1 (CL jobs setup)

## Job Arrival Process
- **Value**: Poisson process with 30-minute average inter-arrival time
- **Rationale**: Models realistic deployment of CL jobs in a production system.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §5.1 (Workloads)

## Number of Concurrent Jobs (Simulation)
- **Value**: 50 jobs
- **Rationale**: Represents a mid-scale multi-job CL deployment for simulation evaluation.
- **Search range**: Varied in §5.5 ablation (up to ~1000 jobs for overhead study)
- **Sensitivity**: high — more jobs increase contention and make scheduling more critical
- **Source**: §5.1 (Workloads)

## Number of Concurrent Jobs (Real Testbed)
- **Value**: 20 jobs
- **Rationale**: Smaller scale limited by real testbed capacity.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §5.1 (Testbed)

## Device Eligibility Categories
- **Value**: 4 categories — General, Compute-Rich, Memory-Rich, High-Performance
- **Rationale**: Reflects real-world CL job hardware requirements; creates varied resource contention patterns.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §5.1 (Resources), Figure 8a

## Number of Device Tiers (V) for Matching
- **Value**: Default not precisely specified; Figure 13 shows V swept from 1 to multiple values
- **Rationale**: Increased granularity improves matching but increases scheduling delay; gains plateau beyond a certain V.
- **Search range**: 1 to several tiers (Figure 13)
- **Sensitivity**: medium — gains plateau after optimal V
- **Source**: §5.5 (Impact of number of tiers), Figure 13

## Fairness Knob (ε)
- **Value**: ε = 2 (used in starvation-prevention experiments)
- **Rationale**: At ε=2, 69% of jobs meet fair-share JCT; balances performance and fairness.
- **Search range**: 0 to ∞; ε=0 is pure IRS, ε→∞ is max-min fairness
- **Sensitivity**: high — JCT improvement decreases monotonically as ε increases
- **Source**: §4.4 (Starvation prevention), §5.5 (Impact of fairness knob), Figure 14

## Device Availability Averaging Window
- **Value**: 24 hours
- **Rationale**: Matches the diurnal period of device availability (Figure 2a); smooths intra-day fluctuations for robust scheduling of multi-day CL jobs.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §4.4 (Dynamic resource supply)

## Tail Latency Percentile for Tier Speed-Up
- **Value**: 95th percentile
- **Rationale**: Excludes failures and extreme stragglers; represents response collection time as the "worst case within normal operation."
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §4.3 (Device Matching)
