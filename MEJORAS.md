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

#### 8a. Archivos rotos — alta prioridad

Verificado 2026-05-14: el directorio `propuestos/` contiene solo `README.md`, `complejidad.md` y `teoria-informacion.md`. El README enlaza a dos archivos que no existen:

| Estado | Problema | Archivo |
|--------|----------|---------|
| [x] | **`propuestos/computabilidad.md` no existe** pero el README lo enlaza (módulo 03): enlace roto visible para cualquier lector | `tutorial/ejercicios/propuestos/computabilidad.md` |
| [x] | **`propuestos/aplicaciones.md` no existe** pero el README lo enlaza (módulo 05): segundo enlace roto, no recogido en la primera detección | `tutorial/ejercicios/propuestos/aplicaciones.md` |

#### 8b. Ejercicios propuestos incompletos

Los módulos 01 y 05 no tienen ningún archivo de enunciados sin solución.
Los módulos 03 y 05 tienen los enlaces rotos (véase 8a).

| Estado | Mejora | Archivo destino |
|--------|--------|-----------------|
| [x] | Crear `propuestos/computabilidad.md` con enunciados de los artículos 03/01-12 | `ejercicios/propuestos/computabilidad.md` |
| [x] | Crear `propuestos/fundamentos.md` con enunciados de módulo 01 (logaritmos, conjuntos, combinatoria, grafos, lógica) | `ejercicios/propuestos/fundamentos.md` |
| [x] | Crear `propuestos/aplicaciones.md` con enunciados de módulo 05 (Kolmogorov, criptografía, cuántica, termodinámica, biología) | `ejercicios/propuestos/aplicaciones.md` |

#### 8c. Artículos nuevos sin ningún notebook

Cuatro artículos creados en la segunda ronda carecen de notebook de ejemplo o de ejercicio.

| Estado | Artículo | Notebook propuesto |
|--------|----------|--------------------|
| [x] | `03/11-oráculos-y-relativización` | `ejemplos/26-oráculos-relativización.ipynb`: simular oráculo de SAT, comparar P^SAT vs NP^SAT conceptualmente |
| [x] | `04/13-eth-seth-consecuencias` | `ejemplos/27-eth-seth-lower-bounds.ipynb`: lower bounds condicionales para LCS y Edit Distance |
| [x] | `05/07-informacion-y-biologia` | `ejemplos/28-codigo-genetico-entropia.ipynb`: calcular entropía del código genético, redundancia, información de Fisher |
| [x] | `02/14-procesos-estocasticos-y-fuentes-con-memoria` | `ejemplos/29-fuentes-con-memoria.ipynb`: fuentes de Markov de orden k, tasa de entropía, comparación con i.i.d. |

#### 8d. Ejercicios resueltos faltantes

Hay 26 artículos sin `ejercicios/resueltos/` asociado. Los de mayor impacto pedagógico:

| Estado | Tema | Artículo |
|--------|------|----------|
| [x] | Codificación aritmética | `02/13` → `resueltos/28-codificacion-aritmetica.md` |
| [x] | Procesos estocásticos y fuentes con memoria | `02/14` → `resueltos/29-procesos-estocasticos.md` |
| [x] | Oráculos y relativización | `03/11` → `resueltos/30-oráculos-y-relativización.md` |
| [x] | Aleatoriedad algorítmica (Chaitin, Martin-Löf) | `03/12` → `resueltos/31-aleatoriedad-algoritmica.md` |
| [x] | #P y conteo | `04/11` → `resueltos/32-sharp-p-y-conteo.md` |
| [x] | Complejidad de comunicación | `04/12` → `resueltos/33-complejidad-comunicacion.md` |
| [x] | ETH/SETH y consecuencias | `04/13` → `resueltos/34-eth-seth-consecuencias.md` |
| [x] | Información y biología | `05/07` → `resueltos/35-informacion-y-biologia.md` |

#### 8e. Tests automáticos en notebooks de ejemplo y ejercicios 01-16

