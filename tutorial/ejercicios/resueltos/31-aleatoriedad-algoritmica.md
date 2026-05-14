# 31 - Aleatoriedad algorítmica

## Contexto

Este ejercicio acompaña el artículo
[Aleatoriedad algorítmica](../../03-computabilidad/12-aleatoriedad-algoritmica.md).

## Enunciado

**Parte A — Complejidad de Kolmogorov:**

1. Define la complejidad de Kolmogorov $K(x)$ de una cadena $x$. ¿Por qué $K$ no es computable?
2. Demuestra (por argumento de conteo) que para todo $n$, existen cadenas de longitud $n$ con $K(x) \geq n$.
3. ¿Es posible que $K(x) > |x| + c$ para todo $x$ y alguna constante $c$? ¿Por qué?

**Parte B — Aleatoriedad de Martin-Löf:**

4. Define informalmente qué significa que una cadena infinita $\omega$ sea **aleatoria en el sentido de Martin-Löf**.
5. ¿Cuál es la relación entre la aleatoriedad de Martin-Löf y la incompresibilidad de Kolmogorov para cadenas finitas?
6. Da un ejemplo de secuencia infinita que **no** sea aleatoria según Martin-Löf. Justifica.

**Parte C — El número $\Omega$ de Chaitin:**

7. Define $\Omega = \sum_{p \text{ para}} 2^{-|p|}$ donde la suma es sobre los programas que paran. ¿Por qué $0 < \Omega < 1$?
8. ¿Por qué $\Omega$ es un número bien definido pero no computable?
9. ¿Qué se puede deducir si se conocen los primeros $n$ bits de $\Omega$?

## Pista

**Conteo:** hay $2^n$ cadenas de longitud $n$ pero solo $2^n - 1$ programas de longitud $< n$.

**Martin-Löf:** una secuencia es aleatoria si no pertenece a ningún conjunto de medida cero enumerable (test de Martin-Löf).

**$\Omega$:** cada programa $p$ que para contribuye $2^{-|p|}$; la suma converge porque el conjunto de programas que paran es prefijo-libre y satisface la desigualdad de Kraft.

## Solución

### Parte A — Complejidad de Kolmogorov

#### 1. Definición e incomputabilidad

La **complejidad de Kolmogorov** $K(x)$ es la longitud del programa más corto $p$ (en una UTM fija $U$) tal que $U(p) = x$:

$$K(x) = \min_{p: U(p) = x} |p|$$

**¿Por qué no es computable?** Supón que $K$ fuera computable. Entonces para cualquier $n$, podríamos computar la cadena $x_n$ de longitud $n$ con mayor complejidad. Pero el programa "genera la cadena de longitud $n$ más incompresible" tiene longitud $O(\log n)$ (necesita codificar $n$). Para $n$ grande, esto produce una cadena $x_n$ con $K(x_n) \leq O(\log n) < n$, contradicción. Formalmente se relaciona con la indecidibilidad del problema de la parada.

#### 2. Existencia de cadenas incompresibles

Para todo $n$: hay $2^n$ cadenas de longitud $n$, pero solo $\sum_{k=0}^{n-1} 2^k = 2^n - 1$ programas de longitud $< n$. Por tanto, al menos una cadena de longitud $n$ no puede tener ningún programa de longitud $< n$ que la produzca, lo que implica $K(x) \geq n$.

De hecho, al menos la mitad de las cadenas tienen $K(x) \geq n-1$, y en general la fracción de cadenas con $K(x) < n - c$ es menor que $2^{-c}$.

#### 3. ¿Puede $K(x) > |x| + c$?

No para ningún $x$ y $c$ arbitrario. Para toda cadena $x$ de longitud $n$, existe el programa trivial "imprime $x$" de longitud $n + O(1)$. Por tanto:

$$K(x) \leq |x| + c_0$$

para alguna constante $c_0$ que depende de la UTM (no de $x$). La complejidad no puede ser mucho mayor que la propia longitud de la cadena.

### Parte B — Aleatoriedad de Martin-Löf

