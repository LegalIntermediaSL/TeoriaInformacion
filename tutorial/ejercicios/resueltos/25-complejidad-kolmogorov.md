# 25 - Complejidad de Kolmogorov y MDL

## Contexto

Este ejercicio acompaña el artículo
[Complejidad de Kolmogorov](../../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md).

## Enunciado

1. Compara $K(x)$ y $K(y)$ para:
   - $x = $ "la cadena de 500 bits que representa el número $2^{499}$ en binario"
   - $y = $ "los primeros 500 bits del decimal de $\sqrt{2}$ en base 2"
   - $z = $ "una cadena obtenida lanzando una moneda 500 veces"
   Justifica cuál tiene mayor complejidad y por qué.

2. **Principio MDL** (Minimum Description Length): entre dos hipótesis $H_1$ y $H_2$
   para un conjunto de datos $D$, MDL prefiere la que minimiza:
   $$L(H) + L(D | H)$$
   donde $L(H)$ es la longitud de la descripción de la hipótesis y $L(D|H)$ la de
   los datos dado el modelo.
   - Si $H_1$ es un polinomio de grado 1 con coeficientes enteros $\leq 100$ y
     $H_2$ es un polinomio de grado 5 con coeficientes enteros $\leq 100$, ¿qué
     longitud de descripción tienen cada uno?
   - Si $H_1$ ajusta los datos con error 0.5 y $H_2$ los ajusta perfectamente,
     ¿cuándo preferirá MDL a $H_1$?

3. Demuestra la **desigualdad de simetría de la información** (informalmente):
   $$K(x, y) \approx K(x) + K(y | x)$$
   ¿Qué consecuencia tiene sobre la información mutua algorítmica?

4. La **distancia de compresión normalizada** (NCD) entre dos cadenas $x$ e $y$ es:
   $$\text{NCD}(x, y) = \frac{K(xy) - \min(K(x), K(y))}{\max(K(x), K(y))}$$
   ¿Por qué $0 \leq \text{NCD}(x,y) \leq 1$? ¿Qué valor toma si $x = y$?

## Pista

**MDL:** $L(H)$ se mide en bits. Un polinomio de grado $k$ con coeficientes en
$[-M, M]$ requiere $O(k \log M)$ bits.

**Simetría:** $K(x, y) = K(y, x)$ + constante; la clave es que la descripción
de $x$ e $y$ juntos equivale a describir $x$ y luego $y$ dado $x$.

## Solución

### 1. Comparación de complejidades

**$x = 2^{499}$ en binario:** es la cadena `1000...0` con 499 ceros. Se describe
con el programa "imprimir 1 seguido de 499 ceros" o equivalentemente "imprimir el
bit 499 de $2^{499}$". Longitud del programa: $O(\log 499) \approx O(9)$ bits.

$$K(x) \approx O(\log 500) \approx 9 \text{ bits} \ll 500 \text{ bits}$$

**$y = $ primeros 500 bits de $\sqrt{2}$:** existe un algoritmo fijo de longitud
constante para calcular los primeros $n$ bits de $\sqrt{2}$ con el método de
Newton. El programa es "calcular $\sqrt{2}$ a 500 bits" con descripción de
longitud $O(\log 500) + c_{\sqrt{2}}$ donde $c_{\sqrt{2}}$ es la constante del algoritmo.

$$K(y) \approx O(\log 500) + c_{\sqrt{2}} \approx 50\text{–}100 \text{ bits}$$

**$z = $ lanzamiento de moneda:** con alta probabilidad (sobre todas las posibles
secuencias de 500 lanzamientos), no existe ningún programa de longitud $< 490$
que genere $z$. Por el argumento de conteo, al menos $1 - 2^{-10}$ de las cadenas
de 500 bits tienen complejidad $\geq 490$.

$$K(z) \approx 490\text{–}500 \text{ bits con probabilidad alta}$$

**Ranking de complejidad:** $K(x) \ll K(y) \ll K(z)$.

### 2. MDL y selección de modelos

**Longitudes de descripción:**

- Un polinomio de grado 1: $H_1(t) = a_0 + a_1 t$ con $a_0, a_1 \in [-100, 100]$.
  - Descripción: especificar el grado (1 bit para "grado 1 vs grado 5") + dos
    coeficientes de $\log_2 201 \approx 7.65 \approx 8$ bits cada uno.
  - $L(H_1) \approx 1 + 2 \times 8 = 17$ bits.

