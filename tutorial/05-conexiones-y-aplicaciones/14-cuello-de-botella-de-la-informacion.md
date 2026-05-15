# 14 - El cuello de botella de la información

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~22 min

El aprendizaje supervisado puede reformularse como un problema de compresión
óptima: encontrar la representación más compacta de los datos de entrada que
preserve toda la información relevante sobre las etiquetas. Ese es el núcleo del
**cuello de botella de la información** (*Information Bottleneck*, IB), un marco
que unifica teoría de la información, aprendizaje profundo y teoría
tasa-distorsión.

## Prerrequisitos

- [Teoría tasa-distorsión](../02-teoria-informacion/09-teoria-tasa-distorsion.md)
- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)
- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)

## Objetivos de aprendizaje

1. Formular el problema IB como un problema de optimización de información mutua.
2. Interpretar la curva información-información y el papel de β como temperatura.
3. Describir el algoritmo iterativo de punto fijo y su variante variacional (VIB).
4. Evaluar críticamente la hipótesis del cuello de botella en redes profundas.
5. Relacionar IB con tasa-distorsión y aplicarlo a ejemplos concretos.

## Intuición

Imagina que debes transmitir datos de entrada $X$ a través de un canal muy
estrecho hacia alguien que necesita predecir una variable objetivo $Y$. La
pregunta natural es: ¿qué partes de $X$ vale la pena transmitir?

Si $X$ es una imagen de alta resolución e $Y$ es la clase ("gato" / "perro"), la
textura del fondo, el ruido del sensor y los detalles irrelevantes no ayudan a
predecir $Y$. Un cuello de botella bien diseñado elimina esa información
superflua y retiene solo la que explica $Y$.

Este es exactamente el trade-off que formaliza el **Information Bottleneck**:
comprimir $X$ tanto como sea posible mientras se preserva la información mutua
con $Y$.

---

## 1. Definición formal del problema IB

Sea $X$ la variable de entrada, $Y$ la variable objetivo y $T$ la representación
comprimida (el cuello de botella). La restricción central es la **cadena de
Markov**:

$$Y \to X \to T$$

lo que significa que $T$ solo puede "ver" $X$, nunca $Y$ directamente. Por la
**desigualdad de procesamiento de datos** se garantiza que

$$I(T; Y) \leq I(X; Y),$$

es decir, ninguna transformación determinista de $X$ puede aumentar la
información que $T$ tiene sobre $Y$.

El problema de optimización IB (Tishby, Pereira y Bialek, 1999) es:

$$\min_{p(t \mid x)} \; I(X; T) - \beta \cdot I(T; Y),$$

donde $\beta \geq 0$ es un parámetro de Lagrange que controla el trade-off entre
**compresión** ($I(X;T)$ pequeño) y **relevancia** ($I(T;Y)$ grande).

- $\beta \to 0$: compresión máxima; $T$ no guarda nada de $X$ ni de $Y$.
- $\beta \to \infty$: relevancia máxima; $T \approx X$ (sin compresión).

La solución óptima satisface:

$$p^*(t \mid x) = \frac{p(t)}{Z(x, \beta)} \exp\!\left\lbrace \beta \sum_y p(y \mid x) \log \frac{p(y \mid t)}{p(y)} \right\rbrace,$$

donde $Z(x, \beta)$ es una constante de normalización.

---

## 2. La curva información-información

Para cada valor de $\beta$ se obtiene un punto en el plano

$$\bigl(I(X; T),\; I(T; Y)\bigr).$$

El conjunto de todos esos puntos forma la **frontera de Pareto** o curva
información-información: la frontera superior de los pares alcanzables. Ninguna
representación puede superar esta curva.

- **Zona inferior izquierda**: alta compresión, baja relevancia.
- **Zona superior derecha**: baja compresión, alta relevancia.
- **Punto óptimo** para un $\beta$ dado: el punto de la curva donde la pendiente
  es exactamente $\beta$ (análogo a la temperatura en termodinámica estadística).

La curva IB es el análogo exacto de la curva tasa-distorsión, con la distorsión
reemplazada por $-I(T;Y)$: maximizar la relevancia es minimizar la pérdida de
información sobre $Y$.

