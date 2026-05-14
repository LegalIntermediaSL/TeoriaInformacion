# Tabla de complejidad unificada

Tabla de referencia cruzada: problema, clase de complejidad, mejor algoritmo conocido, cota inferior y referencia principal. Complementa el artículo [El mapa completo](../05-conexiones-y-aplicaciones/08-mapa-de-conexiones.md).

---

## Problemas de decisión (P y NP)

| Problema | Clase | Mejor algoritmo | Cota inferior | Referencia |
|----------|-------|----------------|---------------|------------|
| Ordenación de $n$ elementos | P | $O(n \log n)$ — mergesort/heapsort | $\Omega(n \log n)$ por comparaciones | Knuth 1968 |
| Camino mínimo (Dijkstra) | P | $O((V+E)\log V)$ | $\Omega(E)$ | Dijkstra 1959 |
| Árbol de expansión mínimo | P | $O(E \log V)$ — Kruskal/Prim | $\Omega(E)$ | Prim 1957 |
| Emparejamiento bipartito | P | $O(E \sqrt{V})$ — Hopcroft-Karp | $\Omega(E)$ | Hopcroft-Karp 1973 |
| SAT (fórmulas booleanas) | NP-c | $O(1.307^n)$ — DPLL optimizado | $2^{\Omega(n)}$ bajo ETH | Cook 1971 |
| 3-SAT | NP-c | $O(1.307^n)$ | $2^{\Omega(n)}$ bajo ETH | Levin 1973 |
| Clique máximo | NP-c | $O(n^{3/4\cdot\omega})$ aprox. | $n^{k/4}$ para $k$-clique bajo ETH | Karp 1972 |
| Colorabilidad con $k$ colores ($k\geq 3$) | NP-c | $O(1.3289^n)$ para 3-col. | $2^{\Omega(n)}$ bajo ETH | — |
| TSP (Viajante de comercio) | NP-c | $O(2^n n^2)$ — Held-Karp | $2^{\Omega(n)}$ bajo ETH | Held-Karp 1962 |
| Mochila 0-1 | NP-c | $O(nW)$ — DP (pseudo-poly) | $\Omega(n)$ si $W$ grande | — |
| Isomorfismo de grafos | Quasi-P | $2^{O((\log n)^3)}$ — Babai 2016 | ? (no NP-c bajo conjeturas) | Babai 2016 |

---

## Problemas de conteo (#P)

| Problema | Clase | Mejor algoritmo exacto | Aproximación | Referencia |
|----------|-------|----------------------|--------------|------------|
| #SAT (contar soluciones de SAT) | #P-c | $O(2^n)$ | No FPRAS bajo P≠NP | Valiant 1979 |
| Permanente de matriz 0-1 | #P-c | $O(n 2^n)$ — Ryser | FPRAS — Jerrum-Sinclair | Valiant 1979 |
| Emparejamientos perfectos en bigrafo | #P-c | $O(n 2^n)$ — Ryser | FPRAS — Jerrum-Sinclair | Valiant 1979 |
| Coloraciones de un grafo | #P-c | $O(2^n n)$ | FPRAS para 2-col. (trivial) | — |
| Partición de un número | #P | $O(n \sqrt{n})$ — Hardy-Ramanujan | Exacto: DP $O(n^{1.5})$ | — |

---

## Problemas de optimización (aproximación)

| Problema | Ratio óptimo | Ratio alcanzado | Límite bajo PCP | Referencia |
|----------|-------------|----------------|-----------------|------------|
| Max-3SAT | 1 (exacto) | $7/8$ — Goemans-Williamson aleatoria | $7/8$-inaprox. bajo UGC | Håstad 2001 |
| Max-Clique | 1 | $n^{1-\varepsilon}$ para todo $\varepsilon$ | inaprox. bajo P≠NP | Håstad 1999 |
| Vertex Cover | 1 | $2 - o(1)$ | $(2-\varepsilon)$ bajo UGC | Khot-Regev 2008 |
| TSP métrico | 1 | $3/2$ — Christofides | NP-difícil de mejorar a $3/2-\varepsilon$ | Christofides 1976 |
| Set Cover | 1 | $\ln n$ | $(1-\varepsilon)\ln n$ bajo P≠NP | Feige 1998 |
| Bin Packing | 1 | APTAS: $1+\varepsilon$ para $\varepsilon$ fijo | PTAS | de la Vega-Lueker 1981 |
| Independiente máximo | 1 | $n^{1-\varepsilon}$ | inaprox. bajo P≠NP | Zuckerman 2007 |

---

## Problemas de codificación y comunicación

| Problema | Cota teórica | Mejor construcción | Algoritmo | Referencia |
|----------|-------------|-------------------|-----------|------------|
| Compresión sin pérdida | $H(X)$ bits/símbolo | Códigos aritméticos | $O(n)$ por símbolo | Shannon 1948 |
| Transmisión sobre BSC($p$) | $C = 1-H(p)$ | Códigos polares | $O(n\log n)$ | Arıkan 2009 |
| Corrección de $t$ errores | $n - k \geq 2t$ (Singleton) | Reed-Solomon | $O(n\log^2 n)$ | Reed-Solomon 1960 |
| Compresión con pérdida | $R(D)$ | Sin construcción práctica óptima | Exponencial en general | Shannon 1959 |
| Codificación aritmética | $H(X) + 2$ bits/bloque | Codif. aritmética adaptativa | $O(n)$ | Witten-Neal-Cleary 1987 |

---

## Problemas parametrizados (FPT)

| Problema | Parámetro $k$ | Algoritmo FPT | Cota inferior | Referencia |
|----------|--------------|---------------|---------------|------------|
| $k$-Vertex Cover | $k$ | $O(2^k \cdot m)$ — BnB | $2^{o(k)}$ bajo ETH | Buss 1993 |
| $k$-Feedback Vertex Set | $k$ | $O(4^k \cdot kn)$ | $2^{o(k)}$ bajo ETH | Becker-Geiger 1996 |
| $k$-Dominating Set | $k$ (treewidth $\leq k$) | $O(3^k \cdot n)$ — Courcelle | W[1]-hard en general | Courcelle 1990 |
| $k$-Longest Path | $k$ | $O(2^k \cdot n)$ — color-coding | W[1]-hard sin param. | Alon-Yuster-Zwick 1995 |
| $k$-Clique | $k$ | $O(n^{k/3 \cdot \omega})$ | W[1]-complete | — |
| Treewidth $\leq k$ | $k$ | $O(2^{3k} \cdot n)$ | $2^{o(k)}$ bajo ETH | Bodlaender 1996 |

---

## Clases de complejidad — relaciones conocidas

```
P ⊆ NP ∩ co-NP ⊆ BPP ⊆ Σ₂P ⊆ PH ⊆ PSPACE ⊆ EXP
       ↕
      NP
      ↑
 P^#P ⊇ PH (Toda 1991)
```

**Inclusiones estrictas conocidas:**
- $P \subsetneq EXP$ (teorema de la jerarquía de tiempo)
- $PSPACE \subsetneq EXPSPACE$ (teorema de la jerarquía de espacio)
- $L \subsetneq PSPACE$ (teorema de Savitch)

**Inclusiones conjeturadas pero no demostradas:**
- $P \subsetneq NP$ (la gran pregunta abierta)
- $NP \subsetneq PSPACE$
- $P \subsetneq BPP$ o $P = BPP$
