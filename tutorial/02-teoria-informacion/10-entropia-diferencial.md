# Entropía Diferencial y Fuentes Continuas

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Entropía e incertidumbre](01-entropia-incertidumbre.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)

## Objetivos de aprendizaje

1. Definir la entropía diferencial h(X) para variables continuas.
2. Calcular h(X) para distribuciones gaussianas y uniformes.
3. Explicar por qué h(X) puede ser negativa y cómo difiere de H(X).


## Intuición

La entropía de Shannon se definió para variables aleatorias discretas. Las fuentes reales —audio,
temperatura, señales analógicas— son continuas. La **entropía diferencial** extiende la idea de
incertidumbre a distribuciones continuas, pero con diferencias importantes: puede ser negativa,
no está acotada inferiormente, y su interpretación requiere cuidado.

## Definición formal

Sea $X$ una variable aleatoria continua con densidad $f(x)$. La **entropía diferencial** es:

$$h(X) = -\int_{-\infty}^{\infty} f(x) \log f(x) \, dx$$

donde el logaritmo está en base 2 (bits) o en base $e$ (nats).

**Diferencias respecto a la entropía discreta:**

| Propiedad | Discreta $H(X)$ | Diferencial $h(X)$ |
|-----------|----------------|---------------------|
| Rango | $[0, \log|\mathcal{X}|]$ | $(-\infty, +\infty)$ |
| Invarianza | Bajo biyecciones | No: $h(aX) = h(X) + \log|a|$ |
| Significado | Bits necesarios para codificar | Límite de bits/símbolo al cuantizar |

## Ejemplos canónicos

### Distribución uniforme en $[0, a]$

$$f(x) = 1/a, \quad h(X) = \log a$$

Para $a < 1$, la entropía diferencial es negativa. No es una contradicción: refleja que la
distribución está más concentrada que una distribución uniforme en $[0,1]$.

### Distribución exponencial con parámetro $\lambda$

$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0, \quad h(X) = 1 - \log \lambda \text{ (nats)}$$

### Distribución Gaussiana $\mathcal{N}(\mu, \sigma^2)$

$$h(X) = \frac{1}{2} \log(2\pi e \sigma^2)$$

La media no afecta a la entropía; solo importa la varianza.

## Máxima entropía para varianza fija

**Teorema.** Entre todas las distribuciones con media $\mu$ y varianza $\sigma^2$, la distribución
Gaussiana $\mathcal{N}(\mu, \sigma^2)$ **maximiza** la entropía diferencial.

**Demostración (esquema):** sea $g(x)$ cualquier distribución con varianza $\sigma^2$. Entonces:

$$h(g) - h(\mathcal{N}) = -\int g \log g + \int g \log \mathcal{N} \leq 0$$

donde la desigualdad viene de que $D_{\text{KL}}(g \| \mathcal{N}) \geq 0$.

**Consecuencias prácticas:**
- El ruido Gaussiano es el más "destructivo" entre todos los ruidos de igual potencia.
- Justifica el teorema de Shannon-Hartley: la capacidad del canal Gaussiano $C = \frac{1}{2}\log(1+\text{SNR})$ se alcanza con señales Gaussianas.
- En aprendizaje automático, modelos que asumen Gaussiana son conservadores en el sentido de
  información: están haciendo la suposición de mínima información extra.

## Entropía diferencial y cuantización

La entropía diferencial surge naturalmente al cuantizar: si se discretiza $X$ en intervalos de
tamaño $\Delta$, la entropía de la variable discreta resultante satisface:

$$H(X_\Delta) \approx h(X) - \log \Delta$$

Para $\Delta \to 0$, $H(X_\Delta) \to \infty$, pero la diferencia $H(X_\Delta) - H(Y_\Delta)$
converge a $h(X) - h(Y)$. Por esto la entropía diferencial es útil para comparar distribuciones
aunque su valor absoluto no tenga interpretación directa en bits.

## Información mutua diferencial

La información mutua es invariante bajo transformaciones biyectivas y tiene la misma interpretación
tanto en el caso discreto como en el continuo:

$$I(X;Y) = h(X) - h(X|Y) = h(Y) - h(Y|X)$$

La información mutua diferencial es **siempre no negativa** y se anula si y solo si $X$ e $Y$
son independientes. Es la cantidad que aparece en la capacidad de canal:

$$C = \max_{p(x)} I(X;Y)$$

## La desigualdad de potencia de entropía

**Entropy Power Inequality (EPI):** para variables independientes $X$ e $Y$:

$$2^{2h(X+Y)/n} \geq 2^{2h(X)/n} + 2^{2h(Y)/n}$$

donde $n$ es la dimensión. Para variables escalares:

$$e^{2h(X+Y)} \geq e^{2h(X)} + e^{2h(Y)}$$