---

## 3. Algoritmo IB: ecuaciones de punto fijo

La solución se calcula iterando tres ecuaciones de punto fijo, análogas al
algoritmo de Blahut-Arimoto:

$$p(t \mid x) = \frac{p(t)}{Z(x,\beta)} \exp\!\left\lbrace -\beta \, D_{\mathrm{KL}}\!\left[p(y \mid x) \;\|\; p(y \mid t)\right] \right\rbrace,$$

$$p(t) = \sum_x p(x)\, p(t \mid x),$$

$$p(y \mid t) = \frac{1}{p(t)} \sum_x p(x)\, p(t \mid x)\, p(y \mid x).$$

El algoritmo converge a un mínimo local del funcional IB. Al igual que
Blahut-Arimoto, garantiza que $I(X;T) - \beta I(T;Y)$ no aumenta en cada
iteración.

**Complejidad**: cada iteración requiere $O(|\mathcal{X}| \cdot |\mathcal{T}|)$
operaciones. El número de iteraciones hasta convergencia depende de $\beta$ y de
la distribución conjunta $p(x, y)$.

---

## 4. IB variacional (VIB)

El algoritmo de punto fijo clásico no escala a datos de alta dimensión. Alemi
et al. (2017) propusieron el **Variational Information Bottleneck** (VIB), que:

1. Parametriza $p(t \mid x)$ mediante una red neuronal $q_\theta(t \mid x)$.
2. Parametriza $p(y \mid t)$ mediante otra red neuronal $q_\phi(y \mid t)$.
3. Usa la **cota variacional**:

$$I(X; T) \leq \mathbb{E}_{p(x)}\!\left[D_{\mathrm{KL}}\!\left[q_\theta(t \mid x) \;\|\; r(t)\right]\right],$$

donde $r(t)$ es una distribución de referencia (p. ej. $\mathcal{N}(0, I)$).

4. Combina con la cota inferior estándar de información mutua:

$$I(T; Y) \geq \mathbb{E}_{p(x,y)}\!\left[\mathbb{E}_{q_\theta(t \mid x)}\!\left[\log q_\phi(y \mid t)\right]\right].$$

El objetivo VIB resultante es:

$$\mathcal{L}_{\mathrm{VIB}} = \mathbb{E}\!\left[\log q_\phi(y \mid t)\right] - \beta \, D_{\mathrm{KL}}\!\left[q_\theta(t \mid x) \;\|\; r(t)\right].$$

Esto es idéntico al objetivo de un **VAE** condicional con factor $\beta$. El
truco de reparametrización permite diferenciarlo y entrenarlo con retropropagación
estándar.

---

## 5. La hipótesis del cuello de botella en redes profundas

Tishby y Schwartz-Ziv (2017) propusieron que el entrenamiento de redes profundas
atraviesa **dos fases**:

1. **Fase de ajuste** (*fitting*): las capas aumentan rápidamente $I(T_\ell; Y)$
   mientras $I(X; T_\ell)$ también crece — la red memoriza.
2. **Fase de compresión** (*compression*): $I(X; T_\ell)$ decrece mientras
   $I(T_\ell; Y)$ se mantiene — la red generaliza al "olvidar" información
   irrelevante de $X$.

La intuición es que la SGD primero encaja los datos y luego los comprime. Si esto
fuera universal, daría una explicación teórica de por qué las redes profundas
generalizan bien.

### El debate posterior

Saxe et al. (2018) replicaron los experimentos con distintas funciones de
activación y encontraron que:

- Con activaciones **ReLU** no se observa la fase de compresión.
- La compresión aparece principalmente con activaciones **tanh** y saturables,
  donde el estimador de información mutua basado en binning captura ruido
  estocástico, no compresión real.
- El fenómeno depende críticamente del **estimador** de $I(X; T_\ell)$ utilizado,
  no solo de la arquitectura.

