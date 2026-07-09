"""
Venn: Contention-Aware IRS Scheduling + Tier-Based Device Matching
Implements Algorithm 1 (Venn-Sched) and Algorithm 2 (Venn-Match) from:
"Venn: Resource Management for Collaborative Learning Jobs", MLSys 2025.

Components implemented here:
  - Request Handler      : receives job requests and device check-ins, triggers scheduling
  - Eligibility Mapper   : maps jobs to device subsets; builds Resource-Homogeneous Job Groups
  - Contention-Aware Scheduler (IRS) : Algorithm 1 (Venn-Sched)
  - Resource-Aware Device Matcher    : Algorithm 2 (Venn-Match)
  - Starvation Prevention Module     : fairness knob ε

This stub implements the CORE novel algorithms only.
No distributed scaffolding, no logging framework, no CLI.
"""

from typing import Dict, List, Set, Tuple, Optional
import random
import math


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Request Handler
# ---------------------------------------------------------------------------

class RequestHandler:
    """
    Receives resource requests from CL jobs and check-ins from edge devices.
    Triggers re-scheduling on job arrival and job completion events.

    Responsibilities (§3, Appendix A):
      - Accepts job.request(requirements, demand) → queues job
      - Accepts device.checkin(hardware_profile) → adds device to pool
      - Fires Venn-Sched + Venn-Match on each scheduling event
      - Dispatches assignment {device → job} to devices
      - Does NOT handle fault tolerance, privacy, or device selection (delegated to jobs)
    """

    def __init__(self) -> None:
        self.job_queue: List["CLJob"] = []
        self.device_pool: List["Device"] = []
        # eligibility_key -> [Device]
        self.pool_by_key: Dict[str, List["Device"]] = {}
        # eligibility_key -> [CLJob]
        self.groups: Dict[str, List["CLJob"]] = {}

    def submit_job(self, job: "CLJob") -> None:
        """Called when a CL job submits a resource request to Venn (Step 0 in Figure 6)."""
        self.job_queue.append(job)
        self.groups.setdefault(job.eligibility_key, []).append(job)
        self._trigger_scheduling()

    def checkin_device(self, device: "Device") -> None:
        """Called when an edge device checks in to Venn (Step 1 in Figure 6)."""
        self.device_pool.append(device)
        self.pool_by_key.setdefault(device.eligibility_key, []).append(device)
        self._trigger_scheduling()

    def complete_job(self, job: "CLJob") -> None:
        """Called when a job round completes; removes job and re-triggers scheduling."""
        key = job.eligibility_key
        if key in self.groups and job in self.groups[key]:
            self.groups[key].remove(job)
        self._trigger_scheduling()

    def _trigger_scheduling(self) -> Dict[str, Tuple["CLJob", List["Device"]]]:
        """
        Invokes Venn-Sched (Algorithm 1) then Venn-Match (Algorithm 2).
        Returns assignment plan {eligibility_key -> (job, devices)}.
        In production, dispatches assignments to devices (Step 2 in Figure 6).
        """
        if not self.groups or not self.pool_by_key:
            return {}
        assignments = venn_sched(self.groups, self.pool_by_key)
        # Apply matching for each served job
        refined: Dict[str, Tuple["CLJob", List["Device"]]] = {}
        for key, (job, devices) in assignments.items():
            matched_devices = venn_match(job, devices, num_tiers=3)
            refined[key] = (job, matched_devices)
        return refined


# ---------------------------------------------------------------------------
# Eligibility Mapper
# ---------------------------------------------------------------------------

def build_job_groups(jobs: List["CLJob"]) -> Dict[str, List["CLJob"]]:
    """
    Groups CL jobs into Resource-Homogeneous Job Groups G = {G_1, ..., G_n}
    where G_j = {J_i | f(J_i) = S_j}.

    Args:
        jobs: All active CL jobs.

    Returns:
        Dict mapping eligibility_key -> list of CLJob with that key.
    """
    groups: Dict[str, List["CLJob"]] = {}
    for job in jobs:
        groups.setdefault(job.eligibility_key, []).append(job)
    return groups


