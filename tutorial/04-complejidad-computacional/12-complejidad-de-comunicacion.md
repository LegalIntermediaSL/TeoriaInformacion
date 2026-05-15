# Complejidad de comunicación

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)

## Objetivos de aprendizaje

1. Definir el modelo Alice-Bob y la complejidad de comunicación D(f).
2. Demostrar el lower bound de igualdad Ω(n) con el argumento de rango.
3. Conectar la complejidad de comunicación con lower bounds de circuitos.


## Intuición

Dos jugadores, Alicia y Bob, tienen entradas $x$ e $y$ respectivamente. Quieren calcular conjuntamente una función $f(x, y)$ intercambiando la menor cantidad posible de bits. La **complejidad de comunicación** estudia cuántos bits necesitan intercambiar en el peor caso, independientemente del poder computacional de cada uno. El modelo es sorprendentemente rico: permite demostrar cotas inferiores para circuitos, memoria de computadores y complejidad espacial que serían muy difíciles de obtener de otro modo.

## El modelo básico

**Protocolo de dos partes:**
- Alicia tiene $x \in \mathcal{X}$, Bob tiene $y \in \mathcal{Y}$.
- Se alternan enviando bits según una función determinista de su entrada y lo que han recibido hasta el momento.
- Al final, alguna de las partes (o ambas) conoce $f(x, y)$.

La **complejidad de comunicación determinista** $D(f)$ es el número de bits transmitidos en el peor caso por el mejor protocolo:

$$D(f) = \min_{\text{protocolo } P} \max_{x, y} \text{bits}(P, x, y)$$

## Matrices de comunicación y rectángulos

Representamos $f: \mathcal{X} \times \mathcal{Y} \to \{0,1\}$ como una matriz $M_f$ con $M_f[x][y] = f(x,y)$.

Un **rectángulo combinatorio** es un subconjunto $R = A \times B \subseteq \mathcal{X} \times \mathcal{Y}$. Los rectángulos son los bloques indivisibles de la comunicación: en un nodo hoja del árbol de comunicación, el conjunto de $(x,y)$ que llegaron a ese nodo es siempre un rectángulo.

**Lema.** En cualquier protocolo determinista de $c$ bits, el árbol de comunicación tiene a lo sumo $2^c$ hojas, y cada hoja corresponde a un rectángulo monócromo (todos 0 o todos 1).

**Corolario.** $D(f) \geq \log_2 C(f)$, donde $C(f)$ es el número mínimo de rectángulos monocromos que recubren la matriz.

## El problema de igualdad (EQ)

El problema de igualdad: $\text{EQ}_n(x, y) = 1$ si y solo si $x = y$, para $x, y \in \{0,1\}^n$.

**Cotas:**
- $D(\text{EQ}_n) \leq n + 1$ bits: Alicia envía $x$, Bob compara.
- $D(\text{EQ}_n) \geq n + 1$ bits: la demostración usa que la matriz de EQ es la identidad $n \times n$, que requiere $2^n$ rectángulos monocromos.

**Protocolo aleatorizado:** con errores tolerados hasta $1/3$, el protocolo de hashing de Freivalds usa solo $O(\log n)$ bits:
1. Bob elige primo aleatorio $p \approx n^2$.
2. Bob envía $y \mod p$ a Alicia.
3. Alicia verifica si $x \mod p$ coincide.

Si $x = y$, siempre correcto. Si $x \neq y$, la probabilidad de error es $O(1/n)$.

## Métodos para cotas inferiores

### El rango (rank lower bound)

**Lema del rango.** $D(f) \geq \log_2 \text{rank}(M_f)$ donde el rango es sobre $\mathbb{R}$.

Para EQ: la matriz es la identidad, rango $= 2^n$, cota inferior $= n$.

El rango sobre $\mathbb{F}_2$ da la cota para protocolos de paridad.

### El método de la cubierta (covering bound)

$D(f) \geq \log_2 C(f)$ donde $C(f)$ es el número mínimo de rectángulos monocromos que cubren $M_f$.

### El método de discrepancia

La **discrepancia** de $f$ respecto a una distribución $\mu$ sobre $\mathcal{X} \times \mathcal{Y}$ es:

$$\text{disc}_\mu(f) = \max_{R \text{ rectángulo}} \left|\mu(R \cap f^{-1}(1)) - \mu(R \cap f^{-1}(0))\right|$$