Trabajos posteriores (Goldfeld et al. 2019; Amjad y Geiger 2019) reforzaron que
la compresión no es una propiedad universal del aprendizaje profundo, sino un
artefacto de la estimación en espacios continuos con estimadores de entropía
diferencial. El debate sigue abierto: la hipótesis IB ofrece intuición valiosa
pero no es un resultado establecido.

---

## 6. Aplicaciones

| Dominio | Aplicación |
|---|---|
| **NLP** | *Sentence embeddings* como cuellos de botella: comprimir el texto fuente preservando la información semántica relevante para traducción o clasificación. |
| **Biología** | Modelado de afinidades de unión proteína-ligando: $X$ = secuencia, $Y$ = afinidad experimental; $T$ = representación latente mínima. |
| **Aprendizaje federado** | Compresión IB de gradientes o representaciones antes de enviarlos al servidor, reduciendo comunicación sin sacrificar precisión. |
| **Clustering semántico** | Agrupamiento de documentos o imágenes donde la relevancia no es geometría euclidiana sino información sobre etiquetas latentes. |
| **Robustez adversarial** | VIB mejora la robustez porque la representación estocástica $T$ dificulta que perturbaciones de $X$ se propaguen a $Y$. |

---

## 7. Relación con tasa-distorsión

La teoría tasa-distorsión busca:

$$R(D) = \min_{p(\hat{x} \mid x):\, \mathbb{E}[d(x,\hat{x})] \leq D} I(X; \hat{X}).$$

El IB es un caso especial donde la "distorsión" no es una función explícita de
reconstrucción sino la pérdida de información sobre $Y$:

$$d_{\mathrm{IB}}(x, t) = -\sum_y p(y \mid x) \log \frac{p(y \mid t)}{p(y)} = D_{\mathrm{KL}}\!\left[p(y \mid x) \;\|\; p(y \mid t)\right].$$

Con esta distorsión, el problema IB se convierte exactamente en un problema
tasa-distorsión. La curva $R(D)$ resultante es la curva información-información
$I(T;Y)$ vs. $I(X;T)$, y los algoritmos de Blahut-Arimoto generalizados se
aplican directamente.

---

## 8. Ejemplo numérico: IB para fuente binaria con canal BSC

**Configuración**: Sea $X \sim \mathrm{Bernoulli}(0.5)$ e $Y = X \oplus N$, donde
$N \sim \mathrm{Bernoulli}(\epsilon)$ con $\epsilon = 0.1$ (canal BSC con
cruce de probabilidad 0.1). Calculamos la curva IB óptima para
$\beta \in \left\lbrace 0.5,\; 1,\; 2 \right\rbrace$.

**Datos relevantes**:

$$I(X; Y) = 1 - H(\epsilon) = 1 - H(0.1) \approx 1 - 0.469 = 0.531 \text{ bits}.$$

Para $T$ binario con $p(T=1 \mid X=0) = \alpha$ y $p(T=1 \mid X=1) = 1-\alpha$
(representación binaria simétrica), se puede calcular analíticamente:

| $\beta$ | $\alpha^*$ | $I(X;T)$ (bits) | $I(T;Y)$ (bits) |
|---|---|---|---|
| 0.5 | 0.50 | 0.000 | 0.000 |
| 1.0 | 0.23 | 0.459 | 0.431 |
| 2.0 | 0.05 | 0.714 | 0.521 |

**Interpretación**:

- $\beta = 0.5$: el coste de comprimir no justifica retener información; $T$ es
  constante (compresión máxima).
- $\beta = 1$: la representación retiene ~81% de $I(X;Y)$ usando ~87% de
  $H(X)$.
- $\beta = 2$: la representación casi iguala $I(X;Y) = 0.531$ bits con
  $I(X;T) = 0.714 < 1 = H(X)$; hay compresión real sin pérdida significativa
  de relevancia.

A medida que $\beta \to \infty$, $T \to X$ e $I(X;T) \to H(X) = 1$ bit,
alcanzando $I(T;Y) = I(X;Y)$.

---

## Ideas clave

- El **IB** busca la representación $T$ que minimiza $I(X;T)$ sujeto a preservar
  $I(T;Y)$, con $\beta$ controlando el trade-off.
