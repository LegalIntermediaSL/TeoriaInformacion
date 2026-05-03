# Cuadernos Jupyter

Espacio para cuadernos Jupyter asociados al tutorial.

La carpeta está pensada para ejemplos ejecutables, ejercicios guiados y
experimentos pequeños que acompañen los artículos teóricos.

## Organización

- [Ejemplos](ejemplos/): cuadernos demostrativos con cálculos, simulaciones y
  visualizaciones.
- [Ejercicios](ejercicios/): cuadernos para practicar conceptos del tutorial,
  con enunciados, celdas preparadas y soluciones cuando proceda.

Para preparar un entorno local, consulta la guía de
[ejecución local](ejecucion-local.md).

Los ejercicios resueltos en Markdown están en
[tutorial/ejercicios/resueltos](../ejercicios/resueltos/README.md).

## Cuadernos disponibles

### Ejemplos

- [Entropía de distribuciones discretas](ejemplos/01-entropia-distribuciones.ipynb)
- [Comparación de crecimiento asintótico](ejemplos/02-crecimiento-asintotico.ipynb)
- [Canal binario simétrico](ejemplos/03-canal-binario-simetrico.ipynb)
- [Códigos prefijo y longitud media](ejemplos/04-codigos-prefijo-longitud-media.ipynb)
- [Información mutua y entropía condicional](ejemplos/05-informacion-mutua-entropia-condicional.ipynb)
- [Compresión y redundancia](ejemplos/06-compresion-y-redundancia.ipynb)
- [Divergencia KL y entropía cruzada](ejemplos/07-divergencia-kl-entropia-cruzada.ipynb)
- [Código de repetición y corrección de errores](ejemplos/08-codigos-repeticion-correccion.ipynb)
- [Entropía conjunta y condicional](ejemplos/09-entropia-conjunta-condicional.ipynb)
- [Autómata finito para paridad](ejemplos/10-automata-finito-paridad.ipynb)

### Ejercicios

- [Entropía y fuentes discretas](ejercicios/01-entropia-y-fuentes-discretas.ipynb)
- [Verificación de certificados en NP](ejercicios/02-verificacion-certificados-np.ipynb)
- [Práctica de códigos prefijo](ejercicios/03-practica-codigos-prefijo.ipynb)
- [Búsqueda exhaustiva para SAT](ejercicios/04-busqueda-sat.ipynb)
- [Grafos y alcanzabilidad](ejercicios/05-grafos-alcanzabilidad.ipynb)
- [Memoria en BFS y DFS](ejercicios/06-memoria-bfs-dfs.ipynb)
- [Tablas de verdad](ejercicios/07-tablas-de-verdad.ipynb)
- [Medición de complejidad temporal](ejercicios/08-medicion-complejidad-temporal.ipynb)

## Convenciones recomendadas

- Nombrar los cuadernos con prefijo numérico y tema, por ejemplo
  `01-entropia-moneda-sesgada.ipynb`.
- Indicar al inicio el módulo del tutorial relacionado.
- Separar claramente explicación, código y ejercicios.
- Mantener las dependencias al mínimo: Python estándar, `numpy`, `matplotlib` y
  bibliotecas similares solo cuando aporten claridad.
- Evitar salidas pesadas o archivos generados innecesarios.

## Temas iniciales sugeridos

- Cálculo de entropía para distribuciones discretas.
- Simulación de una moneda sesgada.
- Comparación de órdenes de crecimiento.
- Verificación de certificados para problemas en NP.
- Exploración de compresión y redundancia en cadenas simples.
