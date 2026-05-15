#!/usr/bin/env python3
"""
Añade/actualiza bloques de navegación (anterior / siguiente) en todos los artículos.

Uso:
    python scripts/generar_navegacion.py          # aplica a todos los artículos
    python scripts/generar_navegacion.py --dry-run # muestra cambios sin escribir

El bloque se inserta antes de ## Referencias (o al final si no existe).
Delimitado por <!-- nav-start --> / <!-- nav-end --> para ser idempotente.
"""
import os
import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
TUTORIAL = ROOT / "tutorial"

MODULES_ORDER = ["00", "01", "02", "03", "04", "05"]
MODULES = {
    "00": TUTORIAL / "00-presentacion",
    "01": TUTORIAL / "01-fundamentos-matematicos",
    "02": TUTORIAL / "02-teoria-informacion",
    "03": TUTORIAL / "03-computabilidad",
    "04": TUTORIAL / "04-complejidad-computacional",
    "05": TUTORIAL / "05-conexiones-y-aplicaciones",
}

NAV_START = "<!-- nav-start -->"
NAV_END = "<!-- nav-end -->"


def get_title(path: Path) -> str:
    """Extrae el título H1 del artículo."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    return m.group(1).strip() if m else path.stem


def build_article_sequence() -> list[Path]:
    """Devuelve todos los artículos en orden módulo→nombre."""
    seq = []
    for mod_id in MODULES_ORDER:
        mod_dir = MODULES[mod_id]
        if not mod_dir.exists():
            continue
        articles = sorted(mod_dir.glob("[0-9]*.md"))
        seq.extend(articles)
    return seq


def make_nav_block(prev_path: Path | None, next_path: Path | None,
                   current: Path) -> str:
    """Genera el bloque Markdown de navegación."""
    lines = [NAV_START, ""]
    lines.append("---")
    parts = []
    if prev_path:
        rel = os.path.relpath(prev_path, current.parent)
        title = get_title(prev_path)
        parts.append(f"← [{title}]({rel})")
    else:
        parts.append("←")
    if next_path:
        rel = os.path.relpath(next_path, current.parent)
        title = get_title(next_path)
        parts.append(f"[{title}]({rel}) →")
    else:
        parts.append("→")
    lines.append(" · ".join(parts))
    lines.append("")
    lines.append(NAV_END)
    return "\n".join(lines)


def update_article(path: Path, prev_path: Path | None, next_path: Path | None,
                   dry_run: bool = False) -> bool:
    """Inserta o reemplaza el bloque de navegación. Devuelve True si hubo cambio."""
    text = path.read_text(encoding="utf-8")
    nav_block = make_nav_block(prev_path, next_path, path)

    # Eliminar bloque existente si lo hay
    pattern = re.compile(
        r'\n?' + re.escape(NAV_START) + r'.*?' + re.escape(NAV_END) + r'\n?',
        re.DOTALL
    )
    text_clean = pattern.sub("", text)

    # Insertar antes de ## Referencias, o al final
    ref_match = re.search(r'\n## Referencias\b', text_clean)
    if ref_match:
        insert_at = ref_match.start()
        new_text = text_clean[:insert_at] + "\n\n" + nav_block + text_clean[insert_at:]
    else:
        new_text = text_clean.rstrip() + "\n\n" + nav_block + "\n"

    if new_text == text:
        return False

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="Mostrar qué cambiaría sin escribir nada")
    args = parser.parse_args()

    articles = build_article_sequence()
    n = len(articles)
    print(f"{'[DRY-RUN] ' if args.dry_run else ''}Procesando {n} artículos...")

    changed = 0
    for i, art in enumerate(articles):
        prev_art = articles[i - 1] if i > 0 else None
        next_art = articles[i + 1] if i < n - 1 else None
        if update_article(art, prev_art, next_art, dry_run=args.dry_run):
            changed += 1
            print(f"  {'(draft) ' if args.dry_run else ''}✓ {art.relative_to(ROOT)}")

    print(f"\n{'Habría modificado' if args.dry_run else 'Modificados'}: {changed}/{n} artículos.")


if __name__ == "__main__":
    main()
