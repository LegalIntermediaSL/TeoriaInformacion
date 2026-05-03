# 04 - Grafos y estructuras discretas

Un grafo es una forma de representar objetos y relaciones entre ellos. Aparece
en rutas de comunicación, dependencias entre tareas, redes, autómatas, estados de
un programa, reducciones y muchos problemas clásicos de complejidad.

Los grafos son importantes porque convierten preguntas abstractas en estructuras
visuales y discretas.

## Vértices y aristas

Un grafo está formado por:

- vértices, que representan objetos;
- aristas, que representan conexiones.

Por ejemplo, si los vértices son ciudades, una arista puede representar una
carretera entre dos ciudades.

```text
V = {A, B, C}
E = {(A, B), (B, C)}
```

Aquí `A` está conectado con `B`, y `B` con `C`.

## Grafos no dirigidos

En un grafo no dirigido, las aristas no tienen orientación. La conexión entre
`A` y `B` puede recorrerse en ambos sentidos.

```text
A -- B
```

Estos grafos sirven para modelar relaciones simétricas:

- amistad;
- conexión física;
- compatibilidad;
- pertenencia a un mismo grupo.

## Grafos dirigidos

En un grafo dirigido, las aristas tienen orientación:

```text
A -> B
```

Esto significa que podemos ir de `A` a `B`, pero no necesariamente de `B` a `A`.

Los grafos dirigidos modelan:

- enlaces web;
- dependencias;
- transiciones de estados;
- llamadas entre funciones;
- relaciones de reducción.

## Caminos

Un camino es una secuencia de vértices conectados por aristas.

En el grafo:

```text
A -> B -> C
```

hay un camino de `A` a `C`.

El problema de alcanzabilidad pregunta si existe un camino entre dos vértices.
Es una de las preguntas más básicas sobre grafos y aparece en computabilidad,
verificación y complejidad.

## Grado

En un grafo no dirigido, el grado de un vértice es el número de aristas que lo
tocan.

En un grafo dirigido distinguimos:

- grado de entrada: cuántas aristas llegan;
- grado de salida: cuántas aristas salen.

El grado ayuda a medir conectividad local. En redes grandes puede revelar nodos
centrales o cuellos de botella.

## Representaciones

Un grafo puede representarse de varias formas.

Una lista de adyacencia guarda, para cada vértice, sus vecinos:

```text
A: B, C
B: C
C:
```

Una matriz de adyacencia usa una tabla donde la entrada `(i, j)` indica si hay
arista de `i` a `j`.

La elección de representación afecta el coste de los algoritmos.

## Búsqueda en grafos

Dos recorridos clásicos son:

- búsqueda en anchura, o BFS;
- búsqueda en profundidad, o DFS.

BFS explora primero los vecinos cercanos. DFS sigue un camino hasta donde puede
antes de retroceder.

Ambos permiten responder preguntas como:

```text
¿es t alcanzable desde s?
```

## Grafos en complejidad

Muchos problemas NP-completos se formulan con grafos:

- `CLIQUE`: existe un conjunto de vértices todos conectados entre sí;
- `VERTEX-COVER`: existe un conjunto pequeño que toca todas las aristas;
- `HAMILTONIAN-CYCLE`: existe un ciclo que visita cada vértice una vez.

Los grafos son un lenguaje común para construir reducciones.

## Grafos como espacios de estados

Un programa, juego o sistema puede verse como un grafo de estados. Cada vértice
es una configuración posible, y cada arista es una transición válida.

Esta idea conecta con:

- máquinas de Turing;
- autómatas;
- planificación;
- búsqueda;
- verificación de sistemas.

## Idea para recordar

Un grafo representa objetos y conexiones. Muchas preguntas sobre cálculo,
comunicación y dificultad pueden convertirse en preguntas sobre caminos,
conectividad o estructuras dentro de grafos.

## Ejercicios

1. Dibuja un grafo dirigido con cuatro vértices y cinco aristas.
2. Da un ejemplo cotidiano de grafo no dirigido.
3. Explica la diferencia entre lista de adyacencia y matriz de adyacencia.
4. ¿Por qué un espacio de estados puede representarse como grafo?
