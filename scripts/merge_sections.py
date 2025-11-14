#!/usr/bin/env python3
"""
merge_sections.py

CLI tool that uses CVBuilder to merge markdown sections
into a unified CV markdown file.
"""

import argparse
from pathlib import Path
from core.builder import CVBuilder


def main():
    parser = argparse.ArgumentParser(description="Merge CV sections into a single Markdown file.")
    parser.add_argument("--sections", type=str, default="sections/", help="Directory with .md section files.")
    parser.add_argument("--output", type=str, default="output/CV.md", help="Final merged markdown file.")

    args = parser.parse_args()

    sections_dir = Path(args.sections)
    output_file = Path(args.output)

    builder = CVBuilder(sections_dir=sections_dir, output_file=output_file)

    print(f"[INFO] Merging sections from {sections_dir} ...")
    try:
        builder.build()
    except NotImplementedError:
        print("[WARN] build() is not implemented yet. Placeholder executed.")
    print(f"[INFO] Output saved to {output_file}")


if __name__ == "__main__":
    main()
