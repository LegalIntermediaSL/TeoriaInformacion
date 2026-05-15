# Aprendizaje Profundo desde la Teoría de la Información

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Divergencia KL y divergencias de información](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)
- [Información en aprendizaje estadístico](05-informacion-en-aprendizaje.md)

## Objetivos de aprendizaje

1. Formalizar el cuello de botella informacional y su interpretación en redes neuronales.
2. Enunciar y aplicar la cota PAC-Bayes de generalización en términos de divergencia KL.
3. Conectar el principio No Free Lunch con la compresión informacional.
4. Entender el dropout como regularización informacional y el gradiente natural en optimización.


## Intuición

¿Por qué una red neuronal con millones de parámetros generaliza bien a datos no vistos?
La teoría de la información ofrece una respuesta: la red está comprimiendo la representación
interna de los datos. Si una representación intermedia retiene poca información sobre la entrada
pero mucha sobre la etiqueta, la red ha aprendido los rasgos verdaderamente relevantes.
La divergencia KL entre la distribución de pesos aprendidos y un prior simple mide cuánta
información ha "memorizado" la red — y esa cantidad acota directamente el error de generalización.

## El cuello de botella informacional

### Definición formal

Dado un modelo con entrada $X$, representación interna $T$ y etiqueta $Y$, Tishby y
Schwartz-Moran (1999, 2017) propusieron el **cuello de botella informacional** (*Information
Bottleneck*, IB):

$$\min_{p(T|X)} \quad I(X; T) - \beta \cdot I(T; Y)$$

donde $\beta > 0$ controla el balance entre compresión (minimizar $I(X;T)$) y
relevancia (maximizar $I(T;Y)$). La solución óptima satisface:

$$\log p(T|X) = \log p(T) + \beta \log \frac{p(Y|T)}{p(Y)} + \lambda(X)$$

### El plano información

En el **plano información** $(I(X;T), I(T;Y))$, cada capa de una red neuronal ocupa un punto.
Durante el entrenamiento:

1. **Fase de ajuste:** $I(T;Y)$ crece rápidamente — la red aprende a predecir $Y$.
2. **Fase de compresión:** $I(X;T)$ decrece — la representación se vuelve más compacta.

La tesis de Tishby es que la segunda fase explica la generalización. Aunque el debate empírico
sobre cuándo ocurre la compresión continúa (Saxe et al., 2019), el marco teórico es
ampliamente aceptado.

### Cota de generalización mediante IB

Sea $\hat{R}$ el error empírico y $R^*$ el error verdadero. Bajo condiciones regulares:

$$R^* - \hat{R} \leq \sqrt{\frac{I(X;T) + \log(1/\delta)}{2m}}$$

con probabilidad $1 - \delta$ sobre muestras de tamaño $m$. Minimizar $I(X;T)$ directamente
implica mejores cotas de generalización.

## Teorema PAC-Bayes

### Enunciado (McAllester, 1999)

Sea $\mathcal{H}$ un espacio de hipótesis, $P$ un prior sobre $\mathcal{H}$ fijado antes
de ver los datos, y $Q$ un posterior aprendido a partir de $m$ muestras. Para todo $\delta > 0$,
con probabilidad $\geq 1-\delta$ sobre el muestreo:

$$\mathbb{E}_{h \sim Q}[R(h)] \leq \mathbb{E}_{h \sim Q}[\hat{R}(h)] + \sqrt{\frac{D_{\mathrm{KL}}(Q \| P) + \log(m/\delta)}{2(m-1)}}$$

### Interpretación informacional

La divergencia $D_{\mathrm{KL}}(Q \| P)$ mide cuántos bits de información sobre los datos de
entrenamiento ha incorporado el posterior $Q$ respecto al prior $P$. Redes que se alejan poco
del prior (pesos cercanos a cero, o distribuciones similares) generalizan mejor, no porque
los pesos sean pequeños, sino porque han codificado menos información del ruido de los datos.

**Aplicación práctica:** en redes bayesianas, el ELBO minimiza exactamente $D_{\mathrm{KL}}(Q \| P)$
más el error de reconstrucción:

$$\mathcal{L} = \mathbb{E}_Q[\log p(y|x, h)] - D_{\mathrm{KL}}(Q \| P)$$

## No Free Lunch desde la perspectiva informacional

El **teorema No Free Lunch** (Wolpert, 1996) establece que, promediando sobre todas las funciones
objetivo posibles, ningún algoritmo de aprendizaje supera a otro. La interpretación informacional:
si el espacio de funciones tiene entropía máxima $H(f) = \log |\mathcal{F}|$, cualquier sesgo
inductivo reduce la entropía sobre el espacio de búsqueda — ganando en algunos problemas lo que
pierde en otros. La información mutua $I(\text{datos}; \text{hipótesis elegida})$ acota
cuánto puede aprender el algoritmo sobre la función subyacente.

## Entropía del gradiente en SGD

El gradiente estocástico introduce ruido efectivo con covarianza $\Sigma(\theta) = \frac{\eta}{2B} C(\theta)$,
donde $\eta$ es la tasa de aprendizaje, $B$ el tamaño de batch y $C(\theta)$ la covarianza del
gradiente. Este ruido actúa como un proceso de difusión que favorece mínimos con alta **entropía
de volumen local** — es decir, mínimos amplios donde la función de pérdida varía poco.

La temperatura efectiva del proceso es $T_{\text{eff}} = \eta / B$, y la distribución
estacionaria de Fokker-Planck es:

$$p_{\text{estac}}(\theta) \propto \exp\!\left(-\frac{\mathcal{L}(\theta)}{T_{\text{eff}}}\right)$$

