# 29 - Procesos estocásticos y fuentes con memoria

## Contexto

Este ejercicio acompaña el artículo
[Procesos estocásticos y fuentes con memoria](../../02-teoria-informacion/14-procesos-estocasticos-y-fuentes-con-memoria.md).

## Enunciado

**Parte A — Cadenas de Markov de orden superior:**

Sea una fuente de Markov de orden 2 sobre el alfabeto $\{0, 1\}$ con las siguientes probabilidades de transición:

$$P(X_n = 1 \mid X_{n-1} = 0, X_{n-2} = 0) = 0.1$$
$$P(X_n = 1 \mid X_{n-1} = 1, X_{n-2} = 0) = 0.6$$
$$P(X_n = 1 \mid X_{n-1} = 0, X_{n-2} = 1) = 0.4$$
$$P(X_n = 1 \mid X_{n-1} = 1, X_{n-2} = 1) = 0.9$$

1. Convierte esta fuente de orden 2 en una cadena de Markov de orden 1 sobre el espacio de estados $\{00, 01, 10, 11\}$.
2. Escribe la matriz de transición $P$ del proceso equivalente.

**Parte B — Tasa de entropía:**

3. La distribución estacionaria del proceso equivalente es aproximadamente $\pi = (0.30, 0.20, 0.20, 0.30)$ para los estados $(00, 01, 10, 11)$. Calcula la tasa de entropía $\bar{H}$.
4. Compara $\bar{H}$ con la entropía de la fuente i.i.d. con la misma distribución marginal de 0s y 1s.
5. ¿Qué significa que $\bar{H} < H(X_1)$? ¿Qué lo explica?

## Pista

**Proceso equivalente:** el estado es el par $(X_{n-1}, X_n)$. Las transiciones son deterministas salvo en el último símbolo: desde estado $(a, b)$ solo se puede ir a $(b, 0)$ o $(b, 1)$.

**Tasa de entropía:**
$$\bar{H} = -\sum_i \pi_i \sum_j P_{ij} \log_2 P_{ij}$$

**Distribución marginal:** $P(X=1) = \pi_{01} + \pi_{11}$ (estados que terminan en 1).

## Solución

### Parte A — Proceso equivalente

#### 1. Espacio de estados y transiciones

Los estados son los pares de bits: $\{00, 01, 10, 11\}$.

Las transiciones válidas (solo se puede pasar de $(a,b)$ a $(b, c)$ para algún $c \in \{0,1\}$):

| Desde | Hacia 0 | $P(\cdot\mid\cdot)$ | Hacia 1 | $P(\cdot\mid\cdot)$ |
|-------|---------|---------------------|---------|---------------------|
| 00    | 00      | 0.9                 | 01      | 0.1                 |
| 01    | 10      | 0.4                 | 11      | 0.6                 |
| 10    | 00      | 0.6                 | 01      | 0.4                 |
| 11    | 10      | 0.1                 | 11      | 0.9                 |

#### 2. Matriz de transición

Ordenando los estados como $(00, 01, 10, 11)$:

$$P = \begin{pmatrix} 0.9 & 0.1 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.4 & 0.6 \\ 0.6 & 0.4 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.1 & 0.9 \end{pmatrix}$$

Las entradas nulas corresponden a transiciones imposibles (e.g., de $00$ no se puede ir a $10$ ni $11$).

### Parte B — Tasa de entropía

#### 3. Cálculo de $\bar{H}$

Con $\pi = (0.30, 0.20, 0.20, 0.30)$:

**Contribución del estado 00** ($\pi_{00} = 0.30$):
$$-0.30 \times (0.9 \log_2 0.9 + 0.1 \log_2 0.1) = -0.30 \times (-0.137 - 0.332) = 0.30 \times 0.469 = 0.141$$

**Contribución del estado 01** ($\pi_{01} = 0.20$):
$$-0.20 \times (0.4 \log_2 0.4 + 0.6 \log_2 0.6) = -0.20 \times (-0.529 - 0.442) = 0.20 \times 0.971 = 0.194$$

**Contribución del estado 10** ($\pi_{10} = 0.20$):
$$-0.20 \times (0.6 \log_2 0.6 + 0.4 \log_2 0.4) = 0.20 \times 0.971 = 0.194$$

**Contribución del estado 11** ($\pi_{11} = 0.30$):
$$-0.30 \times (0.1 \log_2 0.1 + 0.9 \log_2 0.9) = 0.30 \times 0.469 = 0.141$$

$$\bar{H} = 0.141 + 0.194 + 0.194 + 0.141 = 0.670 \text{ bits/símbolo}$$

#### 4. Comparación con la fuente i.i.d.

La distribución marginal de 1s:

$$P(X=1) = \pi_{01} + \pi_{11} = 0.20 + 0.30 = 0.50$$

Entropía i.i.d. con $P(X=1) = 0.5$:

$$H(X) = -(0.5 \log_2 0.5 + 0.5 \log_2 0.5) = 1.0 \text{ bit/símbolo}$$

La tasa de entropía es $\bar{H} = 0.670 < H(X) = 1.0$.

#### 5. Interpretación

$\bar{H} < H(X_1)$ porque la fuente tiene **memoria**: el símbolo actual $X_n$ no es independiente de los anteriores. Conocer el contexto $(X_{n-1}, X_{n-2})$ reduce la incertidumbre sobre $X_n$.

En este caso, los estados $00$ y $11$ son "persistentes" (alta probabilidad de repetir el bit), lo que crea dependencia positiva entre símbolos consecutivos. Esta correlación reduce la entropía efectiva por símbolo respecto a la fuente sin memoria.

Formalmente: $\bar{H} = \lim_{n\to\infty} H(X_n \mid X_{n-1}, \ldots, X_1) \leq H(X_1)$, con igualdad solo si la fuente es i.i.d.
