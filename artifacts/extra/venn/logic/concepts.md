# Concepts

## Job Completion Time (JCT)
- **Notation**: $\text{JCT}_i = T_{\text{sched},i} + T_{\text{resp},i}$
- **Definition**: The total time for a CL job to complete one training round. Composed of two parts: scheduling delay ($T_{\text{sched}}$) — the time from job request submission until sufficient devices are acquired — and response collection time ($T_{\text{resp}}$) — the time from task dispatch until the required fraction of devices submit training results.
- **Boundary conditions**: Applies per-round; multi-round JCT sums individual round JCTs. Not applicable to asynchronous CL jobs where rounds are not synchronized.
- **Related concepts**: Scheduling Delay, Response Collection Time, Collaborative Learning Job

## Scheduling Delay
- **Notation**: $T_{\text{sched},i} = \max_s (x_{ij} \cdot t_s)$ where $x_{ij}=1$ if device $s$ is assigned to job $J_i$
- **Definition**: The time elapsed from when a job submits a resource request to when it has collected sufficient devices to begin computation. Determined by the arrival time of the last needed device under the scheduling assignment.
- **Boundary conditions**: Dominates JCT when resource contention is high (supply < demand). Negligible when devices are plentiful.
- **Related concepts**: Job Completion Time, Intersection Resource Scheduling, Resource-Homogeneous Job Group

## Response Collection Time
- **Notation**: $T_{\text{resp},i}$
- **Definition**: The time from when assigned devices receive their computation tasks until the job server collects the required minimum number of responses (80% of target participants in the paper's default setup). Determined by the slowest (95th-percentile tail latency) responding device among participants.
- **Boundary conditions**: Dominates JCT when resource contention is low. Modeled using the 95th percentile of a log-normal response time distribution.
- **Related concepts**: Job Completion Time, Scheduling Delay, Tier-Based Device Matching

## Intersection Resource Scheduling (IRS)
- **Notation**: IRS; formalized as an integer multi-commodity flow (MCF) problem
- **Definition**: A scheduling problem formulation that explicitly models the intersection structure of device eligibility sets across CL jobs. Each job $J_i$ requires devices from an eligible subset $S_k = f(J_i)$; these subsets may overlap, nest, or be disjoint. The IRS objective is $\min \sum_{j=1}^{m} T_j$ where $T_j = \max_i(x_{ij} \cdot t_i)$, subject to each device being assigned to at most one job and each job receiving exactly $D_j$ devices.
- **Boundary conditions**: NP-hard in general (reduces to integer MCF). Venn solves it via a two-step heuristic. The exact ILP formulation is given in Appendix B of the paper.
- **Related concepts**: Resource-Homogeneous Job Group, Scheduling Delay, Contention-Aware Scheduling

## Resource-Homogeneous Job Group
- **Notation**: $G_j = \{J_i \mid f(J_i) = S_j, \forall J_i \in J\}_{i=1}^{m_j}$
- **Definition**: A group of CL jobs that share identical device eligibility requirements (i.e., they all require devices from the same subset $S_j$). Grouping by resource homogeneity reduces the IRS complexity from a joint over all jobs to intra-group + inter-group subproblems.
- **Boundary conditions**: Effective when jobs have discrete, categorical device requirements. Less applicable when eligibility requirements form a continuum.
- **Related concepts**: Intersection Resource Scheduling, Contention-Aware Scheduling

## Contention-Aware Scheduling
- **Notation**: Algorithm 1 (Venn-Sched)
- **Definition**: Venn's two-level scheduling heuristic. Intra-group: sort jobs within each group by remaining demand in ascending order (Shortest Remaining Demand First). Inter-group: initialize allocation to the scarcest group first; then greedily reallocate intersected resources from resource-rich groups to groups with higher queue-length-to-allocated-resource ratios ($m'_j / |S'_j| > m'_k / |S'_k|$). Complexity: $\max(O(m \log m), O(n^2))$.
- **Boundary conditions**: Invoked on job arrival and completion. Assumes resource eligibility is known at scheduling time. Approximates optimal for the two-group case (proven in Lemma 2) and generalizes greedily to $n$ groups.
- **Related concepts**: Intersection Resource Scheduling, Resource-Homogeneous Job Group, Scheduling Delay

## Tier-Based Device Matching
- **Notation**: Algorithm 2 (Venn-Match); tiers $S_1, \ldots, S_V$; speed-up factor $g_v = t_v / t_0$
- **Definition**: Devices are partitioned into $V$ hardware-capacity tiers. For each served job $J_i$, a random tier $S_u$ is selected. Tier-based matching is applied only if $1 + c_i > V + c_i g_u$, where $c_i = T_{\text{resp}} / T_{\text{sched}}$ is the ratio of response collection time to scheduling delay. If the condition holds, the job is assigned only devices from tier $S_u$, reducing response time at the cost of a factor-$V$ scheduling delay increase.
- **Boundary conditions**: Only beneficial when $c_i$ is large (response time dominates scheduling delay). Adaptive tier thresholds are set based on previous-round participant hardware profiles. First-round jobs skip tier matching (cold-start profiling).
- **Related concepts**: Response Collection Time, Scheduling Delay, Job Completion Time

## Starvation Prevention (Fairness Knob ε)
- **Notation**: $d'_i = d_i \cdot (t_i / T_i)^\varepsilon$; $q'_j = q_j \cdot (\sum_{J_i \in G_j} T_i / \sum_{J_i \in G_j} t_i)^\varepsilon$; $T_i = M \cdot sd_i$
- **Definition**: A fairness mechanism applied on top of IRS. The fair-share JCT for job $J_i$ is $T_i = M \cdot sd_i$, where $M$ is the number of simultaneous CL jobs and $sd_i$ is the JCT without contention. Each job's effective demand and each group's effective queue length are adjusted by the ratio of actual usage to fair-share usage, raised to the power $\varepsilon \in [0, \infty)$. At $\varepsilon=0$: pure IRS. As $\varepsilon \to \infty$: max-min fairness.
- **Boundary conditions**: Effective only when jobs have heterogeneous demands. $\varepsilon=2$ yields 69% of jobs meeting their fair-share JCT in experiments. Higher $\varepsilon$ reduces average JCT improvement.
- **Related concepts**: Contention-Aware Scheduling, Job Completion Time

## Collaborative Learning Job (CL Job)
- **Notation**: $J_i$; demand $D_i$; eligibility $f(J_i) = S_k$
- **Definition**: A distributed ML training task where an aggregation server coordinates edge devices. In each round, the server requests $D_i$ eligible devices; devices download the model, perform local training, and upload results. A round succeeds when at least 80% of $D_i$ target participants respond within a deadline (5–15 min). Each job in production requires 1,000–10,000 participants per round and takes 4–8 days to complete.
- **Boundary conditions**: Paper focuses on synchronous CL. Asynchronous CL is noted as compatible since scheduling depends only on remaining resource demand. Does not include server-side aggregation in the JCT model.
- **Related concepts**: Job Completion Time, Scheduling Delay, Response Collection Time
