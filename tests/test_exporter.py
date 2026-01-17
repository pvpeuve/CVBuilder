from core.exporter import export
from unittest.mock import patch
import pytest


def test_exporter_calls_pandoc(tmp_path):
    """Exporter must call pypandoc.convert_file() to generate the PDF."""

    md_file = tmp_path / "sample.md"
    md_file.write_text("# Test CV", encoding="utf-8")

    exporter = export(input_file=md_file, output_dir=tmp_path)

    with patch("pypandoc.convert_file") as mock_convert:
        pdf_path = exporter.to_pdf()

        mock_convert.assert_called_once()

        args, kwargs = mock_convert.call_args

        assert kwargs["outputfile"] == str(pdf_path)


def test_exporter_missing_file(tmp_path):
    """Exporter must raise error when markdown file does not exist."""

    missing_md = tmp_path / "no_existe.md"
    exporter = export(input_file=missing_md, output_dir=tmp_path)

    with pytest.raises(FileNotFoundError):
        exporter.to_pdf()
