# Experiments

## E01: End-to-End QoE Improvement on Real-World BurstGPT Trace
- **Verifies**: C01, C04, C07
- **Setup**:
  - Model: Phi-3.5-MoE 16×3.8B
  - Hardware: 8 × NVIDIA A100 SXM4 40GB, AWS p4d.24xlarge, tensor parallelism
  - Dataset: Multi-Round ShareGPT dataset; one-hour slice of BurstGPT request trace
  - System: Andes vs vLLM (v0.6.1, FCFS); target TTFT = max(input_length/5000, 1) seconds; user reading speed from Figure 2a distribution
- **Procedure**:
  1. Replay the one-hour BurstGPT trace through vLLM (FCFS) and record per-request token delivery timestamps.
  2. Compute QoE, TTFT, and TDS for each request under vLLM using Equations 1–3.
  3. Replay the same trace through Andes and record per-request token delivery timestamps.
  4. Compute QoE, TTFT, and TDS for each request under Andes.
  5. Plot CDFs of QoE, TTFT, and TDS for both systems (Figure 11).
  6. Record peak queue length (running + waiting requests) at each timestep for both systems (Figures 3 and 13).
  7. Select representative requests and visualize their Actual Delivery Timelines vs Ideal Consumption Timeline (Figure 12).
- **Metrics**: Average QoE (scalar), CDF of QoE at threshold 0.95, average TTFT (seconds), average TDS (tokens/s), peak waiting queue length (requests), GPU memory utilization (%)
- **Expected outcome**:
  - Andes achieves substantially higher average QoE than vLLM
  - Andes serves a much larger fraction of requests at QoE ≥ 0.95 than vLLM
  - Andes achieves significantly lower average TTFT than vLLM
  - Andes and vLLM achieve comparable average TDS (throughput is not sacrificed for QoE)
  - Andes substantially reduces peak queue length compared to vLLM
- **Baselines**: vLLM (v0.6.1, FCFS)
- **Dependencies**: none

## E02: QoE and Resource Savings Under Synthetic Cyclic Burst Load (Varying Intensity)
- **Verifies**: C02, C03, C08
- **Setup**:
  - Models: Phi-3-mini 3.8B (4×A100), Command R 32B (8×A100), Phi-3.5-MoE 16×3.8B (8×A100), Llama 3.1 70B (8×A100)
  - Hardware: NVIDIA A100 SXM4 40GB, AWS p4d.24xlarge
  - Dataset: Multi-Round ShareGPT, ArXiv Summarization, Coding Challenges (one experiment per dataset/model pair)
  - System: Cyclic burst load pattern; default burst duration = 35%; burst intensity varied over [1.5, 2.0, 2.5]; average request rate = system throughput under no burstiness; Poisson arrivals within each phase
- **Procedure**:
  1. For each combination of (model, dataset, burst intensity), generate a one-cycle synthetic trace following the cyclic burst load pattern (Figure 14).
  2. Serve the trace with Andes, vLLM (FCFS), Sarathi-Serve, and LQSF.
  3. Compute average QoE across all requests for each system.
  4. Plot average QoE vs burst intensity for each model/dataset combination (Figure 15, 4×3 grid).
  5. Draw a horizontal line at QoE = 0.95; identify the maximum burst intensity each system can sustain at this threshold.
  6. Compute GPU savings: (1 − burst_intensity_vLLM_max / burst_intensity_Andes_max) × 100%.
- **Metrics**: Average QoE (scalar per configuration), maximum sustainable burst intensity at QoE ≥ 0.95, GPU resource savings (%)
- **Expected outcome**:
  - Andes achieves substantially higher average QoE than vLLM across all model/dataset combinations, with the gap widening at higher burst intensities
  - Andes sustains much higher burst intensity than vLLM while maintaining QoE above the acceptable threshold
  - Andes yields significant GPU resource savings over vLLM by tolerating higher load before QoE degrades
  - Andes consistently outperforms Sarathi-Serve and LQSF on average QoE
- **Baselines**: vLLM (v0.6.1, FCFS), Sarathi-Serve, LQSF
- **Dependencies**: none

## E03: QoE Under Synthetic Cyclic Burst Load (Varying Duration)
- **Verifies**: C08
- **Setup**:
  - Models: Phi-3-mini 3.8B, Command R 32B, Phi-3.5-MoE 16×3.8B, Llama 3.1 70B
  - Hardware: NVIDIA A100 SXM4 40GB, AWS p4d.24xlarge
  - Dataset: Multi-Round ShareGPT, ArXiv Summarization, Coding Challenges
  - System: Cyclic burst load pattern; default burst intensity = 2×; burst duration varied (x-axis shows Duration (%))
