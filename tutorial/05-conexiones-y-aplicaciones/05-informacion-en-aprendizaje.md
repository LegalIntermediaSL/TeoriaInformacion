# Información en el Aprendizaje Estadístico

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)
- [Divergencia KL y entropía cruzada](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)

## Objetivos de aprendizaje

1. Aplicar la divergencia KL y la información de Fisher al aprendizaje estadístico.
2. Entender el principio MDL (Minimum Description Length) como selección de modelos.
3. Relacionar la complejidad del modelo con el sobreajuste desde la perspectiva informacional.


## Intuición

La teoría de la información y el aprendizaje automático están profundamente conectados.
La entropía cuantifica la complejidad de una distribución; la información mutua mide la
dependencia entre variables; la divergencia KL mide el coste de una suposición equivocada.
Estos conceptos aparecen naturalmente en la cota de generalización, la selección de modelos
y la compresión óptima de representaciones.

## El principio MDL: descripción mínima

El **principio de Longitud de Descripción Mínima** (MDL, *Minimum Description Length*,
Rissanen 1978) conecta directamente aprendizaje y compresión:

> El mejor modelo para unos datos es aquel que permite comprimirlos más.

Formalmente, dado un conjunto de hipótesis $\mathcal{H}$ y datos $D$, MDL selecciona:

$$\hat{h} = \arg\min_{h \in \mathcal{H}} \bigl[L(h) + L(D \mid h)\bigr]$$

donde:
- $L(h)$ = longitud de descripción del modelo $h$ (complejidad del modelo).
- $L(D \mid h)$ = longitud de descripción de los datos dado el modelo (ajuste al dato).

Esta formulación evita el sobreajuste: modelos más complejos necesitan más bits para
describirse, penalizando la complejidad innecesaria.

**Conexión con Bayes:** MDL es equivalente a MAP (máximo a posteriori) cuando la prior
sobre modelos es $P(h) \propto 2^{-L(h)}$ (distribución de Solomonoff-Levin).

## Cotas de generalización basadas en información

Para un clasificador binario con hipótesis de clase $\mathcal{H}$ y $m$ ejemplos de entrenamiento,
la **cota de Occam** establece que con probabilidad $\geq 1 - \delta$:

$$R(h) \leq \hat{R}(h) + \sqrt{\frac{L(h) \log 2 + \log(1/\delta)}{2m}}$$

donde $R(h)$ es el riesgo real, $\hat{R}(h)$ el error empírico y $L(h)$ la longitud de
descripción de $h$.

Esta cota formaliza la navaja de Occam: hipótesis más simples (menor $L(h)$) necesitan
menos datos para garantizar buena generalización.

## Dimensión VC y entropía

La **dimensión VC** $d$ de una clase $\mathcal{H}$ es el tamaño del mayor conjunto que $\mathcal{H}$ puede
"destrozar" (asignar todas las etiquetas posibles). La dimensión VC mide la capacidad
representativa de la clase.

**Cota de Vapnik-Chervonenkis:** con probabilidad $\geq 1-\delta$:

$$R(h) \leq \hat{R}(h) + \sqrt{\frac{2d \log(em/d) + \log(2/\delta)}{m}}$$

La conexión con la entropía viene de la **función de crecimiento** $\Pi_{\mathcal{H}}(m)$,
que cuenta el número de dicotomías que $\mathcal{H}$ puede generar sobre $m$ puntos:

$$\Pi_{\mathcal{H}}(m) \leq \left(\frac{em}{d}\right)^d \quad \text{si } m > d$$

La función de crecimiento es el análogo combinatorial del número de tipos de la teoría de
tipos de información.

## Cuello de botella informacional (*Information Bottleneck*)

El **cuello de botella informacional** (Tishby, Pereira y Bialek, 1999) ofrece un marco
para encontrar representaciones comprimidas de una variable $X$ que preserven información
sobre una variable relevante $Y$:

$$\min_{T} I(X; T) \quad \text{sujeto a} \quad I(T; Y) \geq I_0$$

La variable $T$ es la representación comprimida ("cuello de botella"); $I(X; T)$ mide cuánta
información sobre $X$ se retiene; $I(T; Y)$ mide cuánta información sobre $Y$ es accesible
desde $T$.

La solución del problema de optimización define una curva de compromiso información-distorsión
análoga a la curva $R(D)$ de la teoría de tasa-distorsión.

**Interpretación en redes neuronales profundas (Tishby-Schwartz-Ziv, 2017):**
La hipótesis del cuello de botella sugiere que durante el entrenamiento, las capas ocultas
de una red neuronal primero comprimen $X$ (eliminando información irrelevante) y luego
maximizan $I(T; Y)$. Esta hipótesis es polémica y sigue siendo objeto de debate activo.

## Estimación de información mutua

