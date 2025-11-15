#!/usr/bin/env python3
"""
generate_cv.py

High-level wrapper that:
1. Merges sections into a single markdown file.
2. Optionally exports the markdown file into PDF.
"""

import argparse
from pathlib import Path
from core.builder import CVBuilder
from core.exporter import CVExporter


def main():
    parser = argparse.ArgumentParser(description="Generate complete CV (MD + optional PDF).")

    parser.add_argument("--sections", default="sections/", help="Directory of CV sections.")
    parser.add_argument("--md-output", default="output/CV.md", help="Merged markdown output file.")
    parser.add_argument("--pdf-output-dir", default="output/", help="Directory for generated PDF.")
    parser.add_argument("--pdf", action="store_true", help="Enable PDF export.")
    parser.add_argument("--demo", action="store_true", help="Generate a demo CV using placeholders.")

    args = parser.parse_args()

    sections_dir = Path(args.sections)
    md_output = Path(args.md_output)
    pdf_output_dir = Path(args.pdf_output_dir)

    print("[INFO] Step 1: Merging Markdown sections...")
    builder = CVBuilder(sections_dir=sections_dir, output_file=md_output)

    builder.save()
    print(f"[OK] Markdown generated at {md_output}")

    if args.pdf:
        print("[INFO] Step 2: Exporting to PDF...")
        exporter = CVExporter(input_file=md_output, output_dir=pdf_output_dir)

        try:
            result = exporter.to_pdf()
            print(f"[OK] PDF generated at {result}")
        except NotImplementedError:
            print("[WARN] PDF export not implemented. Skipping.")

    if args.demo:
        print("[INFO] Demo mode enabled. Generated demo CV for CI/CD.")

    print("[INFO] CV generation completed.")


if __name__ == "__main__":
    main()
