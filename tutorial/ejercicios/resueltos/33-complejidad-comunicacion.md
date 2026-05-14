# 33 - Complejidad de comunicación

## Contexto

Este ejercicio acompaña el artículo
[Complejidad de comunicación](../../04-complejidad-computacional/12-complejidad-de-comunicacion.md).

## Enunciado

**Parte A — Modelo básico:**

Alice tiene $x \in \{0,1\}^n$ y Bob tiene $y \in \{0,1\}^n$. Ambos quieren computar $f(x,y)$ intercambiando la mínima cantidad de bits.

1. Define la complejidad de comunicación determinista $D(f)$. ¿Qué son las **matrices de comunicación** y las **monocromáticas**?
2. Calcula $D(\text{EQ}_n)$ donde $\text{EQ}_n(x,y) = [x = y]$. Demuestra el lower bound.
3. Calcula $D(\text{IP}_n)$ donde $\text{IP}_n(x,y) = \langle x,y \rangle \pmod 2$ (producto interior mod 2).

**Parte B — Complejidad de comunicación aleatoria:**

4. Define $R(f)$ (complejidad aleatoria con error $\leq 1/3$). ¿Cuánto vale $R(\text{EQ}_n)$?
5. Describe el protocolo de igualdad aleatorio que usa hashing. ¿Por qué funciona?

**Parte C — Aplicaciones a lower bounds:**

6. Explica cómo la complejidad de comunicación implica lower bounds sobre el espacio de algoritmos de streaming. ¿Qué dice el lower bound de Igualdad para streaming?

## Pista

**Lower bound EQ:** considera la matriz de comunicación de $2^n \times 2^n$. Para una función sin columnas duplicadas, $D(f) \geq \log_2 n$ por un argumento de rectángulos.

**Hashing:** Alice elige un polinomio aleatorio $p$ de grado $d$ sobre $\mathbb{F}_q$ y envía $p(x)$; Bob verifica si $p(y) = p(x)$.

**Streaming:** un protocolo de comunicación de $k$ bits implica un algoritmo de streaming con $O(k)$ bits de espacio.

## Solución

### Parte A — Modelo básico

#### 1. Definición y matrices de comunicación

La **complejidad de comunicación determinista** $D(f)$ es el número de bits intercambiados en el peor caso por el protocolo determinista óptimo que computa $f$.

La **matriz de comunicación** $M_f$ tiene filas indexadas por $x \in \{0,1\}^n$, columnas por $y \in \{0,1\}^n$, y la entrada $M_f[x][y] = f(x,y)$.

Un **rectángulo monocromático** es un subconjunto $A \times B$ (con $A \subseteq \{0,1\}^n$, $B \subseteq \{0,1\}^n$) tal que $f(x,y)$ es constante para todo $(x,y) \in A \times B$.

Cada protocolo determinista de $k$ bits particiona la matriz en $2^k$ rectángulos monocromáticos. Por tanto $D(f) \geq \log_2(\text{número de rectángulos mínimo para cubrir } M_f)$.

#### 2. $D(\text{EQ}_n)$

**Cota superior:** Alice envía $x$ (n bits); Bob compara con $y$ y envía 1 bit. Total: $n+1$ bits. Pero se puede hacer mejor: Alice envía $x$ completo, Bob responde con 1 bit. $D(\text{EQ}_n) \leq n+1$.

**Lower bound:** La matriz $M_{\text{EQ}}$ tiene 1 en la diagonal y 0 fuera. Cualquier rectángulo monocromático de valor 1 solo puede contener entradas de la diagonal, es decir, tiene tamaño $|A \times B|$ con $A = B = \{z\}$ (un solo elemento). Por tanto se necesitan al menos $2^n$ rectángulos, lo que implica $D(\text{EQ}_n) \geq n$.

$$D(\text{EQ}_n) = \Theta(n)$$

#### 3. $D(\text{IP}_n)$

El producto interior $\langle x,y\rangle = \bigoplus_i x_i y_i$ tiene matriz de comunicación con exactamente $2^{n-1}$ unos y $2^{n-1}$ ceros distribuidos sin estructura de rectángulos grandes.

Se puede demostrar que $D(\text{IP}_n) = n$ usando el rango sobre $\mathbb{F}_2$: la matriz $M_{\text{IP}}$ tiene rango $n$ sobre $\mathbb{F}_2$ (es la matriz de Hadamard escalada), lo que implica $D(\text{IP}_n) \geq \log_2(\text{rk}_{\mathbb{F}_2} M) = n$.

### Parte B — Complejidad aleatoria

#### 4. $R(\text{EQ}_n) = O(\log n)$

La complejidad aleatoria con error $\leq 1/3$ de EQ es $R(\text{EQ}_n) = O(\log n)$ bits, mucho mejor que el $\Theta(n)$ determinista.

#### 5. Protocolo de hashing para igualdad

**Protocolo (Freivalds-style):**
1. Alice elige un primo aleatorio $p$ de $\{2, 3, \ldots, n^2\}$ y calcula $x \bmod p$.
2. Alice envía $p$ (en $O(\log n)$ bits) y $x \bmod p$ (en $O(\log n)$ bits).
3. Bob calcula $y \bmod p$ y acepta si coincide con el valor recibido.

**Análisis:**
- Si $x = y$: $x \equiv y \pmod{p}$ siempre. Bob siempre acepta (sin error).
- Si $x \neq y$: $|x - y| \leq 2^n$. El número de primos $p$ que dividen $x-y$ es $\leq n$ (por el teorema fundamental de la aritmética). El número de primos en $[2, n^2]$ es $\Theta(n^2/\log n)$. La probabilidad de error es $\leq n / \Theta(n^2/\log n) = O(\log n / n) \to 0$.

Total de bits: $O(\log n)$. El error puede amplificarse para reducirlo a $\leq 1/3$ repitiendo $O(1)$ veces.

### Parte C — Aplicaciones a streaming

#### 6. Lower bound para streaming

**Reducción de comunicación a streaming:** si existe un algoritmo de streaming para $f(x,y)$ que usa $s$ bits de espacio, se puede construir un protocolo de comunicación de $2s$ bits: Alice simula el streaming sobre $x$ y envía el estado de $s$ bits a Bob, quien continúa el streaming sobre $y$ y devuelve el resultado (1 bit).

**Lower bound de igualdad:** como $D(\text{EQ}_n) = \Omega(n)$ y $R(\text{EQ}_n) = \Omega(\log n)$, cualquier algoritmo de streaming que decida si dos flujos de datos son iguales necesita $\Omega(n)$ bits de espacio (determinista) o $\Omega(\log n)$ bits (aleatorio).

**Aplicación concreta:** el problema de "¿tienen dos flujos de datos la misma distribución de frecuencias?" requiere $\Omega(\sqrt{n})$ bits de espacio en el modelo de streaming, derivado de reducciones de comunicación (problema de índice). Esto explica por qué los estimadores de frecuencias como Count-Min Sketch o el sketch de AMS son óptimos en espacio para sus tareas.
