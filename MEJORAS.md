# Mejoras pendientes

Registro de mejoras identificadas para el tutorial.
Marcar con `[x]` cuando se complete. Ordenadas de mayor a menor impacto pedagógico dentro de cada sección.

---

## 1. Artículos nuevos — huecos temáticos

### Módulo 02 — Teoría de la información

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [x] | Codificación aritmética | `02/13-codificacion-aritmetica.md` | Fundamento real de zlib, HEVC, JPEG2000; complementa LZ78 y Huffman |
| [x] | Procesos estocásticos y fuentes con memoria (orden k, mezcla, ergodicidad) | `02/14-procesos-estocasticos-y-fuentes-con-memoria.md` | Generalización del artículo de Markov a fuentes de orden superior |

### Módulo 03 — Computabilidad

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [x] | Jerarquía aritmética (Σ₀, Σ₁, Π₁, Δ₁, oráculo de salto) | `03/10-jerarquia-aritmetica.md` | Estructura fina por encima de RE; falta para cerrar el módulo |
| [x] | Máquinas de Turing con oráculo y relativización | `03/11-oráculos-y-relativización.md` | Por qué P≠NP no puede probarse con diagonalización; Baker-Gill-Solovay |
| [x] | Aleatoriedad algorítmica (Ω de Chaitin, cadenas aleatorias, Martin-Löf) | `03/12-aleatoriedad-algoritmica.md` | Conecta Kolmogorov con probabilidad; la "aleatoriedad real" |

### Módulo 04 — Complejidad computacional

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [x] | #P y problemas de conteo (teorema de Toda, #SAT, permanente) | `04/11-sharp-p-y-conteo.md` | El salto NP→PSPACE tiene protagonistas propios; no cubierto |
| [x] | Complejidad de comunicación (modelo Alice-Bob, lower bounds) | `04/12-complejidad-de-comunicacion.md` | Herramienta clave para lower bounds de circuitos y espacio |
| [x] | Hipótesis ETH y SETH: consecuencias concretas | `04/13-eth-seth-consecuencias.md` | Fine-grained complexity; por qué n² parece óptimo para LCS, etc. |

### Módulo 05 — Conexiones y aplicaciones

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [x] | Información y biología (código genético, entropía del genoma, evolución) | `05/07-informacion-y-biologia.md` | ADN como código corrector, redundancia, información de Fisher en evolución |
| [x] | Artículo de síntesis final ("el mapa completo") | `05/08-mapa-de-conexiones.md` | Cierre del tutorial: tabla unificada de todos los resultados y puentes entre módulos |

### Módulo 00 — Presentación

| Estado | Artículo propuesto | Archivo destino | Nota |
|--------|-------------------|-----------------|------|
| [x] | Guía de rutas de profundización ("¿por dónde sigo?") | `00/02-rutas-de-profundizacion.md` | Lecturas graduadas por nivel y especialización para después del tutorial |

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
| [x] | Teorema de Shannon y capacidad | 02/08 | `resueltos/19-teorema-shannon-capacidad.md` |
| [x] | Gramáticas y jerarquía de Chomsky | 03/06 | `resueltos/20-gramaticas-y-chomsky.md` |
| [x] | Complejidad descriptiva | 03/08 | `resueltos/21-complejidad-descriptiva.md` |
| [x] | Reducciones polinómicas | 04/02 | `resueltos/22-reducciones-polinomicas.md` |
| [x] | Aproximación y heurísticas | 04/06 | `resueltos/23-aproximacion-y-heuristicas.md` |
| [x] | El teorema PCP | 04/09 | `resueltos/24-teorema-pcp.md` |
| [x] | Complejidad de Kolmogorov | 05/01 | `resueltos/25-complejidad-kolmogorov.md` |
| [x] | Criptografía y complejidad | 05/02 | `resueltos/26-criptografia-y-complejidad.md` |
| [x] | Información cuántica | 05/04 | `resueltos/27-informacion-cuantica.md` |

---

## 3. Notebooks — práctica que falta

### Nuevos de ejemplo

