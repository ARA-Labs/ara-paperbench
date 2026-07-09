# System Architecture

## Overview

Venn is a standalone, centralized CL resource manager that operates as a layer above all CL jobs. It receives device check-ins and job resource requests, runs its scheduling and matching algorithms, and assigns each device to exactly one job per check-in event.

## Component Graph

```
[CL Job i]  ---(resource request: requirements + demand Di)---> [Venn Server]
[Edge Device] ---(check-in)---> [Venn Server]
[Venn Server] ---(assignment)---> [Edge Device]
[Edge Device] ---(participate)---> [CL Job i]
[CL Job i] ---(dispatch computation plan)---> [Edge Device]
[Edge Device] ---(report results)---> [CL Job i]
```

## Components

### 1. Request Handler
- **Purpose**: Receives resource requests from CL jobs and check-ins from devices.
- **Inputs**: Job resource request (device requirements: min CPU, memory, software version, data type; resource demand: $D_i$ devices per round). Device check-in (device ID, hardware profile, eligibility tags).
- **Outputs**: Updated job queue $J$; updated device pool $S$.
- **Key design choice**: Venn triggers re-scheduling on both job arrival and job completion events, not on a fixed polling interval.

### 2. Eligibility Mapper
- **Purpose**: Maps each job to its eligible device subset based on declared requirements.
- **Inputs**: Device hardware profiles (CPU score, memory score, software version, data availability); job requirements.
- **Outputs**: Eligibility function $f(J_i) = S_k$; job groups $G = \{G_1, \ldots, G_n\}$ (Resource-Homogeneous Job Groups).
- **Key design choice**: Devices are stratified into 4 hardware categories (General, Compute-Rich, Memory-Rich, High-Performance) based on CPU and memory thresholds (Figure 8a).

### 3. Contention-Aware Scheduler (IRS — Algorithm 1)
- **Purpose**: Determines a job scheduling order that minimizes average scheduling delay by accounting for overlapping device eligibility sets.
- **Inputs**: Job groups $G$; current device pool $S$; queue lengths per group.
- **Outputs**: Prioritized scheduling order per group; resource allocation plan $\{G_j[0], S'_j\}$ for each group.
- **Key design choice**: Two-level decomposition — intra-group sorting by ascending remaining demand; inter-group allocation starting from the scarcest group, then greedy reallocation based on queue-length-to-allocated-resource ratio.
- **Interaction**: Invoked by the Request Handler on job arrival/completion; outputs feed the Device Matcher.

### 4. Resource-Aware Device Matcher (Algorithm 2)
- **Purpose**: For each served job, decides whether to restrict device assignment to a single hardware tier to reduce response collection time.
- **Inputs**: Jobs currently being served; device tier assignments $\{S_1, \ldots, S_V\}$; per-tier speed-up factors $g_v = t_v / t_0$; ratio $c_i = T_{\text{resp}} / T_{\text{sched}}$ from previous round profile.
- **Outputs**: Refined device assignment $\{J_i, S'_j \cap S_u\}$ for each served job.
- **Key design choice**: Condition $1 + c_i > V + c_i g_u$ gates tier-based matching so it is applied only when the JCT reduction from faster response outweighs the JCT increase from higher scheduling delay (factor $V$). Randomized tier selection exposes jobs to device diversity.
- **Interaction**: Receives output of Algorithm 1; sends final assignments to the Request Handler for dispatch.

### 5. Time-Series Eligibility Database
- **Purpose**: Tracks historical device eligibility rates to handle diurnal availability patterns.
- **Inputs**: Real-time device check-in events with timestamps.
- **Outputs**: 24-hour averaged eligibility rates per device category for input to Algorithm 1.
- **Key design choice**: 24-hour averaging window makes the scheduler robust to intra-day fluctuations while remaining accurate for multi-day CL jobs.

### 6. Starvation Prevention Module
- **Purpose**: Applies the fairness knob $\varepsilon$ to prevent large jobs from being indefinitely starved.
- **Inputs**: Per-job usage time $t_i$; fair-share JCT $T_i = M \cdot sd_i$; fairness parameter $\varepsilon$.
- **Outputs**: Adjusted effective demand $d'_i$ and group queue lengths $q'_j$ fed to Algorithm 1.
- **Interaction**: Active in production deployments (all evaluation results in §5 use starvation prevention).

## Workflow (Per Scheduling Event)

1. Device checks in → Eligibility Mapper tags device → device added to pool $S$.
2. Job submits request → Request Handler queues job → Eligibility Mapper assigns to group $G_j$.
3. Contention-Aware Scheduler (Algorithm 1) runs → produces per-group scheduling order and initial allocation.
4. Resource-Aware Device Matcher (Algorithm 2) refines assignment for currently served jobs.
5. Assignments dispatched to devices → devices participate in assigned CL job.
6. Devices report results to CL job server directly (standard CL protocol, not through Venn).

## Responsibility Delegation
Venn explicitly delegates the following to individual CL jobs:
- Device fault tolerance and overcommit decisions
- Custom device selection criteria
- Privacy mechanisms (secure aggregation, differential privacy)
