# Ejercicio resuelto: Códigos polares y polarización de canales

**Módulo:** 02 — Teoría de la información  
**Artículo de referencia:** [Códigos Polares: El Primer Código que Alcanza la Capacidad de Shannon](../../02-teoria-informacion/17-codigos-polares.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

**(a)** Considera el canal de borrado binario BEC(0.4), donde la probabilidad de borrado es $\varepsilon = 0.4$ y el índice de Bhattacharyya inicial es $Z(W) = 0.4$. Usando las fórmulas de evolución $Z(W^-) \leq 2Z - Z^2$ y $Z(W^+) = Z^2$, aplica la transformación de polarización dos veces (obteniendo $N = 4$ sub-canales). Para cada sub-canal calcula $Z$ y la capacidad aproximada $C \approx 1 - Z$. Si quisieras construir un código $(4, 2)$ con $K = 2$ bits de información, ¿qué sub-canales elegirías como canales de información?

**(b)** Un código polar $(N=8, K=4)$ fija los bits congelados en las posiciones $\mathcal{A}^c = \left\lbrace 1, 2, 3, 5 \right\rbrace$ (las más ruidosas, todas a cero) y los bits de información en las posiciones $\mathcal{A} = \left\lbrace 4, 6, 7, 8 \right\rbrace$. El vector de entrada es $\mathbf{u} = (u_1, \dots, u_8)$ con $u_4 = 1$, $u_6 = 0$, $u_7 = 1$, $u_8 = 1$ y los bits congelados iguales a 0. La palabra código se genera como $\mathbf{c} = \mathbf{u}\, G_8$ con $G_8 = B_8 \cdot F^{\otimes 3}$. Usando la estructura recursiva de la codificación polar, calcula los cuatro primeros bits de la palabra código $(c_1, c_2, c_3, c_4)$.

**(c)** Explica por qué el decodificador SCL con lista $L = 8$ supera al decodificador SC simple en longitudes finitas ($N \leq 1024$), a pesar de que SC sea óptimo en el límite asintótico. ¿Por qué añadir un CRC-24 mejora aún más el rendimiento de SCL?

**(d)** En 5G NR, el canal de control usa códigos polares con $N$ hasta 512 y $K$ hasta 164 bits de información, protegidos con un CRC-24. Estima cuántos bits de redundancia total usa este esquema y calcula la tasa de codificación resultante (bits de información útil sobre bits transmitidos).

---

## Solución

### Parte (a): Polarización de BEC(0.4) con N = 4

El canal de borrado binario BEC($\varepsilon$) tiene índice de Bhattacharyya $Z(W) = \varepsilon$. Para $\varepsilon = 0.4$:

$$Z(W) = 0.4, \qquad C(W) = 1 - 0.4 = 0.6$$

**Capa 1** — Se combinan dos copias de $W$ obteniendo dos sub-canales:

$$Z(W^-) = 2Z - Z^2 = 2(0.4) - (0.4)^2 = 0.80 - 0.16 = 0.64$$
$$Z(W^+) = Z^2 = (0.4)^2 = 0.16$$

Verificación de conservación de capacidad: $C(W^-) + C(W^+) = (1 - 0.64) + (1 - 0.16) = 0.36 + 0.84 = 1.20 = 2 \times 0.6 = 2C(W)$. ✓

**Capa 2** — Se aplica la transformación a cada sub-canal de la capa 1, obteniendo los 4 sub-canales de $N = 4$:

A partir de $W^-$ (con $Z = 0.64$):

$$Z\!\left(W_4^{(1)}\right) = Z\!\left((W^-)^-\right) = 2(0.64) - (0.64)^2 = 1.28 - 0.4096 = 0.8704$$
$$Z\!\left(W_4^{(2)}\right) = Z\!\left((W^-)^+\right) = (0.64)^2 = 0.4096$$

A partir de $W^+$ (con $Z = 0.16$):

$$Z\!\left(W_4^{(3)}\right) = Z\!\left((W^+)^-\right) = 2(0.16) - (0.16)^2 = 0.32 - 0.0256 = 0.2944$$
$$Z\!\left(W_4^{(4)}\right) = Z\!\left((W^+)^+\right) = (0.16)^2 = 0.0256$$

Resumen de los 4 sub-canales:

| Sub-canal | Origen | $Z$ | $C \approx 1 - Z$ |
|-----------|--------|-----|-------------------|
| $W_4^{(1)}$ | $(W^-)^-$ | 0.8704 | 0.1296 |
| $W_4^{(2)}$ | $(W^-)^+$ | 0.4096 | 0.5904 |
| $W_4^{(3)}$ | $(W^+)^-$ | 0.2944 | 0.7056 |
| $W_4^{(4)}$ | $(W^+)^+$ | 0.0256 | 0.9744 |

Verificación: $\sum C \approx 0.1296 + 0.5904 + 0.7056 + 0.9744 = 2.40 = 4 \times 0.6 = N \cdot C(W)$. ✓

**Selección de sub-canales para K = 2:** Se eligen los 2 sub-canales con menor $Z$ (mayor capacidad):

$$\mathcal{A} = \left\lbrace 3, 4 \right\rbrace \quad \text{(sub-canales 3 y 4, con } Z = 0.2944 \text{ y } Z = 0.0256 \text{)}$$

Los sub-canales 1 y 2 llevan frozen bits. La tasa resultante es $R = K/N = 2/4 = 0.5 < C(W) = 0.6$, como corresponde a una elección de tasa conservadora por debajo de la capacidad.

---

### Parte (b): Codificación polar (N=8, K=4)

El vector de entrada completo es:

$$\mathbf{u} = (u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8) = (0, 0, 0, 1, 0, 0, 1, 1)$$

La estructura recursiva de $G_8 = B_8 \cdot F^{\otimes 3}$ se puede explotar sin calcular la matriz completa. La codificación polar procede por etapas de mariposa sobre el vector $\mathbf{u}$.

La transformación $F^{\otimes 3}$ se aplica como tres capas de operaciones XOR. En cada capa, los pares de posiciones $(i, i + 2^{k-1})$ para $k = 1, 2, 3$ se combinan como:

$$v_i = u_i \oplus u_{i + 2^{k-1}}, \qquad v_{i + 2^{k-1}} = u_{i + 2^{k-1}}$$

Seguimos las tres capas para obtener $\mathbf{s} = \mathbf{u} \cdot F^{\otimes 3}$ (antes de la permutación bit-reversal):

**Capa 1** (stride = 1, pares adyacentes):

$$s_1^{(1)} = u_1 \oplus u_2 = 0 \oplus 0 = 0$$
$$s_2^{(1)} = u_2 = 0$$
$$s_3^{(1)} = u_3 \oplus u_4 = 0 \oplus 1 = 1$$
$$s_4^{(1)} = u_4 = 1$$
$$s_5^{(1)} = u_5 \oplus u_6 = 0 \oplus 0 = 0$$
$$s_6^{(1)} = u_6 = 0$$
$$s_7^{(1)} = u_7 \oplus u_8 = 1 \oplus 1 = 0$$
$$s_8^{(1)} = u_8 = 1$$

Resultado tras capa 1: $(0, 0, 1, 1, 0, 0, 0, 1)$.

**Capa 2** (stride = 2, pares con distancia 2):

$$s_1^{(2)} = s_1^{(1)} \oplus s_3^{(1)} = 0 \oplus 1 = 1$$
$$s_2^{(2)} = s_2^{(1)} \oplus s_4^{(1)} = 0 \oplus 1 = 1$$
$$s_3^{(2)} = s_3^{(1)} = 1$$
$$s_4^{(2)} = s_4^{(1)} = 1$$
$$s_5^{(2)} = s_5^{(1)} \oplus s_7^{(1)} = 0 \oplus 0 = 0$$
$$s_6^{(2)} = s_6^{(1)} \oplus s_8^{(1)} = 0 \oplus 1 = 1$$
$$s_7^{(2)} = s_7^{(1)} = 0$$
$$s_8^{(2)} = s_8^{(1)} = 1$$

Resultado tras capa 2: $(1, 1, 1, 1, 0, 1, 0, 1)$.

**Capa 3** (stride = 4, pares con distancia 4):

$$s_1^{(3)} = s_1^{(2)} \oplus s_5^{(2)} = 1 \oplus 0 = 1$$
$$s_2^{(3)} = s_2^{(2)} \oplus s_6^{(2)} = 1 \oplus 1 = 0$$
$$s_3^{(3)} = s_3^{(2)} \oplus s_7^{(2)} = 1 \oplus 0 = 1$$
$$s_4^{(3)} = s_4^{(2)} \oplus s_8^{(2)} = 1 \oplus 1 = 0$$
$$s_5^{(3)} = s_5^{(2)} = 0$$
$$s_6^{(3)} = s_6^{(2)} = 1$$
$$s_7^{(3)} = s_7^{(2)} = 0$$
$$s_8^{(3)} = s_8^{(2)} = 1$$

Resultado de $\mathbf{u} \cdot F^{\otimes 3}$: $(1, 0, 1, 0, 0, 1, 0, 1)$.

La permutación bit-reversal $B_8$ reordena los índices según la inversión binaria de 3 bits:

| Índice original | Binario | Invertido | Índice destino |
|-----------------|---------|-----------|----------------|
| 1 | 001 | 100 | 5 |
| 2 | 010 | 010 | 3 |
| 3 | 011 | 110 | 7 |
| 4 | 100 | 001 | 2 |
| 5 | 101 | 101 | 6 |
| 6 | 110 | 011 | 4 |
| 7 | 111 | 111 | 8 |
| 8 | 000 | 000 | 1 |

Aplicando $B_8$ al vector $(1, 0, 1, 0, 0, 1, 0, 1)$: la posición $i$ del resultado va a la posición bit-reversal de $i$.

$$c_1 = s_8^{(3)} = 1, \quad c_2 = s_4^{(3)} = 0, \quad c_3 = s_2^{(3)} = 0, \quad c_4 = s_6^{(3)} = 1$$

Los cuatro primeros bits de la palabra código son:

$$\boxed{(c_1, c_2, c_3, c_4) = (1, 0, 0, 1)}$$

---

### Parte (c): SCL vs SC en longitudes finitas

**Por qué SC falla en longitudes finitas.** El decodificador SC decide cada bit $\hat{u}_i$ de forma irrevocable, de menor a mayor índice. Una vez que comete un error en la posición $i$, ese valor incorrecto se usa como información lateral para todas las decisiones posteriores: el error se propaga y amplifica. En el límite $N \to \infty$, la probabilidad de cada decisión individual tiende a cero con suficiente rapidez para que el error total se anule, pero para $N \leq 1024$ los márgenes de decisión son estrechos y la propagación es significativa.

**Por qué SCL supera a SC.** SCL mantiene simultáneamente $L$ hipótesis de decodificación (trayectorias). En cada posición de bit de información, cada hipótesis se bifurca en dos (bit = 0 y bit = 1), y se conservan solo las $L$ de mayor métrica acumulada (log-verosimilitud de trayectoria). Esto equivale a una búsqueda en árbol de anchura $L$: si el camino correcto fue eliminado en SC por un margen estrecho, en SCL sobrevive en la lista siempre que no haya $L$ caminos mejores que él. Con $L = 8$, la probabilidad de que el camino correcto sea expulsado cae drásticamente respecto a SC ($L = 1$). La mejora es especialmente notable en $N$ finito, donde los márgenes son pequeños; asintóticamente, SC ya opera sin errores y el beneficio de la lista se vuelve marginal.

**Por qué CRC-24 mejora aún más SCL.** Al final de la decodificación SCL, hay $L$ candidatos plausibles pero no se sabe cuál es el correcto: elegir el de mayor métrica puede fallar si el candidato incorrecto acumuló una métrica ligeramente mayor por azar. El CRC-24 actúa como selector: de los $L$ candidatos, se elige el primero que pasa la verificación CRC. La probabilidad de que una palabra incorrecta pase un CRC de 24 bits es $2^{-24} \approx 6 \times 10^{-8}$, que es despreciable. En la práctica, si el candidato correcto está en la lista (lo que ocurre con alta probabilidad con $L = 8$), el CRC lo identifica de forma casi infalible. La combinación SCL + CRC-24 con $L = 8$ alcanza el estado del arte en longitudes cortas y fue la elegida para el canal de control de 5G NR.

---

### Parte (d): Redundancia y tasa en 5G NR

El esquema de canal de control en 5G NR funciona con:

- **Bits de información útil:** $K = 164$ bits (máximo especificado).
- **CRC añadido:** 24 bits de redundancia para verificación.
- **Longitud del bloque polar:** $N = 512$ bits (máximo del canal de control eMBB).

El vector de entrada al codificador polar tiene longitud $N = 512$, de los cuales:
- $K + r_{\text{CRC}} = 164 + 24 = 188$ bits son bits de información efectiva (incluyendo el CRC).
- $N - (K + r_{\text{CRC}}) = 512 - 188 = 324$ bits son frozen bits (redundancia estructural del código polar).

**Redundancia total:**

$$r_{\text{total}} = N - K = 512 - 164 = 348 \text{ bits}$$

Descompuesta en:
- 24 bits de CRC (detectan errores en la lista SCL).
- 324 bits frozen (posiciones de peor calidad, fijadas a cero).

**Tasa de codificación resultante** (bits de información útil sobre bits transmitidos):

$$R = \frac{K}{N} = \frac{164}{512} \approx 0.320$$

Si se incluye el CRC como parte del payload transmitido (es decir, consideramos los 188 bits como "datos de canal" y los 324 como redundancia de corrección):

$$R_{\text{canal}} = \frac{K + r_{\text{CRC}}}{N} = \frac{188}{512} \approx 0.367$$

La tasa útil desde el punto de vista del usuario (ignorando el overhead del CRC) es $R \approx 0.32$, muy por debajo de la capacidad del canal a la SNR de operación. Esta holgura es intencional: el canal de control 5G debe funcionar de forma fiable incluso en condiciones de baja SNR en el borde de la celda, y el margen garantiza una probabilidad de error de bloque inferior a $10^{-3}$.

---

## Ideas clave del ejercicio

1. La polarización es **autocatalítica**: en cada capa, los buenos sub-canales mejoran cuadráticamente ($Z \to Z^2$) y los malos empeoran cuadráticamente ($Z \to 2Z - Z^2 \approx 1 - (1-Z)^2$). Dos capas de BEC(0.4) producen un sub-canal casi perfecto ($Z = 0.0256$) y uno casi inútil ($Z = 0.8704$) a partir de sub-canales mediocres.

2. La codificación polar es **XOR en capas**: la estructura de mariposa de $F^{\otimes n}$ seguida de la permutación bit-reversal $B_N$ se ejecuta como una FFT binaria, con complejidad $O(N \log N)$ y sin multiplicaciones.

3. La limitación de SC en longitudes finitas es **la irrevocabilidad de las decisiones**: un error individual contamina todo el árbol de decodificación posterior. SCL lo corrige manteniendo $L$ hipótesis simultáneas a coste $O(L \cdot N \log N)$.

4. El CRC en SCL actúa como **oráculo de selección a costo mínimo**: no mejora la lista, sino que elige al ganador correcto de entre los $L$ supervivientes con probabilidad de fallo $\approx 2^{-24}$.

5. En 5G NR, la tasa $R \approx 0.32$ del canal de control refleja una elección de **fiabilidad sobre eficiencia espectral**: se transmiten muchos bits de redundancia para garantizar operabilidad en condiciones de canal adversas.
