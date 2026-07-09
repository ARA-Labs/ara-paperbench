# Architecture

Source: `official_solutions/ai_rd_triton_cumsum/official_solution/tao_correct_solution.py`

## Component Graph

```
Input: x (int32[N], GPU)
        |
        v
[prefix_odd_block_kernel] × 128 SMs in parallel
  - Reads: x
  - Writes: intermediate (int32[N+buffer]) — inclusive parity cumsum
  - Side effect: atomic_add → STATIC_MASK_CUMSUM[128] (per-SM positive count prefix)
        |
        v
[contitional_cumsum_kernel] × 128 SMs in parallel
  - Reads: x (offset +1), intermediate, STATIC_MASK_CUMSUM
  - Writes: y (int32[N+buffer]) — conditional value prefix sum (SM-local)
  - Side effect: atomic_add → STATIC_RESULT_CUMSUM[128] (per-SM value sum prefix)
        |
        v
[add_block_sums] × 128 SMs in parallel
  - Reads: y, STATIC_RESULT_CUMSUM
  - Writes: y (in-place) — adds cross-SM offset
        |
        v
Output: y[:N] (int32[N], GPU)
```

## Global State (module-level, persistent across calls)

```python
STATIC_CUMSUMS       = torch.zeros(1024*2, dtype=torch.int32, device="cuda")
STATIC_MASK_CUMSUM   = STATIC_CUMSUMS[:1024]   # view
STATIC_RESULT_CUMSUM = STATIC_CUMSUMS[1024:]   # view
cuda_graphs          = {}  # dict: input_size → CUDAGraph
```

`STATIC_CUMSUMS.zero_()` resets both views before each invocation (single kernel launch).

## Data Flow Detail

| Buffer | Producer | Consumer | Semantics |
|--------|----------|----------|-----------|
| `intermediate[j]` | Kernel 1 | Kernel 2 | Inclusive count of positives in x[0..j] within this SM's stripe + offset from preceding SMs |
| `STATIC_MASK_CUMSUM[pid]` | Kernel 1 (atomic) | Kernel 2 | Total positive count from SMs 0..pid-1 |
| `y[j]` (after K2) | Kernel 2 | Kernel 3 | Conditional prefix sum within SM's stripe, without cross-SM offset |
| `STATIC_RESULT_CUMSUM[pid]` | Kernel 2 (atomic) | Kernel 3 | Total value sum from SMs 0..pid-1 |
| `y[j]` (after K3) | Kernel 3 | caller | Final correct conditional prefix sum |

## Call Paths

```
prefix_sum(x)                          # exported function
  └─ prefix_sum_triton_compiled(x)
       ├─ if n < 1_000_000: prefix_sum_torch(x)   # PyTorch fallback
       └─ else:
            ├─ if not in cuda_graphs: warm up 3× + capture graph
            └─ cuda_graphs[n](x)       # CUDA graph replay
                 └─ prefix_sum_triton_raw(x)
                      ├─ STATIC_CUMSUMS.zero_()
                      ├─ prefix_odd_block_kernel[128]
                      ├─ contitional_cumsum_kernel[128]
                      └─ add_block_sums[128]
```