#### 4. Definición informal

Una secuencia infinita $\omega \in \{0,1\}^\mathbb{N}$ es **aleatoria en el sentido de Martin-Löf** si no pertenece a ningún "test de aleatoriedad": ningún conjunto de medida cero que sea enumerable en el límite (una intersección de abiertos de medida cada vez más pequeña, de forma efectiva).

Intuitivamente: $\omega$ es aleatoria si no exhibe **ningún patrón estadístico computable**. No hay regularidad que un algoritmo pueda detectar y explotar.

#### 5. Relación con incompresibilidad de Kolmogorov

Para cadenas finitas, la conexión es:

- Una cadena $x$ de longitud $n$ es **incompresible** (en el sentido de Kolmogorov) si $K(x) \geq n - c$ para alguna constante $c$.
- Una secuencia infinita $\omega$ es aleatoria (Martin-Löf) si y solo si sus prefijos $\omega_{1:n}$ son casi todos incompresibles: $K(\omega_{1:n}) \geq n - O(1)$.

Esta equivalencia (teorema de Levin-Chaitin) muestra que la aleatoriedad de Martin-Löf coincide con la incompresibilidad universal a nivel de prefijos.

#### 6. Ejemplo de secuencia no aleatoria

La secuencia $\omega = 010101010101\ldots$ (alternancia infinita) **no es aleatoria** según Martin-Löf:

- Su $n$-ésimo prefijo tiene $K(\omega_{1:n}) \leq O(\log n)$ bits (el programa "genera $\lfloor n/2 \rfloor$ copias de '01'" tiene longitud $O(\log n)$).
- Esto viola la condición $K(\omega_{1:n}) \geq n - O(1)$.
- Formalmente, pertenece al test de Martin-Löf "frecuencia de unos entre 0.4 y 0.6" con medida nula en el espacio de Bernoulli de $p = 0.5$.

Cualquier secuencia periódica o generada por una regla computable fija es no aleatoria.

### Parte C — El número $\Omega$ de Chaitin

#### 7. Definición y acotación

$$\Omega = \sum_{\substack{p \in \{0,1\}^* \\ U(p) \text{ para}}} 2^{-|p|}$$

- $\Omega > 0$: basta con que al menos un programa pare (e.g., el programa vacío si $U(\varepsilon)$ para).
- $\Omega < 1$: el conjunto de programas que paran forma un **código prefijo** (ningún programa que para es prefijo de otro que para, en la UTM de prefijo estándar). Por la desigualdad de Kraft: $\sum_{p \text{ para}} 2^{-|p|} \leq 1$.
- La desigualdad es estricta porque no todos los programas paran.

#### 8. Bien definido pero no computable

$\Omega$ está bien definido porque la serie converge absolutamente (suma de positivos acotada por 1).

No es computable porque para computar $\Omega$ con precisión $2^{-n}$ habría que determinar qué programas de longitud $\leq n$ paran, lo que equivale a resolver el problema de la parada para todos ellos.

Sin embargo, $\Omega$ es **semicomputable desde abajo**: se puede computar una secuencia $\Omega_1 \leq \Omega_2 \leq \ldots \to \Omega$ ejecutando todos los programas en paralelo (dovetailing) y sumando las contribuciones de los que paran. La sucesión converge pero no se puede saber cuándo se ha alcanzado la precisión $\epsilon$.

#### 9. Información codificada en los primeros $n$ bits

Si se conocen los primeros $n$ bits de $\Omega$ (es decir, $\lfloor 2^n \Omega \rfloor$), se puede determinar **cuáles de los programas de longitud $\leq n$ paran**, lo que equivale a resolver el problema de la parada para todos los programas de longitud $\leq n$.

Esto implica que los bits de $\Omega$ contienen información que es **imposible de computar** desde cero. En ese sentido, $\Omega$ es "la cadena más aleatoria posible": es algorítmicamente aleatoria (en el sentido de Martin-Löf) y cualquier prefijo finito de $\Omega$ es incompresible.
