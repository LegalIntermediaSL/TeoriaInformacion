# Tutorial

Estructura base del tutorial sobre teoría de la información, computabilidad y
complejidad computacional.

El tutorial está organizado como una ruta progresiva: empieza con el contexto y
las herramientas matemáticas necesarias, avanza hacia los conceptos centrales de
información y computación, y termina con conexiones entre áreas.

## Recorrido sugerido

1. [Presentación](00-presentacion/README.md)
2. [Fundamentos matemáticos](01-fundamentos-matematicos/README.md)
3. [Teoría de la información](02-teoria-informacion/README.md)
4. [Computabilidad](03-computabilidad/README.md)
5. [Complejidad computacional](04-complejidad-computacional/README.md)
6. [Conexiones y aplicaciones](05-conexiones-y-aplicaciones/README.md)

## Ruta de estudio

### Nivel 1 - Orientación y herramientas

- [Mapa del territorio](00-presentacion/01-mapa-del-territorio.md)
- [Logaritmos, probabilidad y crecimiento](01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md)
- [Conjuntos, funciones y relaciones](01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md)
- [Combinatoria y conteo](01-fundamentos-matematicos/03-combinatoria-y-conteo.md)
- [Grafos y estructuras discretas](01-fundamentos-matematicos/04-grafos-y-estructuras-discretas.md)
- [Lógica booleana y proposicional](01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md)

Práctica recomendada:

- [Comparación de crecimiento asintótico](cuadernos/ejemplos/02-crecimiento-asintotico.ipynb)
- [Grafos y alcanzabilidad](cuadernos/ejercicios/05-grafos-alcanzabilidad.ipynb)
- [Tablas de verdad](cuadernos/ejercicios/07-tablas-de-verdad.ipynb)
- [Complejidad temporal básica](ejercicios/resueltos/06-complejidad-temporal-basica.md)

### Nivel 2 - Información, codificación y canales

- [Entropía: medir incertidumbre](02-teoria-informacion/01-entropia-incertidumbre.md)
- [Entropía conjunta y condicional](02-teoria-informacion/07-entropia-conjunta-y-condicional.md)
- [Información mutua](02-teoria-informacion/02-informacion-mutua.md)
- [Codificación de fuente](02-teoria-informacion/03-codificacion-de-fuente.md)
- [Canales discretos y capacidad](02-teoria-informacion/04-canales-discretos-y-capacidad.md)
- [Divergencia KL y entropía cruzada](02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Códigos correctores de errores](02-teoria-informacion/06-codigos-correctores-de-errores.md)
- [Teorema de Shannon y capacidad de canal](02-teoria-informacion/08-teorema-de-shannon-capacidad.md)
- [Teoría de la tasa-distorsión](02-teoria-informacion/09-teoria-tasa-distorsion.md)
- [Entropía diferencial y fuentes continuas](02-teoria-informacion/10-entropia-diferencial.md)
- [Códigos LDPC y Turbo: hacia la capacidad de Shannon](02-teoria-informacion/11-codigos-ldpc-y-turbo.md)
- [Cadenas de Markov y tasa de entropía](02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md)

Práctica recomendada:

- [Entropía de distribuciones discretas](cuadernos/ejemplos/01-entropia-distribuciones.ipynb)
- [Información mutua y entropía condicional](cuadernos/ejemplos/05-informacion-mutua-entropia-condicional.ipynb)
- [Códigos prefijo y longitud media](cuadernos/ejemplos/04-codigos-prefijo-longitud-media.ipynb)
- [Código de repetición y corrección de errores](cuadernos/ejemplos/08-codigos-repeticion-correccion.ipynb)
- [Cadenas de Markov y tasa de entropía](cuadernos/ejemplos/20-cadenas-de-markov-tasa-entropia.ipynb)
- [Tasa-distorsión](cuadernos/ejercicios/14-tasa-distorsion.ipynb)
- [Entropía de fuentes discretas](ejercicios/resueltos/01-entropia-fuentes-discretas.md)
- [Tasa-distorsión: ejercicios resueltos](ejercicios/resueltos/14-tasa-distorsion.md)

### Nivel 3 - Computabilidad y complejidad

