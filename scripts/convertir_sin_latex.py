#!/usr/bin/env python3
"""
Genera versiones sin LaTeX de los artículos más matemáticos del tutorial.

Las fórmulas se convierten a Unicode y texto plano legible en entornos
sin renderizado de fórmulas (GitHub mobile, lectores RSS, terminales).

Estrategia:
  - Letras griegas → equivalentes Unicode (α β γ …)
  - Operadores → símbolos Unicode (≤ ≥ ∈ ∑ …)
  - \frac{a}{b} → a/b
  - \mathbb{X} → ℝ ℕ ℤ etc.
  - Bloques display $$…$$ → bloque de código indentado con etiqueta
  - Inline $…$ → backticks cuando el contenido es compacto, texto plano si no

Uso:
    python scripts/convertir_sin_latex.py              # los 15 más matemáticos
    python scripts/convertir_sin_latex.py --todos      # todos los artículos
    python scripts/convertir_sin_latex.py --articulo tutorial/02-teoria-informacion/08-teorema-de-shannon-capacidad.md
    python scripts/convertir_sin_latex.py --out /tmp/sin-latex  # directorio alternativo
"""
import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
TUTORIAL = ROOT / "tutorial"
DEFAULT_OUT = TUTORIAL / "sin-formulas"

# ── Replacements ──────────────────────────────────────────────────────────────

GREEK = {
    r'\alpha': 'α', r'\beta': 'β', r'\gamma': 'γ', r'\delta': 'δ',
    r'\epsilon': 'ε', r'\varepsilon': 'ε', r'\zeta': 'ζ', r'\eta': 'η',
    r'\theta': 'θ', r'\vartheta': 'θ', r'\iota': 'ι', r'\kappa': 'κ',
    r'\lambda': 'λ', r'\mu': 'μ', r'\nu': 'ν', r'\xi': 'ξ',
    r'\pi': 'π', r'\varpi': 'π', r'\rho': 'ρ', r'\varrho': 'ρ',
    r'\sigma': 'σ', r'\varsigma': 'ς', r'\tau': 'τ', r'\upsilon': 'υ',
    r'\phi': 'φ', r'\varphi': 'φ', r'\chi': 'χ', r'\psi': 'ψ', r'\omega': 'ω',
    r'\Gamma': 'Γ', r'\Delta': 'Δ', r'\Theta': 'Θ', r'\Lambda': 'Λ',
    r'\Xi': 'Ξ', r'\Pi': 'Π', r'\Sigma': 'Σ', r'\Upsilon': 'Υ',
    r'\Phi': 'Φ', r'\Psi': 'Ψ', r'\Omega': 'Ω',
}

