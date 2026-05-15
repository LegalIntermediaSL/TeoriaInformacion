# Geometría de la Información

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min

## Prerrequisitos

- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)
- [Divergencia KL y divergencias de información](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Complejidad de Kolmogorov](01-complejidad-de-kolmogorov.md)

## Objetivos de aprendizaje

1. Interpretar una familia paramétrica de distribuciones como una variedad diferenciable.
2. Definir la métrica de Fisher-Rao y demostrar su invariancia bajo estadísticos suficientes.
3. Derivar la cota de Cramér-Rao como consecuencia de la curvatura de la variedad.
4. Describir las propiedades geométricas de las familias exponenciales: coordenadas duales, divergencia de Bregman y proyecciones.
5. Aplicar el gradiente natural a la optimización en espacios de parámetros curvos.

## Intuición

Cuando modelamos un fenómeno con distribuciones de probabilidad, tendemos a pensar en los parámetros $\theta$ como simples números en un espacio euclidiano. Pero esa visión es engañosa: desplazarse de $\theta$ a $\theta + \varepsilon$ no tiene el mismo "coste informacional" en todas las regiones del espacio de parámetros. Cerca de $p = 0.01$ en una Bernoulli, un cambio de $0.01$ en $p$ casi duplica la probabilidad del evento raro; cerca de $p = 0.5$, el mismo desplazamiento apenas se nota. El espacio de distribuciones tiene una **geometría propia**, y esa geometría está dictada por cuánta información sobre $\theta$ contienen los datos.

La **geometría de la información** (Amari, 1985) formaliza esta idea: dota al espacio de distribuciones de una estructura de variedad diferenciable riemanniana, con una métrica — la de Fisher-Rao — que mide la "distancia informacional" entre distribuciones vecinas. El resultado es un marco unificado que conecta estadística, aprendizaje automático y teoría de la información a través de una sola estructura geométrica.

## Variedades estadísticas

### Familias paramétricas como variedades

Sea $\mathcal{S} = \{p(x;\theta) : \theta \in \Theta \subseteq \mathbb{R}^d\}$ una familia paramétrica regular. Cada distribución $p(x;\theta)$ es un punto de la variedad; el vector $\theta = (\theta^1, \ldots, \theta^d)$ da un sistema de coordenadas local.

La **función score** en la dirección $i$ es

$$\ell_i(x;\theta) = \partial_i \log p(x;\theta),$$

y actúa como vector tangente en el punto $\theta$: mide cómo varía el log-verosímil al desplazarse infinitesimalmente en la dirección $\partial/\partial\theta^i$.

**Ejemplos canónicos:**

- **Bernoulli$(p)$:** $\mathcal{S}_B = \{p^x(1-p)^{1-x} : p \in (0,1)\}$, variedad unidimensional.
- **Gaussiana $\mathcal{N}(\mu,\sigma^2)$:** $\mathcal{S}_G = \{(\mu,\sigma) : \mu \in \mathbb{R},\, \sigma > 0\}$, variedad bidimensional.
- **Distribuciones exponenciales de orden $d$:** familias $d$-dimensionales, que resultan ser geometricamente las más simples (véase §Familias exponenciales).

## La métrica de Fisher-Rao

### Definición

El **tensor métrico de Fisher-Rao** es la matriz $G(\theta)$ con componentes

$$g_{ij}(\theta) = \mathbb{E}_\theta\!\left[\partial_i \log p(x;\theta)\cdot \partial_j \log p(x;\theta)\right] = -\mathbb{E}_\theta\!\left[\partial_i \partial_j \log p(x;\theta)\right].$$

La igualdad entre las dos expresiones se sigue de diferenciar la identidad $\int p(x;\theta)\,dx = 1$ dos veces bajo condiciones de regularidad. La segunda forma, conocida como **información de Fisher observada esperada**, es a menudo más cómoda para el cálculo.

La distancia infinitesimal al cuadrado entre $\theta$ y $\theta + d\theta$ es

$$ds^2 = \sum_{i,j} g_{ij}(\theta)\, d\theta^i\, d\theta^j.$$

### Ejemplo: Bernoulli$(p)$

$\log p(x;p) = x \log p + (1-x)\log(1-p)$. Entonces $\partial_p \log p = x/p - (1-x)/(1-p)$ y

$$g(p) = \mathbb{E}_p\!\left[\left(\frac{X}{p} - \frac{1-X}{1-p}\right)^2\right] = \frac{1}{p(1-p)}.$$

