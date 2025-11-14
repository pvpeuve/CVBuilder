"""
builder.py
-----------

Responsible for merging CV sections into a single Markdown file.
This module provides the CVBuilder class with basic structure.

The logic is implemented progressively as the framework evolves.
"""

from pathlib import Path

class CVBuilder:
    """
    Builds a unified CV from modular markdown sections.
    """

    def __init__(self, sections_dir: str | Path = "sections", output_file: str | Path = "output/CV.md"):
        self.sections_dir = Path(sections_dir)
        self.output_file = Path(output_file)

    def merge(self) -> str:
        """
        Basic merge: join ALL .md files in sections/ in alphabetical order.
        """
        parts = []

        for file in sorted(self.sections_dir.glob("*.md")):
            parts.append(file.read_text(encoding="utf-8"))

        return "\n\n".join(parts)

    def save(self) -> None:
        """Writes merged content to output_file."""
        content = self.merge()
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        self.output_file.write_text(content, encoding="utf-8")
