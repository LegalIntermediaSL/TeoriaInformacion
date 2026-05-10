# Mejoras pendientes

Registro de mejoras identificadas para el tutorial.
Marcar con `[x]` cuando se complete. Ordenadas de mayor a menor impacto pedagógico dentro de cada sección.

---

## 1. Artículos nuevos — huecos temáticos

### Módulo 02 — Teoría de la información

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [ ] | Codificación aritmética | `02/12-codificacion-aritmetica.md` | Fundamento real de zlib, HEVC, JPEG2000; complementa LZ78 y Huffman |
| [ ] | Procesos estocásticos y fuentes con memoria (orden k, mezcla, ergodicidad) | `02/13-procesos-estocásticos.md` | Generalización del artículo de Markov a fuentes de orden superior |

### Módulo 03 — Computabilidad

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [ ] | Jerarquía aritmética (Σ₀, Σ₁, Π₁, Δ₁, oráculo de salto) | `03/10-jerarquia-aritmetica.md` | Estructura fina por encima de RE; falta para cerrar el módulo |
| [ ] | Máquinas de Turing con oráculo y relativización | `03/11-oráculos-y-relativizacion.md` | Por qué P≠NP no puede probarse con diagonalización; Baker-Gill-Solovay |
| [ ] | Aleatoriedad algorítmica (Ω de Chaitin, cadenas aleatorias, Martin-Löf) | `03/12-aleatoriedad-algorítmica.md` | Conecta Kolmogorov con probabilidad; la "aleatoriedad real" |

### Módulo 04 — Complejidad computacional

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [ ] | #P y problemas de conteo (teorema de Toda, #SAT, permanente) | `04/11-sharp-p-y-conteo.md` | El salto NP→PSPACE tiene protagonistas propios; no cubierto |
| [ ] | Complejidad de comunicación (modelo Alice-Bob, lower bounds) | `04/12-complejidad-comunicacion.md` | Herramienta clave para lower bounds de circuitos y espacio |
| [ ] | Hipótesis ETH y SETH: consecuencias concretas | `04/13-eth-seth-consecuencias.md` | Fine-grained complexity; por qué n² parece óptimo para LCS, etc. |

### Módulo 05 — Conexiones y aplicaciones

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [ ] | Información y biología (código genético, entropía del genoma, evolución) | `05/07-informacion-y-biologia.md` | ADN como código corrector, redundancia, información de Fisher en evolución |
| [ ] | Artículo de síntesis final ("el mapa completo") | `05/08-mapa-de-conexiones.md` | Cierre del tutorial: tabla unificada de todos los resultados y puentes entre módulos |

### Módulo 00 — Presentación

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [ ] | Guía de rutas de profundización ("¿por dónde sigo?") | `00/02-rutas-de-profundizacion.md` | Lecturas graduadas por nivel y especialización para después del tutorial |

---

## 2. Ejercicios resueltos — brechas directas

Artículos o notebooks sin `.md` de ejercicios resueltos asociado:

### Con notebook de ejercicio ya existente (prioridad alta)

| Estado | Tema | Artículo | Notebook ejercicio |
|--------|------|----------|--------------------|
| [x] | Tasa-distorsión | 02/09 | ✓ ejercicios/14 |
| [x] | Complejidad aleatoria | 04/08 | ✓ ejercicios/13 |
| [x] | Complejidad parametrizada | 04/10 | ✓ ejercicios/16 |
| [x] | Autómatas de pila / CFL | 03/09 | ✓ ejemplos/21 |
| [x] | Cadenas de Markov y tasa de entropía | 02/12 | ✓ ejemplos/20 |
| [x] | Universalidad y quines | 03/07 | ✓ ejercicios/15 |

### Sin ninguna práctica asociada (prioridad media)

| Estado | Tema | Artículo | Situación |
|--------|------|----------|-----------|
| [ ] | Teorema de Shannon y capacidad | 02/08 | Sin notebook ni resuelto propio |
| [ ] | Gramáticas y jerarquía de Chomsky | 03/06 | Sin notebook ni resuelto |
| [ ] | Complejidad descriptiva | 03/08 | Sin notebook ni resuelto |
| [ ] | Reducciones polinómicas | 04/02 | Sin notebook ni resuelto |
| [ ] | Aproximación y heurísticas | 04/06 | Sin notebook ni resuelto |
| [ ] | El teorema PCP | 04/09 | Sin notebook ni resuelto |
| [ ] | Complejidad de Kolmogorov | 05/01 | Sin notebook específico |
| [ ] | Criptografía y complejidad | 05/02 | Sin notebook ni resuelto |
| [ ] | Información cuántica | 05/04 | Sin notebook ni resuelto |