def build_device_pool(devices: List["Device"]) -> Dict[str, List["Device"]]:
    """
    Partitions devices by eligibility_key to form S = S_1 ∪ ... ∪ S_n.

    Note: In practice, eligibility sets can be nested (e.g., High-Performance
    devices are also eligible for General jobs). Callers should include a device
    in multiple keys when nesting applies.

    Args:
        devices: All checked-in devices.

    Returns:
        Dict mapping eligibility_key -> list of Device with that key.
    """
    pool: Dict[str, List["Device"]] = {}
    for device in devices:
        pool.setdefault(device.eligibility_key, []).append(device)
    return pool

class CLJob:
    """Represents one collaborative learning job."""
    def __init__(
        self,
        job_id: str,
        demand: int,            # D_i: number of devices required this round
        eligibility_key: str,  # key into device eligibility subsets S_k = f(J_i)
        total_remaining_demand: Optional[int] = None,  # optional multi-round lookahead
    ):
        self.job_id = job_id
        self.demand = demand
        self.eligibility_key = eligibility_key
        self.total_remaining_demand = total_remaining_demand or demand
        # Runtime profiling (populated after first round)
        self.prev_response_time: Optional[float] = None   # T_response from last round
        self.prev_schedule_time: Optional[float] = None   # T_schedule from last round
        self.time_used: float = 0.0                       # t_i for fairness knob


class Device:
    """Represents one edge device."""
    def __init__(
        self,
        device_id: str,
        eligibility_key: str,   # which S_k this device belongs to
        hardware_score: float,  # normalized composite score for tier assignment
        checkin_time: float,    # t_s: arrival time
    ):
        self.device_id = device_id
        self.eligibility_key = eligibility_key
        self.hardware_score = hardware_score
        self.checkin_time = checkin_time


# ---------------------------------------------------------------------------
# Algorithm 1: Intersection Resource Scheduling (Venn-Sched)
# ---------------------------------------------------------------------------

