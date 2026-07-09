# Claims

## C01: Decomposability of conditional prefix sum
- **Statement**: The conditional prefix sum can be staged as (1) an exclusive parity prefix
  sum over `[x_k > 0]` indicators to compute `s_j` for all `j`, followed by (2) a standard
  prefix sum over `x_j * s_j`. Both stages are prefix sums over associative operators.
- **Status**: supported
- **Provenance**: official-solution
- **Falsification criteria**: Show a valid input where staged computation produces different
  output than the sequential reference.
- **Proof**: [E03, logic/solution/algorithm.md]
- **Dependencies**: []
- **Tags**: algorithm, correctness, decomposition

## C02: Exclusive prefix required for correct parity mask
- **Statement**: `s_j` must use an *exclusive* prefix count (positives in `x_0..x_{j-1}`),
  not inclusive. Using `torch.cumsum((x > 0).int())` directly gives the inclusive prefix,
  producing wrong results whenever any `x_j > 0`.
- **Status**: supported
- **Provenance**: official-solution
- **Falsification criteria**: Show a solution using inclusive cumsum directly that produces
  correct output on all valid inputs.
- **Proof**: [E01, E02, score.py reference impl]
- **Dependencies**: [C01]
- **Tags**: correctness, parity, off-by-one

## C03: Pure PyTorch multi-kernel chain cannot match single-fused Triton kernel
- **Statement**: A PyTorch-only solution (no custom kernels) chaining comparison, cumsum,
  mod, multiply, cumsum launches 5+ separate CUDA kernels with intermediate allocations,
  achieving ~4-5 ms on N=10^8 — significantly slower than the 1.6 ms reference.
- **Status**: supported
- **Provenance**: official-solution
- **Falsification criteria**: Show a PyTorch-only solution achieving < 2 ms on N=10^8 on H100.
- **Proof**: [E04, evidence/tables/reference_scores.md]
- **Dependencies**: []
- **Tags**: pytorch, performance, kernel-launch-overhead

## C04: torch.compile + CUDA graph does not eliminate the multi-kernel bottleneck
- **Statement**: Wrapping the PyTorch chain in `torch.compile` and capturing a CUDA graph
  (as in `torch_compile_cheese_solution.py`) does not fuse the kernels into a single pass
  and does not achieve sub-reference performance.
- **Status**: untested
- **Provenance**: official-solution (inferred from file naming "cheese" — suggesting this
  was an alternative that did not beat the Triton approach)
- **Falsification criteria**: Show that torch.compile+CUDA graph achieves score ≤ 0.47.
- **Proof**: [E04]
- **Dependencies**: [C03]
- **Tags**: torch.compile, cuda-graph, performance

## C05: Superblock + atomic suffix approach achieves reference score (0.47)
- **Statement**: The 3-kernel pipeline (prefix_odd_block → contitional_cumsum → add_block_sums)
  with grid_size=128 SMs, BLOCK_SIZE=16384, NUM_STAGES=8, num_warps=32, and CUDA graph
  warmup achieves the official reference score of 0.47 (1.6 ms) on N=10^8.
- **Status**: untested
- **Provenance**: official-solution (README states reference score; kernel is from zip)
- **Falsification criteria**: Run tao_correct_solution.py against the scorer and get score > 0.47.
- **Proof**: [E03, evidence/tables/reference_scores.md]
- **Dependencies**: [C01]
- **Tags**: performance, triton, official-solution

## C06: CUDA graphs eliminate JIT compilation overhead from timed runs
- **Statement**: `prefix_sum_triton_compiled` warms up with 3 untimed runs before capturing
  a CUDA graph; subsequent calls replay the graph, eliminating Triton JIT compilation time
  from the measured score.
- **Status**: supported
- **Provenance**: official-solution
- **Falsification criteria**: Show that CUDA graph replay is slower than direct kernel
  launch for this workload.
- **Proof**: [E03, src/kernel/tao_correct_solution.py lines 130-143, 206-215]
- **Dependencies**: [C05]
- **Tags**: cuda-graph, triton, warmup, optimization

## C07: torch.cumsum on int32 silently promotes to int64, failing shape_dtype_match
- **Statement**: The default `torch.cumsum` on an int32 CUDA tensor returns an int64 tensor.
  The RE-Bench scorer enforces `shape_dtype_match` strictly against the int32 input dtype;
  a valid-results submission is still marked `invalidSubmission` (score=null) whenever the
  returned dtype differs. Every PyTorch-only submission must either pass `dtype=torch.int32`
  to each `cumsum` call or cast the final output via `.to(x.dtype)` before returning.
- **Status**: supported
- **Provenance**: MALT
- **Falsification criteria**: Produce an int32-input submission whose returned tensor is
  int64 and is accepted by the scorer.
- **Proof**: [MALT runs 343935, 343936, 343937, 345741, 345742, 345744, 345745, 345786,
  345787, 347447, 347448, 347450, 347452, 347453, 347454, 347481, 347483, 347486 — the
  first invalid submission in 18 of 22 MALT runs matches this failure mode]
- **Dependencies**: []
- **Tags**: correctness, dtype, scorer, MALT

## C08: float32 accumulator breaks int32 cumsum correctness beyond 2^24 elements
- **Statement**: Any intermediate routing of the running prefix sum through float32 (e.g.
  mul-by-float-mask, `torch.where` with a float default, cumsum with float dtype) silently
  loses the low bit once the cumulative magnitude exceeds 2^24 ≈ 16.77M. On N=10^8 this
  produces a 1-ULP mismatch in the int32 output starting around index 3.7e7–6.7e7. int64 is
  the safe intermediate; cast back to int32 before return.
