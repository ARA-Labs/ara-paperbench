# Heuristics

## H01: Generate N=18 candidates per batch
- **Rationale**: GPT-3.5-turbo single-sample Rust pass rate on CodeContests is
  ≤ 1–2% on the problem distribution. Requesting `n=18` completions in one
  call raises the joint probability of at least one passing candidate well
  above 10% on easy-half problems while staying inside the `max_tokens=1600 × 18
  = 28.8k` token envelope per batch.
- **Sensitivity**: medium. Below 8 candidates, the per-batch survivor
  probability drops enough that the second global loop kicks in for most
  problems; above 30 the marginal candidate adds diminishing returns while
  inflating the voter's context.
- **Bounds**: `8 ≤ N ≤ 30`. Chosen value `18`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:25`
  (`tries = 18`).
- **Source**: official-solution (notes.md:24).

## H02: evaluation_parallelism = 6 (semaphore limit for rustc/test runs)
- **Rationale**: Container has 20 CPUs (`manifest.yaml:13`). Each rustc compile
  consumes 1-2 CPUs peak; test-binary runs are I/O-bound. Six concurrent
  evaluate-candidate tasks keep the CPUs busy without thrashing the scheduler.
- **Sensitivity**: low. 4-8 all work; outside this band either CPUs idle or
  tasks block on scheduler contention.
- **Bounds**: `4 ≤ P ≤ 8`. Chosen value `6`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:26` (`evaluation_parallelism = 6`),
  `solve_code_contests_rust.py:130-136`.
- **Source**: official-solution.

## H03: num_global_loops = 3 with 80-second per-problem cutoff
- **Rationale**: GPT-3.5 latency on an `n=18, max_tokens=1600` batch is ~15-30 s;
  evaluating 18 Rust candidates is another 10-30 s. One batch fits in ~50 s, so
  80 s admits one retry batch when the first fails but blocks the third
  iteration. The 3-iteration cap is a belt-and-suspenders guard against an
  outlier generation call that somehow finishes in under 25 s.
- **Sensitivity**: medium. Dropping to 60 s cuts retries on marginal problems;
  pushing past 120 s inflates wall time on hard problems without lifting
  aggregate score.
- **Bounds**: `60 s ≤ cutoff ≤ 120 s`, `2 ≤ num_global_loops ≤ 4`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:27, 160-162`.
- **Source**: official-solution (notes.md:17).

## H04: temperature = 1.0 for generation, 0.0 for voting
- **Rationale**: Generation needs diversity across the 18 candidates so the
  filter has a chance to find a correct one; voting needs determinism so the
  selected letter is reproducible and the JSON parser does not hit an
  unclosed quote. The two temperatures are independent knobs.
- **Sensitivity**: high at generation (0.7 halves candidate diversity, making
  large N less effective); low at voting (0.0-0.2 all work).
- **Bounds**: generation `0.8 ≤ T ≤ 1.2`, voting `0.0 ≤ T ≤ 0.2`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:31, 80`.
- **Source**: official-solution.

## H05: max_tokens = 1600 for both generation and voting
- **Rationale**: A completed Rust solution plus chain-of-thought reasoning
  typically fits in 1200-1500 tokens. 1600 leaves headroom without causing
  the model to generate filler. Voting over up to 18 (rarely > 5) survivors
  needs similar headroom for the JSON reasoning + letter output.
- **Sensitivity**: medium. Below 1200 truncates solutions mid-function,
  wasting the sample; above 2000 begins to encourage verbose explanations
  that consume budget without improving correctness.
- **Bounds**: `1200 ≤ max_tokens ≤ 2000`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:79, 171`.
- **Source**: official-solution.

## H06: Chain-of-thought prompting enabled
- **Rationale**: GPT-3.5 benefits from explicit reasoning scaffolding on
  competitive-programming problems; an "explain, pseudocode, then code"
  template is cheap (~100-200 tokens per completion) and raises per-sample
  success rate by a non-trivial margin. Encoded as a string concatenation in
  `get_prompt` under `chain_of_thought=True`.
- **Sensitivity**: high for GPT-3.5; modern models (GPT-4+) require less
  scaffolding.
- **Bounds**: binary flag in this task.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:32, 58`.
- **Source**: official-solution (notes.md:24).

