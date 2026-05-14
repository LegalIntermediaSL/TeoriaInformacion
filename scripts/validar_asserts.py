#!/usr/bin/env python3
"""
Verifica que cada notebook de ejercicios tiene al menos una celda con 'assert'.

Uso:
    python scripts/validar_asserts.py            # informe en consola
    python scripts/validar_asserts.py --strict   # salir con error si faltan asserts
"""
import json
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
EJERCICIOS_DIR = ROOT / "tutorial" / "cuadernos" / "ejercicios"


def tiene_assert(nb_path: Path) -> bool:
    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        return any(
            "assert" in "".join(cell.get("source", []))
            for cell in nb.get("cells", [])
            if cell.get("cell_type") == "code"
        )
    except Exception:
        return False


def contar_asserts(nb_path: Path) -> int:
    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        return sum(
            "".join(cell.get("source", [])).count("assert")
            for cell in nb.get("cells", [])
            if cell.get("cell_type") == "code"
        )
    except Exception:
        return 0


def main():
    parser = argparse.ArgumentParser(description="Valida asserts en notebooks de ejercicios")
    parser.add_argument("--strict", action="store_true", help="Salir con código 1 si hay notebooks sin assert")
    parser.add_argument("--verbose", action="store_true", help="Mostrar recuento de asserts por notebook")
    args = parser.parse_args()

    if not EJERCICIOS_DIR.exists():
        print(f"Error: directorio {EJERCICIOS_DIR.relative_to(ROOT)} no encontrado")
        sys.exit(2)

    notebooks = sorted(EJERCICIOS_DIR.glob("*.ipynb"))
    if not notebooks:
        print("No se encontraron notebooks en", EJERCICIOS_DIR.relative_to(ROOT))
        sys.exit(0)

    sin_assert = []
    total_asserts = 0

    print(f"Verificando {len(notebooks)} notebooks de ejercicios...")
    print("=" * 60)

    for nb in notebooks:
        n = contar_asserts(nb)
        total_asserts += n
        tiene = n > 0
        if not tiene:
            sin_assert.append(nb)
        if args.verbose or not tiene:
            estado = f"✅ {n} assert(s)" if tiene else "❌ sin assert"
            print(f"  {estado:22}  {nb.name}")

    print("=" * 60)
    print(f"Notebooks totales:    {len(notebooks)}")
    print(f"Con assert:           {len(notebooks) - len(sin_assert)}")
    print(f"Sin assert:           {len(sin_assert)}")
    print(f"Total asserts:        {total_asserts}")
    cobertura = (len(notebooks) - len(sin_assert)) / len(notebooks) * 100
    print(f"Cobertura:            {cobertura:.0f}%")

    if sin_assert:
        print("\nNotebooks sin assert:")
        for nb in sin_assert:
            print(f"  {nb.name}")
        if args.strict:
            sys.exit(1)
    else:
        print("\n✅ Todos los notebooks tienen al menos un assert.")


if __name__ == "__main__":
    main()
