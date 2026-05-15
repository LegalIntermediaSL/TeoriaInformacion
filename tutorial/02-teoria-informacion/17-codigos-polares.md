# Códigos Polares: El Primer Código que Alcanza la Capacidad de Shannon

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min

## Prerrequisitos

- [Teorema de Shannon y capacidad](08-teorema-de-shannon-capacidad.md)
- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)

## Objetivos de aprendizaje

1. Entender el fenómeno de polarización de canales y su demostración intuitiva.
2. Calcular el índice de Bhattacharyya para medir la calidad de un sub-canal.
3. Construir un código polar eligiendo los mejores sub-canales.
4. Describir los algoritmos de decodificación SC y SCL con su complejidad.
5. Ubicar los códigos polares en el contexto de 5G NR y compararlos con LDPC y turbo.

---

## Intuición

Hasta 2009, ningún código con decodificador de complejidad polinomial había demostrado
**alcanzar exactamente** la capacidad de Shannon (no solo aproximarse). Los códigos turbo
y LDPC se quedan a un pequeño margen — demostrable empíricamente, pero sin prueba de
convergencia exacta a capacidad en el sentido teórico estricto.

En 2009, Erdal Arıkan publicó una construcción radicalmente diferente: los **códigos polares**.
La idea central es que si combinas copias de un canal ruidoso de forma inteligente, los canales
resultantes se *polarizan*: unos se vuelven casi perfectos (capacidad ≈ 1) y otros casi
inútiles (capacidad ≈ 0). Con suficientes copias, la fracción de canales buenos tiende
exactamente a la capacidad C del canal original. Se envían datos solo por los buenos;
los malos se "congelan" a valores conocidos.

El resultado: **complejidad de codificación y decodificación O(N log N)**, con una prueba
rigurosa de que la tasa de error tiende a cero al alcanzar la capacidad. Es el único
código con esta garantía teórica.

---

## Polarización de canales

### El núcleo de polarización

Parte de un canal binario simétrico memoryless (B-DMC) W con capacidad C(W). Combina
**dos copias** de W mediante una sencilla transformación:

$$W^-(y_1, y_2 \mid u_1) = \sum_{u_2 \in \left\lbrace 0,1 \right\rbrace} \frac{1}{2}\, W(y_1 \mid u_1 \oplus u_2)\, W(y_2 \mid u_2)$$

$$W^+(y_1, y_2, u_1 \mid u_2) = \frac{1}{2}\, W(y_1 \mid u_1 \oplus u_2)\, W(y_2 \mid u_2)$$

El canal **degradado** $W^-$ recibe $u_1$ sin conocer $u_2$ — como una interferencia extra.
El canal **mejorado** $W^+$ recibe $u_2$ con la ayuda del ya decodificado $u_1$ como información
lateral. Se cumple:

$$C(W^-) + C(W^+) = 2\,C(W)$$

La capacidad total se conserva, pero se *redistribuye*: $W^+$ mejora y $W^-$ empeora.
Al aplicar la transformación recursivamente $n = \log_2 N$ veces sobre $N$ copias del canal,
se obtienen $N$ sub-canales sintéticos $W_N^{(i)}$, $i = 1, \dots, N$.

### El teorema de polarización (Arıkan, 2009)

Para cualquier B-DMC W con capacidad $C(W) \in (0,1)$, y para todo $\delta > 0$:

$$\lim_{N \to \infty} \frac{1}{N} \left| \left\lbrace i : C(W_N^{(i)}) > 1 - \delta \right\rbrace \right| = C(W)$$
$$\lim_{N \to \infty} \frac{1}{N} \left| \left\lbrace i : C(W_N^{(i)}) < \delta \right\rbrace \right| = 1 - C(W)$$

En el límite, la fracción de buenos sub-canales converge **exactamente** a C(W).

---

## Índice de Bhattacharyya

Para medir la calidad de un sub-canal sin calcular su capacidad exacta, se usa el
**índice de Bhattacharyya**:

$$Z(W) = \sum_{y \in \mathcal{Y}} \sqrt{W(y \mid 0)\, W(y \mid 1)}$$

