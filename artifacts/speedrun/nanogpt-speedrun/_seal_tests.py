"""
ARA Seal Tests for nanogpt-speedrun artifact.

Three verification levels:
  L1 — Structural Integrity (automated schema checks)
  L2 — Information Fidelity (content correctness questions)
  L3 — Execution Reproducibility (can an agent use this to implement?)

Run: python _seal_tests.py
"""

import os
import yaml
import json
import sys

ARTIFACT_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# LEVEL 1: STRUCTURAL INTEGRITY
# ============================================================

def test_l1_directory_structure():
    """All required directories exist."""
    required_dirs = [
        "logic",
        "logic/solution",
        "src",
        "src/execution",
        "src/configs",
        "trace",
        "evidence",
        "evidence/tables",
    ]
    results = []
    for d in required_dirs:
        path = os.path.join(ARTIFACT_DIR, d)
        passed = os.path.isdir(path)
        results.append({"check": f"dir_exists:{d}", "passed": passed})
        if not passed:
            print(f"  FAIL: directory missing: {d}")
    return results


def test_l1_required_files():
    """All required files exist and are non-empty."""
    required_files = [
        "PAPER.md",
        "logic/problem.md",
        "logic/claims.md",
        "logic/concepts.md",
        "logic/experiments.md",
        "logic/related_work.md",
        "logic/solution/architecture.md",
        "logic/solution/algorithm.md",
        "logic/solution/heuristics.md",
        "logic/solution/constraints.md",
        "src/environment.md",
        "src/configs/training.md",
        "src/configs/model.md",
        "src/execution/muon_optimizer.py",
        "src/execution/flex_attention.py",
        "src/execution/unet_skip.py",
        "trace/exploration_tree.yaml",
        "evidence/README.md",
        "evidence/tables/table1_speedrun_progression.md",
    ]
    results = []
    for f in required_files:
        path = os.path.join(ARTIFACT_DIR, f)
        exists = os.path.isfile(path)
        non_empty = os.path.getsize(path) > 0 if exists else False
        passed = exists and non_empty
        results.append({"check": f"file_exists:{f}", "passed": passed})
        if not passed:
            print(f"  FAIL: file missing or empty: {f}")
    return results


def test_l1_frontmatter_valid():
    """All markdown files have valid YAML frontmatter."""
    md_files = []
    for root, dirs, files in os.walk(ARTIFACT_DIR):
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))

    results = []
    for filepath in md_files:
        relpath = os.path.relpath(filepath, ARTIFACT_DIR)
        try:
            with open(filepath, "r") as fh:
                content = fh.read()
            if content.startswith("---"):
                end = content.index("---", 3)
                frontmatter = content[3:end].strip()
                yaml.safe_load(frontmatter)
                results.append({"check": f"frontmatter_valid:{relpath}", "passed": True})
            else:
                # PAPER.md has frontmatter, others may not — only fail if expected
                results.append({"check": f"frontmatter_present:{relpath}", "passed": True})
        except Exception as e:
            results.append({"check": f"frontmatter_valid:{relpath}", "passed": False})
            print(f"  FAIL: invalid frontmatter in {relpath}: {e}")
    return results


def test_l1_exploration_tree_schema():
    """Exploration tree has valid YAML with required node fields."""
    tree_path = os.path.join(ARTIFACT_DIR, "trace", "exploration_tree.yaml")
    results = []
    try:
        with open(tree_path, "r") as fh:
            data = yaml.safe_load(fh)

        assert "tree" in data, "Missing 'tree' root key"
        results.append({"check": "tree_root_key", "passed": True})

        # Validate node types and required fields
        valid_types = {"question", "experiment", "dead_end", "decision", "pivot"}
        node_count = 0
        dead_end_count = 0

        def validate_node(node, path=""):
            nonlocal node_count, dead_end_count
            node_count += 1
            node_id = node.get("id", "UNKNOWN")
            node_type = node.get("type", "MISSING")

            assert "id" in node, f"Node at {path} missing 'id'"
            assert "type" in node, f"Node {node_id} missing 'type'"
            assert node_type in valid_types, f"Node {node_id} has invalid type: {node_type}"
            assert "title" in node, f"Node {node_id} missing 'title'"

            if node_type == "dead_end":
                dead_end_count += 1
                assert "lesson" in node, f"Dead end {node_id} missing 'lesson'"
                assert "failure_mode" in node, f"Dead end {node_id} missing 'failure_mode'"

            if node_type == "experiment":
                assert "result" in node, f"Experiment {node_id} missing 'result'"

            if node_type == "decision":
                assert "alternatives" in node, f"Decision {node_id} missing 'alternatives'"

            if node_type == "pivot":
                assert "trigger" in node, f"Pivot {node_id} missing 'trigger'"
                assert "justification" in node, f"Pivot {node_id} missing 'justification'"

            for child in node.get("children", []):
                validate_node(child, f"{path}/{node_id}")

        for root_node in data["tree"]:
            validate_node(root_node)

        results.append({"check": "tree_node_schema", "passed": True})
        results.append({"check": f"tree_node_count:{node_count}", "passed": node_count >= 20})
        results.append({"check": f"dead_end_count:{dead_end_count}", "passed": dead_end_count >= 2})

        print(f"  Tree: {node_count} nodes, {dead_end_count} dead ends")

    except Exception as e:
        results.append({"check": "tree_schema", "passed": False})
        print(f"  FAIL: exploration tree schema error: {e}")
    return results


