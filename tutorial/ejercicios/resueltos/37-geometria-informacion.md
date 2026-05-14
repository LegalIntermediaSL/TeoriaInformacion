# Ejercicio resuelto: Geometría de la información

**Módulo:** 05 — Conexiones y aplicaciones  
**Artículo de referencia:** [Geometría de la información](../../05-conexiones-y-aplicaciones/12-geometria-de-la-informacion.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

**(a)** Calcula la métrica de Fisher para la familia de distribuciones Gaussianas $\mathcal{N}(\mu, \sigma^2)$ con parámetros $\theta = (\mu, \sigma^2)$. Escribe la matriz $G(\theta)$ explícitamente.

**(b)** Para la familia Bernoulli($p$), $p \in (0,1)$, calcula:
- La información de Fisher $I(p)$.
- La transformación de Fisher $\phi(p) = \arcsin(\sqrt{p})$ (estabilizador de varianza). Muestra que la métrica en coordenadas $\phi$ es constante (la variedad es "plana" en esas coordenadas).

**(c)** Dos distribuciones Gaussianas: $p_0 = \mathcal{N}(0, 1)$ y $p_1 = \mathcal{N}(1, 1)$. Aproxima la divergencia KL $D_{KL}(p_0 \| p_1)$ usando la aproximación cuadrática $D_{KL}(p \| q) \approx \frac{1}{2} (\theta_p - \theta_q)^T G(\theta) (\theta_p - \theta_q)$ y compara con el valor exacto.

**(d)** En una red neuronal pequeña, el gradiente estándar de la pérdida es $\nabla L = (0.9, 0.1)^T$ y la matriz de Fisher (estimada) es $G = \begin{pmatrix}4 & 1\\ 1 & 1\end{pmatrix}$. Calcula el gradiente natural $\tilde{\nabla}L = G^{-1} \nabla L$ y explica por qué difiere del estándar.

---

## Solución

### Parte (a): Métrica de Fisher para la Gaussiana

La log-verosimilitud de $\mathcal{N}(\mu, \sigma^2)$ es:
$$\log p(x; \mu, \sigma^2) = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2}$$

Las segundas derivadas son:
$$-\mathbb{E}\!\left[\frac{\partial^2 \log p}{\partial \mu^2}\right] = \frac{1}{\sigma^2}, \quad -\mathbb{E}\!\left[\frac{\partial^2 \log p}{\partial (\sigma^2)^2}\right] = \frac{1}{2\sigma^4}, \quad -\mathbb{E}\!\left[\frac{\partial^2 \log p}{\partial \mu \, \partial \sigma^2}\right] = 0$$

La matriz de Fisher con $\theta = (\mu, \sigma^2)$ es:

$$G(\mu, \sigma^2) = \begin{pmatrix} 1/\sigma^2 & 0 \\ 0 & 1/(2\sigma^4) \end{pmatrix}$$

La métrica es diagonal: la media y la varianza son parámetros ortogonales en el sentido de Fisher.

### Parte (b): Bernoulli y estabilizador de varianza

Para Bernoulli($p$), $p \in (0,1)$:
$$\log p(x; p) = x\log p + (1-x)\log(1-p)$$
$$\frac{d^2 \log p}{dp^2} = -\frac{x}{p^2} - \frac{1-x}{(1-p)^2}$$

Tomando la esperanza bajo $x \sim \text{Bernoulli}(p)$:
$$I(p) = -\mathbb{E}\!\left[\frac{d^2 \log p}{dp^2}\right] = \frac{p}{p^2} + \frac{1-p}{(1-p)^2} = \frac{1}{p} + \frac{1}{1-p} = \frac{1}{p(1-p)}$$

La métrica en coordenada $p$ es $g(p) = I(p) = \frac{1}{p(1-p)}$.

**Transformación de Fisher** $\phi = \arcsin(\sqrt{p})$, con $d\phi/dp = \frac{1}{2\sqrt{p(1-p)}}$:

La métrica en coordenada $\phi$ es:
$$g_\phi = g(p) \cdot \left(\frac{dp}{d\phi}\right)^2 = \frac{1}{p(1-p)} \cdot 4p(1-p) = 4$$

La métrica es constante 4 en coordenadas $\phi$: la variedad de Bernoulli es isométrica a un segmento del círculo unitario (arco de longitud $\pi/2$). Esto confirma que la variedad es "plana" en estas coordenadas.

### Parte (c): Aproximación cuadrática de KL

Para $p_0 = \mathcal{N}(0,1)$ y $p_1 = \mathcal{N}(1,1)$, con $\theta = (\mu, \sigma^2)$:

- $\theta_0 = (0, 1)$, $\theta_1 = (1, 1)$: diferencia $\Delta\theta = (1, 0)^T$
- Métrica en $\sigma^2 = 1$: $G = \begin{pmatrix}1 & 0\\ 0 & 1/2\end{pmatrix}$

**Aproximación cuadrática:**
$$D_{KL}(p_0 \| p_1) \approx \frac{1}{2} \Delta\theta^T G \, \Delta\theta = \frac{1}{2}(1, 0)\begin{pmatrix}1&0\\0&1/2\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \frac{1}{2}$$

**Valor exacto** de $D_{KL}(\mathcal{N}(\mu_0,\sigma^2) \| \mathcal{N}(\mu_1,\sigma^2))$:
$$D_{KL} = \frac{(\mu_1 - \mu_0)^2}{2\sigma^2} = \frac{1}{2}$$

Aquí la aproximación es **exacta** porque la KL entre dos Gaussianas con la misma varianza es exactamente cuadrática en la diferencia de medias. En general, la aproximación de segundo orden es válida cuando $\|\Delta\theta\|$ es pequeño.

### Parte (d): Gradiente natural

Con $\nabla L = (0.9, 0.1)^T$ y $G = \begin{pmatrix}4&1\\1&1\end{pmatrix}$:

$$G^{-1} = \frac{1}{4-1}\begin{pmatrix}1&-1\\-1&4\end{pmatrix} = \frac{1}{3}\begin{pmatrix}1&-1\\-1&4\end{pmatrix}$$

$$\tilde{\nabla}L = G^{-1}\nabla L = \frac{1}{3}\begin{pmatrix}1&-1\\-1&4\end{pmatrix}\begin{pmatrix}0.9\\0.1\end{pmatrix} = \frac{1}{3}\begin{pmatrix}0.8\\0.5\end{pmatrix} = \begin{pmatrix}0.267\\0.167\end{pmatrix}$$

**Interpretación:** El gradiente estándar $(0.9, 0.1)$ sobrevalora el parámetro 1 relativo al 2, sin tener en cuenta que cambios en el parámetro 1 producen variaciones mayores en la distribución (la varianza de Fisher es $G_{11}=4$). El gradiente natural corrige esto: reduce el paso en el parámetro 1 (de 0.9 a 0.267) y escala el parámetro 2 relativamente (de 0.1 a 0.167). En el espacio de distribuciones, el gradiente natural es la dirección de máximo descenso real.

---

## Ideas clave del ejercicio

1. La métrica de Fisher es la única métrica invariante bajo reparametrizaciones suficientes.
2. La estabilización de varianza transforma la variedad en una métrica constante (plana).
3. La KL entre distribuciones de la misma familia es cuadrática en $\Delta\theta$ a segundo orden.
4. El gradiente natural rescala las actualizaciones según la curvatura informacional del espacio de parámetros.