- [El problema de la parada](03-computabilidad/01-problema-de-la-parada.md)
- [Decidibilidad y reconocibilidad](03-computabilidad/02-decidibilidad-y-reconocibilidad.md)
- [Reducciones e indecidibilidad](03-computabilidad/03-reducciones-e-indecidibilidad.md)
- [Máquinas de Turing](03-computabilidad/04-maquinas-de-turing.md)
- [Autómatas finitos y lenguajes regulares](03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md)
- [Gramáticas y la jerarquía de Chomsky](03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md)
- [Universalidad y autorreferencia](03-computabilidad/07-universalidad-y-autorreferencia.md)
- [Autómatas de pila y lenguajes independientes del contexto](03-computabilidad/09-automatas-de-pila-y-lenguajes-contexto-libre.md)
- [P, NP y NP-completitud](04-complejidad-computacional/01-p-np-y-np-completitud.md)
- [SAT y 3-SAT](04-complejidad-computacional/03-sat-y-3-sat.md)
- [Complejidad parametrizada](04-complejidad-computacional/10-complejidad-parametrizada.md)
- [Complejidad temporal de algoritmos](04-complejidad-computacional/05-complejidad-temporal-de-algoritmos.md)
- [Circuitos booleanos y complejidad de circuitos](04-complejidad-computacional/07-circuitos-booleanos.md)
- [Complejidad aleatoria](04-complejidad-computacional/08-complejidad-aleatoria.md)

Práctica recomendada:

- [Simulación de máquinas de Turing](cuadernos/ejemplos/13-maquina-de-turing-simulacion.ipynb)
- [Simulación de circuitos booleanos](cuadernos/ejemplos/15-circuitos-booleanos-simulacion.ipynb)
- [Autómata finito para paridad](cuadernos/ejemplos/10-automata-finito-paridad.ipynb)
- [Autómatas de pila: PDA y CYK](cuadernos/ejemplos/21-automatas-de-pila.ipynb)
- [Máquinas de Turing básicas](cuadernos/ejercicios/11-maquinas-de-turing-basicas.ipynb)
- [Autómatas y lenguajes formales](cuadernos/ejercicios/12-automatas-y-lenguajes.ipynb)
- [Complejidad aleatoria y tests probabilísticos](cuadernos/ejercicios/13-complejidad-aleatoria.ipynb)
- [Búsqueda exhaustiva para SAT](cuadernos/ejercicios/04-busqueda-sat.ipynb)
- [Medición de complejidad temporal](cuadernos/ejercicios/08-medicion-complejidad-temporal.ipynb)
- [Máquinas de Turing: ejercicios resueltos](ejercicios/resueltos/11-maquinas-de-turing.md)
- [Autómatas finitos: ejercicios resueltos](ejercicios/resueltos/12-automatas-finitos.md)
- [SAT y verificación de asignaciones](ejercicios/resueltos/05-sat-verificacion.md)

### Nivel 4 - Conexiones y ampliaciones

- [Complejidad de Kolmogorov](05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)
- [Criptografía y complejidad](05-conexiones-y-aplicaciones/02-criptografia-y-complejidad.md)
- [Aprendizaje automático e información](05-conexiones-y-aplicaciones/03-aprendizaje-automatico-e-informacion.md)
- [Información cuántica](05-conexiones-y-aplicaciones/04-informacion-cuantica.md)
- [Información en el aprendizaje estadístico](05-conexiones-y-aplicaciones/05-informacion-en-aprendizaje.md)
- [Información y termodinámica](05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md)

Práctica recomendada:

- [Compresión y redundancia](cuadernos/ejemplos/06-compresion-y-redundancia.ipynb)
- [Divergencia KL y entropía cruzada](cuadernos/ejemplos/07-divergencia-kl-entropia-cruzada.ipynb)
- [Cadenas de Markov y tasa de entropía](cuadernos/ejemplos/14-cadenas-de-markov-entropia.ipynb)
- [Compresión universal: LZ78](cuadernos/ejemplos/16-compresion-lz78.ipynb)
- [Cadenas de Markov y tasa de entropía](cuadernos/ejemplos/20-cadenas-de-markov-tasa-entropia.ipynb)
- [Información y termodinámica](cuadernos/ejemplos/22-informacion-y-termodinamica.ipynb)
- [Simulación de códigos LDPC](cuadernos/ejemplos/18-codigos-ldpc-simulacion.ipynb)
- [Estimación de información mutua](cuadernos/ejemplos/19-informacion-mutua-estimacion.ipynb)
- [Complejidad parametrizada: k-Vertex Cover](cuadernos/ejercicios/16-complejidad-parametrizada.ipynb)

## Material de apoyo

- [Cuadernos Jupyter](cuadernos/README.md)
- [Ejercicios](ejercicios/README.md)
- [Referencias](referencias/README.md)
- [Referencias por artículo](referencias/por-articulo.md)

## Artículos iniciales