Sus propiedades clave:
- $Z(W) \in [0, 1]$: canal perfecto $\Rightarrow Z = 0$; canal inútil $\Rightarrow Z = 1$.
- Relacionado con la capacidad: $C(W) \approx 1 - Z(W)$ para canales casi perfectos.
- Evolución bajo polarización: $Z(W^-) \leq 2Z(W) - Z(W)^2$ y $Z(W^+) = Z(W)^2$.

El sub-canal mejorado $W^+$ tiene $Z$ cuadráticamente pequeño; el degradado $W^-$ tiene $Z$
cuadráticamente grande. La polarización es **exponencialmente rápida** en el número de capas.

---

## Construcción del código polar

Para un código polar $(N, K)$ con $N = 2^n$:

1. **Calcular** $Z(W_N^{(i)})$ para todos los $N$ sub-canales.
2. **Ordenar** los sub-canales de mejor (menor Z) a peor (mayor Z).
3. **Seleccionar** los $K$ mejores sub-canales: forman el conjunto de índices de información
   $\mathcal{A}$ (*information set*).
4. Los $N - K$ sub-canales restantes son los *frozen bits*: se fijan al valor conocido 0
   (o cualquier valor acordado entre transmisor y receptor).

La tasa del código es $R = K/N$. El conjunto $\mathcal{A}$ depende del canal W y de la
relación señal-ruido (SNR) de operación.

---

## Codificación

Sea $\mathbf{u} = (u_1, \dots, u_N) \in \left\lbrace 0,1 \right\rbrace^N$ el vector de entrada:
los bits de información en las posiciones $\mathcal{A}$ y ceros (frozen) en las demás.
La palabra código es:

$$\mathbf{x} = \mathbf{u}\, G_N$$

donde la **matriz generatriz** es:

$$G_N = B_N\, F^{\otimes n}, \qquad F = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$$

$F^{\otimes n}$ es el producto tensorial de Kronecker de $F$ consigo misma $n$ veces,
y $B_N$ es la permutación *bit-reversal* (inversión de bits del índice en binario).
La codificación se implementa como una mariposa tipo FFT: **complejidad O(N log N)**.

---

## Decodificación: Successive Cancellation (SC)

El decodificador SC explota la estructura recursiva del código mediante un **árbol binario**
de profundidad $n$. Decodifica $\hat{u}_i$ de forma secuencial para $i = 1, \dots, N$:

$$\hat{u}_i = \begin{cases}
  0 & \text{si } i \notin \mathcal{A} \text{ (frozen bit)} \\
  \arg\max_{u \in \left\lbrace 0,1 \right\rbrace} W_N^{(i)}(\mathbf{y}, \hat{u}_1^{i-1} \mid u) & \text{si } i \in \mathcal{A}
\end{cases}$$

La decisión se toma en base a las **razones de verosimilitud logarítmicas** (LLR):

$$L_N^{(i)} = \log \frac{W_N^{(i)}(\mathbf{y}, \hat{u}_1^{i-1} \mid 0)}{W_N^{(i)}(\mathbf{y}, \hat{u}_1^{i-1} \mid 1)}$$

Las LLR se calculan recursivamente en el árbol binario usando las operaciones:

$$f(a, b) = \log \frac{1 + e^{a+b}}{e^a + e^b} \approx \text{sign}(a)\,\text{sign}(b)\,\min(|a|,|b|)$$
$$g(a, b, \hat{u}) = (-1)^{\hat{u}}\, a + b$$

**Complejidad:** $O(N \log N)$ en tiempo y $O(N)$ en espacio.

**Limitación:** en longitudes de bloque finitas, el decodificador SC comete errores
propagados — si $\hat{u}_i$ es incorrecto, las decisiones posteriores se ven afectadas.

---

## Decodificación: SC con Lista (SCL)

El decodificador **SCL** (Tal & Vardy, 2015) mantiene una lista de $L$ hipótesis
de decodificación en paralelo. En cada posición $i$:

- Para frozen bits: todas las hipótesis asignan $\hat{u}_i = 0$.
- Para bits de información: cada hipótesis se bifurca en dos (una por cada valor posible),
  y se conservan solo las $L$ con mayor métrica de trayectoria (path metric).

Al final, se selecciona la hipótesis de mayor métrica (o la que pasa una verificación CRC).

**SCL + CRC** (con un CRC externo de $r$ bits):

- La lista tiene $L$ candidatos; el CRC selecciona el válido entre ellos.
- Típicamente $L = 32$ y $r = 24$ bits son suficientes para el 5G NR.
- En longitudes de bloque finitas (~1000 bits), supera a LDPC y es comparable a turbo.

**Complejidad:** $O(L \cdot N \log N)$ — manejable para $L$ moderado.

---

## Ejemplo numérico: BEC(0.5) con N = 4

Considérese el canal de borrado binario (BEC) con probabilidad de borrado $\varepsilon = 0.5$.
Capacidad: $C = 1 - \varepsilon = 0.5$.

El índice de Bhattacharyya inicial es $Z(W) = \varepsilon = 0.5$.

**Capa 1** (dos copias de W combinadas, $N = 2$):

$$Z(W^-) = 2(0.5) - (0.5)^2 = 0.75, \quad C(W^-) = 0.25$$
$$Z(W^+) = (0.5)^2 = 0.25, \quad C(W^+) = 0.75$$

**Capa 2** (cuatro sub-canales, $N = 4$):

| Sub-canal | Origen   | $Z$                        | $C \approx 1 - Z$ |
|-----------|----------|----------------------------|-------------------|
| $W_4^{(1)}$ | $(W^-)^-$ | $2(0.75) - (0.75)^2 = 0.9375$ | 0.0625         |
| $W_4^{(2)}$ | $(W^-)^+$ | $(0.75)^2 = 0.5625$         | 0.4375            |
| $W_4^{(3)}$ | $(W^+)^-$ | $2(0.25) - (0.25)^2 = 0.4375$ | 0.5625          |
| $W_4^{(4)}$ | $(W^+)^+$ | $(0.25)^2 = 0.0625$         | 0.9375            |

Para un código $(4, 2)$ con $R = 0.5$: se eligen los sub-canales 3 y 4
(los dos de mayor capacidad). Los sub-canales 1 y 2 llevan frozen bits.
La suma de capacidades: $0.0625 + 0.4375 + 0.5625 + 0.9375 = 2.0 = N \cdot C(W)$. ✓

---

## Códigos polares en 5G NR

El estándar **5G New Radio** (3GPP Release 15, 2017) adoptó los códigos polares para:

- **Canal de control eMBB** (Enhanced Mobile Broadband): bloques de información de hasta
  $K = 140$ bits con $N \leq 512$.
- Decodificación **SCL + CRC** con $L = 8$ y CRC-24.
- Codificación **LDPC** para el canal de datos (bloques más largos).

La elección refleja que en longitudes cortas los polares superan a LDPC; en longitudes
largas la ventaja se invierte.

---

## Comparativa: Polar vs LDPC vs Turbo

| Característica          | Códigos polares        | Códigos LDPC           | Códigos turbo          |
|-------------------------|------------------------|------------------------|------------------------|
| Año de invención        | 2009 (Arıkan)          | 1960 (Gallager)        | 1993 (Berrou et al.)   |
| Alcanza capacidad       | Sí (demostrado)        | Solo asintóticamente   | Solo asintóticamente   |
| Complejidad codificación| O(N log N)             | O(N)                   | O(N)                   |
| Complejidad decodificación | O(L · N log N)      | O(iter · N)            | O(iter · N)            |
| Longitudes cortas       | Excelente (SCL+CRC)    | Moderada               | Buena                  |
| Longitudes largas       | Muy buena              | Excelente              | Buena                  |
| Gap a capacidad (finito)| ~0.3–0.5 dB con SCL   | ~0.1–0.3 dB            | ~0.5–1 dB              |
| Uso en 5G NR            | Canal de control       | Canal de datos         | (LTE, no 5G)           |

---

## Ideas clave

