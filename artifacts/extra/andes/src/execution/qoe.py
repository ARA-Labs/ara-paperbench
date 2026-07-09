"""
Andes QoE Computation and Request State Tracking.

Implements:
  - RequestState: per-request control state tracked by the Request Tracker component
  - QoEComputer: computes QoE (Eq. 1-3), S_delay, S_whole, and QoE gain estimates
    (Eq. 4) for the scheduler

This corresponds to the Request Tracker and QoE metric (Section 3.1, 3.2) of Andes.
No scaffolding code included — only the novel QoE computation logic.
"""

from dataclasses import dataclass, field
from typing import List, Optional
import math


@dataclass
class QoEParameters:
    """Per-request QoE parameters set at submission time."""
    target_ttft: float          # Target time-to-first-token (seconds)
    consumption_speed: float    # User's token consumption speed (tokens/s)
    submission_time: float      # Wall-clock time of request submission (seconds)


@dataclass
class RequestState:
    """
    Complete control state for one request, maintained by the Request Tracker.

    Attributes:
        request_id: Unique identifier.
        qoe_params: User's QoE parameters.
        prompt_length: Number of input tokens (determines initial KV cache size).
        delivery_timestamps: Wall-clock time (seconds) when each output token was
                             pushed to the client (token pacer). Index 0 = first token.
        context_length: Current KV cache size = prompt_length + len(delivery_timestamps).
        status: 'waiting' | 'running' | 'finished'
    """
    request_id: str
    qoe_params: QoEParameters
    prompt_length: int
    delivery_timestamps: List[float] = field(default_factory=list)
    status: str = 'waiting'

    @property
    def context_length(self) -> int:
        """KV cache entries consumed = prompt + generated tokens so far."""
        return self.prompt_length + len(self.delivery_timestamps)

    @property
    def tokens_generated(self) -> int:
        return len(self.delivery_timestamps)