La igualdad se da si y solo si $X$ e $Y$ son Gaussianas con varianzas proporcionales.

**Interpretación:** la "potencia de entropía" $e^{2h(X)}$ se comporta como la varianza de una
Gaussiana de igual entropía. La EPI generaliza la ley de adición de varianzas al mundo de la entropía.

## Información de Fisher

La **información de Fisher** $J(X)$ de una distribución con densidad $f(x; \theta)$ mide cuánta
información contiene una muestra sobre el parámetro $\theta$:

$$J(\theta) = \mathbb{E}\left[\left(\frac{\partial}{\partial \theta} \log f(X;\theta)\right)^2\right]$$

Para la familia de localización ($f(x;\mu) = f(x-\mu)$), la información de Fisher satisface la
**desigualdad de Cramér-Rao:** cualquier estimador insesgado $\hat{\mu}$ satisface
$\text{Var}[\hat{\mu}] \geq 1/J(\mu)$.

**Relación con la entropía:** para la familia de localización gaussiana,
$J(\mu) = 1/\sigma^2$ y $h(X) = \frac{1}{2}\log(2\pi e/J)$. La información de Fisher y la
entropía diferencial son conceptos complementarios: la entropía mide incertidumbre global
mientras que Fisher mide sensibilidad local a cambios del parámetro.

## Canal Gaussiano aditivo

El **canal Gaussiano aditivo** es el modelo estándar de comunicación analógica:

$$Y = X + Z, \quad Z \sim \mathcal{N}(0, N), \quad \mathbb{E}[X^2] \leq P$$

La capacidad es:
$$C = \frac{1}{2}\log\left(1 + \frac{P}{N}\right) \text{ bits/uso}$$

La demostración usa que:
1. La señal óptima es $X \sim \mathcal{N}(0, P)$ (maximiza $h(X)$).
2. $h(Y) = h(X + Z) \leq \frac{1}{2}\log(2\pi e(P+N))$ con igualdad para $X$ Gaussiana.
3. $h(Y|X) = h(Z) = \frac{1}{2}\log(2\pi eN)$.
4. $I(X;Y) = h(Y) - h(Y|X) = \frac{1}{2}\log(1 + P/N)$.

## AEP para fuentes continuas

El **teorema de equipartición asintótica** (AEP) tiene un análogo continuo: para una fuente
estacionaria ergódica continua, la probabilidad de la secuencia típica satisface:

$$-\frac{1}{n}\log f(X_1,\ldots,X_n) \to h(X) \quad \text{en probabilidad}$$

Las secuencias típicas ocupan un volumen $\approx 2^{nh(X)}$ en $\mathbb{R}^n$, que crece
exponencialmente. Para representar $n$ muestras con error de cuantización $\epsilon$,
se necesitan $\approx n(h(X) + \log(1/\epsilon))$ bits.

## Ideas clave

- La entropía diferencial $h(X) = -\int f\log f$ puede ser negativa; su valor absoluto no
  tiene interpretación directa en bits, pero las diferencias sí.
- La Gaussiana maximiza la entropía entre distribuciones con varianza fija.
- La información mutua $I(X;Y) = h(X) - h(X|Y)$ es siempre no negativa e invariante de
  escala.
- La EPI generaliza la adición de varianzas al dominio de la entropía.
- La capacidad del canal Gaussiano $C = \frac{1}{2}\log(1+P/N)$ se obtiene directamente
  de la entropía diferencial de la Gaussiana.

## Ejercicios

1. Calcula $h(X)$ para $X \sim \text{Uniforme}[0, 1]$, $X \sim \text{Exponencial}(2)$ y
   $X \sim \mathcal{N}(3, 4)$.
2. Demuestra que $h(aX+b) = h(X) + \log|a|$. ¿Por qué esta fórmula tiene sentido intuitivo?
3. Muestra que $h(X, Y) \leq h(X) + h(Y)$ con igualdad si y solo si $X$ e $Y$ son independientes.
4. ¿Por qué la capacidad del canal Gaussiano depende solo del cociente $P/N$ y no de $P$ o
   $N$ por separado?
5. La desigualdad de Cramér-Rao establece $\text{Var}[\hat{\mu}] \geq 1/J(\mu)$. Para una
   Gaussiana, ¿qué estimador alcanza esta cota?

## Véase también

- [Teoría de tasa-distorsión](09-teoria-tasa-distorsion.md)
- [Información y termodinámica](../05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md)


## Referencias

- Cover, T. y Thomas, J. (2006). *Elements of Information Theory*, 2ª ed., capítulos 8-9.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*.
- Stam, A. J. (1959). Some inequalities satisfied by the quantities of information of Fisher
  and Shannon. *Information and Control*.