- La **polarización** transforma N copias ruidosas en sub-canales que convergen a perfectos
  o inútiles: la fracción de buenos sub-canales iguala exactamente la capacidad C del canal.
- El **índice de Bhattacharyya** Z(W) es una medida computable de calidad del sub-canal;
  evoluciona cuadráticamente bajo polarización, garantizando convergencia exponencial.
- La **construcción del código** consiste en seleccionar los K mejores sub-canales y
  fijar (congelar) el resto — una elección que depende del canal y la SNR objetivo.
- La **matriz generatriz** $G_N = B_N F^{\otimes n}$ se aplica como una FFT binaria en O(N log N).
- El decodificador **SC** tiene complejidad O(N log N) con una garantía de error tendiendo
  a cero en el límite, pero exhibe propagación de errores en longitudes finitas.
- El decodificador **SCL + CRC** subsana la limitación práctica y alcanza el estado del arte
  en longitudes cortas, siendo el elegido para el canal de control en 5G NR.

---

## Ejercicios

1. **Polarización básica.** Para el BSC con probabilidad de error $p = 0.1$, calcula
   $Z(W^-)$ y $Z(W^+)$. ¿Cuántas capas son necesarias para que al menos un sub-canal
   tenga $Z < 0.01$?

2. **Selección de índices.** Para BEC(0.4) con $N = 8$, calcula los 8 índices de
   Bhattacharyya y construye un código $(8, 4)$. Verifica que la suma de capacidades
   de los sub-canales seleccionados supere a los no seleccionados.

3. **Codificación.** Dado el conjunto de información $\mathcal{A} = \left\lbrace 3, 4 \right\rbrace$
   para un código $(4,2)$, y el mensaje $(m_1, m_2) = (1, 0)$, calcula la palabra
   código $\mathbf{x} = \mathbf{u}\, G_4$ con $G_4 = B_4 F^{\otimes 2}$.

4. **Decodificación SC.** Describe el árbol de decodificación SC para $N = 4$.
   ¿En qué orden se calculan las LLR? ¿Cuántas operaciones $f(\cdot)$ y $g(\cdot)$
   se realizan en total?

5. **Comparativa.** Un sistema necesita transmitir bloques de $K = 100$ bits con
   tasa $R = 0.5$ a SNR de $2$ dB. Razona qué código elegirías (polar, LDPC o turbo)
   y qué parámetros del decodificador configurarías.

6. **Desafío.** El índice de Bhattacharyya satisface $Z(W) \leq \sqrt{1 - C(W)^2}$.
   Demuestra esta cota usando la desigualdad de Cauchy-Schwarz aplicada a la definición
   de Z(W) y de la capacidad del canal binario simétrico.

---

## Véase también

- [Códigos LDPC y turbo](11-codigos-ldpc-y-turbo.md)
- [Canales discretos y capacidad](04-canales-discretos-y-capacidad.md)

---


<!-- nav-start -->

---
← [Teoría de la Información en Redes](16-teoria-informacion-en-redes.md) · [Canal con Estado: Teorema de Gel'fand-Pinsker](18-canal-con-estado-gelfand-pinsker.md) →

<!-- nav-end -->
## Referencias

1. Arıkan, E. (2009). *Channel Polarization: A Method for Constructing Capacity-Achieving
   Codes for Symmetric Binary-Input Memoryless Channels*. IEEE Transactions on Information
   Theory, 55(7), 3051–3073.

2. Tal, I., & Vardy, A. (2015). *List Decoding of Polar Codes*. IEEE Transactions on
   Information Theory, 61(5), 2213–2226.

3. Trifonov, P. (2012). *Efficient Design and Decoding of Polar Codes*. IEEE Transactions
   on Communications, 60(11), 3221–3227.

4. 3GPP TS 38.212 (2018). *NR; Multiplexing and Channel Coding*. 3rd Generation Partnership
   Project, Release 15.

5. Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.).
   Wiley-Interscience. Cap. 7–8.

6. Mori, R., & Tanaka, T. (2009). *Performance of Polar Codes with the Construction using
   Density Evolution*. IEEE Communications Letters, 13(7), 519–521.
