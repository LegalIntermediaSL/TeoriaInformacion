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

## Procesos estocásticos discretos

Un **proceso estocástico** es una familia indexada de variables aleatorias $\{X_t\}_{t \geq 1}$ sobre el mismo espacio de probabilidad. Nos restringimos a:

- **Alfabeto finito:** $X_t \in \mathcal{X}$ con $|\mathcal{X}| < \infty$.
- **Tiempo discreto:** $t \in \{1, 2, 3, \ldots\}$.

Las distribuciones finito-dimensionales $P(X_1, \ldots, X_n)$ caracterizan el proceso.

### Estacionariedad

Un proceso es **estacionario** (en sentido estricto) si para todo $k \geq 0$ y todo $n$:

$$P(X_1 = x_1, \ldots, X_n = x_n) = P(X_{1+k} = x_1, \ldots, X_{n+k} = x_n)$$

La distribución conjunta no depende del instante de inicio. La estacionariedad implica que la distribución marginal de cada $X_t$ es la misma para todo $t$.

### Ergodicidad

Un proceso estacionario es **ergódico** si los promedios temporales convergen a los promedios de ensemble con probabilidad 1:

$$\frac{1}{n} \sum_{t=1}^n f(X_t) \xrightarrow{n \to \infty} \mathbb{E}[f(X_1)] \quad \text{c.s.}$$

La ergodicidad garantiza que una única realización larga del proceso contiene información estadística de toda la distribución. Las cadenas de Markov irreducibles y aperiódicas sobre espacios finitos son siempre ergódicas.

## Tasa de entropía

La entropía de los primeros $n$ símbolos es $H(X_1, \ldots, X_n)$. La **tasa de entropía** es:

$$\bar{H} = \lim_{n \to \infty} \frac{1}{n} H(X_1, \ldots, X_n)$$

cuando este límite existe. Para procesos estacionarios, el límite siempre existe y es igual a:

$$\bar{H} = \lim_{n \to \infty} H(X_n | X_{n-1}, \ldots, X_1)$$

La segunda expresión mide cuánta incertidumbre añade el nuevo símbolo dado todo el pasado. Esta sucesión es **monótona decreciente** y acotada inferiormente por 0, lo que garantiza la convergencia.

**Interpretación:** $\bar{H}$ es la información "irreducible" por símbolo una vez eliminada toda la redundancia debida a la memoria.

## Fuentes de orden k (procesos de Markov de orden k)

Una **fuente de Markov de orden $k$** satisface:

$$P(X_t | X_{t-1}, X_{t-2}, \ldots, X_1) = P(X_t | X_{t-1}, \ldots, X_{t-k})$$

El pasado relevante tiene longitud exactamente $k$. La tasa de entropía es:

$$\bar{H} = H(X_t | X_{t-1}, \ldots, X_{t-k})$$

que se puede calcular exactamente a partir de la distribución estacionaria y la matriz de transición de orden $k$.

**Ejemplo:** el lenguaje natural aproximado como Markov de orden 2 (bigramas). Si $P(\text{qu} | \text{q}) \approx 0.98$, la entropía condicional $H(\text{letra} | \text{q})$ es mucho menor que la entropía marginal: la letra `q` reduce drásticamente la incertidumbre sobre la siguiente.

## Estimación empírica de la tasa de entropía

Dado un texto largo $x_1 \ldots x_N$, se puede estimar $\bar{H}$ mediante:

### Estimación por k-gramas

$$\hat{H}_k = -\sum_{x_{1:k+1}} \hat{P}(x_{1:k+1}) \log_2 \hat{P}(x_{t+1} | x_{1:k})$$

donde las probabilidades se estiman por frecuencia relativa. Al aumentar $k$, $\hat{H}_k$ es una sucesión decreciente que converge a $\bar{H}$.

### Estimación por compresión (método de Ziv-Merhav)

Si $L_n$ es la longitud del código óptimo de $x_1 \ldots x_n$, entonces:

$$\bar{H} = \lim_{n \to \infty} \frac{L_n}{n}$$

Se puede estimar $\bar{H}$ ejecutando un compresor (LZ78, gzip) sobre el texto y dividiendo el tamaño comprimido entre la longitud original.

## El teorema AEP para procesos ergódicos

El teorema de equipartición asintótica se extiende a procesos estacionarios ergódicos:

