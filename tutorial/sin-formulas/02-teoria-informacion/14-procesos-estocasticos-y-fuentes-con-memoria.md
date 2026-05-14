> **Nota:** Esta es la versión sin fórmulas LaTeX de [14-procesos-estocasticos-y-fuentes-con-memoria](../../02-teoria-informacion/14-procesos-estocasticos-y-fuentes-con-memoria.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Procesos estocásticos y fuentes con memoria

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Cadenas de Markov y tasa de entropía](12-cadenas-de-markov-y-tasa-de-entropia.md)

## Objetivos de aprendizaje

1. Definir fuentes estacionarias y ergódicas y su tasa de entropía.
2. Calcular la entropía de fuentes de Markov de orden k.
3. Entender el teorema de Shannon-McMillan-Breiman para fuentes ergódicas.


## Intuición

Hasta ahora hemos tratado las fuentes de información como secuencias de símbolos independientes e idénticamente distribuidos (i.i.d.). Pero el lenguaje natural, el genoma, el audio y la mayoría de las señales reales exhiben **memoria**: el símbolo actual depende de los anteriores. Este artículo generaliza la teoría a fuentes con dependencia temporal, definiendo la entropía de un proceso y estudiando cuándo tiene sentido hablar de una "tasa de información" estable.

## Relación con el artículo anterior (02/12)

El artículo [Cadenas de Markov y tasa de entropía](12-cadenas-de-markov-y-tasa-de-entropia.md) introduce el caso especial más importante de fuente con memoria: una cadena de Markov de **orden 1** sobre un alfabeto finito, con una única distribución estacionaria `π` y matriz de transición `P`. Su tasa de entropía es la fórmula cerrada:


> **Fórmula:** `H̄_Markov-1 = -Σ_i π_i Σ_j P_ij log_2 P_ij = Σ_i π_i H(fila_i)`


Este artículo **generaliza ese resultado en tres direcciones**:

| Generalización | Artículo 02/12 | Este artículo (02/14) |
|---------------|---------------|----------------------|
| Orden de memoria | Orden 1 (depende de `X_t-1`) | Orden `k` arbitrario (depende de `X_t-1, …, X_t-k`) |
| Tipo de proceso | Solo cadenas de Markov | Cualquier proceso estacionario ergódico |
| Convergencia del límite | Garantizada por estacionariedad + irreducibilidad | Garantizada por el teorema de Breiman (más general) |
| AEP | Conjunto típico i.i.d.: `≈ 2^(nH)` secuencias | Conjunto típico ergódico: `≈ 2^(nH̄)` secuencias |

**Por qué Markov-1 es un caso especial.** La definición de tasa de entropía en este artículo,


> **Fórmula:** `H̄ = lim_n → ∞ H(X_n | X_n-1, …, X_1)`


se reduce a `H(X_t | X_t-1)` cuando el proceso es Markov de orden 1, recuperando exactamente la fórmula de 02/12. La convergencia del límite —que en 02/12 se demuestra directamente usando la distribución estacionaria— aquí se garantiza por la monotonicidad de `H(X_n | X_1, …, X_n-1)` combinada con el teorema ergódico de Birkhoff.

**Cuándo usar cada artículo.** Si el modelo es una cadena de Markov de orden 1 con matriz de transición conocida, las fórmulas de 02/12 son suficientes y computacionalmente directas. Si el proceso tiene memoria de orden superior, no es Markov, o se conoce solo a través de datos empíricos, las herramientas de este artículo (estimación por `k`-gramas, estimación por compresión, Shannon-McMillan-Breiman) son necesarias.

## Procesos estocásticos discretos

Un **proceso estocástico** es una familia indexada de variables aleatorias `\{X_t\}_t ≥ 1` sobre el mismo espacio de probabilidad. Nos restringimos a:

- **Alfabeto finito:** `X_t ∈ 𝒳` con `|𝒳| < ∞`.
- **Tiempo discreto:** `t ∈ \{1, 2, 3, …\}`.

