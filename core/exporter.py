"""
exporter.py
-----------

Exports unified Markdown CV into PDF using pypandoc.
"""

from pathlib import Path
import pypandoc


class CVExporter:
    """Exports Markdown files into PDF format."""

    def export(self, markdown_file: str | Path, output_file: str | Path) -> Path:
        markdown_file = Path(markdown_file)
        output_file = Path(output_file)

        if not markdown_file.exists():
            raise FileNotFoundError(f"Markdown file not found: {markdown_file}")

        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Convert using pypandoc
        pypandoc.convert_file(
            source_file=str(markdown_file),
            to="pdf",
            outputfile=str(output_file),
            extra_args=["--pdf-engine=xelatex"]
        )

        return output_file
