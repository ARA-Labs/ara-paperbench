"""
Knowledge/Hint Store.

Paper: "The Automated LLM Speedrunning Benchmark" (arXiv:2506.22419)
Loads hint files at configurable abstraction levels and injects them
into ideator/coder prompts.

Hint levels:
  0 -- Raw git diff between consecutive records
  1 -- Pseudocode description of algorithmic changes
  2 -- Natural-language text description with rationale
  3 -- Mini-paper summarizing changes (most detailed)
  9 -- External API documentation (e.g., FlexAttention docs)
  z -- Zero knowledge (no hints provided)

File structure per record:
  data/nanogpt_speedrun_knowledge_in_levels/record_{i}/level_{m}_*.txt

Multiple levels can be combined (e.g., levels=[1, 2, 3] loads
pseudocode + text + mini-paper). The concatenated text is injected
into the KNOWLEDGE_INFO_COMPONENT prompt template.
"""

from pathlib import Path
from typing import List, Optional


class KnowledgeStore:
    """
    Loads and manages hint files for a given record transition.

    Args:
        data_dir: Root directory containing record hint subdirectories
        record: Record index (1-20)
        levels: List of hint levels to load (e.g., [1], [1, 2, 3])
    """

    def __init__(
        self,
        data_dir: str,
        record: int,
        levels: List[int],
    ):
        self.data_dir = Path(data_dir)
        self.record = record
        self.levels = levels
        self._text: Optional[str] = None

    def load(self) -> str:
        """
        Load and concatenate hint files for configured levels.

        File naming convention:
          level_0_diff.txt
          level_1_pseudo.txt
          level_2_description.txt
          level_3_paper.txt
          level_9_*.txt (glob for multiple external docs)

        Returns:
            Concatenated hint text, with level headers for clarity.
        """
        if self._text is not None:
            return self._text

        record_dir = self.data_dir / f"record_{self.record}"
        parts = []

        for level in sorted(self.levels):
            pattern = f"level_{level}_*.txt"
            files = sorted(record_dir.glob(pattern))

            for f in files:
                content = f.read_text().strip()
                if content:
                    parts.append(
                        f"=== Level {level} Knowledge: {f.stem} ===\n\n{content}"
                    )

        self._text = "\n\n".join(parts) if parts else ""
        return self._text

    def get_text(self) -> Optional[str]:
        """
        Get loaded hint text, or None if no levels configured.

        Returns:
            Hint text string or None if levels list is empty.
        """
        if not self.levels:
            return None
        return self.load()

    @staticmethod
    def from_config(
        data_dir: str,
        record: int,
        level_string: str,
    ) -> "KnowledgeStore":
        """
        Create KnowledgeStore from a level string (e.g., "123" -> [1, 2, 3]).

        Args:
            data_dir: Root data directory
            record: Record index
            level_string: String of level digits, e.g., "1", "12", "123", "z"

        Returns:
            Configured KnowledgeStore instance
        """
        if level_string == "z" or not level_string:
            return KnowledgeStore(data_dir, record, levels=[])

        levels = [int(c) for c in level_string]
        return KnowledgeStore(data_dir, record, levels=levels)