Verificado 2026-05-14: los notebooks 06 y 12 tienen 1 celda `assert` cada uno; los 14 restantes (01-05, 07-11, 13-16) tienen cero validaciones automáticas.

| Estado | Mejora | Archivos afectados |
|--------|--------|--------------------|
| [x] | Añadir celda `assert` a notebooks de ejercicio 01-05, 07-11, 13-16 (14 notebooks sin ningún assert) | `cuadernos/ejercicios/01-*.ipynb` … `16-*.ipynb` (excluir 06 y 12 que ya tienen) |
| [x] | Añadir celda `assert` a notebooks de ejemplo seleccionados (los que implementan funciones verificables) | `cuadernos/ejemplos/` — prioridad 01, 03, 04, 08, 11, 12, 13 |

---

### 9. Recursos de referencia nuevos

| Estado | Recurso | Descripción | Archivo destino |
|--------|---------|-------------|-----------------|
| [x] | **Glosario de términos** | Definición breve de cada símbolo y concepto técnico del tutorial: entropía, KL, NP, BPP, treewidth, etc. Ordenado alfabéticamente con enlace al artículo donde se introduce. | `tutorial/referencias/glosario.md` |
| [x] | **Índice de notación matemática** | Tabla de todos los símbolos usados (H, I, K, D_KL, Σ, Π, Δ, ρ, S(ρ)…) con su definición y referencia al artículo. | `tutorial/referencias/notacion.md` |
| [x] | **Tabla de complejidad unificada** | Una única tabla que cruza: problema / clase / mejor algoritmo conocido / cota inferior / referencia. Ampliación de la tabla del artículo 05/08. | `tutorial/referencias/tabla-complejidad.md` |
| [x] | **Mapa de dependencias entre artículos** (SVG) | Grafo dirigido que muestra qué artículo requiere cuáles; generado desde los metadatos de Prerrequisitos. | `tutorial/imagenes/mapa-dependencias.svg` |

---

### 10. Mejoras de infraestructura y CI

Verificado 2026-05-14: `test_notebooks.yml` existe y ejecuta `scripts/validar_repositorio.py`. El script actual comprueba que los artículos listados en READMEs existen en disco, pero **no** valida secciones obligatorias dentro de los artículos ni comprueba enlaces internos entre archivos.

| Estado | Mejora | Descripción | Prioridad |
|--------|--------|-------------|-----------|
| [x] | **CI: validar estructura de artículos** | Extender `scripts/validar_repositorio.py` para comprobar que cada artículo tiene las secciones obligatorias (Prerrequisitos, Objetivos, Ideas clave, Véase también, Referencias) e invocar desde `test_notebooks.yml` | Alta |
| [x] | **CI: verificar enlaces internos** | Añadir paso en CI que compruebe que todos los enlaces `[texto](ruta)` dentro de los artículos apuntan a archivos que existen (habría detectado los dos enlaces rotos de `propuestos/`) | Alta |
| [x] | **GitHub Pages** | Publicar el tutorial como sitio estático con MkDocs o Quarto; añadir `mkdocs.yml` o `_quarto.yml` y configurar el flujo de despliegue | Media |
| [x] | **Exportación a PDF** | Script que genera un PDF por módulo usando Pandoc, útil para estudio offline | Baja |
| [x] | **Script `generar_mapa_dependencias.py`** | Lee los metadatos de Prerrequisitos de cada artículo y genera automáticamente el SVG del grafo de dependencias | Media |

---

### 11. Contenido avanzado — artículos opcionales

Artículos que cubren temas que quedan fuera del tutorial actual pero son extensiones naturales del nivel avanzado:

| Estado | Artículo propuesto | Módulo | Motivación |
|--------|-------------------|--------|------------|
| [x] | **Códigos de Reed-Solomon y aplicaciones** | 02 | Los LDPC y turbo son modernos, pero RS domina almacenamiento (CD, QR codes); cierra el círculo de teoría clásica |
| [x] | **Complejidad cuántica: BQP y QMA** | 04 | Extensión natural de 05/04 (información cuántica) hacia la complejidad; algoritmo de Shor, Grover |
| [x] | **Teoría de juegos e información** | 05 | Equilibrios de Nash, información asimétrica (Lemon market), mecanismos con información privada |
| [x] | **Aprendizaje profundo desde la teoría de la información** | 05 | Cuello de botella de información (Tishby), teorema PAC-Bayes, generalización en redes sobreajustadas |
| [x] | **Privacidad diferencial** | 05 | Conexión con la entropía de Rényi; protocolo de Laplace; aplicaciones prácticas en IA y datos |