La métrica diverge en $p \to 0$ y $p \to 1$: los extremos de la variedad son "infinitamente lejos" en unidades informacionales, lo que refleja que distinguir $p = 0.001$ de $p = 0.002$ requiere muchos más datos que distinguir $p = 0.49$ de $p = 0.50$.

### Unicidad: el teorema de Čencov

La métrica de Fisher-Rao no es una elección arbitraria. Čencov (1982) demostró que es la **única métrica riemanniana invariante** bajo la acción de estadísticos suficientes (transformaciones que no destruyen información): si $T$ es suficiente para $\theta$, entonces la distancia entre $p(\cdot;\theta_1)$ y $p(\cdot;\theta_2)$ calculada en la familia original coincide con la calculada en la familia transformada $q(\cdot;\theta) = p_{T}(\cdot;\theta)$. Esta invariancia es la que confiere a la métrica de Fisher su carácter canónico.

## La cota de Cramér-Rao como consecuencia geométrica

Sea $T(X)$ un estimador insesgado de $\theta$ (escalar por simplicidad). La **cota de Cramér-Rao** afirma que

$$\mathrm{Var}_\theta(T) \geq \frac{1}{I(\theta)},$$

donde $I(\theta) = g(\theta)$ es la información de Fisher. En la variedad estadística, $1/\sqrt{I(\theta)}$ tiene la interpretación de **radio de curvatura**: cuanto más "curva" es la variedad en $\theta$, más difícil es estimar $\theta$ y mayor es la cota inferior de la varianza.

La **distancia geodésica de Fisher-Rao** entre dos distribuciones $p(\cdot;\theta_0)$ y $p(\cdot;\theta_1)$ en la variedad es

$$d_{\mathrm{FR}}(\theta_0, \theta_1) = \int_0^1 \sqrt{g(\theta(t))}\,\dot\theta(t)\,dt,$$

donde $\theta(t)$ recorre la geodésica. Para Bernoulli$(p)$, la parametrización $p = \sin^2(\varphi/2)$ aplana la métrica: $g(\varphi) = 1$ y la distancia geodésica es simplemente $|\varphi_1 - \varphi_0|$. Esta "parametrización de arco de seno" es el cambio de variable estabilizador de varianza clásico de la estadística.

## Familias exponenciales como variedades planas

### Estructura algebraica

Una **familia exponencial** tiene la forma

$$p(x;\theta) = \exp\!\bigl(\theta^\top T(x) - A(\theta)\bigr)\, h(x),$$

donde $\theta \in \mathbb{R}^d$ son las **coordenadas naturales** (o canónicas), $T(x)$ el estadístico suficiente natural, $A(\theta) = \log \int \exp(\theta^\top T(x)) h(x)\,dx$ la **función de partición logarítmica** (o función cumulante), y $h(x) \geq 0$ la medida base.

Incluyen Bernoulli, Gaussiana, Poisson, Gamma y prácticamente todas las distribuciones clásicas.

### Dualidad de coordenadas

La **información de Fisher** para una familia exponencial es

$$G(\theta) = \nabla^2 A(\theta),$$

es decir, el Hessiano de $A$. Las **coordenadas de expectativa** (o mixtura) se definen como

$$\eta = \nabla A(\theta) = \mathbb{E}_\theta[T(X)].$$

El par $(\theta, \eta)$ constituye un sistema de **coordenadas duales**: la transformación $\theta \mapsto \eta$ es un difeomorfismo (cuando $A$ es estrictamente convexa), y la **transformada de Legendre** de $A$, denotada $A^*(\eta) = \sup_\theta \{\theta^\top \eta - A(\theta)\}$, recupera $A^*(\eta) = -H_\theta$ (entropía de Shannon bajo $\eta$).

### Geometría plana y divergencia de Bregman

Las familias exponenciales son **e-planas**: la conexión afín exponencial (conexión $\alpha = 1$ de Amari) tiene curvatura cero en coordenadas $\theta$. Esto significa que las geodésicas e-paralelas son rectas en coordenadas $\theta$.

La divergencia de Kullback-Leibler entre dos miembros de la familia es exactamente la **divergencia de Bregman** generada por $A$:

$$D_{\mathrm{KL}}\!\bigl(p(\cdot;\theta')\,\|\, p(\cdot;\theta)\bigr) = B_A(\theta' \| \theta) = A(\theta') - A(\theta) - \nabla A(\theta)^\top (\theta'-\theta).$$

Esta expresión tiene una consecuencia inmediata: la **proyección e-geodésica** de una distribución $p$ sobre una subvariedad exponencial $\mathcal{E}$ (minimizar $D_{\mathrm{KL}}(q \| p)$ sobre $q \in \mathcal{E}$) coincide con la **estimación de máxima verosimilitud** restringida a $\mathcal{E}$. La MLE es literalmente la proyección ortogonal en la variedad estadística.

## Las $\alpha$-conexiones de Amari

Amari introdujo una familia uniparamétrica de **conexiones afines** $\nabla^{(\alpha)}$ sobre la variedad estadística, para $\alpha \in [-1, 1]$:

- $\alpha = 1$: **conexión exponencial** (e-conexión). Las geodésicas son rectas en coordenadas $\theta$.
- $\alpha = -1$: **conexión mixtura** (m-conexión). Las geodésicas son rectas en coordenadas $\eta$.
- $\alpha = 0$: **conexión de Levi-Civita** (la única compatible con la métrica de Fisher-Rao).

Las dos conexiones extremas $\nabla^{(1)}$ y $\nabla^{(-1)}$ son **duales** respecto a la métrica de Fisher: $\nabla^{(-\alpha)} = (\nabla^{(\alpha)})^*$. Esta dualidad genera la estructura de **variedad estadística de Amari**, que generaliza la geometría riemanniana estándar.

El **teorema de la proyección dual** resume la elegancia de esta estructura: dadas una subvariedad e-plana $\mathcal{E}$ y una m-plana $\mathcal{M}$ que se intersectan en un punto $r$,

$$D_{\mathrm{KL}}(p \| q) = D_{\mathrm{KL}}(p \| r) + D_{\mathrm{KL}}(r \| q) \quad \forall\, p \in \mathcal{M},\, q \in \mathcal{E}.$$

Es el análogo no euclidiano del teorema de Pitágoras, con KL jugando el papel del cuadrado de la distancia.

## El gradiente natural

### Problema con el gradiente estándar

En optimización de parámetros, el **gradiente euclidiano** $\nabla_\theta \mathcal{L}$ ignora la geometría del espacio de distribuciones: trata todos los desplazamientos $\Delta\theta$ como equivalentes, cuando en realidad producen cambios muy distintos en la distribución $p(x;\theta)$. Esto provoca convergencia lenta cuando la matriz de Fisher $G(\theta)$ está mal condicionada (gradientes "escalonados" en valles estrechos de la verosimilitud).

### Definición y propiedades

El **gradiente natural** (Amari, 1998) es el vector que maximiza el descenso de $\mathcal{L}$ bajo la restricción de que el desplazamiento tenga norma unitaria en la métrica de Fisher:

$$\tilde{\nabla}_\theta \mathcal{L} = G(\theta)^{-1} \nabla_\theta \mathcal{L}.$$

La actualización del gradiente natural $\theta \leftarrow \theta - \eta\, G(\theta)^{-1} \nabla_\theta \mathcal{L}$ es invariante bajo reparametrizaciones: si $\phi = f(\theta)$ es un cambio de coordenadas, la dirección de descenso óptima es la misma expresada en $\phi$ que en $\theta$. El gradiente estándar no tiene esta propiedad.

### Conexión con optimizadores modernos

Amari (1998) demostró que el gradiente natural converge en $O(1/n)$ iteraciones en regímenes en que el gradiente estándar converge en $O(1/n^2)$ en ciertos modelos. En redes neuronales profundas:

- **K-FAC** (Martens y Grosse, 2015) aproxima $G(\theta)^{-1}$ con un producto de Kronecker por capas, haciéndolo tratable.
- **Adam** puede interpretarse como una aproximación diagonal de $G(\theta)^{-1}$ con estimación adaptativa de la curvatura, aunque su fundamento geométrico es menos directo.
- **KFAC-Empirical** y variantes naturales se usan en entrenamiento de modelos de lenguaje grandes para acelerar la convergencia inicial.

## La KL como distancia al cuadrado

La divergencia KL no es una distancia (no es simétrica, no satisface la desigualdad triangular en general), pero sí una **divergencia de Bregman** y, localmente, el cuadrado de la distancia de Fisher-Rao. Para $\theta' = \theta + \Delta\theta$ próximos:

$$D_{\mathrm{KL}}\!\bigl(p(\cdot;\theta')\,\|\, p(\cdot;\theta)\bigr) = \frac{1}{2}\, \Delta\theta^\top G(\theta)\, \Delta\theta + O(\|\Delta\theta\|^3).$$

Esto justifica usar KL como función de coste en problemas de optimización sobre distribuciones: minimizar KL es, localmente, minimizar la distancia de Fisher-Rao al cuadrado. Las dos divergencias no simétricas $D_{\mathrm{KL}}(p\|q)$ y $D_{\mathrm{KL}}(q\|p)$ corresponden a las dos geodésicas distintas (e y m) entre los mismos dos puntos, y producen proyecciones distintas (MLE versus momentos coincidentes).

## Ideas clave

1. Las distribuciones de probabilidad forman una **variedad diferenciable** cuya geometría es única y canónica: está determinada por la métrica de Fisher-Rao (teorema de Čencov).
2. La **cota de Cramér-Rao** tiene interpretación geométrica: la varianza mínima de un estimador es inversamente proporcional a la curvatura de la variedad en el punto $\theta$.
3. Las **familias exponenciales** son variedades e-planas; sus geodésicas son rectas en coordenadas naturales. La MLE es la proyección e-geodésica sobre la subvariedad del modelo.
4. La **dualidad** entre coordenadas naturales $\theta$ y coordenadas de expectativa $\eta = \nabla A(\theta)$ es la clave de la estructura de Amari: la KL es la divergencia de Bregman de $A$.
5. El **gradiente natural** $G(\theta)^{-1} \nabla \mathcal{L}$ respeta la geometría del espacio de parámetros y es invariante bajo reparametrizaciones; subyace a optimizadores como K-FAC.

## Ejercicios

1. **Métrica de Fisher para la Gaussiana.** Para $p(x;\mu,\sigma^2) = \mathcal{N}(\mu,\sigma^2)$, calcula la matriz de Fisher $G(\mu,\sigma)$ y verifica que $ds^2 = d\mu^2/\sigma^2 + 2\,d\sigma^2/\sigma^2$. ¿Qué implica geométricamente que las componentes dependan de $\sigma^{-2}$?

2. **Familias exponenciales.** Muestra que la distribución de Poisson $\mathrm{Po}(\lambda)$ es una familia exponencial. Identifica $\theta$, $T(x)$, $A(\theta)$ y $h(x)$. Calcula $\eta = \nabla A(\theta)$ y comprueba que $\eta = \lambda = \mathbb{E}[X]$.

3. **Gradiente natural vs estándar.** Considera minimizar $\mathcal{L}(\mu) = D_{\mathrm{KL}}(\mathcal{N}(0,1)\,\|\,\mathcal{N}(\mu,1))$. La matriz de Fisher es $G(\mu) = 1$ (constante). ¿Coinciden el gradiente estándar y el natural? Ahora repite con $\mathcal{L}(\theta) = D_{\mathrm{KL}}(\mathcal{N}(0,1)\,\|\,p(\cdot;\theta))$ en la parametrización $\theta = (\mu, \log\sigma)$. ¿Por qué divergen los dos gradientes?

4. **KL como cuadrado de distancia (conceptual).** La divergencia KL no es simétrica: $D_{\mathrm{KL}}(p\|q) \neq D_{\mathrm{KL}}(q\|p)$. Sin embargo, localmente ambas coinciden con $\frac{1}{2}\Delta\theta^\top G\,\Delta\theta$. Explica en tus propias palabras por qué la simetría local no implica simetría global, y da un ejemplo con distribuciones de Bernoulli con $p$ y $q$ muy distintos.

## Véase también

- [Divergencia KL y divergencias de información](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)
- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)
- [Aprendizaje profundo desde la información](10-aprendizaje-profundo-desde-la-informacion.md)
- [Privacidad diferencial](11-privacidad-diferencial.md)


<!-- nav-start -->

---
← [Privacidad Diferencial](11-privacidad-diferencial.md) · [13 - MDL y selección de modelos](13-mdl-y-seleccion-de-modelos.md) →

<!-- nav-end -->
## Referencias

- Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- Amari, S. y Nagaoka, H. (2000). *Methods of Information Geometry*. AMS/Oxford University Press.
- Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. American Mathematical Society.
- Nielsen, F. (2020). An elementary introduction to information geometry. *Entropy*, 22(10), 1100.
- Martens, J. (2014). New insights and perspectives on the natural gradient method. *Journal of Machine Learning Research*, 21(146), 1–76.
- Martens, J. y Grosse, R. (2015). Optimizing neural networks with Kronecker-factored approximate curvature. *ICML 2015*.
