# Cadenas de Markov y Tasa de Entropía

## Intuición

Hasta ahora hemos medido la entropía de fuentes sin memoria: cada símbolo se elige
de forma independiente. Las fuentes reales —texto, audio, genoma— tienen **memoria**:
el símbolo actual depende de los anteriores. Las **cadenas de Markov** modelan esta
dependencia y la **tasa de entropía** generaliza la entropía de Shannon a este contexto.

## Cadenas de Markov

Una **cadena de Markov** de primer orden sobre un alfabeto $\mathcal{X}$ es un proceso
estocástico $\{X_n\}$ que satisface la **propiedad de Markov**:

$$P(X_n = x_n \mid X_{n-1} = x_{n-1}, \ldots, X_0 = x_0) = P(X_n = x_n \mid X_{n-1} = x_{n-1})$$

La dinámica queda completamente especificada por:

- **Estado inicial** $\mu_0$: distribución sobre $\mathcal{X}$.
- **Matriz de transición** $P$: $P_{ij} = P(X_n = j \mid X_{n-1} = i)$, con $\sum_j P_{ij} = 1$.

**Distribución estacionaria:** un vector $\pi$ tal que $\pi P = \pi$ y $\sum_i \pi_i = 1$.
Para una cadena **ergódica** (irreducible y aperiódica), la distribución estacionaria
existe, es única, y $\mu_n \to \pi$ independientemente de $\mu_0$.

**Ejemplo:** modelo de bigrama del español. El estado es la letra actual; la transición
es la probabilidad de la siguiente letra dado el estado. Esto captura correlaciones
como "después de 'q' casi siempre viene 'u'".

## Tasa de entropía

Para un proceso estocástico estacionario $\{X_n\}$, la **tasa de entropía** es:

$$\bar{H} = \lim_{n \to \infty} \frac{H(X_1, X_2, \ldots, X_n)}{n}$$

cuando el límite existe. También puede expresarse como:

$$\bar{H} = \lim_{n \to \infty} H(X_n \mid X_{n-1}, \ldots, X_1)$$

Para una cadena de Markov estacionaria con distribución $\pi$ y matriz de transición $P$:

$$\bar{H} = -\sum_{i} \pi_i \sum_{j} P_{ij} \log P_{ij} = \sum_i \pi_i H(X_n \mid X_{n-1} = i)$$

En palabras: la tasa de entropía es la entropía condicional media del siguiente estado
dado el actual, promediada sobre la distribución estacionaria.

**Desigualdad fundamental:**

$$\bar{H} \leq H(X_1)$$

con igualdad si y solo si los $X_n$ son independientes. La memoria siempre reduce o
iguala la incertidumbre por símbolo.

## El teorema AEP para fuentes con memoria

El **Teorema Ergódico de la Información** (McMillan, 1953) generaliza el AEP a fuentes
estacionarias y ergódicas:

$$-\frac{1}{n} \log P(X_1, X_2, \ldots, X_n) \xrightarrow{p} \bar{H}$$

Esto significa que para $n$ grande, casi todas las secuencias tienen probabilidad
aproximadamente $2^{-n\bar{H}}$. El conjunto típico tiene:

- Cardinalidad $\approx 2^{n\bar{H}}$.
- Probabilidad acumulada $\to 1$.
- Longitud de descripción óptima: $\approx n\bar{H}$ bits.

La compresión óptima de una fuente con memoria requiere $\bar{H}$ bits por símbolo,
no $H(X_1)$. El texto en español tiene $H \approx 4.7$ bits/letra si se asume
independencia, pero $\bar{H} \approx 1.3$ bits/letra en un modelo de orden 8.

## Entropía relativa entre cadenas de Markov

Sea $P$ y $Q$ dos matrices de transición sobre el mismo espacio de estados, con
distribuciones estacionarias $\pi$ y $\mu$. La divergencia KL entre los procesos
generados es:

$$D(\pi P \| \mu Q) = \sum_i \pi_i \sum_j P_{ij} \log \frac{P_{ij}}{Q_{ij}}$$

Esto cuantifica el coste de usar el modelo $Q$ cuando la fuente real es $P$; aparece
en la codificación de longitud variable adaptativa y en la detección de cambio de régimen.

## Compresión universal: LZ78 y la tasa de entropía

