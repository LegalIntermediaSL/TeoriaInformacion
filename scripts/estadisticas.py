#!/usr/bin/env python3
"""
Muestra estadísticas del tutorial: artículos, notebooks y ejercicios por módulo.
Útil para ver la cobertura pedagógica.
"""
import json
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


print("=" * 70)
print("ESTADÍSTICAS DEL TUTORIAL DE TEORÍA DE LA INFORMACIÓN")
print("=" * 70)
print()

# --- Artículos por módulo ---
total_articles = 0
print(f"{'Módulo':<45} {'Arts':<6} {'Palabras (aprox)'}")
print("-" * 65)
for mod_id, mod_name, mod_dir in MODULES:
    articles = sorted(mod_dir.glob("[0-9]*.md")) if mod_dir.exists() else []
    words = sum(article_word_count(a) for a in articles)
    total_articles += len(articles)
    print(f"  {mod_id} — {mod_name:<40} {len(articles):<6} {words:>8,}")

print(f"{'TOTAL':<45} {total_articles:<6}")
print()

# --- Notebooks ---
nb_ej = sorted(NOTEBOOKS_EJERCICIOS.glob("*.ipynb")) if NOTEBOOKS_EJERCICIOS.exists() else []
nb_ex = sorted(NOTEBOOKS_EJEMPLOS.glob("*.ipynb"))   if NOTEBOOKS_EJEMPLOS.exists() else []

print(f"Notebooks de ejemplo:   {len(nb_ex):>3}")
print(f"Notebooks de ejercicio: {len(nb_ej):>3}")
print(f"Total notebooks:        {len(nb_ex) + len(nb_ej):>3}")
print()

# --- Ejercicios ---
resueltos = list(RESUELTOS.glob("[0-9]*.md")) if RESUELTOS.exists() else []
propuestos = list(PROPUESTOS.glob("*.md"))    if PROPUESTOS.exists() else []

print(f"Ejercicios resueltos:   {len(resueltos):>3}")
print(f"Ejercicios propuestos:  {len(propuestos):>3}")
print()

# --- Cobertura: artículos con y sin notebook asociado ---
print("Cobertura de notebooks por módulo:")
print(f"  (artículo tiene notebook si existe un .ipynb con número relacionado)")
print()
print(f"{'Módulo':<45} {'Con NB':<8} {'Sin NB'}")
print("-" * 60)
all_nb_numbers = set()
for nb in nb_ej + nb_ex:
    # Extraer prefijo numérico del nombre
    parts = nb.stem.split("-")
    if parts[0].isdigit():
        all_nb_numbers.add(int(parts[0]))

for mod_id, mod_name, mod_dir in MODULES:
    articles = sorted(mod_dir.glob("[0-9]*.md")) if mod_dir.exists() else []
    with_nb = sum(1 for a in articles if any(
        str(i) in a.stem for i in all_nb_numbers
    ))
    without_nb = len(articles) - with_nb
    print(f"  {mod_id} — {mod_name:<40} {with_nb:<8} {without_nb}")

print()

# --- Resumen global ---
total_nb = len(nb_ex) + len(nb_ej)
total_resueltos = len(resueltos)
print("=" * 70)
print(f"  Total artículos:      {total_articles:>3}")
print(f"  Total notebooks:      {total_nb:>3}")
print(f"  Total resueltos:      {total_resueltos:>3}")
print(f"  Ratio NB/artículo:    {total_nb/total_articles:.2f}")
print(f"  Ratio res./artículo:  {total_resueltos/total_articles:.2f}")
print("=" * 70)
