# 35 - Información y biología

## Contexto

Este ejercicio acompaña el artículo
[Información y biología](../../05-conexiones-y-aplicaciones/07-informacion-y-biologia.md).

## Enunciado

**Parte A — El código genético como sistema de información:**

1. El genoma humano tiene aproximadamente $3 \times 10^9$ pares de bases. Si la distribución de bases fuera uniforme (A=T=C=G=25%), ¿cuántos bits de información contiene? ¿Y con la distribución real A=T≈29.5%, C=G≈20.5%?
2. El código genético es **degenerado**: 64 codones codifican 20 aminoácidos (+ STOP). ¿Cuánta información (en bits) se pierde por degeneración cuando se traduce un codón a un aminoácido?
3. Explica por qué la degeneración del código genético puede interpretarse como un mecanismo de corrección de errores.

**Parte B — Evolución e información de Fisher:**

4. Define la **información de Fisher** $I(\theta)$ para un modelo paramétrico. ¿Qué mide en el contexto de la evolución?
5. La cota de Cramér-Rao dice que $\text{Var}(\hat{\theta}) \geq 1/I(\theta)$. ¿Cómo se interpreta en términos de la eficiencia de la selección natural?
6. Si una mutación neutral cambia el fenotipo de forma que la información de Fisher sobre la aptitud aumenta, ¿es esto evolutivamente favorable o desfavorable? Razona.

## Pista

**Entropía del genoma:** $H = -\sum_b p_b \log_2 p_b$ por base.

**Pérdida de información por degeneración:** $H(\text{codón}) - H(\text{aminoácido})$, donde $H(\text{codón}) = \log_2 64 = 6$ bits si la distribución fuera uniforme.

**Corrección de errores:** si varias mutaciones puntuales producen el mismo aminoácido, la proteína es robusta frente a esos errores.

## Solución

### Parte A — El código genético como sistema de información

#### 1. Capacidad informativa del genoma

**Distribución uniforme:**

$$H_{\text{unif}} = \log_2 4 = 2 \text{ bits/base}$$

$$I_{\text{unif}} = 3 \times 10^9 \times 2 = 6 \times 10^9 \text{ bits} \approx 750 \text{ MB}$$

**Distribución real** (A=T=0.295, C=G=0.205):

$$H_{\text{real}} = -2(0.295 \log_2 0.295) - 2(0.205 \log_2 0.205)$$
$$= -2(0.295 \times (-1.762)) - 2(0.205 \times (-2.286))$$
$$= 2 \times 0.520 + 2 \times 0.469 = 1.040 + 0.937 = 1.977 \text{ bits/base}$$

$$I_{\text{real}} = 3 \times 10^9 \times 1.977 \approx 5.93 \times 10^9 \text{ bits}$$

La distribución sesgada reduce marginalmente la información total: se pierde $\approx 1.5\%$ respecto al máximo teórico por la ligera desigualdad AT/GC.

#### 2. Pérdida de información por degeneración

Si la distribución de codones fuera uniforme (64 codones con probabilidad 1/64 cada uno):

$$H(\text{codón}) = \log_2 64 = 6 \text{ bits}$$

Distribución de aminoácidos resultante del código genético estándar (con degeneraciones):

| Aminoácido | # codones | $p$ | $-p\log_2 p$ |
|------------|-----------|-----|--------------|
| Leu, Ser, Arg | 6 cada uno | 6/64 ≈ 0.094 | 0.321 cada uno |
| Val, Pro, Thr, Ala, Gly | 4 cada uno | 4/64 ≈ 0.063 | 0.247 cada uno |
| Ile | 3 | 3/64 ≈ 0.047 | 0.208 |
| Phe, Tyr, His, Gln, Asn, Lys, Asp, Glu, Cys | 2 cada uno | 2/64 ≈ 0.031 | 0.157 cada uno |
| Met, Trp, STOP (3 tipos) | 1/3/3 | ... | ... |