El algoritmo **Lempel-Ziv 78** (1978) comprime sin conocer la distribución de la fuente.

Para cualquier fuente estacionaria y ergódica, la tasa de compresión de LZ78 satisface:

$$\limsup_{n \to \infty} \frac{L_{\text{LZ78}}(X_1^n)}{n} = \bar{H} \quad \text{c.s.}$$

El número de frases del diccionario LZ78 tras $n$ símbolos crece como $n / \log n$,
y la longitud del diccionario converge a la tasa de entropía de la fuente.

Esta es una de las conexiones más profundas de la teoría de la información con la
práctica: la compresión universal es posible y es exactamente óptima.

## Modelos de orden superior y modelos ocultos

**Cadenas de orden $k$:** el siguiente símbolo depende de los $k$ anteriores.
El estado es la $k$-grama. La tasa de entropía es:

$$\bar{H}_k = H(X_n \mid X_{n-1}, \ldots, X_{n-k}) \xrightarrow{k \to \infty} \bar{H}$$

con $\bar{H}_k$ decreciente en $k$ (más contexto, menos incertidumbre).

**Modelos ocultos de Markov (HMM):** el proceso observable $Y_n$ depende de un estado
oculto $Z_n$ que evoluciona como una cadena de Markov. La tasa de entropía del proceso
observable puede calcularse mediante el algoritmo forward:

$$\bar{H} = -\lim_{n\to\infty} \frac{1}{n} \log P(Y_1, \ldots, Y_n)$$

Los HMM modelan el habla (estado = fonema oculto), texto (estado = parte del discurso)
y biología (estado = región genómica funcional).

## Aplicaciones

**Análisis de texto:** la tasa de entropía del español escrito es un indicador de la
complejidad del idioma y del modelo del lenguaje. Shannon estimó empíricamente
$\bar{H} \approx 1.0$ bits/letra para el inglés jugando al "juego de la predicción".

**Biología molecular:** el genoma puede modelarse como una cadena de Markov sobre
$\{A, C, G, T\}$. Las regiones codificantes tienen estadísticas distintas a las no
codificantes.

**Detección de anomalías:** un cambio en la tasa de entropía estimada señala un cambio
de régimen (intrusión en red, fallo en sensor, cambio de idioma).

## Ideas clave

- La cadena de Markov es el modelo estocástico con memoria mínima: el futuro depende
  del presente pero no del pasado más remoto.
- La tasa de entropía $\bar{H}$ generaliza la entropía al caso con memoria y mide la
  incertidumbre asintótica por símbolo.
- Para cadenas de Markov ergódicas, $\bar{H} = \sum_i \pi_i H(\text{fila } i \text{ de } P)$.
- El AEP se extiende a fuentes ergódicas: las secuencias típicas tienen probabilidad
  $\approx 2^{-n\bar{H}}$ y su número es $\approx 2^{n\bar{H}}$.
- LZ78 alcanza $\bar{H}$ sin conocer la distribución: la compresión universal es óptima
  asintóticamente.

## Ejercicios

1. Sea una cadena de Markov binaria con $P = \begin{pmatrix} 1-p & p \\ q & 1-q \end{pmatrix}$.
   Calcula la distribución estacionaria $\pi$ y la tasa de entropía $\bar{H}$ en función
   de $p$ y $q$.
2. ¿Para qué valores de $p$ y $q$ en el ejercicio 1 se maximiza $\bar{H}$?
   ¿Coincide con la cadena i.i.d. uniforme?
3. Estima empíricamente $\bar{H}_k$ para $k = 1, 2, 3, 4$ usando un texto en español
   de al menos 10.000 caracteres. ¿A qué valor converge?
4. Demuestra que $\bar{H} \leq H(X_1)$ usando la desigualdad de cadena de la entropía.
5. Dado un HMM con 2 estados ocultos, 3 símbolos observables y matrices de transición
   y emisión aleatorias, ¿cómo usarías el algoritmo forward para estimar $\bar{H}$?

## Referencias

- Cover, T. y Thomas, J. (2006). *Elements of Information Theory*, capítulos 4 y 16.
- Shannon, C. E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal*.
- McMillan, B. (1953). The basic theorems of information theory. *Ann. Math. Stat.*
- Ziv, J. y Lempel, A. (1978). Compression of individual sequences via variable-rate coding. *IEEE Trans. IT*.