- **Procedure**:
  1. For each (model, dataset, burst duration) combination, generate synthetic trace with cyclic burst pattern.
  2. Serve with Andes, vLLM, Sarathi-Serve, LQSF.
  3. Compute average QoE per system per configuration.
  4. Plot average QoE vs burst duration (Figure 16, 4×3 grid).
- **Metrics**: Average QoE (scalar per configuration)
- **Expected outcome**:
  - Andes achieves higher average QoE than all baselines across all burst durations, models, and datasets
  - The QoE advantage of Andes over baselines grows as burst duration increases
- **Baselines**: vLLM (FCFS), Sarathi-Serve, LQSF
- **Dependencies**: none

## E04: Ablation — Overhead-Aware Refiner vs No Overhead Awareness
- **Verifies**: C05
- **Setup**:
  - Model: Llama 3.1 70B
  - Hardware: 8 × NVIDIA A100 SXM4 40GB
  - Dataset: Multi-Round ShareGPT
  - System: Cyclic burst load pattern; default burst intensity = 2×; burst duration varied [25%, 30%, 35%, 40%, 45%]; compare Andes (with refiner) vs Andes-no-overhead (greedy scheduler only, no refiner) vs vLLM
- **Procedure**:
  1. Run all three configurations across burst durations [25%, 30%, 35%, 40%, 45%].
  2. Record average QoE and average number of preemptions per request for each burst duration.
  3. Plot average QoE vs burst duration (top panel, Figure 17).
  4. Plot average preemptions per request vs burst duration (bottom panel, Figure 17).
- **Metrics**: Average QoE, average preemptions per request
- **Expected outcome**:
  - Andes with the overhead-aware refiner maintains consistently high QoE as burst duration increases
  - Ablating the refiner causes QoE to degrade significantly with longer burst durations due to excessive preemptions
  - Preemptions per request grow steeply with burst duration when the refiner is removed, but remain controlled when it is active
- **Baselines**: vLLM (FCFS)
- **Dependencies**: none

## E05: Comparison of Greedy vs 3D Dynamic Programming Knapsack Solver
- **Verifies**: C06
- **Setup**:
  - Model: Llama 3.1 70B
  - Hardware: 8 × NVIDIA A100 SXM4 40GB
  - Dataset: Multi-Round ShareGPT
  - System: Cyclic burst load pattern; burst intensity varied [1.5, 2.0, 2.5] (left panel); burst duration varied (right panel); compare Andes with greedy solver vs Andes with 3D DP solver
- **Procedure**:
  1. Implement both solvers in Andes: Algorithm 1 (greedy, O(N log N)) and Algorithm 2 (3D DP, O(MN²)).
  2. Run each solver across burst intensity and burst duration sweep.
  3. Measure average QoE for each solver configuration (Figure 18).
  4. Measure per-scheduling-decision runtime for each solver.
  5. Compute speedup: DP runtime / greedy runtime.
- **Metrics**: Average QoE, per-decision solver runtime (ms), speedup ratio
- **Expected outcome**:
  - The greedy solver matches or slightly exceeds the 3D DP solver in average QoE, especially under longer burst durations and higher intensities
  - The greedy solver runs significantly faster per scheduling decision than the 3D DP solver
- **Baselines**: 3D DP solver (optimal but slow)
- **Dependencies**: none

## E06: Robustness Under Poisson Arrival Distribution
- **Verifies**: C08
- **Setup**:
  - Model: Llama 3.1 70B
  - Hardware: 8 × NVIDIA A100 SXM4 40GB
  - Dataset: Multi-Round ShareGPT
  - System: Poisson arrival process (no burst pattern); request rate varied from 1.0 to 1.4 req/s; 20-minute trace duration
- **Procedure**:
  1. Generate traces with Poisson arrivals at varying request rates.
  2. Serve with Andes, vLLM, Sarathi-Serve, LQSF.
  3. Compute average QoE per system per request rate (Figure 20).
- **Metrics**: Average QoE vs request rate (req/s)
- **Expected outcome**:
  - Andes delivers higher average QoE than all baselines across the full range of request rates, with the advantage most pronounced at high load
- **Baselines**: vLLM (FCFS), Sarathi-Serve, LQSF
- **Dependencies**: none
