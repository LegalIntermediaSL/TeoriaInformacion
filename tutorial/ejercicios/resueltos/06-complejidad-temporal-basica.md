# 06 - Complejidad temporal básica

## Contexto

Este ejercicio acompaña el artículo
[Complejidad temporal de algoritmos](../../04-complejidad-computacional/05-complejidad-temporal-de-algoritmos.md).

También se puede practicar con el cuaderno
[Medición de complejidad temporal](../../cuadernos/ejercicios/08-medicion-complejidad-temporal.ipynb).

## Enunciado

Clasifica el coste asintótico de los siguientes fragmentos.

Fragmento A:

```text
para i desde 1 hasta n:
    imprimir i
```

Fragmento B:

```text
para i desde 1 hasta n:
    para j desde 1 hasta n:
        imprimir i, j
```

Fragmento C:

```text
mientras n > 1:
    n = n / 2
```

Fragmento D:

```text
para cada subconjunto S de {1, ..., n}:
    evaluar S
```

## Pista

Cuenta cuántas veces se ejecuta la operación principal en función de `n`.

## Solución

### Fragmento A

El bucle se ejecuta `n` veces.

```text
O(n)
```

### Fragmento B

El bucle externo se ejecuta `n` veces. Por cada iteración, el bucle interno se
ejecuta `n` veces.

Total:

```text
n * n = n^2
```

Coste:

```text
O(n^2)
```

### Fragmento C

Cada iteración divide `n` entre 2.

Después de `k` pasos:

```text
n / 2^k
```

El proceso termina cuando esto llega a 1. Por tanto:

```text
2^k ≈ n
k ≈ log2(n)
```

Coste:

```text
O(log n)
```

### Fragmento D

Un conjunto de `n` elementos tiene:

```text
2^n
```

subconjuntos. Si evaluamos cada uno:

```text
O(2^n)
```

## Comentario

La diferencia entre `O(n^2)` y `O(2^n)` puede ser pequeña para `n` pequeño, pero
enorme para `n` grande. Este es el motivo por el que la búsqueda exhaustiva se
vuelve impracticable rápidamente.

## Para seguir

Clasifica un algoritmo con tres bucles anidados y compáralo con `O(2^n)` para
valores pequeños de `n`.