OPERATORS = {
    r'\leq': '≤', r'\le': '≤', r'\geq': '≥', r'\ge': '≥',
    r'\neq': '≠', r'\ne': '≠', r'\approx': '≈', r'\equiv': '≡',
    r'\sim': '~', r'\simeq': '≃', r'\cong': '≅', r'\propto': '∝',
    r'\ll': '≪', r'\gg': '≫',
    r'\to': '→', r'\rightarrow': '→', r'\leftarrow': '←',
    r'\leftrightarrow': '↔', r'\Rightarrow': '⇒', r'\Leftarrow': '⟸',
    r'\Leftrightarrow': '⟺', r'\mapsto': '↦',
    r'\infty': '∞', r'\nabla': '∇', r'\partial': '∂',
    r'\sum': 'Σ', r'\prod': 'Π', r'\int': '∫',
    r'\in': '∈', r'\notin': '∉', r'\ni': '∋',
    r'\subset': '⊂', r'\subseteq': '⊆', r'\supset': '⊃', r'\supseteq': '⊇',
    r'\cup': '∪', r'\cap': '∩', r'\emptyset': '∅', r'\varnothing': '∅',
    r'\forall': '∀', r'\exists': '∃', r'\nexists': '∄',
    r'\neg': '¬', r'\lnot': '¬', r'\land': '∧', r'\lor': '∨',
    r'\cdot': '·', r'\times': '×', r'\div': '÷', r'\pm': '±', r'\mp': '∓',
    r'\oplus': '⊕', r'\otimes': '⊗',
    r'\lfloor': '⌊', r'\rfloor': '⌋', r'\lceil': '⌈', r'\rceil': '⌉',
    r'\langle': '⟨', r'\rangle': '⟩',
    r'\ldots': '…', r'\cdots': '⋯', r'\vdots': '⋮', r'\ddots': '⋱',
    r'\mid': '|', r'\|': '‖',
    r'\log': 'log', r'\ln': 'ln', r'\exp': 'exp', r'\lim': 'lim',
    r'\min': 'min', r'\max': 'max', r'\sup': 'sup', r'\inf': 'inf',
    r'\det': 'det', r'\dim': 'dim', r'\ker': 'ker', r'\text{tr}': 'tr',
    r'\mathbb{R}': 'ℝ', r'\mathbb{N}': 'ℕ', r'\mathbb{Z}': 'ℤ',
    r'\mathbb{Q}': 'ℚ', r'\mathbb{C}': 'ℂ', r'\mathbb{F}': '𝔽',
    r'\mathbb{P}': 'ℙ', r'\mathbb{E}': '𝔼',
    r'\mathcal{X}': '𝒳', r'\mathcal{Y}': '𝒴', r'\mathcal{H}': 'ℋ',
    r'\mathcal{C}': '𝒞', r'\mathcal{F}': 'ℱ', r'\mathcal{A}': '𝒜',
    r'\mathcal{B}': 'ℬ', r'\mathcal{L}': 'ℒ', r'\mathcal{M}': 'ℳ',
    r'\mathcal{N}': '𝒩', r'\mathcal{O}': '𝒪', r'\mathcal{P}': '𝒫',
    r'\mathcal{S}': '𝒮', r'\mathcal{T}': '𝒯', r'\mathcal{U}': '𝒰',
    r'\mathcal{V}': '𝒱', r'\mathcal{W}': '𝒲',
    r'\text{NP}': 'NP', r'\text{P}': 'P', r'\text{coNP}': 'coNP',
    r'\text{PSPACE}': 'PSPACE', r'\text{BPP}': 'BPP', r'\text{BQP}': 'BQP',
    r'\text{QMA}': 'QMA', r'\text{RE}': 'RE', r'\text{SAT}': 'SAT',
    r'\text{HALT}': 'HALT', r'\text{TOT}': 'TOT', r'\text{FIN}': 'FIN',
}

SUPERSCRIPTS = str.maketrans('0123456789+=-n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁼⁻ⁿ')
SUBSCRIPTS   = str.maketrans('0123456789ianm', '₀₁₂₃₄₅₆₇₈₉ᵢₐₙₘ')


def apply_symbol_map(text: str) -> str:
    for pat, repl in sorted(OPERATORS.items(), key=lambda x: -len(x[0])):
        text = text.replace(pat, repl)
    for pat, repl in sorted(GREEK.items(), key=lambda x: -len(x[0])):
        text = text.replace(pat, repl)
    return text