$H(\text{aminoácido}) \approx \log_2 21 \approx 4.39$ bits (con distribución casi uniforme).

**Pérdida de información por degeneración:**

$$\Delta H = H(\text{codón}) - H(\text{aminoácido}) \approx 6 - 4.39 = 1.61 \text{ bits/codón}$$

Estos $\approx 1.6$ bits "extras" por codón son la redundancia del código que permite la robustez ante mutaciones.

#### 3. La degeneración como corrección de errores

El código genético no es una tabla de traducción arbitraria: las degeneraciones están estructuradas sistemáticamente. En concreto:

- **Posición wobble (tercera del codón):** $\sim$70% de las mutaciones sinónimas ocurren en la tercera posición. Un error de replicación en esta posición suele producir el mismo aminoácido.
- **Aminoácidos similares mismos codones:** los aminoácidos bioquímicamente similares (e.g., Asp/Glu, Ser/Thr) comparten codones adyacentes (diffieren en 1 base). Una mutación que cambia el aminoácido tiende a producir uno con propiedades similares.

Este diseño no aleatorio sugiere que el código genético fue **seleccionado evolutivamente** para minimizar el daño de las mutaciones de un solo nucleótido, en coherencia con un código corrector de errores.

### Parte B — Evolución e información de Fisher

#### 4. Información de Fisher en evolución

La **información de Fisher** $I(\theta)$ mide cuánta información sobre el parámetro $\theta$ contiene una observación $X$:

$$I(\theta) = \mathbb{E}\!\left[\left(\frac{\partial}{\partial\theta} \ln f(X;\theta)\right)^2\right] = -\mathbb{E}\!\left[\frac{\partial^2}{\partial\theta^2} \ln f(X;\theta)\right]$$

En el contexto evolutivo, $\theta$ es la **aptitud** (fitness) de un fenotipo y $X$ es la observación de rasgos en la población. La información de Fisher mide cuán eficientemente la selección natural puede **inferir** la aptitud relativa de los fenotipos a partir de las observaciones.

Mayor $I(\theta)$ → la selección puede distinguir mejor entre individuos de diferente aptitud → evolución más eficiente.

#### 5. Cota de Cramér-Rao e interpretación evolutiva

La cota de Cramér-Rao establece:

$$\text{Var}(\hat{\theta}) \geq \frac{1}{n \cdot I(\theta)}$$

donde $n$ es el tamaño de la población (número de observaciones).

**Interpretación evolutiva:** la varianza del estimador de aptitud es la **imprecisión** con la que la selección natural puede discriminar entre genotipos. Con mayor $I(\theta)$:
- La selección puede detectar diferencias de aptitud más pequeñas.
- La eficiencia de la selección aumenta: fenotipos mejores se fijan más rápido.
- La deriva genética (ruido) tiene menor efecto relativo.

Con menor $I(\theta)$ (e.g., fenotipo muy ruidoso), la selección opera como si hubiera menos individuos: se necesita una diferencia de aptitud mayor para fijar el alelo favorable.

#### 6. Mutación neutral que aumenta $I(\theta)$

Si una mutación neutral (sin efecto en la aptitud actual) aumenta la información de Fisher sobre la aptitud, el fenotipo se vuelve **más discriminable** por la selección en el futuro.

Esto es **evolutivamente favorable** desde la perspectiva de la evolvabilidad: la población gana capacidad de responder más eficientemente a presiones selectivas futuras. Es uno de los mecanismos propuestos para explicar la selección de la **robustez fenotípica** y la **modularidad**: los organismos evolucionan no solo para adaptarse al entorno presente, sino para mantener la capacidad de adaptarse a cambios futuros.

Este resultado conecta la teoría de la información de Fisher con la biología evolutiva de sistemas: la información no es solo un descriptor del estado actual, sino un recurso que la evolución puede explotar y acumular.
