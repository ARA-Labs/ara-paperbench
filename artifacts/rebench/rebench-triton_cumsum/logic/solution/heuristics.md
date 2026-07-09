# Heuristics

Source: `official_solutions/ai_rd_triton_cumsum/official_solution/tao_correct_solution.py`
and `tao_baselining_notebook.py`

## H01: Fix grid size at 128 SMs regardless of input size
- **Rationale**: 128 matches H100's physical SM count. A fixed grid means each SM processes
  `n / 128` elements sequentially — predictable stripe sizes, no dynamic grid math.
- **Provenance**: official-solution
- **Sensitivity**: medium — too few SMs underutilizes the GPU; too many causes small stripes
  with high launch overhead.
- **Bounds**: valid for H100 (132 SMs); may need tuning for other GPU generations.
- **Code ref**: `tao_correct_solution.py` line `grid_size = 128`
- **Source**: official-solution

## H02: BLOCK_SIZE=16384 (1024*16) with NUM_STAGES=8 and num_warps=32
- **Rationale**: Large BLOCK_SIZE reduces the number of iterations per SM, amortizing loop
  overhead. NUM_STAGES=8 enables software pipelining to hide HBM latency. num_warps=32
  fills SM register file and warp slots.
- **Provenance**: official-solution
- **Sensitivity**: high — the baselining notebook shows multiple configs were tried
  (1024*2 through 1024*16 in autotune); the final solution hardcodes the winner.
- **Bounds**: BLOCK_SIZE must be a power of 2; Triton limit on tensor numel (~1M) applies
  only to in-kernel tensors, not loop-chunked access patterns.
- **Code ref**: `tao_correct_solution.py` autotune_args (single config, others commented out)
- **Source**: official-solution

## H03: Use static pre-allocated cumsum buffers; reset with single zero_() call
- **Rationale**: Avoids per-call allocation of the 1024-element coordination tensors.
  A single `STATIC_CUMSUMS.zero_()` resets both `STATIC_MASK_CUMSUM` and
  `STATIC_RESULT_CUMSUM` (they are views into the same buffer) with one kernel launch.
- **Provenance**: official-solution
- **Sensitivity**: low — optimization at the dispatch level, not the kernel level.
- **Bounds**: `cumsum_size = triton.next_power_of_2(grid_size) = 128` must be ≤ 1024
  (size of STATIC_MASK_CUMSUM).
- **Code ref**: `tao_correct_solution.py` lines 147-149, 154
- **Source**: official-solution

## H04: Allocate y with extra buffer space to avoid hot-path masking
- **Rationale**: Computing `must_divisible_num` and allocating `y_allocation_space = kernel_n + must_divisible_num`
  ensures kernel writes never go out of bounds, eliminating the need for `mask=` arguments
  in `tl.store` calls. Masking adds conditional logic that slows the inner loop.
- **Provenance**: official-solution
- **Sensitivity**: medium — incorrect buffer sizing causes silent memory corruption.
- **Bounds**: `kernel_n` is rounded up to the nearest multiple of `must_divisible_num`
  (itself the next power of 2 above the per-SM stripe size).
- **Code ref**: `tao_correct_solution.py` lines 158-165
- **Source**: official-solution

## H05: Warm up 3 times before capturing CUDA graph; fall back to PyTorch for small inputs
- **Rationale**: Triton JIT compilation happens on first call. CUDA graph capture requires
  a warm graph. 3 warmup runs ensure the kernel is compiled and stable before capture.
  Small inputs (< 1M) are not worth the CUDA graph overhead.
- **Provenance**: official-solution
- **Sensitivity**: low — number of warmup runs is not critical; 1-3 all work.
- **Bounds**: CUDA graph captures a static shape; different input sizes need separate graphs
  (hence `cuda_graphs` dict keyed by `x.shape[0]`).
- **Code ref**: `tao_correct_solution.py` lines 206-215
- **Source**: official-solution

## H06: Cast boolean positivity indicator to int32 before cumsum
- **Rationale**: Triton's type system is strict — arithmetic between int1 (bool) and int32
  causes CompilationError. Always cast: `(x > 0).to(tl.int32)` before any arithmetic.
- **Provenance**: official-solution
- **Sensitivity**: high — omitting the cast causes a compilation error that is hard to
  diagnose (error message mentions signedness, not the cast).
- **Bounds**: applies to all Triton versions tested (2.3.1).
- **Code ref**: `tao_correct_solution.py` line `where_positive = (x > 0).to(tl.int32)`
- **Source**: official-solution

