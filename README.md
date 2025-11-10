# CVBuilder — Framework de generación de CVs en Markdown

**CVBuilder** es una herramienta modular en Python diseñada para crear, unificar y exportar CVs o portfolios profesionales a partir de archivos Markdown.  
Su objetivo es ofrecer una base personalizable para generar documentos en formato `.md` y `.pdf` de forma automatizada.

---

## 🚀 Características principales

- 🧩 Estructura modular por secciones (`sections/`)
- 🧱 Plantillas personalizables en Markdown (`templates/`)
- ⚙️ Scripts Python para unir, exportar y publicar (`scripts/`)
- 🧾 Compatibilidad con CI/CD (GitHub Actions)
- 🌐 Soporte multiidioma (ES / EN)

---

## 📂 Estructura del repositorio

CVBuilder/
├── core/ # Módulos internos de construcción/exportación
├── scripts/ # Automatización CLI
├── templates/ # Plantillas base (ES/EN)
├── sections/ # Secciones modulares del CV
├── certificates/ # Certificados del usuario (PDF/JPG)
├── output/ # CV generado (.md / .pdf)
├── docs/ # Documentación adicional
├── tests/ # Pruebas automatizadas
└── .github/workflows/ # CI/CD

---

## 🧠 Ejemplo de uso

### 1. Editar las secciones en `sections/`
```markdown
# sections/profile.md
## Profile
Passionate developer focused on automation and IoT projects.
...
```

### 2. Generar el CV unificado
```bash
python scripts/merge_sections.py
```

### 3. Exportar a PDF
```bash
python scripts/export_pdf.py
```
El resultado se guarda en output/CV_EN.pdf.

---

## 🧪 Pipeline (CI/CD)

1. CI: Linter (ruff) + Tests (pytest)

2. CD: Generación automática del PDF y publicación como artefacto

3. Opcional: Integración con APIs o publicación en LinkedIn / GitHub Pages

## 💡 Ejemplo incluido

En examples/ encontrarás un caso de demostración genérico:

- example_JohnDoe.json

- example_JohnDoe.md

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT.
Eres libre de usar, modificar y adaptar este framework para tus propios CVs o portfolios.

---

## 🧰 Requisitos

- Python ≥ 3.10

- PyPandoc (pip install pypandoc)

- Opcional: GitHub Actions para automatización CI/CD

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas.
Puedes enviar pull requests con mejoras en la estructura, scripts o plantillas.