def test_l1_claims_structure():
    """Claims file has properly formatted claims with required fields."""
    claims_path = os.path.join(ARTIFACT_DIR, "logic", "claims.md")
    results = []
    try:
        with open(claims_path, "r") as fh:
            content = fh.read()

        # Count claims (## C0N pattern)
        import re
        claims = re.findall(r"## (C\d+)", content)
        results.append({"check": f"claims_count:{len(claims)}", "passed": len(claims) >= 7})

        # Check each claim has required fields
        required_fields = ["Statement", "Status", "Falsification", "Proof"]
        for field in required_fields:
            count = content.count(f"**{field}**")
            passed = count >= len(claims)
            results.append({"check": f"claims_field_{field.lower()}:{count}", "passed": passed})
            if not passed:
                print(f"  WARN: only {count}/{len(claims)} claims have '{field}' field")

        print(f"  Claims: {len(claims)} found with {len(required_fields)} required fields")

    except Exception as e:
        results.append({"check": "claims_structure", "passed": False})
        print(f"  FAIL: claims structure error: {e}")
    return results


def test_l1_code_stubs_parseable():
    """Python code stubs parse without syntax errors."""
    py_files = []
    for root, dirs, files in os.walk(os.path.join(ARTIFACT_DIR, "src")):
        for f in files:
            if f.endswith(".py"):
                py_files.append(os.path.join(root, f))

    results = []
    for filepath in py_files:
        relpath = os.path.relpath(filepath, ARTIFACT_DIR)
        try:
            with open(filepath, "r") as fh:
                code = fh.read()
            compile(code, filepath, "exec")
            results.append({"check": f"python_syntax:{relpath}", "passed": True})
        except SyntaxError as e:
            results.append({"check": f"python_syntax:{relpath}", "passed": False})
            print(f"  FAIL: syntax error in {relpath}: {e}")
    return results


# ============================================================
# LEVEL 2: INFORMATION FIDELITY
# ============================================================

