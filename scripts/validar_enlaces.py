#!/usr/bin/env python3
"""
Verifica que todos los enlaces relativos dentro de los archivos .md del repositorio
apuntan a archivos que existen en disco.

Uso:
    python scripts/validar_enlaces.py              # todos los .md
    python scripts/validar_enlaces.py --dir tutorial  # solo tutorial/
    python scripts/validar_enlaces.py --verbose    # muestra enlaces válidos también
"""
import re
import sys
import argparse
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parent.parent


def es_enlace_externo(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:", "#", "ftp://"))


def extraer_enlaces(texto: str):
    """Extrae todos los [texto](href) de un Markdown, devuelve lista de href."""
    return re.findall(r'\[(?:[^\]]*)\]\(([^)]+)\)', texto)


def validar_archivo(md_path: Path, verbose: bool = False):
    """Valida todos los enlaces relativos de un .md. Devuelve lista de errores."""
    errores = []
    texto = md_path.read_text(encoding="utf-8")
    enlaces = extraer_enlaces(texto)

    for href in enlaces:
        # Quitar fragmentos (#seccion)
        href_limpio = href.split("#")[0].strip()
        if not href_limpio or es_enlace_externo(href_limpio):
            continue

        destino = (md_path.parent / href_limpio).resolve()
        if destino.exists():
            if verbose:
                print(f"  ✓ {href_limpio}")
        else:
            errores.append((md_path, href_limpio))

    return errores


def main():
    parser = argparse.ArgumentParser(description="Valida enlaces relativos en archivos Markdown")
    parser.add_argument("--dir", default=".", help="Directorio raíz a escanear (relativo a la raíz del repo)")
    parser.add_argument("--verbose", action="store_true", help="Mostrar también los enlaces válidos")
    parser.add_argument("--strict", action="store_true", help="Salir con error si hay avisos")
    args = parser.parse_args()

    scan_dir = ROOT / args.dir
    if not scan_dir.exists():
        print(f"Error: directorio {scan_dir} no existe")
        sys.exit(2)

    EXCLUIR_NOMBRES = {"_plantilla-articulo.md"}
    EXCLUIR_DIRS = {"sin-formulas"}  # copias derivadas; rutas relativas apuntan a originales
    md_files = sorted(
        f for f in scan_dir.rglob("*.md")
        if f.name not in EXCLUIR_NOMBRES
        and not any(d in f.parts for d in EXCLUIR_DIRS)
    )
    print(f"Escaneando {len(md_files)} archivos .md en {scan_dir.relative_to(ROOT)}/")
    print("=" * 60)

    todos_errores = []
    archivos_con_errores = 0

    for md_path in md_files:
        errores = validar_archivo(md_path, verbose=args.verbose)
        if errores:
            archivos_con_errores += 1
            print(f"\n❌ {md_path.relative_to(ROOT)}")
            for _, href in errores:
                print(f"   → Enlace roto: {href}")
            todos_errores.extend(errores)
        elif args.verbose:
            print(f"\n✓ {md_path.relative_to(ROOT)} — todos los enlaces válidos")

    print("\n" + "=" * 60)
    if todos_errores:
        print(f"❌ {len(todos_errores)} enlace(s) roto(s) en {archivos_con_errores} archivo(s)")
        sys.exit(1)
    else:
        print(f"✅ Todos los enlaces relativos son válidos ({len(md_files)} archivos revisados)")
        sys.exit(0)


if __name__ == "__main__":
    main()
