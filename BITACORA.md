# Bitácora del proyecto

Registro de avances, decisiones y próximos pasos del repositorio
`TeoriaInformacion`.

La bitácora sirve para dejar constancia del razonamiento detrás de la evolución
del proyecto: qué se incorpora, por qué se organiza de una determinada manera y
qué temas conviene abordar después.

## Cómo usar esta bitácora

- Registrar decisiones de estructura, alcance o enfoque pedagógico.
- Anotar avances relevantes en contenidos, ejemplos, ejercicios o referencias.
- Dejar pendientes claros para continuar el trabajo en sesiones posteriores.
- Mantener las entradas en orden cronológico inverso, con la más reciente arriba.

## Entradas

### 2026-05-09 - Tercera ronda: entropía diferencial, PCP, complejidad descriptiva y quines

Avances:

- Artículo `02-teoria-informacion/10-entropia-diferencial.md`: entropía diferencial
  $h(X) = -\int f\log f$, máxima entropía Gaussiana, EPI, información de Fisher,
  canal Gaussiano aditivo, AEP continuo.
- Artículo `03-computabilidad/08-complejidad-descriptiva.md`: FO = AC0, P = FO+LFP,
  teorema de Fagin (NP = ∃SO), PSPACE = FO+PFP, lenguajes regulares = MSO.
- Artículo `04-complejidad-computacional/09-teorema-pcp.md`: PCP$(log n, 1)$ = NP,
  Max-3SAT y ratio 7/8, gap amplification, UGC, SNARKs.
- Notebook `cuadernos/ejemplos/17-entropia-diferencial-gaussiana.ipynb`: entropías
  analíticas, comparación misma varianza, invarianza por escala, capacidad Gaussiana,
  estimación numérica.
- Notebook `cuadernos/ejercicios/14-tasa-distorsion.ipynb`: R(D) para Bernoulli y
  Gaussiana, comparación de distribuciones, separación fuente-canal.
- Notebook `cuadernos/ejercicios/15-universalidad-y-quines.ipynb`: quines en Python,
  teorema de Rice experimental, diagonalización de Cantor, puntos fijos numéricos.
- Actualización de todos los índices README y BITACORA.md.

Decisiones:

- La complejidad descriptiva es avanzada pero cierra el módulo de computabilidad
  con la perspectiva lógica (NP = ∃SO), que conecta directamente con las gramáticas.
- El teorema PCP es el resultado más importante no cubierto en complejidad; justifica
  los límites de aproximación de los mejores algoritmos conocidos.
- El notebook de quines es experimental y pedagógico: permite observar la autorreferencia
  directamente en Python sin necesidad de implementar una UTM completa.

Pendientes:

- Artículo sobre complejidad parametrizada (FPT, W[1]-hardness, kernelización).
- Notebook sobre el teorema AEP empírico para fuentes continuas.
- Ejercicios resueltos sobre complejidad aleatoria y tasa-distorsión.

### 2026-05-09 - Expansión: complejidad aleatoria, tasa-distorsión, universalidad y LZ78

Segunda ronda de ampliación en la misma sesión.

Avances:

- Artículo `04-complejidad-computacional/08-complejidad-aleatoria.md`: BPP, RP,
  ZPP, amplificación, Miller-Rabin, Schwartz-Zippel, IP=PSPACE, desaleatorización.
- Artículo `02-teoria-informacion/09-teoria-tasa-distorsion.md`: función $R(D)$,
  ejemplos Bernoulli y Gaussiana, dualidad con capacidad, JPEG/MP3.
- Artículo `03-computabilidad/07-universalidad-y-autorreferencia.md`: UTM, teorema
  del punto fijo, diagonalización del problema de la parada, teorema de Rice,
  conexión con incompletitud de Gödel.
- Notebook `cuadernos/ejemplos/15-circuitos-booleanos-simulacion.ipynb`: clase
  Circuit con AND/OR/NOT/XOR; semisumador, sumador de 4 bits, DNF, árbol XOR,
  comparativa tamaño-profundidad.
- Notebook `cuadernos/ejemplos/16-compresion-lz78.ipynb`: implementación
  completa de LZ78, convergencia a la entropía para fuentes i.i.d. y Markov,
  crecimiento del diccionario como $n/\log n$.
- Notebook `cuadernos/ejercicios/13-complejidad-aleatoria.ipynb`: ejercicios
  para Miller-Rabin (test de primalidad) y Freivalds (verificación matricial)
  con soluciones de referencia y estudio de amplificación.
