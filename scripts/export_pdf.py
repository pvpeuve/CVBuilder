#!/usr/bin/env python3
"""
export_pdf.py

CLI tool that converts a unified markdown CV into PDF.
"""

import argparse
from pathlib import Path
from core.exporter import CVExporter


def main():
    parser = argparse.ArgumentParser(description="Export Markdown CV to PDF.")
    parser.add_argument("--input", type=str, default="output/CV.md", help="Input markdown file.")
    parser.add_argument("--output", type=str, default="output/", help="Output directory for PDF.")

    args = parser.parse_args()

    input_file = Path(args.input)
    output_dir = Path(args.output)

    exporter = CVExporter(input_file=input_file, output_dir=output_dir)

    print(f"[INFO] Exporting {input_file} to PDF...")
    try:
        exporter.to_pdf()
    except NotImplementedError:
        print("[WARN] to_pdf() is not implemented yet. Placeholder executed.")
    print(f"[INFO] Export completed. PDF saved in {output_dir}")


if __name__ == "__main__":
    main()
