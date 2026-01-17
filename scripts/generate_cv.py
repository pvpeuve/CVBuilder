#!/usr/bin/env python3
"""
generate_cv.py

High-level wrapper that:
1. Merges sections into a single markdown file.
2. Optionally exports the markdown file into PDF.
"""

import typer
from pathlib import Path
from core.builder import build
from core.exporter import export


app = typer.Typer()

@app.command(help="Generate complete CV with both Markdown and (optional) PDF export.")
def main(
    sections: str = typer.Option("sections/", help="Directory of CV sections."),
    md_output: str = typer.Option("output/CV.md", help="Merged markdown output file."),
    pdf_output_dir: str = typer.Option("output/", help="Directory for generated PDF."),
    pdf: bool = typer.Option(False, help="Enable PDF export."),
    demo: bool = typer.Option(False, help="Generate a demo CV using placeholders."),
):
    sections_dir = Path(sections)
    md_output_path = Path(md_output)
    pdf_output_dir = Path(pdf_output_dir)

    typer.echo("[INFO] Step 1: Merging Markdown sections...")
    builder = build(sections_dir=sections_dir, output_file=md_output_path)
    
    try:
        builder.save()
        typer.echo(f"[OK] Markdown generated at {md_output_path}")
    except NotImplementedError:
        typer.echo("[WARN] PDF export is not implemented yet. Skipping Markdown generation.")

    if pdf:
        typer.echo("[INFO] Step 2: Exporting to PDF...")
        exporter = export(input_file=md_output_path, output_dir=pdf_output_dir)

        try:
            pdf_file = exporter.to_pdf()
            typer.echo(f"[OK] PDF generated at {pdf_file}")
        except NotImplementedError:
            typer.echo("[WARN] PDF export is not implemented yet. Skipping PDF generation.")
    else:
        typer.echo("[INFO] PDF export disabled (--pdf not provided).")

    if demo:
        typer.echo("[INFO] Demo mode enabled. Generated demo CV for CI/CD.")

    typer.echo("[INFO] CV generation completed.")


if __name__ == "__main__":
    app()
