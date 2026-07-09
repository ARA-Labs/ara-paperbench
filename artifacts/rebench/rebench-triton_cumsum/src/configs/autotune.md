# Autotune Configuration

Source: `official_solutions/ai_rd_triton_cumsum/official_solution/tao_correct_solution.py`

## Final Configuration (tao_correct_solution.py)

All three kernels share the same autotune args (single active config, others commented out):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `BLOCK_SIZE` | 16384 (1024×16) | Large blocks amortize loop overhead; commented-out alternatives: 2048, 8192, 16384×2 |
| `NUM_STAGES` | 8 | Software pipelining depth; hides HBM latency |
| `num_warps` | 32 | Fills SM warp slots; tried 8 and 16 in notebook |
| `grid_size` | 128 | Fixed, not autotuned — matches H100 SM count |
| `key` | `[]` | Autotune does not re-run for different input sizes |

The autotune config in `tao_correct_solution.py` has a single active entry (the winner),
with all alternatives commented out — indicating the sweep was done during development
and the best config was hardcoded.

## Development Config (tao_baselining_notebook.py)

The baselining notebook shows the sweep candidates that were tried:

| BLOCK_SIZE | num_warps | Status |
|-----------|-----------|--------|
| 1024×2 | 8 | commented out |
| 1024×8 | 8 | commented out |
| 1024×16 | 8 | commented out (baseline notebook used this) |
| 1024×16 | 8 | active in notebook |
| 1024×1, ×4, ×32, ×64 | 8 | commented out |
| 1024×8 | 4, 12 stage variants | commented out |

The notebook's final active config (`BLOCK_SIZE=1024*16, NUM_STAGES=8, num_warps=8`) differs
from the production config (`num_warps=32`), suggesting further tuning happened between the
notebook and the submitted solution.

## Dispatch Parameters

```python
grid_size = 128          # fixed number of SMs
cumsum_size = 128        # = next_power_of_2(grid_size), size of coordination buffers
```

These are not autotuned — hardcoded in `prefix_sum_triton_raw`.
