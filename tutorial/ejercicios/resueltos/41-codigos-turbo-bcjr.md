# Ejercicio resuelto: Códigos Turbo y algoritmo BCJR

**Módulo:** 02 — Teoría de la información  
**Artículo de referencia:** [Códigos Turbo y el Algoritmo BCJR](../../02-teoria-informacion/19-codigos-turbo.md)  
**Dificultad:** ⭐⭐⭐

---

## Problema

**(a)** Un RSC de tasa 1/2 con polinomios generadores $(g_1, g_2) = (5, 7)$ en octal tiene memoria $\nu = 2$ y estados $\left\lbrace 00, 01, 10, 11 \right\rbrace$. Para la secuencia de entrada $u = (1, 0, 1)$ con estado inicial $S_0 = 00$, trazar el treillis completo: listar todos los estados visitados y los bits de paridad producidos. ¿Cuántos estados tiene el treillis? ¿Cuántas transiciones?

**(b)** BCJR simplificado: dado un código convolucional de memoria 1 con polinomios $(1,\; 1+D)$, que tiene 2 estados $\left\lbrace 0, 1 \right\rbrace$, calcular las variables $\alpha_1$, $\alpha_2$ y $\beta_1$, $\beta_2$ para una secuencia de 2 bits recibida $y = (+0.8,\; -0.3)$ en un canal AWGN con $L_c = 2$. Usar inicialización $\alpha_0(0) = 1$, $\alpha_0(1) = 0$. Mostrar el LLR a posteriori $L(u_1)$.

**(c)** Información extrínseca: en la primera iteración del decodificador turbo, BCJR₁ produce $L(u) = (+1.2,\; -0.8,\; +2.1)$ y la información del canal es $L_c \cdot y = (+0.6,\; -0.4,\; +0.9)$. Calcular la información extrínseca $L_e$ para cada bit y explicar por qué $L_e(u_2)$ puede tener signo opuesto a $L_c \cdot y_2$.

**(d)** Puncturing en LTE: un turbo code de tasa 1/3 con $K = 100$ bits de información produce 300 bits ($100$ sistemáticos $+$ $100$ paridades RSC₁ $+$ $100$ paridades RSC₂). Para llegar a tasa 1/2 se eliminan 100 bits de paridad. Proponer un patrón de puncturing equilibrado entre RSC₁ y RSC₂ y calcular la tasa exacta resultante.

---

## Solución

### Parte (a): Treillis del RSC (5, 7)

Los polinomios $(5, 7)$ en octal corresponden a $g_1 = 101_2 = 1 + D^2$ y $g_2 = 111_2 = 1 + D + D^2$. El codificador es sistemático recursivo con la relación:

$$p_k = u_k \oplus s_{k-1} \oplus s_{k-2}$$

donde el estado en el instante $k$ es $(s_{k-1}, s_{k-2})$ — los contenidos de los dos registros de desplazamiento.

**Convención de estado:** el estado $S_k = (r_1, r_2)$ representa los valores almacenados en los dos registros *tras* procesar $u_k$. Tras introducir $u_k$, el nuevo estado es $S_k = (u_k \oplus r_2^{\text{ant}},\; r_1^{\text{ant}})$ (realimentación desde la salida del sumador XOR a la entrada del primer registro).

Para el RSC con realimentación $g_1 = 1 + D^2$, la entrada efectiva al registro es $v_k = u_k \oplus s_{k-2}$, y el estado nuevo es $(v_k, s_{k-1}^{\text{ant}})$.

**Evolución paso a paso** con estado inicial $S_0 = (00)$:

**Paso 1: $u_1 = 1$, estado actual $S_0 = (r_1, r_2) = (0, 0)$**

$$v_1 = u_1 \oplus r_2 = 1 \oplus 0 = 1$$

$$S_1 = (v_1,\; r_1) = (1, 0)$$

$$p_1 = v_1 \oplus r_1 \oplus r_2 = 1 \oplus 0 \oplus 0 = 1$$

Transición: $00 \xrightarrow{u=1} 10$, paridad $p_1 = 1$, salida $(s_1, p_1) = (1, 1)$.

**Paso 2: $u_2 = 0$, estado actual $S_1 = (r_1, r_2) = (1, 0)$**

