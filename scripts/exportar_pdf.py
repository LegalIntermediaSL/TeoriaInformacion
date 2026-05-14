#!/usr/bin/env python3
"""
Genera un PDF por módulo concatenando todos sus artículos y ejecutando Pandoc.

Requiere: pandoc >= 2.0

Uso:
    python scripts/exportar_pdf.py              # todos los módulos
    python scripts/exportar_pdf.py --modulo 02  # solo módulo 02
    python scripts/exportar_pdf.py --out /tmp   # directorio de salida alternativo
"""
import subprocess
import sys
import argparse
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
TUTORIAL = ROOT / "tutorial"
DEFAULT_OUT = ROOT / "pdf"

MODULES = [
    ("00", "Presentacion",              TUTORIAL / "00-presentacion"),
    ("01", "Fundamentos-matematicos",   TUTORIAL / "01-fundamentos-matematicos"),
    ("02", "Teoria-informacion",        TUTORIAL / "02-teoria-informacion"),
    ("03", "Computabilidad",            TUTORIAL / "03-computabilidad"),
    ("04", "Complejidad-computacional", TUTORIAL / "04-complejidad-computacional"),
    ("05", "Conexiones-y-aplicaciones", TUTORIAL / "05-conexiones-y-aplicaciones"),
]

PANDOC_FLAGS = [
    "--pdf-engine=xelatex",
    "--toc",
    "--toc-depth=2",
    "--number-sections",
    "-V", "lang=es",
    "-V", "geometry:margin=2.5cm",
    "-V", "fontsize=11pt",
    "-V", "linestretch=1.3",
    "-V", "colorlinks=true",
    "-V", "linkcolor=blue",
    "--highlight-style=tango",
    "--standalone",
]


def check_pandoc():
    try:
        result = subprocess.run(["pandoc", "--version"], capture_output=True, text=True)
        version = result.stdout.splitlines()[0]
        print(f"  Usando {version}")
        return True
    except FileNotFoundError:
        print("Error: pandoc no encontrado. Instalar con: brew install pandoc")
        return False


def exportar_modulo(mod_id: str, mod_name: str, mod_dir: Path, out_dir: Path) -> bool:
    articles = sorted(mod_dir.glob("[0-9]*.md")) if mod_dir.exists() else []
    if not articles:
        print(f"  Módulo {mod_id}: sin artículos, omitido.")
        return True

    out_pdf = out_dir / f"modulo-{mod_id}-{mod_name}.pdf"
    print(f"  Módulo {mod_id} ({len(articles)} artículos) → {out_pdf.name}")

    # Preprocess: fix relative image paths (../imagenes/ → absolute)
    combined_parts = []
    for art in articles:
        text = art.read_text(encoding="utf-8")
        text = text.replace("../imagenes/", str(TUTORIAL / "imagenes") + "/")
        combined_parts.append(f"\n\n---\n\n{text}")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", encoding="utf-8",
                                     delete=False) as tmp:
        tmp.write("".join(combined_parts))
        tmp_path = Path(tmp.name)

    cmd = ["pandoc", str(tmp_path), "-o", str(out_pdf)] + PANDOC_FLAGS
    result = subprocess.run(cmd, capture_output=True, text=True)
    tmp_path.unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"    ❌ Error:\n{result.stderr[:400]}")
        return False

    size_kb = out_pdf.stat().st_size // 1024
    print(f"    ✅ {size_kb} KB")
    return True


def main():
    parser = argparse.ArgumentParser(description="Exporta módulos del tutorial a PDF via Pandoc")
    parser.add_argument("--modulo", metavar="ID", help="Exportar solo este módulo (ej: 02)")
    parser.add_argument("--out", default=str(DEFAULT_OUT), metavar="DIR",
                        help=f"Directorio de salida (default: {DEFAULT_OUT.relative_to(ROOT)})")
    args = parser.parse_args()

    if not check_pandoc():
        sys.exit(1)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    modules = MODULES
    if args.modulo:
        modules = [(mid, name, d) for mid, name, d in MODULES if mid == args.modulo]
        if not modules:
            print(f"Error: módulo '{args.modulo}' no reconocido. Válidos: 00-05")
            sys.exit(1)

    print(f"Exportando {len(modules)} módulo(s) → {out_dir.relative_to(ROOT)}/")
    print("=" * 60)

    ok = all(exportar_modulo(mid, name, d, out_dir) for mid, name, d in modules)

    print("=" * 60)
    if ok:
        pdfs = list(out_dir.glob("*.pdf"))
        total_mb = sum(p.stat().st_size for p in pdfs) / 1e6
        print(f"✅ {len(pdfs)} PDF(s) generado(s) — {total_mb:.1f} MB total")
    else:
        print("⚠️  Algunos módulos fallaron (ver errores arriba)")
        sys.exit(1)


if __name__ == "__main__":
    main()
