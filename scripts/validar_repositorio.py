#!/usr/bin/env python3
"""
Valida la coherencia del repositorio:
- Todos los artículos listados en READMEs existen en disco.
- Todos los archivos .md en módulos están listados en su README.
- Todos los notebooks referenciados existen.
- Los ejercicios resueltos listados en su README existen.
- Todos los artículos tienen las secciones obligatorias.
- Los ejercicios propuestos no tienen enlaces rotos.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
TUTORIAL = ROOT / "tutorial"

MODULES = {
    "00": TUTORIAL / "00-presentacion",
    "01": TUTORIAL / "01-fundamentos-matematicos",
    "02": TUTORIAL / "02-teoria-informacion",
    "03": TUTORIAL / "03-computabilidad",
    "04": TUTORIAL / "04-complejidad-computacional",
    "05": TUTORIAL / "05-conexiones-y-aplicaciones",
}

errors = []
warnings = []


def check(condition, msg, level="error"):
    if not condition:
        (errors if level == "error" else warnings).append(msg)


def extract_md_links(text):
    """Extrae todos los enlaces .md de un texto Markdown."""
    return re.findall(r'\[.*?\]\((.*?\.md)\)', text)


def extract_ipynb_links(text):
    return re.findall(r'\[.*?\]\((.*?\.ipynb)\)', text)


# --- 1. Validar módulos ---
for mod_id, mod_dir in MODULES.items():
    readme = mod_dir / "README.md"
    if not readme.exists():
        errors.append(f"Falta README: {readme.relative_to(ROOT)}")
        continue

    readme_text = readme.read_text(encoding="utf-8")

    # Artículos en disco
    articles_on_disk = sorted(mod_dir.glob("[0-9]*.md"))
    for art in articles_on_disk:
        check(
            art.name in readme_text,
            f"Artículo no listado en README: {art.relative_to(ROOT)}",
            "warning"
        )

    # Artículos mencionados en README
    for link in extract_md_links(readme_text):
        link_path = mod_dir / link
        check(
            link_path.exists(),
            f"Enlace roto en {readme.relative_to(ROOT)}: {link}"
        )


# --- 2. Validar README principal del tutorial ---
main_readme = TUTORIAL / "README.md"
if main_readme.exists():
    main_text = main_readme.read_text(encoding="utf-8")
    for link in extract_md_links(main_text):
        link_path = TUTORIAL / link
        check(
            link_path.exists(),
            f"Enlace roto en tutorial/README.md: {link}"
        )


# --- 3. Validar notebooks ---
for nb_dir in [TUTORIAL / "cuadernos" / "ejemplos", TUTORIAL / "cuadernos" / "ejercicios"]:
    if not nb_dir.exists():
        warnings.append(f"Directorio no existe: {nb_dir.relative_to(ROOT)}")
        continue

    readme = nb_dir / "README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        for nb_file in nb_dir.glob("*.ipynb"):
            check(
                nb_file.name in readme_text,
                f"Notebook no listado en README: {nb_file.relative_to(ROOT)}",
                "warning"
            )

    # Verificar que cada notebook tiene metadata mínima
    import json
    for nb_file in nb_dir.glob("*.ipynb"):
        try:
            nb = json.loads(nb_file.read_text(encoding="utf-8"))
            check("cells" in nb, f"Notebook inválido (sin cells): {nb_file.relative_to(ROOT)}")
        except json.JSONDecodeError as e:
            errors.append(f"Notebook con JSON inválido: {nb_file.relative_to(ROOT)}: {e}")


# --- 4. Validar ejercicios resueltos ---
resueltos_dir = TUTORIAL / "ejercicios" / "resueltos"
resueltos_readme = resueltos_dir / "README.md"
if resueltos_readme.exists():
    readme_text = resueltos_readme.read_text(encoding="utf-8")
    for md_file in resueltos_dir.glob("[0-9]*.md"):
        check(
            md_file.name in readme_text,
            f"Resuelto no listado en README: {md_file.relative_to(ROOT)}",
            "warning"
        )
    for link in extract_md_links(readme_text):
        link_path = resueltos_dir / link
        check(
            link_path.exists(),
            f"Enlace roto en resueltos/README.md: {link}"
        )


# --- 5. Validar referencias cruzadas en artículos ---
for mod_dir in MODULES.values():
    for art in mod_dir.glob("[0-9]*.md"):
        text = art.read_text(encoding="utf-8")
        for link in extract_md_links(text):
            if link.startswith("http") or link.startswith("#"):
                continue
            link_path = art.parent / link
            check(
                link_path.exists(),
                f"Enlace roto en {art.relative_to(ROOT)}: {link}"
            )


# --- 6. Validar secciones obligatorias en artículos ---
SECCIONES_OBLIGATORIAS = ["## Ideas clave", "## Ejercicios"]
SECCIONES_RECOMENDADAS = ["## Prerrequisitos", "## Objetivos", "## Véase también"]

for mod_dir in MODULES.values():
    for art in mod_dir.glob("[0-9]*.md"):
        text = art.read_text(encoding="utf-8")
        for seccion in SECCIONES_OBLIGATORIAS:
            check(
                seccion in text,
                f"Artículo sin sección obligatoria '{seccion}': {art.relative_to(ROOT)}"
            )
        for seccion in SECCIONES_RECOMENDADAS:
            check(
                seccion in text,
                f"Artículo sin sección recomendada '{seccion}': {art.relative_to(ROOT)}",
                "warning"
            )


# --- 7. Validar ejercicios propuestos ---
propuestos_dir = TUTORIAL / "ejercicios" / "propuestos"
propuestos_readme = propuestos_dir / "README.md"
if propuestos_readme.exists():
    readme_text = propuestos_readme.read_text(encoding="utf-8")
    for link in extract_md_links(readme_text):
        link_path = propuestos_dir / link
        check(
            link_path.exists(),
            f"Enlace roto en propuestos/README.md: {link}"
        )


# --- Reporte ---
print("=" * 60)
print("VALIDACIÓN DEL REPOSITORIO")
print("=" * 60)

if errors:
    print(f"\n❌ ERRORES ({len(errors)}):")
    for e in errors:
        print(f"   • {e}")
else:
    print("\n✅ Sin errores.")

if warnings:
    print(f"\n⚠️  AVISOS ({len(warnings)}):")
    for w in warnings:
        print(f"   • {w}")
else:
    print("✅ Sin avisos.")

print(f"\nResumen: {len(errors)} errores, {len(warnings)} avisos.")

sys.exit(1 if errors else 0)
