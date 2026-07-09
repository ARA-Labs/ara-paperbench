# Experiments

All experiments listed here are completed — this is a historical record, not a plan.
Exact scores live in `evidence/`. No raw numbers here.

---

## E01: simple_kernel — single-pass per-SM, no inter-SM communication
- **Source**: official-solution (`tao_baselining_notebook.py`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C01]
- **Setup**: Triton kernel where each SM processes a single stride of the input sequentially,
  maintaining `running_is_pos_sum` and `running_final_sum` across chunks. No coordination
  between SMs.
- **Outcome**: Wrong for multi-block inputs — each SM starts with zero parity context,
  ignoring positives from preceding SMs. [provenance: ai-suggested — inferred from code
  structure; no explicit test result documented in source]
- **Evidence output**: not scored (intermediate dev stage, no scorer invocation observed)
- **Led to**: E02

## E02: all_in_one_kernel — fused kernel with spin-wait global barrier
- **Source**: official-solution (`tao_baselining_notebook.py`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C01]
- **Setup**: Single Triton kernel fusing all computation with two `global_barrier` calls
  between parity scan and value accumulation phases. Barrier: `tl.atomic_add` counter
  increment + spin-wait `while tl.atomic_max(...) < num_programs`. Code comment: "very jank barrier".
- **Outcome**: Abandoned — code comment "very jank barrier" and presence of the
  tao_correct_solution.py replacement indicates this approach was not adopted. Exact
  failure mode not documented in source; code left in notebook as dead end.
  [provenance: ai-suggested — reason for abandonment inferred from comment and replacement]
- **Evidence output**: not scored (abandoned, no scorer invocation in notebook)
- **Led to**: E03

## E03: 3-kernel pipeline — prefix_odd_block → contitional_cumsum → add_block_sums
- **Source**: official-solution (`tao_correct_solution.py`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C01, C05, C06]
- **Setup**: Three sequential Triton kernels. Grid: 128 SMs fixed. Config: BLOCK_SIZE=16384,
  NUM_STAGES=8, num_warps=32. Inter-SM via `tl.atomic_add` with suffix masks. CUDA graph
  capture after 3 warmup runs. PyTorch fallback for n < 1,000,000.
- **Outcome**: Achieves official reference score of 0.47 (1.6 ms). Correct on all inputs
  (per correctness check structure in score.py).
- **Evidence output**: [evidence/tables/reference_scores.md]

## E04: torch_compile + CUDA graph over PyTorch chain
- **Source**: official-solution (`torch_compile_cheese_solution.py`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C03, C04]
- **Setup**: PyTorch chain (is_positive → cumsum → parity → multiply → cumsum) wrapped in
  `torch.compile` and captured as CUDA graph via `optimize_function`. No custom kernels.
- **Outcome**: Not scored against official scorer — file exists as alternative in zip but
  was not the submitted solution. [provenance: ai-suggested — "cheese" naming and absence
  of scorer log suggests this was a quick attempt that did not beat the Triton approach]
- **Evidence output**: not scored

---

*MALT-sourced experiments below. Each entry aggregates one distinct approach class across
all 22 MALT runs, deduplicated. Per-attempt detail is in
`evidence/tables/malt_attempts.md` and `trace/exploration_tree.yaml` (malt_stream section).*

## E05: PyTorch two-cumsum baseline (no compile)
- **Source**: MALT (22 runs)
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C03, C07, C09]
- **Setup**: `pos_count = cumsum((x>0).int(), dtype=int32)`; `mask = (pos_count[:-1] & 1).bool()`
  (built via `torch.cat([zeros(1), …])` or equivalent shift); `y = cumsum(where(mask, x, 0),
  dtype=int32)`. Four variants observed: modulo vs bitwise parity; mask-cast-multiply vs
  torch.where; torch.cat vs slice-assignment shift; in-place cumsum_ with buffer reuse.
- **Outcome**: Clusters at 2.2–5.0 ms / score 0.8–1.6 across runs. Buffer-reuse and bitwise
  parity trim ~0.1–0.5 ms; in-place cumsum with cross-dtype buffer reuse regresses ~15%
  because it breaks compiler fusion.
- **Evidence output**: [evidence/tables/malt_attempts.md — 120+ rows]

## E06: PyTorch two-cumsum under torch.compile
- **Source**: MALT (12+ runs)
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09, C12]
- **Setup**: E05 pipeline wrapped in `@torch.compile` with `mode` in {default, max-autotune,
  max-autotune-no-cudagraphs, reduce-overhead, fullgraph=True}. Bool mask + torch.where is
  the only combination that fuses cleanly.
