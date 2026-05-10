# Aleatoriedad algorítmica

## Intuición

¿Qué significa que una cadena sea verdaderamente aleatoria? Una cadena como `0101010101` parece demasiado regular para ser aleatoria, pero según la definición probabilística clásica tiene exactamente la misma probabilidad que cualquier otra cadena de 10 bits. La **aleatoriedad algorítmica** da una respuesta satisfactoria: una cadena es aleatoria si no puede ser comprimida, si supera todos los tests estadísticos computables, y si no puede predecirse mejor que al azar por ningún algoritmo. Estos tres criterios distintos resultan ser equivalentes.

## Complejidad de Kolmogorov (repaso)

La **complejidad de Kolmogorov** de una cadena $x$ relativa a una máquina universal $U$ es:

$$K(x) = \min\{|\pi| : U(\pi) = x\}$$

La cadena $x$ es **incompresible** si $K(x) \geq |x| - c$ para una constante $c$ pequeña. Para la mayoría de las cadenas de longitud $n$, $K(x) \approx n$: no tienen descripción corta.

**Limitación:** $K(x)$ mide la complejidad de cadenas finitas. Para definir aleatoriedad de una secuencia infinita $\omega = \omega_1 \omega_2 \omega_3 \ldots$, necesitamos un concepto asintótico.

## Los tres enfoques de aleatoriedad

### 1. Aleatoriedad por incompresibilidad (Schnorr-Chaitin-Levin)

Una secuencia infinita $\omega$ es **aleatoria en el sentido de Martin-Löf** si sus prefijos son incompresibles:

$$\liminf_{n \to \infty} \frac{K(\omega_1 \ldots \omega_n)}{n} = 1$$

Es decir, los prefijos de $\omega$ de longitud $n$ requieren aproximadamente $n$ bits para describirse: no hay compresión asintótica.

**Intuición:** las secuencias aleatorias son las que "resisten" ser comprimidas indefinidamente. Una secuencia regular como `010101...` tiene $K(\text{prefijo de longitud } n) = O(\log n)$, que es drásticamente compresible.

### 2. Tests de Martin-Löf

Un **test de Martin-Löf** es una sucesión computable de conjuntos abiertos $U_1, U_2, \ldots$ con $P(U_n) \leq 2^{-n}$. Una secuencia $\omega$ **pasa** el test si $\omega \notin \bigcap_n U_n$.

Una secuencia es **aleatoria de Martin-Löf** si pasa todos los tests de Martin-Löf. Este es el concepto más refinado: los tests capturan todas las regularidades estadísticas computables (test de chi-cuadrado, test de rachas, test de kolmogorov-smirnov, etc.).

### 3. Impredecibilidad (martingalas)

Una **martingala computable** es una función $d: \{0,1\}^* \to \mathbb{R}^+$ computable que satisface:

$$d(w) = \frac{d(w0) + d(w1)}{2}$$

La estrategia $d$ intenta ganar apostando en cada bit. Una secuencia $\omega$ es **impredecible** si ninguna martingala computable acumula ganancia ilimitada sobre los prefijos de $\omega$:

$$\limsup_{n \to \infty} d(\omega_1 \ldots \omega_n) < \infty$$

## Equivalencia de los tres enfoques

**Teorema (Martin-Löf, Schnorr, Levin).** Para una secuencia $\omega$, las tres condiciones siguientes son equivalentes:

1. $\omega$ es incompresible ($K(\omega_1 \ldots \omega_n)/n \to 1$).
2. $\omega$ pasa todos los tests de Martin-Löf.
3. Ninguna martingala computable gana ilimitadamente sobre $\omega$.

Esta equivalencia justifica hablar de **la** noción de aleatoriedad algorítmica. Cualquiera de los tres enfoques define el mismo conjunto de secuencias aleatorias.

## El número de Chaitin Ω

El **número de parada de Chaitin** es:

$$\Omega = \sum_{\pi: U(\pi) \downarrow} 2^{-|\pi|}$$

donde la suma es sobre todos los programas (prefijo-libres) que se detienen. Satisface $0 < \Omega < 1$ y su expansión binaria $\Omega = 0.\omega_1\omega_2\omega_3\ldots$ es una secuencia aleatoria de Martin-Löf.

