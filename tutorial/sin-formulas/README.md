# Versiones sin LaTeX

Esta carpeta contiene versiones de los artículos más matemáticos del tutorial con todas las fórmulas LaTeX convertidas a texto plano y símbolos Unicode.

Están pensadas para lectores que acceden desde entornos sin renderizado de fórmulas: GitHub Mobile, lectores RSS, terminales de texto o impresión.

## Artículos disponibles

| Módulo | Artículo | Original |
|--------|----------|---------|
| 02 | Teorema de Shannon (canal) | [02/08](../02-teoria-informacion/08-teorema-de-shannon-capacidad.md) |
| 02 | Teoría de tasa-distorsión | [02/09](../02-teoria-informacion/09-teoria-tasa-distorsion.md) |
| 02 | Entropía diferencial | [02/10](../02-teoria-informacion/10-entropia-diferencial.md) |
| 02 | Procesos estocásticos y fuentes con memoria | [02/14](../02-teoria-informacion/14-procesos-estocasticos-y-fuentes-con-memoria.md) |
| 02 | Códigos de Reed-Solomon | [02/15](../02-teoria-informacion/15-codigos-reed-solomon.md) |
| 03 | Jerarquía aritmética | [03/10](../03-computabilidad/10-jerarquia-aritmetica.md) |
| 03 | Oráculos y relativización | [03/11](../03-computabilidad/11-oráculos-y-relativización.md) |
| 03 | Aleatoriedad algorítmica | [03/12](../03-computabilidad/12-aleatoriedad-algoritmica.md) |
| 04 | Complejidad aleatoria (BPP, ZPP, RP) | [04/08](../04-complejidad-computacional/08-complejidad-aleatoria.md) |
| 04 | Complejidad parametrizada | [04/10](../04-complejidad-computacional/10-complejidad-parametrizada.md) |
| 04 | Complejidad de comunicación | [04/12](../04-complejidad-computacional/12-complejidad-de-comunicacion.md) |
| 04 | Complejidad cuántica (BQP, QMA) | [04/14](../04-complejidad-computacional/14-complejidad-cuantica-bqp-qma.md) |
| 05 | Complejidad de Kolmogorov | [05/01](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md) |
| 05 | Deep learning desde la información | [05/10](../05-conexiones-y-aplicaciones/10-aprendizaje-profundo-desde-la-informacion.md) |
| 05 | Privacidad diferencial | [05/11](../05-conexiones-y-aplicaciones/11-privacidad-diferencial.md) |

## Convenciones de conversión

| LaTeX | Conversión |
|-------|-----------|
| `\alpha`, `\beta`, `\sigma`… | α, β, σ… (Unicode) |
| `\leq`, `\geq`, `\neq` | ≤, ≥, ≠ |
| `\in`, `\subset`, `\cup` | ∈, ⊂, ∪ |
| `\sum`, `\prod`, `\infty` | Σ, Π, ∞ |
| `\mathbb{R}`, `\mathbb{N}` | ℝ, ℕ |
| `\frac{a}{b}` | `a/b` |
| `\sqrt{x}` | `√(x)` |
| Fórmulas display `$$…$$` | Bloque `> **Fórmula:** ...` |
| Inline `$…$` | `` `...` `` (backticks) |

## Regenerar

```bash
python scripts/convertir_sin_latex.py          # los 15 artículos predeterminados
python scripts/convertir_sin_latex.py --todos  # todos los artículos del tutorial
```
