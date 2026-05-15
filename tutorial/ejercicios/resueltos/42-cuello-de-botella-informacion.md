# Ejercicio resuelto: El cuello de botella de la información

**Módulo:** 05 — Conexiones y aplicaciones  
**Artículo de referencia:** [El cuello de botella de la información](../../05-conexiones-y-aplicaciones/14-cuello-de-botella-de-la-informacion.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

**(a)** Sea $X \sim \mathrm{Bernoulli}(0.5)$ con variable relevante $Y = X$ (perfectamente correlada, sin ruido). Calcula la curva IB óptima en el plano $(I(X;T),\; I(T;Y))$ para $\beta \in \left\lbrace 0.5,\; 1,\; 2,\; \infty \right\rbrace$. ¿Qué ocurre en los límites $\beta \to 0$ y $\beta \to \infty$? ¿Cuál es el punto de máxima compresión sin pérdida de información relevante?

**(b)** Sea $X$ con tres valores equiprobables $\left\lbrace a, b, c \right\rbrace$ e $Y = f(X)$ donde $f(a) = f(b) = 0$ y $f(c) = 1$. Diseña la representación $T$ óptima para $\beta = 1$: ¿qué clustering de $X$ maximiza el objetivo $I(T;Y) - \frac{1}{\beta} \cdot I(X;T)$? Calcula $I(X;T)$ e $I(T;Y)$ para tu solución.

**(c)** En el VIB (Variational Information Bottleneck), el objetivo es maximizar $I(T;Y) - \beta \cdot I(X;T)$ donde $T \sim \mathcal{N}(\mu(x), \sigma^2(x))$. Muestra que el término $-\beta \cdot I(X;T)$ equivale a $-\beta \cdot \mathbb{E}_{p(x)}\!\left[D_{\mathrm{KL}}\!\left[q(T \mid X) \;\|\; r(T)\right]\right]$ cuando $r(T) \sim \mathcal{N}(0, 1)$ es un prior gaussiano estándar. ¿Por qué esto conecta el IB con el $\beta$-VAE?

**(d)** Una red neuronal de tres capas ocultas procesa imágenes MNIST ($X$ = 784 píxeles, $Y$ = 10 clases). Según la hipótesis de Tishby-Schwartz-Ziv, durante la fase de memorización $I(T;X)$ crece y durante la fase de compresión decrece. Si $I(X;Y) \approx 2.0$ bits y la red alcanza $I(T;Y) \approx 1.9$ bits en la capa final, ¿qué fracción de la información relevante se retiene? ¿Por qué el trabajo de Saxe et al. cuestiona que la compresión sea una propiedad universal del entrenamiento?

---

## Solución

### Parte (a): Curva IB para fuente binaria perfectamente correlada

**Configuración.** $X \sim \mathrm{Bernoulli}(0.5)$, $Y = X$. Por tanto $H(X) = 1$ bit, $H(Y) = 1$ bit e $I(X;Y) = 1$ bit. La cadena de Markov es $Y \to X \to T$, con $Y = X$ este caso es el más favorable: toda la información de $X$ es relevante para $Y$.

**Cálculo analítico.** Con $Y = X$ la distorsión IB es:

$$d_{\mathrm{IB}}(x, t) = D_{\mathrm{KL}}\!\left[p(y \mid x) \;\|\; p(y \mid t)\right].$$

Pero $p(y \mid x) = \mathbf{1}[y = x]$ (distribución degenerada), luego cualquier $T$ que mezcle los dos valores de $X$ introduce distorsión. Para $T$ binario simétrico con $p(T=1 \mid X=0) = \alpha$ y $p(T=1 \mid X=1) = 1 - \alpha$:

$$I(X;T) = 1 - H(\alpha), \qquad I(T;Y) = 1 - H(\alpha).$$

Dado que $Y = X$ sin ruido, las dos cantidades son idénticas: $I(T;Y) = I(X;T)$ para todo $\alpha$. La curva IB es la **diagonal** del cuadrado $[0,1]^2$:

$$I(T;Y) = I(X;T), \quad I(X;T) \in [0, 1] \text{ bit}.$$

**Puntos óptimos para cada $\beta$:**

| $\beta$ | $\alpha^*$ | $I(X;T)$ (bits) | $I(T;Y)$ (bits) | Interpretación |
|---|---|---|---|---|
| 0.5 | 0.5 | 0.000 | 0.000 | Compresión total; $T$ constante |
| 1.0 | cualquier $\alpha$ | cualquier valor | mismo valor | Toda la curva es óptima |
| 2.0 | 0.0 (o 1.0) | 1.000 | 1.000 | $T = X$; sin compresión |
| $\infty$ | 0.0 (o 1.0) | 1.000 | 1.000 | $T = X$; sin compresión |

**Límites:**

- $\beta \to 0$: el coste de comprimir es infinitamente más valioso que la relevancia. El óptimo es $\alpha = 0.5$, que da $T$ constante ($I(X;T) = 0$, $I(T;Y) = 0$).
- $\beta \to \infty$: la relevancia es infinitamente más valiosa que la compresión. El óptimo es $\alpha = 0$ (o $\alpha = 1$), que da $T = X$ ($I(X;T) = H(X) = 1$ bit, $I(T;Y) = 1$ bit).

**Punto de máxima compresión sin pérdida:** como $I(T;Y) = I(X;T)$ en todo momento, cualquier punto en la diagonal alcanza $I(T;Y) = I(X;T)$. Sin embargo, el punto que maximiza la compresión manteniendo $I(T;Y) = I(X;Y) = 1$ bit es $\alpha = 0$, es decir, $T = X$: no existe compresión real sin pérdida de relevancia en este caso. Esto refleja un hecho fundamental: cuando toda la información de $X$ es relevante para $Y$, comprimir $X$ implica necesariamente perder información sobre $Y$.

---

### Parte (b): Clustering óptimo para $X$ con tres valores equiprobables

**Distribuciones.** $p(X = a) = p(X = b) = p(X = c) = 1/3$. La variable $Y$ vale 0 para $X \in \left\lbrace a, b \right\rbrace$ y 1 para $X = c$, luego:

$$p(Y = 0) = 2/3, \quad p(Y = 1) = 1/3.$$

$$H(Y) = -\frac{2}{3}\log_2\frac{2}{3} - \frac{1}{3}\log_2\frac{1}{3} \approx 0.918 \text{ bits}.$$

**Candidatos a clustering.** Se consideran tres particiones posibles de $\left\lbrace a, b, c \right\rbrace$:

- **Clustering C1**: $T = \left\lbrace \{a,b\},\; \{c\} \right\rbrace$ — agrupa los elementos con la misma imagen por $f$.
- **Clustering C2**: $T = \left\lbrace \{a,c\},\; \{b\} \right\rbrace$ — agrupa $a$ con $c$.
- **Clustering C3**: $T = X$ — sin compresión, tres clústeres.

**Evaluación del objetivo $\mathcal{F} = I(T;Y) - I(X;T)$ para $\beta = 1$:**

**C1: $T_0 = \left\lbrace a,b \right\rbrace$, $T_1 = \left\lbrace c \right\rbrace$.**

$$p(T_0) = 2/3, \quad p(T_1) = 1/3.$$

Dada la cadena de Markov $Y \to X \to T$:

$$p(Y=0 \mid T_0) = 1, \quad p(Y=1 \mid T_0) = 0,$$
$$p(Y=0 \mid T_1) = 0, \quad p(Y=1 \mid T_1) = 1.$$

Entonces $H(Y \mid T) = 0$, luego $I(T;Y) = H(Y) - H(Y \mid T) = 0.918$ bits.

Para $I(X;T)$ con C1, $T$ es función determinista de $X$ que agrupa $a$ y $b$:

$$H(T) = H(2/3,\; 1/3) \approx 0.918 \text{ bits}.$$
$$H(X \mid T): \text{ dado } T_0,\; X \in \left\lbrace a, b \right\rbrace \text{ con prob. } 1/2 \text{ cada uno} \Rightarrow H(X \mid T_0) = 1 \text{ bit}.$$
$$\text{Dado } T_1,\; X = c \text{ con certeza} \Rightarrow H(X \mid T_1) = 0.$$
$$H(X \mid T) = \frac{2}{3} \cdot 1 + \frac{1}{3} \cdot 0 = \frac{2}{3} \text{ bits}.$$
$$I(X;T) = H(X) - H(X \mid T) = \log_2 3 - \frac{2}{3} \approx 1.585 - 0.667 = 0.918 \text{ bits}.$$

Objetivo C1: $\mathcal{F}_1 = 0.918 - 0.918 = 0.000$ bits.

**C2: $T_0 = \left\lbrace b \right\rbrace$, $T_1 = \left\lbrace a, c \right\rbrace$.**

$$p(T_0) = 1/3, \quad p(T_1) = 2/3.$$

$$p(Y=0 \mid T_0) = 1, \quad p(Y=1 \mid T_0) = 0,$$
$$p(Y=0 \mid T_1) = p(Y=0, X=a) / p(T_1) = (1/3)/(2/3) = 1/2,$$
$$p(Y=1 \mid T_1) = (1/3)/(2/3) = 1/2.$$

$$H(Y \mid T) = \frac{1}{3} \cdot 0 + \frac{2}{3} \cdot H(1/2, 1/2) = \frac{2}{3} \cdot 1 = 0.667 \text{ bits}.$$
$$I(T;Y) = 0.918 - 0.667 = 0.251 \text{ bits}.$$

$$H(X \mid T): \text{ dado } T_0,\; X = b \text{ con certeza} \Rightarrow 0. \text{ Dado } T_1,\; X \in \left\lbrace a, c \right\rbrace \text{ equiprobables} \Rightarrow 1 \text{ bit}.$$
$$H(X \mid T) = \frac{1}{3} \cdot 0 + \frac{2}{3} \cdot 1 = 2/3 \text{ bits}.$$
$$I(X;T) = \log_2 3 - 2/3 \approx 0.918 \text{ bits}.$$

Objetivo C2: $\mathcal{F}_2 = 0.251 - 0.918 = -0.667$ bits.

**C3: $T = X$ (sin compresión).**

$$I(T;Y) = I(X;Y) = H(Y) - H(Y \mid X) = H(Y) - 0 = 0.918 \text{ bits}.$$
$$I(X;T) = H(X) = \log_2 3 \approx 1.585 \text{ bits}.$$

Objetivo C3: $\mathcal{F}_3 = 0.918 - 1.585 = -0.667$ bits.

**Conclusión:** El clustering C1 que agrupa $\left\lbrace a, b \right\rbrace$ (los dos valores con la misma imagen $f(x) = 0$) maximiza el objetivo con $\mathcal{F}_1 = 0$ bits. Todos los demás clusterings obtienen valores negativos.

$$\boxed{I(X;T) = 0.918 \text{ bits}, \quad I(T;Y) = 0.918 \text{ bits} \quad \text{(clustering C1)}.}$$

La representación óptima colapsa exactamente los elementos de $X$ que son indistinguibles para $Y$: $a$ y $b$ producen el mismo $Y = 0$, por lo que no hay información en distinguirlos para predecir $Y$.

---

### Parte (c): VIB y conexión con el $\beta$-VAE

**Descomposición de $I(X;T)$.** Por definición:

$$I(X;T) = \mathbb{E}_{p(x,t)}\!\left[\log \frac{p(t \mid x)}{p(t)}\right] = \mathbb{E}_{p(x)}\!\left[D_{\mathrm{KL}}\!\left[p(t \mid x) \;\|\; p(t)\right]\right].$$

**Cota variacional.** La distribución marginal $p(t) = \int p(t \mid x)\, p(x)\, dx$ es intrateable en general. Se introduce un prior tractable $r(t)$ para acotar superiormente $I(X;T)$:

$$D_{\mathrm{KL}}\!\left[p(t \mid x) \;\|\; p(t)\right] \leq D_{\mathrm{KL}}\!\left[p(t \mid x) \;\|\; r(t)\right],$$

pues $D_{\mathrm{KL}}\!\left[p(t) \;\|\; r(t)\right] \geq 0$ implica que $r(t)$ es menos eficiente que $p(t)$ para comprimir. Integrando sobre $p(x)$:

$$I(X;T) \leq \mathbb{E}_{p(x)}\!\left[D_{\mathrm{KL}}\!\left[q_\theta(t \mid x) \;\|\; r(t)\right]\right].$$

Con el encoder gaussiano $q_\theta(t \mid x) = \mathcal{N}(\mu_\theta(x),\, \sigma^2_\theta(x))$ y prior $r(t) = \mathcal{N}(0, 1)$, la divergencia KL tiene forma cerrada:

$$D_{\mathrm{KL}}\!\left[\mathcal{N}(\mu, \sigma^2) \;\|\; \mathcal{N}(0,1)\right] = \frac{1}{2}\!\left(\mu^2 + \sigma^2 - \ln \sigma^2 - 1\right).$$

**Objetivo VIB resultante:**

$$\mathcal{L}_{\mathrm{VIB}} = \mathbb{E}_{p(x,y)}\!\left[\mathbb{E}_{q_\theta(t \mid x)}\!\left[\log q_\phi(y \mid t)\right]\right] - \beta \cdot \mathbb{E}_{p(x)}\!\left[D_{\mathrm{KL}}\!\left[q_\theta(t \mid x) \;\|\; r(t)\right]\right].$$

**Conexión con el $\beta$-VAE.** El $\beta$-VAE minimiza:

$$\mathcal{L}_{\beta\text{-VAE}} = \mathbb{E}_{q_\theta(z \mid x)}\!\left[\log p_\phi(x \mid z)\right] - \beta \cdot D_{\mathrm{KL}}\!\left[q_\theta(z \mid x) \;\|\; r(z)\right].$$

La estructura es formalmente idéntica:
- En ambos casos hay un encoder $q_\theta(\cdot \mid x)$ gaussiano y un prior $r(\cdot) = \mathcal{N}(0, I)$.
- El término de reconstrucción $\log p_\phi(x \mid z)$ (VAE) corresponde al término de relevancia $\log q_\phi(y \mid t)$ (VIB): en el VAE se reconstruye la entrada completa $x$; en el VIB solo se predice la etiqueta $y$.
- El factor $\beta$ controla en ambos casos el trade-off entre calidad de reconstrucción/relevancia y compresión del espacio latente.

La diferencia conceptual es que el VAE busca comprimir $x$ para reconstruirlo (información autosuficiente), mientras que el VIB busca comprimir $x$ para predecir $y$ (información relevante). El $\beta$-VAE es, en este sentido, un IB con distorsión de reconstrucción en lugar de pérdida de información sobre etiquetas.

---

### Parte (d): Hipótesis IB en redes profundas y debate Saxe et al.

**Fracción de información relevante retenida.**

$$\frac{I(T;Y)}{I(X;Y)} = \frac{1.9}{2.0} = 0.95.$$

La capa final retiene el **95%** de la información relevante disponible en los datos. El 5% restante (0.1 bits) se pierde irrecuperablemente por la desigualdad de procesamiento de datos.

**La hipótesis Tishby-Schwartz-Ziv.** El argumento es que el SGD induce dos fases observables al trazar $(I(X;T_\ell),\; I(T_\ell;Y))$ para cada capa $\ell$ a lo largo del entrenamiento:

1. **Fase de ajuste (memorización):** $I(T_\ell;Y)$ crece rápidamente porque la red aprende a discriminar clases. Al mismo tiempo $I(X;T_\ell)$ crece porque la red retiene mucha información sobre la entrada.

2. **Fase de compresión (generalización):** $I(X;T_\ell)$ decrece mientras $I(T_\ell;Y)$ permanece estable. La red "olvida" información irrelevante de $X$ — ruido de fondo, variaciones sin valor predictivo — y retiene solo la señal discriminativa.

Si esto fuera universal, la SGD actuaría como un optimizador IB natural: primero memoriza y luego comprime, alcanzando espontáneamente representaciones cercanas a la frontera óptima.

**El debate Saxe et al. (2018).**

Saxe et al. replicaron los experimentos con distintas arquitecturas y encontraron tres problemas fundamentales:

1. **Dependencia de la función de activación.** Con activaciones **ReLU** no se observa la fase de compresión: $I(X;T_\ell)$ crece monótonamente durante todo el entrenamiento. La compresión aparece principalmente con activaciones **tanh** y otras funciones saturables.

2. **Artefacto del estimador.** El estimador de $I(X;T_\ell)$ utilizado por Tishby y Schwartz-Ziv se basa en binning del espacio de activaciones. Con tanh, las activaciones se concentran en los extremos $\left\lbrace -1, +1 \right\rbrace$ al saturarse, lo que el estimador por binning interpreta erróneamente como reducción de entropía (compresión). En realidad, lo que crece es el ruido estocástico del SGD en las zonas de saturación.

3. **El estimador no mide la cantidad correcta.** Para variables continuas $T$, la información mutua $I(X;T)$ depende del estimador utilizado: binning, estimadores $k$-NN, o kernels dan resultados cualitativamente distintos. Con ReLU, donde las activaciones son no saturables, el estimador capta la variabilidad real sin artefactos de saturación.

**Síntesis.** La fracción de información relevante retenida (95% en el ejemplo) es una cantidad observable y sin ambigüedad: $I(T;Y)$ puede estimarse porque $Y$ es discreta. La controversia recae sobre $I(X;T_\ell)$ con $X$ y $T_\ell$ continuos de alta dimensión. La hipótesis IB ofrece una intuición valiosa sobre el aprendizaje como compresión, pero no es un resultado probado: la compresión espontánea de representaciones intermedias no es universal y depende críticamente de la función de activación y del estimador empleado.

---

## Ideas clave del ejercicio

1. Cuando $Y = X$ (sin ruido), la curva IB es la diagonal del plano: toda compresión tiene coste en relevancia y no existe punto de "máxima compresión sin pérdida". El IB solo puede comprimir lo que es irrelevante para $Y$.

2. El clustering óptimo para $\beta = 1$ agrupa exactamente los valores de $X$ que son indistinguibles para $Y$ (misma imagen bajo $f$). La solución IB redescubre la partición inducida por la función objetivo.

3. El término $-\beta \cdot I(X;T)$ del VIB se acota superiormente mediante $-\beta \cdot D_{\mathrm{KL}}\!\left[q(T \mid X) \;\|\; r(T)\right]$ con prior gaussiano. Esto hace el objetivo tratable y produce una función de pérdida formalmente idéntica a la del $\beta$-VAE, revelando que ambos modelos son casos especiales del mismo principio de compresión.

4. La fracción de información relevante retenida $I(T;Y)/I(X;Y)$ es una métrica robusta del rendimiento informacional de una red: valores cercanos a 1 indican que la red se acerca al límite teórico de Bayes.

5. El debate Saxe et al. no invalida el marco IB, sino que revela que la compresión espontánea de representaciones no es universal: depende de la función de activación (tanh vs. ReLU) y del estimador de información mutua, no solo de la arquitectura o del optimizador.