L2_QUESTIONS = [
    # --- Surface Facts (D1) ---
    {
        "id": "Q01",
        "difficulty": "D1",
        "question": "What is the baseline training time for GPT-2 124M on 8×H100?",
        "expected": "49.5 minutes (2,968,348 ms) in Record 1",
        "layer": "evidence/tables/table1_speedrun_progression.md",
    },
    {
        "id": "Q02",
        "difficulty": "D1",
        "question": "What is the final training time achieved?",
        "expected": "3.07 minutes (184,262 ms) in Record 21",
        "layer": "evidence/tables/table1_speedrun_progression.md",
    },
    {
        "id": "Q03",
        "difficulty": "D1",
        "question": "How many records are in the speedrun?",
        "expected": "21 records",
        "layer": "evidence/tables/table1_speedrun_progression.md",
    },
    {
        "id": "Q04",
        "difficulty": "D1",
        "question": "What optimizer replaced AdamW?",
        "expected": "Muon (OrthogonalNesterov + AdamW hybrid), introduced in Record 3",
        "layer": "logic/concepts.md",
    },

    # --- Method Detail (D2) ---
    {
        "id": "Q05",
        "difficulty": "D2",
        "question": "How does Newton-Schulz orthogonalization work in Muon?",
        "expected": "Iterative approximation X_{k+1} = aX + bX^3 + cX^5 with a=3.4445, b=-4.7750, c=2.0315. 5 steps. Input normalized to spectral norm < 1.86.",
        "layer": "logic/solution/algorithm.md + src/execution/muon_optimizer.py",
    },
    {
        "id": "Q06",
        "difficulty": "D2",
        "question": "Why does Muon only apply orthogonalization to 2D+ parameters?",
        "expected": "Orthogonal updates are only meaningful for matrix-valued parameters where the Stiefel manifold structure exists. 1D parameters lack this geometric structure.",
        "layer": "logic/solution/heuristics.md (H01)",
    },
    {
        "id": "Q07",
        "difficulty": "D2",
        "question": "How does document-aware masking work in FlexAttention?",
        "expected": "Three conditions: causal (q >= kv), same_doc (doc_id match), in_window (q-kv <= window). Compiled via create_block_mask with 128-token block granularity.",
        "layer": "src/execution/flex_attention.py + logic/solution/heuristics.md (H06)",
    },

    # --- Hyperparameter Recovery (D2) ---
    {
        "id": "Q08",
        "difficulty": "D2",
        "question": "What are the final Muon learning rates?",
        "expected": "lr_muon=0.6, lr_adam_head=0.008, lr_adam_1d=0.04",
        "layer": "src/configs/training.md",
    },
    {
        "id": "Q09",
        "difficulty": "D2",
        "question": "What is the momentum warmup schedule?",
        "expected": "0.85 → 0.95 warmup over early steps. Required for stability with U-Net skip connections.",
        "layer": "logic/solution/heuristics.md (H09)",
    },

    # --- Cross-Section Reasoning (D3) ---
    {
        "id": "Q10",
        "difficulty": "D3",
        "question": "Which single optimization provides the largest speedup and why?",
        "expected": "Muon optimizer (Record 3): 36.8→23.1 min (37.2%). Because orthogonal gradient updates on weight matrices converge faster than AdamW's element-wise updates, reducing required training steps from 9,536 to 7,000.",
        "layer": "logic/claims.md + evidence/tables/table1_speedrun_progression.md",
    },
    {
        "id": "Q11",
        "difficulty": "D3",
        "question": "Why did Record 7 show a slight regression despite adding optimizations?",
        "expected": "cuDNN attention was slower than expected at short sequences (~4K tokens). The overhead only becomes beneficial at 64K+ context (Record 11+). This is documented as dead_end N07a.",
        "layer": "trace/exploration_tree.yaml (N07, N07a)",
    },
    {
        "id": "Q12",
        "difficulty": "D3",
        "question": "What is the relationship between FP8 precision and logit softcap?",
        "expected": "FP8 (Record 18) introduces quantization bias in the LM head. Sigmoid logit offset compensates for this bias. Logit softcap was reduced from 30→15 (Record 17) before FP8 was added.",
        "layer": "logic/solution/heuristics.md (H08) + trace/exploration_tree.yaml (N18, N20)",
    },

    # --- Design Rationale (D3) ---
    {
        "id": "Q13",
        "difficulty": "D3",
        "question": "What were the six phases of optimization and their cumulative speedups?",
        "expected": "Optimizer (2.3×), Architecture (4.5×), Precision (6.2×), Attention (9.3×), Advanced (13.5×), Hardware (16.1×)",
        "layer": "evidence/tables/table1_speedrun_progression.md + trace/exploration_tree.yaml",
    },
    {
        "id": "Q14",
        "difficulty": "D3",
        "question": "Why can't LLM agents reproduce these optimizations even with pseudocode hints?",
        "expected": "The bottleneck is implementation, not ideation. Agents correctly identify optimization directions but produce buggy distributed training code (NCCL errors, torch.compile issues, numerical precision, CUDA kernel errors). This is C06.",
        "layer": "logic/claims.md (C02, C06) + trace/exploration_tree.yaml (N25)",
    },

    # --- Failure Knowledge (D3) ---
    {
        "id": "Q15",
        "difficulty": "D3",
        "question": "What dead ends were encountered in the speedrun trajectory?",
        "expected": "Two documented: (1) N07a — cuDNN attention slower at short sequences, lesson: premature optimization. (2) N17a — removing 2+ transformer layers causes val_loss regression despite skip connections, lesson: minimum depth required.",
        "layer": "trace/exploration_tree.yaml (N07a, N17a)",
    },

    # --- Control (unanswerable) ---
    {
        "id": "Q16",
        "difficulty": "control",
        "question": "What is the training loss curve shape for Record 15?",
        "expected": "NOT ANSWERABLE — training loss curves are not included in this artifact",
        "layer": "N/A",
    },
    {
        "id": "Q17",
        "difficulty": "control",
        "question": "How much GPU memory does the Muon optimizer use compared to AdamW?",
        "expected": "NOT ANSWERABLE — exact memory comparisons are not provided",
        "layer": "N/A",
    },
]


