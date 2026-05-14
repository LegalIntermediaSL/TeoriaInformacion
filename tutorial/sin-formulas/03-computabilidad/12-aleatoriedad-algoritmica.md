> **Nota:** Esta es la versión sin fórmulas LaTeX de [12-aleatoriedad-algoritmica](../../03-computabilidad/12-aleatoriedad-algoritmica.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Aleatoriedad algorítmica

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Complejidad de Kolmogorov](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)
- [Máquinas de Turing](04-maquinas-de-turing.md)

## Objetivos de aprendizaje

1. Definir la aleatoriedad de Martin-Löf mediante tests de nulidad.
2. Entender la constante Ω de Chaitin como número real no computable.
3. Relacionar la aleatoriedad algorítmica con la incompresibilidad de Kolmogorov.


## Intuición

¿Qué significa que una cadena sea verdaderamente aleatoria? Una cadena como `0101010101` parece demasiado regular para ser aleatoria, pero según la definición probabilística clásica tiene exactamente la misma probabilidad que cualquier otra cadena de 10 bits. La **aleatoriedad algorítmica** da una respuesta satisfactoria: una cadena es aleatoria si no puede ser comprimida, si supera todos los tests estadísticos computables, y si no puede predecirse mejor que al azar por ningún algoritmo. Estos tres criterios distintos resultan ser equivalentes.

## Complejidad de Kolmogorov (repaso)

La **complejidad de Kolmogorov** de una cadena `x` relativa a una máquina universal `U` es:


> **Fórmula:** `K(x) = min\{|π| : U(π) = x\}`


La cadena `x` es **incompresible** si `K(x) ≥ |x| - c` para una constante `c` pequeña. Para la mayoría de las cadenas de longitud `n`, `K(x) ≈ n`: no tienen descripción corta.

**Limitación:** `K(x)` mide la complejidad de cadenas finitas. Para definir aleatoriedad de una secuencia infinita `ω = ω_1 ω_2 ω_3 …`, necesitamos un concepto asintótico.

## Los tres enfoques de aleatoriedad

### 1. Aleatoriedad por incompresibilidad (Schnorr-Chaitin-Levin)

Una secuencia infinita `ω` es **aleatoria en el sentido de Martin-Löf** si sus prefijos son incompresibles:


> **Fórmula:** `liminf_n → ∞ (K(ω_1 … ω_n))/n = 1`


Es decir, los prefijos de `ω` de longitud `n` requieren aproximadamente `n` bits para describirse: no hay compresión asintótica.

**Intuición:** las secuencias aleatorias son las que "resisten" ser comprimidas indefinidamente. Una secuencia regular como `010101...` tiene `K(prefijo de longitud  n) = O(log n)`, que es drásticamente compresible.

### 2. Tests de Martin-Löf

Un **test de Martin-Löf** es una sucesión computable de conjuntos abiertos `U_1, U_2, …` con `P(U_n) ≤ 2⁻ⁿ`. Una secuencia `ω` **pasa** el test si `ω ∉ cap_n U_n`.

Una secuencia es **aleatoria de Martin-Löf** si pasa todos los tests de Martin-Löf. Este es el concepto más refinado: los tests capturan todas las regularidades estadísticas computables (test de chi-cuadrado, test de rachas, test de kolmogorov-smirnov, etc.).

### 3. Impredecibilidad (martingalas)

Una **martingala computable** es una función `d: \{0,1\}^* → ℝ^+` computable que satisface:


> **Fórmula:** `d(w) = (d(w0) + d(w1))/2`


La estrategia `d` intenta ganar apostando en cada bit. Una secuencia `ω` es **impredecible** si ninguna martingala computable acumula ganancia ilimitada sobre los prefijos de `ω`:


> **Fórmula:** `limsup_n → ∞ d(ω_1 … ω_n) < ∞`


## Equivalencia de los tres enfoques

**Teorema (Martin-Löf, Schnorr, Levin).** Para una secuencia `ω`, las tres condiciones siguientes son equivalentes:

1. `ω` es incompresible (`K(ω_1 … ω_n)/n → 1`).
2. `ω` pasa todos los tests de Martin-Löf.
3. Ninguna martingala computable gana ilimitadamente sobre `ω`.

Esta equivalencia justifica hablar de **la** noción de aleatoriedad algorítmica. Cualquiera de los tres enfoques define el mismo conjunto de secuencias aleatorias.

## El número de Chaitin Ω

El **número de parada de Chaitin** es:


> **Fórmula:** `Ω = Σ_π: U(π) \downarrow 2^(-|π|)`


