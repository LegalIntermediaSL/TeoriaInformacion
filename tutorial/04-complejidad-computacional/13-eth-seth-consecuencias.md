# Hipótesis ETH y SETH: complejidad de grano fino

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [SAT y 3-SAT](03-sat-y-3-sat.md)

## Objetivos de aprendizaje

1. Enunciar la ETH y la SETH y distinguir sus conjeturas.
2. Derivar lower bounds condicionales para LCS, Edit Distance y Diameter.
3. Entender qué significa que un algoritmo sea «óptimo» bajo ETH.


## Intuición

NP-completitud dice que un problema es "tan difícil como SAT", pero no dice *cuánto* exactamente. ¿SAT se puede resolver en $2^{0.001n}$? ¿O necesita $2^n$? La **complejidad de grano fino** (*fine-grained complexity*) estudia las constantes en los exponentes, asumiendo hipótesis más fuertes que P ≠ NP. La **hipótesis del tiempo exponencial** (ETH) y su forma fuerte (SETH) conectan problemas aparentemente dispares bajo una misma red de reducciones que preservan exponentes exactos.

## La hipótesis del tiempo exponencial (ETH)

**ETH (Impagliazzo-Paturi, 2001).** No existe ningún algoritmo que resuelva $k$-SAT en tiempo $2^{o(n)}$, donde $n$ es el número de variables.

Más precisamente, existe una constante $s_k > 0$ tal que $k$-SAT no puede resolverse en tiempo $2^{s_k n} \cdot \text{poly}(n)$ para ninguna constante menor que $s_k$, y $s_k \to \ln 2$ cuando $k \to \infty$.

**Consecuencias directas de ETH:**

- **3-SAT en tiempo $2^{o(n)}$ es imposible** (si ETH es cierta).
- Los mejores algoritmos conocidos para 3-SAT tardan $O(1.307^n)$; ETH dice que no pueden bajar de $2^{\epsilon n}$ para algún $\epsilon > 0$.
- Si ETH es falsa, existiría un algoritmo quasi-polinomial para 3-SAT, lo que implicaría que NP ⊆ DTIME($n^{\log n}$), colapso radical de la jerarquía.

## El lema de sparsificación

Un resultado clave que hace ETH robusta:

**Lema de sparsificación (Impagliazzo-Paturi-Zane).** Para cada $\epsilon > 0$, todo $k$-SAT con $n$ variables y $m$ cláusulas se puede reducir (en tiempo $2^{\epsilon n}$) a una disyunción de instancias de $k$-SAT con $O(n)$ cláusulas.

Consecuencia: ETH formulada con el número de variables y con el número de cláusulas es equivalente. No importa si el parámetro es $n$ o $m$.

## La hipótesis del tiempo exponencial fuerte (SETH)

**SETH (Impagliazzo-Paturi, 2001).** Para todo $\epsilon > 0$, existe $k$ tal que $k$-SAT no puede resolverse en tiempo $(2 - \epsilon)^n$.

SETH es más fuerte que ETH: afirma que los mejores algoritmos para $k$-SAT con $k$ grande se acercan a $2^n$ y no pueden mejorarse sustancialmente. Es equivalente a decir que no existe un algoritmo que mejore exponencialmente la fuerza bruta en SAT.

**Advertencia:** muchos expertos creen que SETH es más probable de ser falsa que ETH; sin embargo, los resultados que se deducen de SETH son en su mayoría considerados correctos intuitivamente.

## Consecuencias de ETH/SETH en problemas concretos

### Longest Common Subsequence (LCS)

**Teorema (Abboud-Backurs-Williams, 2015).** Si LCS de dos cadenas de longitud $n$ puede resolverse en tiempo $O(n^{2-\epsilon})$ para algún $\epsilon > 0$, entonces SETH es falsa.

El mejor algoritmo conocido es $O(n^2 / \log n)$, y el resultado sugiere que no mejorará mucho. El coste cuadrático de LCS parece ser *óptimo bajo SETH*.

### Edit Distance (distancia de edición)

**Teorema.** Si edit distance puede calcularse en $O(n^{2-\epsilon})$, SETH es falsa.

Misma situación que LCS. El algoritmo de programación dinámica en $O(n^2)$ es aparentemente óptimo.

### Subset Sum

**Teorema (ETH).** Subset Sum de $n$ números no puede resolverse en tiempo $2^{o(n)}$ bajo ETH. Los algoritmos $O(2^{n/2})$ por meet-in-the-middle son óptimos bajo ETH.