---

## 3. Notebooks — práctica que falta

### Nuevos de ejemplo

| Estado | Notebook | Artículo que ilustra |
|--------|----------|----------------------|
| [ ] | `23-codificacion-aritmetica.ipynb` | 02 (art. pendiente): codificador aritmético desde cero, comparación con Huffman |
| [ ] | `24-complejidad-comunicacion.ipynb` | 04 (art. pendiente): protocolo Alice-Bob, lower bound de igualdad |
| [ ] | `25-aleatoriedad-algorítmica.ipynb` | 03 (art. pendiente): compresibilidad, cadenas de Chaitin, test de Martin-Löf |

### Nuevos de ejercicio

| Estado | Notebook | Artículo que cubre |
|--------|----------|--------------------|
| [ ] | `17-sharp-p-y-conteo.ipynb` | 04/11 (pendiente): contar coloraciones, permanente, aproximación de Jerrum-Sinclair |
| [ ] | `18-kolmogorov-y-compresion.ipynb` | 05/01: longitud de descripción, compresibilidad, invarianza |
| [ ] | `19-jerarquia-aritmetica.ipynb` | 03/10 (pendiente): oráculo de salto, conjuntos Σ₁ y Π₁ |
| [ ] | `20-criptografia-basica.ipynb` | 05/02: OTP, RSA modular, Diffie-Hellman, hash resistente |
| [ ] | `21-informacion-cuantica.ipynb` | 05/04: qubit, puerta Hadamard, entropía de Von Neumann, teletransporte |

---

## 4. Calidad estructural — mejoras transversales

### Alta prioridad

| Estado | Mejora | Archivo afectado |
|--------|--------|------------------|
| [x] | **`referencias/por-articulo.md`**: el archivo llega solo hasta 05/04 (información cuántica); faltan las entradas de los ~20 artículos creados en sesiones posteriores (02/09-12, 03/07-09, 04/08-10, 05/05-06) | `tutorial/referencias/por-articulo.md` |
| [x] | **Ruta de estudio Nivel 2** en el README principal: lista 8 artículos pero el módulo 02 tiene 12; faltan tasa-distorsión (09), entropía diferencial (10), LDPC (11), cadenas de Markov (12) | `tutorial/README.md` |
| [x] | **Ruta de estudio Nivel 3** en el README principal: falta el artículo de autómatas de pila (03/09) que se añadió en la quinta ronda | `tutorial/README.md` |

### Media prioridad

| Estado | Mejora | Archivo afectado |
|--------|--------|------------------|
| [ ] | **Carpeta `ejercicios/propuestos/`**: enunciados sin solución extraídos de las secciones "Ejercicios" de cada artículo, para uso en clase o examen | directorio nuevo |
| [ ] | **Tests automáticos en notebooks de ejercicio**: añadir celda final con `assert resultado_alumno == resultado_ref` para hacer los ejercicios autoevaluables sin necesidad de leer la solución | todos los `.ipynb` de `cuadernos/ejercicios/` |
| [ ] | **Ejemplos numéricos guiados** en los artículos que solo tienen teoría y ejercicios abstractos: 03/08 (complejidad descriptiva), 04/09 (PCP), 05/01 (Kolmogorov) | artículos individuales |
| [ ] | **Sección "Prerrequisitos"** al inicio de cada artículo con enlaces a los artículos previos que se necesitan entender | todos los artículos |

### Baja prioridad

| Estado | Mejora | Archivo afectado |
|--------|--------|------------------|
| [ ] | Unificar sección "Ideas clave" a exactamente 5 puntos en todos los artículos (actualmente varía entre 3 y 8) | todos los artículos |
| [ ] | Añadir `## Objetivos de aprendizaje` explícitos al inicio de cada artículo que no los tenga | artículos individuales |
| [ ] | Añadir nivel de dificultad estimado a cada artículo: `⭐ Básico`, `⭐⭐ Intermedio`, `⭐⭐⭐ Avanzado` | todos los artículos |
| [ ] | **Sección "Véase también"** al final de cada artículo: lista de 2-4 artículos del tutorial directamente relacionados | todos los artículos |
| [ ] | Añadir estimación de tiempo de lectura a cada artículo (e.g. `~20 min`) | todos los artículos |

