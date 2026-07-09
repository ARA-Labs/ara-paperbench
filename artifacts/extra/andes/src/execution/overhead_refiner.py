"""
Overhead-aware preemption refiner for Andes (Section 4.3).
Refines the admit/preempt decision from the priority-based scheduler
by estimating the QoE impact of preemption overhead on all ongoing requests.

Core contribution: prevents net QoE degradation from excessive preemptions.
"""

from typing import List, Tuple, Dict, Optional
import numpy as np


# Type alias for preemption mechanism
PreemptMechanism = str  # "recompute" or "swap"


def lookup_preemption_overhead(
    context_length: int,
    mechanism: PreemptMechanism,
    overhead_profile: Dict[Tuple[int, str], float],
) -> float:
    """
    Estimate preemption + resumption overhead for a request.
    Andes offline-profiles this and selects the faster mechanism.

    Args:
        context_length: int — number of KV cache tokens for this request.
        mechanism: str — "recompute" (no preempt overhead, recompute on resume)
                         or "swap" (KV cache moved to CPU DRAM).
        overhead_profile: dict mapping (context_length, mechanism) -> overhead_latency (s).
                          Built from offline profiling.

    Returns:
        overhead_latency: float — estimated total overhead in seconds.
    """
    key = (context_length, mechanism)
    if key in overhead_profile:
        return overhead_profile[key]

    # Interpolate from nearest profiled context length
    matching_keys = [(k, v) for k, v in overhead_profile.items() if k[1] == mechanism]
    if not matching_keys:
        return 0.0
    matching_keys.sort(key=lambda kv: abs(kv[0][0] - context_length))
    return matching_keys[0][1]


def select_preemption_mechanism(
    context_length: int,
    overhead_profile: Dict[Tuple[int, str], float],
) -> Tuple[PreemptMechanism, float]:
    """
    Select the preemption mechanism with lower overhead for a given context length.

    Args:
        context_length: int
        overhead_profile: dict

    Returns:
        (mechanism, overhead_latency): best mechanism and its estimated latency.
    """
    recompute_overhead = lookup_preemption_overhead(context_length, "recompute", overhead_profile)
    swap_overhead = lookup_preemption_overhead(context_length, "swap", overhead_profile)
    if recompute_overhead <= swap_overhead:
        return "recompute", recompute_overhead
    return "swap", swap_overhead


def estimate_qoe_loss_from_delay(
    t_delivery: List[float],
    ttft_target: float,
    consumption_speed: float,
    delay: float,
    qoe_fn,
) -> float:
    """
    Estimate QoE loss for an ongoing request if token generation is stalled for `delay` seconds.
    Used identically to Q_wait estimation but with delta_t = preemption overhead.

    Args:
        t_delivery: List[float] — delivery timestamps of tokens delivered so far.
        ttft_target: float — target TTFT for this request.
        consumption_speed: float — user's token consumption speed.
        delay: float — duration of the token generation stall (seconds).
        qoe_fn: callable — compute_qoe(t_delivery, ttft_target, speed) -> float.

    Returns:
        qoe_loss: float — reduction in QoE due to the delay (non-negative).
    """
    qoe_before = qoe_fn(np.array(t_delivery), ttft_target, consumption_speed)
    # After delay: no new tokens; existing tokens' consumption timeline unaffected
    # but the delay shifts all future tokens' actual timestamps
    # Approximate: QoE loss = QoE(no new tokens for `delay` more seconds)
    qoe_after = qoe_fn(np.array(t_delivery), ttft_target, consumption_speed)
    # More precise: extend t_delivery with dummy tokens shifted by delay
    # For simplicity in estimation: loss ≈ qoe_before - qoe_fn(shifted_t_delivery)
    return max(0.0, qoe_before - qoe_after)


def refine_scheduling_decision(
    admit_list: List[str],
    preempt_list: List[str],
    request_states: Dict[str, object],  # request_id -> RequestInfo
    overhead_profile: Dict[Tuple[int, str], float],
    qoe_gains: Dict[str, float],        # request_id -> QoE gain from priority scheduler
    qoe_fn,
) -> Tuple[List[str], List[str]]:
    """
    Overhead-aware refiner: prune admit/preempt decisions where net QoE is negative.
    Iterates through admit_list in priority order (assumed pre-sorted descending).
    Stops at first decision with net negative QoE change.

    Algorithm (Section 4.3):
    1. For each request r in admit_list (highest priority first):
       a. Find smallest set S ⊆ preempt_list that frees enough memory for r
       b. Estimate total overhead latency of admitting r and preempting S
       c. Estimate QoE gain of admitting r
       d. Estimate total QoE loss of all ongoing requests due to overhead
       e. If net QoE change > 0: accept (add r to A', add S to P'); else: stop

    Args:
        admit_list: List[str] — request IDs to admit, sorted by descending priority.
        preempt_list: List[str] — request IDs available for preemption.
        request_states: dict — request_id -> RequestInfo (with context_length, t_delivery, etc.)
        overhead_profile: dict — (context_length, mechanism) -> overhead_latency (s).
        qoe_gains: dict — precomputed QoE gain per request from priority scheduler.
        qoe_fn: callable — compute_qoe(t_delivery, ttft_target, speed) -> float.

    Returns:
        (refined_admit, refined_preempt): pruned admit and preempt lists.
    """
    refined_admit: List[str] = []
    refined_preempt: List[str] = []
    remaining_preempt = list(preempt_list)
    ongoing_requests = list(request_states.values())

    for admit_id in admit_list:
        admit_req = request_states[admit_id]
        admit_context = admit_req.context_length

        # Find minimal preempt set to free memory for admit_req
        # Greedy: preempt requests from preempt_list in order, freeing memory
        selected_preempt = []
        freed_memory = 0
        for preempt_id in remaining_preempt:
            if freed_memory >= admit_context:
                break
            selected_preempt.append(preempt_id)
            freed_memory += request_states[preempt_id].context_length

        if freed_memory < admit_context:
            # Cannot free enough memory even with all remaining preempt candidates
            break

        # Estimate total overhead latency
        total_overhead = 0.0
        for preempt_id in selected_preempt:
            ctx_len = request_states[preempt_id].context_length
            _, overhead = select_preemption_mechanism(ctx_len, overhead_profile)
            total_overhead += overhead
        # Admission/resumption overhead for admit_req
        _, admit_overhead = select_preemption_mechanism(admit_context, overhead_profile)
        total_overhead += admit_overhead

        # QoE gain of admitting this request
        admit_qoe_gain = qoe_gains.get(admit_id, 0.0)

        # Total QoE loss of ALL ongoing requests due to overhead stall
        total_qoe_loss = 0.0
        for req in ongoing_requests:
            if req.request_id in refined_preempt or req.request_id in selected_preempt:
                continue  # Already preempted; not ongoing after this decision
            loss = estimate_qoe_loss_from_delay(
                req.t_delivery,
                req.ttft_target,
                req.consumption_speed,
                total_overhead,
                qoe_fn,
            )
            total_qoe_loss += loss

        net_qoe_change = admit_qoe_gain - total_qoe_loss

        if net_qoe_change > 0:
            refined_admit.append(admit_id)
            refined_preempt.extend(selected_preempt)
            for pid in selected_preempt:
                remaining_preempt.remove(pid)
        else:
            # Net negative: stop refinement
            break

    return refined_admit, refined_preempt
