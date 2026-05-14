# Teoría de la Tasa-Distorsión

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)
- [Teorema de Shannon](08-teorema-de-shannon-capacidad.md)

## Objetivos de aprendizaje

1. Definir la función de tasa-distorsión R(D) y su interpretación.
2. Calcular R(D) para la fuente Bernoulli y la fuente gaussiana.
3. Entender el compromiso fundamental entre tasa de compresión y distorsión.


## Intuición

La codificación de fuente sin pérdida busca comprimir hasta la entropía $H(X)$ sin perder ningún bit. Pero en muchos contextos prácticos —audio, imagen, vídeo— cierta pérdida de calidad es aceptable. La **teoría de la tasa-distorsión** estudia la pregunta: ¿cuántos bits por símbolo se necesitan si se tolera un error de reconstrucción promedio de a lo sumo $D$?

## Medidas de distorsión

Una **función de distorsión** $d: \mathcal{X} \times \hat{\mathcal{X}} \to [0,\infty)$ mide el coste de reconstruir $\hat{x}$ cuando el símbolo original era $x$. Las elecciones más comunes son:

- **Distorsión Hamming:** $d(x,\hat{x}) = \mathbf{1}[x \neq \hat{x}]$ (error por símbolo).
- **Error cuadrático medio (MSE):** $d(x,\hat{x}) = (x-\hat{x})^2$.
- **PSNR en imágenes:** derivado del MSE en escala logarítmica.

La distorsión media de un código es $D = \mathbb{E}[d(X,\hat{X})]$.

## La función de tasa-distorsión

Dado un nivel de distorsión tolerable $D \geq 0$, la **función de tasa-distorsión** $R(D)$ es la tasa mínima de compresión que permite una distorsión media $\leq D$:

$$R(D) = \min_{p(\hat{x}|x): \mathbb{E}[d(X,\hat{X})] \leq D} I(X;\hat{X})$$

La minimización es sobre todas las distribuciones condicionales $p(\hat{x}|x)$ que inducen una distorsión media $\leq D$. $I(X;\hat{X})$ es la información mutua entre la fuente y su reconstrucción.

**Propiedades de $R(D)$:**
- $R(0) = H(X)$ (sin distorsión, la tasa mínima es la entropía).
- $R(D) = 0$ para $D \geq D_{\max}$, donde $D_{\max}$ es la distorsión de ignorar la entrada.
- $R(D)$ es una función convexa y decreciente en $D$.

## El teorema de codificación con pérdida

**Teorema (Shannon, 1959).** Para una fuente i.i.d. $X^n$ y una función de distorsión $d$, existe un código de longitud $nR$ bits que permite reconstruir $\hat{X}^n$ con distorsión media $\leq D + \epsilon$ si y solo si $R > R(D)$.

El resultado tiene dos partes:

- **Alcanzabilidad:** para cualquier $R > R(D)$, existe un código con tasa $R$ y distorsión $\leq D$.
- **Cota inferior:** cualquier código con tasa $R < R(D)$ necesariamente incurre en distorsión $> D$.

La demostración de alcanzabilidad usa codebooks aleatorios: se eligen $2^{nR}$ secuencias $\hat{x}^n$ al azar según la distribución marginales óptima $p^*(\hat{x})$, y se asigna a cada $x^n$ el índice del codeword más cercano en distorsión.

## Ejemplos canónicos

![Curva de tasa-distorsión R(D): eje X es la distorsión permitida D (de 0 a D_max), eje Y es la tasa mínima de compresión R en bits/símbolo. La curva decrece monótonamente y es convexa. Se muestran dos curvas: Bernoulli(1/2) con hamming distortion (R(D)=1-H_b(D) para 0≤D≤1/2) y Gaussiana(0,σ²) con error cuadrático (R(D)=½·log(σ²/D) para D≤σ²). Ambas alcanzan R=0 en D=D_max.](../imagenes/rate-distortion-curve.svg)

### Fuente Bernoulli con distorsión Hamming

Sea $X \sim \text{Ber}(1/2)$ y $d$ la distorsión Hamming. Entonces:
$$R(D) = 1 - H_b(D), \quad 0 \leq D \leq 1/2$$

donde $H_b(D) = -D\log D - (1-D)\log(1-D)$ es la entropía binaria. Para $D > 1/2$, $R(D) = 0$ (se puede ignorar la fuente y adivinar).

**Interpretación:** para reproducir cada bit con tasa de error $\leq D$, se necesitan $1 - H_b(D)$ bits por símbolo. Con $D = 0.1$ (10% de error), basta con $\approx 0.53$ bits; sin error se necesita 1 bit completo.

