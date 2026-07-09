# MALT Attempts — triton_cumsum

Source: 22 MALT runs (`code/rebench-pipeline/malt_outputs/triton_cumsum/run_*/`).
Reference score = 0.47 (ln-ms). Attempts with `score < 0.47` are excluded per PIPELINE.md §3.7.

Score = `ln(time_ms)`; lower is faster. `status: invalid` = correctness failure or dtype mismatch.

| run_id | model | attempt | approach | score (ln) | time (ms) | status |
|--------|-------|---------|----------|-----------|----------|--------|
| 343935 | sonnet-4 | 1 | PyTorch two-cumsum + bool mask, default cumsum dtype (output int64) | null | 5.143 | invalid (shape_dtype_match=False) |
| 343935 | sonnet-4 | 2 | PyTorch two-cumsum + bool mask, explicit int32 cumsum dtype | 0.9491 | 2.584 | valid |
| 343935 | sonnet-4 | 3 | Memory-alloc-optimized PyTorch pipeline (after torch.where out= TypeError fix) | 0.8689 | 2.384 | valid |
| 343935 | sonnet-4 | 4 | Streamlined variant using torch.cat to build prev-count | 0.9046 | 2.471 | valid |
| 343935 | sonnet-4 | 5 | @torch.compile on two-cumsum pipeline (breakthrough) | 0.4807 | 1.617 | valid |
| 343935 | sonnet-4 | 6 | Aggressive inlined fusion on torch.compile base | 0.4933 | 1.638 | valid |
| 343935 | sonnet-4 | 7 | Revert + re-score of torch.compile base | 0.5095 | 1.664 | valid |
| 343935 | sonnet-4 | 8 | Micro-opt: prev_count & 1 int32 mask (no bool tensor) | 0.4889 | 1.631 | valid |
| 343935 | sonnet-4 | 9 | torch.roll(pos_count,1) with [0]=0 for prev-count | null | 1.595 | invalid (results_match=False, off-by-one at i=2) |
| 343935 | sonnet-4 | 10 | Re-score of compiled stable base | 0.4888 | 1.630 | valid |
| 343935 | sonnet-4 | 11 | Bitwise AND odd check + torch.cat prev-shift | 0.5207 | 1.683 | valid |
| 343935 | sonnet-4 | 12 | Single-pass arange + pos_count[indices-1] + torch.where guard | null | 1.584 | invalid (results_match=False, negative-index wrap) |
| 343935 | sonnet-4 | 13 | Re-score of compiled stable base (best valid of run) | 0.4789 | 1.614 | valid |
| 343935 | sonnet-4 | 14 | torch.roll + bitwise odd-check retry under torch.compile | null | 1.597 | invalid (results_match=False, solution all zeros) |
| 343935 | sonnet-4 | 15 | Re-score of stable compiled base | 0.4823 | 1.620 | valid |
| 343935 | sonnet-4 | 16 | Custom Triton @triton.jit kernel loaded via exec() | null | null | invalid (OSError in inspect.getsourcelines; Triton JIT source introspection failed) |
| 343935 | sonnet-4 | 17 | Re-score of compiled stable base | 0.4801 | 1.616 | valid |
| 343935 | sonnet-4 | 18 | Alternative algorithmic re-expression on compiled base | 0.5044 | 1.656 | valid |
| 343935 | sonnet-4 | 19 | Re-score of compiled stable base | 0.4805 | 1.617 | valid |
| 343935 | sonnet-4 | 20 | Advanced-indexing / gather-based conditional build | 1.3605 | 3.898 | valid |
| 343935 | sonnet-4 | 21 | Final submission: compiled two-cumsum base | 0.4808 | 1.617 | valid |
| 343936 | sonnet-4 | 1 | torch cumsum chain, dtype not cast to int32 | null | 4.9038 | invalid (shape_dtype_match=False; int32→int64 promotion) |
| 343936 | sonnet-4 | 2 | torch cumsum chain + explicit .to(int32) on final result | 1.6647 | 5.2843 | valid |
| 343936 | sonnet-4 | 3 | micro-opt: pre-alloc zeros, drop torch.cat | 1.5564 | 4.7417 | valid |
| 343936 | sonnet-4 | 4 | re-score of attempt 3 (same file) | 1.5535 | 4.7281 | valid |
| 343936 | sonnet-4 | 5 | memory reuse: fold parity + x mul into pos_counts buffer | 1.3391 | 3.8157 | valid |
| 343936 | sonnet-4 | 6 | tensor opt: torch.empty + bitwise AND for parity | 1.2566 | 3.5136 | valid |
| 343936 | sonnet-4 | 7 | hyper opt: aggressive in-place torch ops | 0.8094 | 2.2466 | valid |
| 343936 | sonnet-4 | 8 | zero-alloc: single buffer, torch.cumsum(..., out=work) in-place | 0.6602 | 1.9352 | valid |
| 343936 | sonnet-4 | 9 | "memory perfect" variant (slight regression of attempt 8) | 0.6672 | 1.9488 | valid |
| 343936 | sonnet-4 | 10 | re-score after reverting to attempt 8 method | 0.6671 | 1.9486 | valid |
| 343937 | sonnet-4 | 1 | PyTorch cumsum chain, initial dtype bug (indicators via .int() promoted to int64) | null | 4.645 | invalid (shape_dtype_match=False) |
| 343937 | sonnet-4 | 2 | PyTorch cumsum chain, dtype fixed (indicators -> cumsum -> shift -> conditional -> cumsum) | 1.613 | 5.018 | valid |
| 343937 | sonnet-4 | 3 | PyTorch cumsum chain, regression from micro-optimization attempts | 1.706 | 5.505 | valid |
| 343937 | sonnet-4 | 4 | PyTorch cumsum chain with hybrid micro-optimizations | 1.582 | 4.866 | valid |
| 343937 | sonnet-4 | 5 | Buffer-reuse PyTorch cumsum chain (two persistent buffers, out= everywhere) | 0.835 | 2.305 | valid |
| 343937 | sonnet-4 | 6 | Buffer-reuse variant with zero_tensor allocation removed (regression) | 1.412 | 4.106 | valid |
| 344673 | opus-4 | 1 | Triton single-pass kernel fusing positive-count tracking and conditional accumulation | null | 947.28 | invalid (wrong output, all zeros; first_different_index=2) |
| 344673 | opus-4 | 2 | Same single-pass Triton kernel, reordered so positive-count updates after inclusion test | null | 947.31 | invalid (wrong output, all zeros; first_different_index=4) |
| 345738 | opus-4 | 1 | PyTorch 5-pass (indicators, cumsum, parity mask, multiply, cumsum); int32 forced | null | 4.6396 | invalid (shape_dtype_match=False) |
| 345738 | opus-4 | 2 | PyTorch 5-pass with dtype preservation | 1.6118 | 5.0118 | valid |
| 345738 | opus-4 | 3 | Chunked PyTorch with cross-chunk running-count carry | 2.6280 | 13.8464 | valid |
| 345738 | opus-4 | 4 | Fused Triton mask-and-multiply kernel reading pos_cumsum[idx-1] | null | 3.5071 | invalid (results_match=False, first_diff=1) |
| 345738 | opus-4 | 5 | Fused Triton kernel with zeros_like buffers (attempt 1) | null | 3.6945 | invalid (results_match=False, first_diff=3) |
| 345738 | opus-4 | 6 | Fused Triton kernel with zeros_like buffers (attempt 2) | null | 3.6814 | invalid (results_match=False, first_diff=3) |
| 345738 | opus-4 | 7 | PyTorch 5-pass with bitwise-AND parity | 1.5188 | 4.5669 | valid |
| 345738 | opus-4 | 8 | torch.jit.script wrapper over PyTorch pipeline | 1.8531 | 6.3794 | valid |
| 345738 | opus-4 | 9 | Clean PyTorch baseline (rollback) | 1.5182 | 4.5640 | valid |
| 345738 | opus-4 | 10 | torch.compile(mode='max-autotune') over PyTorch pipeline | 1.3760 | 3.9592 | valid |
| 345738 | opus-4 | 11 | torch.compile(fullgraph=True) hand-fused body | 1.7690 | 5.8651 | valid |
| 345738 | opus-4 | 12 | Segmented PyTorch with per-segment running-count carry | 1.8572 | 6.4056 | valid |
| 345738 | opus-4 | 13 | Final: torch.compile max-autotune (rerun of attempt 10) | 1.4037 | 4.0703 | valid |
| 345741 | opus-4 | 1 | PyTorch pipeline, float intermediates (positive mask -> cumsum -> mod2 -> multiply -> cumsum) | null | 4.712 | invalid (wrong output, first_different_index=67084935) |
| 345741 | opus-4 | 2 | PyTorch pipeline, integer-only (int32 mask, int64 cumsum, cast back) | 1.7238 | 5.606 | valid |
| 345741 | opus-4 | 3 | PyTorch pipeline with minor tweak to drop intermediate bool | 1.7168 | 5.567 | valid |
| 345741 | opus-4 | 4 | int8 positive mask + torch.compile max-autotune, dtype not cast back | null | 4.536 | invalid (shape_dtype_match=False) |
| 345741 | opus-4 | 5 | int8 positive mask + dtype fix to int32 (best valid score this run) | 0.8303 | 2.294 | valid |
| 345741 | opus-4 | 6 | .bool() method called in compiled context, module import failed | null | null | invalid (RuntimeError: Tensor has no attribute bool) |
| 345741 | opus-4 | 7 | torch.compile mode='max-autotune-no-cudagraphs' on same pipeline | 5.3796 | 216.946 | valid (but compile-time dominated) |
| 345741 | opus-4 | 8 | Chunked processing wrapper over PyTorch pipeline | 1.9368 | 6.937 | valid |
| 345741 | opus-4 | 9 | 'v2' variant keeping cumsum in int32 throughout | 0.8974 | 2.453 | valid |
| 345741 | opus-4 | 10 | Re-run of best pipeline (variance) | 1.3202 | 3.744 | valid |
| 345741 | opus-4 | 11 | Cache-friendly chunking fully enabled | 2.8335 | 17.004 | valid |
| 345741 | opus-4 | 12 | 'Minimal operations' variant, fewer explicit intermediates | 1.4697 | 4.348 | valid |
| 345741 | opus-4 | 13 | In-place masking with clone() and single cumsum | 1.2180 | 3.380 | valid |
| 345741 | opus-4 | 14 | torch.compile backend='inductor' mode='reduce-overhead' | 5.4550 | 233.936 | valid (but compile-time dominated) |
| 345741 | opus-4 | 15 | Revert to N464 baseline | 1.3238 | 3.758 | valid |
| 345741 | opus-4 | 16 | Triton single-pass sequential kernel (scored path still PyTorch) | 1.3260 | 3.766 | valid |
| 345741 | opus-4 | 17 | 'Flip pattern' vectorized reformulation (same primitives) | 1.4838 | 4.410 | valid |
| 345741 | opus-4 | 18 | Re-run baseline | 1.3192 | 3.741 | valid |
| 345741 | opus-4 | 19 | 'Radical back-to-basics' (surface rewrite of same primitives) | 1.3753 | 3.956 | valid |
| 345741 | opus-4 | 20 | Re-run baseline with memory-bandwidth analysis printed | 1.3217 | 3.750 | valid |
| 345741 | opus-4 | 21 | Second 'single-pass' Triton draft (scored path unchanged) | 1.3177 | 3.735 | valid |
| 345741 | opus-4 | 22 | Final re-score (1) | 1.3335 | 3.794 | valid |
| 345741 | opus-4 | 23 | Final re-score (2) | 1.3435 | 3.833 | valid |
| 345741 | opus-4 | 24 | Final re-score (3) | 1.3212 | 3.748 | valid |
| 345742 | opus-4 | 1 | PyTorch pipeline (is_positive int32 cumsum, shift, parity mask, cumsum) without explicit dtype cast | 1.5457 | 4.691 | valid |
| 345742 | opus-4 | 2 | PyTorch pipeline, missing final int32 cast; torch.cumsum upcast to int64 | null | 5.250 | invalid (shape/dtype mismatch) |
| 345742 | opus-4 | 3 | Single-program Triton fused kernel over full array | null | 947.206 | invalid (wrong output, first_different_index=3) |
| 345742 | opus-4 | 4 | PyTorch pipeline retry; dtype bug recurred | null | 5.114 | invalid (shape/dtype mismatch) |
| 345742 | opus-4 | 5 | PyTorch pipeline with explicit int32 cast of final cumsum | 1.7062 | 5.508 | valid |
| 345742 | opus-4 | 6 | torch.compile (default) over the fixed PyTorch pipeline | 1.2646 | 3.542 | valid |
| 345742 | opus-4 | 7 | Hand-rewritten eager-mode PyTorch variant (no torch.compile) | 1.5433 | 4.680 | valid |
| 345742 | opus-4 | 8 | torch.jit.script over the PyTorch pipeline | 1.6212 | 5.059 | valid |
| 345742 | opus-4 | 9 | torch.compile + int8 positive indicator only | 1.2991 | 3.666 | valid |
| 345742 | opus-4 | 10 | torch.compile(mode="max-autotune") + int32 pipeline | 1.2096 | 3.352 | valid |
| 345742 | opus-4 | 11 | max-autotune + collapsed single-expression body | 1.1622 | 3.197 | valid |
| 345742 | opus-4 | 12 | uint8 indicator AND uint8 parity-count intermediate + max-autotune | 0.5874 | 1.799 | valid |
| 345742 | opus-4 | 13 | Same, but torch.compile(mode="reduce-overhead") | 0.8697 | 2.386 | valid |
| 345742 | opus-4 | 14 | Attempted CUDA graph capture with 1000-element warmup | null | null | invalid (TorchRuntimeError broadcast 100M vs 1000) |
| 345742 | opus-4 | 15 | Re-submitted uint8 + max-autotune pipeline (variance) | 0.7008 | 2.015 | valid |
| 345742 | opus-4 | 16 | uint8 pipeline with inline mask (no separate include_mask tensor) | 0.6164 | 1.852 | valid |
| 345742 | opus-4 | 17 | torch.masked_fill variant with off-by-one count shift | null | 3.764 | invalid (wrong output, first_different_index=1) |
| 345742 | opus-4 | 18 | Restored uint8 + max-autotune pipeline | 0.5854 | 1.796 | valid |
| 345742 | opus-4 | 19 | Hybrid: custom Triton kernel for small-n + uint8 PyTorch for large-n | 0.5840 | 1.793 | valid |
| 345742 | opus-4 | 20 | torch.jit.script + uint8 pipeline (tensor.bool() call) | null | null | invalid (RuntimeError: Tensor has no method 'bool') |
| 345742 | opus-4 | 21 | torch._dynamo.optimize wrapper imported inside function | null | null | invalid (UnboundLocalError on 'torch') |
| 345742 | opus-4 | 22 | Re-submitted uint8 + max-autotune pipeline | 0.5865 | 1.798 | valid |
| 345742 | opus-4 | 23 | torch.where-based mask application (uint8 pipeline) | 0.6198 | 1.858 | valid |
| 345742 | opus-4 | 24 | int8 cumsum for parity counter (result buf int64 then cast); max-autotune | 0.5217 | 1.685 | valid |
| 345743 | opus-4 | 1 | PyTorch two-cumsum baseline; output dtype int64 instead of int32 | null | 4.881858825683594 | invalid (shape_dtype_match=False) |
| 345743 | opus-4 | 2 | PyTorch two-cumsum baseline with int32 cast | 0.9880619261179995 | 2.686023712158203 | valid |
| 345743 | opus-4 | 3 | Two-pass Triton block kernel (local + offset); wrong cross-block logic | null | 805.9072494506836 | invalid (results_match=False at idx 1026) |
| 345743 | opus-4 | 4 | PyTorch baseline for small + chunked PyTorch for large inputs | 1.5163273457028157 | 4.555463790893555 | valid |
| 345743 | opus-4 | 5 | Single-program Triton sequential kernel; `tl.zeros(1,...)` compile error | null | null | invalid (CompilationError: 'int' object is not iterable) |
| 345743 | opus-4 | 6 | Block-based Triton fallback for large inputs; block-boundary zeros | null | 4058.4092140197754 | invalid (results_match=False at idx 65536) |
| 345743 | opus-4 | 7 | Simplified PyTorch: cumsum(positive) → parity mask → masked cumsum | 0.7823189172222844 | 2.1865367889404297 | valid |
| 345743 | opus-4 | 8 | PyTorch two-cumsum wrapped in @torch.compile(mode='max-autotune') | 0.8888563651462121 | 2.4323463439941406 | valid |
| 345743 | opus-4 | 9 | PyTorch two-cumsum restructured with clone() + in-place ops | 0.9065387456072115 | 2.475738525390625 | valid |
| 345743 | opus-4 | 10 | torch.jit.script-compiled two-cumsum pipeline | 0.7937030050387626 | 2.2115707397460938 | valid |
| 345743 | opus-4 | 11 | JIT-scripted PyTorch two-cumsum with tighter op fusion (run best-tie) | 0.6936706107461678 | 2.001047134399414 | valid |
| 345743 | opus-4 | 12 | Simplified uncompiled PyTorch after torch.compile(reduce-overhead) failed | 0.8360245215442828 | 2.3071765899658203 | valid |
| 345743 | opus-4 | 13 | Cache-optimized Triton kernel; silently returns all zeros past idx 5 | null | 969.2699909210205 | invalid (results_match=False at idx 5) |
| 345743 | opus-4 | 14 | PyTorch two-cumsum pipeline rerun after Triton dead end | 0.8394288679487109 | 2.315044403076172 | valid |
| 345743 | opus-4 | 15 | PyTorch two-cumsum with memory-bandwidth tweaks (no algorithmic change) | 0.8424110286245395 | 2.321958541870117 | valid |
| 345743 | opus-4 | 16 | JIT-scripted two-cumsum rerun (N272 repeat) | 0.6967636420010043 | 2.0072460174560547 | valid |
| 345743 | opus-4 | 17 | JIT-scripted two-cumsum final submission | 0.6930746986851508 | 1.9998550415039062 | valid |
| 345744 | opus-4 | 1 | PyTorch 4-pass pipeline, default cumsum dtype (int64 output) | null | 4585.74 | invalid (shape_dtype mismatch) |
| 345744 | opus-4 | 2 | Fixed O(n^2) small-path Triton kernel; large path still default cumsum dtype | null | 4573.58 | invalid (shape_dtype mismatch) |
| 345744 | opus-4 | 3 | PyTorch 4-pass with explicit dtype=int32 cumsum | 0.8078 | 2243.04 | valid |
| 345744 | opus-4 | 4 | Replace torch.cat shift with mask[1:] assignment | 0.8422 | 2321.48 | valid |
| 345744 | opus-4 | 5 | torch.roll shift + bitwise AND parity | 0.8826 | 2417.09 | valid |
| 345744 | opus-4 | 6 | torch.where masking instead of multiply | 0.8650 | 2374.89 | valid |
| 345744 | opus-4 | 7 | Minimal PyTorch 4-pass, no micro-tricks | 0.8043 | 2235.17 | valid |
| 345744 | opus-4 | 9 | torch.compile mode=max-autotune + medium Triton kernel | 0.4992 | 1647.47 | valid |
| 345744 | opus-4 | 11 | In-place cumsum_ with buffer reuse | 0.9512 | 2588.75 | valid |
| 345744 | opus-4 | 12 | Fused O(n^2) single-pass Triton kernel for N>=1e7 | null | 1514.67 | invalid (all-zero output) |
| 345744 | opus-4 | 14 | torch.jit.script mask + torch.compile mode=reduce-overhead | 0.5281 | 1695.63 | valid |
| 345744 | opus-4 | 16 | Grid-stride single-pass Triton kernel, O(n^2) inner loop | null | 3040.55 | invalid (all-zero output) |
| 345745 | opus-4 | 1 | Single-threaded Triton @jit kernel, sequential Python loop | 8.9708 | 7869.84 | valid |
| 345745 | opus-4 | 2 | PyTorch 3-pass cumsum pipeline (dtype not int32) | null | 4.42 | invalid (shape/dtype mismatch) |
| 345745 | opus-4 | 3 | PyTorch 3-pass cumsum with .to(int32) cast | 1.5726 | 4.82 | valid |
| 345745 | opus-4 | 4 | PyTorch 3-pass, simplified ordering | 1.5165 | 4.56 | valid |
| 345745 | opus-4 | 5 | PyTorch 3-pass, bool mask variant | 1.5181 | 4.56 | valid |
| 345745 | opus-4 | 6 | PyTorch 3-pass, int64 intermediate for x*mask | 1.5211 | 4.58 | valid |
| 345745 | opus-4 | 7 | Two-kernel Triton with block-offset (compile error) | null | null | invalid (compile: loop-carried int32/int64 mismatch) |
| 345745 | opus-4 | 8 | Float32 intermediate cumsum for speed | null | 4.35 | invalid (results mismatch at idx 67091334, fp32 precision loss) |
| 345745 | opus-4 | 9 | PyTorch 3-pass int64 intermediate (retest) | 1.5873 | 4.89 | valid |
| 345745 | opus-4 | 10 | Triton: per-thread scan 'count all positives before chunk' | null | 12393.27 | invalid (O(n^2) work, output all zeros) |
| 345745 | opus-4 | 11 | PyTorch 3-pass + torch.compile (default) | 1.3976 | 4.05 | valid |
| 345745 | opus-4 | 12 | Triton: in-kernel result[i] = ... assignment | null | null | invalid (compile: AssertionError on scalar indexed assignment) |
| 345745 | opus-4 | 13 | PyTorch 3-pass + torch.compile max-autotune | 1.5436 | 4.68 | valid |
| 345745 | opus-4 | 14 | PyTorch variant with uninitialized torch.empty mask | null | 4.49 | invalid (shape/dtype mismatch) |
| 345745 | opus-4 | 15 | PyTorch 3-pass baseline (retest) | 1.5855 | 4.88 | valid |
| 345745 | opus-4 | 16 | Triton: grid=(1,) single-thread kernel (2nd attempt) | null | 94072.94 | invalid (O(n^2), output all zeros) |
| 345745 | opus-4 | 17 | PyTorch + torch.compile reduce-overhead + torch.where | 1.3699 | 3.94 | valid |
| 345745 | opus-4 | 18 | Triton: grid=(1,) sequential kernel (3rd attempt) | null | 1280.06 | invalid (output all zeros) |
| 345745 | opus-4 | 19 | PyTorch 3-pass + torch.compile (retest) | 1.3473 | 3.85 | valid |
| 345745 | opus-4 | 20 | PyTorch + torch.compile max-autotune-no-cudagraphs | 1.2780 | 3.59 | valid |
| 345745 | opus-4 | 21 | PyTorch + torch.compile max-autotune-no-cudagraphs (re-measure) | 1.1153 | 3.05 | valid |
| 345745 | opus-4 | 22 | PyTorch + torch.compile max-autotune-no-cudagraphs (final re-measure) | 1.3012 | 3.67 | valid |
| 345785 | sonnet-4 | 1 | PyTorch pos_mask + shifted cumsum + masked cumsum ("Ultra Optimized") | 0.5778 | 1.7822 | valid |
| 345785 | sonnet-4 | 2 | Same algorithm, "Chunked Optimized" variant selection (PyTorch view/stride tweaks) | 0.5793 | 1.7848 | valid |
| 345785 | sonnet-4 | 3 | "Math Reformulation" — same 2-cumsum algorithm, op reordering (best of run) | 0.5690 | 1.7664 | valid |
| 345785 | sonnet-4 | 4 | Final solution.py rewrite after token-budget pressure; same pipeline | 0.5764 | 1.7796 | valid |
| 345786 | sonnet-4 | 1 | 4-step PyTorch+Triton hybrid, cumsum returns int64 (no cast back) | null | 3719.57 | invalid (dtype mismatch) |
| 345786 | sonnet-4 | 2 | 4-step hybrid, int32 preserved via explicit cast | 1.7102 | 5530.12 | valid |
| 345786 | sonnet-4 | 3 | Earlier 4-step valid variant (from score-history dump) | 1.5518 | 4719.73 | valid |
| 345786 | sonnet-4 | 4 | Single-thread Triton sequential scan kernel | null | 2176912.55 | invalid (all-zero output, results_match=False) |
| 345786 | sonnet-4 | 5 | float32 intermediate cumsum for speed | null | 3480.20 | invalid (precision freeze at idx 37,280,717) |
| 345786 | sonnet-4 | 6 | int64 intermediate cumsum, int32 final cast | 1.4735 | 4364.49 | valid |
| 345786 | sonnet-4 | 7 | BLOCK_SIZE=8192, PyTorch positive-mask, fused Triton filter | 1.2171 | 3377.44 | valid |
| 345786 | sonnet-4 | 8 | Added CUDA stream + torch.empty pre-allocation | 1.3217 | 3749.61 | valid |
| 345786 | sonnet-4 | 9 | Bitwise-AND parity (prefix & 1) replacing modulo | 1.1989 | 3316.40 | valid |
| 345786 | sonnet-4 | 10 | Pure PyTorch (no Triton) — missing import torch | null | null | invalid (NameError) |
| 345786 | sonnet-4 | 11 | torch.where(prefix & 1, x, 0) with Long condition | null | null | invalid (where requires bool condition) |
| 345786 | sonnet-4 | 12 | Pure PyTorch with (prefix & 1).bool() fix | 1.6384 | 5146.74 | valid |
| 345786 | sonnet-4 | 13 | Hybrid reverted with super-optimized bitwise filter + out= cumsum | 1.2197 | 3386.02 | valid |
| 345786 | sonnet-4 | 14 | Custom Triton work-efficient parallel scan replacing torch.cumsum | 1.3604 | 3897.91 | valid |
| 345786 | sonnet-4 | 15 | Adaptive BLOCK_SIZE + eviction-policy hints + cumsum out= | 1.1348 | 3110.41 | valid |
| 345786 | sonnet-4 | 16 | 32KB BLOCK_SIZE, .cg/.wb cache hints, mul-filter, torch.empty | 1.0924 | 2981.42 | valid |
| 345786 | sonnet-4 | 17 | 64KB BLOCK_SIZE, .evict_last + .cg combined modifiers | null | null | invalid (PTX codegen: incompatible cache modifiers) |
| 345786 | sonnet-4 | 18 | 32KB BLOCK_SIZE with compatible .cg/.wb only | 1.0811 | 2947.81 | valid (best in run) |
| 345786 | sonnet-4 | 19 | Mathematical-optimization reformulation (details not recorded) | 1.6228 | 5067.35 | valid |
| 345786 | sonnet-4 | 20 | Re-score of reverted 32KB hybrid best | 1.1152 | 3050.33 | valid |
| 345786 | sonnet-4 | 21 | Final verification score on same solution | 1.1094 | 3032.68 | valid |
| 345787 | sonnet-4 | 1 | PyTorch pipeline, output not cast to int32 | null | 4.732 | invalid (shape_dtype_match=False) |
| 345787 | sonnet-4 | 2 | PyTorch pipeline (cumsum/shift/parity/cumsum) with int32 cast | 1.644 | 5.175 | valid |
| 345787 | sonnet-4 | 3 | Aggressive V2: fewer intermediate allocations, PyTorch only | 1.347 | 3.845 | valid |
| 345787 | sonnet-4 | 4 | Ultra Efficient: bitwise-AND parity, in-place shift (PyTorch cumsum x2) | 1.247 | 3.480 | valid |
| 345787 | sonnet-4 | 5 | Memory Optimized: reordered PyTorch ops, same pipeline | 1.530 | 4.617 | valid |
| 345787 | sonnet-4 | 6 | Block Optimized: Triton kernel for mask with tuned block size | 1.254 | 3.505 | valid |
| 345787 | sonnet-4 | 7 | Dtype Optimized: float32 intermediates for cumsum | null | 3.596 | invalid (results_match=False at idx 37284089, fp32 precision loss) |
| 345787 | sonnet-4 | 8 | Memory Patterns: chunked/streamed processing across boundaries | 2.030 | 7.613 | valid |
| 345787 | sonnet-4 | 9 | Simple Triton: one Triton kernel for parity-mask + multiply; cumsums in ATen | 1.129 | 3.093 | valid |
| 345787 | sonnet-4 | 10 | No Concat: replace torch.cat shift with in-place slice assignment | 1.172 | 3.228 | valid |
| 345787 | sonnet-4 | 11 | Re-submission of Simple Triton after revert | 1.131 | 3.098 | valid |
| 347447 | opus-4 | 1 | PyTorch cumsum chain (int64 output, dtype mismatch) | null | 4.242897033691406 | invalid (shape_dtype_match: False) |
| 347447 | opus-4 | 2 | PyTorch cumsum chain, output cast to int32 | 0.8656525476905746 | 2.376556396484375 | valid |
| 347447 | opus-4 | 4 | Triton single-pass strided kernel using `continue` | null | null | invalid (UnsupportedLanguageConstruct: Continue) |
| 347447 | opus-4 | 5 | Manually chunked torch.cumsum pipeline | 1.283876999552499 | 3.6106109619140625 | valid |
| 347447 | opus-4 | 7 | Triton single-pass kernel using tl.shift_left | null | null | invalid (AttributeError: tl.shift_left) |
| 347447 | opus-4 | 8 | Eager torch pipeline without shift_left | 0.8610270995243344 | 2.365589141845703 | valid |
| 347447 | opus-4 | 9 | Torch pipeline variant, alternative op order | 0.902002277231825 | 2.4645328521728516 | valid |
| 347447 | opus-4 | 10 | Ultra-simple eager torch pipeline | 0.8627389976313458 | 2.3696422576904297 | valid |
| 347447 | opus-4 | 11 | Custom Triton block-parallel kernel (no cross-block carry) | null | 3567.887783050537 | invalid (results_match: False, all-zeros output) |
| 347447 | opus-4 | 12 | Torch pipeline exploring warp-level/JIT primitives | 0.8986106367888708 | 2.456188201904297 | valid |
| 347447 | opus-4 | 14 | Final eager torch pipeline variant | 0.8768258482886998 | 2.40325927734375 | valid |
| 347447 | opus-4 | 15 | Parity-only boolean cumulative-XOR torch pipeline | 1.1887648983860408 | 3.2830238342285156 | valid |
| 347448 | opus-4 | 1 | PyTorch mask+cumsum, int64-leak from cumsum | null | 4556.7 | invalid (shape_dtype mismatch) |
| 347448 | opus-4 | 2 | PyTorch mask+cumsum, int64-leak from cumsum | null | 4848.7 | invalid (shape_dtype mismatch) |
| 347448 | opus-4 | 3 | PyTorch 5-pass (is_pos, cumsum, mask, filter, cumsum) with int32 cast | 1.6597 | 5257.6 | valid |
| 347448 | opus-4 | 4 | Single-thread Triton kernel with Python for loop | null | 976259.7 | invalid (wrong output at idx 4) |
| 347448 | opus-4 | 5 | PyTorch 5-pass with torch.where, int8 mask, pre-alloc | 1.2467 | 3478.8 | valid |
| 347448 | opus-4 | 6 | Single-thread chunked Triton on full 100M | 8.5775 | 5310957.4 | valid |
| 347448 | opus-4 | 7 | torch.compile(fullgraph=True), int8 masks, bitwise parity | 0.9036 | 2468.6 | valid |
| 347448 | opus-4 | 8 | torch.compile alternate mode on clean recipe | 0.5034 | 1654.4 | valid |
| 347448 | opus-4 | 9 | torch.compile with heavier op-fusion refactor | 1.0127 | 2753.0 | valid |
| 347448 | opus-4 | 10 | torch.jit.script of 5-pass recipe | 0.9091 | 2482.2 | valid |
| 347448 | opus-4 | 11 | torch.compile(max-autotune) replay #1 | 0.8488 | 2336.7 | valid |
| 347448 | opus-4 | 12 | torch.compile(reduce-overhead), aggressive dtype hints | 1.0411 | 2832.4 | valid |
| 347448 | opus-4 | 13 | torch.compile(max-autotune) replay #2 | 0.8475 | 2333.9 | valid |
| 347448 | opus-4 | 14 | Segment approach via torch.nonzero + pairing | 0.5410 | 1717.8 | valid |
| 347448 | opus-4 | 15 | CUDA graph capture around compiled forward | null | null | invalid (CUDA capture error) |
| 347448 | opus-4 | 16 | Simplified PyTorch + torch.compile(max-autotune) | 0.5384 | 1713.3 | valid |
| 347448 | opus-4 | 17 | torch.where in compiled region | 1.0052 | 2732.5 | valid |
| 347448 | opus-4 | 18 | torch.compile(max-autotune) replay #3 | 0.8485 | 2336.0 | valid |
| 347448 | opus-4 | 19 | torch.compile(max-autotune) replay #4 | 0.8505 | 2340.8 | valid |
| 347448 | opus-4 | 20 | torch.compile(max-autotune) replay #5 (declared final) | 0.8451 | 2328.2 | valid |
| 347448 | opus-4 | 21 | torch.compile(max-autotune) replay #6 (final confirmation) | 0.9157 | 2498.6 | valid |
| 347450 | Opus 4 | 1 | Sequential single-thread Triton kernel (grid=1), scalar pos_count+cumsum loop over all 100M elements | 9.2349 | 10248.18 | valid |
| 347450 | Opus 4 | 2 | Parallel blocks (BLOCK_SIZE=1024) + combine kernel, used Python `break` inside for-loop | null | null | invalid (CompileError: Triton 2.3.1 does not support `break`; output also all zeros) |
| 347450 | Opus 4 | 3 | Single-thread kernel, initialized scalar via `tl.zeros((1,), dtype=tl.int32)[0]` | null | null | invalid (CompileError: unsupported tensor index constexpr[0]) |
| 347450 | Opus 4 | 4 | Block-local scan + combine with per-block (pos_count,cumsum) handoff, BLOCK_SIZE=1024 | null | 27.81 | invalid (wrong output, first_different_index=8192 = 8 * BLOCK_SIZE, block-boundary bug) |
| 347450 | Opus 4 | 5 | Corrected serial single-thread Triton kernel (grid=1), verified results_match | 8.5812 | 5330.36 | valid |
| 347450 | Opus 4 | 6 | Branchless serial kernel: x[i] * (pos_count & 1) added unconditionally | 8.6033 | 5449.68 | valid |
| 347450 | Opus 4 | 7 | 16-element inner-loop unrolled serial Triton kernel | 7.9911 | 2954.44 | valid |
| 347450 | Opus 4 | 8 | 32-element inner-loop unrolled serial Triton kernel | 7.9439 | 2818.40 | valid |
| 347450 | Opus 4 | 9 | 64-element inner-loop unrolled serial Triton kernel (best Triton in this run) | 7.5284 | 1860.18 | valid |
| 347450 | Opus 4 | 10 | Dual-outcome parallel blocks: each block computes even-start and odd-start candidates, combine kernel selects per parity | 7.9430 | 2815.75 | valid |
| 347450 | Opus 4 | 11 | Cache-chunked memory-optimized kernel (256-elt chunks, 16-unroll inner) | 8.0068 | 3001.15 | valid |
| 347450 | Opus 4 | 12 | Hyper-optimized serial kernel (32-unroll) + parallel workers launch | 7.9551 | 2850.13 | valid |
| 347450 | Opus 4 | 13 | Re-test of 64-element unrolled serial kernel | 7.9549 | 2849.61 | valid |
| 347450 | Opus 4 | 14 | PyTorch reformulation: two torch.cumsum (count positives, mask & cumsum values), int32 output promoted to int64 | null | 4.68 | invalid (shape_dtype_match=False; results_match=True) |
| 347450 | Opus 4 | 15 | PyTorch two-cumsum reformulation with explicit dtype=torch.int32 in both cumsums | 1.3797 | 3.97 | valid |
| 347450 | Opus 4 | 16 | Same PyTorch two-cumsum reformulation wrapped with torch.compile | 1.0224 | 2.78 | valid |
| 347452 | opus-4 | 1 | O(n^2) naive Triton: one thread per output, O(i) sequential work | null | null | invalid (timeout) |
| 347452 | opus-4 | 2 | Two-pass PyTorch cumsum chain (output fp32, not int32) | null | 4.67 | invalid (shape_dtype_match=False) |
| 347452 | opus-4 | 3 | Two-pass PyTorch cumsum chain, dtype cast back to int32 | 1.6203 | 5.05 | valid |
| 347452 | opus-4 | 4 | PyTorch cumsum with multiplication (dtype drift back to fp32) | null | 4.77 | invalid (shape_dtype_match=False) |
| 347452 | opus-4 | 5 | Custom Triton kernel with mixed int32/fp32 tile state | null | null | invalid (Triton CompilationError: y int32 rebound to fp32) |
| 347452 | opus-4 | 6 | PyTorch mask-cast-to-dtype variant (dtype round-trip broken) | null | 4.46 | invalid (shape_dtype_match=False) |
| 347452 | opus-4 | 7 | Two-pass PyTorch cumsum, eager, dtype fixed | 1.3248 | 3.76 | valid |
| 347452 | opus-4 | 8 | torch.compile(mode='max-autotune', fullgraph=True) on two-cumsum chain | 0.5328 | 1.70 | valid |
| 347452 | opus-4 | 9 | int8 mask + masked_fill (defeats compile fusion) | 1.3868 | 4.00 | valid |
| 347452 | opus-4 | 10 | torch.jit.script variant with direct multiplication | 1.8245 | 6.20 | valid |
| 347452 | opus-4 | 11 | Chunked two-cumsum with boundary parity/sum carry | null | 3.64 | invalid (results_match=False at index 25000000) |
| 347452 | opus-4 | 12 | torch.compile dual strategies (max-autotune + reduce-overhead dispatch) | 1.0505 | 2.86 | valid |
| 347452 | opus-4 | 13 | Custom Triton with per-block O(blocks) prefix re-count | null | null | invalid (timeout, O(n^2)) |
| 347452 | opus-4 | 14 | torch.compile with mask materialized in x.dtype | 1.2708 | 3.56 | valid |
| 347452 | opus-4 | 15 | Single-pass Triton kernel with heterogeneous (fp32, int32) prefix carry | null | null | invalid (Triton CompilationError: prev_sum type conflict) |
| 347452 | opus-4 | 16 | CUDA graph wrapping of compiled two-cumsum pipeline | null | null | invalid (RuntimeError: generator outside graph capture) |
| 347452 | opus-4 | 17 | Multi-strategy compile variants (where / int8-mask / min-alloc) with size dispatch | 0.4850 | 1.62 | valid |
| 347452 | opus-4 | 18 | masked_fill_ 'ultra-fused' variant blocking inductor fusion | 1.5079 | 4.52 | valid |
| 347452 | opus-4 | 19 | torch.compile mode='reduce-overhead' for very-large arrays | 1.2485 | 3.49 | valid |
| 347453 | opus-4 | 1 | Naive O(n^2) Triton kernel with per-element inner loop (timeout) | null | null | invalid (timeout) |
| 347453 | opus-4 | 2 | Block-parallel Triton kernel using python 'continue' (compile error) | null | null | invalid (UnsupportedLanguageConstruct: Continue) |
| 347453 | opus-4 | 3 | Reworked O(n^2) kernel without continue/break (timeout) | null | null | invalid (timeout) |
| 347453 | opus-4 | 4 | Another O(n^2) variant (timeout) | null | null | invalid (timeout) |
| 347453 | opus-4 | 5 | PyTorch three-pass chain (x>0).cumsum -> %2 mask -> masked cumsum; no int32 cast | null | 4.438 | invalid (shape_dtype_match=False) |
| 347453 | opus-4 | 6 | PyTorch three-pass chain with int32 cast on output | 1.5153 | 4.551 | valid |
| 347453 | opus-4 | 7 | Near-identical PyTorch three-pass chain, minor mask-build rearrangement | 1.5182 | 4.564 | valid |
| 347453 | opus-4 | 8 | Fused Triton kernel using (pos_count & 1) as if-predicate | null | null | invalid (CompilationError: cannot bitcast i32 to i1) |
| 347453 | opus-4 | 9 | PyTorch chain using torch.where(include_mask, x, 0).cumsum | 1.4400 | 4.221 | valid |
| 347453 | opus-4 | 10 | "Single-pass" wrapper retaining PyTorch large-input path | 1.4470 | 4.251 | valid |
| 347453 | opus-4 | 11 | PyTorch chain + buggy 1024-element Triton fastpath (large path used for scoring) | 1.4237 | 4.153 | valid |
| 347453 | opus-4 | 12 | Minimal-memory PyTorch chain: (x>0).cumsum then (x*(pos_cumsum[:-1] & 1)).cumsum | 1.3145 | 3.723 | valid |
| 347453 | opus-4 | 13 | Same minimal-memory chain, rescored ('ultimate' variant) | 1.3144 | 3.722 | valid |
| 347453 | opus-4 | 14 | Another single-pass Triton-wrapped variant of the minimal chain | 1.3181 | 3.736 | valid |
| 347453 | opus-4 | 15 | torch.compile wrapper around the minimal-memory chain | 1.7449 | 5.725 | valid |
| 347453 | opus-4 | 16 | Restored minimal-memory chain (final) | 1.3186 | 3.738 | valid |
| 347454 | opus-4 | 1 | O(n^3) Python reference on small inputs (verification only, not scored) | n/a | n/a | dev-only |
| 347454 | opus-4 | 2 | Two-cumsum PyTorch decomposition, no dtype cast (int64 output) | 1.5664 | 4789.59 | valid |
| 347454 | opus-4 | 3 | Same decomposition, re-submitted without dtype fix | null | 4797.46 | invalid (shape_dtype_match=False) |
| 347454 | opus-4 | 4 | Same decomposition, second invalid re-submission | null | 4793.17 | invalid (shape_dtype_match=False) |
| 347454 | opus-4 | 5 | Two-cumsum decomposition with explicit int32 cast on final cumsum | 1.6196 | 5050.90 | valid |
| 347454 | opus-4 | 6 | Bitwise-AND parity (`& 1`) variant of the decomposition | 1.6223 | 5064.96 | valid |
| 347454 | opus-4 | 7 | Tightened decomposition: fewer intermediates, direct mask write | 1.2481 | 3483.77 | valid |
| 347454 | opus-4 | 8 | view()+in-place cumsum variant (regression) | 1.4231 | 4150.15 | valid |
| 347454 | opus-4 | 9 | Best formulation: pre-alloc bool mask + two cumsum + int32 cast | 1.1155 | 3051.04 | valid |
| 347454 | opus-4 | 10 | Concatenation/alternating-segment range variant | 1.1520 | 3164.53 | valid |
| 347454 | opus-4 | 11 | Re-run of best decomposition after H100 bandwidth discovery | 1.1180 | 3058.67 | valid |
| 347454 | opus-4 | 12 | Parallel chunk-based Triton attempt (effectively two-cumsum at runtime) | 1.1158 | 3052.00 | valid |
| 347454 | opus-4 | 13 | Two-cumsum pipeline with cuDNN benchmark and other PyTorch flags | 1.1164 | 3053.90 | valid |
| 347454 | opus-4 | 14 | Minor rearrangement of same two-cumsum pipeline | 1.1168 | 3055.10 | valid |
| 347454 | opus-4 | 15 | Segment-based algorithm using torch.nonzero on N=10^8 | null | n/a | invalid (timeout on full-size run) |
| 347454 | opus-4 | 16 | Revert to best formulation after timeout | 1.1345 | 3109.69 | valid |
| 347454 | opus-4 | 17 | Final Triton single-pass attempt (falls back to two-cumsum) | 1.1171 | 3056.05 | valid |
| 347454 | opus-4 | 18 | Final submission confirm run | 1.1168 | 3055.10 | valid |
| 347481 | sonnet-4 | 1 | PyTorch two-cumsum chain, no dtype= on cumsum (int32 silently promoted to int64) | null | 3907.0 | invalid (shape_dtype_match=False) |
| 347481 | sonnet-4 | 2 | PyTorch two-cumsum chain with explicit int32 dtype, torch.cat shift | 0.8365410771629799 | 2.308368682861328 | valid |
| 347481 | sonnet-4 | 3 | Same chain with zeros_like+slice-assign shift and bitwise-AND parity | 0.8091076742337490 | 2.2459030151367188 | valid |
| 347481 | sonnet-4 | 4 | Re-run of bitwise-AND / slice-assign variant | 0.8386046354685021 | 2.3131370544433594 | valid |
| 347481 | sonnet-4 | 5 | torch.roll + index-mask shift variant of baseline | 0.8762304329689361 | 2.4018287658691406 | valid |
| 347481 | sonnet-4 | 6 | Baseline torch.cat variant re-submission | 0.8054918030177032 | 2.2377967834472656 | valid |
| 347481 | sonnet-4 | 7 | Baseline torch.cat variant re-submission (bitwise-AND parity) | 0.8062373166578556 | 2.2394657135009766 | valid |
| 347481 | sonnet-4 | 8 | Baseline torch.cat variant re-submission (pure vectorized) | 0.8025041780895018 | 2.231121063232422 | valid |
| 347481 | sonnet-4 | 9 | F.pad shift with explicit boolean cast | 1.018397745909098 | 2.7687549591064453 | valid |
| 347481 | sonnet-4 | 10 | Advanced-indexing shift (gather at idx-1 with clamp) | 1.3392987122100377 | 3.816366195678711 | valid |
| 347481 | sonnet-4 | 11 | torch.where-based parity mask | 1.6203681024963832 | 5.054950714111328 | valid |
| 347481 | sonnet-4 | 12 | Toggle-interpretation reformulation (same underlying ops) | 0.8059178788656488 | 2.238750457763672 | valid |
| 347481 | sonnet-4 | 13 | torch.roll-based shift with mask (re-benchmark) | 1.0709818627296572 | 2.918243408203125 | valid |
| 347481 | sonnet-4 | 14 | Zone-based fallback (baseline dispatched at 100M) | 0.8087891521734035 | 2.245187759399414 | valid |
| 347481 | sonnet-4 | 15 | Scan-like reformulation (compiles to baseline) | 0.8378828743400925 | 2.3114681243896484 | valid |
| 347481 | sonnet-4 | 16 | Baseline re-submission (final torch.roll attempt) | 0.8776191843080957 | 2.4051666259765625 | valid |
| 347481 | sonnet-4 | 17 | Final submission: baseline torch.cat variant | 0.8014350023220889 | 2.2287368774414062 | valid |
| 347483 | sonnet-4 | 1 (v1) | PyTorch cumsum chain; BLOCK_SIZE=1024 fused for small arrays; int64 final cumsum | 1.1780 | 3247.98 | valid |
| 347483 | sonnet-4 | 2 (v2) | Removed int64 cast in final cumsum to cut bandwidth | null | 3136.87 | invalid (wrong output, first_different_index=67107488, int32 overflow) |
| 347483 | sonnet-4 | 3 (v3) | Full int64 pipeline to fix overflow | 1.5914 | 4910.47 | valid |
| 347483 | sonnet-4 | 4 (v4) | Selective int64 only for final cumsum | 1.2760 | 3582.24 | valid |
| 347483 | sonnet-4 | 5 (v5) | v4 pipeline, fused-kernel threshold raised to BLOCK_SIZE=4096 | 1.2765 | 3584.15 | valid |
| 347483 | sonnet-4 | 6 (v6) | Two-pass fused Triton, BLOCK_SIZE=8192, tl.cumsum per block (no cross-block carry) | null | 1909.49 | invalid (wrong output, first_different_index=2, local-only scan) |
| 347483 | sonnet-4 | 7 (v7) | v4 with BLOCK_SIZE=16384 + custom Triton mask-apply kernel | 1.1737 | 3233.91 | valid |
| 347483 | sonnet-4 | 8 (v8) | v7 with BLOCK_SIZE=32768 | 1.5305 | 4620.55 | valid |
| 347483 | sonnet-4 | 9 (v9) | CUDA stream context + bitwise & 1 parity + in-place shift | 1.3050 | 3687.62 | valid |
| 347483 | sonnet-4 | 10 (v10) | Python-loop multi-chunk with result[start-1].item() offset | null | 256094.93 | invalid (wrong at chunk boundary idx=8192; 256 ms) |
| 347483 | sonnet-4 | 11 (v11) | @torch.jit.script + slice-assignment shift over v7 | 1.1497 | 3157.14 | valid |
| 347483 | sonnet-4 | 12 (v12) | v11 with BLOCK_SIZE=65536 (best valid in run) | 1.1452 | 3143.07 | valid |
| 347483 | sonnet-4 | 13 (v13) | Multi-phase Triton scan with `mask[-1]` negative index | null | null | invalid (CompilationError: constexpr[-1]) |
| 347483 | sonnet-4 | 14 (v14) | Retry with `scanned[last_valid_idx]` runtime index | null | null | invalid (CompilationError: runtime index into block tensor) |
| 347483 | sonnet-4 | 15 (v15) | BLOCK_SIZE=131072 ultra-fused kernel | null | null | invalid (timeout during kernel compilation) |
| 347483 | sonnet-4 | 16 (v16) | Python-loop hybrid chunked 65536 | null | null | invalid (timeout, 1024-warmup already 10.3 s) |
| 347483 | sonnet-4 | 17 (v17) | float32 intermediate for final cumsum | null | 3857.61 | invalid (wrong output at idx=67134331, float32 precision > 2^24) |
| 347483 | sonnet-4 | 18 (v18) | Revert float32, keep other v17 cleanup | 1.3635 | 3909.83 | valid |
| 347483 | sonnet-4 | 19 (v19) | Two-pass Triton with `local_cumsum[end_pos-1]` | null | null | invalid (CompilationError, same indexing restriction) |
| 347483 | sonnet-4 | 20 (v20) | Hybrid Triton pos-count + Python offset loop + torch final cumsum | 3.5751 | 35696.51 | valid |
| 347483 | sonnet-4 | 21 (final) | v12 with fused before-count computation | 1.4275 | 4168.27 | valid |
| 347486 | sonnet-4 | 1 | PyTorch cumsum+cat+cumsum, int64 output (missing dtype=int32) | null | 4847.3 | invalid (shape_dtype_match=False) |
| 347486 | sonnet-4 | 2 | PyTorch cumsum+cat+cumsum with dtype=int32 (baseline) | 0.9843 | 2676.0 | valid |
| 347486 | sonnet-4 | 3 | PyTorch 'optimized v1' combined expressions (regression) | 1.0331 | 2809.8 | valid |
| 347486 | sonnet-4 | 4 | PyTorch v4 minimal_ops: index-assignment inclusion (no torch.cat) | 0.8583 | 2359.2 | valid |
| 347486 | sonnet-4 | 5 | torch.jit.script wrapper over cumsum+cat+cumsum | 0.8182 | 2266.4 | valid |
| 347486 | sonnet-4 | 6 | PyTorch 'ultra optimized' cumsum+cat+cumsum (best valid) | 0.8110 | 2250.2 | valid |
| 347486 | sonnet-4 | 7 | PyTorch segment-based inclusion, no torch.cat (regression) | 0.8573 | 2356.8 | valid |
| 347486 | sonnet-4 | 8 | PyTorch minimal_memory with torch.empty_like (regression) | 0.8172 | 2264.3 | valid |
| 347486 | sonnet-4 | 9 | PyTorch bitwise '& 1' in place of '% 2' | 0.8149 | 2259.0 | valid |
| 347486 | sonnet-4 | 10 | torch.jit.script Python for-loop with .item() over 100M GPU elements | null | null | invalid (timeout) |
| 347486 | sonnet-4 | 11 | PyTorch no_cat_v2 index-assignment, second attempt (regression) | 0.8626 | 2369.4 | valid |
| 347486 | sonnet-4 | 12 | Final revert to 'ultra optimized' cumsum+cat+cumsum pipeline | 0.8166 | 2262.8 | valid |