- Actualización de todos los índices README y BITACORA.md.

Decisiones:

- LZ78 en lugar de LZ77 porque su estructura de diccionario explícito es más
  sencilla de implementar y analizar pedagógicamente; la convergencia teórica
  es la misma.
- Tasa-distorsión completa el módulo 02 con la compresión con pérdida, que era
  el hueco más relevante tras el teorema de canal.
- Universalidad y autorreferencia formaliza la UTM y el teorema de Rice, que son
  necesarios para cerrar el módulo 03 con rigor.

Pendientes:

- Ejercicio resuelto sobre complejidad aleatoria (Miller-Rabin manual).
- Notebook sobre el teorema de Shannon: verificación empírica de la capacidad.
- Artículo sobre complejidad de descripción (Kolmogorov) — ya existe en 05 pero
  podría ampliarse con la conexión a compresión universal.

### 2026-05-09 - Nuevos artículos, notebooks y ejercicios resueltos

Ampliación del tutorial con contenidos que cubrían huecos identificados en la
sesión anterior.

Avances:

- Artículo `02-teoria-informacion/08-teorema-de-shannon-capacidad.md`: teorema
  de codificación de canal, BSC, BEC, AEP, Shannon-Hartley, separación
  fuente-canal.
- Artículo `03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md`: tipos 0-3,
  gramáticas libres de contexto, autómatas de pila, lemas de bombeo.
- Artículo `04-complejidad-computacional/07-circuitos-booleanos.md`: tamaño y
  profundidad, P/poly, AC0, NC, teorema de Håstad (paridad ∉ AC0), TC0.
- Notebook `cuadernos/ejemplos/13-maquina-de-turing-simulacion.ipynb`:
  simulador completo con trazas paso a paso; palíndromos, paridad, unario.
- Notebook `cuadernos/ejemplos/14-cadenas-de-markov-entropia.ipynb`: clase
  MarkovChain, distribución estacionaria, tasa de entropía, estimación empírica.
- Notebook `cuadernos/ejercicios/11-maquinas-de-turing-basicas.ipynb`:
  ejercicios para $a^n b^n$ y $0^*1^*$ con soluciones de referencia y conteo
  de pasos.
- Notebook `cuadernos/ejercicios/12-automatas-y-lenguajes.ipynb`: clase DFA
  con run/trace; DFA para terminar en '01', divisibilidad mod 3, pumping lemma.
- Ejercicio resuelto `ejercicios/resueltos/11-maquinas-de-turing.md`: diseño
  completo con tablas de transición, trazas y análisis de complejidad.
- Ejercicio resuelto `ejercicios/resueltos/12-automatas-finitos.md`: DFA
  mínimos, pumping lemma para $a^n b^n$, minimización de estados.
- Actualización de todos los índices README (cuadernos, ejercicios, módulos
  02-04, tutorial principal) y de la bitácora.

Decisiones:

- El teorema de Shannon de codificación de canal era el artículo central que
  faltaba en el módulo 02; complementa los artículos de capacidad y codificación
  ya existentes.
- Los circuitos booleanos completan el módulo 04 con la perspectiva no uniforme
  (P/poly) y la jerarquía de circuitos (AC0, NC, TC0).
- La jerarquía de Chomsky cierra la conexión entre autómatas y gramáticas en el
  módulo 03.
- Los notebooks de ejercicios 11 y 12 siguen el mismo patrón de los anteriores:
  esqueleto de implementación + solución de referencia descomentable.

Pendientes:

- Añadir ejercicios resueltos sobre circuitos booleanos (ejercicio 13).
- Incorporar un notebook de ejemplo sobre el teorema de Shannon (prueba empírica
  de la cota de capacidad).
- Ampliar referencias bibliográficas para los tres nuevos artículos.

### 2026-05-04 - Ejercicios avanzados, referencias y notebooks

Se ejecuta la siguiente mejora pedagógica del tutorial: ampliar ejercicios
resueltos, asociar referencias específicas por artículo y añadir notebooks más
avanzados.

Avances:

- Redacción de ejercicios resueltos sobre decidibilidad, reducciones,
  canales/capacidad y divergencia KL.
- Creación del mapa `tutorial/referencias/por-articulo.md`.
- Enlace del mapa de referencias desde el índice de referencias y el índice del
  tutorial.
- Creación de notebooks avanzados sobre Huffman, Hamming (7,4), dovetailing de
  reconocedores y selección de modelos con entropía cruzada.
