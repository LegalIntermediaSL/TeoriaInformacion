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
