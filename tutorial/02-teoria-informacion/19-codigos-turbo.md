# Códigos Turbo y el Algoritmo BCJR

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~28 min


## Prerrequisitos

- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)
- [Canales discretos y capacidad](04-canales-discretos-y-capacidad.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)

## Objetivos de aprendizaje

1. Entender la estructura de un código turbo: concatenación paralela de dos RSC con entrelazador.
2. Derivar el algoritmo BCJR para decodificación MAP de un código convolucional.
3. Comprender el papel de la información extrínseca y por qué evita el double-counting.
4. Analizar la convergencia de la decodificación iterativa mediante curvas EXIT.


## Intuición

En 1993, Berrou, Glavieux y Thitimajshima presentaron en ICC un código que operaba a solo 0.5 dB de la capacidad de Shannon — un resultado que la comunidad tardó años en aceptar. El truco: dos codificadores convolucionales sencillos, separados por una permutación aleatoria de los bits, que se decodifican de forma iterativa intercambiándose información suave. Cada decodificador mejora su estimación usando lo que el otro ya aprendió, convergiendo iteración tras iteración hacia la solución óptima.

El nombre "turbo" viene de la analogía con el turbocompresor: la salida de un proceso retroalimenta la entrada del otro.

## Códigos convolucionales recursivos sistemáticos (RSC)

Un código turbo usa como componentes dos codificadores **RSC** (*Recursive Systematic Convolutional*). La sistematicidad garantiza que los bits de información aparecen directamente en la salida (facilita la decodificación suave). La recursividad — realimentar la salida de los registros a la entrada — es esencial para que los códigos turbo funcionen: hace que la secuencia codificada tenga memoria infinita, lo que permite que el decodificador MAP aproveche toda la trama.

Un RSC de tasa $1/2$ con polinomios generadores $(g_1, g_2) = (1 + D^2, 1 + D + D^2)$ en notación octal $(5, 7)$:

```
         ┌────────────────────────┐
u_k ──┬──► (+) ──► [D] ──► [D] ──┘
      │    │
      │    └──► (+) ──► p_k
      │
      └──────────────────────────► s_k  (sistemático)
```

La salida es $(s_k, p_k) = (u_k, u_k \oplus s_{k-1} \oplus s_{k-2})$ donde $s_k$ es el bit sistemático y $p_k$ la paridad.

## Estructura del código turbo

Un código turbo de tasa $1/3$ consiste en:

1. **Codificador RSC₁:** recibe los bits de información $\mathbf{u} = (u_1, \ldots, u_K)$ y produce paridades $\mathbf{p}^{(1)}$.
2. **Entrelazador $\Pi$:** permuta $\mathbf{u}$ en orden pseudoaleatorio para producir $\mathbf{u}' = \Pi(\mathbf{u})$.
3. **Codificador RSC₂:** recibe $\mathbf{u}'$ y produce paridades $\mathbf{p}^{(2)}$.

La palabra código transmitida es:

$$\mathbf{c} = \bigl(s_1, p_1^{(1)}, p_1^{(2)},\; s_2, p_2^{(1)}, p_2^{(2)},\; \ldots\bigr)$$

con tasa $R = 1/3$. En la práctica, **puncturing** (eliminar paridades alternadas) permite alcanzar tasas $1/2$, $2/3$, $3/4$.

### Por qué el entrelazador es esencial

Sin entrelazador, los dos RSC ven la misma secuencia y sus errores están correlados — el decodificador iterativo no converge. El entrelazador pseudoaleatorio garantiza que los errores que RSC₂ no puede corregir (palabras de peso bajo bajo la permutación) sean distintos de los que RSC₁ no puede corregir. Esta diversidad permite que la decodificación iterativa elimine los errores residuales de cada etapa.

## El algoritmo BCJR

El algoritmo **BCJR** (Bahl, Cocke, Jelinek, Raviv, 1974) calcula la probabilidad a posteriori exacta de cada bit dado el canal, operando sobre el **treillis** del código convolucional.

### El treillis

