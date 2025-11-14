"""
parser.py
-----------

Reads structured JSON/YAML data and injects it into templates.
Useful for fully automated CV generation.

Not required for basic functionality.
"""

import json
from pathlib import Path
from typing import Dict, Any

class SectionParser:
    """
    Minimal section parser.

    The test suite expects:
        SectionParser("sections")
    So we must accept a directory path.
    """

    def __init__(self, sections_dir: str | Path):
        self.sections_dir = Path(sections_dir)

    def parse(self, text: str) -> str:
        """Basic parser that simply trims whitespace."""
        return text.strip()

    def load_section(self, name: str) -> str:
        """
        Loads a markdown section file by name.
        Example:
            load_section("perfil") -> sections/perfil.md
        """

        file = self.sections_dir / f"{name}.md"
        if not file.exists():
            return ""

        return file.read_text(encoding="utf-8")

class DataParser:
    """Utility to load user data from JSON files."""

    def load_json(self, file: Path) -> Dict[str, Any]:
        """Return dictionary loaded from a JSON file."""
        with file.open("r", encoding="utf-8") as f:
            return json.load(f)