def convert_frac(text: str) -> str:
    """Replace \frac{a}{b} with (a)/(b), iterating for nested fracs."""
    for _ in range(10):
        m = re.search(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', text)
        if not m:
            break
        num, den = m.group(1), m.group(2)
        num_s = f'({num})' if any(c in num for c in '+-/ ') else num
        den_s = f'({den})' if any(c in den for c in '+-/ ') else den
        text = text[:m.start()] + f'{num_s}/{den_s}' + text[m.end():]
    return text


def convert_sqrt(text: str) -> str:
    """Replace \sqrt{x} with √(x) or \sqrt[n]{x} with ⁿ√(x)."""
    text = re.sub(r'\\sqrt\[([^\]]+)\]\{([^{}]*)\}', r'\1√(\2)', text)
    text = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', text)
    return text


def convert_hat_bar(text: str) -> str:
    text = re.sub(r'\\hat\{(\w)\}', r'\1̂', text)
    text = re.sub(r'\\bar\{(\w)\}', r'\1̄', text)
    text = re.sub(r'\\tilde\{(\w)\}', r'\1̃', text)
    text = re.sub(r'\\vec\{(\w)\}', r'\1→', text)
    return text


def convert_text_cmd(text: str) -> str:
    """Remove \text{...}, \mathrm{...}, \mathbf{...}, \mathit{...}."""
    text = re.sub(r'\\(?:text|mathrm|mathbf|mathit|mathsf|boldsymbol)\{([^}]*)\}', r'\1', text)
    return text


def convert_subscript_superscript(text: str) -> str:
    """Convert simple ^{n} and _{i} to unicode or plain."""
    # Simple single-char: x^2 → x²
    text = re.sub(r'\^(\d)', lambda m: m.group(1).translate(SUPERSCRIPTS), text)
    # Braced: x^{23} → x²³ if all digits
    def sup_braced(m):
        inner = m.group(1)
        if re.fullmatch(r'[\d+\-=n]+', inner):
            return inner.translate(SUPERSCRIPTS)
        return f'^({inner})'
    text = re.sub(r'\^\{([^}]+)\}', sup_braced, text)
    # Subscript braced: x_{i} → keep as x_i (already readable)
    text = re.sub(r'_\{([^}]+)\}', r'_\1', text)
    return text


def strip_remaining_commands(text: str) -> str:
    """Remove unrecognised commands like \left, \right, \big, \!, \,."""
    for cmd in [r'\left', r'\right', r'\bigl', r'\bigr', r'\Bigl', r'\Bigr',
                r'\big', r'\Big', r'\!', r'\,', r'\;', r'\\', r'\quad', r'\qquad',
                r'\nonumber', r'\label', r'\tag', r'\notag']:
        text = text.replace(cmd, '')
    return text


def convert_math(math: str) -> str:
    """Convert a single math expression (without surrounding $ signs)."""
    math = convert_text_cmd(math)
    math = apply_symbol_map(math)
    math = convert_frac(math)
    math = convert_sqrt(math)
    math = convert_hat_bar(math)
    math = convert_subscript_superscript(math)
    math = strip_remaining_commands(math)
    math = math.strip()
    return math


def convert_display_block(math: str) -> str:
    """Convert a display math block to a readable indented block."""
    converted = convert_math(math.strip())
    # Split multi-line (aligned environments)
    converted = re.sub(r'\\begin\{[^}]*\}|\\end\{[^}]*\}', '', converted)
    converted = re.sub(r'&', '  ', converted)
    converted = converted.replace(r'\\ ', '\n')
    lines = [l.strip() for l in converted.splitlines() if l.strip()]
    if len(lines) == 1:
        return f'\n> **Fórmula:** `{lines[0]}`\n'
    else:
        block = '\n'.join(f'    {l}' for l in lines)
        return f'\n```\n{block}\n```\n'


def convert_inline(math: str) -> str:
    """Convert inline math to readable text."""
    converted = convert_math(math)
    return f'`{converted}`'


def convert_document(text: str) -> str:
    """Full document conversion pipeline."""
    # Protect code blocks (```...```) from conversion
    code_blocks = {}
    placeholder_base = '\x00CODEBLOCK{}\x00'

    def protect_code(m):
        idx = len(code_blocks)
        key = placeholder_base.format(idx)
        code_blocks[key] = m.group(0)
        return key

    # Protect fenced code blocks and inline code
    text = re.sub(r'```[\s\S]*?```', protect_code, text)
    text = re.sub(r'`[^`]+`', protect_code, text)

    # Convert display math $$ ... $$
    def replace_display(m):
        return convert_display_block(m.group(1))

    text = re.sub(r'\$\$\s*([\s\S]*?)\s*\$\$', replace_display, text)

    # Protect remaining backtick sequences that may contain $ (e.g. \text{`...`})
    # by replacing them temporarily
    text = re.sub(r'`[^`\n]+`', protect_code, text)

    # Convert inline math $ ... $ (allow up to 300 chars, may span escaped chars)
    def replace_inline(m):
        inner = m.group(1)
        if '\n' in inner or len(inner) > 300:
            return convert_display_block(inner)
        return convert_inline(inner)

    # Two-pass: first long inline (greedy won't work, use non-greedy with higher limit)
    text = re.sub(r'\$([^\$]{1,300}?)\$', replace_inline, text)

    # Restore code blocks
    for key, val in code_blocks.items():
        text = text.replace(key, val)

    return text


def add_header(text: str, art_path: Path) -> str:
    """Prepend a notice about the LaTeX version."""
    rel = art_path.relative_to(TUTORIAL)
    notice = (
        f"> **Nota:** Esta es la versión sin fórmulas LaTeX de "
        f"[{art_path.stem}](../../{rel}). "
        f"Las expresiones matemáticas se muestran en texto plano y Unicode. "
        f"Para la versión completa con renderizado de fórmulas, consulta el archivo original "
        f"o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).\n\n"
        f"---\n\n"
    )
    return notice + text


TOP_ARTICLES_BY_MODULE = [
    TUTORIAL / "02-teoria-informacion" / "08-teorema-de-shannon-capacidad.md",
    TUTORIAL / "02-teoria-informacion" / "09-teoria-tasa-distorsion.md",
    TUTORIAL / "02-teoria-informacion" / "10-entropia-diferencial.md",
    TUTORIAL / "02-teoria-informacion" / "14-procesos-estocasticos-y-fuentes-con-memoria.md",
    TUTORIAL / "02-teoria-informacion" / "15-codigos-reed-solomon.md",
    TUTORIAL / "03-computabilidad"     / "10-jerarquia-aritmetica.md",
    TUTORIAL / "03-computabilidad"     / "11-oráculos-y-relativización.md",
    TUTORIAL / "03-computabilidad"     / "12-aleatoriedad-algoritmica.md",
    TUTORIAL / "04-complejidad-computacional" / "08-complejidad-aleatoria.md",
    TUTORIAL / "04-complejidad-computacional" / "10-complejidad-parametrizada.md",
    TUTORIAL / "04-complejidad-computacional" / "12-complejidad-de-comunicacion.md",
    TUTORIAL / "04-complejidad-computacional" / "14-complejidad-cuantica-bqp-qma.md",
    TUTORIAL / "05-conexiones-y-aplicaciones" / "01-complejidad-de-kolmogorov.md",
    TUTORIAL / "05-conexiones-y-aplicaciones" / "10-aprendizaje-profundo-desde-la-informacion.md",
    TUTORIAL / "05-conexiones-y-aplicaciones" / "11-privacidad-diferencial.md",
]


def main():
    parser = argparse.ArgumentParser(description="Genera versiones sin LaTeX de artículos")
    parser.add_argument("--todos", action="store_true", help="Convertir todos los artículos")
    parser.add_argument("--articulo", metavar="PATH", help="Convertir solo este artículo")
    parser.add_argument("--out", default=str(DEFAULT_OUT), metavar="DIR",
                        help=f"Directorio de salida (default: tutorial/sin-formulas/)")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.articulo:
        articles = [Path(args.articulo)]
    elif args.todos:
        articles = sorted(TUTORIAL.rglob("[0-9]*.md"))
        articles = [a for a in articles if "sin-formulas" not in str(a)]
    else:
        articles = [a for a in TOP_ARTICLES_BY_MODULE if a.exists()]

    print(f"Convirtiendo {len(articles)} artículo(s) → {out_dir.relative_to(ROOT)}/")
    print("=" * 60)

    for art in articles:
        text = art.read_text(encoding="utf-8")
        converted = convert_document(text)
        converted = add_header(converted, art)

        # Preserve module subdirectory structure
        try:
            rel_parts = art.relative_to(TUTORIAL).parts
            sub = rel_parts[0] if len(rel_parts) > 1 else ""
            sub_dir = out_dir / sub
            sub_dir.mkdir(parents=True, exist_ok=True)
            out_file = sub_dir / art.name
        except ValueError:
            out_file = out_dir / art.name

        out_file.write_text(converted, encoding="utf-8")

        # Count remaining $ (unconverted formulas)
        remaining = converted.count('$')
        status = "✅" if remaining == 0 else f"⚠️  ({remaining} $ restantes)"
        print(f"  {status}  {art.relative_to(TUTORIAL)}")

    print("=" * 60)
    print(f"Listo. Archivos en {out_dir.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
