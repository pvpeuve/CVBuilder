import pypandoc
from pathlib import Path


class export:
    """
    Export Markdown files into PDF/HTML formats.
    """

    def __init__(self, input_file: Path, output_dir: Path):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)

    def to_pdf(self) -> Path:
        """
        Converts the Markdown input file to a PDF file using pypandoc.
        """
        if not self.input_file.exists():
            raise FileNotFoundError(f"Markdown file not found: {self.input_file}")

        self.output_dir.mkdir(exist_ok=True, parents=True)

        output_pdf = self.output_dir / (self.input_file.stem + ".pdf")

        # Llamada real a Pandoc vía pypandoc
        pypandoc.convert_file(
            str(self.input_file),
            "pdf",
            outputfile=str(output_pdf),
            extra_args=["--pdf-engine=xelatex",
			"-V", "geometry:margin=1.5cm",
			"-V", "mainfont=DejaVu Serif",
			"-V", "sansfont=DejaVu Sans",
			"-V", "monofont=DejaVu Sans Mono"
			]
        )

        return output_pdf

    def to_html(self) -> Path:
        """
        Converts Markdown to HTML file.
        """
        if not self.input_file.exists():
            raise FileNotFoundError(f"Markdown file not found: {self.input_file}")

        self.output_dir.mkdir(exist_ok=True, parents=True)

        output_html = self.output_dir / (self.input_file.stem + ".html")

        pypandoc.convert_file(
            str(self.input_file),
            "html",
            outputfile=str(output_html)
        )

        return output_html