- Actualización de índices de cuadernos, ejercicios y referencias.

Decisiones:

- Mantener las referencias por artículo en un archivo central para evitar repetir
  bibliografía en cada capítulo.
- Priorizar notebooks avanzados que conecten teoría con algoritmos concretos:
  codificación óptima, corrección de errores, reconocibilidad y modelado
  probabilístico.
- Conservar implementaciones con biblioteca estándar de Python para facilitar la
  ejecución local.

Pendientes:

- Añadir ejercicios resueltos sobre máquinas de Turing y autómatas.
- Añadir un artículo específico sobre Huffman y otro sobre Hamming si la ruta
  requiere más profundidad teórica.
- Incorporar recursos abiertos con enlaces en la bibliografía.

### 2026-05-03 - Ruta de estudio y ejercicios resueltos

Se consolida el material existente con una ruta de estudio más explícita y una
primera colección de ejercicios resueltos.

Avances:

- Creación de la carpeta `tutorial/ejercicios/resueltos`.
- Redacción de ejercicios resueltos sobre entropía, información mutua, códigos
  prefijo, grafos, SAT y complejidad temporal.
- Actualización del `README.md` principal para enlazar ejercicios resueltos.
- Reorganización del índice del tutorial con una ruta por niveles.
- Enlace entre artículos, cuadernos y ejercicios dentro del recorrido sugerido.
- Actualización del README de ejercicios con colecciones disponibles y nuevos
  pendientes.

Decisiones:

- Priorizar soluciones comentadas sobre más contenido nuevo para reforzar el uso
  pedagógico del repositorio.
- Organizar la ruta de estudio en cuatro niveles: fundamentos, información,
  computabilidad/complejidad y conexiones.
- Mantener los ejercicios resueltos en Markdown para que sean fáciles de revisar
  desde GitHub sin ejecutar notebooks.

Pendientes:

- Ampliar ejercicios resueltos para máquinas de Turing, decidibilidad y
  reducciones.
- Añadir ejercicios resueltos sobre canales, KL y códigos correctores.
- Incorporar referencias específicas al final de los artículos principales.

### 2026-05-03 - Lógica, autómatas y medición temporal

Se amplía el tutorial con nuevas piezas formales y notebooks de apoyo para
conectar lógica, entropía conjunta, modelos finitos y análisis temporal.

Avances:

- Redacción del artículo `05-logica-booleana-y-proposicional.md`.
- Redacción del artículo `07-entropia-conjunta-y-condicional.md`.
- Redacción del artículo `05-automatas-finitos-y-lenguajes-regulares.md`.
- Redacción de los artículos `05-complejidad-temporal-de-algoritmos.md` y
  `06-aproximacion-y-heuristicas.md`.
- Redacción del artículo `04-informacion-cuantica.md`.
- Creación de cuadernos sobre entropía conjunta y autómatas finitos.
- Creación de cuadernos de ejercicios sobre tablas de verdad y medición temporal.
- Actualización de índices generales, módulos y sección de cuadernos.

Decisiones:

- Introducir lógica booleana como fundamento explícito para SAT y circuitos.
- Añadir autómatas finitos antes de seguir hacia modelos más potentes.
- Separar complejidad temporal, aproximación y heurísticas para distinguir
  garantías formales de estrategias prácticas.
- Presentar información cuántica como una ruta de ampliación conceptual.

Pendientes:

- Crear ejercicios resueltos para lógica booleana, autómatas y SAT.
- Añadir un artículo específico sobre circuitos booleanos.
- Añadir un cuaderno introductorio de compuertas lógicas.

### 2026-05-03 - Grafos, KL, corrección de errores y espacio

Se amplía el tutorial con nuevos temas de soporte matemático, información,
computabilidad, complejidad y aplicaciones, junto con cuadernos asociados.

Avances:

- Redacción del artículo `04-grafos-y-estructuras-discretas.md`.
- Redacción de los artículos `05-divergencia-kl-y-entropia-cruzada.md` y
  `06-codigos-correctores-de-errores.md`.
- Redacción del artículo `04-maquinas-de-turing.md`.
- Redacción del artículo `04-complejidad-espacial.md`.
- Redacción del artículo `03-aprendizaje-automatico-e-informacion.md`.
- Creación de cuadernos de ejemplo sobre divergencia KL y códigos de repetición.
- Creación de cuadernos de ejercicios sobre alcanzabilidad en grafos y memoria
  en BFS/DFS.
