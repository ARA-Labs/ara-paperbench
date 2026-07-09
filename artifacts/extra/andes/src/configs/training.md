# Training / Serving Configuration Parameters

## target_ttft_formula
- **Value**: `max(input_length / 5000, 1)` seconds
- **Rationale**: Input tokens require prefill computation; at 5000 tokens/s prefill throughput on the evaluation hardware, longer prompts warrant proportionally longer TTFT targets. Floor of 1 second prevents unrealistically tight targets for short inputs.
- **Search range**: Not specified in paper; formula derived from hardware prefill throughput.
- **Sensitivity**: medium
- **Source**: Section 6.1, "QoE Parameters"

## user_reading_speed_distribution
- **Value**: Sampled from Figure 2a distribution (18–24: 28%, 25–44: 52%, 45–54: 11%, 55–64: 6%, 65+: 3%); average reading speed ≈ 4.8 tokens/s; average listening speed ≈ 3.3 tokens/s
- **Rationale**: Real user demographics; 1 word ≈ 1.3 tokens (OpenAI tokenization).
- **Search range**: Fixed to demographic distribution for evaluation; real deployments set per application.
- **Sensitivity**: high — consumption speed directly determines QoE parameters and Ideal Consumption Timeline.
- **Source**: Section 6.1; Figure 2

## kv_cache_watermark
- **Value**: 90% GPU KV cache occupancy
- **Rationale**: Trigger scheduling algorithm only when memory pressure is high to avoid unnecessary overhead. 90% provides buffer before OOM while acting early enough to prevent blocking.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Section 4.2, "Selective Triggering"

## prefill_throughput_hardware
- **Value**: 5000 tokens/s (on 8×A100 hardware for Phi-3.5-MoE 16×3.8B)
- **Rationale**: Used to derive target TTFT formula.
- **Search range**: Hardware-dependent.
- **Sensitivity**: low (affects TTFT target formula, not scheduling directly)
- **Source**: Section 6.1, "QoE Parameters"

## delta_t_qoe_gain_estimation
- **Value**: Not specified exactly in paper; evaluated empirically in Figure 19; described as "roughly consistent" across values
- **Rationale**: Look-ahead window for QoE gain estimation; longer Δt provides more stable estimates but may be less responsive; best value depends on model and request distribution.
- **Search range**: Varied in Figure 19 (exact range not specified in paper text)
- **Sensitivity**: medium — best value requires per-deployment tuning.
- **Source**: Section 4.1; Section 6.4, "QoE Gain Estimation Time Horizon"

## burst_pattern_default_intensity
- **Value**: 2 (burst request rate = 2× average request rate)
- **Rationale**: Matches BurstGPT statistics: average ≈2× higher request rate during bursts.
- **Search range**: [1.5, 2.5] in experiments.
- **Sensitivity**: high — intensity determines QoE degradation severity.
- **Source**: Section 6.3; Figure 14

## burst_pattern_default_duration
- **Value**: 35% (fraction of time in burst phase)
- **Rationale**: Matches BurstGPT statistics: each burst sustains ≈7 minutes average out of ≈20-minute cycles.
- **Search range**: [25%, 45%] in ablation (Figure 17); broader range in Figure 16.
- **Sensitivity**: high
- **Source**: Section 6.3; Figure 14