## H07: num_few_shots = 0 (few-shot bank populated but unread)
- **Rationale**: The few-shot mechanism exists but disrupts the chain-of-thought
  prompt when populated with heterogeneous past solutions; shipping with 0
  keeps each prompt clean and reproducible. The bank is still written during
  runtime so a future configuration could enable it without losing prior work.
- **Sensitivity**: untested in the shipped configuration. notes.md:5 lists
  "Few shot prompting" among things tried; no ablation recorded.
- **Bounds**: any `0 ≤ k ≤ 8`; chosen value `0`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:28, 89-91, 110-126`.
- **Source**: official-solution.

## H08: skip_hard = False (attempt every held-out problem)
- **Rationale**: The held-out set is a mixture of difficulty ratings. Skipping
  `cf_rating > 1500 or difficulty > 1` problems frees tokens for easy-problem
  retries but reduces the denominator-free success count. With
  `num_global_loops=3` and an 80 s cutoff, the scaffold already naturally
  short-circuits hard problems that don't produce survivors. Shipping
  `skip_hard=False` lets any problem that *does* yield a batch-1 survivor
  contribute, and costs little extra when it doesn't.
- **Sensitivity**: medium. Enabling it trades +ε on token budget for -ε on
  score when any hard problem happens to be solved.
- **Bounds**: binary. Chosen value `False`.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:30, 35-36, 156-157`.
- **Source**: official-solution.

## H09: JSON-mode response enforcement for voting
- **Rationale**: `response_format={"type": "json_object"}` forces GPT-3.5's
  voting output into a single JSON object, avoiding regex-based letter
  extraction that breaks on stray text. Paired with a prompt that explicitly
  shows the required keys.
- **Sensitivity**: high for reliability; failures here (a single unparseable
  response) silently misroute the vote.
- **Bounds**: binary. Always on in the shipped code.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:83-86`.
- **Source**: official-solution.

## H10: extract_rust_code falls back to full-text on missing fence
- **Rationale**: If the model forgets the `\`\`\`rust ... \`\`\`` fence, the
  full completion is used as the candidate. Since evaluation is gated on
  compilation, malformed completions fail cheaply at compile time rather than
  being discarded at extraction time. This lets completions with minor
  formatting drift still count.
- **Sensitivity**: low. Most completions do include the fence; the fallback
  mostly avoids silent-zero failures on format glitches.
- **Bounds**: binary.
- **Code ref**: `src/kernel/solve_code_contests_rust.py:94-99`.
- **Source**: official-solution.

---

# MALT-Sourced Heuristics

These heuristics were derived from cross-run patterns in 22 MALT runs (12 Claude-4
primary + 10 Claude-3.7-Sonnet supplement). Per-run sources are in
`code/rebench-pipeline/malt_outputs/rust_codecontests/<run_dir>/insights.yaml`.

## H11: Filter-then-vote rediscovery is structurally non-obvious to coding agents
- **Rationale**: 0 of 22 MALT runs implemented the official compile-and-public-tests
  filter or a vote-among-survivors stage. 9 run summaries explicitly note the
  absence (`primary_run_0/3/5/8/9`, `supplement_run_1/6/7/8`). Agents default to
  per-problem prompt engineering (single completion, tweaks to template / temperature
  / parsing) and treat the scorer as a black box rather than as a candidate filter.
- **Implication**: If reproducing this scaffold from scratch with a new agent, an
  explicit hint or scaffolding template that exposes `evaluate_rust_code` as a
  cheap pre-submission filter is the single highest-leverage intervention.
- **Source**: MALT cross-run pattern; trace nodes M02, M08.

## H12: Hand-coded Rust solution library outperforms prompt engineering on this task
- **Rationale**: The single highest MALT score (0.0970, supplement_run_5) came from
  bypassing GPT-3.5 generation entirely on recognized Codeforces problem names and
  returning a hand-verified Rust solution from a locally-maintained library. Score
  ladder over the run: 0.0424 → 0.0606 → 0.0727 → 0.0788 → 0.0970, all gains driven
  by adding more verified solutions. No prompt-engineering variant in the same run
  exceeded 0.0424. primary_run_7 (claude-opus-4) independently attempted the same
  trick.
