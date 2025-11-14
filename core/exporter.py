"""
exporter.py
------------

Handles conversion from Markdown to PDF/HTML using external tools
like Pandoc or PyPandoc.

This file contains structure only — implementation is added gradually.
"""

from pathlib import Path


class CVExporter:
    """
    Export Markdown files into PDF/HTML formats.

    Parameters
    ----------
    input_file : Path
        Path to the markdown file to export.
    output_dir : Path
        Folder where outputs (PDF/HTML) will be saved.
    """

    def __init__(self, input_file: Path, output_dir: Path):
        self.input_file = input_file
        self.output_dir = output_dir

    def to_pdf(self) -> Path:
        """
        Convert the Markdown input file to PDF.

        Stub — implementation is added later.
        """
        raise NotImplementedError("to_pdf() will be implemented in later versions.")

    def to_html(self) -> Path:
        """
        Convert the Markdown input file to HTML.

        Stub — implementation is added later.
        """
        raise NotImplementedError("to_html() will be implemented in later versions.")
