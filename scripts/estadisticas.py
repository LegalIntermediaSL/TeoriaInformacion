#!/usr/bin/env python3
"""
Muestra estadísticas del tutorial: artículos, notebooks y ejercicios por módulo.
Incluye métricas de cobertura: % con ejercicio resuelto, % de notebooks con assert,
y artículos sin entrada en por-articulo.md.

Uso:
    python scripts/estadisticas.py           # informe en consola
    python scripts/estadisticas.py --md      # además genera ESTADISTICAS.md
"""
import json
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
TUTORIAL = ROOT / "tutorial"

MODULES = [
    ("00", "Presentación",              TUTORIAL / "00-presentacion"),
    ("01", "Fundamentos matemáticos",   TUTORIAL / "01-fundamentos-matematicos"),
    ("02", "Teoría de la información",  TUTORIAL / "02-teoria-informacion"),
    ("03", "Computabilidad",            TUTORIAL / "03-computabilidad"),
    ("04", "Complejidad computacional", TUTORIAL / "04-complejidad-computacional"),
    ("05", "Conexiones y aplicaciones", TUTORIAL / "05-conexiones-y-aplicaciones"),
]

NOTEBOOKS_EJEMPLOS  = TUTORIAL / "cuadernos" / "ejemplos"
NOTEBOOKS_EJERCICIOS = TUTORIAL / "cuadernos" / "ejercicios"
RESUELTOS = TUTORIAL / "ejercicios" / "resueltos"
PROPUESTOS = TUTORIAL / "ejercicios" / "propuestos"


def count_files(directory, pattern):
    if not directory.exists():
        return 0
    return len(list(directory.glob(pattern)))


def notebook_cell_count(nb_path):
    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        return len(nb.get("cells", []))
    except Exception:
        return 0


def article_word_count(art_path):
    try:
        return len(art_path.read_text(encoding="utf-8").split())
    except Exception:
        return 0


parser = argparse.ArgumentParser(description="Estadísticas del tutorial")
parser.add_argument("--md", action="store_true", help="Generar también ESTADISTICAS.md")
args = parser.parse_args()

output_lines = []  # para generar el .md opcional


def pr(*a, **kw):
    line = " ".join(str(x) for x in a)
    output_lines.append(line)
    print(line, **kw)


pr("=" * 70)
pr("ESTADÍSTICAS DEL TUTORIAL DE TEORÍA DE LA INFORMACIÓN")
pr("=" * 70)
pr()

# --- Artículos por módulo ---
total_articles = 0
pr(f"{'Módulo':<45} {'Arts':<6} {'Palabras (aprox)'}")
pr("-" * 65)
all_articles = []
for mod_id, mod_name, mod_dir in MODULES:
    articles = sorted(mod_dir.glob("[0-9]*.md")) if mod_dir.exists() else []
    words = sum(article_word_count(a) for a in articles)
    total_articles += len(articles)
    all_articles.extend(articles)
    pr(f"  {mod_id} — {mod_name:<40} {len(articles):<6} {words:>8,}")

pr(f"{'TOTAL':<45} {total_articles:<6}")
pr()

# --- Notebooks ---
nb_ej = sorted(NOTEBOOKS_EJERCICIOS.glob("*.ipynb")) if NOTEBOOKS_EJERCICIOS.exists() else []
nb_ex = sorted(NOTEBOOKS_EJEMPLOS.glob("*.ipynb"))   if NOTEBOOKS_EJEMPLOS.exists() else []

pr(f"Notebooks de ejemplo:   {len(nb_ex):>3}")
pr(f"Notebooks de ejercicio: {len(nb_ej):>3}")
pr(f"Total notebooks:        {len(nb_ex) + len(nb_ej):>3}")
pr()

# --- Ejercicios ---
resueltos = list(RESUELTOS.glob("[0-9]*.md")) if RESUELTOS.exists() else []
propuestos = list(PROPUESTOS.glob("*.md"))    if PROPUESTOS.exists() else []

pr(f"Ejercicios resueltos:   {len(resueltos):>3}")
pr(f"Ejercicios propuestos:  {len(propuestos):>3}")
pr()

# --- Cobertura: artículos con y sin notebook asociado ---
pr("Cobertura de notebooks por módulo:")
pr()
pr(f"{'Módulo':<45} {'Con NB':<8} {'Sin NB'}")
pr("-" * 60)
all_nb_numbers = set()
for nb in nb_ej + nb_ex:
    parts = nb.stem.split("-")
    if parts[0].isdigit():
        all_nb_numbers.add(int(parts[0]))

