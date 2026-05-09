# Mejoras pendientes

Registro de mejoras identificadas para el tutorial. Marcar con `[x]` cuando se complete.

---

## 1. Artículos con hueco real

| Estado | Artículo | Módulo | Nota |
|--------|----------|--------|------|
| [ ] | Jerarquía aritmética (Σ₀, Σ₁, Π₁, Δ₁) | 03 | Los artículos de decidibilidad llegan hasta RE pero no mapean los niveles de la jerarquía |
| [ ] | Complejidad de comunicación (Alice-Bob, lower bounds) | 04 | Clave entre circuitos y espacio; da lower bounds de forma elemental |
| [ ] | #P y problemas de conteo (teorema de Toda, #SAT) | 04 | El salto NP→PSPACE tiene protagonistas propios que no están cubiertos |
| [ ] | Codificación aritmética | 02 | El codificador real detrás de zlib/HEVC/JPEG2000; complementa LZ78 |
| [ ] | Artículo de síntesis final ("el mapa completo") | 05 | Cierre del tutorial: tabla unificada de todos los resultados y cómo se relacionan |

---

## 2. Ejercicios resueltos — brechas directas

Artículos con notebook pero sin `.md` de ejercicios resueltos:

| Estado | Tema | Artículo | Notebook existente |
|--------|------|----------|--------------------|
| [ ] | Tasa-distorsión | 02/09 | ✓ ejercicios/14 |
| [ ] | Complejidad aleatoria | 04/08 | ✓ ejercicios/13 |
| [ ] | Complejidad parametrizada | 04/10 | ✓ ejercicios/16 |
| [ ] | Autómatas de pila / CFL | 03/09 | ✓ ejemplos/21 |
| [ ] | Cadenas de Markov y tasa de entropía | 02/12 | ✓ ejemplos/20 |

---

## 3. Notebooks — práctica que falta

| Estado | Notebook | Tipo | Artículo que cubre |
|--------|----------|------|--------------------|
| [ ] | `23-codificacion-aritmetica.ipynb` | ejemplo | 02 (artículo pendiente de crear) |
| [ ] | `24-complejidad-comunicacion.ipynb` | ejemplo | 04 (artículo pendiente) |
| [ ] | `17-sharp-p-y-conteo.ipynb` | ejercicio | 04 (artículo pendiente) |
| [ ] | `18-kolmogorov-y-compresion.ipynb` | ejercicio | 05/01 Kolmogorov |
| [ ] | `19-jerarquia-aritmetica.ipynb` | ejercicio | 03/02-03 decidibilidad |

---

## 4. Calidad estructural — mejoras transversales

### Alta prioridad

| Estado | Mejora |
|--------|--------|
| [ ] | **`referencias/por-articulo.md`**: sincronizar con los ~35 artículos añadidos desde la sesión inicial |
| [ ] | **Ruta de estudio Nivel 2** en `tutorial/README.md`: solo lista 8 artículos pero el módulo 02 tiene 12 (faltan tasa-distorsión, entropía diferencial, LDPC, cadenas de Markov) |

### Media prioridad

| Estado | Mejora |
|--------|--------|
| [ ] | **Carpeta `ejercicios/propuestos/`**: enunciados sin solución extraídos de los artículos, para uso en clase o autoevaluación |
| [ ] | **Tests automáticos en notebooks de ejercicio**: añadir celda final con `assert resultado_alumno == resultado_ref` para hacer los ejercicios autoevaluables |

### Baja prioridad

| Estado | Mejora |
|--------|--------|
| [ ] | Añadir `## Objetivos de aprendizaje` explícitos al inicio de cada artículo que no los tenga |
| [ ] | Unificar sección "Ideas clave" a 5 puntos en todos los artículos (actualmente varía entre 3 y 8) |