**Propiedades de Ω:**
- **Bien definido:** la suma converge porque los programas autodelimitados forman un código prefijo (desigualdad de Kraft).
- **No computable:** conocer los primeros $n$ bits de $\Omega$ permite resolver el problema de la parada para todos los programas de longitud $\leq n$.
- **Aleatoriedad:** $K(\Omega_1 \ldots \Omega_n) \geq n - O(1)$; los bits de $\Omega$ son irreduciblemente aleatorios.
- **No único:** $\Omega$ depende de la máquina universal $U$, pero todos los $\Omega_U$ son aleatorios.

## Grados de aleatoriedad y la jerarquía

No todas las secuencias no-aleatorias son igual de regulares. Se puede relativizar la aleatoriedad:

- Una secuencia $\omega$ es **$A$-aleatoria** (aleatoria relativa al oráculo $A$) si pasa todos los tests de Martin-Löf computables con oráculo $A$.
- La aleatoriedad relativa da una jerarquía: las secuencias aleatorias relativas a $\emptyset'$ (el problema de la parada) son las $\emptyset'$-aleatorias, que incluyen a $\Omega$.

La **reducción de Solovay** captura las relaciones: $\alpha \leq_S \beta$ si los bits de $\alpha$ se pueden aproximar computablemente a partir de los bits de $\beta$.

## Aleatoriedad y compresión universal

La equivalencia entre aleatoriedad e incompresibilidad tiene consecuencias para los compresores:

**Teorema.** Ningún algoritmo de compresión puede comprimir todas las cadenas. Más precisamente, para cualquier compresión $C$ computable y cualquier $n$, al menos $2^n - 2^{n-c+1}$ cadenas de longitud $n$ no se comprimen más de $c$ bits.

Esto es consecuencia directa del argumento de conteo: el número de descripciones de longitud $< n$ es $< 2^n$.

**Corolario:** en media, las secuencias no se pueden comprimir. Los compresores ganan porque los datos reales tienen estructura (baja complejidad de Kolmogorov condicional), pero en el peor caso siempre fallan.

## Relación con la entropía de Shannon

La complejidad de Kolmogorov y la entropía de Shannon están relacionadas pero miden cosas distintas:

| Concepto | Mide | Objeto |
|---------|------|--------|
| $H(X)$ | Incertidumbre promedio | Distribución $P$ |
| $K(x)$ | Longitud mínima de descripción | Cadena individual $x$ |

**Conexión:** si $x$ es una muestra típica de una fuente i.i.d. con entropía $H$, entonces $K(x) \approx nH$ con alta probabilidad. El conjunto típico del AEP coincide con el conjunto de cadenas incompresibles.

## Ideas clave

1. Aleatoriedad algorítmica = incompresibilidad = pasar todos los tests = impredecibilidad. Los tres son equivalentes.
2. El número de Chaitin $\Omega$ es el ejemplo canónico de secuencia aleatoria no computable.
3. Conocer los primeros $n$ bits de $\Omega$ equivale a resolver el problema de la parada para programas cortos.
4. Los compresores universales como LZ78 convergen a la tasa de entropía exactamente porque procesan secuencias cuya complejidad de Kolmogorov es cercana a $n$.
5. La aleatoriedad se relativiza: $\Omega$ es aleatoria respecto a $\emptyset$ pero no respecto a $\emptyset'$.

## Ejercicios

1. Demuestra que para cualquier $n$, el número de cadenas binarias de longitud $n$ con $K(x) < n - 10$ es menor que $2^{n-10}$.

2. Explica por qué $\Omega$ no puede ser computable: ¿cómo resolverías el problema de la parada con acceso a $\Omega$?

3. ¿Es la secuencia $0^n 1^n 0^n 1^n \ldots$ aleatoria de Martin-Löf? ¿Por qué?

4. La secuencia de dígitos de $\pi$ en base 2, ¿es aleatoria de Martin-Löf? (Esta es una pregunta abierta en matemáticas; discute qué se sabe y por qué es difícil.)

## Referencias

- Martin-Löf, P. (1966). The definition of random sequences. *Information and Control*, 9(6), 602–619.
- Chaitin, G.J. (1975). A theory of program size formally identical to information theory. *J. ACM*, 22(3), 329–340.
- Li, M. y Vitányi, P. (2008). *An Introduction to Kolmogorov Complexity and Its Applications*, 3ª ed. Springer.
- Downey, R.G. y Hirschfeldt, D.R. (2010). *Algorithmic Randomness and Complexity*. Springer.
