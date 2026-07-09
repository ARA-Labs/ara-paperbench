# Claims

## C01: Venn reduces average JCT by up to 1.88× over random matching across diverse CL workloads
- **Statement**: Across five workload types (Even, Small, Large, Low, High) in event-driven simulation with 50 jobs and Poisson arrival (30-min average inter-arrival), Venn achieves average JCT speedups of 1.87×, 1.78×, 1.72×, 1.88×, and 1.63× respectively over optimized random matching.
- **Status**: supported
- **Falsification criteria**: Venn's average JCT speedup over random matching falls below 1.63× on any of the five standard workloads under the same experimental setup.
- **Proof**: [E01]
- **Dependencies**: C02, C03
- **Tags**: JCT, end-to-end, speedup, workloads, simulation

## C02: Contention-aware IRS scheduling is the primary driver of JCT improvement under high contention
- **Statement**: The IRS scheduling component alone (Venn w/o matching) achieves 1.79× average JCT improvement in the Low workload; without scheduling (Venn w/o sched / FIFO), improvement is only 1.62×. Under High workload, IRS yields 1.63× and matching adds no further gain.
- **Status**: supported
- **Falsification criteria**: Removing the IRS scheduling component does not reduce average JCT improvement by more than 5% relative to full Venn in any tested workload.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: IRS, scheduling, ablation, scheduling-delay

## C03: Tier-based device matching reduces JCT primarily under low resource contention
- **Statement**: The matching component alone (Venn w/o sched) achieves 1.62× JCT improvement in the Low workload versus FIFO's 1.55×, but under High workload both Venn w/o sched and FIFO achieve 1.42× — matching provides no benefit when contention is high.
- **Status**: supported
- **Falsification criteria**: The matching component provides statistically significant JCT improvement over FIFO in the High contention workload.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: device-matching, tier-based, response-collection-time, low-contention

## C04: Venn achieves logarithmic-linear time complexity and introduces negligible scheduling overhead
- **Statement**: Venn's scheduling algorithm has time complexity max(O(m log m), O(n²)) where m is the number of jobs and n is the number of job groups. Empirically, scheduling latency remains below ~1 ms for up to 1000 jobs and 100 job groups.
- **Status**: supported
- **Falsification criteria**: Scheduling latency exceeds 10 ms for 1000 jobs or 100 job groups in the overhead evaluation.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: complexity, overhead, scalability

## C05: Venn does not adversely affect CL model accuracy while speeding up convergence
- **Statement**: In real CL system experiments (ResNet-18 + MobileNet-V2 on FEMNIST, 20 jobs), Venn and its baselines (FIFO, SRSF) converge to the same final average test accuracy (~0.75), but Venn reaches this accuracy faster.
- **Status**: supported
- **Falsification criteria**: Venn's final model accuracy is more than 1 percentage point below that of random matching under the same number of rounds.
- **Proof**: [E04]
- **Dependencies**: C01
- **Tags**: accuracy, convergence, model-quality, real-experiment

## C06: Venn's fairness knob (ε) provides a controllable tradeoff between JCT and fairness
- **Statement**: At ε=2, 69% of jobs receive their fair-share JCT (defined as Ti = M × sdi). As ε increases from 0, average JCT speedup decreases while the percentage of jobs meeting fair-share JCT increases monotonically.
- **Status**: supported
- **Falsification criteria**: At ε=2, fewer than 50% of jobs meet their fair-share JCT, or increasing ε beyond 2 decreases the percentage of jobs meeting fair-share JCT.
- **Proof**: [E05]
- **Dependencies**: C01
- **Tags**: fairness, starvation-prevention, epsilon, tradeoff
