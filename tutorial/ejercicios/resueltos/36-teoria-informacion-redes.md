# Ejercicio resuelto: Teoría de la información en redes

**Módulo:** 02 — Teoría de la Información  
**Artículo de referencia:** [Teoría de la información en redes](../../02-teoria-informacion/16-teoria-informacion-en-redes.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

Considera un canal de acceso múltiple (MAC) gaussiano con dos usuarios. Las señales recibidas son:

$$Y = X_1 + X_2 + Z$$

donde $Z \sim \mathcal{N}(0,1)$ es ruido gaussiano, y las restricciones de potencia son $\mathbb{E}[X_i^2] \leq P_i$, con $P_1 = 3$ y $P_2 = 1$.

**(a)** Escribe las tres desigualdades que definen la región de capacidad del MAC gaussiano.

**(b)** Calcula los tres vértices de la región de capacidad (las tasas máximas individuales y la suma máxima).

**(c)** ¿Qué tasa de suma máxima se obtiene si el receptor decodifica los mensajes de forma sucesiva (SIC)? ¿Coincide con la cota de la parte (b)?

**(d)** Aplica el principio de Slepian-Wolf: si $X_1$ y $X_2$ son fuentes correlacionadas con $H(X_1) = 2$, $H(X_2) = 1.5$ y $H(X_1, X_2) = 2.8$ bits, ¿cuáles son las tasas mínimas de compresión para que la decodificación conjunta sea posible?

---

## Solución

### Parte (a): Región de capacidad del MAC gaussiano

Para un MAC gaussiano con dos usuarios y ruidos independientes, la región de capacidad es el conjunto de pares $(R_1, R_2)$ que satisfacen simultáneamente:

$$R_1 \leq \frac{1}{2}\log_2\!\left(1 + \frac{P_1}{1 + P_2}\right) \quad \text{(sola, con interferencia del otro)}$$

$$R_2 \leq \frac{1}{2}\log_2\!\left(1 + \frac{P_2}{1 + P_1}\right)$$

$$R_1 + R_2 \leq \frac{1}{2}\log_2\!\left(1 + P_1 + P_2\right)$$

La última desigualdad es la cota de capacidad total (como si hubiera un único transmisor con potencia $P_1 + P_2$).

### Parte (b): Vértices de la región

Con $P_1 = 3$, $P_2 = 1$ y $\sigma^2 = 1$:

**Tasa máxima de usuario 1 solo (usuario 2 silencioso):**
$$R_1^{\max} = \frac{1}{2}\log_2(1 + P_1) = \frac{1}{2}\log_2(4) = 1 \text{ bit/uso}$$

**Tasa máxima de usuario 2 solo:**
$$R_2^{\max} = \frac{1}{2}\log_2(1 + P_2) = \frac{1}{2}\log_2(2) = 0.5 \text{ bits/uso}$$

**Suma máxima:**
$$R_1 + R_2 \leq \frac{1}{2}\log_2(1 + P_1 + P_2) = \frac{1}{2}\log_2(5) \approx 1.161 \text{ bits/uso}$$

Los vértices de la región de capacidad (poliedro pentagonal) son:

| Vértice | $R_1$ | $R_2$ |
|---------|-------|-------|
| A (máx $R_1$ con $R_2=0$) | $\log_2(4)/2 = 1$ | $0$ |
| B (máx $R_1$ s.t. $R_2 = \log_2(2)/2$) | $\approx 0.661$ | $0.5$ |
| C (máx $R_2$ s.t. $R_1 = 0$) | $0$ | $0.5$ |

El vértice B se obtiene como: $R_2 = R_2^{\max} = 0.5$, $R_1 = \frac{1}{2}\log_2(5) - 0.5 = \frac{1}{2}\log_2(5/2) \approx 0.661$.

### Parte (c): SIC (Successive Interference Cancellation)

Con SIC, el receptor decodifica primero el usuario con mayor SNR (usuario 1), cancela su señal, y luego decodifica al usuario 2:

**Paso 1:** Decodificar $X_1$ tratando $X_2$ como ruido: $R_1 = \frac{1}{2}\log_2\!\left(\frac{1+P_1+P_2}{1+P_2}\right) = \frac{1}{2}\log_2\!\left(\frac{5}{2}\right) \approx 0.661$ bits/uso.

**Paso 2:** Cancelar $X_1$; decodificar $X_2$: $R_2 = \frac{1}{2}\log_2(1+P_2) = 0.5$ bits/uso.

**Suma total:** $R_1 + R_2 \approx 0.661 + 0.5 = 1.161$ bits/uso $= \frac{1}{2}\log_2(5)$. ✅

La suma SIC coincide exactamente con la cota superior. Esto demuestra que SIC es óptimo en suma de tasas para el MAC gaussiano.

### Parte (d): Slepian-Wolf

Con $H(X_1) = 2$, $H(X_2) = 1.5$, $H(X_1,X_2) = 2.8$ bits:

La información mutua es $I(X_1;X_2) = H(X_1) + H(X_2) - H(X_1,X_2) = 2 + 1.5 - 2.8 = 0.7$ bits.

La región de Slepian-Wolf exige:
$$R_1 \geq H(X_1 | X_2) = H(X_1,X_2) - H(X_2) = 2.8 - 1.5 = 1.3 \text{ bits/símbolo}$$
$$R_2 \geq H(X_2 | X_1) = H(X_1,X_2) - H(X_1) = 2.8 - 2 = 0.8 \text{ bits/símbolo}$$
$$R_1 + R_2 \geq H(X_1,X_2) = 2.8 \text{ bits/símbolo}$$

**Conclusión:** Para decodificación conjunta perfecta, basta con $R_1 \geq 1.3$ y $R_2 \geq 0.8$. Si cada fuente se comprimiera sin conocer la otra, necesitaría $R_1 \geq H(X_1) = 2$ y $R_2 \geq H(X_2) = 1.5$. La correlación permite **ahorrar 0.7 bits/símbolo** en total.

---

## Ideas clave del ejercicio

1. La región de capacidad del MAC es un polígono convexo definido por $2^k - 1$ desigualdades para $k$ usuarios.
2. SIC alcanza la suma máxima — la ganancia multiusuario es real y computable.
3. Slepian-Wolf demuestra que compresión conjunta permite tasas imposibles de forma independiente.
4. La información mutua cuantifica exactamente el ahorro de Slepian-Wolf.