| Estado | Notebook | Artículo que ilustra |
|--------|----------|----------------------|
| [x] | `23-codificacion-aritmetica.ipynb` | 02/13: codificador aritmético desde cero, comparación con Huffman |
| [x] | `24-complejidad-comunicacion.ipynb` | 04/12: protocolo Alice-Bob, lower bound de igualdad |
| [x] | `25-aleatoriedad-algorítmica.ipynb` | 03/12: compresibilidad, cadenas de Chaitin, test de Martin-Löf |

### Nuevos de ejercicio

| Estado | Notebook | Artículo que cubre |
|--------|----------|--------------------|
| [x] | `17-sharp-p-y-conteo.ipynb` | 04/11: contar coloraciones, permanente, aproximación de Jerrum-Sinclair |
| [x] | `18-kolmogorov-y-compresion.ipynb` | 05/01: longitud de descripción, compresibilidad, invarianza |
| [x] | `19-jerarquia-aritmetica.ipynb` | 03/10: oráculo de salto, conjuntos Σ₁ y Π₁ |
| [x] | `20-criptografia-basica.ipynb` | 05/02: OTP, RSA modular, Diffie-Hellman, hash resistente |
| [x] | `21-informacion-cuantica.ipynb` | 05/04: qubit, puerta Hadamard, entropía de Von Neumann, teletransporte |

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
| [x] | **Carpeta `ejercicios/propuestos/`**: enunciados sin solución extraídos de las secciones "Ejercicios" de cada artículo, para uso en clase o examen | `ejercicios/propuestos/` creado con enunciados de módulos 02 y 04 |
| [x] | **Tests automáticos en notebooks de ejercicio**: añadir celda final con `assert resultado_alumno == resultado_ref` para hacer los ejercicios autoevaluables sin necesidad de leer la solución | todos los `.ipynb` de `cuadernos/ejercicios/` |
| [x] | **Ejemplos numéricos guiados** en los artículos que solo tienen teoría y ejercicios abstractos: 03/08 (complejidad descriptiva), 04/09 (PCP), 05/01 (Kolmogorov) | artículos individuales |
| [x] | **Sección "Prerrequisitos"** al inicio de cada artículo con enlaces a los artículos previos que se necesitan entender | todos los artículos |

### Baja prioridad

| Estado | Mejora | Archivo afectado |
|--------|--------|------------------|
| [x] | Unificar sección "Ideas clave" a exactamente 5 puntos en todos los artículos (actualmente varía entre 3 y 8) | todos los artículos |
| [x] | Añadir `## Objetivos de aprendizaje` explícitos al inicio de cada artículo que no los tenga | artículos individuales |
| [x] | Añadir nivel de dificultad estimado a cada artículo: `⭐ Básico`, `⭐⭐ Intermedio`, `⭐⭐⭐ Avanzado` | todos los artículos |
| [x] | **Sección "Véase también"** al final de cada artículo: lista de 2-4 artículos del tutorial directamente relacionados | todos los artículos |
| [x] | Añadir estimación de tiempo de lectura a cada artículo (e.g. `~20 min`) | todos los artículos |

---

## 5. Diagramas y visualizaciones

Los artículos son solo texto y fórmulas. Algunas visualizaciones añadirían mucho:

| Estado | Diagrama | Artículo | Descripción |
|--------|----------|----------|-------------|
| [x] | Grafo de Tanner con 6 nodos variable y 3 restricción | 02/11 LDPC | Imagen SVG del grafo bipartito del código ejemplo |
| [x] | Diagrama de la jerarquía de Chomsky (4 niveles anidados) | 03/06 + 03/09 | Anillo de contenidos: Regular ⊂ CFL ⊂ CSL ⊂ RE |
| [x] | Diagrama de clases de complejidad anidadas | 04/01 P/NP | P ⊆ NP ⊆ PSPACE ⊆ EXP con los problemas canónicos de cada nivel |
| [x] | Curva de tasa-distorsión R(D) para Bernoulli y Gaussiana | 02/09 | Gráfico comparativo de ambas curvas |
| [x] | Árbol de búsqueda acotado para k-Vertex Cover k=3 | 04/10 | Árbol binario de branching con 8 hojas |
| [x] | Diagrama del demonio de Maxwell | 05/06 | Dos compartimentos + compuerta + molécula rápida/lenta |
| [x] | Polarización de canal para códigos polares (n=4) | 02/11 | Árbol de canales sintéticos buenos/malos |