---

## 5. Diagramas y visualizaciones

Los artículos son solo texto y fórmulas. Algunas visualizaciones añadirían mucho:

| Estado | Diagrama | Artículo | Descripción |
|--------|----------|----------|-------------|
| [ ] | Grafo de Tanner con 6 nodos variable y 3 restricción | 02/11 LDPC | Imagen SVG del grafo bipartito del código ejemplo |
| [ ] | Diagrama de la jerarquía de Chomsky (4 niveles anidados) | 03/06 + 03/09 | Anillo de contenidos: Regular ⊂ CFL ⊂ CSL ⊂ RE |
| [ ] | Diagrama de clases de complejidad anidadas | 04/01 P/NP | P ⊆ NP ⊆ PSPACE ⊆ EXP con los problemas canónicos de cada nivel |
| [ ] | Curva de tasa-distorsión R(D) para Bernoulli y Gaussiana | 02/09 | Gráfico comparativo de ambas curvas |
| [ ] | Árbol de búsqueda acotado para k-Vertex Cover k=3 | 04/10 | Árbol binario de branching con 8 hojas |
| [ ] | Diagrama del demonio de Maxwell | 05/06 | Dos compartimentos + compuerta + molécula rápida/lenta |
| [ ] | Polarización de canal para códigos polares (n=4) | 02/11 | Árbol de canales sintéticos buenos/malos |

---

## 6. Coherencia y consistencia interna

Problemas detectados que afectan a la coherencia del conjunto:

| Estado | Problema | Artículos afectados |
|--------|----------|---------------------|
| [ ] | El artículo 05/03 ("Aprendizaje automático e información") solapa con 05/05 ("Información en el aprendizaje estadístico"): el primero es general/introductorio, el segundo más técnico. Debería haber un enlace explícito entre ambos y delimitar claramente qué cubre cada uno | 05/03, 05/05 |
| [ ] | El artículo 03/06 (gramáticas) y 03/09 (autómatas de pila) están separados pero son dos caras del mismo teorema (CFG ↔ PDA). Añadir nota de remisión mutua | 03/06, 03/09 |
| [ ] | Las referencias a "el artículo de LDPC" en el notebook 18 apuntan al artículo 11 del módulo 02, pero la ruta relativa en el notebook puede haberse roto si se mueve algún archivo | `cuadernos/ejemplos/18-codigos-ldpc-simulacion.ipynb` |
| [ ] | Los notebooks de ejercicios 11 y 12 (Turing y autómatas) no tienen celda de solución de referencia explícita, a diferencia de los más recientes | `cuadernos/ejercicios/11-*.ipynb`, `12-*.ipynb` |

---

## 7. Infraestructura y automatización

| Estado | Mejora | Prioridad |
|--------|--------|-----------|
| [ ] | **Script de validación**: verificar que todos los artículos listados en los READMEs existen en disco y viceversa (detecta entradas huérfanas o archivos sin índice) | Alta |
| [ ] | **Script de estadísticas**: contar artículos, notebooks y ejercicios por módulo y mostrar cobertura (artículos con/sin notebook, con/sin resuelto) | Media |
| [ ] | **GitHub Actions CI**: ejecutar los notebooks con `jupyter nbconvert --execute` en cada push para detectar errores de sintaxis Python | Media |
| [ ] | **Plantilla de artículo** (`_plantilla-articulo.md`) con la estructura canónica: Intuición / Definición formal / Ejemplo / Teorema principal / Ideas clave / Ejercicios / Referencias | Baja |
| [ ] | **Plantilla de notebook de ejemplo** y **plantilla de notebook de ejercicio** para homogeneizar estructura | Baja |

---

## Resumen de estado

| Categoría | Total ítems | Completados |
|-----------|-------------|-------------|
| Artículos nuevos | 10 | 0 |
| Ejercicios resueltos | 15 | 6 |
| Notebooks nuevos | 8 | 0 |
| Calidad estructural | 11 | 3 |
| Diagramas | 7 | 0 |
| Coherencia interna | 4 | 0 |
| Infraestructura | 5 | 0 |
| **Total** | **60** | **9** |

> Actualizar la tabla de resumen al completar ítems.