---
*MALT-derived heuristics below (cross-run patterns observed in agent transcripts).*

## H07: Pass dtype=torch.int32 (or .to(x.dtype)) to every cumsum on the int path
- **Rationale**: Default `torch.cumsum` on int32 CUDA tensors returns int64; the RE-Bench
  scorer enforces `shape_dtype_match` strictly and rejects the submission with `score=None`
  even when `results_match=True`. This is the single most common invalid-first-submission
  failure mode across MALT runs.
- **Provenance**: MALT
- **Sensitivity**: high — every affected run burned ≥1 attempt correcting it.
- **Bounds**: applies to pure-PyTorch paths; Triton kernels avoid the promotion if they
  declare their accumulator dtype explicitly.
- **Source refs**: [MALT runs 343935/343936/343937/345741–347486 — 18 of 22 runs hit this]
- **Source**: MALT

## H08: Use int64 (not float32) for the running prefix accumulator on N≥10^8
- **Rationale**: float32 has only a 24-bit integer-exact mantissa; once the running sum
  magnitude exceeds 2^24 ≈ 16.77M (around index 3.7e7–6.7e7 on typical inputs) the low bit
  is silently lost, producing a 1-ULP mismatch in the int32 output. int64 accumulation with
  a final `.to(torch.int32)` cast avoids this at the cost of doubling intermediate memory.
- **Provenance**: MALT
- **Sensitivity**: high — silent correctness failure, not a compile error.
- **Bounds**: applies whenever cumulative sums can exceed 2^24; for smaller inputs float32
  remains safe.
- **Source refs**: [MALT 345741 attempt 1; 345745 attempt 8; 345786 attempt 5; 345787
  attempt 7; 347483 v17]
- **Source**: MALT

## H09: Build the parity mask from the *exclusive* positive-count prefix
- **Rationale**: The inclusion mask at position j must use `pos_count[:-1] & 1` (positives
  strictly before j), not the inclusive `pos_count & 1`. Agents that use
  `torch.cumsum((x>0).int()) & 1` directly, or that shift via `torch.roll(…, 1)` under
  `@torch.compile` (which may retain the wrapped-around last element), produce an
  off-by-one mismatch starting at `first_different_index=1`. Safe patterns:
  `torch.cat([zeros(1), pos_cumsum[:-1]])` or in-place slice assignment into a pre-zeroed
  buffer.
- **Provenance**: MALT (reinforces C02)
- **Sensitivity**: high — silent off-by-one.
- **Source refs**: [MALT 343935 attempts 9, 14 (torch.roll under compile); 345738 attempts
  4–6; 345742 attempt 17; 347486 verification trace]
- **Source**: MALT

## H10: Benchmark directly at N=10^8 — smaller sizes mis-rank variants
- **Rationale**: Python/launch overhead dominates at N<10^7 but the two cumsum passes
  dominate at N=10^8. Extrapolations from 1M–50M systematically mis-rank approaches at
  100M: 345785 projected 12 ms and 5 ms from 1M/10M microbenchmarks vs actual 4.25 / 1.77 ms;
  345787 "Memory Patterns" projected 3.39 ms at 50M but measured 7.61 ms at 100M. Always
  run the scoring-size benchmark before selecting a variant.
- **Provenance**: MALT
- **Sensitivity**: medium — a wrong ranking costs attempts, not correctness.
- **Source refs**: [MALT 343937 MSG 93/97; 345785 estimate vs measured; 345787 attempts 8/10]
- **Source**: MALT

## H11: Use bool masks with torch.where + torch.compile; avoid masked_fill / int8 masks
- **Rationale**: Under `torch.compile`, the canonical pipeline
  `mask = (pos_count[:-1] & 1).bool(); y = torch.cumsum(torch.where(mask, x, 0), dtype=int32)`
  fuses the mask application into the downstream cumsum. Replacing `torch.where` with
  `masked_fill_` breaks inductor fusion (in-place mutation is not folded). Replacing the
  bool mask with an int8 or x-dtype mask forces an extra dtype conversion inside the fused
  kernel and widens mask traffic. Both substitutions give ~3× regression on the same
  algorithm.
- **Provenance**: MALT
- **Sensitivity**: medium — costs ~1.5–3× on the PyTorch floor.
- **Source refs**: [MALT 347452 N867 (bool where, 1.70 ms) vs N868 (int8 mask, 4.00 ms) vs
  N877 (masked_fill, 4.52 ms); 343935 attempt 21 bool mask multiply vs attempt 20 gather]