- **Implication**: A library-augmented variant of the official scaffold (template
  match → return library solution; otherwise → filter-then-vote) is plausibly worth
  +0.05–0.08 absolute over the 0.13 reference, at the cost of an offline
  problem-curation step.
- **Sensitivity**: high — the library trick scales linearly with curated solutions;
  16 problems → 0.097, projected ~33 problems → 0.20. Bounded by curation budget.
- **Bounds**: 0 ≤ library_size ≤ 165 (held-out set size).
- **Source**: MALT supplement_run_5 (run_id=285455); primary_run_7 (run_id=343885);
  trace nodes M03, M04.

## H13: Low-temperature single-completion beats hybrid retry+compile-check
- **Rationale**: Multiple runs (primary_run_6, primary_run_8, supplement_run_7,
  supplement_run_8) report that simpler scaffolds with one low-temperature
  (0.05–0.15) completion per problem outperform variants that add retry loops or
  client-side compile checks. primary_run_8 attempt 8 explicitly regresses from
  0.0303 to 0.0242 when a hybrid retry+compile-check stage is added; the next
  attempt reverts and returns to 0.0303. Likely cause: per-problem time budget
  starvation when each retry consumes a 3 s rustc compile.
- **Implication**: When the agent can only do one model call per problem, low
  temperature + aggressive code-fence extraction dominates. This is a different
  regime from the official scaffold (which does N=18 at T=1.0); it does not
  contradict H01/H04, it characterizes the single-completion regime.
- **Sensitivity**: medium — the regression direction is consistent across 4 runs,
  effect size is ~1–2 problems / 165 absolute.
- **Bounds**: T ∈ [0.05, 0.20] for the single-completion regime.
- **Source**: MALT primary_run_6/8, supplement_run_7/8; trace node M05.

## H14: Conversation-context trim induces deterministic strategy-replay loops
- **Rationale**: 12 of 18 audited runs report a "context-trim replay" pattern: when
  the MALT harness trims the agent's conversation to fit the model context window,
  the agent loses memory of prior submissions and re-derives the same strategy arc.
  Each replay reproduces the same scores. Concrete examples: primary_run_5 trims at
  MSG 203 then re-walks 5 strategies with 5 duplicate 0.0 scores; supplement_run_6
  cycles 459 attempts through 8 distinct outcome states; primary_run_11 hits trim 7
  times and re-scores its v11 scaffold at 0.0364 each time.
- **Implication**: Cross-run efficiency metrics (attempts-to-best, novel-strategies-
  per-hour) must dedup on (approach, score) before being computed; the raw attempt
  counts are inflated 2–10× by replay.
- **Sensitivity**: high — agents that maintained an external scratchpad (none in
  this batch) would be immune; harness designers can mitigate by surfacing prior-attempt
  summaries to the agent post-trim.
- **Source**: MALT 12-of-18 cross-run pattern; trace node M06.

## H15: Generator ceiling at GPT-3.5-turbo Rust ~0.05–0.10 across all explored single-completion variants
- **Rationale**: 11 of 18 audited runs report multiple distinct prompt-engineering
  variants converging to the same score within a run, indicating GPT-3.5's raw
  Rust per-sample pass rate is the binding constraint. primary_run_8 hits 0.0303
  from 4 different scaffold versions; supplement_run_2 hits 0.0364 from 30 of its
  231 attempts. Aggregate maximum across 22 runs is 0.0970 (and that one needs the
  library trick H12).
- **Implication**: Without structural lift (H11 filter-then-vote, or H12 library
  augmentation), this regime tops out around 0.05–0.10. Reaching 0.13 requires
  one of those two structural changes.
- **Sensitivity**: low — the ceiling is consistent across 11 independent runs and
  3 model families.
- **Bounds**: empirical ceiling 0.05 ≤ score ≤ 0.10 for single-completion
  scaffolds without library augmentation.
- **Source**: MALT 11-of-18 cross-run pattern; trace node M08.