---

### 12. Internacionalización y accesibilidad

| Estado | Mejora | Descripción |
|--------|--------|-------------|
| [ ] | **Resumen en inglés** de cada artículo (abstract de 3 líneas) | Permitiría indexación en buscadores internacionales y uso en contextos bilingües |
| [x] | **Texto alternativo detallado para todos los SVG** | Los 7 SVG actuales no tienen `alt` text accesible; añadir descripción en el markdown |
| [x] | **Versión ligera sin LaTeX** de los artículos más matemáticos | Para lectores que acceden desde entornos sin renderizado de fórmulas (GitHub mobile, algunos lectores RSS) |

---

## Resumen de estado (segunda ronda)

Actualizado 2026-05-14.

| Categoría | Total ítems | Completados |
|-----------|-------------|-------------|
| **Primera ronda (completada)** | **60** | **60** |
| Huecos de cobertura (8a-8e) | 19 | 19 |
| Recursos de referencia (9) | 4 | 4 |
| Infraestructura y CI (10) | 5 | 5 |
| Contenido avanzado (11) | 5 | 5 |
| Accesibilidad (12) | 3 | 1 |
| **Total segunda ronda** | **36** | **34** |
| **Total acumulado** | **96** | **94** |

---

## Tercera ronda — Sugerencias (0/12)

Huecos y mejoras detectados en la verificación del 2026-05-14.

---

### 13. Huecos detectados en la verificación

#### 13a. `referencias/por-articulo.md` desactualizado

El ítem de la primera ronda (§4 alta prioridad) lo actualizó hasta los artículos de la quinta sesión de la primera ronda (02/12, 03/09). Los artículos de la **segunda ronda** siguen sin entradas bibliográficas: 11 artículos sin referencias.

| Estado | Artículo sin referencias | Sección a añadir en `por-articulo.md` |
|--------|--------------------------|---------------------------------------|
| [x] | `02/13-codificacion-aritmetica` | Witten, Neal y Cleary (1987); Moffat, Neal y Witten (1998); Salomon (2007) |
| [x] | `02/14-procesos-estocasticos-y-fuentes-con-memoria` | Gray (1988) *Entropy and Information Theory*; Billingsley (1965) *Ergodic Theory and Information* |
| [x] | `03/10-jerarquia-aritmetica` | Rogers (1967) *Theory of Recursive Functions*; Soare (1987) *Recursively Enumerable Sets* |
| [x] | `03/11-oráculos-y-relativización` | Baker, Gill y Solovay (1975); Arora y Barak cap. 3 |
| [x] | `03/12-aleatoriedad-algoritmica` | Li y Vitányi (2008) *Kolmogorov Complexity*; Nies (2009) *Computability and Randomness* |
| [x] | `04/11-sharp-p-y-conteo` | Valiant (1979); Toda (1991); Jerrum y Sinclair (1989) |
| [x] | `04/12-complejidad-de-comunicacion` | Kushilevitz y Nisan (1997) *Communication Complexity* |
| [x] | `04/13-eth-seth-consecuencias` | Impagliazzo y Paturi (2001); Cygan et al. (2016) *Parameterized Algorithms* cap. 14 |
| [x] | `05/07-informacion-y-biologia` | Gatlin (1972); Adami (2004); Wagner (2011) |
| [x] | `05/08-mapa-de-conexiones` | No requiere nuevas fuentes; verificar que enlaza todos los artículos de la segunda ronda |
| [x] | `00/02-rutas-de-profundizacion` | Actualizar con lecturas para los temas avanzados (segunda ronda) |

