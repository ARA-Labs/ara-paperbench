"""
Andes Token-Level QoE-Aware Request Scheduler.

Implements:
  1. Priority-Based Greedy Packing (Algorithm 1, Section 4.2)
     - Priority: QoE gain / context_length
     - Greedy packing respecting memory (M) and batch size (B) constraints
     - Batch size search space pruning [B_min, B_max]
     - Selective triggering (KV watermark, latency threshold)

  2. Overhead-Aware Refiner (Section 4.3)
     - Post-processes greedy decision
     - Prunes admit/preempt pairs with non-positive net QoE change

Corresponds to the Token-Level Request Scheduler component (Figure 6).
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict, Callable, Optional
import math

from qoe import RequestState, QoEComputer


@dataclass
class SchedulingDecision:
    """Output of the scheduler for one quantum."""
    admit_resume: List[str]   # request_ids to admit or resume
    preempt: List[str]        # request_ids to preempt


class PriorityGreedyScheduler:
    """
    Priority-based greedy knapsack packing (Algorithm 1).

    For each candidate batch size B in [B_min, B_max], sorts requests by
    priority = QoE_gain / context_length (descending) and greedily packs
    until memory M or batch size B is exhausted. Returns the set of requests
    achieving the maximum total QoE gain across all B.

    Time complexity: O(N log N) per batch size value.
    """

    def __init__(
        self,
        memory_capacity: int,          # M: max KV cache entries
        token_latency_fn: Callable,    # batch_size -> per-token latency (seconds)
        delta_t: float,                # look-ahead window for QoE gain estimation
        kv_watermark: float = 0.90,    # trigger threshold for memory-bound case
    ):
        """
        Args:
            memory_capacity: GPU KV cache capacity in tokens (M).
            token_latency_fn: Profiled function mapping batch_size -> latency per token.
            delta_t: Time horizon for QoE gain estimation.
            kv_watermark: KV cache occupancy fraction above which scheduler is triggered.
        """
        self.M = memory_capacity
        self.token_latency_fn = token_latency_fn
        self.delta_t = delta_t
        self.kv_watermark = kv_watermark

    def should_trigger(
        self,
        requests: List[RequestState],
        current_kv_used: int,
        min_consumption_speed: float,
        current_batch_size: int
    ) -> bool:
        """
        Selective triggering: only run the scheduler if the system is resource-constrained.

        Args:
            requests: All ongoing requests (running + waiting).
            current_kv_used: Current KV cache usage in tokens.
            min_consumption_speed: Most stringent (highest) user consumption speed (tokens/s).
            current_batch_size: Current running batch size.

        Returns:
            True if the scheduler should run this quantum.
        """
        # Memory-bound: KV cache occupancy exceeds watermark
        memory_bound = (current_kv_used / self.M) > self.kv_watermark

        # Compute-bound: token generation latency exceeds most stringent consumption speed
        if current_batch_size > 0:
            latency = self.token_latency_fn(current_batch_size)
            compute_bound = latency > (1.0 / min_consumption_speed)
        else:
            compute_bound = False

        return memory_bound or compute_bound

    def compute_batch_size_bounds(
        self,
        requests: List[RequestState],
        min_consumption_speed: float
    ) -> Tuple[int, int]:
        """
        Compute B_min and B_max for batch size search space pruning.

        B_max: largest feasible batch (pack shortest-context requests until M is reached).
        B_min: largest B where TDS > r_user_min (generating faster than most stringent user).

        Args:
            requests: All ongoing requests sorted by context length ascending.
            min_consumption_speed: Most stringent consumption speed (tokens/s).

        Returns:
            (B_min, B_max) tuple.
        """
        # B_max: fill with shortest context requests
        sorted_by_ctx = sorted(requests, key=lambda r: r.context_length)
        total_ctx = 0
        b_max = 0
        for req in sorted_by_ctx:
            if total_ctx + req.context_length <= self.M:
                total_ctx += req.context_length
                b_max += 1
            else:
                break
        b_max = max(1, b_max)

        # B_min: largest B where latency < 1/min_consumption_speed
        b_min = 1
        for b in range(1, b_max + 1):
            latency = self.token_latency_fn(b)
            if latency < (1.0 / min_consumption_speed):
                b_min = b
            else:
                break
        b_min = max(1, b_min)

        return b_min, b_max

    def greedy_pack(
        self,
        requests: List[RequestState],
        qoe_gains: Dict[str, float],
        batch_size_B: int,
        current_time: float
    ) -> Tuple[List[str], float]:
        """
        Algorithm 1: Priority-based greedy packing for a fixed batch size B.

        Args:
            requests: All ongoing requests.
            qoe_gains: Mapping request_id -> QoE gain at batch size B.
            batch_size_B: Target batch size to pack.
            current_time: Current wall-clock time.

        Returns:
            (selected_ids, total_qoe_gain): IDs of selected requests and their total gain.
        """
        # Compute priority = QoE gain / context length
        priorities = []
        for req in requests:
            gain = qoe_gains.get(req.request_id, 0.0)
            priority = gain / max(req.context_length, 1)
            priorities.append((priority, req))

        # Sort descending by priority
        priorities.sort(key=lambda x: x[0], reverse=True)

        selected_ids: List[str] = []
        total_gain = 0.0
        m_used = 0
        n_used = 0

        for priority, req in priorities:
            if m_used + req.context_length <= self.M and n_used + 1 <= batch_size_B:
                selected_ids.append(req.request_id)
                total_gain += qoe_gains.get(req.request_id, 0.0)
                m_used += req.context_length
                n_used += 1
            else:
                break  # Greedy: stop when first constraint is violated

        return selected_ids, total_gain

    def schedule(
        self,
        requests: List[RequestState],
        currently_running: List[str],
        current_time: float,
        min_consumption_speed: float
    ) -> Tuple[List[str], List[str], int]:
        """
        Main scheduling entry point. Runs greedy packing for all B in [B_min, B_max]
        and returns the best decision.

        Args:
            requests: All ongoing requests (running + waiting).
            currently_running: IDs of currently running requests.
            current_time: Current wall-clock time.
            min_consumption_speed: Most stringent user consumption speed.

        Returns:
            (serve_ids, preempt_ids, best_B): IDs to serve, IDs to preempt, chosen B.
        """
        b_min, b_max = self.compute_batch_size_bounds(requests, min_consumption_speed)

        best_serve_ids: List[str] = []
        best_total_gain = -math.inf
        best_B = b_min

        for B in range(b_min, b_max + 1):
            # Compute QoE gains for all requests at this batch size
            qoe_gains: Dict[str, float] = {}
            for req in requests:
                gain = QoEComputer.compute_qoe_gain(
                    req, B, self.token_latency_fn, self.delta_t, current_time
                )
                qoe_gains[req.request_id] = gain

            serve_ids, total_gain = self.greedy_pack(
                requests, qoe_gains, B, current_time
            )

            if total_gain > best_total_gain:
                best_total_gain = total_gain
                best_serve_ids = serve_ids
                best_B = B

        # Determine preemptions: currently running but not in serve set
        serve_set = set(best_serve_ids)
        preempt_ids = [rid for rid in currently_running if rid not in serve_set]

        return best_serve_ids, preempt_ids, best_B


class OverheadAwareRefiner:
    """
    Refines the greedy scheduler's admission/preemption decisions to ensure
    preemption overhead does not cause net QoE degradation (Section 4.3).

    For each (admit, preempt) pair (in priority order), estimates:
      net_delta_QoE = QoE_gain(admit) - sum(QoE_loss(req, overhead) for all ongoing)
    and retains the pair only if net_delta_QoE > 0.
    """

    def __init__(
        self,
        overhead_profile: Callable,    # context_length -> overhead latency (seconds)
        token_latency_fn: Callable,    # batch_size -> per-token latency
        delta_t: float,
    ):
        """
        Args:
            overhead_profile: Profiled function mapping context_length -> preemption overhead (s).
            token_latency_fn: Profiled function mapping batch_size -> per-token latency.
            delta_t: Time horizon for QoE gain estimation.
        """
        self.overhead_profile = overhead_profile
        self.token_latency_fn = token_latency_fn
        self.delta_t = delta_t

    def refine(
        self,
        proposed_admit: List[str],           # from greedy scheduler, highest-priority first
        proposed_preempt: List[str],         # from greedy scheduler, lowest-priority first
        all_requests: Dict[str, RequestState],
        currently_running: List[str],
        qoe_gains: Dict[str, float],
        current_time: float,
        batch_size: int
    ) -> Tuple[List[str], List[str]]:
        """
        Iterates over admit/preempt pairs. For each pair, estimates net QoE change.
        Stops at first pair with non-positive net change.

        Args:
            proposed_admit: Request IDs to potentially admit (descending priority).
            proposed_preempt: Request IDs to potentially preempt (ascending priority, i.e., lowest first).
            all_requests: Map from request_id -> RequestState.
            currently_running: All currently running request IDs.
            qoe_gains: Precomputed QoE gains for proposed_admit requests.
            current_time: Current wall-clock time.
            batch_size: Current batch size from greedy decision.

        Returns:
            (refined_admit, refined_preempt): Pruned admission and preemption lists.
        """
        refined_admit: List[str] = []
        refined_preempt: List[str] = []

        # Pair up: each admit needs the corresponding preempt to free memory
        for admit_id, preempt_id in zip(proposed_admit, proposed_preempt):
            admit_state = all_requests[admit_id]
            preempt_state = all_requests[preempt_id]

            # Estimate overhead of this specific preempt + admit operation
            overhead_latency = self.overhead_profile(preempt_state.context_length)

            # QoE gain from admitting this request
            qoe_gain = qoe_gains.get(admit_id, 0.0)

            # QoE loss: overhead delays all ongoing requests (treat as delta_t = overhead)
            total_qoe_loss = 0.0
            for running_id in currently_running:
                if running_id == preempt_id:
                    continue  # This request is being preempted anyway
                running_state = all_requests[running_id]
                q_current = QoEComputer.compute_qoe(running_state)
                q_after_overhead = QoEComputer.estimate_qoe_if_waiting(
                    running_state, overhead_latency, current_time
                )
                total_qoe_loss += max(0.0, q_current - q_after_overhead)

            net_delta = qoe_gain - total_qoe_loss

            if net_delta > 0.0:
                refined_admit.append(admit_id)
                refined_preempt.append(preempt_id)
            else:
                # Net QoE change non-positive: stop here (all lower-priority pairs worse)
                break

        return refined_admit, refined_preempt


class AndesScheduler:
    """
    Top-level Andes scheduler combining greedy packing and overhead-aware refining.

    Usage per scheduling quantum:
      1. Check if scheduling should trigger (selective triggering).
      2. Run PriorityGreedyScheduler to get initial (serve, preempt) decision.
      3. Run OverheadAwareRefiner to prune decision.
      4. Return final SchedulingDecision to Executor.
    """

    def __init__(
        self,
        memory_capacity: int,
        token_latency_fn: Callable,
        overhead_profile: Callable,
        delta_t: float,
        kv_watermark: float = 0.90,
    ):
        self.greedy = PriorityGreedyScheduler(
            memory_capacity, token_latency_fn, delta_t, kv_watermark
        )
        self.refiner = OverheadAwareRefiner(overhead_profile, token_latency_fn, delta_t)
        self.token_latency_fn = token_latency_fn
        self.delta_t = delta_t

    def step(
        self,
        all_requests: Dict[str, RequestState],
        currently_running: List[str],
        current_time: float,
        current_kv_used: int
    ) -> SchedulingDecision:
        """
        Execute one scheduling quantum.

        Args:
            all_requests: All ongoing requests (running + waiting).
            currently_running: IDs of currently running requests.
            current_time: Current wall-clock time.
            current_kv_used: Current total KV cache tokens in use.

        Returns:
            SchedulingDecision with admit_resume and preempt lists.
        """
        requests = list(all_requests.values())
        if not requests:
            return SchedulingDecision(admit_resume=[], preempt=[])

        min_speed = min(r.qoe_params.consumption_speed for r in requests)

        # Selective triggering
        if not self.greedy.should_trigger(
            requests, current_kv_used, min_speed, len(currently_running)
        ):
            return SchedulingDecision(
                admit_resume=currently_running,
                preempt=[]
            )

        # Greedy scheduling
        serve_ids, preempt_ids, best_B = self.greedy.schedule(
            requests, currently_running, current_time, min_speed
        )

        # Compute QoE gains for refiner
        qoe_gains: Dict[str, float] = {}
        for req in requests:
            if req.request_id in set(serve_ids) - set(currently_running):
                # Newly admitted requests
                gain = QoEComputer.compute_qoe_gain(
                    req, best_B, self.token_latency_fn, self.delta_t, current_time
                )
                qoe_gains[req.request_id] = gain

        # New admissions (not currently running) that require preemptions
        new_admissions = [rid for rid in serve_ids if rid not in currently_running]

        # Overhead-aware refinement
        refined_admit, refined_preempt = self.refiner.refine(
            proposed_admit=new_admissions,
            proposed_preempt=preempt_ids,
            all_requests=all_requests,
            currently_running=currently_running,
            qoe_gains=qoe_gains,
            current_time=current_time,
            batch_size=best_B
        )

        # Final serve set: currently running (minus refined preempts) + refined admits
        preempt_set = set(refined_preempt)
        final_serve = [rid for rid in currently_running if rid not in preempt_set]
        final_serve.extend(refined_admit)

        return SchedulingDecision(
            admit_resume=final_serve,
            preempt=refined_preempt
        )