---

## 6. Coherencia y consistencia interna

Problemas detectados que afectan a la coherencia del conjunto:

| Estado | Problema | Artículos afectados |
|--------|----------|---------------------|
| [x] | El artículo 05/03 ("Aprendizaje automático e información") solapa con 05/05 ("Información en el aprendizaje estadístico"): añadida sección "Véase también" en ambos con delimitación explícita | 05/03, 05/05 |
| [x] | El artículo 03/06 (gramáticas) y 03/09 (autómatas de pila) son dos caras del mismo teorema (CFG ↔ PDA): añadida nota de remisión mutua en ambos | 03/06, 03/09 |
| [x] | Las referencias a "el artículo de LDPC" en el notebook 18 apuntan al artículo 11 del módulo 02: ruta verificada correcta (`../../02-teoria-informacion/11-codigos-ldpc-y-turbo.md`) | `cuadernos/ejemplos/18-codigos-ldpc-simulacion.ipynb` |
| [x] | Los notebooks de ejercicios 11 y 12 (Turing y autómatas) no tienen celda de solución de referencia explícita: añadidas celdas de referencia | `cuadernos/ejercicios/11-*.ipynb`, `12-*.ipynb` |

---

## 7. Infraestructura y automatización

| Estado | Mejora | Prioridad |
|--------|--------|-----------|
| [x] | **Script de validación** (`scripts/validar_repositorio.py`): verifica que todos los artículos listados en los READMEs existen en disco y viceversa | Alta |
| [x] | **Script de estadísticas** (`scripts/estadisticas.py`): cuenta artículos, notebooks y ejercicios por módulo y muestra cobertura | Media |
| [x] | **GitHub Actions CI** (`.github/workflows/test_notebooks.yml`): ejecuta los notebooks con `jupyter nbconvert --execute` en cada push para detectar errores de sintaxis Python | Media |
| [x] | **Plantilla de artículo** (`tutorial/_plantilla-articulo.md`) con la estructura canónica: Intuición / Definición formal / Ejemplo / Teorema principal / Ideas clave / Ejercicios / Referencias | Baja |
| [x] | **Plantillas de notebook** (`tutorial/_plantilla-notebook-ejemplo.ipynb` y `_plantilla-notebook-ejercicio.ipynb`) para homogeneizar estructura | Baja |

---

## Resumen de estado

| Categoría | Total ítems | Completados |
|-----------|-------------|-------------|
| Artículos nuevos | 10 | 10 |
| Ejercicios resueltos | 15 | 15 |
| Notebooks nuevos | 8 | 8 |
| Calidad estructural | 11 | 11 |
| Diagramas | 7 | 7 |
| Coherencia interna | 4 | 4 |
| Infraestructura | 5 | 5 |
| **Total** | **60** | **60** |

> Actualizar la tabla de resumen al completar ítems.

---

## Segunda ronda — Sugerencias (0/40)

El plan original de 60 ítems está completado al 100 %. Las siguientes sugerencias
amplían el tutorial con contenido nuevo, cierran huecos de cobertura detectados
y mejoran la experiencia de lectura y práctica.

---

### 8. Huecos de cobertura detectados

#### 8a. Archivo roto — alta prioridad

| Estado | Problema | Archivo |
|--------|----------|---------|
| [ ] | **`propuestos/computabilidad.md` no existe** pero el README lo enlaza: enlace roto visible para cualquier lector | `tutorial/ejercicios/propuestos/computabilidad.md` |

#### 8b. Ejercicios propuestos incompletos

Los módulos 01 y 05 no tienen ningún archivo de enunciados sin solución.
El módulo 03 tiene el enlace roto (véase 8a).

