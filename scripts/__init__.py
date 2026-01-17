"""
CVAssembler scripts package.

Contains the main CLI tools for:
- generating CVs
- exporting CVs to PDF
- merging sections

This package is intentionally minimal.
Full logic is implemented progressively in later versions.
"""

from .generate_cv import main as generate
from .export_pdf import main as export
from .merge_sections import main as merge

__all__ = ["generate", "export", "merge"]