for mod_id, mod_name, mod_dir in MODULES:
    articles = sorted(mod_dir.glob("[0-9]*.md")) if mod_dir.exists() else []
    with_nb = sum(1 for a in articles if any(
        str(i) in a.stem for i in all_nb_numbers
    ))
    without_nb = len(articles) - with_nb
    pr(f"  {mod_id} — {mod_name:<40} {with_nb:<8} {without_nb}")

pr()

# --- NUEVA MÉTRICA: % de artículos con ejercicio resuelto ---
resueltos_nombres = {r.stem for r in resueltos}
# Extraer prefixos de artículos del nombre del resuelto (e.g. "13-complejidad-aleatoria")
resueltos_keywords = set()
for r in resueltos:
    parts = r.stem.split("-")
    if len(parts) >= 2:
        resueltos_keywords.add("-".join(parts[1:]))  # quitar el número

arts_con_resuelto = []
arts_sin_resuelto = []
for art in all_articles:
    art_key = "-".join(art.stem.split("-")[1:])
    tiene = any(rk in art_key or art_key in rk for rk in resueltos_keywords)
    if tiene:
        arts_con_resuelto.append(art)
    else:
        arts_sin_resuelto.append(art)

pct_resueltos = len(arts_con_resuelto) / total_articles * 100 if total_articles else 0
pr(f"Cobertura ejercicios resueltos: {len(arts_con_resuelto)}/{total_articles} artículos ({pct_resueltos:.0f}%)")
pr()

# --- NUEVA MÉTRICA: % de notebooks de ejercicio con assert ---
def tiene_assert(nb_path):
    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        return any("assert" in "".join(c.get("source", [])) for c in nb.get("cells", []))
    except Exception:
        return False

nb_con_assert = [nb for nb in nb_ej if tiene_assert(nb)]
nb_sin_assert = [nb for nb in nb_ej if not tiene_assert(nb)]
pct_assert = len(nb_con_assert) / len(nb_ej) * 100 if nb_ej else 0
pr(f"Notebooks de ejercicio con assert: {len(nb_con_assert)}/{len(nb_ej)} ({pct_assert:.0f}%)")
if nb_sin_assert:
    pr(f"  Sin assert: {', '.join(nb.name for nb in nb_sin_assert)}")
pr()

# --- NUEVA MÉTRICA: artículos sin entrada en por-articulo.md ---
por_art_path = TUTORIAL / "referencias" / "por-articulo.md"
arts_sin_referencia = []
if por_art_path.exists():
    por_art_text = por_art_path.read_text(encoding="utf-8")
    for art in all_articles:
        # Buscar el nombre del archivo sin extensión en el texto de por-articulo.md
        if art.stem not in por_art_text and art.name not in por_art_text:
            arts_sin_referencia.append(art)
    pr(f"Artículos sin entrada en por-articulo.md: {len(arts_sin_referencia)}/{total_articles}")
    for a in arts_sin_referencia[:10]:
        pr(f"  {a.relative_to(ROOT)}")
    if len(arts_sin_referencia) > 10:
        pr(f"  ... y {len(arts_sin_referencia)-10} más")
    pr()

# --- Resumen global ---
total_nb = len(nb_ex) + len(nb_ej)
total_resueltos = len(resueltos)
pr("=" * 70)
pr(f"  Total artículos:                {total_articles:>3}")
pr(f"  Total notebooks:                {total_nb:>3}")
pr(f"  Total resueltos:                {total_resueltos:>3}")
pr(f"  Ratio NB/artículo:              {total_nb/total_articles:.2f}")
pr(f"  Ratio res./artículo:            {total_resueltos/total_articles:.2f}")
pr(f"  Cobertura resueltos:            {pct_resueltos:.0f}%")
pr(f"  Notebooks de ejercicio c/assert:{pct_assert:.0f}%")
pr("=" * 70)

# --- Salida Markdown opcional ---
if args.md:
    md_path = ROOT / "ESTADISTICAS.md"
    md_content = "# Estadísticas del tutorial\n\n"
    md_content += "Generado automáticamente por `scripts/estadisticas.py`.\n\n"
    md_content += "```\n" + "\n".join(output_lines) + "\n```\n"
    md_path.write_text(md_content, encoding="utf-8")
    print(f"\nInforme guardado en {md_path.relative_to(ROOT)}")
