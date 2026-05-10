# 14 - Teoría de la tasa-distorsión

## Contexto

Este ejercicio acompaña el artículo
[Teoría de la tasa-distorsión](../../02-teoria-informacion/09-teoria-tasa-distorsion.md).

También se puede practicar con el cuaderno
[Tasa-distorsión](../../cuadernos/ejercicios/14-tasa-distorsion.ipynb).

## Enunciado

**Parte A — Bernoulli:**

Sea X ~ Bernoulli(0.3): P(X=1) = 0.3, P(X=0) = 0.7. La función de distorsión es
el error de bit (distorsión de Hamming): d(x, x̂) = 1 si x ≠ x̂, 0 si x = x̂.

1. Calcula R(D) para D = 0, 0.1, 0.2, 0.3.
2. ¿Cuál es la distorsión de saturación D* donde R(D*) = 0?

**Parte B — Gaussiana:**

Sea X ~ N(0, σ²) con σ² = 4. Distorsión cuadrática media.

3. Calcula R(D) para D = 0.5, 1, 2, 4.
4. Un canal AWGN con capacidad C = 1 bit/uso tiene acceso a esta fuente. ¿Cuál
   es la distorsión mínima D* que puede alcanzar (separación fuente-canal)?

## Pista

**Bernoulli:** la función de tasa-distorsión es:

```text
R(D) = Hb(p) - Hb(D)  para D ≤ min(p, 1-p)
R(D) = 0               para D ≥ min(p, 1-p)
```

donde Hb(x) = -x·log₂(x) - (1-x)·log₂(1-x).

**Gaussiana:** la función de tasa-distorsión es:

```text
R(D) = ½·log₂(σ²/D)  para D ≤ σ²
R(D) = 0              para D > σ²
```

**Separación fuente-canal:** D* = σ²·2^(-2C).

## Solución

### Parte A — Bernoulli(0.3)

Hb(0.3) = -0.3·log₂(0.3) - 0.7·log₂(0.7) ≈ 0.881 bits.

La saturación ocurre en D* = min(0.3, 0.7) = 0.3.

| D    | Hb(D)  | R(D) = Hb(0.3) - Hb(D) |
|------|--------|--------------------------|
| 0.00 | 0.000  | 0.881 bits               |
| 0.10 | 0.469  | 0.412 bits               |
| 0.20 | 0.722  | 0.159 bits               |
| 0.30 | 0.881  | 0.000 bits               |

**Interpretación:** para reconstruir X con error medio ≤ 0.1 (90% de acierto)
se necesitan 0.412 bits/símbolo. Para reproducción perfecta (D=0) se necesitan
todos los 0.881 bits de entropía.

**D* = 0.3:** si se permite fallar 30% de los bits, se puede comprimir a tasa 0.
Esto tiene sentido: simplemente predecir siempre X̂ = 0 (el símbolo más probable)
da un error medio de P(X=1) = 0.3.

### Parte B — Gaussiana N(0, 4)

σ² = 4. La saturación ocurre en D* = σ² = 4 (predicción constante, R=0).

| D   | R(D) = ½·log₂(4/D) |
|-----|---------------------|
| 0.5 | ½·log₂(8) = 1.5 bits |
| 1.0 | ½·log₂(4) = 1.0 bit  |
| 2.0 | ½·log₂(2) = 0.5 bits |
| 4.0 | ½·log₂(1) = 0.0 bits |

**Interpretación:** cada bit adicional de tasa reduce la distorsión a la mitad:
pasar de 1 a 2 bits/símbolo reduce el MSE de 2 a 1, luego de 1 a 0.5.

### Parte B.4 — Separación fuente-canal

Canal AWGN con C = 1 bit/uso, fuente Gaussiana con σ² = 4:

```text
D* = σ²·2^(-2C) = 4·2^(-2) = 4·(1/4) = 1
```

La distorsión mínima alcanzable es **D* = 1** (MSE = 1). El teorema de separación
garantiza que se puede lograr sin pérdida de optimalidad codificando fuente y
canal por separado.

## Comentario

La curva R(D) marca el límite de lo que es físicamente posible: no existe ningún
código (por complicado que sea) que alcance distorsión D con menos de R(D) bits.
Esto es análogo al límite de Shannon para canales: C marca lo que es posible con
tasa arbitrariamente baja de error.

## Para seguir

Calcula R(D) para una fuente Laplace con parámetro b=1 (varianza σ²=2b²=2)
y compárala con la Gaussiana de misma varianza. ¿Cuál requiere más bits para
la misma distorsión?