- **Source**: MALT

## H12: torch.compile mode matters — default/max-autotune win, reduce-overhead loses
- **Rationale**: `reduce-overhead` targets kernel-launch cost, which is not the bottleneck
  for a bandwidth-bound two-cumsum scan; it regresses to ~3 ms or worse. `max-autotune`
  gives the tightest fused code but adds a 200 ms–3 s first-call autotune cost that cold
  scorer runs can charge to the submission. `max-autotune-no-cudagraphs` is a practical
  middle ground when graph capture itself is fragile. `fullgraph=True` regresses further
  and produces multi-second warmups on small calibration inputs.
- **Provenance**: MALT
- **Sensitivity**: high — wrong mode can 2–100× the scored time on a cold run.
- **Source refs**: [MALT 345741 attempts 7/14 (reduce-overhead 216–233 ms); 345738 attempt
  11 (fullgraph warmup 3.07 s); 345744 MSG 133/141/181; 347452 N867/N871/N878; 347453
  attempt 15 (compile regressed 3.72→5.73 ms on torch.compile)]
- **Source**: MALT

## H13: Triton 2.3.1 language restrictions — no break/continue/return, no tl.shift_left
- **Rationale**: Triton 2.3.1 rejects several Python control constructs inside `@triton.jit`:
  `break`, `continue`, and `return` inside for/while loops raise `UnsupportedLanguageConstruct`.
  `tl.shift_left` is not exposed (`AttributeError`). `tl.zeros(1, dtype=…)` must pass an
  iterable shape (`tl.zeros([1], …)`). Subscript assignment into block-shaped tensors
  (`count[i] = …`) and constexpr negative indices (`mask[-1]`) are rejected at
  AST-to-TTIR time. Work around with mask-gated `tl.load`/`tl.store`, scalar accumulators,
  Python `<<` on tensor values, and masked reductions (e.g. `tl.sum(tile * (offs == k))`)
  to simulate last-lane reads.
- **Provenance**: MALT
- **Sensitivity**: high — kernels that rely on any of these fail at compile time.
- **Source refs**: [MALT 345743 N264, 345745 attempts 1/7/12, 347447 attempts 4/7, 347450
  attempts 2/3, 347453 attempts 2/8, 347454 N911, 347483 v13/v14/v19, 347486 final kernel]
- **Source**: MALT

## H14: Triton 2.3.1 loop-carried variable dtype is fixed at first assignment
- **Rationale**: A variable initialized as int32 cannot be reassigned to int64 inside a
  loop or conditional branch; a tile variable cannot switch from int32 to fp32 across
  `tl.where` branches. The compiler raises AssertionError at `ast_to_ttir`. Always declare
  accumulators with their intended final dtype via `tl.zeros([], dtype=tl.int64)` (or the
  correct tl type) and avoid mixed-precision rebinding in conditional code.
- **Provenance**: MALT
- **Sensitivity**: high — silent compile failure with unhelpful error text.
- **Source refs**: [MALT 345745 attempt 7; 347452 N864, N874; 347454 N911]
- **Source**: MALT

## H15: Block-level O(n²) schemes and Python-level chunking are dead ends at N=10^8
- **Rationale**: (a) "For each output i, loop over j≤i" kernels are O(n²) globally and
  time out on N=10^8; per-block variants that recompute left-prefix state from all
  preceding blocks have the same O(num_blocks²) structure and also time out. (b)
  Python-level loops with `.item()` sync or per-chunk kernel launches pay per-chunk launch
  + host-device round-trip overhead that dominates any L2 reuse gain — measured 7×–64000×
  regressions in observed runs. Correct inter-block state propagation belongs inside a
  single kernel or a 3-kernel pipeline with atomic / scan-based coordination (per the
  official solution), not in a Python loop.
- **Provenance**: MALT (reinforces the official-solution architecture decision)
- **Sensitivity**: high — either wrong or multi-second runtimes.
- **Source refs**: [MALT 345744 N319/N321 (O(n²) all-zero); 347447 attempt 5 (3.61 ms
  chunked); 347450 attempts 5–10 (1.86–5.3 s serial); 347452 N872 timeout; 347481 N1028
  (12.9 s on 1M); 347483 v10/v16 timeouts]
- **Source**: MALT
