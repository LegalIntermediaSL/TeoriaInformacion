# 13 - Cadenas de Markov y tasa de entropía

## Contexto

Este ejercicio acompaña el artículo
[Cadenas de Markov y tasa de entropía](../../02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md).

También se puede practicar con el cuaderno
[Cadenas de Markov y tasa de entropía](../../cuadernos/ejemplos/20-cadenas-de-markov-tasa-entropia.ipynb).

## Enunciado

Sea una cadena de Markov binaria con matriz de transición:

```text
P = | 1-p   p |
    |  q   1-q|
```

con p = 0.2 y q = 0.4.

1. Calcula la distribución estacionaria π.
2. Calcula la tasa de entropía H̄.
3. Compara H̄ con la entropía marginal H(X₁) = H(π). ¿Cuál es mayor?
4. ¿Para qué valores de p y q la cadena es i.i.d. (H̄ = H(X₁))?

## Pista

La distribución estacionaria satisface π·P = π con π₀ + π₁ = 1:

```text
π₀ = q / (p + q)
π₁ = p / (p + q)
```

La tasa de entropía es:

```text
H̄ = π₀ · H(fila 0) + π₁ · H(fila 1)
   = π₀ · Hb(p) + π₁ · Hb(q)
```

donde Hb(x) = -x·log₂(x) - (1-x)·log₂(1-x) es la entropía binaria.

## Solución

### 1. Distribución estacionaria

Con p = 0.2 y q = 0.4:

```text
π₀ = q / (p + q) = 0.4 / 0.6 = 2/3 ≈ 0.6667
π₁ = p / (p + q) = 0.2 / 0.6 = 1/3 ≈ 0.3333
```

Verificación: π₀·(1-p) + π₁·q = 2/3·0.8 + 1/3·0.4 = 0.533 + 0.133 = 0.667 = π₀ ✓

### 2. Tasa de entropía

Entropía binaria de cada fila:

```text
Hb(p) = Hb(0.2) = -0.2·log₂(0.2) - 0.8·log₂(0.8)
                 ≈ 0.2·2.322 + 0.8·0.322
                 ≈ 0.464 + 0.258 ≈ 0.722 bits

Hb(q) = Hb(0.4) = -0.4·log₂(0.4) - 0.6·log₂(0.6)
                 ≈ 0.4·1.322 + 0.6·0.737
                 ≈ 0.529 + 0.442 ≈ 0.971 bits
```

Tasa de entropía:

```text
H̄ = π₀·Hb(p) + π₁·Hb(q)
   = (2/3)·0.722 + (1/3)·0.971
   ≈ 0.481 + 0.324
   ≈ 0.805 bits/símbolo
```

### 3. Comparación con H(X₁)

La entropía marginal (con π₀ = 2/3, π₁ = 1/3):

```text
H(π) = Hb(1/3) = -1/3·log₂(1/3) - 2/3·log₂(2/3)
                ≈ 1/3·1.585 + 2/3·0.585
                ≈ 0.528 + 0.390 ≈ 0.918 bits
```

Comparación:

```text
H̄ ≈ 0.805 bits  <  H(X₁) ≈ 0.918 bits
```

La tasa de entropía es **menor** que la entropía marginal: la memoria reduce la
incertidumbre por símbolo. Esto siempre ocurre: H̄ ≤ H(X₁), con igualdad solo
si la cadena es sin memoria.

### 4. Condición para que H̄ = H(X₁)

La cadena es i.i.d. cuando el estado actual no da información sobre el siguiente,
es decir, cuando las filas de P son iguales:

```text
p = q  →  ambas filas son [1-p, p] = [q, 1-q]
```

En ese caso, π₀ = π₁ = 1/2 y las transiciones son independientes del estado actual.
También ocurre trivialmente cuando p = 0 o p = 1 (la cadena es determinista, H̄ = 0).

## Comentario

La desigualdad H̄ ≤ H(X₁) es el fundamento teórico de que los compresores que
explotan la memoria (LZ78, contextos de orden k) siempre hacen mejor que los que
asumen independencia (Huffman sobre símbolos individuales).

## Para seguir

Fija p + q = 0.5 y varía p entre 0 y 0.5. ¿Para qué valor de p se maximiza H̄?
¿Coincide con la cadena simétrica p = q = 0.25?
