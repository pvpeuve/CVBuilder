import pypandoc
from pathlib import Path

BASE = Path(__file__).parent.parent
INPUT = BASE / "salidas" / "CV_ES.md"
OUTPUT = BASE / "salidas" / "CV_ES.pdf"

def export_pdf():
    try:
        pypandoc.convert_text(
            INPUT.read_text(encoding="utf-8"),
            "pdf",
            format="md",
            outputfile=str(OUTPUT),
            extra_args=["--standalone"]
        )
        print(f"✅ PDF generado correctamente: {OUTPUT}")
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")

if __name__ == "__main__":
    export_pdf()
