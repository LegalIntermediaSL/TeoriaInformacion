# 23 - Aproximación y heurísticas

## Contexto

Este ejercicio acompaña el artículo
[Aproximación y heurísticas](../../04-complejidad-computacional/06-aproximacion-y-heuristicas.md).

## Enunciado

1. El algoritmo Greedy-VC para Vertex Cover elige iterativamente cualquier arista,
   añade ambos extremos al cover, y elimina todas las aristas cubiertas.
   Demuestra que es una 2-aproximación.

2. Considera el siguiente grafo $G$ para Vertex Cover:
   ```text
   Vértices: {1, 2, 3, 4, 5, 6}
   Aristas: {1-2, 1-3, 2-4, 3-4, 4-5, 4-6}
   ```
   - (a) Ejecuta Greedy-VC eligiendo las aristas en el orden dado. ¿Qué cover produce?
   - (b) ¿Cuál es el cover óptimo? ¿Qué ratio de aproximación real obtuvo el algoritmo?

3. Para TSP (Traveling Salesman Problem) en grafos con la desigualdad triangular,
   el algoritmo Christofides-Serdyuk garantiza un ratio de $3/2$. ¿Por qué el
   TSP general (sin desigualdad triangular) no tiene FPTAS a menos que P = NP?

4. Explica la diferencia entre:
   - Algoritmo de aproximación con ratio garantizado.
   - Heurística sin garantía (por ejemplo, búsqueda local para TSP).
   - FPTAS.

## Pista

**2-aproximación de Greedy-VC:** sea $M$ el conjunto de aristas elegidas. Los
vértices de $M$ forman un matching. Cualquier cover óptimo debe cubrir cada
arista de $M$ con al menos un vértice. El algoritmo elige 2 por cada una.

**TSP general sin DTL:** si hubiese una $\rho$-aproximación para TSP general, se
podría resolver el problema del ciclo hamiltoniano (NP-completo) en tiempo
polinomial.

## Solución

### 1. Greedy-VC es 2-aproximación

Sea $C$ el cover producido por Greedy-VC y $C^*$ el cover óptimo.

**Llave:** el conjunto $M$ de aristas elegidas por el algoritmo (las que se
usan para añadir vértices al cover) forma un **matching** (ninguna dos aristas
de $M$ comparten vértice). Esto es porque cada vez que se elige una arista,
se eliminan todas las aristas adyacentes a sus extremos.

**Cota del OPT:** cualquier cover $C^*$ debe cubrir cada arista de $M$. Como
las aristas de $M$ son disjuntas (matching), $C^*$ necesita al menos un vértice
distinto por cada arista de $M$:

$$|C^*| \geq |M|$$

**Cota del algoritmo:** por cada arista en $M$, el algoritmo añade exactamente 2
vértices:

$$|C| = 2|M|$$

**Ratio:**

$$\frac{|C|}{|C^*|} \leq \frac{2|M|}{|M|} = 2$$

Luego Greedy-VC es una **2-aproximación**. ✓

### 2. Ejemplo con G = (6 vértices)

**Aristas en orden:** {1-2, 1-3, 2-4, 3-4, 4-5, 4-6}

**(a) Ejecución de Greedy-VC:**

```text
Elegir arista 1-2 → añadir {1, 2} al cover → eliminar aristas con 1 o 2:
  Eliminadas: {1-2, 1-3, 2-4}. Quedan: {3-4, 4-5, 4-6}

Elegir arista 3-4 → añadir {3, 4} al cover → eliminar aristas con 3 o 4:
  Eliminadas: {3-4, 4-5, 4-6}. Quedan: {}

Cover resultante: C = {1, 2, 3, 4}. Tamaño: 4.
```

Verificación: todas las aristas cubiertas ✓ (1-2: 1,2 ✓; 1-3: 1,3 ✓; 2-4: 2,4 ✓; 3-4: 3,4 ✓; 4-5: 4 ✓; 4-6: 4 ✓)