$$v_2 = u_2 \oplus r_2 = 0 \oplus 0 = 0$$

$$S_2 = (v_2,\; r_1) = (0, 1)$$

$$p_2 = v_2 \oplus r_1 \oplus r_2 = 0 \oplus 1 \oplus 0 = 1$$

Transición: $10 \xrightarrow{u=0} 01$, paridad $p_2 = 1$, salida $(s_2, p_2) = (0, 1)$.

**Paso 3: $u_3 = 1$, estado actual $S_2 = (r_1, r_2) = (0, 1)$**

$$v_3 = u_3 \oplus r_2 = 1 \oplus 1 = 0$$

$$S_3 = (v_3,\; r_1) = (0, 0)$$

$$p_3 = v_3 \oplus r_1 \oplus r_2 = 0 \oplus 0 \oplus 1 = 1$$

Transición: $01 \xrightarrow{u=1} 00$, paridad $p_3 = 1$, salida $(s_3, p_3) = (1, 1)$.

**Resumen del treillis:**

| Instante | Estado anterior | $u_k$ | $p_k$ | Estado siguiente |
|----------|----------------|--------|--------|-----------------|
| $k=1$    | $00$           | $1$    | $1$    | $10$            |
| $k=2$    | $10$           | $0$    | $1$    | $01$            |
| $k=3$    | $01$           | $1$    | $1$    | $00$            |

La palabra de paridad producida es $\mathbf{p} = (1, 1, 1)$.

**Conteo del treillis completo** para $K = 3$ y $\nu = 2$:

- **Número de estados:** $2^\nu = 4$ estados posibles en cada columna, con $K + 1 = 4$ columnas (instantes $k = 0, 1, 2, 3$): **4 estados por columna, 16 nodos totales**.
- **Número de transiciones:** en cada instante hay a lo sumo $2^\nu \times 2 = 8$ transiciones (cada estado puede recibir $u \in \left\lbrace 0, 1 \right\rbrace$). Para $K = 3$ instantes: **hasta 24 transiciones** (en el treillis completo sin restricciones de inicio/fin). Con la restricción de estado inicial fijo en $S_0 = 00$, solo las transiciones alcanzables desde $00$ son activas: en este treillis de 3 pasos, los estados alcanzables desde $00$ son $\left\lbrace 10, 00 \right\rbrace$ en $k=1$, luego $\left\lbrace 01, 11, 00, 10 \right\rbrace$ en $k=2$, por lo que el treillis tiene **6 transiciones activas** en los 3 pasos (2 desde el estado $k=0$, 4 desde los 2 estados en $k=1$, y expandiéndose progresivamente).

Para el treillis completo (sin restricción de estado final), con los 4 estados activos y 2 ramas por estado: **$K \times 2^\nu \times 2 / 2 = 3 \times 8 = 24$ transiciones** en total si todos los estados estuviesen activos en cada columna.

---

### Parte (b): BCJR simplificado con 2 estados

El código tiene memoria 1, polinomios $(1,\; 1+D)$, y 2 estados $\left\lbrace 0, 1 \right\rbrace$. La tabla de transiciones es:

| Estado $s$ | $u_k$ | Paridad $p_k$ | Estado siguiente $s'$ |
|-----------|--------|--------------|----------------------|
| $0$       | $0$    | $0$          | $0$                  |
| $0$       | $1$    | $1$          | $1$                  |
| $1$       | $0$    | $1$          | $0$                  |
| $1$       | $1$    | $0$          | $1$                  |

**Canal AWGN y gamma:** Para un canal AWGN con $L_c = 2$ y símbolo recibido $y_k$, la verosimilitud del canal para el par transmitido $(s_k, p_k)$ usando modulación BPSK $(\pm 1)$ es:

$$\gamma_k(s \to s') \propto \exp\!\left(\frac{L_c}{2}\bigl[(2u_k - 1)\,y_k^{(s)} + (2p_k - 1)\,y_k^{(p)}\bigr]\right)$$

Para simplificar, con información a priori uniforme ($L_a = 0$) y tomando solo el bit sistemático recibido $y_k$ (ignorando la paridad por brevedad en este ejemplo de 2 estados):

$$\gamma_k(s \to s') = \exp\!\left(\frac{L_c}{2}(2u_k - 1)\,y_k\right)$$

Con $L_c = 2$: $\gamma_k = \exp((2u_k - 1)\,y_k)$.

**Paso forward — $\alpha$:**

Inicialización: $\alpha_0(0) = 1$, $\alpha_0(1) = 0$.

Para $k = 1$, $y_1 = +0.8$:

$$\gamma_1(0 \to 0) = e^{(2 \cdot 0 - 1)(+0.8)} = e^{-0.8} \approx 0.449$$

$$\gamma_1(0 \to 1) = e^{(2 \cdot 1 - 1)(+0.8)} = e^{+0.8} \approx 2.225$$

$$\gamma_1(1 \to 0) = e^{(2 \cdot 1 - 1)(+0.8)} = e^{+0.8} \approx 2.225 \quad (u=0 \text{ conduce a } s'=0 \text{ desde } s=1)$$

Recalculando según la tabla: desde $s=1$, $u=0$ lleva a $s'=0$, así que $\gamma_1(1\to 0) = e^{-0.8} \approx 0.449$.

$$\alpha_1(0) = \alpha_0(0)\cdot\gamma_1(0\to 0) + \alpha_0(1)\cdot\gamma_1(1\to 0) = 1 \cdot e^{-0.8} + 0 \cdot e^{-0.8} = e^{-0.8} \approx 0.449$$

$$\alpha_1(1) = \alpha_0(0)\cdot\gamma_1(0\to 1) + \alpha_0(1)\cdot\gamma_1(1\to 1) = 1 \cdot e^{+0.8} + 0 = e^{+0.8} \approx 2.225$$

Para $k = 2$, $y_2 = -0.3$:

$$\gamma_2(0 \to 0) = e^{-(-0.3)} = e^{+0.3} \approx 1.350 \quad (u=0)$$

$$\gamma_2(0 \to 1) = e^{+(-0.3)} = e^{-0.3} \approx 0.741 \quad (u=1)$$

$$\gamma_2(1 \to 0) = e^{+(-0.3)} = e^{-0.3} \approx 0.741 \quad (u=0 \text{ desde } s=1)$$

$$\gamma_2(1 \to 1) = e^{-(-0.3)} = e^{+0.3} \approx 1.350 \quad (u=1 \text{ desde } s=1)$$

$$\alpha_2(0) = \alpha_1(0)\cdot e^{+0.3} + \alpha_1(1)\cdot e^{-0.3} = e^{-0.8}\cdot e^{+0.3} + e^{+0.8}\cdot e^{-0.3} = e^{-0.5} + e^{+0.5} \approx 0.607 + 1.649 = 2.256$$

$$\alpha_2(1) = \alpha_1(0)\cdot e^{-0.3} + \alpha_1(1)\cdot e^{+0.3} = e^{-0.8}\cdot e^{-0.3} + e^{+0.8}\cdot e^{+0.3} = e^{-1.1} + e^{+1.1} \approx 0.333 + 3.004 = 3.337$$

**Paso backward — $\beta$:**

Con terminación libre (no hay restricción de estado final), se inicializa $\beta_2(0) = \beta_2(1) = 1$.

$$\beta_1(0) = \beta_2(0)\cdot\gamma_2(0\to 0) + \beta_2(1)\cdot\gamma_2(0\to 1) = 1\cdot e^{+0.3} + 1\cdot e^{-0.3} = e^{+0.3} + e^{-0.3} \approx 1.350 + 0.741 = 2.091$$

$$\beta_1(1) = \beta_2(0)\cdot\gamma_2(1\to 0) + \beta_2(1)\cdot\gamma_2(1\to 1) = 1\cdot e^{-0.3} + 1\cdot e^{+0.3} = e^{-0.3} + e^{+0.3} \approx 0.741 + 1.350 = 2.091$$

**LLR a posteriori $L(u_1)$:**

$$L(u_1) = \log\frac{P(u_1=0 \mid \mathbf{y})}{P(u_1=1 \mid \mathbf{y})} = \log\frac{\displaystyle\sum_{(s\to s'): u=0} \alpha_0(s)\cdot\gamma_1(s,s')\cdot\beta_1(s')}{\displaystyle\sum_{(s\to s'): u=1} \alpha_0(s)\cdot\gamma_1(s,s')\cdot\beta_1(s')}$$

Transiciones con $u_1 = 0$: solo $(0 \to 0)$, pues $\alpha_0(1) = 0$.

$$\text{Numerador} = \alpha_0(0)\cdot\gamma_1(0\to 0)\cdot\beta_1(0) = 1\cdot e^{-0.8}\cdot 2.091 \approx 0.449 \times 2.091 \approx 0.939$$

Transiciones con $u_1 = 1$: solo $(0 \to 1)$.

$$\text{Denominador} = \alpha_0(0)\cdot\gamma_1(0\to 1)\cdot\beta_1(1) = 1\cdot e^{+0.8}\cdot 2.091 \approx 2.225 \times 2.091 \approx 4.652$$

$$\boxed{L(u_1) = \log\frac{0.939}{4.652} \approx \log(0.202) \approx -1.60}$$

El signo negativo indica que el decodificador favorece $u_1 = 1$ (con la convención de que $L < 0$ implica que el bit 1 es más probable), lo que es coherente con $y_1 = +0.8 > 0$, que corresponde a la transmisión de un $+1$ en BPSK, es decir, $u_1 = 1$.

---

### Parte (c): Información extrínseca

La descomposición del LLR a posteriori es:

$$L(u_k) = L_c \cdot y_k + L_a(u_k) + L_e(u_k)$$

En la primera iteración, la información a priori es nula ($L_a = 0$), por lo que:

$$L_e(u_k) = L(u_k) - L_c \cdot y_k$$

Con los valores dados:

| Bit | $L(u_k)$ | $L_c \cdot y_k$ | $L_e(u_k) = L(u_k) - L_c \cdot y_k$ |
|-----|----------|-----------------|--------------------------------------|
| $u_1$ | $+1.2$ | $+0.6$ | $+1.2 - 0.6 = +0.6$ |
| $u_2$ | $-0.8$ | $-0.4$ | $-0.8 - (-0.4) = -0.4$ |
| $u_3$ | $+2.1$ | $+0.9$ | $+2.1 - 0.9 = +1.2$ |

**¿Por qué $L_e(u_2)$ puede tener signo opuesto a $L_c \cdot y_2$?**

En este caso ambos son negativos, así que no hay inversión de signo. Sin embargo, en general, la información extrínseca puede tener signo opuesto al del canal por la siguiente razón:

$L_c \cdot y_2$ refleja únicamente la evidencia local del bit $u_2$ en el canal: qué tan probable es haber recibido $y_2$ si se envió $+1$ frente a $-1$. En cambio, $L_e(u_2)$ captura la evidencia sobre $u_2$ que proviene de los *otros* bits a través de las restricciones del código (las transiciones del treillis). El código RSC impone restricciones entre bits consecutivos: si los vecinos $u_1$ y $u_3$ tienen paridades que son más coherentes con $u_2 = 0$ que con $u_2 = 1$, entonces $L_e(u_2) > 0$ incluso si $y_2$ apunta a $u_2 = 1$.

En un caso extremo, si $y_2$ está cerca de cero (canal muy ruidoso en ese símbolo) pero la paridad del código exige fuertemente que $u_2 = 0$ dado el contexto de bits adyacentes, entonces $L_e(u_2) > 0$ y $L_c \cdot y_2 < 0$: la información contextual del código supera la débil evidencia local del canal.

Esta es precisamente la razón de ser de la decodificación iterativa: cada BCJR aporta la perspectiva contextual de su propio código, y la información extrínseca que se intercambia entre los dos decodificadores es la ganancia de cada uno sobre la información local del canal.

---

### Parte (d): Puncturing equilibrado en LTE

**Situación inicial:** tasa $R = 1/3$, bloque de $K = 100$ bits.

- 100 bits sistemáticos (nunca se punctúan: llevan la información)
- 100 bits de paridad RSC₁: $\mathbf{p}^{(1)} = (p_1^{(1)}, p_2^{(1)}, \ldots, p_{100}^{(1)})$
- 100 bits de paridad RSC₂: $\mathbf{p}^{(2)} = (p_1^{(2)}, p_2^{(2)}, \ldots, p_{100}^{(2)})$

Total transmitido: 300 bits. Para alcanzar tasa $R = 1/2$ con la misma cantidad de información ($K = 100$ bits), el número de bits transmitidos debe ser:

$$N_{\text{trans}} = \frac{K}{R} = \frac{100}{1/2} = 200 \text{ bits}$$

Por tanto hay que eliminar $300 - 200 = 100$ bits de paridad.

**Patrón de puncturing equilibrado:** se eliminan 50 bits de RSC₁ y 50 bits de RSC₂, intercalando las posiciones para maximizar la separación entre bits conservados. Un patrón estándar es:

- **RSC₁:** conservar los bits en posiciones impares: $p_1^{(1)}, p_3^{(1)}, p_5^{(1)}, \ldots, p_{99}^{(1)}$ (50 bits). Puncturar: $p_2^{(1)}, p_4^{(1)}, \ldots, p_{100}^{(1)}$.
- **RSC₂:** conservar los bits en posiciones pares: $p_2^{(2)}, p_4^{(2)}, p_6^{(2)}, \ldots, p_{100}^{(2)}$ (50 bits). Puncturar: $p_1^{(2)}, p_3^{(2)}, \ldots, p_{99}^{(2)}$.

En notación de máscara de puncturing (1 = transmitido, 0 = eliminado), repitiendo el patrón de periodo 2:

$$\text{RSC}_1: \left\lbrace 1, 0, 1, 0, \ldots \right\rbrace \quad \text{RSC}_2: \left\lbrace 0, 1, 0, 1, \ldots \right\rbrace$$

Este patrón es **complementario**: para cada posición $k$, exactamente una de las dos paridades se transmite, lo que garantiza que en cada instante temporal el receptor recibe información de al menos uno de los dos codificadores.

**Verificación de la tasa resultante:**

$$\text{Bits transmitidos} = 100 \text{ (sistemáticos)} + 50 \text{ (paridades RSC}_1\text{)} + 50 \text{ (paridades RSC}_2\text{)} = 200 \text{ bits}$$

$$R = \frac{K}{N_{\text{trans}}} = \frac{100}{200} = \frac{1}{2}$$

La tasa exacta resultante es $R = 1/2$.

**Por qué el patrón equilibrado importa:** si se eliminasen todos los bits de una sola componente (p. ej., todos los de RSC₂), el decodificador de RSC₂ no tendría información propia de canal; solo podría usar la información extrínseca de RSC₁, degradando la convergencia iterativa. El patrón complementario garantiza que ambos BCJR tienen evidencia directa del canal para la mitad de los instantes, manteniendo el equilibrio de la decodificación iterativa.

---

## Ideas clave del ejercicio

1. El treillis de un RSC $(5,7)$ con $\nu = 2$ tiene $2^\nu = 4$ estados; para $K$ bits de entrada tiene $K$ columnas de transiciones y $K \times 2^\nu \times 2 / 2$ transiciones totales si todos los estados están activos.
2. El algoritmo BCJR combina las variables forward $\alpha$ (que acumulan evidencia pasada) y backward $\beta$ (que acumulan evidencia futura) para calcular el LLR exacto de cada bit; el producto $\alpha_{k-1}(s) \cdot \gamma_k(s,s') \cdot \beta_k(s')$ integra toda la observación.
3. La información extrínseca $L_e(u_k) = L(u_k) - L_c \cdot y_k - L_a(u_k)$ es la ganancia contextual del código: lo que el decodificador aprende de $u_k$ a través de los bits vecinos y las restricciones del treillis, excluyendo la evidencia local del canal.
4. $L_e(u_k)$ puede tener signo opuesto a $L_c \cdot y_k$ cuando la información contextual del código supera la evidencia directa del canal para ese símbolo; esto es especialmente frecuente en bits con canal ruidoso y vecinos bien determinados.
5. El puncturing equilibrado entre RSC₁ y RSC₂ (patrón complementario) asegura que ambos decodificadores componentes tengan evidencia directa del canal, preservando el equilibrio y la convergencia de la decodificación iterativa turbo.
