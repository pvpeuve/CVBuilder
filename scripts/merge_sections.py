#!/usr/bin/env python3
"""
merge_sections.py

CLI tool that uses CVBuilder to merge markdown sections
into a unified CV markdown file.
"""

import typer
from pathlib import Path
from core.builder import build


app = typer.Typer()

@app.command(help="Merge CV sections into a single Markdown file.")
def main(
    sections: str = typer.Option("sections/", help="Directory with .md section files."),
    output: str = typer.Option("output/CV.md", help="Final merged markdown file."),
):
    sections_dir = Path(sections)
    output_file = Path(output)

    builder = build(sections_dir=sections_dir, output_file=output_file)

    typer.echo(f"[INFO] Merging sections from {sections_dir} ...")
    try:
        builder.merge()
    except NotImplementedError:
        typer.echo("[WARN] merge() is not implemented yet. Placeholder executed.")
    typer.echo(f"[INFO] Output saved to {output_file}")


if __name__ == "__main__":
    app()
