# 28 - Codificación aritmética

## Contexto

Este ejercicio acompaña el artículo
[Codificación aritmética](../../02-teoria-informacion/13-codificacion-aritmetica.md).

## Enunciado

**Parte A — Codificación:**

Sea la fuente con tres símbolos: $P(a) = 0.5$, $P(b) = 0.3$, $P(c) = 0.2$.

1. Define los intervalos acumulados iniciales para los símbolos $a$, $b$ y $c$.
2. Codifica la secuencia `"abc"` usando codificación aritmética. Muestra el intervalo tras cada símbolo.
3. ¿Cuál es el número de bits necesario para representar el intervalo final? Compara con la entropía $H \cdot 3$.

**Parte B — Decodificación:**

4. Dado el número $x = 0.534$ y la distribución anterior, decodifica los tres primeros símbolos de la secuencia.
5. Explica por qué la codificación aritmética puede superar a Huffman en eficiencia para secuencias cortas.

## Pista

**Intervalos acumulados:** si los símbolos son $s_1, s_2, s_3$ con probabilidades $p_1, p_2, p_3$, los intervalos son $[0, p_1)$, $[p_1, p_1+p_2)$, $[p_1+p_2, 1)$.

**Actualización del intervalo:** si el intervalo actual es $[L, H)$ y el símbolo $s$ tiene intervalo $[l_s, h_s)$, el nuevo intervalo es $[L + (H-L) \cdot l_s,\ L + (H-L) \cdot h_s)$.

**Bits necesarios:** $\lceil \log_2(1/\text{ancho final}) \rceil + 1$.

## Solución

### Parte A — Codificación

#### 1. Intervalos acumulados iniciales

| Símbolo | Probabilidad | Intervalo $[L_s, H_s)$ |
|---------|-------------|----------------------|
| $a$     | 0.5         | $[0.0, 0.5)$         |
| $b$     | 0.3         | $[0.5, 0.8)$         |
| $c$     | 0.2         | $[0.8, 1.0)$         |

#### 2. Codificación de `"abc"`

**Estado inicial:** $[L, H) = [0.0, 1.0)$, ancho $= 1.0$.

**Símbolo $a$ (intervalo $[0.0, 0.5)$):**

$$L' = 0.0 + 1.0 \times 0.0 = 0.0$$
$$H' = 0.0 + 1.0 \times 0.5 = 0.5$$

Intervalo: $[0.0, 0.5)$, ancho $= 0.5$.

**Símbolo $b$ (intervalo $[0.5, 0.8)$):**

$$L' = 0.0 + 0.5 \times 0.5 = 0.25$$
$$H' = 0.0 + 0.5 \times 0.8 = 0.40$$

Intervalo: $[0.25, 0.40)$, ancho $= 0.15$.

**Símbolo $c$ (intervalo $[0.8, 1.0)$):**

$$L' = 0.25 + 0.15 \times 0.8 = 0.25 + 0.12 = 0.37$$
$$H' = 0.25 + 0.15 \times 1.0 = 0.40$$

**Intervalo final:** $[0.37, 0.40)$, ancho $= 0.03$.

#### 3. Bits necesarios

$$\text{bits} = \left\lceil \log_2\!\left(\frac{1}{0.03}\right) \right\rceil + 1 = \lceil 5.06 \rceil + 1 = 6 + 1 = 7 \text{ bits}$$

**Entropía $\times 3$:**

$$H = -(0.5 \log_2 0.5 + 0.3 \log_2 0.3 + 0.2 \log_2 0.2) \approx 1.485 \text{ bits/símbolo}$$
$$3 \times H \approx 4.46 \text{ bits}$$

La codificación aritmética usa 7 bits (con overhead de implementación), mientras que el mínimo teórico es $\approx 4.46$ bits. Para secuencias más largas, el overhead relativo tiende a 0.

### Parte B — Decodificación

#### 4. Decodificación de $x = 0.534$

**Paso 1:** ¿En qué intervalo cae $x = 0.534$?
- $a$: $[0.0, 0.5)$ → 0.534 ≥ 0.5, **no**.
- $b$: $[0.5, 0.8)$ → 0.5 ≤ 0.534 < 0.8, **sí**. Símbolo decodificado: $b$.

Actualizar: $x' = (0.534 - 0.5) / 0.3 = 0.034 / 0.3 \approx 0.1133$.

**Paso 2:** ¿En qué intervalo cae $x' = 0.1133$?
- $a$: $[0.0, 0.5)$ → **sí**. Símbolo decodificado: $a$.

Actualizar: $x'' = 0.1133 / 0.5 = 0.2267$.

**Paso 3:** ¿En qué intervalo cae $x'' = 0.2267$?
- $a$: $[0.0, 0.5)$ → **sí**. Símbolo decodificado: $a$.

**Secuencia decodificada:** `"baa"`.

#### 5. Ventaja sobre Huffman

Huffman asigna un número entero de bits por símbolo. Para la distribución $P(a)=0.5$:
- Huffman asigna 1 bit a $a$, cuando $-\log_2 0.5 = 1$ bit exacto (aquí no hay overhead).
- Pero para $P(b)=0.3$: Huffman asigna 2 bits cuando lo óptimo es $-\log_2 0.3 \approx 1.74$ bits.
- La codificación aritmética evita el redondeo al código conjunto de la secuencia completa, no símbolo a símbolo.

Para $n$ símbolos, la codificación aritmética necesita a lo sumo $H(X^n) + 2$ bits, mientras que Huffman por símbolo puede gastar hasta $H + 1$ bits por símbolo, lo que suma $nH + n$ bits. La ventaja crece con $n$.