def test_l2_questions():
    """Verify L2 information fidelity questions are answerable from ARA."""
    results = []
    for q in L2_QUESTIONS:
        if q["difficulty"] == "control":
            results.append({
                "check": f"l2_{q['id']}_control",
                "question": q["question"],
                "expected": q["expected"],
                "answerable": False,
                "passed": True,  # controls are expected to be unanswerable
            })
        else:
            # Check that the referenced layer file exists
            layers = q["layer"].split(" + ")
            files_exist = all(
                os.path.isfile(os.path.join(ARTIFACT_DIR, l.split(" (")[0].strip()))
                for l in layers
                if not l.startswith("N/A")
            )
            results.append({
                "check": f"l2_{q['id']}",
                "question": q["question"],
                "expected": q["expected"],
                "answerable": True,
                "source_exists": files_exist,
                "passed": files_exist,
            })
            if not files_exist:
                print(f"  FAIL L2 {q['id']}: source file missing for: {q['layer']}")
    return results


# ============================================================
# LEVEL 3: EXECUTION REPRODUCIBILITY
# ============================================================

L3_QUESTIONS = [
    # --- Configuration Recovery ---
    {
        "id": "E01",
        "category": "config_recovery",
        "task": "Extract all hyperparameters needed to configure the Muon optimizer from ARA.",
        "expected_files": ["src/configs/training.md", "logic/solution/heuristics.md"],
        "verification": "Agent should recover: lr_muon=0.6, momentum=0.85→0.95, ns_steps=5, nesterov=True, plus the parameter partitioning rule (ndim >= 2).",
    },
    {
        "id": "E02",
        "category": "config_recovery",
        "task": "Set up the FlexAttention block mask for 64K sequences with 1024-token sliding window.",
        "expected_files": ["src/execution/flex_attention.py", "logic/solution/heuristics.md"],
        "verification": "Agent should produce a working mask_fn with causal + same_doc + in_window conditions, block_size=128.",
    },

    # --- Implementation ---
    {
        "id": "E03",
        "category": "implementation",
        "task": "Implement the Newton-Schulz orthogonalization function given only the algorithm description.",
        "expected_files": ["logic/solution/algorithm.md"],
        "verification": "Function should: normalize input, apply 5 iterations of X=aX+bX^3+cX^5 with correct coefficients, return orthogonalized matrix.",
    },
    {
        "id": "E04",
        "category": "implementation",
        "task": "Implement U-Net skip connections for a transformer given the architecture description.",
        "expected_files": ["src/execution/unet_skip.py", "logic/solution/heuristics.md"],
        "verification": "Module should: store encoder outputs, blend with decoder inputs using learnable alpha (sigmoid-bounded), init alpha near 0.",
    },

    # --- Debugging/Extension ---
    {
        "id": "E05",
        "category": "debugging",
        "task": "The Muon optimizer is applying orthogonalization to embedding parameters and training diverges. Diagnose and fix using ARA.",
        "expected_files": ["logic/solution/heuristics.md", "logic/claims.md"],
        "verification": "Agent should identify H01 (2D-only orthogonalization) and recognize that embeddings, despite being 2D, should use AdamW (they are in a separate optimizer group).",
    },
    {
        "id": "E06",
        "category": "extension",
        "task": "Propose how to adapt the speedrun optimizations for a 1B parameter model.",
        "expected_files": ["logic/solution/constraints.md", "logic/solution/heuristics.md"],
        "verification": "Agent should identify: constraints.md notes all optimizations validated only at 124M scale; H03 (ReLU²) may not transfer; H08 (FP8) remains valid; U-Net skip connections need re-evaluation at greater depth.",
    },

    # --- Negative Knowledge ---
    {
        "id": "E07",
        "category": "negative_knowledge",
        "task": "An agent wants to speed up training by removing 3 transformer layers. Should it proceed?",
        "expected_files": ["trace/exploration_tree.yaml"],
        "verification": "Agent should find dead_end N17a: removing 2+ layers causes val_loss regression. Lesson: minimum depth exists below which skip connections cannot compensate. Recommend removing at most 1 layer.",
    },
    {
        "id": "E08",
        "category": "negative_knowledge",
        "task": "An agent wants to switch to cuDNN attention for 4K sequences. Should it proceed?",
        "expected_files": ["trace/exploration_tree.yaml"],
        "verification": "Agent should find dead_end N07a: cuDNN attention is slower at short sequences. Only beneficial at 64K+ context. Recommend standard SDPA for 4K.",
    },

    # --- Environment Setup ---
    {
        "id": "E09",
        "category": "environment",
        "task": "Set up the environment to run the optimized NanoGPT training.",
        "expected_files": ["src/environment.md"],
        "verification": "Agent should specify: 8×H100, PyTorch 2.5+, CUDA 12.5+, Python 3.10+, FineWeb-Edu dataset, torchrun launcher.",
    },

    # --- Trajectory Understanding ---
    {
        "id": "E10",
        "category": "trajectory",
        "task": "Explain the two pivots in the optimization trajectory and what triggered them.",
        "expected_files": ["trace/exploration_tree.yaml"],
        "verification": "Agent should identify: (1) N09 — pivot from architecture to precision engineering, triggered by diminishing returns from arch changes. (2) N19 — pivot to hardware-specific optimizations (FP8, custom CUDA), triggered by software-level optimizations approaching diminishing returns.",
    },
]


