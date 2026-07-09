# Problem Specification

## Observations

### O1: CL devices exhibit diurnal availability patterns
- **Statement**: Real-world CL device availability (devices that are charging and connected to WiFi) fluctuates significantly over time following a diurnal pattern. A real-world client availability trace (FedScale) encompasses 180 million trace items of device behavior over a week.
- **Evidence**: Figure 2a (diurnal availability plot); FedScale trace (Lai et al., 2021a)
- **Implication**: CL jobs cannot assume on-demand resource availability; they must wait for devices to become available, causing inherent scheduling delays.

### O2: Edge devices are highly heterogeneous in hardware capacity
- **Statement**: Edge devices in CL vary widely in CPU and memory capacities. For example, different models (MobileNet, VideoSR, MobileBERT) have different minimum hardware requirements, and many devices fall below the threshold for higher-demand models.
- **Evidence**: Figure 2b (CPU vs. Memory score scatter plot from AI Benchmark, Ignatov et al., 2019)
- **Implication**: Jobs can only use a subset of the available device pool; this subset varies per job based on hardware requirements.

### O3: Multiple CL jobs compete for overlapping device subsets
- **Statement**: CL jobs require specific device subsets (based on hardware, data, software version). These subsets can overlap, nest, or be mutually exclusive, creating complex multi-resource contentions.
- **Evidence**: Figure 3 toy example; Figure 8a (device stratification into 4 categories); §2.1
- **Implication**: Assigning a device to the wrong job wastes a scarce resource and prolongs another job's scheduling delay.

### O4: Scheduling delay is a significant and neglected JCT component
- **Statement**: When multiple CL jobs compete for devices, scheduling delay (time to acquire enough devices) grows substantially and can dominate total JCT. In experiments with 1–20 concurrent jobs (ResNet-18, 100 clients/round, FEMNIST), scheduling delay increases sharply as job count rises.
- **Evidence**: Figure 5 (JCT breakdown: scheduling delay vs. response collection time vs. job count); §2.3
- **Implication**: Optimizing only response collection time (as most prior work does) leaves major JCT savings on the table.

### O5: Existing CL resource managers all use random device-to-job matching
- **Statement**: Apple (Paulik et al., 2021), Meta (Huba et al., 2022), and Google (Bonawitz et al., 2019) use random matching in various forms (client-driven sampling, centralized random matching, job-driven random sampling).
- **Evidence**: §2.2; cited implementations
- **Implication**: Random matching is suboptimal under resource contention; it wastes scarce resources on jobs that have plentiful alternatives.

### O6: Resource contention degrades model accuracy
- **Statement**: Evenly partitioning a device pool across 1, 5, 10, and 20 concurrent CL jobs causes noticeable degradation in round-to-accuracy performance (ResNet-18, 100 clients/round, FEMNIST).
- **Evidence**: Figure 4 (average test accuracy vs. round for different numbers of jobs)
- **Implication**: Participant diversity is reduced under contention; smart scheduling can recover this diversity.

## Gaps

### G1: No existing CL resource manager accounts for inter-job resource contention
- **Statement**: Existing single-job optimizations (Oort, FedScale, GlueFL) assume sufficient devices are always available. Multi-job managers (Apple, Meta, Google) use random matching and do not model overlapping eligibility sets.
- **Caused by**: O3, O5
- **Existing attempts**: Client selection heuristics (Lai et al., 2021b; Balakrishnan et al., 2022); quantization (Reisizadeh et al., 2020)
- **Why they fail**: They operate at the single-job level and do not coordinate device assignment across competing jobs.

### G2: Scheduling delay is not modeled or minimized by prior work
- **Statement**: Prior work on CL optimization focuses exclusively on response collection time (model convergence, straggler mitigation). Scheduling delay is ignored as a JCT factor.
- **Caused by**: O4, O5
- **Existing attempts**: SRSF, FIFO — borrowed from cluster scheduling, not designed for CL's overlapping eligibility structure
- **Why they fail**: SRSF and FIFO do not account for the intersection structure of device eligibility sets across jobs; they can waste scarce resources on jobs that have abundant alternatives (Figure 3).

### G3: No efficient algorithm exists for multi-CL-job resource scheduling at planetary scale
- **Statement**: The exact multi-commodity flow (MCF) problem is NP-hard (Even et al., 1975). Even linear approximations are computationally infeasible given millions of devices and hundreds of jobs.
- **Caused by**: O1, O2, O3
- **Existing attempts**: ILP formulations (Appendix B of paper)
- **Why they fail**: Computational complexity is exacerbated by device scale and diverse eligibility constraints.

## Key Insight

- **Insight**: By grouping jobs with identical device requirements into Resource-Homogeneous Job Groups and decoupling the scheduling problem into (1) intra-group ordering by smallest-remaining-demand and (2) inter-group ordering by scarcity + queue-length ratio, Venn reduces the NP-hard MCF problem to a tractable max(O(m log m), O(n²)) heuristic that achieves near-optimal average JCT.
- **Derived from**: O3, O4, G1, G2, G3
- **Enables**: Contention-aware scheduling (IRS, Algorithm 1) and tier-based device matching (Algorithm 2) that jointly minimize average JCT across competing CL jobs.

## Assumptions

- A1: Devices check in to a centralized Venn scheduler before being assigned to jobs.
- A2: Each device is assigned to at most one CL job per check-in.
- A3: Device eligibility is deterministic and known at scheduling time (based on hardware capacity, data, software version).
- A4: Device response time distribution follows a log-normal distribution.
- A5: CL jobs are synchronous (each round requires a minimum fraction of target participants); asynchronous extensions are noted but not the primary focus.
- A6: Resource arrival patterns have a 24-hour periodicity (diurnal), making 24-hour averaging of eligibility rates robust.
