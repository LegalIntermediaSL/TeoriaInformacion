# 34 - ETH, SETH y consecuencias

## Contexto

Este ejercicio acompaña el artículo
[ETH y SETH: consecuencias concretas](../../04-complejidad-computacional/13-eth-seth-consecuencias.md).

## Enunciado

**Parte A — Las hipótesis:**

1. Enuncia la Hipótesis Exponencial (ETH). ¿Qué implica sobre algoritmos para 3-SAT?
2. Enuncia la Hipótesis Exponencial Fuerte (SETH). ¿Qué diferencia hay entre ETH y SETH?
3. ¿Son ETH y SETH demostrables desde los axiomas actuales? ¿Se conoce algún algoritmo que las refute?

**Parte B — Lower bounds condicionales:**

4. Bajo SETH, demuestra (informalmente) que no existe un algoritmo para **Edit Distance** en tiempo $O(n^{2-\varepsilon})$. ¿Cuál es la reducción clave?
5. ¿Qué implica ETH sobre la **k-clique** en grafos de $n$ vértices? ¿Y sobre el viajante de comercio (TSP) con $n$ ciudades?
6. Bajo ETH, ¿puede el problema 3-Colorabilidad resolverse en tiempo $2^{o(n)}$?

**Parte C — Distinción práctica:**

7. ¿Cuál es la utilidad práctica de los lower bounds bajo ETH/SETH en contraste con los basados en P ≠ NP?

## Pista

**SETH → Edit Distance:** la reducción de Backurs-Indyk (2016) muestra que un algoritmo $O(n^{2-\varepsilon})$ para Edit Distance implicaría $k$-SAT en tiempo $2^{(1-\delta)n}$ para algún $\delta > 0$, refutando SETH.

**ETH → k-clique:** el problema k-clique requiere tiempo $n^{k/3}$ bajo ETH (reducción desde 3-partición de 3-SAT).

## Solución

### Parte A — Las hipótesis

#### 1. Hipótesis Exponencial (ETH)

**ETH (Impagliazzo-Paturi 2001):** existe una constante $\delta > 0$ tal que 3-SAT no puede resolverse en tiempo $2^{\delta n}$ (donde $n$ es el número de variables).

Equivalentemente: existe $s_3 > 0$ tal que 3-SAT requiere tiempo $\Omega(2^{s_3 n})$.

**Implicación directa:** no existe un algoritmo para 3-SAT que corra en tiempo $2^{o(n)}$, es decir, subexponencial en el número de variables. Los mejores algoritmos conocidos (DPLL con poda, algoritmos de separación local) corren en tiempo $O(1.307^n)$ o similar, todos exponenciales.

#### 2. ETH vs. SETH

**SETH (Impagliazzo-Paturi-Zane 2001):** para todo $\varepsilon > 0$, existe $k$ tal que $k$-SAT no puede resolverse en tiempo $O(2^{(1-\varepsilon)n})$.

Equivalentemente: el exponente óptimo de $k$-SAT tiende a 1 cuando $k \to \infty$.

**Diferencias:**
| | ETH | SETH |
|--|-----|------|
| Afirmación | 3-SAT necesita $2^{\Omega(n)}$ | $k$-SAT necesita $2^{(1-o(1))n}$ para $k$ grande |
| Fuerza | Más débil | Más fuerte (SETH implica ETH) |
| Lower bounds | Exponentiales en $n$ | Cuadráticos/subcuadráticos en $n$ |

#### 3. Demostrabilidad

Ninguna de las dos es demostrable con las técnicas actuales: ambas implican $P \neq NP$. Tampoco se conoce ningún algoritmo que las refute. Son **hipótesis de complejidad**, análogas a conjeturas como la hipótesis de Riemann en número: bien motivadas pero sin demostración.

### Parte B — Lower bounds condicionales

#### 4. SETH → lower bound para Edit Distance

**Backurs e Indyk (2016):** si existiera un algoritmo para Edit Distance de dos cadenas de longitud $n$ en tiempo $O(n^{2-\varepsilon})$, entonces existiría un algoritmo para CNF-SAT con $n$ variables en tiempo $2^{(1-\delta)n}$ para algún $\delta > 0$ que depende de $\varepsilon$.

**Idea de la reducción:** se codifica una instancia de $k$-SAT con $n$ variables como un par de cadenas $(s, t)$ tales que la distancia de edición $d(s,t)$ está directamente relacionada con la satisfacibilidad. La reducción tiene longitud $|s| = |t| = O(2^{n/2})$. Un algoritmo subcuadrático para Edit Distance sobre cadenas de esta longitud correspondería a tiempo $2^{(1-\varepsilon/2)n}$ para SAT, refutando SETH.

**Conclusión:** bajo SETH, Edit Distance (y también LCS, Longest Common Subsequence) son inherentemente cuadráticos. Décadas de investigación sin mejorar $O(n^2)$ tiene una justificación condicional precisa.

#### 5. ETH → k-clique y TSP

**k-clique:** bajo ETH, decidir si un grafo de $n$ vértices contiene una $k$-clique requiere tiempo $n^{\Omega(k)}$. La reducción es desde $k/3$-SAT con $n$ variables hacia $k$-clique en un grafo de $n^{k/3}$ vértices (los grupos de $k/3$ variables forman gadgets). El tiempo óptimo es $\Theta(n^{\omega k/3})$ donde $\omega$ es el exponente de multiplicación de matrices.

**TSP con $n$ ciudades:** bajo ETH, TSP (versión decisión) no puede resolverse en tiempo $2^{o(n)}$. El mejor algoritmo conocido (Held-Karp 1962) corre en $O(2^n n^2)$. Bajo ETH este exponente $n$ no puede eliminarse.

#### 6. ETH → 3-Colorabilidad

Sí. Bajo ETH, 3-Colorabilidad no puede resolverse en tiempo $2^{o(n)}$ (donde $n$ es el número de vértices). La reducción es desde 3-SAT con $n$ variables hacia un grafo de $O(n)$ vértices que es 3-coloreable si y solo si la fórmula es satisfacible. Por tanto, un algoritmo $2^{o(n)}$ para 3-Colorabilidad implicaría $2^{o(n)}$ para 3-SAT, refutando ETH.

### Parte C — Utilidad práctica

**Lower bounds basados en P ≠ NP:** solo dicen "no hay algoritmo polinomial" (si P ≠ NP). No distinguen entre $O(n^{100})$ y $O(n^2)$, ni entre $2^n$ y $2^{n/2}$.

**Lower bounds basados en ETH/SETH:** son cuantitativos y precisos. Permiten:
1. **Confirmar optimalidad de algoritmos específicos:** el algoritmo de Wagner-Fischer ($O(n^2)$) para Edit Distance es óptimo bajo SETH.
2. **Guiar la investigación:** si no existe $O(n^{1.5})$ para LCS bajo SETH, no vale la pena buscarlo.
3. **Fine-grained complexity:** clasificar problemas por si son "cuadráticos", "cúbicos", etc., no solo "polinómicos vs. exponenciales".
4. **Planificación de ingeniería:** saber que un algoritmo de $O(n^2)$ no puede mejorarse a $O(n^{1.99})$ bajo SETH ayuda a priorizar optimizaciones de constantes en lugar de exponentes.
