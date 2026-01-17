"""
CVAssembler core package.

Contains the main building blocks for:
- merging sections
- exporting generated CVs
- parsing data files (JSON/YAML)

This package is intentionally minimal.
Full logic is implemented progressively in later versions.
"""

from .builder import build
from .exporter import export

__all__ = ["build", "export"]