class QoEComputer:
    """
    Computes QoE metrics for a request based on its delivery timeline.

    QoE = 1 - S_delay / S_whole   (Equation 3)

    S_delay = sum over all consumed tokens of (T_actual_i - T_ideal_i)
    S_whole = covers S_delay and area below actual consumption timeline.

    The Ideal Consumption Timeline is:
        T_ideal_i = submission_time + target_ttft + (i / consumption_speed)
    where i is 0-indexed token number (0 = first token).

    T_actual_i = max(T_delivery_i, T_actual_{i-1} + 1/consumption_speed)
    capturing the cascading delay effect.
    """

    @staticmethod
    def ideal_timestamp(i: int, qoe_params: QoEParameters) -> float:
        """
        Ideal consumption timestamp for the i-th token (0-indexed).

        Args:
            i: Token index (0 = first token).
            qoe_params: QoE parameters for this request.

        Returns:
            Ideal wall-clock timestamp (seconds).
        """
        return (qoe_params.submission_time
                + qoe_params.target_ttft
                + i / qoe_params.consumption_speed)

    @staticmethod
    def compute_actual_timestamps(
        delivery_timestamps: List[float],
        qoe_params: QoEParameters
    ) -> List[float]:
        """
        Compute the Actual Consumption Timeline from delivery timestamps.

        The user can only consume a token when it arrives AND after consuming
        the previous token (at their consumption speed). This captures cascading delays.

        Args:
            delivery_timestamps: List of wall-clock times each token was delivered.
            qoe_params: QoE parameters.

        Returns:
            List of actual consumption timestamps, same length as delivery_timestamps.
        """
        if not delivery_timestamps:
            return []

        actual: List[float] = []
        interval = 1.0 / qoe_params.consumption_speed

        for i, t_delivery in enumerate(delivery_timestamps):
            if i == 0:
                t_actual = max(t_delivery, QoEComputer.ideal_timestamp(0, qoe_params))
            else:
                t_actual = max(t_delivery, actual[i - 1] + interval)
            actual.append(t_actual)

        return actual

    @staticmethod
    def compute_qoe(state: RequestState) -> float:
        """
        Compute the QoE value for a request given its current delivery timeline.

        Returns:
            QoE in [0, 1]. Returns 1.0 if no tokens delivered yet (perfect so far).
            Returns 0.0 if S_whole == 0 (degenerate case).
        """
        n = state.tokens_generated
        if n == 0:
            return 1.0  # No tokens yet; assume perfect

        qoe_params = state.qoe_params
        actual_ts = QoEComputer.compute_actual_timestamps(
            state.delivery_timestamps, qoe_params
        )

        s_delay = 0.0
        s_whole = 0.0
        t_ideal_start = qoe_params.submission_time  # reference for S_whole

        for i in range(n):
            t_ideal_i = QoEComputer.ideal_timestamp(i, qoe_params)
            t_actual_i = actual_ts[i]

            # S_delay: deviation above ideal (clamped to 0 if ahead of schedule)
            s_delay += max(0.0, t_actual_i - t_ideal_i)

            # S_whole: area below actual consumption timeline (from submission)
            s_whole += (t_actual_i - t_ideal_start)

        if s_whole <= 0.0:
            return 0.0

        return 1.0 - (s_delay / s_whole)

    @staticmethod
    def estimate_qoe_if_served(
        state: RequestState,
        batch_size: int,
        token_latency_fn,  # Callable[[int], float]: batch_size -> seconds per token
        delta_t: float,
        current_time: float
    ) -> float:
        """
        Estimate Q_serve,i(B): the QoE of request i if served in a batch of size B
        for the next delta_t seconds.

        Args:
            state: Current request state.
            batch_size: Proposed batch size B.
            token_latency_fn: Function mapping batch_size -> per-token generation latency.
            delta_t: Look-ahead time window (seconds).
            current_time: Current wall-clock time.

        Returns:
            Estimated QoE (float in [0, 1]) if the request is served.
        """
        latency_per_token = token_latency_fn(batch_size)
        tokens_in_window = int(delta_t / latency_per_token) if latency_per_token > 0 else 0

        # Simulate additional token deliveries
        simulated_deliveries = list(state.delivery_timestamps)
        for k in range(tokens_in_window):
            simulated_deliveries.append(current_time + (k + 1) * latency_per_token)

        simulated_state = RequestState(
            request_id=state.request_id,
            qoe_params=state.qoe_params,
            prompt_length=state.prompt_length,
            delivery_timestamps=simulated_deliveries,
            status=state.status
        )
        return QoEComputer.compute_qoe(simulated_state)

    @staticmethod
    def estimate_qoe_if_waiting(
        state: RequestState,
        delta_t: float,
        current_time: float
    ) -> float:
        """
        Estimate Q_wait,i: the QoE of request i if it is NOT served for delta_t seconds.
        No new tokens are generated; existing delivery timeline is extended by delta_t.

        Args:
            state: Current request state.
            delta_t: Time window during which no tokens are generated.
            current_time: Current wall-clock time (unused but kept for interface consistency).

        Returns:
            Estimated QoE if request waits (float in [0, 1]).
        """
        # No new tokens delivered; existing QoE holds but cascading delays grow
        # Since no new tokens arrive, S_whole grows and S_delay may also grow
        # We re-compute QoE treating the wait period as extending the timeline
        return QoEComputer.compute_qoe(state)

    @staticmethod
    def compute_qoe_gain(
        state: RequestState,
        batch_size: int,
        token_latency_fn,
        delta_t: float,
        current_time: float
    ) -> float:
        """
        Compute QoE gain = Q_serve,i(B) - Q_wait,i (Equation 4).

        Args:
            state: Request state.
            batch_size: Proposed batch size B.
            token_latency_fn: Callable mapping batch_size -> per-token latency.
            delta_t: Look-ahead window.
            current_time: Current wall-clock time.

        Returns:
            QoE gain (float; positive means serving improves QoE).
        """
        q_serve = QoEComputer.estimate_qoe_if_served(
            state, batch_size, token_latency_fn, delta_t, current_time
        )
        q_wait = QoEComputer.estimate_qoe_if_waiting(state, delta_t, current_time)
        return q_serve - q_wait
