# 10 - KL y entropía cruzada

## Contexto

Este ejercicio acompaña el artículo
[Divergencia KL y entropía cruzada](../../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md).

También se puede practicar con el cuaderno
[Divergencia KL y entropía cruzada](../../cuadernos/ejemplos/07-divergencia-kl-entropia-cruzada.ipynb).

## Enunciado

Sea la distribución real:

```text
P(A) = 0.5
P(B) = 0.5
```

y dos modelos:

```text
Q1(A) = 0.5, Q1(B) = 0.5
Q2(A) = 0.9, Q2(B) = 0.1
```

1. Calcula `H(P)`.
2. Calcula `H(P, Q1)` y `D_KL(P || Q1)`.
3. Calcula `H(P, Q2)` y `D_KL(P || Q2)`.
4. Interpreta qué modelo es mejor para codificar datos generados por `P`.

## Pista

Usa:

```text
H(P) = - sum_x P(x) log2 P(x)
H(P, Q) = - sum_x P(x) log2 Q(x)
D_KL(P || Q) = H(P, Q) - H(P)
```

## Solución

### Entropía de `P`

Como `P` es uniforme sobre dos símbolos:

```text
H(P) = 1 bit
```

### Modelo `Q1`

`Q1` coincide exactamente con `P`.

```text
H(P, Q1) = -0.5 log2(0.5) - 0.5 log2(0.5)
         = 1 bit
```

Entonces:

```text
D_KL(P || Q1) = H(P, Q1) - H(P)
              = 1 - 1
              = 0 bits
```

No hay coste extra por usar `Q1`.

### Modelo `Q2`

Calculamos:

```text
H(P, Q2) = -0.5 log2(0.9) - 0.5 log2(0.1)
```

Usando aproximaciones:

```text
log2(0.9) ≈ -0.152
log2(0.1) ≈ -3.322
```

Entonces:

```text
H(P, Q2) ≈ -0.5(-0.152) - 0.5(-3.322)
         ≈ 0.076 + 1.661
         ≈ 1.737 bits
```

La divergencia KL:

```text
D_KL(P || Q2) = H(P, Q2) - H(P)
              ≈ 1.737 - 1
              ≈ 0.737 bits
```

### Interpretación

`Q1` es mejor modelo para datos generados por `P`, porque coincide con la
distribución real. `Q2` espera que `A` aparezca mucho más que `B`, así que paga
un coste extra cuando los datos reales son equilibrados.

## Comentario

La divergencia KL puede entenderse como exceso de longitud media de código. Si
el modelo probabilístico se equivoca, la codificación se vuelve menos eficiente.

## Para seguir

Calcula `D_KL(Q2 || P)` y compárala con `D_KL(P || Q2)`.