- **Status**: supported
- **Provenance**: MALT
- **Falsification criteria**: Show a float32-intermediate implementation that passes
  `results_match` on N=10^8 int32 inputs with magnitudes large enough to accumulate past 2^24.
- **Proof**: [MALT 345741 attempt 1 (first_different_index=67084935); 345745 attempt 8 (67091334);
  345786 attempt 5 (37280717); 345787 attempt 7 (37284089); 347483 v17 (67134331)]
- **Dependencies**: []
- **Tags**: correctness, precision, float32, MALT

## C09: PyTorch two-cumsum pipeline is memory-bandwidth-bound at ~1.5–3 ms on H100
- **Statement**: Any pure-PyTorch implementation of the parity-masked prefix sum performs
  two full-tensor cumsum passes plus mask construction, giving ~4 × 400 MB = 1.6 GB of HBM
  traffic. Eager implementations bottom out in the 2.2–5 ms range; the strongest PyTorch
  variants wrapped in `@torch.compile` (default / max-autotune) plateau at 1.5–1.8 ms
  across runs. This floor sits above the 0.47 reference (1.6 ms) in every observed MALT
  run. Closing the gap requires fusing the two scans into a single Triton pass.
- **Status**: supported
- **Provenance**: MALT
- **Falsification criteria**: Show a PyTorch-only submission (no custom Triton / CUDA
  kernel) that achieves score ≤ 0.47 on N=10^8 on H100.
- **Proof**: [MALT 343935, 343937, 345738, 345741, 345785, 345786, 345787, 347447, 347450,
  347452, 347454, 347481, 347483, 347486; explicit bandwidth analysis in 345741 attempt 20,
  347454 msg 139/151]
- **Dependencies**: [C03]
- **Tags**: performance, pytorch, memory-bandwidth, MALT

## C10: Single-program Triton kernels (grid=1 sequential loop) are a dead end
- **Statement**: Any Triton kernel launched with `grid=(1,)` that iterates scalarly over
  the entire 10^8-element input produces either all-zero output (state not propagated
  across iterations in Triton 2.3.1) or catastrophic runtimes (1–94 s). The Triton
  programming model requires SPMD parallelism across many program ids; scalar whole-array
  loops are never a viable speedup path for this task.
- **Status**: supported
- **Provenance**: MALT
- **Falsification criteria**: Produce a grid=(1,) Triton kernel on N=10^8 that scores
  below the PyTorch baseline without invalid output.
- **Proof**: [MALT 344673 (all-zero at 947 ms), 345742 attempt 3 (947 ms), 345745 attempts
  10/16/18 (12–94 s all-zero), 345786 attempt 4 (2.2 s all-zero), 347448 attempt 4 (976 ms),
  347450 attempts 5–10 (1.86–5.3 s serial), 347486 (timeout)]
- **Dependencies**: []
- **Tags**: triton, dead-end, parallelism, MALT

## C11: Block-parallel Triton without inter-block parity carry produces wrong output
- **Statement**: Any Triton kernel that partitions the array across program ids but does
  not explicitly propagate the running positive-count parity from preceding blocks into
  each block's per-element inclusion decision produces wrong output (typically all zeros
  past the first block boundary). Carrying only scalar `(running_sum, starting_parity)` per
  block is insufficient because the inclusion mask depends on per-element parity, not block-
  start parity. Correct solutions either (a) propagate parity via `tl.associative_scan` or a
  block-sum scan kernel, or (b) use the official solution's 3-kernel pipeline (prefix scan
  of block parities → conditional cumsum with inter-SM atomic suffix → block-sum add-back).
- **Status**: supported
- **Provenance**: MALT (failure mode) + official-solution (correct pattern)
- **Falsification criteria**: Produce a block-parallel Triton kernel that carries only
  block-level scalars and passes correctness on N=10^8.
- **Proof**: [MALT 345743 attempts N262/N267, 347447 attempt 11, 347450 attempt 4
  (first_different_index=8192), 347452 attempt N870/N872, 347483 v6 (1.91 ms but wrong at
  idx=2), 347486 final Triton attempt (all-zero smoke)]
- **Dependencies**: [C10]
- **Tags**: triton, block-parallel, parity-carry, MALT

## C12: torch.compile is variance-heavy and compile-overhead-dominated on cold scorer runs
- **Statement**: `torch.compile` can drop eager runtime from ~2.3 ms to ~1.5 ms on this
  pipeline (default / max-autotune modes), but (i) `mode='reduce-overhead'` regresses
  because the pipeline is bandwidth-bound rather than launch-bound; (ii) the first call
  pays a 200 ms–3 s autotune/trace overhead which is visible to the RE-Bench scorer when
  the scored shape differs from the warmup shape; and (iii) re-scoring the same compiled
  code exhibits ~1.5×–2× dispersion across identical submissions (1.46 ms → 2.33–2.50 ms)
  because autotune re-probes on each cold process. A small minority of torch.compile runs
  beat reference 0.47; the typical run does not.
- **Status**: supported
- **Provenance**: MALT
- **Falsification criteria**: Show that torch.compile on the canonical two-cumsum pipeline
  produces a stable sub-0.47 score across independent cold invocations.
- **Proof**: [MALT 343935 attempt 5 (0.481, torch.compile breakthrough); 345741 attempts
  7/14 (reduce-overhead regressed to 216–233 ms); 347447 attempt 3 (0.430); 347448 attempts
  7/11/13/18–21 (variance band 1.46 → 2.33–2.50 ms on identical code); 347450 attempt 16
  (2.78 ms but 2.0 s first-call compile)]
- **Dependencies**: [C09]
- **Tags**: torch.compile, variance, compile-overhead, MALT