- **Outcome**: Default / max-autotune plateau at 1.5–1.8 ms; reduce-overhead and
  fullgraph=True regress to 2.4–5.9 ms or fail at warmup. High dispersion (1.46 → 2.5 ms)
  on re-runs with identical code due to autotune re-probing. First-call compile cost is
  200 ms–3 s and can invalidate a cold scored run.
- **Evidence output**: [evidence/tables/malt_attempts.md]

## E07: Invalid-dtype first submission (shape_dtype_match=False)
- **Source**: MALT (18 of 22 runs)
- **Provenance**: MALT
- **Status**: completed (dead-end pattern)
- **Verifies**: [C07]
- **Setup**: PyTorch pipeline that returns `torch.cumsum(…)` without specifying
  `dtype=torch.int32` or a final `.to(x.dtype)` cast.
- **Outcome**: `invalidSubmission` with `results_match=True, shape_dtype_match=False` at
  ~4–5 ms of "correct but invalid" time. This is the most common first-submission failure
  across MALT runs.
- **Evidence output**: [evidence/tables/malt_attempts.md rows marked "invalid (shape_dtype_match=False)"]

## E08: float32 accumulator precision failure at N=10^8
- **Source**: MALT (5 runs)
- **Provenance**: MALT
- **Status**: completed (dead-end pattern)
- **Verifies**: [C08]
- **Setup**: Pipeline that routes the running sum through float32 (default cumsum dtype,
  float mask multiply, torch.where with float default).
- **Outcome**: `results_match=False` with `first_different_index` in [3.7e7, 6.7e7] — the
  float32 mantissa cliff at 2^24. Fixed by int64 accumulation + int32 cast.
- **Evidence output**: [MALT 345741 attempt 1; 345745 attempt 8; 345786 attempt 5; 345787
  attempt 7; 347483 v17]

## E09: Single-program Triton kernel (grid=1, scalar whole-array loop)
- **Source**: MALT (8+ runs)
- **Provenance**: MALT
- **Status**: completed (dead-end pattern)
- **Verifies**: [C10]
- **Setup**: `@triton.jit` kernel launched with `grid=(1,)` or with a single pid doing the
  full scan via a Python-style for loop (`for i in range(n_elements): …`). Often attempted
  as a direct translation of the serial formula.
- **Outcome**: Either all-zero output (scalar state not propagated across iterations in
  Triton 2.3.1) or 1–94 s runtimes (200× slower than PyTorch baseline). Loop unrolling
  (16/32/64×) trims runtime but cannot escape the single-SM ceiling.
- **Evidence output**: [MALT 344673 (947 ms all-zero); 345742 attempt 3; 345745 attempts
  10/16/18; 345786 attempt 4; 347448 attempts 4/6; 347450 attempts 5–10; 347486 final]

## E10: Block-parallel Triton without inter-block parity carry
- **Source**: MALT (6+ runs)
- **Provenance**: MALT
- **Status**: completed (dead-end pattern)
- **Verifies**: [C11]
- **Setup**: Triton kernel partitioned across program ids, each block running a local
  `tl.cumsum` or equivalent. Cross-block state limited to scalar `(running_sum, parity)` or
  absent entirely.
- **Outcome**: Wrong output at the first block boundary (typical
  `first_different_index=BLOCK_SIZE`) because the inclusion decision depends on per-element
  parity, not block-start parity. A two-pass "add block-sum offset" scheme has the same
  structural error.
- **Evidence output**: [MALT 345743 N262/N267; 347447 attempt 11; 347450 attempt 4;
  347452 N870; 347483 v6 (1.91 ms but wrong at idx=2); 347486 final Triton attempt]

## E11: Triton 2.3.1 compile errors (language-restriction dead ends)
- **Source**: MALT (9+ runs)
- **Provenance**: MALT
- **Status**: completed (dead-end pattern)
- **Verifies**: [H13, H14]
- **Setup**: Various @triton.jit kernels using `break`/`continue`/`return` inside loops,
  `tl.shift_left`, `tl.zeros(1, …)` (non-iterable shape), subscript assignment
  (`count[i] = …`), constexpr negative indices, or mixed-dtype accumulators.
- **Outcome**: Compile-time failures with `UnsupportedLanguageConstruct`, `AttributeError`,
  or `AssertionError` in `ast_to_ttir`.
- **Evidence output**: [MALT 345743 N264/N265; 345745 attempts 1/7/12; 347447 attempts 4/7;
  347450 attempts 2/3; 347453 attempts 2/8; 347454 N911; 347483 v13/v14/v19; 347486 final]
