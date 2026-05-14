> **Nota:** Esta es la versión sin fórmulas LaTeX de [10-complejidad-parametrizada](../../04-complejidad-computacional/10-complejidad-parametrizada.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Complejidad Parametrizada

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Definir la clase FPT y distinguirla de XP.
2. Aplicar la técnica de árbol de búsqueda acotado a k-Vertex Cover.
3. Entender la kernelización y el ancho de árbol como herramientas FPT.


## Intuición

Muchos problemas NP-difíciles son intratables en general pero tienen instancias "pequeñas"
que aparecen en la práctica. La **complejidad parametrizada** formaliza esta idea: un problema
se parametriza por alguna medida `k` de la instancia (tamaño de la solución, ancho de árbol
del grafo, etc.) y se estudia si puede resolverse en tiempo `f(k) · n^c` para alguna
función `f` y constante `c`.

## Problemas fijos en parámetro: FPT

Un problema parametrizado `(L, k)` es **fijo en parámetro** (FPT, *Fixed-Parameter Tractable*)
si puede resolverse en tiempo `f(k) · n^(O(1))` para alguna función computable `f`
(posiblemente exponencial en `k`) y `n = |x|`.

La clave es que la dependencia exponencial está confinada al parámetro `k`: si `k` es pequeño,
el algoritmo es eficiente.

**Ejemplo:** `k`-Vertex Cover. Dado un grafo `G` y un entero `k`, ¿tiene `G` un vertex cover
de tamaño `≤ k`? (Un vertex cover es un conjunto `S` de vértices tal que toda arista tiene
al menos un extremo en `S`.)

El problema es NP-completo en general. Pero admite un algoritmo FPT sencillo:

**Árbol de búsqueda acotado:**

![Árbol de búsqueda acotado para k-Vertex Cover con k=3: la raíz representa el grafo original. Cada nivel divide por arista {u,v}: la rama izquierda incluye u en el cubrimiento (k disminuye en 1), la rama derecha incluye v. El árbol tiene profundidad k=3 y como máximo 2^3=8 hojas. Las ramas que exceden k quedan podadas.](../imagenes/bounded-search-tree-vc.svg)

- Si la instancia tiene una arista `(u,v)`, al menos uno de `u,v` debe estar en el cover.
- Branching: incluir `u` (reduce `k` en 1) o incluir `v` (reduce `k` en 1).
- El árbol tiene `2^k` ramas y cada rama procesa el grafo en `O(n)`.
- Tiempo total: `O(2^k · n)`.

Para `k = 20` y `n = 10⁶`, esto es `≈ 10⁹` operaciones — manejable.

## La jerarquía W

La clase **W[1]** contiene problemas que se cree no están en FPT pero que son "tratables"
de forma parametrizada con respecto a alguna noción debilitada. La jerarquía es:


> **Fórmula:** `FPT ⊆ W[1] ⊆ W[2] ⊆ ⋯ ⊆ XP`


**XP** contiene los problemas resolubles en tiempo `n^(f(k))` (polinomial para `k` fijo,
pero el exponente crece con `k`).

**W[1]-completo:** `k`-Clique, `k`-Independent Set, `k`-Multicolored Clique.

**W[2]-completo:** `k`-Dominating Set.

La conjetura **ETH** (Exponential Time Hypothesis, Impagliazzo-Paturi 2001):
3-SAT no puede resolverse en tiempo `2^(o(n))`. Bajo ETH:

- `k`-Clique no está en FPT (requiere `n^(Ω(k))`).
- `k`-Independent Set no está en FPT.

## Kernelización

Una **kernelización** de un problema parametrizado `(L, k)` es una reducción polinomial
que transforma `(x, k)` en una instancia equivalente `(x', k')` con `|x'| ≤ g(k)` y
`k' ≤ k` para alguna función `g`.

Si existe una kernelización con `|x'| ≤ p(k)` polinomial en `k`, el problema tiene
un **kernel polinomial**.

**Teorema:** un problema en NP está en FPT si y solo si tiene una kernelización
(no necesariamente polinomial).

**Ejemplo: kernel para `k`-Vertex Cover.** Reglas de reducción:

1. Si hay un vértice de grado `> k`, debe estar en el cover → incluirlo, reducir `k`.
2. Si hay aristas aisladas que no inciden en ningún vértice de grado `> 0`, eliminarlas.
3. Si quedan más de `k²` aristas, la respuesta es NO.
4. Tras las reducciones, el kernel tiene `≤ k²` aristas y `≤ 2k²` vértices.

Con el kernel de tamaño `O(k²)`, el árbol de búsqueda acotado resuelve el problema
en tiempo `O(2^k · k²)`.

**Kernel lineal para Vertex Cover (Crown Decomposition):**
Existe un kernel de tamaño `2k` vértices usando descomposición en corona. Es el kernel
de tamaño óptimo conocido.

## Ancho de árbol (treewidth)

El **ancho de árbol** `tw(G)` mide qué tan "parecido a un árbol" es un grafo.
Para un árbol, `tw = 1`. Para la rejilla `n × n`, `tw = n`.

**Descomposición en árbol:** una descomposición de `G` en árbol es un árbol `T` donde
cada nodo `i ∈ T` tiene una "bolsa" `B_i ⊆ V(G)` tal que:
1. `cup_i B_i = V(G)`.
2. Para cada arista `(u,v) ∈ G`, existe `B_i` que contiene ambos.
3. Para cada vértice `v`, los nodos de `T` con `v ∈ B_i` forman un subárbol conexo.

El ancho de árbol es `tw(G) = min_T (max_i |B_i| - 1)`.

**Teorema de Courcelle (1990):** todo problema expresable en lógica de segundo orden
monadica (MSO) puede resolverse en tiempo `f(tw) · n` para grafos de ancho
de árbol `≤ tw`.

Esto incluye coloración, ciclos Hamiltonianos, domination, independient set, etc. —
todos son FPT parametrizados por el ancho de árbol.

**Programación dinámica en la descomposición en árbol:**
Para `k`-Vertex Cover con `tw(G) = w`, la DP en la descomposición procesa
cada bolsa considerando `2^(|B_i|)` subconjuntos, dando tiempo `O(2^w · n)`.

## Ejemplos de problemas FPT

| Problema | Parámetro | Complejidad FPT |
|---------|-----------|-----------------|
| `k`-Vertex Cover | `k` | `O(1.2738^k + kn)` (mejor algoritmo conocido) |
| `k`-Feedback Vertex Set | `k` | `O(4^k · kn)` |
| `k`-Longest Path | `k` | `O(4^k · n^(O(1)))` |
| Graph problems | `tw` | `O(f(tw) · n)` (Courcelle) |
| `k`-Planar Subgraph | `k` | `O(2^(O(k)) + n)` |

## Problemas W[1]-difíciles

| Problema | Por qué W[1]-difícil |
|---------|---------------------|
| `k`-Clique | Reducción desde Independent Set |
| `k`-Independent Set | Reducción desde Clique |
| `k`-Multicolored Clique | Clave para reducciones de W[1] |
| `k`-Weighted 2-SAT | Reducción desde Independent Set |

## Ideas clave

- FPT captura los problemas NP-difíciles que son manejables cuando el parámetro es pequeño.
- El árbol de búsqueda acotado es la técnica FPT más simple: branching con reducción de `k`.
- La kernelización reduce la instancia a un tamaño `g(k)` en tiempo polinomial: es una
  preprocesamiento garantizado.
- El ancho de árbol es el parámetro "universal" para grafos: vía el teorema de Courcelle,
  cualquier propiedad MSO es FPT parametrizada por `tw`.
- La jerarquía W[`i`] y la ETH proporcionan evidencia condicional de que ciertos problemas
  (clique, independent set) no son FPT.

## Ejercicios

1. Implementa el árbol de búsqueda acotado para `k`-Vertex Cover y mide el tiempo para
   grafos aleatorios con `n = 100` y `k ∈ \{5, 10, 15, 20\}`.
2. Aplica las reglas de kernelización para Vertex Cover a un grafo de ejemplo con 8 vértices.
3. Calcula el ancho de árbol de: (a) un camino `P_n`, (b) un ciclo `C_n`, (c) `K_4`.
4. ¿Por qué `k`-Clique es W[1]-difícil? Esboza la reducción desde `k`-Independent Set.
5. Si la ETH es verdadera, ¿puede `k`-Clique resolverse en tiempo `f(k) · n^(k/3)`?
   ¿Y en tiempo `f(k) · n^(√(k))`?

## Véase también

- [Aproximación y heurísticas](06-aproximacion-y-heuristicas.md)
- [ETH y SETH](13-eth-seth-consecuencias.md)


## Referencias

- Cygan, M. et al. (2015). *Parameterized Algorithms*. Springer. Disponible en línea.
- Downey, R. y Fellows, M. (2013). *Fundamentals of Parameterized Complexity*. Springer.
- Courcelle, B. (1990). The monadic second-order logic of graphs I. *Information and Computation*.
- Impagliazzo, R. y Paturi, R. (2001). On the complexity of `k`-SAT. *J. Comput. Syst. Sci.*
