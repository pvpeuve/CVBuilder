"""
CVBuilder core package.

Contains the main building blocks for:
- merging sections
- exporting generated CVs
- parsing data files (JSON/YAML)

This package is intentionally minimal.
Full logic is implemented progressively in later versions.
"""

from .builder import CVBuilder
from .exporter import CVExporter

__all__ = ["CVBuilder", "CVExporter"]
