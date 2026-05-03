# 03 - Códigos prefijo y longitud media

## Contexto

Este ejercicio acompaña los artículos:

- [Codificación de fuente](../../02-teoria-informacion/03-codificacion-de-fuente.md)
- [Códigos correctores de errores](../../02-teoria-informacion/06-codigos-correctores-de-errores.md)

También se puede practicar con los cuadernos:

- [Códigos prefijo y longitud media](../../cuadernos/ejemplos/04-codigos-prefijo-longitud-media.ipynb)
- [Práctica de códigos prefijo](../../cuadernos/ejercicios/03-practica-codigos-prefijo.ipynb)

## Enunciado

Considera la fuente:

```text
P(A) = 0.5
P(B) = 0.25
P(C) = 0.125
P(D) = 0.125
```

y el código:

```text
A -> 0
B -> 10
C -> 110
D -> 111
```

1. Comprueba si el código es prefijo.
2. Calcula la suma de Kraft.
3. Calcula la longitud media.
4. Compara con un código fijo de 2 bits por símbolo.

## Pista

Un código es prefijo si ninguna palabra de código aparece al principio de otra.

La suma de Kraft es:

```text
sum_i 2^(-l_i)
```

La longitud media es:

```text
L = sum_x p(x) l(x)
```

## Solución

Las longitudes son:

```text
l(A) = 1
l(B) = 2
l(C) = 3
l(D) = 3
```

### Propiedad prefijo

La palabra `0` no es prefijo de ninguna otra, porque todas las demás empiezan
por `1`. La palabra `10` no es prefijo de `110` ni de `111`. Y `110`, `111` son
distintas y de igual longitud.

Por tanto, el código es prefijo.

### Suma de Kraft

```text
2^(-1) + 2^(-2) + 2^(-3) + 2^(-3)
= 1/2 + 1/4 + 1/8 + 1/8
= 1
```

La suma de Kraft igual a 1 indica que el árbol de código está completo.

### Longitud media

```text
L = 0.5*1 + 0.25*2 + 0.125*3 + 0.125*3
  = 0.5 + 0.5 + 0.375 + 0.375
  = 1.75 bits/símbolo
```

Un código fijo para cuatro símbolos usa:

```text
2 bits/símbolo
```

Este código variable ahorra:

```text
2 - 1.75 = 0.25 bits/símbolo
```

## Comentario

El ahorro aparece porque el símbolo más frecuente recibe la palabra más corta.
Este es el principio que algoritmos como Huffman explotan de forma sistemática.

## Para seguir

Cambia la fuente para que los cuatro símbolos sean equiprobables. ¿Sigue siendo
ventajoso el código variable?