### Fuente Gaussiana con MSE

Sea $X \sim \mathcal{N}(0, \sigma^2)$ y $d(x,\hat{x}) = (x-\hat{x})^2$. Entonces:
$$R(D) = \frac{1}{2}\log\frac{\sigma^2}{D}, \quad 0 \leq D \leq \sigma^2$$

Con $D = \sigma^2$ (reconstruir siempre el promedio), $R(D) = 0$. Cada bit extra de tasa cuadruplica la fidelidad (reduce $D$ a la mitad cada bit adicional).

La fuente Gaussiana es la de **mayor tasa-distorsión** entre todas las fuentes de igual varianza: necesita más bits que cualquier otra fuente para alcanzar la misma calidad de reconstrucción. Esta propiedad extremal es clave en la teoría.

## La dualidad tasa-distorsión y capacidad de canal

Hay una dualidad matemática profunda entre la función de tasa-distorsión $R(D)$ y la capacidad de canal $C(\text{SNR})$:

- En la tasa-distorsión: se minimiza la información mutua $I(X;\hat{X})$ sujeto a la distorsión.
- En la capacidad: se maximiza la información mutua $I(X;Y)$ sujeto a la restricción de potencia.

El **teorema de separación fuente-canal** de Shannon establece que en comunicación punto a punto se puede separar el problema de compresión (alcanzar $R(D)$) del de transmisión por canal (alcanzar la capacidad $C$), sin pérdida de optimalidad.

## Cuantización vectorial

En la práctica, la codificación con pérdida óptima es la **cuantización vectorial**: dado un vector $x^n$, se le asigna el índice del codeword más cercano de un codebook de $2^{nR}$ vectores. Con $n \to \infty$, la cuantización vectorial puede alcanzar $R(D)$.

La cuantización escalar (símbolo a símbolo) es subóptima en general. La **relajación en cuantización** de Shannon muestra que la cuantización vectorial mejora al escalar en $\leq 0.255$ bits.

Algoritmos prácticos como JPEG (DCT + cuantización escalar), MP3 (banco de filtros + cuantización) y los codecs de vídeo H.264/H.265 son aproximaciones prácticas a la frontera tasa-distorsión.

## Tasa-distorsión para imágenes: intuición

En JPEG:
1. La imagen se divide en bloques de $8 \times 8$ píxeles.
2. Se aplica la DCT para transformar al dominio de frecuencias.
3. Los coeficientes de alta frecuencia (donde el ojo humano es menos sensible) se cuantifican con paso grande.
4. Los coeficientes resultantes se codifican con Huffman.

El paso de cuantización (paso 3) introduce pérdida; el teorema de tasa-distorsión garantiza que existe un límite inferior a la distorsión alcanzable con una tasa dada.

## Ideas clave

- $R(D)$ describe la tasa mínima de bits por símbolo para tolerar una distorsión promedio $D$.
- Para la fuente Bernoulli: $R(D) = 1 - H_b(D)$; para la Gaussiana: $R(D) = \frac{1}{2}\log(\sigma^2/D)$.
- La demostración del teorema usa codebooks aleatorios; la clave es que el típico set de secuencias de distorsión cubre el espacio.
- La dualidad con capacidad de canal formaliza la intuición de que comprimir y transmitir son problemas inversos.
- Codecs modernos (JPEG, MP3, H.265) son aproximaciones prácticas a la frontera de tasa-distorsión.

## Ejercicios

1. Calcula $R(D)$ para una fuente Bernoulli con $p = 1/4$ y distorsión Hamming.
2. Compara la tasa necesaria para reproducir una fuente Gaussiana $\mathcal{N}(0,1)$ con distorsión $D = 0.01$ y $D = 0.25$.
3. ¿Qué ocurre con $R(D)$ cuando $D \geq D_{\max}$? Interpreta el resultado.
4. Una fuente binaria tiene símbolos 0 y 1 con $p(0) = 3/4$. Con distorsión Hamming, ¿cuántos bits se necesitan para reproducirla con 5% de error?
5. Explica por qué la cuantización vectorial es asintóticamente óptima mientras que la escalar no lo es.

## Véase también

- [Teorema de Shannon y capacidad](08-teorema-de-shannon-capacidad.md)
- [Entropía diferencial](10-entropia-diferencial.md)


## Referencias

- Cover, T. y Thomas, J. (2006). *Elements of Information Theory*, 2ª ed., capítulo 10.
- Shannon, C. E. (1959). Coding theorems for a discrete source with a fidelity criterion. *IRE National Convention Record*.
- Gersho, A. y Gray, R. M. (1992). *Vector Quantization and Signal Compression*. Kluwer.
