#!/usr/bin/env python3
"""
generate_cv.py

High-level wrapper that:
1. Merges sections into a single markdown file.
2. Exports the markdown file into PDF.
"""

import argparse
from pathlib import Path
from core.builder import CVBuilder
from core.exporter import CVExporter


def main():
    parser = argparse.ArgumentParser(description="Generate complete CV (MD + PDF).")
    parser.add_argument("--sections", type=str, default="sections/", help="Directory of CV sections.")
    parser.add_argument("--md-output", type=str, default="output/CV.md", help="Merged markdown output file.")
    parser.add_argument("--pdf-output-dir", type=str, default="output/", help="Directory for generated PDF.")

    args = parser.parse_args()

    sections_dir = Path(args.sections)
    md_output = Path(args.md_output)
    pdf_output_dir = Path(args.pdf_output_dir)

    print("[INFO] Step 1: Merging Markdown sections...")
    builder = CVBuilder(sections_dir=sections_dir, output_file=md_output)
    try:
        builder.build()
    except NotImplementedError:
        print("[WARN] build() not implemented yet. Placeholder executed.")

    print("[INFO] Step 2: Exporting to PDF...")
    exporter = CVExporter(input_file=md_output, output_dir=pdf_output_dir)
    try:
        exporter.to_pdf()
    except NotImplementedError:
        print("[WARN] to_pdf() not implemented yet. Placeholder executed.")

    print("[INFO] CV generation process completed.")


if __name__ == "__main__":
    main()