donde la suma es sobre todos los programas (prefijo-libres) que se detienen. Satisface `0 < Ω < 1` y su expansión binaria `Ω = 0.ω_1ω_2ω_3…` es una secuencia aleatoria de Martin-Löf.

**Propiedades de Ω:**
- **Bien definido:** la suma converge porque los programas autodelimitados forman un código prefijo (desigualdad de Kraft).
- **No computable:** conocer los primeros `n` bits de `Ω` permite resolver el problema de la parada para todos los programas de longitud `≤ n`.
- **Aleatoriedad:** `K(Ω_1 … Ω_n) ≥ n - O(1)`; los bits de `Ω` son irreduciblemente aleatorios.
- **No único:** `Ω` depende de la máquina universal `U`, pero todos los `Ω_U` son aleatorios.

## Grados de aleatoriedad y la jerarquía

No todas las secuencias no-aleatorias son igual de regulares. Se puede relativizar la aleatoriedad:

- Una secuencia `ω` es **`A`-aleatoria** (aleatoria relativa al oráculo `A`) si pasa todos los tests de Martin-Löf computables con oráculo `A`.
- La aleatoriedad relativa da una jerarquía: las secuencias aleatorias relativas a `∅'` (el problema de la parada) son las `∅'`-aleatorias, que incluyen a `Ω`.

La **reducción de Solovay** captura las relaciones: `α ≤_S β` si los bits de `α` se pueden aproximar computablemente a partir de los bits de `β`.

## Aleatoriedad y compresión universal

La equivalencia entre aleatoriedad e incompresibilidad tiene consecuencias para los compresores:

**Teorema.** Ningún algoritmo de compresión puede comprimir todas las cadenas. Más precisamente, para cualquier compresión `C` computable y cualquier `n`, al menos `2^n - 2^(n-c+1)` cadenas de longitud `n` no se comprimen más de `c` bits.

Esto es consecuencia directa del argumento de conteo: el número de descripciones de longitud `< n` es `< 2^n`.

**Corolario:** en media, las secuencias no se pueden comprimir. Los compresores ganan porque los datos reales tienen estructura (baja complejidad de Kolmogorov condicional), pero en el peor caso siempre fallan.

## Relación con la entropía de Shannon

La complejidad de Kolmogorov y la entropía de Shannon están relacionadas pero miden cosas distintas:

| Concepto | Mide | Objeto |
|---------|------|--------|
| `H(X)` | Incertidumbre promedio | Distribución `P` |
| `K(x)` | Longitud mínima de descripción | Cadena individual `x` |

**Conexión:** si `x` es una muestra típica de una fuente i.i.d. con entropía `H`, entonces `K(x) ≈ nH` con alta probabilidad. El conjunto típico del AEP coincide con el conjunto de cadenas incompresibles.

## Ideas clave

1. Aleatoriedad algorítmica = incompresibilidad = pasar todos los tests = impredecibilidad. Los tres son equivalentes.
2. El número de Chaitin `Ω` es el ejemplo canónico de secuencia aleatoria no computable.
3. Conocer los primeros `n` bits de `Ω` equivale a resolver el problema de la parada para programas cortos.
4. Los compresores universales como LZ78 convergen a la tasa de entropía exactamente porque procesan secuencias cuya complejidad de Kolmogorov es cercana a `n`.
5. La aleatoriedad se relativiza: `Ω` es aleatoria respecto a `∅` pero no respecto a `∅'`.

## Ejercicios

1. Demuestra que para cualquier `n`, el número de cadenas binarias de longitud `n` con `K(x) < n - 10` es menor que `2ⁿ⁻¹⁰`.

2. Explica por qué `Ω` no puede ser computable: ¿cómo resolverías el problema de la parada con acceso a `Ω`?

3. ¿Es la secuencia `0^n 1^n 0^n 1^n …` aleatoria de Martin-Löf? ¿Por qué?

4. La secuencia de dígitos de `π` en base 2, ¿es aleatoria de Martin-Löf? (Esta es una pregunta abierta en matemáticas; discute qué se sabe y por qué es difícil.)

## Véase también

- [Complejidad de Kolmogorov](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)
- [Jerarquía aritmética](10-jerarquia-aritmetica.md)


## Referencias

- Martin-Löf, P. (1966). The definition of random sequences. *Information and Control*, 9(6), 602–619.
- Chaitin, G.J. (1975). A theory of program size formally identical to information theory. *J. ACM*, 22(3), 329–340.
- Li, M. y Vitányi, P. (2008). *An Introduction to Kolmogorov Complexity and Its Applications*, 3ª ed. Springer.
- Downey, R.G. y Hirschfeldt, D.R. (2010). *Algorithmic Randomness and Complexity*. Springer.
