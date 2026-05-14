#!/usr/bin/env python3
"""
Genera el mapa de dependencias entre artículos del tutorial.

Lee la sección ## Prerrequisitos de cada artículo y construye un grafo dirigido
(artículo → prerrequisito). Produce:
  - tutorial/imagenes/mapa-dependencias.svg   (SVG embebible en GitHub)
  - tutorial/imagenes/mapa-dependencias.dot   (formato Graphviz para procesado externo)

Uso:
    python scripts/generar_mapa_dependencias.py
    python scripts/generar_mapa_dependencias.py --dot-only   # solo DOT
"""
import re
import sys
import argparse
import html
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
TUTORIAL = ROOT / "tutorial"
OUT_SVG = TUTORIAL / "imagenes" / "mapa-dependencias.svg"
OUT_DOT = TUTORIAL / "imagenes" / "mapa-dependencias.dot"

MODULES = [
    ("00", "Presentación",              TUTORIAL / "00-presentacion",              "#94a3b8"),
    ("01", "Fundamentos",               TUTORIAL / "01-fundamentos-matematicos",    "#60a5fa"),
    ("02", "Teoría info.",              TUTORIAL / "02-teoria-informacion",         "#34d399"),
    ("03", "Computabilidad",            TUTORIAL / "03-computabilidad",             "#f59e0b"),
    ("04", "Complejidad",               TUTORIAL / "04-complejidad-computacional",  "#f87171"),
    ("05", "Conexiones",                TUTORIAL / "05-conexiones-y-aplicaciones",  "#a78bfa"),
]

# Layout constants
COL_W   = 200   # column width (px)
COL_PAD = 30    # horizontal padding between columns
ROW_H   = 38    # row height per article
ROW_PAD = 8     # vertical padding between articles
NODE_W  = 184   # node box width
NODE_H  = 28    # node box height
TOP_PAD = 60    # space for column headers
LEFT_PAD = 20


def short_name(path: Path) -> str:
    """Strip leading number and extension, truncate if too long."""
    stem = path.stem
    parts = stem.split("-", 1)
    name = parts[1].replace("-", " ") if len(parts) > 1 else stem
    return name[:28] + "…" if len(name) > 28 else name


def extract_prereqs(art: Path) -> list[Path]:
    try:
        text = art.read_text(encoding="utf-8")
    except Exception:
        return []
    m = re.search(r'## Prerrequisitos\n(.*?)(?=\n##|\Z)', text, re.DOTALL)
    if not m:
        return []
    result = []
    for href in re.findall(r'\[(?:[^\]]*)\]\(([^)]+)\)', m.group(1)):
        href_clean = href.split("#")[0].strip()
        if href_clean and not href_clean.startswith("http"):
            target = (art.parent / href_clean).resolve()
            if target.exists():
                result.append(target)
    return result


def build_graph():
    articles = {}   # path -> (col_idx, row_idx, mod_id, color)
    prereqs = {}    # path -> [path]
    col_articles = defaultdict(list)

    for col_idx, (mod_id, _, mod_dir, color) in enumerate(MODULES):
        arts = sorted(mod_dir.glob("[0-9]*.md")) if mod_dir.exists() else []
        for row_idx, art in enumerate(arts):
            articles[art] = (col_idx, row_idx, mod_id, color)
            col_articles[col_idx].append(art)
        for art in arts:
            prereqs[art] = extract_prereqs(art)

    return articles, prereqs, col_articles


def node_pos(col_idx: int, row_idx: int) -> tuple[float, float]:
    x = LEFT_PAD + col_idx * (COL_W + COL_PAD)
    y = TOP_PAD + row_idx * (ROW_H + ROW_PAD)
    return x, y


def node_center(col_idx: int, row_idx: int) -> tuple[float, float]:
    x, y = node_pos(col_idx, row_idx)
    return x + NODE_W / 2, y + NODE_H / 2