Entrenar con $\eta/B$ grande favorece mínimos planos que generalizan mejor (Keskar et al., 2017).

## Dropout como regularización informacional

El dropout (Srivastava et al., 2014) elimina aleatoriamente neuronas durante el entrenamiento con
probabilidad $p$. Desde la teoría de la información, dropout limita la información mutua entre
la activación de una neurona y la entrada:

$$I(\text{neurona}_j; X) \leq (1-p) \cdot I(\text{neurona}_j^{\text{sin dropout}}; X)$$

Esto impide que la red memorizase patrones específicos de entrenamiento a través de neuronas
individuales, forzando representaciones distribuidas con menor $I(X; T)$.

## Optimización natural y la información de Fisher

El **gradiente natural** (Amari, 1998) corrige el gradiente ordinario por la métrica del
espacio de distribuciones — la **información de Fisher**:

$$\tilde{\nabla} \mathcal{L} = F(\theta)^{-1} \nabla \mathcal{L}(\theta)$$

donde $F(\theta)_{ij} = \mathbb{E}\!\left[\frac{\partial \log p(y|x,\theta)}{\partial \theta_i} \frac{\partial \log p(y|x,\theta)}{\partial \theta_j}\right]$.

La información de Fisher es exactamente la curvatura de la divergencia KL:
$D_{\mathrm{KL}}(p_\theta \| p_{\theta+d\theta}) \approx \frac{1}{2} d\theta^\top F(\theta)\, d\theta$.
El gradiente natural da pasos de igual tamaño en el espacio de distribuciones (geometría
de la información), no en el espacio de parámetros, lo que acelera la convergencia cerca
de puntos en que $F$ es mal condicionada.

## Información mutua como medida de sobreajuste

Una red sobreajustada tiene $I(T; Y_{\text{train}}) \gg I(T; Y_{\text{test}})$. La brecha
entre ambas cantidades puede acotarse mediante $D_{\mathrm{KL}}(Q \| P)$ a través de PAC-Bayes.
Estimar $I(X;T)$ directamente en redes profundas requiere estimadores como MINE (Belghazi et al., 2018),
que aproxima $I(X;T) = \sup_{f} \mathbb{E}_{p(x,t)}[f] - \log \mathbb{E}_{p(x)p(t)}[e^f]$.

## Ideas clave

- El cuello de botella informacional formaliza la intuición de que las buenas representaciones
  comprimen la entrada ($I(X;T)$ pequeño) mientras retienen la información relevante ($I(T;Y)$ grande).
- La cota PAC-Bayes vincula la generalización directamente con $D_{\mathrm{KL}}(Q \| P)$: redes
  que no se alejan demasiado del prior generalizan mejor independientemente de su tamaño.
- El ruido de SGD no es un problema sino una ventaja: actúa como regularizador informacional
  que favorece mínimos planos con alta entropía local.
- El dropout reduce la información mutua entre neuronas y la entrada, forzando representaciones
  distribuidas y robustas.
- El gradiente natural optimiza en el espacio de distribuciones (métrica de Fisher), dando
  pasos de igual "significado informacional" en lugar de igual norma euclidiana.

## Ejercicios

1. Para una red con una capa oculta y activación sigmoide, estima $I(X;T)$ e $I(T;Y)$ en un
   problema de clasificación binaria simple usando la estimación por cuantización de Tishby.
2. Calcula la cota PAC-Bayes para una red con prior $P = \mathcal{N}(0, I)$ y posterior
   $Q = \mathcal{N}(\mu, \sigma^2 I)$ donde $\|\mu\| = 1$ y $\sigma = 0.01$, con $m = 1000$ y $\delta = 0.05$.
3. ¿Por qué entrenar con batch grande ($B$ grande) tiende a encontrar mínimos más afilados
   que batch pequeño? Argumenta usando la temperatura efectiva $T_{\text{eff}} = \eta/B$.
4. Demuestra que la matriz de información de Fisher es semidefinida positiva y que $D_{\mathrm{KL}}(p_\theta \| p_{\theta+\epsilon}) = \frac{1}{2}\epsilon^\top F(\theta) \epsilon + O(\|\epsilon\|^3)$.
5. Si aplicamos dropout con $p = 0.5$ a todas las capas de una red, ¿cómo afecta esto a las
   cotas de $I(X;T)$ según la fórmula de la sección de dropout?
6. Compara el gradiente ordinario y el gradiente natural para el problema de regresión logística
   con dos parámetros. ¿En qué dirección difieren cuando la función de pérdida tiene curvatura
   muy diferente en cada dirección?

## Véase también

- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)
- [Información en aprendizaje estadístico](05-informacion-en-aprendizaje.md)
- [Divergencia KL y divergencias de información](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Privacidad diferencial](11-privacidad-diferencial.md)


<!-- nav-start -->

---
← [Teoría de Juegos e Información Asimétrica](09-teoria-de-juegos-e-informacion.md) · [Privacidad Diferencial](11-privacidad-diferencial.md) →

<!-- nav-end -->
## Referencias

- Tishby, N. y Zaslavsky, N. (2015). Deep learning and the information bottleneck principle. *IEEE ITW*.
- McAllester, D. A. (1999). Some PAC-Bayesian theorems. *Machine Learning*, 37(3), 355–363.
- Amari, S. (1998). Natural gradient works efficiently in learning. *Neural Computation*, 10(2), 251–276.
- Keskar, N. S. et al. (2017). On large-batch training for deep learning. *ICLR 2017*.
- Belghazi, M. I. et al. (2018). MINE: Mutual information neural estimation. *ICML 2018*.