- Actualización de índices generales, índices de módulos y sección de cuadernos.

Decisiones:

- Añadir grafos como puente hacia problemas de complejidad y recorridos
  algorítmicos.
- Introducir KL y entropía cruzada antes de profundizar más en aprendizaje
  automático.
- Presentar corrección de errores con repetición antes de códigos más
  sofisticados.
- Conectar complejidad espacial con experimentos simples de frontera en BFS y
  DFS.

Pendientes:

- Añadir un artículo sobre complejidad temporal de algoritmos básicos.
- Crear un cuaderno de máquinas de Turing simples o autómatas finitos.
- Añadir soluciones comentadas para los cuadernos de ejercicios.

### 2026-05-03 - Segunda expansión de tutorial y cuadernos

Se continúa la ampliación del material con artículos de desarrollo y una nueva
tanda de cuadernos de ejemplo y práctica.

Avances:

- Redacción del artículo `03-combinatoria-y-conteo.md`.
- Redacción de los artículos `03-codificacion-de-fuente.md` y
  `04-canales-discretos-y-capacidad.md`.
- Redacción del artículo `03-reducciones-e-indecidibilidad.md`.
- Redacción del artículo `03-sat-y-3-sat.md`.
- Redacción del artículo `02-criptografia-y-complejidad.md`.
- Creación de los cuadernos de ejemplo sobre información mutua y compresión.
- Creación de los cuadernos de ejercicios sobre códigos prefijo y SAT.
- Inclusión de `requirements.txt` y guía de ejecución local para Jupyter.
- Actualización de índices generales, índices de módulos y sección de cuadernos.

Decisiones:

- Profundizar en los conceptos que conectan directamente con los notebooks:
  conteo, codificación, canales, satisfacibilidad y seguridad computacional.
- Mantener los cuadernos centrados en implementaciones pequeñas, transparentes y
  modificables por la persona lectora.
- Añadir una guía de entorno sin imponer herramientas pesadas de publicación.

Pendientes:

- Añadir soluciones comentadas para algunos ejercicios.
- Incorporar referencias específicas al final de cada artículo.
- Crear un cuaderno sobre códigos correctores de errores.
- Crear un cuaderno sobre búsqueda exhaustiva frente a heurísticas simples.

### 2026-05-03 - Nuevos cuadernos de canales, códigos y NP

Se amplía la colección de cuadernos Jupyter para cubrir ejemplos prácticos de
teoría de la información y ejercicios guiados de complejidad.

Avances:

- Creación del cuaderno `03-canal-binario-simetrico.ipynb`.
- Creación del cuaderno `04-codigos-prefijo-longitud-media.ipynb`.
- Creación del cuaderno de ejercicios `01-entropia-y-fuentes-discretas.ipynb`.
- Creación del cuaderno de ejercicios
  `02-verificacion-certificados-np.ipynb`.
- Actualización de los índices de ejemplos, ejercicios y cuadernos.

Decisiones:

- Usar implementaciones pequeñas con Python estándar para que los notebooks sean
  fáciles de ejecutar en entornos mínimos.
- Mantener `matplotlib` como mejora opcional en los cuadernos con gráficas.
- Separar claramente notebooks demostrativos y notebooks de práctica.

Pendientes:

- Añadir un cuaderno sobre información mutua y entropía condicional.
- Añadir un cuaderno sobre compresión y redundancia en cadenas.
- Crear una guía breve de ejecución local para Jupyter.

### 2026-05-03 - Expansión inicial de artículos y notebooks

Se amplía el tutorial con contenidos de segundo nivel y con los primeros
cuadernos Jupyter demostrativos.

Avances:

- Redacción de un artículo de fundamentos sobre conjuntos, funciones y
  relaciones.
- Redacción de un artículo de teoría de la información sobre información mutua.
- Redacción de un artículo de computabilidad sobre decidibilidad y
  reconocibilidad.
- Redacción de un artículo de complejidad sobre reducciones polinómicas.
- Redacción de un artículo de conexiones sobre complejidad de Kolmogorov.
- Creación de un cuaderno de ejemplo para calcular entropía en distribuciones
  discretas.
- Creación de un cuaderno de ejemplo para comparar órdenes de crecimiento
  asintótico.
- Actualización de índices de módulos y de la sección de cuadernos.
- Inclusión de `.gitignore` para evitar checkpoints, entornos locales y archivos
  generados habituales.

Decisiones:

- Ampliar primero los conceptos que actúan como puentes entre módulos:
  lenguajes, información compartida, reconocibilidad, reducciones y compresión
  algorítmica.
- Mantener notebooks sin salidas guardadas para que el repositorio siga ligero.
- Usar solo Python estándar en el núcleo de los cuadernos y tratar `matplotlib`
  como dependencia opcional.

Pendientes:

- Añadir ejercicios resueltos asociados a los nuevos artículos.
- Crear notebooks de práctica en `tutorial/cuadernos/ejercicios`.
- Asociar referencias específicas a cada artículo nuevo.

### 2026-05-03 - Carpeta para cuadernos Jupyter

Se crea un espacio específico para cuadernos Jupyter dentro del tutorial.

Avances:

- Creación de la carpeta `tutorial/cuadernos`.
- Separación inicial entre `tutorial/cuadernos/ejemplos` y
  `tutorial/cuadernos/ejercicios`.
- Inclusión de README orientativos para definir convenciones y posibles temas.
- Enlace a los cuadernos desde el índice principal del tutorial.

Decisiones:

- Ubicar los cuadernos dentro de `tutorial` para mantener juntos teoría,
  ejercicios, ejemplos y material ejecutable.
- Separar ejemplos demostrativos y ejercicios prácticos desde el inicio.

Pendientes:

- Crear los primeros cuadernos `.ipynb`.
- Definir dependencias mínimas para ejecutar los ejemplos.
- Añadir indicaciones de entorno cuando se incorporen notebooks reales.

### 2026-05-03 - Primeros artículos del tutorial

Se inicia la redacción de contenidos del tutorial con un primer conjunto de
artículos introductorios.

Avances:

- Redacción del artículo de presentación sobre el mapa general del territorio.
- Redacción de un artículo de fundamentos sobre logaritmos, probabilidad y
  crecimiento asintótico.
- Redacción de un artículo de teoría de la información sobre entropía e
  incertidumbre.
- Redacción de un artículo de computabilidad sobre el problema de la parada.
- Redacción de un artículo de complejidad sobre P, NP y NP-completitud.
- Actualización de los índices de los módulos para enlazar los nuevos artículos.

Decisiones:

- Empezar con artículos cortos, autónomos y conectados entre sí.
- Mantener una estructura pedagógica común: intuición, formulación, ejemplos,
  idea para recordar y ejercicios.
- Priorizar temas que funcionen como puerta de entrada a cada área principal.

Pendientes:

- Ampliar cada módulo con artículos de segundo nivel.
- Añadir soluciones o pistas para los ejercicios propuestos.
- Crear ejercicios transversales que conecten información, computabilidad y
  complejidad.

### 2026-05-03 - Estructura base del tutorial

Se crea la carpeta `tutorial` como espacio principal para desarrollar la ruta de
aprendizaje del repositorio.

Avances:

- Creación del índice general del tutorial en `tutorial/README.md`.
- Definición de módulos numerados para una lectura progresiva.
- Creación de carpetas para presentación, fundamentos matemáticos, teoría de la
  información, computabilidad, complejidad computacional, conexiones y
  aplicaciones.
- Creación de espacios de apoyo para ejercicios y referencias.
- Enlace al tutorial desde el `README.md` principal.

Decisiones:

- Usar numeración en las carpetas para preservar el orden pedagógico.
- Separar ejercicios y referencias como material transversal.
- Mantener cada módulo con un `README.md` inicial que describa objetivos,
  contenidos previstos, ejemplos y resultado esperado.

Pendientes:

- Desarrollar el contenido completo de cada módulo.
- Crear un índice detallado de capítulos por módulo.
- Añadir ejercicios resueltos y no resueltos.
- Conectar referencias específicas con los temas de cada sección.

### 2026-05-03 - Inicio de la estructura documental

Se establece el repositorio como un espacio de información, notas y tutoriales
sobre teoría de la información, computabilidad y complejidad computacional.

Avances:

- Creación de una portada inicial del proyecto en `README.md`.
- Definición del alcance general del repositorio.
- Identificación de las áreas principales: teoría de la información,
  computabilidad, complejidad computacional y conexiones entre ellas.
- Creación de esta bitácora para documentar decisiones y evolución del trabajo.
- Creación del changelog para registrar cambios relevantes del proyecto.

Pendientes:

- Crear un índice progresivo de contenidos.
- Empezar los primeros capítulos introductorios.
- Incorporar ejercicios, ejemplos y referencias bibliográficas.
