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
