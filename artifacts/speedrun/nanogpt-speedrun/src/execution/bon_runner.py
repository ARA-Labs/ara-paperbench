"""
Best-of-N Science Runner with AIDE extensions.

Paper: "The Automated LLM Speedrunning Benchmark" (arXiv:2506.22419)
Core search loop implementing Algorithm 1: version selection -> ideation -> coding -> execution -> analysis.

Search variants are configured by parameter choices:
  - Tree:       N_0=1, N=3, p_debug=0
  - Forest:     N_0=3, N=3, p_debug=0
  - AIDE:       N_0=5, N=1, p_debug=0.5, D_max=3
  - Multi-AIDE: N_0=3, N=3, p_debug=0.5, D_max=3
  - Flat:       N_0=20, N=0, p_debug=0
"""

from typing import Dict, List, Optional, Tuple
import random


class BoNScienceRunner:
    """
    Implements the main agent search loop over a versioned workspace tree.

    Extends the base ScienceRunner with:
    - Configurable initial population (N_0)
    - Branching factor (N) for parallel hypothesis exploration
    - Debug probability (p_debug) for alternating between exploit and debug modes
    - Max bug depth (D_max) to abandon unfixable branches

    Args:
        workspace: VersionTree managing code versions
        ideator: Hypothesis generator (or DummyIdeator for hint pass-through)
        coder: AiderCoder for diff-based code editing
        executor: Slurm job submission and monitoring
        analyzer: Log summarization and metric extraction
        knowledge_store: KnowledgeStore for loading hint files
        n_initial_hypotheses: N_0 -- number of initial root solutions
        n_hypotheses: N -- branching factor per iteration
        debug_prob: p_debug -- probability of selecting buggy leaf for debug
        max_bug_depth: D_max -- max consecutive debug attempts
        max_n_nodes: M -- total search budget (number of solutions to evaluate)
    """

    def __init__(
        self,
        workspace,          # VersionTree
        ideator,            # BaseIdeator | DummyIdeator
        coder,              # AiderCoder | BaseCoder
        executor,           # SlurmExecutor | LocalExecutor
        analyzer,           # Analyzer
        knowledge_store,    # Optional[KnowledgeStore]
        n_initial_hypotheses: int = 3,
        n_hypotheses: int = 3,
        debug_prob: float = 0.5,
        max_bug_depth: int = 3,
        max_n_nodes: int = 20,
    ):
        self.workspace = workspace
        self.ideator = ideator
        self.coder = coder
        self.executor = executor
        self.analyzer = analyzer
        self.knowledge = knowledge_store
        self.n_0 = n_initial_hypotheses
        self.n = n_hypotheses
        self.p_debug = debug_prob
        self.d_max = max_bug_depth
        self.m = max_n_nodes

    def select_next_version(self) -> Tuple[str, bool]:
        """
        Select parent version for next iteration.

        With probability p_debug, selects a random buggy leaf version
        (if any exist with bug_depth <= D_max). Otherwise, selects the
        best-performing valid version by selection metric (lowest train_time
        among solutions with val_loss <= 3.28).

        Returns:
            (version_id, is_debug_mode): Selected version and whether
            we're in debug mode.
        """
        buggy_leaves = self.workspace.get_buggy_leaves(max_depth=self.d_max)

        if buggy_leaves and random.random() < self.p_debug:
            return random.choice(buggy_leaves), True

        return self.workspace.get_best_version(
            metric="train_time",
            constraint={"val_loss": ("<=", 3.28)},
            lower_is_better=True,
        ), False

    def run_experiment(
        self,
        parent_version: str,
        hypothesis: str,
        is_debug: bool = False,
    ) -> str:
        """
        Execute one experiment: branch workspace, code changes, submit job.

        Steps:
        1. Branch workspace from parent_version -> new version
        2. Apply code edits via Coder (AiderCoder diff-based editing)
        3. Submit modified train_gpt2.py to Slurm executor
        4. Return new version ID (results populated asynchronously)

        Args:
            parent_version: Version to branch from
            hypothesis: Natural-language hypothesis to implement
            is_debug: Whether this is a debug attempt (affects prompting)

        Returns:
            new_version_id: The created version identifier
        """
        new_version = self.workspace.branch(parent_version)

        bug_history = (
            self.workspace.get_bug_history(parent_version)
            if is_debug else None
        )

        self.coder.edit(
            workspace_path=self.workspace.get_path(new_version),
            hypothesis=hypothesis,
            bug_history=bug_history,
            knowledge=self.knowledge.get_text() if self.knowledge else None,
        )

        self.executor.submit(
            script_path=f"{self.workspace.get_path(new_version)}/train_gpt2.py",
            version_id=new_version,
        )

        return new_version

    def run(self) -> Dict:
        """
        Main search loop implementing Algorithm 1.

        Phase 1: Generate N_0 initial solutions from root version.
        Phase 2: Iteratively select parent, generate N hypotheses,
                 branch + code + execute for each, until budget M exhausted.

        Returns:
            Dict with 'best_version', 'best_train_time', 'total_nodes'
        """
        node_count = 0
        root = self.workspace.root_version

        # Phase 1: Initial population
        for _ in range(self.n_0):
            if node_count >= self.m:
                break
            hypothesis = self.ideator.generate(
                code=self.workspace.get_code(root),
                knowledge=self.knowledge,
            )
            self.run_experiment(root, hypothesis)
            node_count += 1

        self.executor.wait_all()
        self.analyzer.process_all_pending()

        # Phase 2: Iterative search
        while node_count < self.m:
            parent, is_debug = self.select_next_version()

            if is_debug:
                hypothesis = self.ideator.debug(
                    code=self.workspace.get_code(parent),
                    bug_summary=self.workspace.get_bug_summary(parent),
                )
                self.run_experiment(parent, hypothesis, is_debug=True)
                node_count += 1
            else:
                for _ in range(min(self.n, self.m - node_count)):
                    hypothesis = self.ideator.generate(
                        code=self.workspace.get_code(parent),
                        knowledge=self.knowledge,
                        history=self.workspace.get_history(parent),
                    )
                    self.run_experiment(parent, hypothesis)
                    node_count += 1

            self.executor.wait_all()
            self.analyzer.process_all_pending()

        best = self.workspace.get_best_version(
            metric="train_time",
            constraint={"val_loss": ("<=", 3.28)},
            lower_is_better=True,
        )

        return {
            "best_version": best,
            "best_train_time": self.workspace.get_metric(best, "train_time"),
            "total_nodes": node_count,
        }