def venn_sched(
    job_groups: Dict[str, List[CLJob]],
    device_pool: Dict[str, List[Device]],
    epsilon: float = 0.0,
    fair_share_jcts: Optional[Dict[str, float]] = None,
    num_concurrent_jobs: int = 1,
) -> Dict[str, Tuple[CLJob, List[Device]]]:
    """
    Algorithm 1: Intersection Resource Scheduling.

    Groups CL jobs by resource-homogeneous eligibility key, then:
      1. Sorts jobs within each group by ascending remaining demand (SRDF).
      2. Generates an initial device allocation starting from the scarcest group.
      3. Greedily reallocates intersected resources across groups to minimize
         average scheduling delay.

    Args:
        job_groups: Mapping from eligibility_key -> list of CLJob in that group.
            e.g. {"general": [J1, J3], "compute_rich": [J2]}
        device_pool: Mapping from eligibility_key -> list of Device with that key.
            Note: devices with key "compute_rich" are ALSO eligible for "general"
            when eligibility is nested; caller must handle eligibility overlap
            by including devices in multiple keys as appropriate.
        epsilon: Fairness knob ε ∈ [0, ∞). 0 = pure IRS; higher = more fairness.
        fair_share_jcts: Mapping job_id -> T_i = M * sd_i (fair-share JCT).
            Required when epsilon > 0.
        num_concurrent_jobs: M (total concurrent jobs) for fair-share computation.

    Returns:
        Dict mapping eligibility_key -> (first_job_in_group, allocated_devices).
        The caller should assign allocated_devices to first_job_in_group and
        continue serving the rest of the group in order.
    """
    # ── Step 0: Apply fairness knob (starvation prevention) ──────────────
    if epsilon > 0.0 and fair_share_jcts is not None:
        job_groups = _apply_fairness_knob(job_groups, fair_share_jcts, epsilon)

    # ── Step 1: Sort within each group by ascending (adjusted) demand ─────
    sorted_groups: Dict[str, List[CLJob]] = {}
    for key, jobs in job_groups.items():
        sorted_groups[key] = sorted(jobs, key=lambda j: j.demand)

    # ── Step 2: Initial allocation — scarcest group first ─────────────────
    # Sort groups by number of eligible devices (ascending = scarcest first)
    group_keys_by_scarcity: List[str] = sorted(
        sorted_groups.keys(),
        key=lambda k: len(device_pool.get(k, []))
    )

    remaining_devices: Dict[str, List[Device]] = {
        k: list(v) for k, v in device_pool.items()
    }
    allocated: Dict[str, List[Device]] = {k: [] for k in sorted_groups}

    for key in group_keys_by_scarcity:
        eligible = remaining_devices.get(key, [])
        allocated[key] = list(eligible)
        # Remove allocated devices from remaining pool for ALL groups
        # (each device assigned to at most one group initially)
        allocated_ids = {d.device_id for d in eligible}
        for other_key in remaining_devices:
            remaining_devices[other_key] = [
                d for d in remaining_devices[other_key]
                if d.device_id not in allocated_ids
            ]

    # ── Step 3: Greedy cross-group reallocation ───────────────────────────
    # Process groups from most abundant to least abundant
    group_keys_by_abundance: List[str] = sorted(
        sorted_groups.keys(),
        key=lambda k: len(device_pool.get(k, [])),
        reverse=True
    )

    # Queue lengths (number of jobs per group, adjusted for fairness)
    queue_lengths: Dict[str, int] = {k: len(v) for k, v in sorted_groups.items()}

    for key_j in group_keys_by_abundance:
        if len(allocated[key_j]) == 0:
            continue
        eligible_j = set(d.device_id for d in device_pool.get(key_j, []))
        # Compare with groups that have fewer eligible devices and intersect
        for key_k in group_keys_by_scarcity:
            if key_k == key_j:
                continue
            eligible_k = set(d.device_id for d in device_pool.get(key_k, []))
            if len(eligible_k) >= len(eligible_j):
                continue  # key_k is not scarcer than key_j
            intersection = eligible_j & eligible_k
            if not intersection:
                continue  # no shared devices

            # Compute queue-length-to-allocated-resource ratios
            m_prime_j = _get_queue_len(key_j, queue_lengths)
            m_prime_k = _get_queue_len(key_k, queue_lengths)
            s_prime_j = max(len(allocated[key_j]), 1)
            s_prime_k = max(len(allocated[key_k]), 1)

            ratio_j = m_prime_j / s_prime_j
            ratio_k = m_prime_k / s_prime_k

            if ratio_j > ratio_k:
                # Reallocate intersected devices from key_k to key_j
                intersect_devices = [
                    d for d in allocated[key_k]
                    if d.device_id in intersection
                ]
                allocated[key_j].extend(intersect_devices)
                intersect_ids = {d.device_id for d in intersect_devices}
                allocated[key_k] = [
                    d for d in allocated[key_k]
                    if d.device_id not in intersect_ids
                ]
            else:
                break  # stop allocating from remaining groups to key_j

    # ── Assemble output: first job in each group + its allocated devices ──
    result: Dict[str, Tuple[CLJob, List[Device]]] = {}
    for key, jobs in sorted_groups.items():
        if jobs:
            result[key] = (jobs[0], allocated.get(key, []))
    return result


def _get_queue_len(key: str, queue_lengths: Dict[str, int]) -> int:
    """
    Returns the effective queue length for a job group (m').
    In full implementation this accounts for deprioritized jobs across groups.
    Here approximated as group queue length.
    """
    return queue_lengths.get(key, 0)


