# Concepts

## Conditional Prefix Sum
- **Notation**: `Y_i = sum_{j=0}^{i} x_j * s_j`
- **Definition**: A prefix sum where each element `x_j` is gated by a binary signal `s_j`
  that depends on a prefix computation over preceding elements.
- **Boundary conditions**: `Y_0 = x_0 * s_0`; `s_0 = 0` (no positives before position 0),
  so `Y_0 = 0` always.
- **Related concepts**: parity prefix sum, exclusive prefix sum

## Parity Prefix Sum
- **Notation**: `s_j = p_j mod 2`, where `p_j = count(x_k > 0 for k < j)`
- **Definition**: A binary signal derived from the mod-2 of an exclusive prefix count.
  `s_j = 1` when an odd number of positive elements precede position `j`.
- **Boundary conditions**: `s_0 = 0`; toggles at each positive element in `x`.
- **Related concepts**: exclusive prefix sum, conditional prefix sum

## Exclusive vs. Inclusive Prefix Sum
- **Definition**: An *inclusive* prefix sum at position `j` includes element `j` itself.
  An *exclusive* prefix sum at position `j` includes only elements `0..j-1`.
- **Boundary conditions**: exclusive prefix at 0 is always 0 (identity element).
- **Relevance**: `s_j` requires an exclusive prefix. `torch.cumsum` and `tl.cumsum` both
  compute inclusive. Converting: `exclusive[j] = inclusive[j] - self[j]`, or shift by 1.
- **Related concepts**: parity prefix sum

## Superblock (Fixed Grid) Scan
- **Definition**: A parallel scan strategy where a fixed number of SMs (`grid_size`) each
  process a contiguous stripe of the input sequentially, with inter-SM communication via
  atomic operations to a shared coordination buffer.
- **Boundary conditions**: requires `grid_size` ≤ coordination buffer size; each SM's
  stripe size = `ceil(N / grid_size)`.
- **Related concepts**: two-pass scan, decoupled look-back

## CUDA Graph
- **Definition**: A mechanism to record a sequence of GPU operations (kernel launches,
  memory copies) into a graph that can be replayed without CPU overhead.
- **Boundary conditions**: captures a static computation — same input shape and memory
  addresses required at replay. Different shapes need separate graphs.
- **Relevance**: eliminates Triton JIT and kernel-launch overhead from the timed run.
- **Related concepts**: warmup, software pipelining

## tl.atomic_add with Suffix Mask
- **Definition**: A Triton pattern where each program instance atomically adds a value to
  all indices *after* its own index: `tl.atomic_add(ptr + arange(0, SIZE), val * (arange(0, SIZE) > pid))`.
  This propagates each SM's total to all subsequent SMs without a separate scan kernel.
- **Boundary conditions**: requires coordination buffer size = next power of 2 ≥ grid_size;
  all SMs must complete Kernel 1 before Kernel 2 reads the buffer (sequential kernel launches enforce this).
- **Related concepts**: superblock scan, inter-SM communication

## Software Pipelining (num_stages)
- **Definition**: Triton's `num_stages` parameter in `tl.range` overlaps memory loads of
  future iterations with computation of the current iteration, hiding HBM latency.
- **Boundary conditions**: higher stages = more registers; at `num_stages=8`, register
  pressure may limit occupancy on some workloads.
- **Code ref**: `for i in range(n_iters, num_stages=NUM_STAGES)`
- **Related concepts**: memory latency hiding, BLOCK_SIZE tuning
