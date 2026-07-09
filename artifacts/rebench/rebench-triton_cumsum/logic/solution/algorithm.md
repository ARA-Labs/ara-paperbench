# Algorithm

Source: `official_solutions/ai_rd_triton_cumsum/official_solution/tao_correct_solution.py`
and `tao_baselining_notebook.py`

## Overview

The official solution uses a **superblock + atomic suffix** 3-kernel pipeline. Rather than
a classical Blelloch scan (up-sweep / down-sweep), it assigns a fixed grid of 128 SMs to
process equal-sized stripes of the input sequentially within each SM, with inter-SM
communication via atomic add to suffix masks.

## Kernel 1: `prefix_odd_block_kernel`

**Purpose**: Compute the inclusive parity cumsum for each position — i.e., for each index,
how many positive elements have occurred up to and including that position (stored as raw
count, not mod 2). Also propagate each SM's total positive count forward to all subsequent
SMs via atomic add.

**Algorithm**:
1. Each of the 128 SMs (`pid = tl.program_id(0)`) owns a contiguous stripe of the input.
2. Iterates over its stripe in chunks of BLOCK_SIZE=16384 with software pipelining
   (`num_stages=8`), maintaining a running `running_sum` of positive elements seen so far.
3. For each chunk: loads `x`, computes `where_positive = (x > 0).to(tl.int32)`,
   computes `result = tl.cumsum(where_positive) + running_sum`, stores to intermediate buffer,
   updates `running_sum`.
4. After processing its full stripe: uses `tl.atomic_add` with a suffix mask
   (`mask = tl.arange(0, BLOCK_SUM_SIZE) > pid`) to add `running_sum` to all subsequent
   SM slots in `STATIC_MASK_CUMSUM`. This propagates the parity context forward.

**Output**: `intermediate` buffer (inclusive parity count per position) + `STATIC_MASK_CUMSUM`
(cumulative positive count from all preceding SMs, per SM).

## Kernel 2: `contitional_cumsum_kernel`

**Purpose**: Compute the conditional value prefix sum `Y`, using the parity context from
Kernel 1 to determine which elements to include.

**Algorithm**:
1. Each SM reads its stripe of `x` (offset by +1 for exclusive semantics — reads `x[j+1]`
   while the parity was computed for position `j`).
2. For each chunk: loads the intermediate parity count, adds `STATIC_MASK_CUMSUM[pid]`
   (the cumulative count from preceding SMs), takes mod 2 to get the inclusion mask,
   multiplies `x * mask`, computes cumsum, accumulates.
3. After processing stripe: uses `tl.atomic_add` with suffix mask to propagate this SM's
   value sum forward in `STATIC_RESULT_CUMSUM`.

**Output**: `y` buffer (partial value prefix sums, not yet adjusted for cross-SM offsets)
+ `STATIC_RESULT_CUMSUM` (cumulative value sum from preceding SMs, per SM).

## Kernel 3: `add_block_sums`

**Purpose**: Add the cross-SM value offset to each position in `y`.

**Algorithm**: Each SM loads `STATIC_RESULT_CUMSUM[pid]` (total value sum from all preceding
SMs) and adds it to every position in its stripe of `y`.

**Output**: Final correct `y` buffer.

## Dispatch and CUDA Graph

```python
grid = lambda meta: (128,)  # fixed grid of 128 SMs
prefix_odd_block_kernel[grid](x, intermediate, STATIC_MASK_CUMSUM, kernel_n, n, cumsum_size)
contitional_cumsum_kernel[grid](x, intermediate, y, STATIC_MASK_CUMSUM, STATIC_RESULT_CUMSUM, kernel_n, n, cumsum_size)
add_block_sums[grid](y, STATIC_RESULT_CUMSUM, kernel_n, cumsum_size)
```

For inputs with `n >= 1_000_000`, the 3-kernel sequence is captured as a CUDA graph after
3 warmup runs. Subsequent calls replay the graph, eliminating JIT overhead from timing.
For small inputs (`n < 1_000_000`), falls back to a PyTorch chain (correctness-only path).

## Development History (from `tao_baselining_notebook.py`)

The official solution evolved through three visible stages:

1. **`simple_kernel`** (single-pass, single SM): Correct within a single block, but does
   not handle multi-block inputs — each SM computes its stripe independently without
   cross-SM communication.

2. **`all_in_one_kernel`**: Attempted single-kernel design using a spin-wait barrier
   (`global_barrier` with `tl.atomic_max`). Abandoned — likely due to Triton limitations
   with while-loop based barriers or unreliable SM coordination.

3. **Final 3-kernel pipeline**: Split coordination across 3 kernels with atomic suffix
   adds. Avoids barrier limitations, allows pipelining within each kernel.

## Key Design Decisions (source: official solution code)

- **Grid size fixed at 128**: matches or slightly exceeds H100 SM count, ensuring all SMs
  are active without over-subscription.
- **BLOCK_SIZE=16384, NUM_STAGES=8, num_warps=32** (final config in tao_correct_solution.py):
  large blocks amortize launch overhead; 8-stage pipelining hides memory latency; 32 warps
  saturates SM occupancy.
- **Static cumsum buffers** (`STATIC_CUMSUMS`): pre-allocated module-level tensors avoid
  allocation overhead. One `zero_()` call resets both `STATIC_MASK_CUMSUM` and
  `STATIC_RESULT_CUMSUM` before each invocation.
- **Oversized `y` allocation**: `y_allocation_space = kernel_n + must_divisible_num` avoids
  masking in the hot path by allocating extra space beyond the valid range.
