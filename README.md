# 📄 CVAssembler — Framework modular para generar CVs en Markdown y PDF

**CVAssembler** es una herramienta modular escrita en Python que permite construir, unificar y exportar CVs profesionales usando secciones en Markdown y plantillas dinámicas.

Incluye scripts CLI, plantillas personalizables, soporte para CI/CD y generación automática de PDF mediante `pypandoc` y `xelatex`.

---

## 🚀 Características principales

* 🧩 **Secciones modulares** (`sections/`) → perfiles, educación, experiencia, habilidades, proyectos…
* 🎨 **Plantillas personalizables** (`templates/default.md`)
* 🛠️ **Core en Python** para unir secciones y exportar a PDF/HTML
* 📦 **Scripts CLI** (`scripts/`) listos para automatizar generación y exportación
* 🔄 **CI/CD integrado** (GitHub Actions)
* 🧪 **Tests automáticos** con pytest + ruff

---

## 📂 Estructura del repositorio

```bash
CVAssembler/
├── core/ # Lógica interna: builder, parser, exporter
├── scripts/ # Scripts de automatización CLI
├── templates/ # Plantillas base (Markdown)
├── sections/ # Secciones modulares del CV
├── output/ # Archivos generados (.md / .pdf)
├── certificates/ # Certificados opcionales del usuario
├── tests/ # Pruebas automáticas
├── docs/ # Documentación (changelog, etc.)
└── .github/workflows/ # CI/CD (lint, tests, demo PDF)
```

---

## 🧠 ¿Cómo funciona?

### 1. Unir secciones en un único CV Markdown

```bash
python scripts/merge_sections.py
```
Esto genera:

**output/CV.md**

### 2. Exportar el CV a PDF

```bash
python scripts/export_pdf.py --input output/CV.md --output output/
```
Esto genera:

**output/CV.pdf**

### 3. Generar un CV completo (merge + export)

```bash
python scripts/generate_cv.py --pdf
```
Modo demo (usado en CI/CD):
```bash
python scripts/generate_cv.py --demo --pdf
```

---

## 🎨 Plantilla personalizable

Se encuentra en:

**templates/default.md**

Incluye placeholders como:
```bash
{{nombre_completo}}
{{email}}
{{experiencia}}
{{habilidades_tecnicas}}
```

---

## 🔧 Scripts incluidos

| Script | Función |
|:------:|:-------:|
| merge_sections.py | Une todas las secciones en un solo Markdown |
| export_pdf.py | Convierte un Markdown a PDF con Pandoc |
| generate_cv.py | Pipeline completo (merge + PDF) |
| demo (CI/CD) | Genera automáticamente demo_CV.pdf |

---

## 🧪 Tests automáticos

* CI ejecuta:
  * Ruff (lint)
  * Pytest (tests unitarios)

* Se prueban:
  * Unión de secciones
  * Parser de secciones
  * Exporter con mocking de pypandoc

---

## 🔄 CI/CD (GitHub Actions)

### CI — Lint + Tests

* Ejecuta automáticamente:
  * Formato con Ruff
  * Test suite con pytest

### CD — Build Demo CV

* Cuando CI pasa correctamente:
  * Genera un demo_CV.md
  * Exporta demo_CV.pdf
  * Lo sube como artifact en GitHub

Esto garantiza que cualquiera que haga fork tiene un CV funcional desde el primer minuto.

---

## 📦 Ejemplo de datos

En la carpeta sections/ ya existe un CV completo de demostración con placeholders totalmente genéricos.

Los usuarios solo deben abrirlos y reemplazar los valores.

---

## 🧰 Requisitos

* Python ≥ 3.12
* pypandoc
* pandoc (se instala dentro del CI/CD)
* xelatex (se instala dentro del CI/CD)

---

## 📄 Licencia

Este proyecto está bajo licencia MIT.

Puedes usarlo, modificarlo y adaptarlo libremente.

---

## 🤝 Contribuciones

Pull requests y mejoras son bienvenidas.
