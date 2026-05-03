# 04 - Grafos y alcanzabilidad

## Contexto

Este ejercicio acompaña el artículo
[Grafos y estructuras discretas](../../01-fundamentos-matematicos/04-grafos-y-estructuras-discretas.md).

También se puede practicar con el cuaderno
[Grafos y alcanzabilidad](../../cuadernos/ejercicios/05-grafos-alcanzabilidad.ipynb).

## Enunciado

Considera el grafo dirigido:

```text
A -> B
A -> C
B -> D
C -> E
E -> D
D -> F
```

1. ¿Existe un camino de `A` a `F`?
2. ¿Existe un camino de `C` a `B`?
3. Da un recorrido BFS desde `A`.
4. Explica por qué conviene marcar vértices visitados.

## Pista

En BFS se exploran primero los vecinos a distancia 1, luego distancia 2, y así
sucesivamente.

## Solución

### Camino de `A` a `F`

Sí existe. Un camino posible es:

```text
A -> B -> D -> F
```

También existe:

```text
A -> C -> E -> D -> F
```

### Camino de `C` a `B`

No existe con las aristas dadas. Desde `C` podemos ir a:

```text
C -> E -> D -> F
```

pero no aparece ninguna arista que lleve hacia `B`.

### Recorrido BFS desde `A`

Un recorrido BFS posible es:

```text
A, B, C, D, E, F
```

Dependiendo del orden en que se almacenen los vecinos, `D` y `E` podrían
aparecer en otro orden. Lo importante es que BFS explora por niveles.

Niveles desde `A`:

```text
distancia 0: A
distancia 1: B, C
distancia 2: D, E
distancia 3: F
```

### Vértices visitados

Conviene marcar visitados para evitar repetir trabajo y para no caer en ciclos.

Si un grafo contiene:

```text
A -> B
B -> A
```

una búsqueda sin conjunto de visitados podría alternar para siempre entre `A` y
`B`.

## Comentario

La alcanzabilidad es una pregunta simple, pero aparece en muchos lugares:
análisis de programas, rutas de red, dependencias, autómatas y espacios de
estados.

## Para seguir

Añade una arista `F -> C`. ¿Cambia la respuesta sobre `A -> F`? ¿Qué cambia para
una búsqueda sin visitados?