- [Mapa del territorio: información, cálculo y dificultad](00-presentacion/01-mapa-del-territorio.md)
- [Logaritmos, probabilidad y crecimiento](01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md)
- [Conjuntos, funciones y relaciones](01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md)
- [Combinatoria y conteo](01-fundamentos-matematicos/03-combinatoria-y-conteo.md)
- [Grafos y estructuras discretas](01-fundamentos-matematicos/04-grafos-y-estructuras-discretas.md)
- [Lógica booleana y proposicional](01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md)
- [Entropía: medir incertidumbre](02-teoria-informacion/01-entropia-incertidumbre.md)
- [Información mutua](02-teoria-informacion/02-informacion-mutua.md)
- [Codificación de fuente](02-teoria-informacion/03-codificacion-de-fuente.md)
- [Canales discretos y capacidad](02-teoria-informacion/04-canales-discretos-y-capacidad.md)
- [Divergencia KL y entropía cruzada](02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Códigos correctores de errores](02-teoria-informacion/06-codigos-correctores-de-errores.md)
- [Entropía conjunta y condicional](02-teoria-informacion/07-entropia-conjunta-y-condicional.md)
- [Teorema de Shannon y capacidad de canal](02-teoria-informacion/08-teorema-de-shannon-capacidad.md)
- [Teoría de la tasa-distorsión](02-teoria-informacion/09-teoria-tasa-distorsion.md)
- [Entropía diferencial y fuentes continuas](02-teoria-informacion/10-entropia-diferencial.md)
- [Códigos LDPC y Turbo: hacia la capacidad de Shannon](02-teoria-informacion/11-codigos-ldpc-y-turbo.md)
- [Cadenas de Markov y tasa de entropía](02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md)
- [El problema de la parada](03-computabilidad/01-problema-de-la-parada.md)

- [Decidibilidad y reconocibilidad](03-computabilidad/02-decidibilidad-y-reconocibilidad.md)
- [Reducciones e indecidibilidad](03-computabilidad/03-reducciones-e-indecidibilidad.md)
- [Máquinas de Turing](03-computabilidad/04-maquinas-de-turing.md)
- [Autómatas finitos y lenguajes regulares](03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md)
- [Gramáticas y la jerarquía de Chomsky](03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md)
- [Universalidad y autorreferencia](03-computabilidad/07-universalidad-y-autorreferencia.md)
- [Complejidad descriptiva](03-computabilidad/08-complejidad-descriptiva.md)
- [Autómatas de pila y lenguajes independientes del contexto](03-computabilidad/09-automatas-de-pila-y-lenguajes-contexto-libre.md)
- [P, NP y NP-completitud](04-complejidad-computacional/01-p-np-y-np-completitud.md)
- [Reducciones polinómicas](04-complejidad-computacional/02-reducciones-polinomicas.md)
- [SAT y 3-SAT](04-complejidad-computacional/03-sat-y-3-sat.md)
- [Complejidad espacial](04-complejidad-computacional/04-complejidad-espacial.md)
- [Complejidad temporal de algoritmos](04-complejidad-computacional/05-complejidad-temporal-de-algoritmos.md)
- [Aproximación y heurísticas](04-complejidad-computacional/06-aproximacion-y-heuristicas.md)
- [Circuitos booleanos y complejidad de circuitos](04-complejidad-computacional/07-circuitos-booleanos.md)
- [Complejidad aleatoria](04-complejidad-computacional/08-complejidad-aleatoria.md)
- [El teorema PCP y la dureza de aproximación](04-complejidad-computacional/09-teorema-pcp.md)
- [Complejidad parametrizada](04-complejidad-computacional/10-complejidad-parametrizada.md)
- [Complejidad de Kolmogorov](05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)
- [Criptografía y complejidad](05-conexiones-y-aplicaciones/02-criptografia-y-complejidad.md)
- [Aprendizaje automático e información](05-conexiones-y-aplicaciones/03-aprendizaje-automatico-e-informacion.md)
- [Información cuántica](05-conexiones-y-aplicaciones/04-informacion-cuantica.md)
- [Información en el aprendizaje estadístico](05-conexiones-y-aplicaciones/05-informacion-en-aprendizaje.md)
- [Información y termodinámica](05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md)

## Convenciones de cada módulo

Cada módulo podrá incorporar:

- objetivos de aprendizaje;
- conceptos clave;
- desarrollo teórico;
- ejemplos guiados;
- ejercicios;
- referencias específicas.

## Estado

Esta carpeta contiene la estructura inicial. Los contenidos se irán completando
de forma incremental.
