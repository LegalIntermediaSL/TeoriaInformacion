# 04 - Complejidad espacial

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


La complejidad temporal mide cuántos pasos necesita un algoritmo. La complejidad
espacial mide cuánta memoria utiliza.

Ambas medidas son importantes. Un algoritmo puede ser rápido pero consumir mucha
memoria, o ser lento pero usar muy poco espacio.

## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Definir las clases PSPACE, L y NL y sus relaciones con P y NP.
2. Enunciar el teorema de Savitch: NPSPACE = PSPACE.
3. Demostrar que PSPACE-completitud mediante el problema TQBF.


## Espacio como recurso

El espacio suele medirse en función del tamaño de la entrada `n`.

Por ejemplo:

```text
O(1)       espacio constante
O(log n)   espacio logarítmico
O(n)       espacio lineal
O(n^2)     espacio cuadrático
```

No siempre se cuenta la memoria usada para almacenar la entrada original. A
menudo se mide el espacio adicional de trabajo.

## Tiempo frente a espacio

Tiempo y espacio pueden intercambiarse. Guardar resultados intermedios puede
ahorrar tiempo, pero consumir más memoria. Recalcularlos puede ahorrar memoria,
pero aumentar el tiempo.

Este tipo de intercambio aparece en:

- programación dinámica;
- búsqueda en grafos;
- algoritmos de ordenación;
- verificación de pruebas;
- resolución de problemas combinatorios.

## Clases espaciales

Algunas clases importantes son:

```text
L       problemas decidibles en espacio logarítmico
PSPACE  problemas decidibles en espacio polinómico
EXPSPACE problemas decidibles en espacio exponencial
```

`PSPACE` contiene problemas que pueden resolverse usando una cantidad de memoria
polinómica, aunque quizá necesiten mucho tiempo.

## Relación con P y NP

Sabemos que:

```text
P subset PSPACE
NP subset PSPACE
```

La intuición para `NP subset PSPACE` es que una búsqueda exponencial puede
realizarse reutilizando memoria. Aunque pruebe muchísimos candidatos, no necesita
guardarlos todos a la vez.

No se sabe si `P = PSPACE`. Se cree que `PSPACE` contiene problemas más difíciles
que los de `P`.

## Problemas PSPACE-completos

Un problema PSPACE-completo es, informalmente, uno de los más difíciles dentro de
`PSPACE`.

Ejemplos clásicos aparecen en:

- lógica cuantificada;
- juegos de tablero generalizados;
- planificación;
- verificación de sistemas.

Muchos juegos se vuelven PSPACE-completos cuando se generalizan a tableros de
tamaño arbitrario.

## Búsqueda en profundidad y memoria

La búsqueda en profundidad puede explorar grafos grandes usando poca memoria, ya
que solo necesita mantener el camino actual y algunos datos de control.

La búsqueda en anchura, en cambio, guarda una frontera completa de nodos por
nivel. Esto puede consumir mucha memoria si el número de vecinos crece rápido.

Así, dos algoritmos que buscan en el mismo espacio pueden tener perfiles de
memoria muy distintos.

## Savitch

El teorema de Savitch muestra una relación sorprendente entre espacio
determinista y no determinista:

```text
NSPACE(f(n)) subset SPACE(f(n)^2)
```

De forma informal, el no determinismo no ahorra tanto espacio como podría
parecer. Este resultado es una pieza central de la teoría de complejidad
espacial.

## Idea para recordar

La memoria también es un límite computacional. La complejidad espacial permite
estudiar problemas donde el obstáculo principal no es solo cuánto tarda un
algoritmo, sino cuánta información necesita mantener mientras trabaja.

## Ideas clave

- PSPACE es la clase de problemas decidibles con espacio polinomial; contiene NP y co-NP.
- El teorema de Savitch: NPSPACE = PSPACE; el no determinismo solo cuadra el espacio.
- TQBF (verdad de fórmulas booleanas cuantificadas) es PSPACE-completo; generaliza SAT añadiendo cuantificadores ∀.
- L y NL son las clases de espacio logarítmico; NL = co-NL por el teorema de Immerman-Szelepcsényi.
- La jerarquía de espacio es estricta (DSPACE(s(n)) ⊊ DSPACE(s'(n)) si s' ≫ s), a diferencia del tiempo donde el análogo es abierto.


## Ejercicios

1. Da un ejemplo de algoritmo que use espacio lineal.
2. ¿Por qué `P` está contenido en `PSPACE`?
3. Explica por qué BFS puede usar más memoria que DFS.
4. ¿Qué significa que un problema sea PSPACE-completo?

## Véase también

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Circuitos booleanos](07-circuitos-booleanos.md)

<!-- nav-start -->

---
← [03 - SAT y 3-SAT](03-sat-y-3-sat.md) · [05 - Complejidad temporal de algoritmos](05-complejidad-temporal-de-algoritmos.md) →

<!-- nav-end -->