| Estado | Mejora | Archivo destino |
|--------|--------|-----------------|
| [ ] | Crear `propuestos/computabilidad.md` con enunciados de los artículos 03/01-12 | `ejercicios/propuestos/computabilidad.md` |
| [ ] | Crear `propuestos/fundamentos.md` con enunciados de módulo 01 (logaritmos, conjuntos, combinatoria, grafos, lógica) | `ejercicios/propuestos/fundamentos.md` |
| [ ] | Crear `propuestos/conexiones.md` con enunciados de módulo 05 (Kolmogorov, criptografía, cuántica, termodinámica, biología) | `ejercicios/propuestos/conexiones.md` |

#### 8c. Artículos nuevos sin ningún notebook

Cuatro artículos creados en la segunda ronda carecen de notebook de ejemplo o de ejercicio.

| Estado | Artículo | Notebook propuesto |
|--------|----------|--------------------|
| [ ] | `03/11-oráculos-y-relativización` | `ejemplos/26-oráculos-relativización.ipynb`: simular oráculo de SAT, comparar P^SAT vs NP^SAT conceptualmente |
| [ ] | `04/13-eth-seth-consecuencias` | `ejemplos/27-eth-seth-lower-bounds.ipynb`: lower bounds condicionales para LCS y Edit Distance |
| [ ] | `05/07-informacion-y-biologia` | `ejemplos/28-codigo-genetico-entropia.ipynb`: calcular entropía del código genético, redundancia, información de Fisher |
| [ ] | `02/14-procesos-estocasticos-y-fuentes-con-memoria` | `ejemplos/29-fuentes-con-memoria.ipynb`: fuentes de Markov de orden k, tasa de entropía, comparación con i.i.d. |

#### 8d. Ejercicios resueltos faltantes

Hay 26 artículos sin `ejercicios/resueltos/` asociado. Los de mayor impacto pedagógico:

| Estado | Tema | Artículo |
|--------|------|----------|
| [ ] | Codificación aritmética | `02/13` → `resueltos/28-codificacion-aritmetica.md` |
| [ ] | Procesos estocásticos y fuentes con memoria | `02/14` → `resueltos/29-procesos-estocasticos.md` |
| [ ] | Oráculos y relativización | `03/11` → `resueltos/30-oráculos-y-relativización.md` |
| [ ] | Aleatoriedad algorítmica (Chaitin, Martin-Löf) | `03/12` → `resueltos/31-aleatoriedad-algoritmica.md` |
| [ ] | #P y conteo | `04/11` → `resueltos/32-sharp-p-y-conteo.md` |
| [ ] | Complejidad de comunicación | `04/12` → `resueltos/33-complejidad-comunicacion.md` |
| [ ] | ETH/SETH y consecuencias | `04/13` → `resueltos/34-eth-seth-consecuencias.md` |
| [ ] | Información y biología | `05/07` → `resueltos/35-informacion-y-biologia.md` |

#### 8e. Tests automáticos en notebooks de ejemplo y ejercicios 01-16

Las celdas `assert` solo existen en los notebooks de ejercicio 17-21.
Los notebooks 01-16 no tienen ninguna validación automática.

| Estado | Mejora | Archivos afectados |
|--------|--------|--------------------|
| [ ] | Añadir celda `assert` a notebooks de ejercicio 01-16 | `cuadernos/ejercicios/01-*.ipynb` … `16-*.ipynb` |
| [ ] | Añadir celda `assert` a notebooks de ejemplo seleccionados (los que implementan funciones verificables) | `cuadernos/ejemplos/` — prioridad 01, 03, 04, 08, 11, 12, 13 |

---

### 9. Recursos de referencia nuevos

| Estado | Recurso | Descripción | Archivo destino |
|--------|---------|-------------|-----------------|
| [ ] | **Glosario de términos** | Definición breve de cada símbolo y concepto técnico del tutorial: entropía, KL, NP, BPP, treewidth, etc. Ordenado alfabéticamente con enlace al artículo donde se introduce. | `tutorial/referencias/glosario.md` |
| [ ] | **Índice de notación matemática** | Tabla de todos los símbolos usados (H, I, K, D_KL, Σ, Π, Δ, ρ, S(ρ)…) con su definición y referencia al artículo. | `tutorial/referencias/notacion.md` |
| [ ] | **Tabla de complejidad unificada** | Una única tabla que cruza: problema / clase / mejor algoritmo conocido / cota inferior / referencia. Ampliación de la tabla del artículo 05/08. | `tutorial/referencias/tabla-complejidad.md` |
| [ ] | **Mapa de dependencias entre artículos** (SVG) | Grafo dirigido que muestra qué artículo requiere cuáles; generado desde los metadatos de Prerrequisitos. | `tutorial/imagenes/mapa-dependencias.svg` |