- Un polinomio de grado 5: $H_2(t) = a_0 + a_1 t + \ldots + a_5 t^5$.
  - $L(H_2) \approx 1 + 6 \times 8 = 49$ bits.

**¿Cuándo prefiere MDL a $H_1$?**

MDL prefiere $H_1$ si:
$$L(H_1) + L(D|H_1) < L(H_2) + L(D|H_2)$$

Con $L(D|H_2) = 0$ (ajuste perfecto, cero error residual a describir) y $L(H_2) = 49$:

$$17 + L(D|H_1) < 49 + 0$$
$$L(D|H_1) < 32 \text{ bits}$$

Si describir los residuos de $H_1$ (el error 0.5 por punto) cuesta menos de 32 bits
en total, MDL prefiere $H_1$.

Para $n$ puntos con error medio 0.5, si el error se modela como Gaussiano con
$\sigma = 0.5$:
$$L(D|H_1) \approx \frac{n}{2} \log_2(2\pi e \sigma^2) \approx \frac{n}{2} \cdot 0.46 \approx 0.23n$$

MDL prefiere $H_1$ si $0.23n < 32$, es decir, **para $n < 139$ puntos de datos**.

Para conjuntos de datos grandes, $H_2$ (ajuste perfecto) puede ser preferible aunque
sea más compleja como hipótesis.

### 3. Simetría de la información

**Enunciado informal.** Para todas las cadenas $x, y$:

$$K(x, y) = K(x) + K(y | x) + O(\log(K(x) + K(y)))$$

**Intuición:** una descripción de $\langle x, y \rangle$ equivale a:
(1) una descripción de $x$, más (2) una descripción de $y$ sabiendo $x$.
El término logarítmico proviene de los separadores necesarios para desambiguar
las longitudes.

**Consecuencia: información mutua algorítmica**

La **información mutua algorítmica** entre $x$ e $y$ es:

$$I(x : y) = K(x) + K(y) - K(x, y) + O(\log K(x,y))$$

Por la simetría: $I(x : y) \approx K(y) - K(y | x)$.

Interpretación: $I(x:y)$ mide cuánto se puede comprimir $y$ si ya se conoce $x$.
Es el análogo individual (determinista) de la información mutua de Shannon $I(X; Y)$,
que mide la reducción de incertidumbre en promedio.

### 4. NCD: cotas y caso $x = y$

**Cota inferior $\text{NCD}(x,y) \geq 0$:**

$$K(xy) \geq \min(K(x), K(y))$$

porque cualquier descripción de $xy$ debe al menos describir el prefijo $x$ o el
sufijo $y$ (en términos de contenido informativo). Luego el numerador es $\geq 0$.

**Cota superior $\text{NCD}(x,y) \leq 1$:**

$$K(xy) \leq K(x) + K(y) + O(1) \leq 2\max(K(x), K(y)) + O(1)$$

Así: $K(xy) - \min(K(x), K(y)) \leq 2\max - \min \leq \max + (\max - \min) \leq 2\max$.

Luego $\text{NCD}(x,y) \leq 1 + O(1/\max)$, que se aproxima a 1 para cadenas largas.

**Caso $x = y$:**

$$K(xx) = K(x) + O(1)$$

porque dado $x$, copiar $x$ es gratis (solo cuesta un bit de "duplicar"). Luego:

$$\text{NCD}(x, x) = \frac{K(x) - K(x)}{\max(K(x), K(x))} = \frac{O(1)}{K(x)} \approx 0$$

**Interpretación:** $\text{NCD}(x,y)$ es una **métrica de similitud**: vale $\approx 0$
cuando $x$ e $y$ son similares (uno puede describirse dado el otro) y $\approx 1$
cuando son "ortogonales" informativamente.

Aplicaciones: clustering de lenguajes, clasificación de malware, comparación de genomas.

## Comentario

MDL es la formalización computacional del principio de la navaja de Occam:
la hipótesis más simple que explica los datos es la preferida. La diferencia con
BIC/AIC estadísticos es que MDL usa la longitud de descripción computacional
(aproximada por la complejidad de Kolmogorov) en lugar de parámetros contados.
Para modelos complejos, MDL y BIC coinciden asintóticamente.

## Para seguir

La **complejidad de Kolmogorov universal** define una distribución de probabilidad
sobre cadenas: $P_U(x) = 2^{-K(x)}$ (distribución de Solomonoff). Demuestra que
esta distribución domina multiplicativamente a toda distribución computable: para
toda distribución computable $\mu$, existe una constante $c$ tal que
$P_U(x) \geq c \cdot \mu(x)$ para todo $x$.