**Lema.** $R^{1/3}(f) \geq \frac{1}{2} \log_2 \frac{1}{\text{disc}_\mu(f)}$ para todo $\mu$, donde $R^{1/3}$ es la complejidad aleatoria con error $\leq 1/3$.

La discrepancia pequeña implica alta complejidad de comunicación. Se usa para demostrar cotas para IP (producto interno modular 2).

## El problema del producto interno (IP)

$\text{IP}_n(x, y) = \langle x, y \rangle \mod 2 = \sum_i x_i y_i \mod 2$.

**Teorema.** $R^{1/3}(\text{IP}_n) = \Theta(n)$.

Demostración de cota inferior: la discrepancia de IP con distribución uniforme es $2^{-n/2}$, que da $R^{1/3} \geq n/2$.

Cota superior: $O(n)$ bits obviamente basta. IP es "dura" incluso para protocolos aleatorios.

## Complejidad de comunicación multipartita

**Modelo número en frente (number-in-hand):** $k$ jugadores $P_1, \ldots, P_k$ tienen entradas $x_1, \ldots, x_k$. Todos los mensajes son públicos (pizarra compartida). La complejidad de comunicación es el número total de bits escritos.

**Modelo número en cabeza (number-on-forehead):** el jugador $P_i$ ve todas las entradas **excepto** $x_i$. Este modelo está relacionado con circuitos de profundidad constante (AC⁰): cotas inferiores en complejidad de comunicación con cabeza implican cotas de circuitos.

## Aplicaciones a circuitos y espacio

### Cotas de circuitos (AC⁰)

Razborov (1987) y Smolensky (1987) usaron variantes de argumentos de comunicación para demostrar que la función mayoría requiere circuitos de AC⁰ exponencialmente grandes. Hastad demostró en 1988 que la paridad requiere profundidad $\Omega(\log n / \log \log n)$ en AC⁰.

### Complejidad espacial (PSPACE)

**Teorema de Lund et al.** IP = PSPACE. La demostración usa protocolos de comunicación interactivos (verificadores) que permiten verificar en $O(n)$ rondas y espacio polinomial cosas que parecerían requerir exponencial.

### Complejidad de streaming

En el modelo de **streaming** un algoritmo procesa una secuencia de datos con memoria limitada. Muchas cotas inferiores de memoria en streaming se demuestran reduciendo el problema a un problema de comunicación de dos partes.

## Ideas clave

1. La complejidad de comunicación mide los bits intercambiados para calcular $f(x,y)$ en el peor caso.
2. La matriz $M_f$ y sus rectángulos monocromos son la estructura fundamental del análisis.
3. Métodos de cota inferior: rango, cubierta, discrepancia.
4. El problema EQ requiere $\Omega(n)$ bits deterministas pero solo $O(\log n)$ aleatorios.
5. Las cotas de comunicación implican cotas de circuitos, espacio y streaming.

## Ejercicios

1. Calcula el rango sobre $\mathbb{R}$ de la matriz $M_{\text{AND}_n}$ donde $\text{AND}_n(x,y) = x \wedge y$ para $x,y \in \{0,1\}$. ¿Qué cota inferior da para $D(\text{AND}_n)$?

2. Diseña un protocolo de comunicación de $\lceil \log_2 n \rceil + 1$ bits para calcular $\text{GT}_n(x,y) = [x > y]$ (mayor-que) con entradas de $n$ bits.

3. ¿Por qué el protocolo de hashing para EQ requiere que $p$ sea mucho mayor que $x$ e $y$? ¿Qué pasa si $p$ es demasiado pequeño?

4. Demuestra que $D(f) \leq \min(|\mathcal{X}|, |\mathcal{Y}|) + 1$ para cualquier función $f$.

## Véase también

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)



<!-- nav-start -->

---
← [#P y problemas de conteo](11-sharp-p-y-conteo.md) · [Hipótesis ETH y SETH: complejidad de grano fino](13-eth-seth-consecuencias.md) →

<!-- nav-end -->
## Referencias

- Kushilevitz, E. y Nisan, N. (1997). *Communication Complexity*. Cambridge University Press.
- Razborov, A.A. (1992). On the distributional complexity of disjointness. *Theoretical Computer Science*, 106(2), 385–390.
- Raz, R. (1992). On the complexity of matrix product. *Proc. STOC*, 144–151.
- Arora, S. y Barak, B. (2009). *Computational Complexity*, cap. 13. Cambridge.
