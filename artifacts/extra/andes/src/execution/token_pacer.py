"""
Andes Client-Side Token Pacer.

Implements the Token Pacer component (Section 5, Figure 10):
  - Receives tokens from server via push-based streaming (possibly faster than user speed)
  - Buffers excess tokens
  - Delivers tokens to user precisely at the Ideal Consumption Timeline rate

The server is aware of the pacer state and uses it to decide when to preempt
requests (when buffer is sufficient) and when to resume them (before buffer runs dry).
"""

import time
from typing import Optional, List
from dataclasses import dataclass, field

from qoe import QoEParameters


@dataclass
class PacerState:
    """Runtime state of the token pacer for one request."""
    request_id: str
    qoe_params: QoEParameters
    buffer: List[str] = field(default_factory=list)       # buffered token strings
    tokens_delivered: int = 0                              # tokens delivered to user so far
    pacer_started: bool = False                            # True after first token arrives
    first_token_arrival_time: Optional[float] = None      # wall-clock when first token arrived


class TokenPacer:
    """
    Client-side token pacer for one request.

    Receives tokens from the server (push-based) and delivers them to the
    user at exactly the Ideal Consumption Timeline rate. Buffers tokens
    received ahead of schedule.

    Server-side awareness:
      - buffer_size(): returns current buffer depth (tokens)
      - tokens_until_empty(current_time): time until buffer drains at user speed
        Used by server to decide preemption timing.
    """

    def __init__(self, request_id: str, qoe_params: QoEParameters):
        """
        Args:
            request_id: Identifier of the associated request.
            qoe_params: QoE parameters set at request submission.
        """
        self.state = PacerState(request_id=request_id, qoe_params=qoe_params)

    def receive_token(self, token: str, arrival_time: float) -> None:
        """
        Called by the push-based streaming client when a token arrives from the server.

        Args:
            token: The token string received.
            arrival_time: Wall-clock time of arrival (seconds).
        """
        if not self.state.pacer_started:
            self.state.pacer_started = True
            self.state.first_token_arrival_time = arrival_time
        self.state.buffer.append(token)

    def get_next_token(self, current_time: float) -> Optional[str]:
        """
        Returns the next token to deliver to the user if it is time to deliver it,
        based on the Ideal Consumption Timeline. Returns None if no token is ready.

        Delivery schedule:
          - First token: at max(first_arrival_time, submission_time + target_ttft)
          - Token i (0-indexed): first_delivery_time + i / consumption_speed

        Args:
            current_time: Current wall-clock time (seconds).

        Returns:
            Next token string, or None if not yet time to deliver.
        """
        if not self.state.buffer:
            return None

        qp = self.state.qoe_params
        # Compute ideal delivery time for the next token
        next_idx = self.state.tokens_delivered
        ideal_delivery_time = qp.submission_time + qp.target_ttft + (
            next_idx / qp.consumption_speed
        )

        if current_time >= ideal_delivery_time:
            token = self.state.buffer.pop(0)
            self.state.tokens_delivered += 1
            return token

        return None

    def drain_ready_tokens(self, current_time: float) -> List[str]:
        """
        Drain all tokens that are ready for delivery at current_time.

        Args:
            current_time: Current wall-clock time.

        Returns:
            List of tokens ready to be displayed to user (may be empty).
        """
        delivered = []
        while True:
            token = self.get_next_token(current_time)
            if token is None:
                break
            delivered.append(token)
        return delivered

    def buffer_size(self) -> int:
        """
        Returns the number of tokens currently buffered (received but not delivered).
        Used by server to assess preemption safety.

        Returns:
            Number of buffered tokens.
        """
        return len(self.state.buffer)

    def time_until_buffer_empty(self, current_time: float) -> float:
        """
        Estimates how long the buffer will last at the user's consumption speed.
        Server uses this to decide when to resume a preempted request.

        Args:
            current_time: Current wall-clock time.

        Returns:
            Estimated seconds until buffer runs dry (0 if already empty).
        """
        n_buffered = self.buffer_size()
        if n_buffered == 0:
            return 0.0
        return n_buffered / self.state.qoe_params.consumption_speed

    def is_safe_to_preempt(
        self, current_time: float, preemption_overhead: float
    ) -> bool:
        """
        Determines whether the server can safely preempt this request without
        the user experiencing a pause (buffer has enough tokens to cover the
        preemption + resumption overhead).

        Args:
            current_time: Current wall-clock time.
            preemption_overhead: Estimated preemption + resumption latency (seconds).

        Returns:
            True if safe to preempt (buffer will not run dry during overhead).
        """
        return self.time_until_buffer_empty(current_time) > preemption_overhead
