# Currículum Profesional — Pablo Varela Mille
> Este proyecto implementa un sistema modular para mantener y generar el currículum en formato Markdown, permitiendo actualizar secciones individuales y automatizar la exportación a PDF o su sincronización con plataformas de empleo.
> Repositorio donde mantengo las versiones actualizadas de mi CV y portfolio técnico.

## Perfil
Técnico en IoT y Desarrollador Python Junior con experiencia práctica en automatización local, visión por computadora e integración domótica.

## Enlaces
- [LinkedIn](https://www.linkedin.com/in/pvpeuve/)
- [GitHub](https://github.com/pvpeuve)
- [Email](mailto:userandroidsp@gmail.com)

## Pipeline
1. Generar CV unificado en Markdown (scripts/unir_secciones.py)
2. Convertir a PDF (scripts/exportar_md_a_pdf.py)
3. Sincronizar con LinkedIn (scripts/actualizar_linkedin.py)

## Tecnologías utilizadas
- **Markdown** para estructurar contenido modular.
- **Python 3** para automatización de compilado y exportación.
- **Pandoc / PyPandoc** para conversión a PDF.
- **GitHub Actions (pendiente)** para CI/CD y publicación automática.

## Estructura del repositorio
```markdown
CV/
├── datos/              # Secciones del CV (perfil, experiencia, etc.)
├── certificaciones/    # Certificados clasificados por empresa
├── plantillas/         # Plantillas Markdown (ES/EN)
├── scripts/            # Automatización (unión, exportación, sincronización)
├── salidas/            # CV generado (.md y .pdf)
└── README.md           # Este archivo
```

## Cómo generar el CV (pendiente de desarrollo)
1. Clonar el repositorio
  ```bash
  git clone https://github.com/pvpeuve/CV.git
  cd CV
  ```
2. Instalar dependencias
  ```bash
  pip install pypandoc
  ```
3. Generar CV
  ```bash
  python3 scripts/unir_secciones.py
  ```
4. Exportar a PDF
  ```bash
  python3 scripts/exportar_md_a_pdf.py
  ```

## Última versión del CV
[Descargar CV en formato PDF](salidas/CV_ES.pdf)

## Licencia
Este repositorio se distribuye bajo [licencia MIT](LICENSE).
Puedes reutilizar el código de automatización y estructura del CV con atribución.
