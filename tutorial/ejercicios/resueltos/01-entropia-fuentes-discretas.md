# 01 - Entropía de fuentes discretas

## Contexto

Este ejercicio acompaña los artículos:

- [Entropía: medir incertidumbre](../../02-teoria-informacion/01-entropia-incertidumbre.md)
- [Logaritmos, probabilidad y crecimiento](../../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md)

También se puede practicar con el cuaderno
[Entropía de distribuciones discretas](../../cuadernos/ejemplos/01-entropia-distribuciones.ipynb).

## Enunciado

Considera tres fuentes discretas:

```text
A = {0: 1}
B = {0: 1/2, 1: 1/2}
C = {a: 1/2, b: 1/4, c: 1/4}
```

1. Calcula la entropía de cada fuente.
2. Ordénalas de menor a mayor incertidumbre.
3. Explica por qué una fuente con más símbolos no siempre tiene más entropía.

## Pista

Usa:

```text
H(X) = - sum_x p(x) log2 p(x)
```

Recuerda que:

```text
log2(1) = 0
log2(1/2) = -1
log2(1/4) = -2
```

## Solución

Para la fuente `A`:

```text
H(A) = -1 log2(1) = 0 bits
```

La fuente siempre produce el mismo resultado. No hay incertidumbre.

Para la fuente `B`:

```text
H(B) = -(1/2 log2(1/2) + 1/2 log2(1/2))
     = -(1/2(-1) + 1/2(-1))
     = 1 bit
```

Para la fuente `C`:

```text
H(C) = -(1/2 log2(1/2) + 1/4 log2(1/4) + 1/4 log2(1/4))
     = -(1/2(-1) + 1/4(-2) + 1/4(-2))
     = 1.5 bits
```

Orden:

```text
A < B < C
```

## Comentario

La cantidad de símbolos posibles importa, pero también importan sus
probabilidades. Una fuente con muchos símbolos puede tener baja entropía si casi
siempre produce el mismo símbolo.

Por ejemplo:

```text
{a: 0.99, b: 0.01}
```

tiene dos símbolos, pero mucha menos incertidumbre que una moneda equilibrada.

## Para seguir

Modifica la distribución `C` para que tenga tres símbolos pero entropía menor que
`B`.
