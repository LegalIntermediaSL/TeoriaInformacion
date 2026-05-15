# Canal con Estado: Teorema de Gel'fand-Pinsker

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~22 min

## Prerrequisitos

- [Teorema de Shannon y capacidad de canal](08-teorema-de-shannon-capacidad.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)

## Objetivos de aprendizaje

1. Comprender el modelo de canal con estado conocido solo en el transmisor.
2. Enunciar el teorema de Gel'fand-Pinsker (1980) e interpretar la variable auxiliar $U$.
3. Distinguir el conocimiento causal del no causal del estado y sus implicaciones en capacidad.
4. Derivar el Dirty Paper Coding (Costa, 1983) como caso especial Gaussiano.
5. Identificar aplicaciones en MIMO, watermarking y redes inalámbricas.

---

## Intuición

Imagina que el transmisor de un canal de comunicación conoce de antemano una interferencia que va a afectar al receptor. El receptor no conoce esa interferencia. ¿Puede el transmisor "esconderse" dentro de ella y transmitir información gratis?

La respuesta es sorprendente: **sí, y sin coste adicional de potencia**. Este es el núcleo del teorema de Gel'fand-Pinsker y su caso más famoso, el *Dirty Paper Coding* (DPC) de Costa: en un canal Gaussiano con interferencia aditiva conocida en el transmisor, la capacidad es exactamente la misma que si la interferencia no existiera.

La idea recuerda a escribir en un folio sucio: si conoces exactamente dónde están las manchas antes de escribir, puedes rodearlas sin que el lector pierda ningún bit de información.

---

## Modelo formal

### Canal con estado

Sea un canal discreto sin memoria con:

- Entrada del transmisor: $X \in \mathcal{X}$
- Estado del canal: $S \in \mathcal{S}$, i.i.d. con distribución $p(s)$
- Salida del receptor: $Y \in \mathcal{Y}$

El canal queda definido por la distribución condicional:

$$p(y \mid x, s)$$

La relación entre variables puede escribirse funcionalmente como $Y = f(X, S, Z)$ donde $Z$ representa ruido adicional independiente.

**Supuesto central:** el estado $S^n = (S_1, \ldots, S_n)$ es conocido por el **transmisor** antes de la transmisión, pero **no** por el receptor.

### Dos regímenes de conocimiento

| Régimen | Conocimiento del estado | Capacidad |
|---------|------------------------|-----------|
| **No causal** | $S^n$ completo antes de codificar | $C = \max_{p(u,x\mid s)} \left[ I(U;Y) - I(U;S) \right]$ |
| **Causal** | Solo $S_i$ en el instante $i$ | $C = \max_{p(x\mid s)} I(X;Y)$ |
| **Sin conocimiento** | $S$ desconocido en Tx | $C \leq \max_{p(x)} I(X;Y)$ (capacidad reducida) |

---

## Teorema de Gel'fand-Pinsker (1980)

### Enunciado

Sea un canal con estado $p(y \mid x, s)$ donde el estado $S \sim p(s)$ es conocido **no causalmente** en el transmisor. La capacidad del canal es:

$$\boxed{C = \max_{p(u,x \mid s)} \left[ I(U; Y) - I(U; S) \right]}$$

donde la maximización se realiza sobre todas las distribuciones conjuntas $p(u, x \mid s)$ y $U$ es una **variable auxiliar** (*auxiliary random variable*) con alfabeto $\mathcal{U}$ que puede tomarse de cardinalidad $|\mathcal{U}| \leq |\mathcal{X}| \cdot |\mathcal{S}| + 1$.

### La variable auxiliar $U$: precoding

La variable $U$ es la clave del teorema. Representa el **mensaje precodificado** que el transmisor diseña teniendo en cuenta el estado. En lugar de transmitir $X$ directamente, el transmisor elige $U$ que "absorbe" parte de la información del estado, y luego genera $X$ a partir de $(U, S)$.

Intuitivamente:

- $I(U; Y)$ mide cuánta información sobre $U$ llega al receptor a través de $Y$.
- $I(U; S)$ mide cuánta información sobre el estado $S$ está "contenida" en $U$, es decir, la parte de $U$ que ha sido "gastada" en combatir la interferencia.
- La diferencia $I(U;Y) - I(U;S)$ es la información **neta** que puede comunicarse.

