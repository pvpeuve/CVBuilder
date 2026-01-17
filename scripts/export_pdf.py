#!/usr/bin/env python3
"""
export_pdf.py

CLI tool that converts a unified markdown CV into PDF.
"""

import typer
from pathlib import Path
from core.exporter import export


app = typer.Typer()

@app.command(help="Export Markdown CV to PDF.")
def main(
    input: str = typer.Option("output/CV.md", help="Input markdown file."),
    output: str = typer.Option("output/", help="Output directory for PDF."),
):
    input_file = Path(input)
    output_dir = Path(output)

    exporter = export(input_file=input_file, output_dir=output_dir)

    typer.echo(f"[INFO] Exporting {input_file} to PDF...")

    pdf_path = exporter.to_pdf()
    typer.echo(f"[OK] PDF generated at: {pdf_path}")


if __name__ == "__main__":
    app()