#### 13b. `05/08-mapa-de-conexiones` — coherencia con la segunda ronda

El artículo de síntesis fue creado en la primera ronda. Con los 11 artículos añadidos en la segunda ronda, el mapa puede estar incompleto.

| Estado | Mejora | Archivo |
|--------|--------|---------|
| [x] | Verificar y actualizar el artículo `05/08-mapa-de-conexiones.md` para que incluya los artículos de la segunda ronda (02/13-14, 03/10-12, 04/11-13, 05/07) en la tabla de conexiones | `05-conexiones-y-aplicaciones/08-mapa-de-conexiones.md` |

---

### 14. Infraestructura — cobertura y métricas

| Estado | Mejora | Descripción | Prioridad |
|--------|--------|-------------|-----------|
| [x] | **Ampliar `scripts/estadisticas.py`** | Añadir al informe actual: (1) % de artículos con ejercicio resuelto asociado, (2) % de notebooks de ejercicio con celda `assert`, (3) artículos sin entrada en `por-articulo.md`. Convierte la cobertura en un número medible. | Alta |
| [x] | **Script `scripts/validar_enlaces.py`** | Nuevo script independiente que recorre todos los `.md` del repositorio y verifica que cada enlace relativo `[texto](ruta)` apunta a un archivo existente. Integrar en CI. Habría detectado los dos enlaces rotos de `propuestos/`. | Alta |
| [x] | **`scripts/estadisticas.py` — salida en Markdown** | Añadir opción `--md` que vuelca el informe en `ESTADISTICAS.md` (en raíz del repo) para que sea visible en GitHub sin ejecutar Python. | Baja |
| [x] | **Script `scripts/validar_asserts.py`** | Nuevo script dedicado que verifica que cada notebook de ejercicios tiene al menos una celda con `assert`; muestra cobertura y acepta `--strict` para CI. | Media |

---

### 15. Calidad de contenido — mejoras específicas

| Estado | Mejora | Descripción | Artículo afectado |
|--------|--------|-------------|-------------------|
| [x] | **Ejemplo numérico completo en `03/11`** | El artículo de oráculos y relativización es muy abstracto; añadir una traza concreta del teorema de Baker-Gill-Solovay con un oráculo simple | `03/11-oráculos-y-relativización.md` |
| [x] | **Tabla resumen de clases en `03/10`** | La jerarquía aritmética introduce muchos símbolos (Σ₁, Π₁, Δ₁, Σ₂…); añadir una tabla con nombre, definición informal, ejemplo canónico y posición en la jerarquía | `03/10-jerarquia-aritmetica.md` |
| [x] | **Conectar `02/14` con `02/12`** | El artículo de procesos estocásticos generaliza el de cadenas de Markov; añadir sección "Relación con el artículo anterior" que señale explícitamente qué se generaliza y por qué | `02/14-procesos-estocasticos-y-fuentes-con-memoria.md` |
| [x] | **Ejercicio de síntesis en `05/08`** | El artículo de cierre no tiene ejercicios propios; añadir 3-4 preguntas transversales que obliguen a conectar resultados de distintos módulos | `05/08-mapa-de-conexiones.md` |

---

## Resumen de estado (tercera ronda)

Actualizado 2026-05-14.

| Categoría | Total ítems | Completados |
|-----------|-------------|-------------|
| **Primera ronda (completada)** | **60** | **60** |
| **Segunda ronda (completada)** | **36** | **35** |
| Referencias `por-articulo.md` (13a) | 11 | 11 |
| Coherencia mapa de conexiones (13b) | 1 | 1 |
| Infraestructura métricas (14) | 4 | 4 |
| Calidad de contenido (15) | 4 | 4 |
| **Total tercera ronda** | **20** | **20** |
| **Total acumulado** | **116** | **115** |

### Pendiente (1 ítem — alcance muy alto)

| Ítem | Sección | Complejidad |
|------|---------|-------------|
| Resumen en inglés por artículo (abstract de 3 líneas × 59 artículos) | §12 | Alta (excluido explícitamente) |