def _apply_fairness_knob(
    job_groups: Dict[str, List[CLJob]],
    fair_share_jcts: Dict[str, float],
    epsilon: float,
) -> Dict[str, List[CLJob]]:
    """
    Adjusts each job's demand by the fairness multiplier (t_i / T_i)^epsilon.
    Returns a new job_groups dict with adjusted demands.
    d'_i = d_i * (t_i / T_i)^epsilon
    """
    adjusted: Dict[str, List[CLJob]] = {}
    for key, jobs in job_groups.items():
        new_jobs = []
        for job in jobs:
            T_i = fair_share_jcts.get(job.job_id, 1.0)
            t_i = max(job.time_used, 1e-9)
            multiplier = (t_i / T_i) ** epsilon
            # Create a shallow copy with adjusted demand
            adj_job = CLJob(
                job_id=job.job_id,
                demand=max(1, int(math.ceil(job.demand * multiplier))),
                eligibility_key=job.eligibility_key,
                total_remaining_demand=job.total_remaining_demand,
            )
            adj_job.time_used = job.time_used
            adj_job.prev_response_time = job.prev_response_time
            adj_job.prev_schedule_time = job.prev_schedule_time
            new_jobs.append(adj_job)
        adjusted[key] = new_jobs
    return adjusted


# ---------------------------------------------------------------------------
# Algorithm 2: Tier-Based Device Matching (Venn-Match)
# ---------------------------------------------------------------------------

def venn_match(
    job: CLJob,
    candidate_devices: List[Device],
    num_tiers: int,
    tier_speedup_factors: Optional[List[float]] = None,
) -> List[Device]:
    """
    Algorithm 2: Tier-based device-to-job matching.

    Partitions candidate_devices into V tiers by hardware_score.
    Randomly selects one tier u. Applies tier-based restriction to job
    only if it reduces JCT: condition 1 + c_i > V + g_u * c_i.

    Args:
        job: The CL job being served (must have prev_response_time and
             prev_schedule_time set from the previous round for profiling).
        candidate_devices: Devices allocated to this job by venn_sched.
        num_tiers: V — number of hardware capacity tiers.
        tier_speedup_factors: Pre-computed g_v = t_v / t_0 for each tier v.
            If None, profiling mode: return all devices (cold start).

    Returns:
        Subset of candidate_devices assigned to this job after tier filtering.
    """
    # Cold start: no profile data — return all devices and profile this round
    if (job.prev_response_time is None or
            job.prev_schedule_time is None or
            tier_speedup_factors is None):
        return candidate_devices

    if not candidate_devices:
        return candidate_devices

    # Partition devices into V tiers by hardware_score (ascending)
    sorted_devices = sorted(candidate_devices, key=lambda d: d.hardware_score)
    tier_size = max(1, len(sorted_devices) // num_tiers)
    tiers: List[List[Device]] = []
    for v in range(num_tiers):
        start = v * tier_size
        end = start + tier_size if v < num_tiers - 1 else len(sorted_devices)
        tiers.append(sorted_devices[start:end])

    # Randomly select a tier u for this job (promotes device diversity)
    u = random.randint(0, num_tiers - 1)
    g_u = tier_speedup_factors[u] if u < len(tier_speedup_factors) else 1.0

    # Compute c_i = T_response / T_schedule from previous round
    c_i = job.prev_response_time / max(job.prev_schedule_time, 1e-9)

    # Apply tier-based matching condition: 1 + c_i > V + g_u * c_i
    # Equivalent: (1 - g_u) * c_i > V - 1
    if (num_tiers + g_u * c_i) < (c_i + 1):
        return tiers[u]  # restrict to tier u
    else:
        return candidate_devices  # no tier restriction


def compute_tier_speedup_factors(
    tier_response_times: List[float],  # 95th-percentile response time per tier [t_1, ..., t_V]
    baseline_response_time: float,     # t_0: 95th-percentile without tiering
) -> List[float]:
    """
    Computes g_v = t_v / t_0 for each tier v.
    Response times should be 95th-percentile values (log-normal tail latency).

    Args:
        tier_response_times: List of per-tier 95th-percentile response times.
        baseline_response_time: 95th-percentile response time without tiering (t_0).

    Returns:
        List of speed-up factors g_v ∈ (0, 1] for each tier.
    """
    if baseline_response_time <= 0:
        return [1.0] * len(tier_response_times)
    return [t_v / baseline_response_time for t_v in tier_response_times]
