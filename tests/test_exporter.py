from core.exporter import CVExporter
from unittest.mock import patch
import pytest


def test_exporter_calls_pandoc(tmp_path):
    """Exporter must call pypandoc.convert_file() to generate the PDF."""

    exporter = CVExporter()

    md_file = tmp_path / "sample.md"
    out_file = tmp_path / "out.pdf"

    md_file.write_text("# Test CV", encoding="utf-8")

    with patch("pypandoc.convert_file") as mock_convert:
        exporter.export(md_file, out_file)

        mock_convert.assert_called_once()
        args, kwargs = mock_convert.call_args
        assert kwargs["outputfile"] == str(out_file)


def test_exporter_missing_file():
    """Exporter must raise error when markdown file does not exist."""

    exporter = CVExporter()

    with pytest.raises(FileNotFoundError):
        exporter.export("no_existe.md", "salida.pdf")
