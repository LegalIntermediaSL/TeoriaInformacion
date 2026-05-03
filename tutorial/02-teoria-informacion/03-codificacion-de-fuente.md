# 03 - Codificación de fuente

La codificación de fuente estudia cómo representar mensajes de una fuente usando
símbolos de un código, normalmente bits. Su pregunta principal es:

```text
¿cuántos bits necesitamos, en promedio, para describir los mensajes?
```

La entropía marca un límite teórico. La codificación busca acercarse a ese
límite con esquemas concretos.

## Fuentes y mensajes

Una fuente produce símbolos o mensajes con cierta distribución de probabilidad.
Si los símbolos no son igualmente probables, podemos aprovechar esa estructura.

Por ejemplo:

```text
P(A) = 0.5
P(B) = 0.25
P(C) = 0.125
P(D) = 0.125
```

El símbolo `A` aparece con más frecuencia que `C` o `D`. Tiene sentido asignarle
una palabra de código más corta.

## Códigos de longitud fija

En un código de longitud fija, todos los símbolos usan el mismo número de bits.
Para cuatro símbolos podemos usar:

```text
A -> 00
B -> 01
C -> 10
D -> 11
```

Cada símbolo cuesta 2 bits, sin importar su probabilidad.

Los códigos de longitud fija son simples, pero no siempre eficientes si la
fuente tiene símbolos muy frecuentes y otros muy raros.

## Códigos de longitud variable

En un código de longitud variable, las palabras de código pueden tener longitudes
distintas:

```text
A -> 0
B -> 10
C -> 110
D -> 111
```

Aquí `A` usa 1 bit, `B` usa 2 bits y `C`, `D` usan 3 bits. Si `A` es frecuente,
la longitud promedio puede bajar.

## Longitud media

La longitud media de un código es:

```text
L = sum_x p(x) l(x)
```

donde `p(x)` es la probabilidad del símbolo `x` y `l(x)` la longitud de su
palabra de código.

Para la fuente anterior y el código variable:

```text
L = 0.5*1 + 0.25*2 + 0.125*3 + 0.125*3 = 1.75 bits
```

El código fijo costaba 2 bits por símbolo. El código variable aprovecha la
redundancia de la fuente.

## Códigos prefijo

Un código prefijo es un código donde ninguna palabra de código es prefijo de
otra.

El código:

```text
A -> 0
B -> 10
C -> 110
D -> 111
```

es prefijo. Al leer bits de izquierda a derecha, sabemos cuándo termina cada
palabra sin necesitar separadores.

En cambio:

```text
A -> 0
B -> 01
```

no es prefijo, porque `0` es prefijo de `01`.

## Desigualdad de Kraft

Para un código prefijo binario con longitudes `l_1, l_2, ..., l_n`, se cumple:

```text
sum_i 2^(-l_i) <= 1
```

Esta condición se llama desigualdad de Kraft. Da una forma de comprobar si un
conjunto de longitudes puede corresponder a un código prefijo.

No construye el código por sí sola, pero indica si las longitudes caben en un
árbol binario de decodificación.

## Huffman

El algoritmo de Huffman construye códigos prefijo óptimos para una distribución
discreta cuando se codifica símbolo a símbolo.

Su intuición es asignar palabras más largas a símbolos menos probables y palabras
más cortas a símbolos más probables. Lo hace combinando iterativamente los dos
símbolos menos probables.

Huffman no contradice la entropía: se acerca al límite, pero la longitud media
puede quedar por encima de `H(X)`.

## Teorema de codificación de fuente

El teorema de codificación de fuente de Shannon dice, de forma intuitiva, que la
entropía es el límite fundamental de la compresión sin pérdida.

Para mensajes largos generados por una fuente, podemos codificar cerca de:

```text
H(X) bits por símbolo
```

pero no podemos hacerlo, en promedio, por debajo de esa cantidad sin perder
información.

## Idea para recordar

La codificación de fuente convierte regularidad probabilística en ahorro de
bits. La entropía indica el límite; los códigos concretos intentan acercarse a
él.

## Ejercicios

1. Calcula la longitud media del código fijo de cuatro símbolos.
2. Comprueba que el código `A -> 0`, `B -> 10`, `C -> 110`, `D -> 111` es
   prefijo.
3. Calcula la suma de Kraft para las longitudes `1, 2, 3, 3`.
4. Explica por qué una fuente uniforme ofrece menos margen para códigos de
   longitud variable.
