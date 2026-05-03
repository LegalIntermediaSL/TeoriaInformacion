# 02 - Información mutua y dependencia

## Contexto

Este ejercicio acompaña los artículos:

- [Información mutua](../../02-teoria-informacion/02-informacion-mutua.md)
- [Entropía conjunta y condicional](../../02-teoria-informacion/07-entropia-conjunta-y-condicional.md)

También se puede explorar con el cuaderno
[Información mutua y entropía condicional](../../cuadernos/ejemplos/05-informacion-mutua-entropia-condicional.ipynb).

## Enunciado

Sean `X` e `Y` variables binarias. Compara estos dos casos:

Caso 1:

```text
X e Y son monedas equilibradas independientes.
```

Caso 2:

```text
Y = X, y X es una moneda equilibrada.
```

Para cada caso:

1. Calcula `H(X)`.
2. Calcula `H(X | Y)`.
3. Calcula `I(X; Y)`.
4. Explica qué significa el resultado.

## Pista

Usa:

```text
I(X; Y) = H(X) - H(X | Y)
```

Piensa primero si observar `Y` ayuda a predecir `X`.

## Solución

En ambos casos, `X` es una moneda equilibrada:

```text
H(X) = 1 bit
```

### Caso 1: independencia

Si `X` e `Y` son independientes, conocer `Y` no cambia la incertidumbre sobre
`X`.

```text
H(X | Y) = H(X) = 1 bit
```

Entonces:

```text
I(X; Y) = H(X) - H(X | Y)
        = 1 - 1
        = 0 bits
```

No comparten información.

### Caso 2: copia perfecta

Si `Y = X`, observar `Y` revela completamente `X`.

```text
H(X | Y) = 0 bits
```

Entonces:

```text
I(X; Y) = H(X) - H(X | Y)
        = 1 - 0
        = 1 bit
```

`Y` contiene toda la información necesaria para conocer `X`.

## Comentario

La información mutua no mide cuánta entropía tiene una variable por separado.
Mide cuánta incertidumbre de una variable se reduce al observar la otra.

Dos variables pueden tener entropía alta y, aun así, información mutua cero si
son independientes.

## Para seguir

Construye un caso intermedio donde `Y` sea una copia de `X` con probabilidad de
error `0.1`.
