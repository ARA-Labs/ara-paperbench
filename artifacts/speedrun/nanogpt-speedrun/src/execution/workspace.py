"""
Versioned Workspace Manager.

Paper: "The Automated LLM Speedrunning Benchmark" (arXiv:2506.22419)
Maintains a tree of code versions where each node stores train_gpt2.py,
metadata (parent, children, timestamps), and results (metrics, hypothesis).

Each version v_k is a directory containing:
- train_gpt2.py: The modified training script
- meta.json: {parent, children, bug_depth, stable_ancestor, created_at}
- results.json: {status, metrics: {val_loss, train_time, n_steps},
                 hypothesis, outcome_summary, is_valid}
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class VersionTree:
    """
    Manages a tree of code versions for agent search.

    The tree supports:
    - Branching: create v_{k+1} from any existing v_k
    - Best-first selection: find the version with lowest train_time
      among valid solutions (val_loss <= 3.28)
    - Debug selection: find buggy leaves within max bug depth
    - History traversal: walk up the tree from any version to collect
      the chain of hypotheses and outcomes for context

    Args:
        base_dir: Root directory for all version subdirectories
        template_code: Initial train_gpt2.py content for v_0
    """

    def __init__(self, base_dir: str, template_code: str):
        self.base_dir = Path(base_dir)
        self.versions: Dict[str, Dict] = {}
        self.next_id = 0

        # Create root version v_0
        self.root_version = self._create_version(
            parent=None,
            code=template_code,
        )

    def _create_version(
        self,
        parent: Optional[str],
        code: str,
    ) -> str:
        """Create a new version directory with code and metadata."""
        vid = f"v_{self.next_id}"
        self.next_id += 1

        vdir = self.base_dir / vid
        vdir.mkdir(parents=True, exist_ok=True)

        (vdir / "train_gpt2.py").write_text(code)

        meta = {
            "parent": parent,
            "children": [],
            "bug_depth": 0,
            "created_at": None,  # timestamp set by caller
        }
        (vdir / "meta.json").write_text(json.dumps(meta, indent=2))

        if parent:
            # Update parent's children list
            parent_meta = self._read_meta(parent)
            parent_meta["children"].append(vid)
            self._write_meta(parent, parent_meta)

        self.versions[vid] = meta
        return vid

    def branch(self, parent: str) -> str:
        """
        Create a new version branched from parent.

        Copies parent's train_gpt2.py to new version directory.
        Sets bug_depth to parent's bug_depth + 1 if parent is buggy,
        else 0.

        Args:
            parent: Version ID to branch from

        Returns:
            New version ID
        """
        parent_code = self.get_code(parent)
        new_vid = self._create_version(parent=parent, code=parent_code)
        return new_vid

    def get_code(self, version: str) -> str:
        """Read train_gpt2.py from a version directory."""
        return (self.base_dir / version / "train_gpt2.py").read_text()

    def get_path(self, version: str) -> str:
        """Get filesystem path for a version directory."""
        return str(self.base_dir / version)

    def get_metric(self, version: str, metric: str) -> Optional[float]:
        """Get a specific metric value from a version's results."""
        results = self._read_results(version)
        if results and "metrics" in results:
            return results["metrics"].get(metric)
        return None

    def get_best_version(
        self,
        metric: str = "train_time",
        constraint: Optional[Dict] = None,
        lower_is_better: bool = True,
    ) -> str:
        """
        Find the version with the best metric value among valid solutions.

        Args:
            metric: Metric name to optimize (default: train_time)
            constraint: Dict of {metric_name: (op, threshold)} filters
                       e.g., {"val_loss": ("<=", 3.28)}
            lower_is_better: Minimize metric if True, maximize if False

        Returns:
            Version ID of the best valid solution
        """
        candidates = []
        for vid in self.versions:
            results = self._read_results(vid)
            if results and results.get("is_valid", False):
                if constraint:
                    passes = all(
                        self._check_constraint(
                            results["metrics"].get(k), op, thresh
                        )
                        for k, (op, thresh) in constraint.items()
                    )
                    if not passes:
                        continue
                candidates.append((vid, results["metrics"].get(metric, float("inf"))))

        if not candidates:
            return self.root_version

        candidates.sort(key=lambda x: x[1], reverse=not lower_is_better)
        return candidates[0][0]

    def get_buggy_leaves(self, max_depth: int = 3) -> List[str]:
        """
        Find buggy leaf versions within max bug depth.

        A version is a buggy leaf if:
        - Its status is 'buggy' (runtime error, crash, or val_loss > 3.28)
        - It has no children
        - Its bug_depth <= max_depth

        Returns:
            List of buggy leaf version IDs
        """
        leaves = []
        for vid, meta in self.versions.items():
            if not meta.get("children"):
                results = self._read_results(vid)
                if results and results.get("status") == "buggy":
                    if meta.get("bug_depth", 0) <= max_depth:
                        leaves.append(vid)
        return leaves

    def get_history(self, version: str) -> List[Dict]:
        """
        Walk up the tree from version to root, collecting
        hypothesis + outcome pairs for context.

        Returns:
            List of {version, hypothesis, outcome_summary, metrics}
            from root to version (chronological order).
        """
        history = []
        current = version
        while current:
            results = self._read_results(current)
            if results:
                history.append({
                    "version": current,
                    "hypothesis": results.get("hypothesis", ""),
                    "outcome_summary": results.get("outcome_summary", ""),
                    "metrics": results.get("metrics", {}),
                })
            meta = self._read_meta(current)
            current = meta.get("parent")
        history.reverse()
        return history

    def get_bug_history(self, version: str) -> List[Dict]:
        """
        Collect bug summaries from version back to last non-buggy ancestor.

        Returns:
            List of {version, bug_summary, error_type} for consecutive
            buggy versions in the chain.
        """
        bugs = []
        current = version
        while current:
            results = self._read_results(current)
            if results and results.get("status") == "buggy":
                bugs.append({
                    "version": current,
                    "bug_summary": results.get("outcome_summary", ""),
                    "error_type": results.get("error_type", "unknown"),
                })
            else:
                break
            meta = self._read_meta(current)
            current = meta.get("parent")
        bugs.reverse()
        return bugs

    def get_bug_summary(self, version: str) -> str:
        """Get a formatted bug summary for a version."""
        results = self._read_results(version)
        if results:
            return results.get("outcome_summary", "No bug summary available")
        return "No results available"

    def _read_meta(self, version: str) -> Dict:
        path = self.base_dir / version / "meta.json"
        return json.loads(path.read_text()) if path.exists() else {}

    def _write_meta(self, version: str, meta: Dict) -> None:
        path = self.base_dir / version / "meta.json"
        path.write_text(json.dumps(meta, indent=2))

    def _read_results(self, version: str) -> Optional[Dict]:
        path = self.base_dir / version / "results.json"
        return json.loads(path.read_text()) if path.exists() else None

    @staticmethod
    def _check_constraint(value, op: str, threshold) -> bool:
        if value is None:
            return False
        ops = {"<=": lambda a, b: a <= b, ">=": lambda a, b: a >= b}
        return ops.get(op, lambda a, b: False)(value, threshold)
