# 02 - Conjuntos, funciones y relaciones

> **Dificultad:** ⭐ Básico · **Tiempo de lectura:** ~20 min


La teoría de la información, la computabilidad y la complejidad usan un lenguaje
común: conjuntos de objetos, funciones entre ellos y relaciones que expresan
propiedades. Antes de introducir modelos más formales, conviene fijar esta base.

El objetivo no es desarrollar teoría de conjuntos en profundidad, sino disponer
de una notación clara para hablar de alfabetos, cadenas, programas, grafos,
lenguajes y problemas de decisión.

## Prerrequisitos

- [Logaritmos, probabilidad y crecimiento](01-logaritmos-probabilidad-y-crecimiento.md)

## Objetivos de aprendizaje

1. Operar con conjuntos (unión, intersección, complemento, producto cartesiano).
2. Distinguir funciones inyectivas, sobreyectivas y biyectivas.
3. Comprender relaciones de equivalencia y de orden.


## Conjuntos

Un conjunto es una colección de elementos. Podemos describirlo enumerando sus
elementos:

```text
A = {0, 1}
B = {a, b, c}
```

o mediante una propiedad:

```text
P = {n : n es un número natural par}
```

La notación `x in A` indica que `x` pertenece al conjunto `A`. Si `x` no
pertenece a `A`, escribimos `x notin A`.

En este tutorial aparecerán conjuntos como:

- alfabetos de símbolos;
- conjuntos de cadenas;
- conjuntos de estados;
- conjuntos de entradas válidas;
- clases de problemas.

## Subconjuntos

Decimos que `A` es subconjunto de `B` si todo elemento de `A` también pertenece a
`B`.

```text
A subset B
```

Por ejemplo:

```text
{0, 1} subset {0, 1, 2}
```

Esta idea aparece cuando decimos que una clase de problemas está contenida en
otra. Por ejemplo, en complejidad:

```text
P subset NP
```

Esto significa que todo problema que puede resolverse eficientemente también
puede verificarse eficientemente.

## Producto cartesiano

El producto cartesiano `A x B` contiene todos los pares ordenados cuyo primer
elemento viene de `A` y cuyo segundo elemento viene de `B`.

Si:

```text
A = {0, 1}
B = {x, y}
```

entonces:

```text
A x B = {(0, x), (0, y), (1, x), (1, y)}
```

Esto permite modelar entradas compuestas. Por ejemplo, el problema de la parada
recibe un par:

```text
(programa, entrada)
```

## Funciones

Una función asigna a cada elemento de un conjunto de partida un único elemento
de un conjunto de llegada.

```text
f: A -> B
```

Si `f` toma un elemento `a` de `A`, su resultado se escribe:

```text
f(a)
```

En computación, un algoritmo puede verse como una función parcial o total sobre
sus entradas:

- total si siempre devuelve un resultado;
- parcial si para algunas entradas no termina o no produce salida.

Esta distinción será importante al estudiar decidibilidad.

## Funciones inyectivas, sobreyectivas y biyectivas

Una función es inyectiva si no colapsa dos entradas distintas en la misma salida.
Formalmente:

```text
si f(a) = f(b), entonces a = b
```

Una función es sobreyectiva si todo elemento del conjunto de llegada aparece como
salida de alguna entrada.

Una función es biyectiva si es inyectiva y sobreyectiva. En ese caso, establece
una correspondencia exacta entre dos conjuntos.

Las biyecciones permiten hablar de "tener el mismo tamaño" incluso entre
conjuntos infinitos. Esta idea aparece en computabilidad al contar programas,
cadenas y problemas posibles.

## Relaciones

Una relación entre elementos de `A` y `B` es un subconjunto de `A x B`.

Por ejemplo, si `A` es un conjunto de personas y `B` un conjunto de libros, una
relación podría indicar qué persona leyó qué libro.

En teoría de la computación, las relaciones aparecen como:

- relaciones de equivalencia;
- relaciones de orden;
- relaciones de reducción entre problemas;
- relaciones de alcanzabilidad en grafos.

## Lenguajes como conjuntos

Un alfabeto es un conjunto finito de símbolos. Si:

```text
Sigma = {0, 1}
```

entonces una cadena sobre `Sigma` es una secuencia finita de ceros y unos:

```text
0
1
00
101
1110
```

El conjunto de todas las cadenas finitas sobre `Sigma` se escribe normalmente:

```text
Sigma*
```

Un lenguaje formal es un subconjunto de `Sigma*`. Por ejemplo, el lenguaje de las
cadenas binarias con número par de unos:

```text
L = {w in {0,1}* : w tiene un número par de unos}
```

Esta forma de ver problemas como lenguajes será central en computabilidad y
complejidad.

## Problemas de decisión como lenguajes

Un problema de decisión pregunta si una entrada cumple o no una propiedad. Si
codificamos cada entrada como una cadena, el problema puede identificarse con el
conjunto de cadenas cuya respuesta es "sí".

Por ejemplo:

```text
PRIMO = {n : n codifica un número primo}
```

Decidir `PRIMO` significa construir un algoritmo que, dada una cadena, responda
si pertenece o no a ese conjunto.

## Idea para recordar

Los conjuntos describen colecciones, las funciones transforman elementos y las
relaciones comparan objetos. Con esas tres piezas podemos modelar fuentes,
programas, lenguajes y problemas.

## Ideas clave

- Un conjunto es la noción más básica de colección; operaciones como unión e intersección se usan en la descripción de clases de complejidad.
- Una función biyectiva establece una correspondencia uno a uno; las bijeaciones cuentan objetos (argumento de diagonalización de Cantor).
- Las relaciones de equivalencia particionan un conjunto en clases; son la base de los autómatas de estados equivalentes.
- El producto cartesiano A×B es el conjunto de todos los pares; modela la entrada de funciones de dos variables y tablas de verdad.
- La cardinalidad infinita (contable vs. incontable) determina la existencia de lenguajes indecidibles: hay más lenguajes que programas.


## Ejercicios

1. Da un ejemplo de conjunto finito y otro infinito.
2. Si `A = {0, 1}` y `B = {a, b, c}`, enumera los elementos de `A x B`.
3. Explica por qué un algoritmo que siempre termina puede verse como una función
   total.
4. Describe como lenguaje el problema "una cadena binaria contiene al menos un
   `1`".

## Véase también

- [Combinatoria y conteo](03-combinatoria-y-conteo.md)
- [Grafos y estructuras discretas](04-grafos-y-estructuras-discretas.md)

