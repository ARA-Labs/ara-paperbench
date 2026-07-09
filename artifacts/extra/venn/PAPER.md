---
title: "Venn: Resource Management for Collaborative Learning Jobs"
authors: ["Jiachen Liu", "Fan Lai", "Ding Ding", "Yiwen Zhang", "Mosharaf Chowdhury"]
year: 2025
venue: "MLSys 2025"
doi: "arXiv:2312.08298"
ara_version: "1.0"
domain: "Federated/Collaborative Learning, Systems, Resource Management"
keywords:
  - collaborative learning
  - federated learning
  - resource management
  - job scheduling
  - device heterogeneity
  - intersection resource scheduling
  - straggler mitigation
  - job completion time
  - edge devices
  - contention-aware scheduling
claims_summary:
  - "Venn reduces average JCT by up to 1.88× over random matching across diverse real-world CL workloads"
  - "Contention-aware IRS scheduling minimizes scheduling delay by prioritizing jobs with scarce resources and smallest remaining demand"
  - "Tier-based device-to-job matching reduces response collection time and is most beneficial under low resource contention"
  - "Venn's joint scheduling+matching achieves max(O(m log m), O(n²)) complexity and scales to thousands of jobs"
abstract: "In recent years, collaborative learning (CL) has emerged as a promising approach for machine learning (ML) and data science across distributed edge devices. As the deployment of CL jobs increases, they inevitably contend for limited resources. However, efficient resource scheduling in this context is challenging because of the ephemeral nature and resource heterogeneity of devices, coupled with the overlapping resource requirements of diverse CL jobs. Existing resource managers often assign devices to CL jobs randomly for simplicity and scalability, but this approach compromises job efficiency. In this paper, we present Venn, a CL resource manager that efficiently schedules ephemeral, heterogeneous devices among multiple CL jobs to reduce the average job completion time (JCT). Venn formulates the Intersection Resource Scheduling (IRS) problem to identify complex resource contention among multiple CL jobs. It then proposes a contention-aware scheduling heuristic to minimize the average scheduling delay. Furthermore, it proposes a resource-aware device-to-job matching heuristic to optimize response collection time by mitigating stragglers. Our evaluation shows that, compared to the state-of-the-art CL resource managers, Venn improves the average JCT by up to 1.88×."
---

# Venn: Resource Management for Collaborative Learning Jobs

## Overview

Venn is a CL resource manager for efficiently allocating heterogeneous, ephemeral edge devices across multiple concurrent collaborative learning (CL) jobs to minimize average job completion time (JCT). JCT consists of two components: scheduling delay (time to acquire sufficient devices) and response collection time (time for devices to complete training and report back). Existing managers (Apple, Meta, Google) all use random device-to-job matching, which fails under resource contention.

Venn introduces two novel algorithms: (1) Intersection Resource Scheduling (IRS), which groups jobs by resource type, then orders them intra-group by smallest remaining demand and inter-group by scarcity and queue length; and (2) a tier-based device-to-job matching algorithm that partitions devices into V hardware-capacity tiers and conditionally assigns a single tier per job if doing so reduces total JCT. Evaluated across 5 workload scenarios on simulation and real testbeds, Venn improves average JCT by up to 1.88× over random matching and up to 2.27× on biased workloads.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating Venn |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 9 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: Venn 2-module pipeline (IRS + matching) |
| [solution/algorithm.md](logic/solution/algorithm.md) | IRS (Algorithm 1) + Device Matching (Algorithm 2), complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence and deployment tricks |
| [related_work.md](logic/related_work.md) | 10 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/venn_scheduler.py](src/execution/venn_scheduler.py) | IRS (Algorithm 1) + Device Matching (Algorithm 2) stubs | C01, C02, C03 |
| [configs/training.md](src/configs/training.md) | CL job and simulation parameters | — |
| [configs/model.md](src/configs/model.md) | Model configurations for real CL experiments | — |
| [environment.md](src/environment.md) | Hardware, deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 4 tables + 5 figures |
| [tables/table1_jct_improvement.md](evidence/tables/table1_jct_improvement.md) | JCT speedup vs. random matching by workload |
| [tables/table2_jct_by_demand.md](evidence/tables/table2_jct_by_demand.md) | JCT improvement breakdown by demand percentile |
| [tables/table3_jct_by_resource.md](evidence/tables/table3_jct_by_resource.md) | JCT improvement breakdown by resource eligibility type |
| [tables/table4_biased_workloads.md](evidence/tables/table4_biased_workloads.md) | JCT improvement on four biased workloads |
| [figures/fig3_toy_example.md](evidence/figures/fig3_toy_example.md) | Toy example JCT comparison across scheduling strategies |
| [figures/fig4_contention_impact.md](evidence/figures/fig4_contention_impact.md) | Impact of number of jobs on test accuracy |
| [figures/fig10_overhead.md](evidence/figures/fig10_overhead.md) | Scheduling overhead vs. number of jobs and groups |
| [figures/fig11_ablation_breakdown.md](evidence/figures/fig11_ablation_breakdown.md) | Ablation: per-component JCT improvement |
| [figures/fig14_fairness_knob.md](evidence/figures/fig14_fairness_knob.md) | Effect of fairness knob ε on JCT and fairness |
