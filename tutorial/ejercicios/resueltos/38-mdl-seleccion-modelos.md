# Ejercicio resuelto: MDL y selección de modelos

**Módulo:** 05 — Conexiones y aplicaciones  
**Artículo de referencia:** [MDL y selección de modelos](../../05-conexiones-y-aplicaciones/13-mdl-y-seleccion-de-modelos.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

**(a)** Tienes $n = 100$ observaciones i.i.d. Se prueban dos modelos:
- Modelo A: Bernoulli con 1 parámetro, log-verosimilitud máxima $\hat{\ell}_A = -62$ nats.
- Modelo B: mezcla de 2 Bernoulli con 3 parámetros, log-verosimilitud máxima $\hat{\ell}_B = -58$ nats.

Usando la aproximación BIC-MDL ($\text{MDL} \approx -\hat{\ell} + \frac{k}{2}\ln n$), ¿qué modelo favorece MDL? ¿Y AIC ($\text{AIC} = -2\hat{\ell} + 2k$)?

**(b)** Deriva la complejidad estocástica NML para la familia Bernoulli($p$) con $n$ observaciones. Muestra que la constante de normalización es $C_n = \sum_{j=0}^{n} \binom{n}{j} (j/n)^j (1-j/n)^{n-j}$ y aproxima $\log_2 C_n \approx \frac{1}{2}\log_2 n - \frac{1}{2}\log_2(2\pi e / 4)$ para $n$ grande.

**(c)** ¿Por qué MDL no sobreajusta aunque maximice la verosimilitud dentro de cada modelo? Razona desde la perspectiva de la longitud de descripción.

**(d)** Un compresor gzip comprime $n = 10000$ bytes de texto a 6200 bytes. Estima la tasa de entropía del texto en bits/byte. ¿Cómo se relaciona este resultado con el principio MDL?

---

## Solución

### Parte (a): MDL vs AIC

La aproximación BIC-MDL convierte nats a bits: $-\hat{\ell}$ en nats se divide por $\ln 2 \approx 0.693$ para pasar a bits. Pero es más limpio comparar directamente en nats.

**Modelo A** ($k=1$, $\hat{\ell}_A = -62$):
$$\text{MDL}_A \approx 62 + \frac{1}{2}\ln(100) = 62 + 2.30 = 64.30 \text{ nats}$$
$$\text{AIC}_A = 2 \times 62 + 2 \times 1 = 126 \text{ nats}$$

**Modelo B** ($k=3$, $\hat{\ell}_B = -58$):
$$\text{MDL}_B \approx 58 + \frac{3}{2}\ln(100) = 58 + 6.91 = 64.91 \text{ nats}$$
$$\text{AIC}_B = 2 \times 58 + 2 \times 3 = 122 \text{ nats}$$

**Conclusión:**
- **MDL favorece el Modelo A** (64.30 < 64.91): el ahorro de verosimilitud de 4 nats no compensa los 3 parámetros extra para $n = 100$.
- **AIC favorece el Modelo B** (122 < 126): AIC penaliza menos la complejidad ($2k$ vs $\frac{k}{2}\ln n = 2.3k$).

Para $n = 100$, la penalización MDL/BIC por parámetro ($\frac{\ln 100}{2} \approx 2.3$ nats) es mayor que la de AIC (2 nats). AIC sobreestima la complejidad óptima; MDL/BIC son más conservadores y consistentes.

### Parte (b): NML para Bernoulli

Para $n$ observaciones i.i.d. Bernoulli($p$), si se observan $j$ éxitos, el MLE es $\hat{p} = j/n$, y la verosimilitud máxima es:
$$p(x^n; \hat{p}) = \binom{n}{j} \hat{p}^j (1-\hat{p})^{n-j} = \binom{n}{j} \left(\frac{j}{n}\right)^j \left(1-\frac{j}{n}\right)^{n-j}$$

La constante de normalización NML suma sobre todas las posibles secuencias con el mismo número de éxitos:
$$C_n = \sum_{j=0}^{n} \binom{n}{j} \left(\frac{j}{n}\right)^j \left(1-\frac{j}{n}\right)^{n-j}$$

Para $n$ grande, la contribución principal proviene de valores de $j$ cerca de $n/2$. Usando aproximación de Stirling y la integral de Laplace:
$$C_n \approx \sqrt{\frac{n}{2\pi \cdot p(1-p)}} \bigg|_{p=1/2} \cdot \int_0^1 dp = \sqrt{\frac{2n}{\pi}} \cdot \frac{1}{2} \approx \sqrt{\frac{n}{2\pi}}$$

Más precisamente, la complejidad de parámetro (regret) es:
$$\log_2 C_n \approx \frac{1}{2}\log_2 n + \frac{1}{2}\log_2\!\left(\frac{2}{\pi e}\right) + O(n^{-1})$$

Numéricamente, para $n = 100$: $\log_2 C_{100} \approx \frac{1}{2}\log_2(100) + \text{constante} \approx 3.32 + 0.24 \approx 3.56$ bits. Esta es la penalización de complejidad de la familia Bernoulli con 100 datos.

### Parte (c): MDL no sobreajusta

El sobreajuste ocurre cuando un modelo con muchos parámetros ajusta el ruido además de la señal: mejora el fit en los datos de entrenamiento pero generaliza mal.

MDL penaliza el sobreajuste desde el principio: un modelo con $k$ parámetros es útil solo si el ahorro en longitud de descripción de los datos $\Delta L_{\text{datos}} = L(x^n | M_A) - L(x^n | M_B)$ supera el coste de describir el modelo más complejo $\Delta L_{\text{modelo}} = L(M_B) - L(M_A) \approx \frac{k_B - k_A}{2}\ln n$ bits.

Si el modelo B sobreajusta, los parámetros extra capturan ruido. En nuevas muestras del mismo proceso, la mejora de verosimilitud sería $\approx 0$ (el ruido es incompresible). Por tanto:
$$\Delta L_{\text{total}} = \underbrace{\Delta L_{\text{datos}}}_{\approx 0} - \underbrace{\Delta L_{\text{modelo}}}_{> 0} < 0$$

MDL rechazaría el modelo B. En esencia, **MDL es equivalente a buscar el código más corto total**: un código que memoriza ruido no puede ser corto porque el ruido no tiene estructura comprimible.

### Parte (d): Tasa de entropía vía compresión

Gzip comprime $n = 10000$ bytes a 6200 bytes. La tasa de compresión es:
$$\frac{L_{\text{comprimido}}}{n} = \frac{6200}{10000} = 0.62 \text{ bytes/byte} = 4.96 \text{ bits/byte}$$

Por el teorema de la fuente de Shannon, la tasa de compresión de cualquier compresor universal converge a la entropía del proceso: $L_n / n \to \bar{H}$. La estimación es $\bar{H} \approx 4.96$ bits/byte (con el texto en bytes, no en caracteres).

**Conexión con MDL:** Gzip implementa el compresor de Lempel-Ziv-Welch (LZW), que es un estimador MDL del modelo de fuente más corto. Al comprimir, construye implícitamente un modelo del texto (tabla de frases repetidas), lo describe, y luego describe los datos dado ese modelo. La longitud total del archivo comprimido es exactamente la longitud de descripción MDL de la fuente. Para $n$ grande, este modelo converge al mejor modelo de la fuente (el que minimiza la longitud total = entropía del proceso).

---

## Ideas clave del ejercicio

1. MDL/BIC penaliza más fuertemente los parámetros extra que AIC, especialmente cuando $n$ es grande.
2. La complejidad NML para Bernoulli crece como $\frac{1}{2}\log_2 n$ bits — la penalización natural de una familia de 1 parámetro.
3. MDL no sobreajusta porque la mejora de verosimilitud del ruido no puede compensar el coste de describir parámetros adicionales.
4. La longitud de compresión de un compresor universal es el estimador MDL práctico de la entropía del proceso.