---

### 10. Mejoras de infraestructura y CI

| Estado | Mejora | Descripción | Prioridad |
|--------|--------|-------------|-----------|
| [ ] | **CI: validar estructura de artículos** | Extender `test_notebooks.yml` para comprobar que cada artículo tiene las secciones obligatorias (Prerrequisitos, Objetivos, Ideas clave, Véase también, Referencias) usando `scripts/validar_repositorio.py` | Alta |
| [ ] | **CI: verificar enlaces internos** | Añadir paso en CI que compruebe que todos los enlaces `[texto](ruta)` dentro de los artículos apuntan a archivos que existen | Alta |
| [ ] | **GitHub Pages** | Publicar el tutorial como sitio estático con MkDocs o Quarto; añadir `mkdocs.yml` o `_quarto.yml` y configurar el flujo de despliegue | Media |
| [ ] | **Exportación a PDF** | Script que genera un PDF por módulo usando Pandoc, útil para estudio offline | Baja |
| [ ] | **Script `generar_mapa_dependencias.py`** | Lee los metadatos de Prerrequisitos de cada artículo y genera automáticamente el SVG del grafo de dependencias | Media |

---

### 11. Contenido avanzado — artículos opcionales

Artículos que cubren temas que quedan fuera del tutorial actual pero son extensiones naturales del nivel avanzado:

| Estado | Artículo propuesto | Módulo | Motivación |
|--------|-------------------|--------|------------|
| [ ] | **Códigos de Reed-Solomon y aplicaciones** | 02 | Los LDPC y turbo son modernos, pero RS domina almacenamiento (CD, QR codes); cierra el círculo de teoría clásica |
| [ ] | **Complejidad cuántica: BQP y QMA** | 04 | Extensión natural de 05/04 (información cuántica) hacia la complejidad; algoritmo de Shor, Grover |
| [ ] | **Teoría de juegos e información** | 05 | Equilibrios de Nash, información asimétrica (Lemon market), mecanismos con información privada |
| [ ] | **Aprendizaje profundo desde la teoría de la información** | 05 | Cuello de botella de información (Tishby), teorema PAC-Bayes, generalización en redes sobreajustadas |
| [ ] | **Privacidad diferencial** | 05 | Conexión con la entropía de Rényi; protocolo de Laplace; aplicaciones prácticas en IA y datos |

---

### 12. Internacionalización y accesibilidad

| Estado | Mejora | Descripción |
|--------|--------|-------------|
| [ ] | **Resumen en inglés** de cada artículo (abstract de 3 líneas) | Permitiría indexación en buscadores internacionales y uso en contextos bilingües |
| [ ] | **Texto alternativo detallado para todos los SVG** | Los 7 SVG actuales no tienen `alt` text accesible; añadir descripción en el markdown |
| [ ] | **Versión ligera sin LaTeX** de los artículos más matemáticos | Para lectores que acceden desde entornos sin renderizado de fórmulas (GitHub mobile, algunos lectores RSS) |

---

## Resumen de estado (segunda ronda)

| Categoría | Total ítems | Completados |
|-----------|-------------|-------------|
| **Primera ronda (completada)** | **60** | **60** |
| Huecos de cobertura (8a-8e) | 18 | 0 |
| Recursos de referencia (9) | 4 | 0 |
| Infraestructura y CI (10) | 5 | 0 |
| Contenido avanzado (11) | 5 | 0 |
| Accesibilidad (12) | 3 | 0 |
| **Total segunda ronda** | **35** | **0** |
| **Total acumulado** | **95** | **60** |