Un código convolucional de $\nu$ registros tiene $2^\nu$ estados. El treillis tiene $K+\nu$ columnas (una por bit más las colas de terminación) y $2^\nu$ filas. Cada nodo $(k, s)$ representa el estado $s$ en el instante $k$. Cada transición $(k, s) \to (k+1, s')$ corresponde a enviar el bit $u_k$ y producir la paridad $p_k$.

### Variables forward y backward

BCJR define tres conjuntos de probabilidades:

**Alpha (hacia adelante):** $\alpha_k(s) = P(S_k = s,\; y_1^k)$ — probabilidad de estar en estado $s$ en el instante $k$ habiendo observado $y_1^k$.

**Beta (hacia atrás):** $\beta_k(s) = P(y_{k+1}^K \mid S_k = s)$ — probabilidad de observar el resto de la secuencia dado que estamos en $s$ en el instante $k$.

**Gamma (transición):** para la transición $s \to s'$ que emite $(u_k, p_k)$:

$$\gamma_k(s, s') = P(y_k \mid u_k, p_k) \cdot P(u_k)$$

donde $P(y_k \mid u_k, p_k)$ es la verosimilitud del canal y $P(u_k)$ es la probabilidad a priori del bit.

### Recursiones

$$\alpha_k(s') = \sum_{s} \alpha_{k-1}(s) \cdot \gamma_k(s, s')$$

$$\beta_k(s) = \sum_{s'} \beta_{k+1}(s') \cdot \gamma_{k+1}(s, s')$$

con condiciones de contorno $\alpha_0(0) = 1$, $\alpha_0(s \neq 0) = 0$ (empezamos en el estado cero); $\beta_K(0) = 1$, $\beta_K(s \neq 0) = 0$ (terminamos en el estado cero, si se usa terminación del treillis).

### Probabilidad a posteriori y LLR

La probabilidad a posteriori del bit $u_k = b$ es:

$$P(u_k = b \mid \mathbf{y}) = \frac{1}{Z} \sum_{\substack{(s \to s') \\ u_k(s,s')=b}} \alpha_{k-1}(s) \cdot \gamma_k(s, s') \cdot \beta_k(s')$$

El **log-likelihood ratio** a posteriori (*L-value*):

$$L(u_k) = \log \frac{P(u_k = 0 \mid \mathbf{y})}{P(u_k = 1 \mid \mathbf{y})}$$

En la práctica se trabaja con log-probabilidades para evitar underflow numérico (algoritmo log-MAP o max-log-MAP).

## Información extrínseca y decodificación iterativa

La clave del turbo es descomponer el LLR a posteriori en tres términos:

$$L(u_k) = L_c(y_k) + L_a(u_k) + L_e(u_k)$$

donde:
- $L_c(y_k)$: **información del canal** — LLR del bit sistemático recibido.
- $L_a(u_k)$: **información a priori** — lo que se sabe de $u_k$ antes de observar el canal.
- $L_e(u_k)$: **información extrínseca** — lo que el decodificador aprende de $u_k$ a partir de *los demás bits*, a través de las restricciones del código.

### El protocolo iterativo

En cada iteración $i$:

1. **BCJR₁** recibe $L_c(\mathbf{y})$ y $L_a^{(i)}(\mathbf{u})$ (información extrínseca del turno anterior de BCJR₂, permutada).  
   Produce $L_e^{(i)}(\mathbf{u})$.

2. **Intercambio:** $L_e^{(i)}(\mathbf{u})$ se despermuta con $\Pi^{-1}$ y se convierte en la información a priori para BCJR₂.

3. **BCJR₂** recibe $L_c(\mathbf{y}')$ (canal de las paridades de RSC₂) y $L_a^{(i)}(\mathbf{u}')$.  
   Produce $L_e^{(i)}(\mathbf{u}')$.

4. **Intercambio:** $L_e^{(i)}(\mathbf{u}')$ se permuta con $\Pi$ y se convierte en $L_a^{(i+1)}(\mathbf{u})$ para la siguiente iteración de BCJR₁.

5. Tras un número fijo de iteraciones (típicamente 6–10), se decide $\hat{u}_k = \text{sgn}(L(u_k))$.

**¿Por qué no se pasa la información propia?** Si BCJR₁ incluyera su propia $L_e$ como información a priori para sí mismo, estaría contando dos veces la misma evidencia (*double-counting*), lo que causa divergencia. Solo se pasa la extrínseca del *otro* decodificador.

## Análisis de convergencia: curvas EXIT

Las **curvas EXIT** (*Extrinsic Information Transfer*) son una herramienta para predecir y visualizar la convergencia de la decodificación iterativa sin simular a nivel de bloque.

Se define la **información mutua** entre el LLR extrínseco y el bit verdadero:

$$I_E = I(u_k;\; L_e(u_k))$$

La curva EXIT de un decodificador componente traza $I_E$ en función de $I_A = I(u_k;\; L_a(u_k))$ para un SNR dado.

**Principio:** el turbo decodificador converge si y solo si existe un **túnel** entre las curvas EXIT de los dos componentes — es decir, si la curva de BCJR₁ no corta a la inversa de la curva de BCJR₂.

Esto permite diseñar el entrelazador y los polinomios generadores para maximizar la apertura del túnel, acercándose al límite de Shannon.

## Puncturing y adaptación de tasa

Los códigos turbo se usan en múltiples tasas (3GPP LTE: $1/3$, $1/2$, $2/3$, $3/4$, $5/6$) eliminando paridades según un patrón fijo:

| Tasa | Bits transmitidos por bloque de $K$ bits |
|------|------------------------------------------|
| $1/3$ | $K$ sistemáticos + $K$ paridades RSC₁ + $K$ paridades RSC₂ |
| $1/2$ | $K$ sistemáticos + $K/2$ paridades RSC₁ + $K/2$ paridades RSC₂ |
| $2/3$ | $K$ sistemáticos + $K/4$ paridades de cada RSC |

El receptor conoce el patrón de puncturing e inserta valores nulos ($L = 0$, ni a favor ni en contra) en las posiciones borradas antes del BCJR.

## Rendimiento y usos reales

Los turbo codes se usan en:

- **3G (UMTS/HSPA):** todos los canales de datos usan turbo codes con tasa $1/3$ y puncturing.
- **4G (LTE):** canal de datos (PDSCH, PUSCH) con tamaños de bloque entre 40 y 6144 bits.
- **CCSDS** (comunicaciones espaciales): NASA y ESA para telemetría de misiones profundas.
- **DVB-RCS:** canal de retorno en redes satelitales.

Los turbo codes han sido reemplazados en 5G NR por LDPC (canal de datos) y polares (canal de control), pero siguen activos en 4G y sistemas satelitales.

| Métrica | Turbo (LTE) | LDPC (5G NR) | Polar (5G NR) |
|---------|------------|-------------|--------------|
| Gap a capacidad | ~0.5 dB | ~0.1 dB | → 0 (asint.) |
| Complejidad decodif. | $O(N \cdot I)$ | $O(N \cdot I)$ | $O(N \log N)$ |
| Longitud de bloque | 40–6144 bits | 792–8448 bits | 32–1024 bits |
| Uso en estándar | 3G/4G | 5G datos | 5G control |


## Ideas clave

- Un código turbo es la concatenación paralela de dos RSC conectados por un entrelazador pseudoaleatorio.
- El algoritmo BCJR calcula el LLR a posteriori exacto de cada bit recorriendo el treillis en dos pasadas (forward-backward).
- La información extrínseca es lo que un decodificador aprende de un bit a través de los *demás* bits. Pasarla al otro decodificador (y solo a él) evita el double-counting.
- Las curvas EXIT predicen la convergencia: el turbo converge si hay un túnel entre las curvas de los dos componentes.
- Puncturing adapta la tasa sin cambiar el código base: se eliminan paridades y el receptor inserta LLR = 0 en esas posiciones.

## Ejercicios

1. Para el RSC con polinomios $(5, 7)$ en octal y memoria $\nu = 2$, dibuja el treillis para $K = 4$ bits y estado inicial $S_0 = 00$. ¿Cuántas transiciones tiene?

2. Demuestra que $L(u_k) = L_c(y_k) + L_a(u_k) + L_e(u_k)$ a partir de la definición del LLR a posteriori y la descomposición de $\gamma_k$.

3. Un turbo code de tasa $1/3$ con $K = 1000$ bits se puntúa a tasa $1/2$. ¿Cuántos bits de paridad se eliminan? ¿Cómo se distribuyen entre RSC₁ y RSC₂ para mantener equilibrio?

4. ¿Por qué no funcionaría un turbo code sin entrelazador (usando la misma secuencia $\mathbf{u}$ en ambos RSC)? Razona en términos de distancia mínima del código compuesto.

5. Las curvas EXIT de dos componentes se cruzan a $I_A = 0.6$, $I_E = 0.8$. ¿Convergerá el decodificador iterativo? ¿Qué modificación del diseño podría abrir el túnel?

## Véase también

- [Códigos LDPC y Turbo](11-codigos-ldpc-y-turbo.md)
- [Códigos Polares](17-codigos-polares.md)
- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)
- [Teorema de Shannon y capacidad de canal](08-teorema-de-shannon-capacidad.md)



<!-- nav-start -->

---
← [Canal con Estado: Teorema de Gel'fand-Pinsker](18-canal-con-estado-gelfand-pinsker.md) · [01 - El problema de la parada](../03-computabilidad/01-problema-de-la-parada.md) →

<!-- nav-end -->
## Referencias

- Berrou, C., Glavieux, A. y Thitimajshima, P. (1993). Near Shannon limit error-correcting coding and decoding: Turbo-codes. *IEEE ICC 1993*.
- Bahl, L., Cocke, J., Jelinek, F. y Raviv, J. (1974). Optimal decoding of linear codes for minimizing symbol error rate. *IEEE Trans. Information Theory*, 20(2), 284–287.
- Benedetto, S. y Montorsi, G. (1996). Unveiling turbo codes. *IEEE Trans. Information Theory*, 42(2), 409–428.
- ten Brink, S. (2001). Convergence behavior of iteratively decoded parallel concatenated codes. *IEEE Trans. Communications*, 49(10), 1727–1737.
- Richardson, T. y Urbanke, R. (2008). *Modern Coding Theory*. Cambridge University Press, cap. 6.
- 3GPP TS 36.212 — LTE multiplexing and channel coding (especificación de turbo codes en LTE).