### Esquema de codificación (binning)

La prueba de alcanzabilidad emplea la técnica de **binning de Wyner**:

1. Generar $2^{n(I(U;S) + \epsilon)}$ palabras $u^n$ i.i.d. según $p(u)$.
2. Dividir aleatoriamente en $2^{nR}$ bins, cada uno con $\approx 2^{n \cdot I(U;S)}$ palabras.
3. Para transmitir el mensaje $m$ (bin $m$) dada la secuencia de estado $s^n$: buscar una $u^n$ en el bin $m$ que sea **conjuntamente típica** con $s^n$. Con alta probabilidad existe tal $u^n$.
4. Generar $x^n$ símbolo a símbolo desde $p(x_i \mid u_i, s_i)$ y transmitir.
5. El receptor, sin conocer $s^n$, busca la única $u^n$ conjuntamente típica con $y^n$. Puede hacerlo si $R < I(U;Y) - I(U;S)$.

---

## Caso causal: Shannon (1958)

Cuando el transmisor solo conoce $S_i$ en el instante $i$ (conocimiento **causal**), la capacidad se reduce a:

$$C_{\text{causal}} = \max_{p(x \mid s)} I(X; Y)$$

Esto equivale a que el transmisor adapte su símbolo $X_i$ al estado actual $S_i$, pero sin la capacidad de "pre-codificar" usando el estado futuro. En el canal binario aditivo con estado, esto puede recuperar parte de la pérdida, pero no toda.

**Resultado notable:** el conocimiento causal permite igualar la capacidad del canal sin estado cuando la interferencia es aditiva modulada ($Y = X \oplus S$, canal binario simétrico con estado), pero en el caso Gaussiano el conocimiento no causal es estrictamente mejor.

---

## Dirty Paper Coding: el caso Gaussiano (Costa, 1983)

### Modelo

Considera el canal Gaussiano con interferencia conocida:

$$Y = X + S + Z$$

donde:
- $X$ es la entrada con restricción de potencia $\mathbb{E}[X^2] \leq P$
- $S \sim \mathcal{N}(0, Q)$ es la interferencia conocida en el transmisor (no en el receptor)
- $Z \sim \mathcal{N}(0, N)$ es ruido Gaussiano independiente

### Resultado

Costa demostró que la capacidad es:

$$C_{\text{DPC}} = \frac{1}{2} \log\!\left(1 + \frac{P}{N}\right)$$

**¡Exactamente la misma que si $S = 0$!** La interferencia $S$, aunque desconocida para el receptor y potencialmente de potencia $Q$ arbitrariamente grande, no reduce la capacidad en absoluto.

### Variable auxiliar óptima

La variable auxiliar que logra esta capacidad es:

$$U = X + \alpha S, \qquad \alpha = \frac{P}{P + N}$$

Con $X \sim \mathcal{N}(0, P)$ independiente de $S$ y $Z$. Se puede verificar:

$$I(U; Y) - I(U; S) = \frac{1}{2} \log\!\left(1 + \frac{P}{N}\right)$$

La elección de $\alpha$ cancela exactamente la interferencia en la variable $U$, sin gastar potencia adicional.

### Interpretación geométrica

El transmisor "escribe" el mensaje en el espacio ortogonal a la interferencia conocida. Como conoce $S^n$ de antemano, puede orientar su señal $X^n$ de modo que el receptor vea solo la componente útil más el ruido $Z^n$, ignorando $S^n$ por completo.

---

## Ejemplo numérico: canal binario con estado

### Configuración

Sea el canal binario con estado:

$$Y = X \oplus S \oplus Z$$

con $X, S, Z \in \left\lbrace 0, 1 \right\rbrace$, $S \sim \text{Bernoulli}(q)$, $Z \sim \text{Bernoulli}(p)$, y $S$ conocido no causalmente en el transmisor.

Cuando $p(u, x \mid s)$ se elige con $U = X \oplus S$ (precoding XOR), se puede calcular:

$$I(U; Y) = 1 - H(p), \qquad I(U; S) = 0$$

ya que $U = X \oplus S$ y $Y = U \oplus Z$, de modo que $U$ y $S$ resultan independientes bajo la distribución óptima.

### Cálculo numérico

Para $q = 0.3$, $p = 0.1$:

| Distribución | $I(U;Y)$ | $I(U;S)$ | $C$ |
|---|---|---|---|
| Sin precoding ($U = X$) | $1 - H(p * q) \approx 0.529$ | $0$ | $0.529$ bits |
| Con precoding ($U = X \oplus S$) | $1 - H(p) \approx 0.531$ | $0$ | **$0.531$ bits** |

donde $H(p * q)$ usa la convolución binaria $p * q = p(1-q) + q(1-p)$.

En este ejemplo, el precoding recupera la capacidad $1 - H(p)$, correspondiente al canal sin interferencia, ya que el estado queda cancelado.

---

## Conexiones con otros resultados

### Dualidad con Wyner-Ziv

El teorema de Gel'fand-Pinsker y el de Wyner-Ziv (compresión de fuente con información lateral en el decodificador) son **duales source-channel**:

| Problema | Información lateral | Fórmula |
|---|---|---|
| **Wyner-Ziv** (compresión) | En el decodificador | $R = I(U; X) - I(U; Y)$ |
| **Gel'fand-Pinsker** (canal) | En el codificador | $C = I(U; Y) - I(U; S)$ |

Ambos usan la misma técnica de binning; en Wyner-Ziv el receptor usa la información lateral para descifrar el bin correcto, mientras que en Gel'fand-Pinsker el transmisor usa la información lateral para elegir la palabra de código correcta dentro del bin.

### Canal broadcast degradado

En el canal broadcast de Marton y en el DPC para MIMO, la técnica de Gel'fand-Pinsker se aplica iterativamente: el mensaje del primer usuario actúa como interferencia "conocida" al codificar para el segundo usuario, permitiendo alcanzar la región de capacidad completa.

---

## Aplicaciones

### MIMO con DPC (precoding sucesivo)

En sistemas MIMO con $M$ antenas transmisoras y múltiples usuarios, el DPC se aplica **sucesivamente**: al codificar para el usuario $k$, las señales de los usuarios $1, \ldots, k-1$ ya codificadas actúan como interferencia conocida. El resultado alcanza la misma región de capacidad que el canal broadcast sin interferencia entre usuarios.

### Canales broadcast con beamforming

Los sistemas 5G/6G con beamforming masivo usan aproximaciones al DPC (como *Tomlinson-Harashima precoding*) para gestionar la interferencia inter-usuario. La ganancia teórica del DPC exacto es el límite superior de lo que estos esquemas prácticos pueden alcanzar.

### Marca de agua digital (watermarking)

El problema de watermarking robusto puede modelarse como un canal con estado:
- El "canal" es el proceso de ataque (compresión, recorte, ruido).
- El estado $S$ es el contenido portador (imagen, audio).
- El transmisor embebe la marca $X$ en el portador conocido.

El teorema G-P garantiza que el transmisor puede embeber información a tasa positiva incluso con portadores adversariales, siempre que los ataques sean acotados en energía.

### Redes inalámbricas con interferencia gestionada

En redes heterogéneas donde la estación base conoce la interferencia que generará sobre usuarios secundarios (por coordinación entre nodos), puede aplicar precoding G-P para maximizar el rendimiento global sin incrementar potencia.

---

## Ideas clave

1. **Gel'fand-Pinsker (1980):** la capacidad de un canal con estado conocido no causalmente en el transmisor es $C = \max_{p(u,x\mid s)} \left[ I(U;Y) - I(U;S) \right]$. La variable auxiliar $U$ actúa como señal precodificada.

2. **Binning como herramienta:** el transmisor genera muchas palabras $u^n$ y elige la que es típica conjuntamente con el estado observado; el receptor identifica el mensaje a partir de la salida del canal.