**(b) Cover óptimo:**

El vértice 4 cubre las aristas {2-4, 3-4, 4-5, 4-6}. Las aristas restantes
son {1-2, 1-3}, que se cubren con el vértice 1.

**Cover óptimo:** $C^* = \{1, 4\}$, tamaño 2.

**Ratio real:** $|C|/|C^*| = 4/2 = 2$.

El algoritmo alcanzó exactamente el factor 2 de aproximación en este ejemplo:
el peor caso posible.

### 3. Por qué TSP general no tiene FPTAS

**El problema del ciclo hamiltoniano (HC):** dado un grafo $G$, ¿tiene un ciclo
que visita todos los vértices exactamente una vez? HC es NP-completo.

**Reducción de HC a TSP:** dado $G = (V, E)$, construir una instancia de TSP
con $n = |V|$ ciudades:
- Distancia $d(u,v) = 1$ si $(u,v) \in E$.
- Distancia $d(u,v) = n \cdot \rho + 1$ si $(u,v) \notin E$ (para cualquier $\rho$).

Si $G$ tiene un ciclo hamiltoniano, el TSP óptimo tiene coste $n$.

Si $G$ no tiene ciclo hamiltoniano, cualquier tour debe usar al menos una
arista "cara", con coste $\geq n \cdot \rho + 1 > \rho \cdot n$.

**Consecuencia:** si existiese una $\rho$-aproximación polinómica para TSP
general, podría distinguir los dos casos (coste $\leq \rho \cdot n$ vs.
coste $> \rho \cdot n$), resolviendo HC en tiempo polinomial. Como HC es
NP-completo, esto implicaría P = NP.

**Por tanto:** para cualquier ratio $\rho$ polinómica (incluso un FPTAS),
TSP general sin desigualdad triangular no puede tener una $\rho$-aproximación
a menos que P = NP. ∎

### 4. Tipos de algoritmos de optimización

| Tipo | Garantía | Ejemplo |
|------|---------|---------|
| **Aproximación con ratio $\rho$** | $\text{ALG} \leq \rho \cdot \text{OPT}$ en todos los casos | Greedy-VC (ρ=2), Christofides (ρ=3/2 para TSP-métrico) |
| **Heurística sin garantía** | Ninguna cota en el peor caso, buena en la práctica | Búsqueda local 2-opt para TSP, hill climbing |
| **FPTAS** | $\text{ALG} \leq (1+\epsilon) \cdot \text{OPT}$ en tiempo $\text{poly}(n, 1/\epsilon)$ | Knapsack, Subset Sum |

**Diferencias clave:**
- El ratio de aproximación es **absoluto** (válido para toda instancia).
- Las heurísticas pueden fallar en casos específicos pero son rápidas en la práctica.
- Un FPTAS es mejor que cualquier ratio fijo: con $\epsilon = 0.01$ da 1%-optimales.

**Jerarquía:** FPTAS ⊂ PTAS ⊂ APX ⊂ NPO. Los problemas TSP-general y Clique máxima
están en NPO pero no en APX (inaproximables bajo P≠NP con ratio polinómica).

## Comentario

La inaproximabilidad de TSP general es más fuerte que su NP-completitud: no solo
es difícil resolverlo exactamente, sino que es difícil aproximarlo. El teorema PCP
(Probabilistically Checkable Proofs) es la herramienta matemática que permite
demostrar resultados de inaproximabilidad: MAX-3SAT no puede aproximarse más de
7/8 a menos que P = NP.

## Para seguir

El problema del **Set Cover** tiene un algoritmo greedy con ratio $\ln n + 1$.
Demuestra que este ratio es óptimo bajo la hipótesis P ≠ NP: Hastad demostró en
1999 que Set Cover no puede aproximarse con ratio $(1-\epsilon)\ln n$ a menos que NP ⊆
DTIME($n^{O(\log \log n)}$). ¿Qué hace especial a $\ln n$?