Las distribuciones finito-dimensionales `P(X_1, …, X_n)` caracterizan el proceso.

### Estacionariedad

Un proceso es **estacionario** (en sentido estricto) si para todo `k ≥ 0` y todo `n`:


> **Fórmula:** `P(X_1 = x_1, …, X_n = x_n) = P(X_1+k = x_1, …, X_n+k = x_n)`


La distribución conjunta no depende del instante de inicio. La estacionariedad implica que la distribución marginal de cada `X_t` es la misma para todo `t`.

### Ergodicidad

Un proceso estacionario es **ergódico** si los promedios temporales convergen a los promedios de ensemble con probabilidad 1:


> **Fórmula:** `1/n Σ_t=1^n f(X_t) \xrightarrow{n → ∞} 𝔼[f(X_1)]  c.s.`


La ergodicidad garantiza que una única realización larga del proceso contiene información estadística de toda la distribución. Las cadenas de Markov irreducibles y aperiódicas sobre espacios finitos son siempre ergódicas.

## Tasa de entropía

La entropía de los primeros `n` símbolos es `H(X_1, …, X_n)`. La **tasa de entropía** es:


> **Fórmula:** `H̄ = lim_n → ∞ 1/n H(X_1, …, X_n)`


cuando este límite existe. Para procesos estacionarios, el límite siempre existe y es igual a:


> **Fórmula:** `H̄ = lim_n → ∞ H(X_n | X_n-1, …, X_1)`


La segunda expresión mide cuánta incertidumbre añade el nuevo símbolo dado todo el pasado. Esta sucesión es **monótona decreciente** y acotada inferiormente por 0, lo que garantiza la convergencia.

**Interpretación:** `H̄` es la información "irreducible" por símbolo una vez eliminada toda la redundancia debida a la memoria.

## Fuentes de orden k (procesos de Markov de orden k)

Una **fuente de Markov de orden `k`** satisface:


> **Fórmula:** `P(X_t | X_t-1, X_t-2, …, X_1) = P(X_t | X_t-1, …, X_t-k)`


El pasado relevante tiene longitud exactamente `k`. La tasa de entropía es:


> **Fórmula:** `H̄ = H(X_t | X_t-1, …, X_t-k)`


que se puede calcular exactamente a partir de la distribución estacionaria y la matriz de transición de orden `k`.

**Ejemplo:** el lenguaje natural aproximado como Markov de orden 2 (bigramas). Si `P(qu | q) ≈ 0.98`, la entropía condicional `H(letra | q)` es mucho menor que la entropía marginal: la letra `q` reduce drásticamente la incertidumbre sobre la siguiente.

## Estimación empírica de la tasa de entropía

Dado un texto largo `x_1 … x_N`, se puede estimar `H̄` mediante:

### Estimación por k-gramas


> **Fórmula:** `Ĥ_k = -Σ_x_{1:k+1} P̂(x_1:k+1) log_2 P̂(x_t+1 | x_1:k)`


donde las probabilidades se estiman por frecuencia relativa. Al aumentar `k`, `Ĥ_k` es una sucesión decreciente que converge a `H̄`.

### Estimación por compresión (método de Ziv-Merhav)

Si `L_n` es la longitud del código óptimo de `x_1 … x_n`, entonces:


> **Fórmula:** `H̄ = lim_n → ∞ L_n/n`


Se puede estimar `H̄` ejecutando un compresor (LZ78, gzip) sobre el texto y dividiendo el tamaño comprimido entre la longitud original.

## El teorema AEP para procesos ergódicos

El teorema de equipartición asintótica se extiende a procesos estacionarios ergódicos:

**Teorema (Shannon-McMillan-Breiman).** Sea `\{X_t\}` un proceso estacionario ergódico con tasa de entropía `H̄`. Entonces:


> **Fórmula:** `-1/n log_2 P(X_1, …, X_n) \xrightarrow{n → ∞} H̄  en probabilidad (y c.s.)`