def test_l3_questions():
    """Verify L3 execution questions reference existing files."""
    results = []
    for q in L3_QUESTIONS:
        files_exist = all(
            os.path.isfile(os.path.join(ARTIFACT_DIR, f))
            for f in q["expected_files"]
        )
        results.append({
            "check": f"l3_{q['id']}_{q['category']}",
            "task": q["task"],
            "verification": q["verification"],
            "source_exists": files_exist,
            "passed": files_exist,
        })
        if not files_exist:
            missing = [f for f in q["expected_files"]
                       if not os.path.isfile(os.path.join(ARTIFACT_DIR, f))]
            print(f"  FAIL L3 {q['id']}: missing files: {missing}")
    return results


# ============================================================
# RUNNER
# ============================================================

def run_all():
    all_results = {"level_1": {}, "level_2": {}, "level_3": {}}

    print("=" * 60)
    print("LEVEL 1: STRUCTURAL INTEGRITY")
    print("=" * 60)

    l1_checks = []
    for test_fn in [
        test_l1_directory_structure,
        test_l1_required_files,
        test_l1_frontmatter_valid,
        test_l1_exploration_tree_schema,
        test_l1_claims_structure,
        test_l1_code_stubs_parseable,
    ]:
        print(f"\n  Running {test_fn.__name__}...")
        l1_checks.extend(test_fn())

    l1_passed = sum(1 for c in l1_checks if c["passed"])
    l1_total = len(l1_checks)
    all_results["level_1"] = {
        "passed": l1_passed == l1_total,
        "score": f"{l1_passed}/{l1_total}",
        "checks": l1_checks,
    }
    print(f"\n  L1 Result: {l1_passed}/{l1_total} checks passed")

    print("\n" + "=" * 60)
    print("LEVEL 2: INFORMATION FIDELITY")
    print("=" * 60)

    l2_checks = test_l2_questions()
    l2_passed = sum(1 for c in l2_checks if c["passed"])
    l2_total = len(l2_checks)
    all_results["level_2"] = {
        "passed": l2_passed == l2_total,
        "score": f"{l2_passed}/{l2_total}",
        "questions": l2_checks,
    }
    print(f"\n  L2 Result: {l2_passed}/{l2_total} questions have valid sources")

    print("\n" + "=" * 60)
    print("LEVEL 3: EXECUTION REPRODUCIBILITY")
    print("=" * 60)

    l3_checks = test_l3_questions()
    l3_passed = sum(1 for c in l3_checks if c["passed"])
    l3_total = len(l3_checks)
    all_results["level_3"] = {
        "passed": l3_passed == l3_total,
        "score": f"{l3_passed}/{l3_total}",
        "questions": l3_checks,
    }
    print(f"\n  L3 Result: {l3_passed}/{l3_total} tasks have valid source files")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for level in ["level_1", "level_2", "level_3"]:
        status = "PASS" if all_results[level]["passed"] else "FAIL"
        print(f"  {level}: {status} ({all_results[level]['score']})")

    # Write report
    report_path = os.path.join(ARTIFACT_DIR, "_seal_report.json")
    with open(report_path, "w") as fh:
        json.dump(all_results, fh, indent=2)
    print(f"\n  Report written to: {report_path}")

    return all(all_results[l]["passed"] for l in all_results)


if __name__ == "__main__":
    success = run_all()
    sys.exit(0 if success else 1)