Para distribuciones continuas, la información mutua $I(X; Y)$ no puede calcularse en
forma cerrada en general. El estimador **MINE** (*Mutual Information Neural Estimator*,
Belghazi et al., 2018) usa la dualidad de Donsker-Varadhan:

$$I(X; Y) = \sup_{T: \Omega \to \mathbb{R}} \mathbb{E}_{p_{XY}}[T] - \log \mathbb{E}_{p_X \otimes p_Y}[e^T]$$

donde el supremo es sobre todas las funciones medibles $T$. Se parametriza $T$ con una
red neuronal y se maximiza sobre los datos.

El estimador **k-NN de Kraskov-Stögbauer-Grassberger (KSG)** usa la distancia al $k$-ésimo
vecino más cercano en el espacio conjunto para estimar entropías diferenciales:

$$\hat{I}(X;Y) = \psi(k) - \langle \psi(n_x) + \psi(n_y) \rangle + \psi(n)$$

donde $\psi$ es la función digamma y $n_x$, $n_y$ son contadores de vecinos en las
proyecciones marginales.

## Máxima verosimilitud y minimización de KL

El principio de **máxima verosimilitud** (ML) es equivalente a minimizar la divergencia KL
entre la distribución real $p$ y el modelo $q_\theta$:

$$\hat{\theta}_{\text{ML}} = \arg\max_\theta \frac{1}{m}\sum_{i=1}^m \log q_\theta(x_i) = \arg\min_\theta D_{\text{KL}}(p \| q_\theta)$$

La entropía cruzada $H(p, q_\theta) = H(p) + D_{\text{KL}}(p \| q_\theta)$ es la función
objetivo de clasificación en redes neuronales. Minimizarla equivale a ajustar el modelo $q$
a la distribución real $p$ en el sentido de KL.

## Compresión y aprendizaje: el Teorema de No Free Lunch

El teorema de **No Free Lunch** (Wolpert-Macready, 1997) establece que ningún algoritmo
de aprendizaje supera a los demás en promedio sobre todos los problemas. En términos de
información: si no se tiene información previa sobre la distribución de los datos (prior
plana sobre todas las funciones booleanas), no es posible generalizar.

La información previa —incorporada vía la elección de la arquitectura, el bias inductivo,
la regularización o el kernel— es lo que permite la generalización. Sin compresión implícita
(prior), no hay aprendizaje.

## Ideas clave

- MDL conecta aprendizaje con compresión: el mejor modelo es el que permite la descripción
  más corta de los datos.
- Las cotas de generalización formalizan la navaja de Occam: modelos más simples generalizan
  con menos datos.
- La dimensión VC mide la capacidad de la clase de hipótesis; la función de crecimiento es
  su análogo combinatorial de los tipos de información.
- El cuello de botella informacional proporciona un marco unificador para representaciones
  comprimidas que preservan información relevante.
- La máxima verosimilitud es equivalente a minimizar KL, conectando directamente el
  entrenamiento de modelos con la teoría de la información.

## Ejercicios

1. Aplica MDL para seleccionar entre un polinomio de grado 1 y uno de grado 5 para un
   conjunto de 20 puntos. ¿Cómo codificarías los coeficientes?
2. Calcula la dimensión VC de la clase de intervalos en $\mathbb{R}$ y de la clase de
   semiespacios en $\mathbb{R}^2$.
3. ¿Por qué minimizar la entropía cruzada en clasificación es equivalente a maximizar
   la verosimilitud?
4. Dado que $I(X;T) \leq H(X)$, ¿cuál es la restricción más informativa que puede
   satisfacer el cuello de botella?
5. ¿Qué implicaciones tiene el Teorema de No Free Lunch para el diseño de algoritmos
   de aprendizaje? ¿Contradice la efectividad del aprendizaje profundo en la práctica?


<!-- nav-start -->

---
← [04 - Información cuántica](04-informacion-cuantica.md) · [Información y Termodinámica](06-informacion-y-termodinamica.md) →

<!-- nav-end -->
## Referencias

- Rissanen, J. (1978). Modeling by shortest data description. *Automatica*.
- Tishby, N., Pereira, F. y Bialek, W. (1999). The information bottleneck method. *Allerton*.
- Valiant, L. (1984). A theory of the learnable. *CACM*.
- Belghazi, M. et al. (2018). Mutual information neural estimation. *ICML 2018*.
- Cover, T. y Thomas, J. (2006). *Elements of Information Theory*, capítulo 5.

## Véase también

- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md) — introducción más accesible al mismo tema: entropía cruzada como función de pérdida, información mutua y compresión. Este artículo (05/05) es la continuación técnica con MDL, VC y el cuello de botella.
- [Complejidad de Kolmogorov](01-complejidad-de-kolmogorov.md) — el MDL es la versión práctica del principio de Kolmogorov aplicado a la selección de modelos.
- [El mapa de conexiones](08-mapa-de-conexiones.md) — cuadro unificado de todos los resultados del tutorial, incluido el papel de la información en el aprendizaje.
