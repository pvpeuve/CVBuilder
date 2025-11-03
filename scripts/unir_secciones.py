import re
from pathlib import Path

BASE = Path(__file__).parent.parent
TEMPLATE = BASE / "plantillas" / "plantilla_ES.md"
OUTPUT = BASE / "salidas" / "CV_ES.md"

# Mapeo entre etiquetas y archivos fuente
sources = {
    "nombre_completo": BASE / "datos" / "contacto.md",
    "contacto": BASE / "datos" / "contacto.md",
    "perfil": BASE / "datos" / "perfil.md",
    "experiencia": BASE / "datos" / "experiencia.md",
    "educacion": BASE / "datos" / "educacion.md",
    "habilidades_tecnicas": BASE / "datos" / "habilidades_tecnicas.md",
    "habilidades_blandas": BASE / "datos" / "habilidades_blandas.md",
    "idiomas": BASE / "datos" / "idiomas.md",
    "certificaciones": BASE / "certificaciones" / "resumen_certificaciones.md",  # opcional
}

def build_cv():
    text = TEMPLATE.read_text(encoding="utf-8")

    for key, path in sources.items():
        content = path.read_text(encoding="utf-8") if path.exists() else f"⚠️ Falta {key}"
        text = re.sub(r"{{\s*" + key + r"\s*}}", content.strip(), text)

    OUTPUT.write_text(text, encoding="utf-8")
    print(f"✅ CV generado en: {OUTPUT}")

if __name__ == "__main__":
    build_cv()