**Consecuencia:** existe un conjunto típico `A_ε^((n))` con `|A_ε^((n))| ≈ 2^(nH̄)` secuencias que concentran casi toda la probabilidad. Los mejores códigos de fuente deben describir estas secuencias con aproximadamente `H̄` bits por símbolo.

## Fuentes mezclables y condiciones de regularidad

Para que la tasa de entropía tenga propiedades útiles, el proceso debe cumplir cierta regularidad asintótica. Las condiciones más comunes son:

- **Mezcla fuerte (`φ`-mixing):** la dependencia entre `X_1, …, X_m` y `X_m+k, …` decae a cero cuando `k → ∞`.
- **`ψ`-mixing:** condición más fuerte que implica resultados exponenciales sobre conjuntos típicos.

Las cadenas de Markov irreducibles y aperiódicas son `φ`-mixing con decaimiento geométrico: la dependencia entre el pasado y el futuro lejano decae exponencialmente en la distancia.

## Capacidad de canales con memoria

La noción de tasa de entropía se extiende al estudio de canales con memoria. La **capacidad de información** de un canal estacionario ergódico es:


> **Fórmula:** `C = sup_\{X_t\  estacionario} Ī(X; Y)`


donde `Ī(X;Y) = lim_n → ∞ 1/n I(X_1^n; Y_1^n)` es la tasa de información mutua. Para canales sin memoria con memoria en la entrada, se recuperan los resultados del teorema de Shannon clásico.

## Ejemplos de fuentes con memoria

| Fuente | Modelo | Tasa de entropía |
|--------|--------|-----------------|
| Lenguaje inglés | Markov de orden alto + modelos de lenguaje | ~1–2 bits/carácter |
| ADN | Markov de orden 1–3 (codones) | ~1.8–2 bits/base |
| Audio PCM | AR(10)–AR(50) | Variable |
| Señal financiera | GARCH (heterocedasticidad condicional) | Alta (mercados eficientes) |

## Ideas clave

1. La tasa de entropía `H̄` generaliza la entropía por símbolo a fuentes con memoria.
2. Para procesos estacionarios, `H̄ = lim_n H(X_n | X_n-1, …, X_1)`.
3. El AEP (Shannon-McMillan-Breiman) extiende el conjunto típico a procesos ergódicos.
4. Las fuentes de Markov de orden `k` dan estimaciones computables de `H̄` mediante tablas de frecuencia.
5. Los compresores universales (LZ78, LZMA) convergen a `H̄` sin conocer el modelo.

## Ejercicios

1. Sea `\{X_t\}` un proceso Markov de orden 1 sobre `\{a, b, c\}` con matriz de transición `P` donde `P_ij = 1/3` para todo `i,j`. ¿Cuál es `H̄`? ¿Coincide con la entropía de la distribución marginal?

2. Para el proceso i.i.d. con `P(X_t = 1) = p`, verifica que `H̄ = H_b(p)` usando la definición de límite.

3. Estima la tasa de entropía del texto de un artículo web contando bigramas y trigramas. ¿Cuál da menor estimación? ¿Por qué?

4. Enuncia y demuestra que la sucesión `H(X_n | X_1, …, X_n-1)` es monótona decreciente en `n` para cualquier proceso estacionario.

## Véase también

- [Cadenas de Markov y tasa de entropía](12-cadenas-de-markov-y-tasa-de-entropia.md)
- [Teorema de Shannon](08-teorema-de-shannon-capacidad.md)


## Referencias

- Cover, T.M. y Thomas, J.A. (2006). *Elements of Information Theory*, 2ª ed., cap. 4 y 16. Wiley.
- Shannon, C.E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal*, 30(1), 50–64.
- Breiman, L. (1957). The individual ergodic theorem of information theory. *Annals of Mathematical Statistics*, 28(3), 809–811.
- Shields, P.C. (1996). *The Ergodic Theory of Discrete Sample Paths*. AMS.