3. **DPC de Costa (1983):** en el canal Gaussiano $Y = X + S + Z$ con $S$ conocido en el transmisor, la capacidad es $\frac{1}{2}\log(1 + P/N)$, idéntica a la del canal sin interferencia. La interferencia de potencia arbitraria queda cancelada sin coste de potencia.

4. **Conocimiento causal vs. no causal:** el conocimiento causal permite adaptar la transmisión pero no precodificar; el conocimiento no causal es estrictamente más valioso en el caso Gaussiano.

5. **Dualidad Wyner-Ziv / Gel'fand-Pinsker:** los roles del codificador y decodificador se intercambian; la misma técnica de binning aparece en ambos extremos de la dualidad fuente-canal.

---

## Ejercicios

**Ejercicio 1 (básico).** En el canal binario simétrico con estado $Y = X \oplus S \oplus Z$, $S \sim \text{Bern}(0.5)$, $Z \sim \text{Bern}(p)$, sin conocimiento del estado en el transmisor. Calcula la capacidad y compárala con la capacidad G-P cuando $S$ es conocido no causalmente.

**Ejercicio 2 (medio).** Verifica algebraicamente que para el canal Gaussiano $Y = X + S + Z$ con $U = X + \alpha S$, la elección $\alpha = P/(P+N)$ maximiza $I(U;Y) - I(U;S)$ y que el valor máximo es $\frac{1}{2}\log(1 + P/N)$.

**Ejercicio 3 (medio).** Considera un canal binario con estado donde $\mathcal{X} = \mathcal{S} = \mathcal{Y} = \left\lbrace 0,1 \right\rbrace$, $S \sim \text{Bern}(0.3)$ y $Y = X \cdot S$ (canal borrado por el estado). Calcula $C_{\text{GP}}$ para el caso no causal y $C_{\text{causal}}$. ¿Cuál es la diferencia?

**Ejercicio 4 (avanzado).** En un sistema MIMO $2 \times 2$ con dos usuarios monoanténicos, plantea el problema DPC sucesivo. ¿Cuál es el orden óptimo de codificación si los usuarios tienen ganancias de canal distintas $h_1 > h_2$? Justifica usando la fórmula G-P.

**Ejercicio 5 (avanzado).** Demuestra que si el estado $S$ es independiente de $Y$ dado $X$ (es decir, el estado no afecta al receptor), entonces $C_{\text{GP}} = C_{\text{sin estado}}$. ¿Qué dice esto sobre la inutilidad del precoding cuando el estado no influye en la salida?

---

## Véase también

- [Teoría de la información en redes](16-teoria-informacion-en-redes.md) — capacidad de redes multi-usuario, región de capacidad broadcast y acceso múltiple.
- [Teoría tasa-distorsión](09-teoria-tasa-distorsion.md) — dualidad fuente-canal y el teorema de Wyner-Ziv como contraparte del teorema G-P.

---


<!-- nav-start -->

---
← [Códigos Polares: El Primer Código que Alcanza la Capacidad de Shannon](17-codigos-polares.md) · [Códigos Turbo y el Algoritmo BCJR](19-codigos-turbo.md) →

<!-- nav-end -->
## Referencias

1. **Gel'fand, S. I. & Pinsker, M. S.** (1980). Coding for channel with random parameters. *Problems of Control and Information Theory*, 9(1), 19–31.

2. **Costa, M. H. M.** (1983). Writing on dirty paper. *IEEE Transactions on Information Theory*, 29(3), 439–441.

3. **Shannon, C. E.** (1958). Channels with side information at the transmitter. *IBM Journal of Research and Development*, 2(4), 289–293.

4. **Cover, T. M. & Thomas, J. A.** (2006). *Elements of Information Theory* (2.ª ed.). Wiley. Capítulo 7: Channel Capacity with Side Information.

5. **Caire, G. & Shamai, S.** (2003). On the achievable throughput of a multiantenna Gaussian broadcast channel. *IEEE Transactions on Information Theory*, 49(7), 1691–1706.

6. **Weingarten, H., Steinberg, Y. & Shamai, S.** (2006). The capacity region of the Gaussian multiple-input multiple-output broadcast channel. *IEEE Transactions on Information Theory*, 52(9), 3936–3964.
