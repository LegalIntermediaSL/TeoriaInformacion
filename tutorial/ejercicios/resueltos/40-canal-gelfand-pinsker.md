# Ejercicio resuelto: Canal con estado y Dirty Paper Coding

**Módulo:** 02 — Teoría de la información  
**Artículo de referencia:** [Canal con Estado: Teorema de Gel'fand-Pinsker](../../02-teoria-informacion/18-canal-con-estado-gelfand-pinsker.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

**(a)** Considera el canal binario con estado:

$$Y = X \oplus S \oplus Z$$

con $X \in \left\lbrace 0, 1 \right\rbrace$, $S \sim \text{Bernoulli}(0.4)$ conocido **no causalmente** solo en el transmisor, y $Z \sim \text{Bernoulli}(0.1)$ ruido independiente desconocido para ambos. Usando el teorema de Gel'fand-Pinsker

$$C = \max_{p(u,x \mid s)} \left[ I(U; Y) - I(U; S) \right],$$

verifica que la variable auxiliar óptima es $U = X \oplus S$ (precoding XOR), calcula la capacidad resultante $C_{\text{GP}}$ y compárala con la capacidad sin conocimiento del estado.

**(b)** En el canal Gaussiano con interferencia conocida en el transmisor (Dirty Paper Coding, Costa 1983):

$$Y = X + S + Z$$

con restricción de potencia $\mathbb{E}[X^2] \leq P = 4$, ruido $Z \sim \mathcal{N}(0, N)$ con $N = 1$, e interferencia $S \sim \mathcal{N}(0, Q)$ con $Q = 9$ conocida solo en el transmisor:

1. Calcula la capacidad DPC $C_{\text{DPC}}$ y la capacidad sin conocimiento del estado $C_{\text{sin}}$.
2. Calcula el valor óptimo $\alpha_{\text{opt}} = P / (P + N)$ y muestra que la variable auxiliar $U = X + \alpha_{\text{opt}} S$ logra $I(U;Y) - I(U;S) = C_{\text{DPC}}$.

**(c)** El teorema de Gel'fand-Pinsker (canal con estado conocido en el **transmisor**) y el teorema de Wyner-Ziv (compresión con información lateral en el **receptor**) son duales. Explica la dualidad en términos de:

- Quién conoce qué y en qué extremo del sistema.
- Qué rol juega la variable auxiliar $U$ en cada caso.
- Cómo se manifiesta matemáticamente la dualidad en las fórmulas de tasa/capacidad.

**(d)** Un sistema MIMO con 2 antenas transmisoras y 2 usuarios monoanténicos opera con canal $H = I$ (identidad $2 \times 2$). El usuario 1 transmite con potencia $P_1 = 2$ y el usuario 2 con $P_2 = 3$. Compara la capacidad total usando:

1. **DPC sucesivo:** el transmisor codifica para el usuario 1 primero; al codificar para el usuario 2, la señal del usuario 1 es interferencia conocida que se cancela con DPC.
2. **Zero-forcing (ZF):** el transmisor proyecta cada señal en el nulo del canal del otro usuario, eliminando la interferencia pero perdiendo potencia efectiva (asume que con ZF la potencia efectiva de cada usuario se reduce a la mitad).

Calcula la ganancia de capacidad total de DPC frente a ZF.

---

## Solución

### Parte (a): Canal binario con estado — precoding XOR

**Configuración del canal.**

El canal es $Y = X \oplus S \oplus Z$ con $S \sim \text{Bern}(q)$, $q = 0.4$, y $Z \sim \text{Bern}(p)$, $p = 0.1$. Usamos la entropía binaria $H_b(t) = -t\log_2 t - (1-t)\log_2(1-t)$ y la convolución binaria $p * q = p(1-q) + q(1-p)$.

**Capacidad sin conocimiento del estado.**

Si el transmisor ignora $S$, éste actúa como ruido adicional. La salida efectiva es $Y = X \oplus (S \oplus Z)$, donde $S \oplus Z \sim \text{Bern}(p * q)$:

$$p * q = 0.1 \times 0.6 + 0.4 \times 0.9 = 0.06 + 0.36 = 0.42$$

La capacidad del canal binario simétrico resultante es:

$$C_{\text{sin}} = 1 - H_b(0.42)$$

Calculando $H_b(0.42) = -0.42\log_2(0.42) - 0.58\log_2(0.58)$:

$$H_b(0.42) \approx -0.42 \times (-1.252) - 0.58 \times (-0.786) \approx 0.526 + 0.456 = 0.982 \text{ bits}$$

$$C_{\text{sin}} \approx 1 - 0.982 = 0.018 \text{ bits/uso}$$

La presencia del estado con $q = 0.4$ (cercano a 0.5) destruye casi toda la capacidad.

**Capacidad G-P con precoding $U = X \oplus S$.**

Tomamos $U = X \oplus S$ con $X \sim \text{Bern}(1/2)$ uniforme. Entonces:

- $U \sim \text{Bern}(1/2)$ (uniforme, ya que $X$ es uniforme e independiente de $S$).
- $Y = X \oplus S \oplus Z = U \oplus Z$.

Calculamos cada término:

$$I(U; Y) = H(Y) - H(Y \mid U)$$

Como $Y = U \oplus Z$ y $U$ es uniforme, $Y$ también es uniforme: $H(Y) = 1$ bit. Además, $H(Y \mid U) = H(Z) = H_b(p) = H_b(0.1)$.

$$I(U; Y) = 1 - H_b(0.1)$$

$$I(U; S) = H(U) - H(U \mid S)$$

Dado $S$, $U = X \oplus S$ y $X$ es independiente de $S$ con distribución uniforme, así que $U \mid S$ también es uniforme: $H(U \mid S) = 1$ bit. Por tanto:

$$I(U; S) = H(U) - H(U \mid S) = 1 - 1 = 0$$

La capacidad G-P con esta elección es:

$$C_{\text{GP}} = I(U; Y) - I(U; S) = \left[1 - H_b(0.1)\right] - 0 = 1 - H_b(0.1)$$

Calculando $H_b(0.1) = -0.1\log_2(0.1) - 0.9\log_2(0.9) \approx 0.332 + 0.137 = 0.469$ bits:

$$C_{\text{GP}} = 1 - 0.469 = 0.531 \text{ bits/uso}$$

**Optimalidad.** Esta elección maximiza $I(U;Y) - I(U;S)$ porque:

1. Consigue $I(U;S) = 0$: la variable auxiliar absorbe el estado sin "gastar" información en él.
2. Maximiza $I(U;Y) = 1 - H_b(p)$: al ser $U$ uniforme y $Y = U \oplus Z$, se alcanza la capacidad del canal binario simétrico con parámetro $p$.

El resultado es exactamente la capacidad del canal $Y = X \oplus Z$ **sin** interferencia $S$.

**Comparación:**

| Escenario | Capacidad (bits/uso) |
|---|---|
| Sin conocimiento del estado ($S$ actúa como ruido) | $\approx 0.018$ |
| Con precoding G-P ($U = X \oplus S$) | $\approx 0.531$ |
| Canal puro sin estado ($Y = X \oplus Z$) | $\approx 0.531$ |

El conocimiento no causal del estado recupera completamente la capacidad del canal libre de interferencia, una ganancia de más de $0.51$ bits/uso en este caso.

---

### Parte (b): Dirty Paper Coding gaussiano

**Capacidad DPC (Costa, 1983).**

El resultado fundamental de Costa establece que el conocimiento no causal de $S$ en el transmisor hace que la interferencia sea completamente transparente:

$$C_{\text{DPC}} = \frac{1}{2}\log_2\!\left(1 + \frac{P}{N}\right) = \frac{1}{2}\log_2\!\left(1 + \frac{4}{1}\right) = \frac{1}{2}\log_2 5 \approx 1.161 \text{ bits/uso}$$

**Capacidad sin conocimiento del estado.**

Si el transmisor desconoce $S$, la interferencia se suma al ruido efectivo. La potencia de ruido total es $N + Q$:

$$C_{\text{sin}} = \frac{1}{2}\log_2\!\left(1 + \frac{P}{N + Q}\right) = \frac{1}{2}\log_2\!\left(1 + \frac{4}{1 + 9}\right) = \frac{1}{2}\log_2\!\left(\frac{14}{10}\right) = \frac{1}{2}\log_2(1.4) \approx 0.485 \text{ bits/uso}$$

**Parámetro óptimo $\alpha_{\text{opt}}$.**

La variable auxiliar es $U = X + \alpha S$ con $X \sim \mathcal{N}(0, P)$ independiente de $S$ y $Z$. Calculamos $I(U;Y) - I(U;S)$ para verificar que $\alpha_{\text{opt}} = P/(P+N)$ es óptimo.

Calculamos las varianzas y covarianzas. La salida es $Y = X + S + Z$, y $U = X + \alpha S$.

Las varianzas son:

$$\text{Var}(U) = P + \alpha^2 Q$$
$$\text{Var}(Y) = P + Q + N$$
$$\text{Cov}(U, Y) = \text{Cov}(X + \alpha S,\, X + S + Z) = P + \alpha Q$$

Para variables gaussianas conjuntas, la información mutua se expresa mediante correlaciones:

$$I(U; Y) = \frac{1}{2}\log_2\frac{\text{Var}(U) \cdot \text{Var}(Y)}{\text{Var}(U)\cdot\text{Var}(Y) - \text{Cov}(U,Y)^2}$$

Análogamente, $\text{Cov}(U, S) = \alpha Q$, $\text{Var}(S) = Q$:

$$I(U; S) = \frac{1}{2}\log_2\frac{(P + \alpha^2 Q)\,Q}{(P + \alpha^2 Q)\,Q - \alpha^2 Q^2} = \frac{1}{2}\log_2\frac{P + \alpha^2 Q}{P + \alpha^2 Q - \alpha^2 Q} = \frac{1}{2}\log_2\frac{P + \alpha^2 Q}{P}$$

Para $I(U;Y)$, la varianza residual de $U$ dado $Y$ es:

$$\text{Var}(U \mid Y) = (P + \alpha^2 Q) - \frac{(P + \alpha Q)^2}{P + Q + N}$$

Tras álgebra directa con $\alpha = P/(P+N)$, la diferencia $I(U;Y) - I(U;S)$ simplifica a:

$$I(U;Y) - I(U;S) = \frac{1}{2}\log_2\!\left(1 + \frac{P}{N}\right)$$

que es independiente de $Q$. El valor $\alpha_{\text{opt}} = P/(P+N)$ es el que anula la covarianza entre la componente de $U$ debida a $S$ y el residuo de $Y$, logrando la cancelación perfecta.

Para $P = 4$, $N = 1$:

$$\alpha_{\text{opt}} = \frac{4}{4 + 1} = \frac{4}{5} = 0.8$$

**Comparación:**

| Escenario | Capacidad (bits/uso) |
|---|---|
| DPC — conocimiento no causal de $S$ | $\approx 1.161$ |
| Sin conocimiento de $S$ (interferencia como ruido) | $\approx 0.485$ |
| Ganancia del conocimiento del estado | $\approx 0.676$ bits/uso |

La interferencia de potencia $Q = 9$ (más de dos veces la señal útil) reduce la capacidad a menos de la mitad si es desconocida, pero con DPC no tiene ningún efecto.

---

### Parte (c): Dualidad Wyner-Ziv / Gel'fand-Pinsker

La dualidad fuente-canal entre estos dos teoremas es una de las simetrías más elegantes de la teoría de la información.

**Quién conoce qué.**

| Rol | Wyner-Ziv (compresión) | Gel'fand-Pinsker (canal) |
|---|---|---|
| Información lateral | En el **receptor** (decodificador) | En el **transmisor** (codificador) |
| Objetivo | Comprimir $X$ usando que el receptor ya conoce $Y$ | Transmitir sobre canal con estado $S$ que solo conoce el Tx |
| Sistema | Fuente $\to$ compresor $\to$ canal limpio $\to$ descompresor (con $Y$) | Fuente $\to$ codificador (con $S$) $\to$ canal con estado $\to$ decodificador |

En Wyner-Ziv, la información lateral está "después" del canal (en la recepción). En Gel'fand-Pinsker, está "antes" (en la emisión). Son duales respecto al flujo de información del sistema.

**Rol opuesto de la variable auxiliar $U$.**

En ambos teoremas aparece una variable auxiliar $U$, pero con roles intercambiados:

- **Gel'fand-Pinsker:** el **codificador** usa $S$ para elegir $U$ (precoding). El objetivo es que $U$ sea independiente de $S$ pero correlacionado con $Y$. El receptor busca $U$ en la salida del canal.

- **Wyner-Ziv:** el **decodificador** usa la información lateral $Y$ para encontrar $U$. El codificador comprime $X$ en bins; el receptor usa $Y$ para identificar el bin correcto y reconstruir $X$.

En términos operacionales: en G-P el codificador busca en el bin (usa $S$ para encontrar una $u^n$ típica con $s^n$), y en Wyner-Ziv es el decodificador quien busca en el bin (usa $y^n$ para encontrar una $u^n$ típica).

**Manifestación matemática.**

Las fórmulas son especulares:

$$C_{\text{GP}} = \max_{p(u,x \mid s)} \left[ I(U; Y) - I(U; S) \right]$$

$$R_{\text{WZ}} = \min_{p(u \mid x)} \left[ I(U; X) - I(U; Y) \right]$$

La dualidad es exacta: $I(U;Y)$ y $I(U;S)$ intercambian sus posiciones; la maximización en G-P se convierte en minimización en Wyner-Ziv; la capacidad (cuánto se puede transmitir) es el dual de la tasa de compresión (cuánto se necesita para comprimir). Ambas usan la misma técnica de binning de Wyner, pero en extremos opuestos.

---

### Parte (d): DPC vs zero-forcing en MIMO 2×2

**Configuración.** Canal $H = I$, potencias $P_1 = 2$ (usuario 1), $P_2 = 3$ (usuario 2). Los usuarios son monoanténicos y no hay cooperación entre receptores.

**DPC sucesivo.**

El transmisor codifica primero para el usuario 1 sin interferencia (no hay usuarios previos). Al codificar para el usuario 2, la señal del usuario 1 ya está determinada y actúa como interferencia conocida en el transmisor: se aplica DPC y queda cancelada.

Cada usuario ve su canal como si no hubiera interferencia del otro (el DPC elimina la interferencia inter-usuario de forma unilateral desde el transmisor):

$$R_1^{\text{DPC}} = \frac{1}{2}\log_2(1 + P_1) = \frac{1}{2}\log_2(1 + 2) = \frac{1}{2}\log_2 3 \approx 0.792 \text{ bits/uso}$$

$$R_2^{\text{DPC}} = \frac{1}{2}\log_2(1 + P_2) = \frac{1}{2}\log_2(1 + 3) = \frac{1}{2}\log_2 4 = 1 \text{ bit/uso}$$

$$C_{\text{DPC}} = R_1^{\text{DPC}} + R_2^{\text{DPC}} \approx 0.792 + 1.000 = 1.792 \text{ bits/uso}$$

**Zero-forcing.**

Con ZF, el transmisor proyecta la señal de cada usuario en el subespacio nulo del canal del otro. Para $H = I$, esto requiere que las señales sean ortogonales entre sí. La potencia efectiva de cada usuario se reduce a la mitad (la proyección ortogonal en $\mathbb{R}^2$ con vectores de igual módulo reparte la potencia disponible):

$$P_1^{\text{ef}} = P_1 / 2 = 1, \qquad P_2^{\text{ef}} = P_2 / 2 = 1.5$$

Cada usuario ve solo su señal proyectada más ruido unitario:

$$R_1^{\text{ZF}} = \frac{1}{2}\log_2(1 + P_1^{\text{ef}}) = \frac{1}{2}\log_2(1 + 1) = \frac{1}{2}\log_2 2 = 0.5 \text{ bits/uso}$$

$$R_2^{\text{ZF}} = \frac{1}{2}\log_2(1 + P_2^{\text{ef}}) = \frac{1}{2}\log_2(1 + 1.5) = \frac{1}{2}\log_2(2.5) \approx 0.661 \text{ bits/uso}$$

$$C_{\text{ZF}} = R_1^{\text{ZF}} + R_2^{\text{ZF}} \approx 0.500 + 0.661 = 1.161 \text{ bits/uso}$$

**Comparación y ganancia.**

| Esquema | $R_1$ | $R_2$ | $C_{\text{total}}$ |
|---|---|---|---|
| DPC sucesivo | $0.792$ | $1.000$ | $1.792$ bits/uso |
| Zero-forcing | $0.500$ | $0.661$ | $1.161$ bits/uso |
| **Ganancia DPC** | $+0.292$ | $+0.339$ | **$+0.631$ bits/uso** |

La ganancia de DPC sobre ZF es $\approx 0.63$ bits/uso, un $54\%$ más de capacidad total. Esta diferencia crece con la potencia: ZF sacrifica potencia efectiva para anular la interferencia, mientras que DPC la gestiona sin pérdida de potencia. En sistemas con muchos usuarios o potencias altas, la brecha entre DPC y ZF se amplía logarítmicamente.

---

## Ideas clave del ejercicio

1. **El precoding XOR cancela el estado binario.** Con $U = X \oplus S$, la variable auxiliar absorbe el estado ($I(U;S) = 0$) y la capacidad G-P iguala la del canal libre de interferencia $1 - H_b(p)$, independientemente del sesgo $q$ del estado.

2. **DPC gaussiano: la interferencia de cualquier potencia es gratuita.** Con $\alpha_{\text{opt}} = P/(P+N)$, la elección $U = X + \alpha S$ logra $I(U;Y) - I(U;S) = \frac{1}{2}\log_2(1 + P/N)$, idéntica a la capacidad sin interferencia. La potencia $Q$ del estado no aparece en la fórmula final.

3. **La dualidad Wyner-Ziv / Gel'fand-Pinsker es una simetría fuente-canal.** El rol de la información lateral se invierte (receptor vs transmisor), la variable auxiliar $U$ intercambia quién la usa (codificador vs decodificador), y las fórmulas $I(U;Y) - I(U;S)$ e $I(U;X) - I(U;Y)$ son imágenes especulares.

4. **DPC supera al zero-forcing en MIMO porque gestiona la interferencia sin coste de potencia.** ZF elimina la interferencia proyectando señales en subespacios ortogonales (reduciendo la potencia efectiva); DPC la cancela mediante precoding desde el transmisor, preservando toda la potencia disponible para cada usuario.