### Clique y conjuntos independientes

**Teorema (ETH).** No existe algoritmo $f(k) \cdot n^{o(k)}$ para $k$-Clique bajo ETH. El mejor conocido es $n^{k/3}$ (multiplicación de matrices); si ETH es cierta, no puede ser $n^{o(k)}$.

### k-SUM

$k$-SUM: ¿existen $k$ números en un conjunto de $n$ que sumen 0?

**Teorema.** Bajo SETH, $k$-SUM requiere tiempo $n^{\lceil k/2 \rceil - o(1)}$. Para $k=3$ (3-SUM): $\Omega(n^{2-o(1)})$.

El problema 3-SUM con cota $\tilde{O}(n^2)$ estaba abierto durante décadas; recientemente se mejora ligeramente a $O(n^2 / \log n)$, pero la barrera $n^{2-\epsilon}$ parece sólida bajo SETH.

## Reducción de grano fino

Las reducciones en complejidad de grano fino deben **preservar exponentes**. Una reducción de $A$ a $B$ es válida en este contexto si transforma instancias de $A$ de tamaño $n$ en instancias de $B$ de tamaño $\text{poly}(n)$ en tiempo $O(n^c)$, de modo que:

- Algoritmo de $B$ en tiempo $O(n^\alpha) \Rightarrow$ algoritmo de $A$ en tiempo $O(n^{\max(\alpha, c)})$.

Esta estructura crea una **web de reducciones de grano fino**: si cualquiera de los problemas centrales (LCS, Edit Distance, APSP, 3-SUM) tiene un algoritmo subóptimo, otros muchos también lo tendrían.

## El problema del camino más corto entre todos los pares (APSP)

APSP: ¿cuáles son las distancias más cortas entre todos los pares de nodos en un grafo ponderado de $n$ vértices?

**Hipótesis APSP.** No existe algoritmo $O(n^{3-\epsilon})$ para APSP.

Bajo esta hipótesis (implicada por SETH para grafos densos), se demuestran cotas inferiores para:

- Detección de triángulo de peso mínimo.
- Detección de ciclo negativo.
- Multiplicación de matrices booleanas.

## Ideas clave

1. ETH: $k$-SAT requiere tiempo $2^{\Omega(n)}$; no hay algoritmos quasi-polinomiales.
2. SETH: $k$-SAT con $k$ grande requiere tiempo $(2-\epsilon)^n$; la fuerza bruta es casi inevitable.
3. Bajo ETH/SETH, LCS, Edit Distance y 3-SUM requieren tiempo cuadrático en $n$.
4. Las reducciones de grano fino preservan exponentes exactos, creando una web de equivalencias condicionales.
5. La hipótesis APSP extiende la red a problemas de grafos con coste cúbico aparentemente óptimo.

## Ejercicios

1. Si 3-SAT con $n$ variables puede resolverse en tiempo $O(1.1^n)$, ¿qué implica para ETH?

2. Explica por qué el lema de sparsificación es necesario para que ETH sea robusta respecto al parámetro usado (variables vs. cláusulas).

3. El algoritmo de Floyd-Warshall para APSP tarda $O(n^3)$. ¿Qué hipótesis adicional se necesita para conjeturar que es óptimo?

4. ¿Puede ETH ser cierta y P = NP al mismo tiempo? Justifica.

## Véase también

- [Complejidad parametrizada](10-complejidad-parametrizada.md)
- [SAT y 3-SAT](03-sat-y-3-sat.md)



<!-- nav-start -->

---
← [Complejidad de comunicación](12-complejidad-de-comunicacion.md) · [Complejidad cuántica: BQP y QMA](14-complejidad-cuantica-bqp-qma.md) →

<!-- nav-end -->
## Referencias

- Impagliazzo, R. y Paturi, R. (2001). On the complexity of k-SAT. *Journal of Computer and System Sciences*, 62(2), 367–375.
- Abboud, A., Backurs, A. y Williams, V.V. (2015). Tight hardness results for LCS and other sequence similarity measures. *Proc. FOCS*, 59–78.
- Williams, V.V. (2018). On some fine-grained questions in algorithms and complexity. *Proc. ICM*.
- Vassilevska Williams, V. (2015). Hardness of easy problems: Basing hardness on popular conjectures. *Proc. IPEC*.
