"""
Per-request state tracking for Andes.
Maintains QoE parameters, token delivery history, and resource usage
for all ongoing requests in the serving system.
"""

import time
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class RequestInfo:
    """
    Complete state for a single request throughout its lifecycle.
    Fed to the Token-Level Request Scheduler at every scheduling quantum.
    """
    request_id: str
    prompt_tokens: int                  # Number of input tokens
    ttft_target: float                  # Target TTFT in seconds
    consumption_speed: float            # User's token consumption speed (tokens/s)
    arrival_time: float                 # Wall-clock time of request submission
    t_delivery: List[float] = field(default_factory=list)  # Token delivery timestamps (relative to arrival)
    context_length: int = 0             # Current KV cache usage = prompt + output tokens
    is_running: bool = False            # Whether request is currently in a batch
    is_finished: bool = False           # Whether all tokens have been generated
    pacer_buffer_tokens: int = 0        # Estimated tokens buffered in client pacer


class RequestTracker:
    """
    Maintains the control state of all active requests.
    Updated on: request arrival, token generation, preemption, completion.
    Queried by: Token-Level Request Scheduler at each scheduling quantum.
    """

    def __init__(self) -> None:
        self._requests: Dict[str, RequestInfo] = {}

    def register_request(
        self,
        request_id: str,
        prompt_tokens: int,
        ttft_target: float,
        consumption_speed: float,
    ) -> None:
        """
        Register a newly arrived request.

        Args:
            request_id: Unique identifier for this request.
            prompt_tokens: Number of input (prompt) tokens.
            ttft_target: Target TTFT in seconds (from QoE parameters).
            consumption_speed: User token consumption speed (tokens/s).
        """
        info = RequestInfo(
            request_id=request_id,
            prompt_tokens=prompt_tokens,
            ttft_target=ttft_target,
            consumption_speed=consumption_speed,
            arrival_time=time.monotonic(),
            context_length=prompt_tokens,
        )
        self._requests[request_id] = info

    def record_token_generated(
        self,
        request_id: str,
        delivery_timestamp: float,
    ) -> None:
        """
        Record that a token was generated and pushed to the client pacer.

        Args:
            request_id: Request identifier.
            delivery_timestamp: Wall-clock time of token delivery,
                                relative to request arrival_time (seconds).
        """
        info = self._requests[request_id]
        info.t_delivery.append(delivery_timestamp)
        info.context_length += 1  # Each output token adds one KV cache entry

    def mark_running(self, request_id: str) -> None:
        """Mark a request as admitted/resumed into the current batch."""
        self._requests[request_id].is_running = True

    def mark_waiting(self, request_id: str) -> None:
        """Mark a request as preempted/waiting."""
        self._requests[request_id].is_running = False

    def mark_finished(self, request_id: str) -> None:
        """Mark a request as fully generated (EOS token produced)."""
        info = self._requests[request_id]
        info.is_running = False
        info.is_finished = True

    def update_pacer_buffer(self, request_id: str, buffered_tokens: int) -> None:
        """
        Update the estimated number of tokens buffered in the client-side token pacer.
        Used by the server to decide when a request can be safely preempted
        without the user experiencing a pause.

        Args:
            request_id: Request identifier.
            buffered_tokens: Number of tokens currently in the pacer buffer.
        """
        self._requests[request_id].pacer_buffer_tokens = buffered_tokens

    def get_ongoing_requests(self) -> List[RequestInfo]:
        """Return all non-finished requests (running + waiting)."""
        return [r for r in self._requests.values() if not r.is_finished]

    def get_request(self, request_id: str) -> Optional[RequestInfo]:
        """Retrieve state for a specific request."""
        return self._requests.get(request_id)

    def remove_request(self, request_id: str) -> None:
        """Remove a finished request from the tracker."""
        self._requests.pop(request_id, None)