**Teorema (Shannon-McMillan-Breiman).** Sea $\{X_t\}$ un proceso estacionario ergódico con tasa de entropía $\bar{H}$. Entonces:

$$-\frac{1}{n} \log_2 P(X_1, \ldots, X_n) \xrightarrow{n \to \infty} \bar{H} \quad \text{en probabilidad (y c.s.)}$$

**Consecuencia:** existe un conjunto típico $A_\epsilon^{(n)}$ con $|A_\epsilon^{(n)}| \approx 2^{n\bar{H}}$ secuencias que concentran casi toda la probabilidad. Los mejores códigos de fuente deben describir estas secuencias con aproximadamente $\bar{H}$ bits por símbolo.

## Fuentes mezclables y condiciones de regularidad

Para que la tasa de entropía tenga propiedades útiles, el proceso debe cumplir cierta regularidad asintótica. Las condiciones más comunes son:

- **Mezcla fuerte ($\phi$-mixing):** la dependencia entre $X_1, \ldots, X_m$ y $X_{m+k}, \ldots$ decae a cero cuando $k \to \infty$.
- **$\psi$-mixing:** condición más fuerte que implica resultados exponenciales sobre conjuntos típicos.

Las cadenas de Markov irreducibles y aperiódicas son $\phi$-mixing con decaimiento geométrico: la dependencia entre el pasado y el futuro lejano decae exponencialmente en la distancia.

## Capacidad de canales con memoria

La noción de tasa de entropía se extiende al estudio de canales con memoria. La **capacidad de información** de un canal estacionario ergódico es:

$$C = \sup_{\{X_t\} \text{ estacionario}} \bar{I}(X; Y)$$

donde $\bar{I}(X;Y) = \lim_{n \to \infty} \frac{1}{n} I(X_1^n; Y_1^n)$ es la tasa de información mutua. Para canales sin memoria con memoria en la entrada, se recuperan los resultados del teorema de Shannon clásico.

## Ejemplos de fuentes con memoria

| Fuente | Modelo | Tasa de entropía |
|--------|--------|-----------------|
| Lenguaje inglés | Markov de orden alto + modelos de lenguaje | ~1–2 bits/carácter |
| ADN | Markov de orden 1–3 (codones) | ~1.8–2 bits/base |
| Audio PCM | AR(10)–AR(50) | Variable |
| Señal financiera | GARCH (heterocedasticidad condicional) | Alta (mercados eficientes) |

## Ideas clave

1. La tasa de entropía $\bar{H}$ generaliza la entropía por símbolo a fuentes con memoria.
2. Para procesos estacionarios, $\bar{H} = \lim_n H(X_n | X_{n-1}, \ldots, X_1)$.
3. El AEP (Shannon-McMillan-Breiman) extiende el conjunto típico a procesos ergódicos.
4. Las fuentes de Markov de orden $k$ dan estimaciones computables de $\bar{H}$ mediante tablas de frecuencia.
5. Los compresores universales (LZ78, LZMA) convergen a $\bar{H}$ sin conocer el modelo.

## Ejercicios

1. Sea $\{X_t\}$ un proceso Markov de orden 1 sobre $\{a, b, c\}$ con matriz de transición $P$ donde $P_{ij} = 1/3$ para todo $i,j$. ¿Cuál es $\bar{H}$? ¿Coincide con la entropía de la distribución marginal?

2. Para el proceso i.i.d. con $P(X_t = 1) = p$, verifica que $\bar{H} = H_b(p)$ usando la definición de límite.

3. Estima la tasa de entropía del texto de un artículo web contando bigramas y trigramas. ¿Cuál da menor estimación? ¿Por qué?

4. Enuncia y demuestra que la sucesión $H(X_n | X_1, \ldots, X_{n-1})$ es monótona decreciente en $n$ para cualquier proceso estacionario.

## Véase también

- [Cadenas de Markov y tasa de entropía](12-cadenas-de-markov-y-tasa-de-entropia.md)
- [Teorema de Shannon](08-teorema-de-shannon-capacidad.md)


## Referencias

- Cover, T.M. y Thomas, J.A. (2006). *Elements of Information Theory*, 2ª ed., cap. 4 y 16. Wiley.
- Shannon, C.E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal*, 30(1), 50–64.
- Breiman, L. (1957). The individual ergodic theorem of information theory. *Annals of Mathematical Statistics*, 28(3), 809–811.
- Shields, P.C. (1996). *The Ergodic Theory of Discrete Sample Paths*. AMS.