- La **cadena de Markov** $Y \to X \to T$ y la desigualdad de procesamiento de
  datos garantizan que ninguna representación puede superar $I(X;Y)$.
- El **algoritmo iterativo** converge a mínimos del funcional IB, análogo a
  Blahut-Arimoto.
- El **VIB** hace el IB escalable mediante redes neuronales y el truco de
  reparametrización, con un objetivo equivalente al de un $\beta$-VAE.
- La **hipótesis IB** sobre redes profundas (fases de ajuste y compresión) es
  sugerente pero no universal: depende de la función de activación y del
  estimador de información mutua.
- El IB es **tasa-distorsión** con distorsión $= D_{\mathrm{KL}}[p(y|x) \| p(y|t)]$.

---

## Ejercicios

1. **Verificación de la cadena de Markov**: Demuestra que si $Y \to X \to T$
   entonces $p(y \mid x, t) = p(y \mid x)$. ¿Qué implica esto sobre la
   independencia condicional?

2. **Derivación del funcional**: A partir de la restricción lagrangiana
   $I(X;T) - \beta I(T;Y)$, deriva las ecuaciones de punto fijo del algoritmo
   IB usando el método de multiplicadores de Lagrange sobre $p(t \mid x)$.

3. **Curva información-información**: Para $X \sim \mathrm{Bernoulli}(0.5)$ e
   $Y = X$ (sin ruido), calcula analíticamente la curva IB y argumenta por qué
   es una línea recta con pendiente 1.

4. **Objetivo VIB**: Muestra que el objetivo $\mathcal{L}_{\mathrm{VIB}}$ es una
   cota inferior del funcional IB exacto. ¿Cuándo es la cota ajustada?

5. **Debate sobre compresión**: Explica en tus propias palabras por qué el
   estimador de información mutua por binning puede producir la ilusión de
   compresión con activaciones tanh pero no con ReLU. ¿Qué experimento
   diseñarías para zanjar el debate?

6. **Extensión al ejemplo BSC**: En el ejemplo numérico de la sección 8, calcula
   $I(X;T)$ e $I(T;Y)$ para $\beta = 5$ y compara con el límite $I(X;Y)$.

---

## Véase también

- [Aprendizaje profundo desde la información](10-aprendizaje-profundo-desde-la-informacion.md)
- [Geometría de la información](12-geometria-de-la-informacion.md)
- [MDL y selección de modelos](13-mdl-y-seleccion-de-modelos.md)

---


<!-- nav-start -->

---
← [13 - MDL y selección de modelos](13-mdl-y-seleccion-de-modelos.md) · →

<!-- nav-end -->
## Referencias

- Tishby, N., Pereira, F. C., & Bialek, W. (1999). *The information bottleneck
  method*. Proceedings of the 37th Annual Allerton Conference on Communication,
  Control, and Computing.
- Alemi, A. A., Fischer, I., Dillon, J. V., & Murphy, K. (2017). *Deep
  variational information bottleneck*. ICLR 2017.
  [arXiv:1612.00410](https://arxiv.org/abs/1612.00410)
- Tishby, N., & Schwartz-Ziv, R. (2017). *Opening the black box of deep neural
  networks via information*. ICLR 2017 (Workshop).
  [arXiv:1703.00810](https://arxiv.org/abs/1703.00810)
- Saxe, A. M., Bansal, Y., Dapello, J., Advani, M., Kolchinsky, A., Tracey, B.
  D., & Cox, D. D. (2018). *On the information bottleneck theory of deep
  learning*. ICLR 2018.
- Goldfeld, Z., van den Berg, E., Greenewald, K., Melnyk, I., Nguyen, N.,
  Kingsbury, B., & Polyanskiy, Y. (2019). *Estimating information flow in deep
  neural networks*. ICML 2019.
- Amjad, R. A., & Geiger, B. C. (2019). *Learning representations for neural
  network-based classification using the information bottleneck principle*.
  IEEE Transactions on Pattern Analysis and Machine Intelligence.
- Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd
  ed.). Wiley. Cap. 10 (tasa-distorsión).