def generate_svg(articles, prereqs, col_articles) -> str:
    max_rows = max((len(v) for v in col_articles.values()), default=1)
    total_w = LEFT_PAD * 2 + len(MODULES) * COL_W + (len(MODULES) - 1) * COL_PAD
    total_h = TOP_PAD + max_rows * (ROW_H + ROW_PAD) + 20

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" '
        f'width="{total_w}" height="{total_h}" font-family="ui-monospace,monospace" font-size="11">',
        # Background
        f'<rect width="{total_w}" height="{total_h}" fill="#0f172a"/>',
        # Arrow marker
        '<defs>',
        '  <marker id="arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">',
        '    <path d="M0,0 L8,3 L0,6 Z" fill="#64748b"/>',
        '  </marker>',
        '</defs>',
    ]

    # Column headers
    for col_idx, (mod_id, mod_name, _, color) in enumerate(MODULES):
        x = LEFT_PAD + col_idx * (COL_W + COL_PAD)
        cx = x + NODE_W / 2
        lines.append(f'<text x="{cx}" y="22" text-anchor="middle" fill="{color}" '
                      f'font-weight="bold" font-size="13">{html.escape(mod_id)} — {html.escape(mod_name)}</text>')
        # Column separator line
        if col_idx > 0:
            sep_x = x - COL_PAD / 2
            lines.append(f'<line x1="{sep_x}" y1="30" x2="{sep_x}" y2="{total_h - 10}" '
                          f'stroke="#1e293b" stroke-width="1"/>')

    # Edges (drawn first, under nodes)
    for art, deps in prereqs.items():
        if art not in articles:
            continue
        col1, row1, _, _ = articles[art]
        cx1, cy1 = node_center(col1, row1)
        for dep in deps:
            if dep not in articles:
                continue
            col2, row2, _, _ = articles[dep]
            cx2, cy2 = node_center(col2, row2)
            # Control points for a bezier curve
            mid_x = (cx1 + cx2) / 2
            # Shorten endpoint to not overlap node
            dx = cx2 - cx1
            dy = cy2 - cy1
            length = (dx**2 + dy**2) ** 0.5
            if length < 1:
                continue
            shrink = NODE_W / 2 + 4
            ex = cx2 - dx / length * shrink
            ey = cy2 - dy / length * shrink
            lines.append(
                f'<path d="M{cx1:.1f},{cy1:.1f} C{mid_x:.1f},{cy1:.1f} {mid_x:.1f},{ey:.1f} '
                f'{ex:.1f},{ey:.1f}" fill="none" stroke="#64748b" stroke-width="1.2" '
                f'marker-end="url(#arr)"/>'
            )

    # Nodes
    for art, (col_idx, row_idx, mod_id, color) in articles.items():
        x, y = node_pos(col_idx, row_idx)
        name = short_name(art)
        num = art.stem.split("-")[0]
        # Lighten color for node fill
        lines.append(
            f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="4" ry="4" '
            f'fill="{color}22" stroke="{color}" stroke-width="1.2"/>'
        )
        lines.append(
            f'<text x="{x + 6}" y="{y + 11}" fill="{color}" font-size="9" opacity="0.7">'
            f'{html.escape(mod_id)}/{html.escape(num)}</text>'
        )
        lines.append(
            f'<text x="{x + 6}" y="{y + 21}" fill="#e2e8f0" font-size="10">'
            f'{html.escape(name)}</text>'
        )

    lines.append('</svg>')
    return "\n".join(lines)


def generate_dot(articles, prereqs) -> str:
    lines = [
        'digraph dependencias {',
        '  rankdir=LR;',
        '  node [shape=box style=filled fontname="Helvetica" fontsize=10 margin="0.1,0.05"];',
        '  edge [color="#888888" arrowsize=0.7];',
        '',
    ]
    colors = {mod_id: color for mod_id, _, _, color in MODULES}

    # Subgraphs per module
    for col_idx, (mod_id, mod_name, _, color) in enumerate(MODULES):
        lines.append(f'  subgraph cluster_{mod_id} {{')
        lines.append(f'    label="{mod_id} — {mod_name}";')
        lines.append(f'    color="{color}";')
        lines.append(f'    fontcolor="{color}";')
        for art, (c, r, mid, clr) in articles.items():
            if mid == mod_id:
                node_id = art.stem.replace("-", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                label = short_name(art)
                lines.append(f'    {node_id} [label="{label}" fillcolor="{color}44"];')
        lines.append('  }')
        lines.append('')

    # Edges
    for art, deps in prereqs.items():
        if art not in articles:
            continue
        src_id = art.stem.replace("-", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        for dep in deps:
            if dep not in articles:
                continue
            dst_id = dep.stem.replace("-", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            lines.append(f'  {src_id} -> {dst_id};')

    lines.append('}')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Genera mapa de dependencias entre artículos")
    parser.add_argument("--dot-only", action="store_true", help="Generar solo el fichero DOT (sin SVG)")
    args = parser.parse_args()

    print("Analizando prerrequisitos de los artículos...")
    articles, prereqs, col_articles = build_graph()

    total_arts = len(articles)
    total_edges = sum(len(v) for v in prereqs.values())
    print(f"  Artículos: {total_arts}")
    print(f"  Dependencias: {total_edges}")

    OUT_SVG.parent.mkdir(parents=True, exist_ok=True)

    # DOT
    dot = generate_dot(articles, prereqs)
    OUT_DOT.write_text(dot, encoding="utf-8")
    print(f"  DOT → {OUT_DOT.relative_to(ROOT)}")

    if not args.dot_only:
        svg = generate_svg(articles, prereqs, col_articles)
        OUT_SVG.write_text(svg, encoding="utf-8")
        print(f"  SVG → {OUT_SVG.relative_to(ROOT)}")

    print("Listo.")


if __name__ == "__main__":
    main()
