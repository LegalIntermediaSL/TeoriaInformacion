# 22 - Reducciones polinómicas

## Contexto

Este ejercicio acompaña el artículo
[Reducciones polinómicas](../../04-complejidad-computacional/02-reducciones-polinomicas.md).

## Enunciado

1. Demuestra que CLIQUE ≤ₚ INDEPENDENT SET (IS):
   - CLIQUE: ¿tiene el grafo $G$ una clique de tamaño $k$?
   - IS: ¿tiene el grafo $G$ un conjunto independiente de tamaño $k$?

2. Demuestra que IS ≤ₚ VERTEX COVER (VC):
   - VC: ¿tiene el grafo $G$ un vertex cover de tamaño $k$?

3. Con las reducciones anteriores, explica por qué CLIQUE es NP-completo.

4. Considera el grafo $G$ con 5 vértices y aristas $\{1\text{-}2, 1\text{-}3, 2\text{-}3, 3\text{-}4, 4\text{-}5\}$.
   - (a) ¿Cuál es la clique máxima?
   - (b) Aplica la reducción CLIQUE → IS para traducir la instancia.
   - (c) ¿Cuál es el IS máximo en el grafo complemento?

## Pista

**CLIQUE → IS:** el complemento de un grafo es el grafo con las aristas opuestas.
Una clique en $G$ es un IS en $\bar{G}$ (el complemento).

**IS → VC:** un conjunto $S$ es IS si y solo si $V \setminus S$ es VC. Así,
$k$-IS existe ↔ $(n-k)$-VC existe.

## Solución

### 1. CLIQUE ≤ₚ INDEPENDENT SET

**Construcción de la reducción:**

Dado $\langle G, k \rangle$ (instancia de CLIQUE), construir $\langle \bar{G}, k \rangle$
donde $\bar{G}$ es el **grafo complemento** de $G$:

$$\bar{G} = (V, \overline{E}) \quad \text{donde} \quad \overline{E} = \{(u,v) : (u,v) \notin E, u \neq v\}$$

La reducción es $f(\langle G, k \rangle) = \langle \bar{G}, k \rangle$.

**Corrección:**

- **Si $G$ tiene una $k$-clique $S$:** en $S$, todos los pares de vértices están
  conectados en $G$, luego ningún par está en $\overline{E}$. Por tanto $S$ es
  un IS de tamaño $k$ en $\bar{G}$.

- **Si $\bar{G}$ tiene un IS $S$ de tamaño $k$:** en $S$, ningún par de vértices
  está en $\overline{E}$, luego todos los pares están en $E$. Por tanto $S$ es una
  clique de tamaño $k$ en $G$.

**Tiempo:** construir $\bar{G}$ requiere $O(n^2)$ tiempo. La reducción es polinómica. ✓

### 2. IS ≤ₚ VERTEX COVER

**Construcción:**

Dado $\langle G, k \rangle$ (instancia de IS), construir $\langle G, n-k \rangle$
donde $n = |V|$. El grafo no cambia, solo el parámetro.

La reducción es $f(\langle G, k \rangle) = \langle G, n-k \rangle$.

**Corrección (lema complementariedad IS-VC):**

Sea $G = (V, E)$. Afirmamos: $S$ es IS ↔ $V \setminus S$ es VC.

- **($\Rightarrow$)** Si $S$ es IS, para toda arista $(u, v) \in E$: como $S$ es
  IS, no pueden estar $u$ y $v$ ambos en $S$. Luego al menos uno está en
  $V \setminus S$. Por tanto $V \setminus S$ cubre toda arista: es VC.

- **($\Leftarrow$)** Si $V \setminus S$ es VC, para toda arista $(u,v) \in E$
  alguno de $u, v$ está en $V \setminus S$, es decir, no pueden estar ambos en $S$.
  Por tanto $S$ es IS.

Así: $G$ tiene IS de tamaño $k$ ↔ $G$ tiene VC de tamaño $n-k$. ✓

**Tiempo:** la reducción es trivial, $O(1)$. ✓

### 3. NP-completitud de CLIQUE

**Teorema.** CLIQUE es NP-completo.

**CLIQUE ∈ NP:** dado el certificado $S$ (la clique candidata), verificar en tiempo
$O(k^2)$ que todos los pares en $S$ son adyacentes. ✓

**CLIQUE es NP-difícil:** ya sabemos que SAT ≤ₚ 3-SAT ≤ₚ INDEPENDENT SET (por el
teorema de Cook-Levin y reducciones conocidas). Usando el resultado del apartado 1:

$$\text{IS} \leq_p \text{CLIQUE}$$

(simplemente aplicamos la misma reducción de CLIQUE→IS en sentido inverso:
IS en $G$ = CLIQUE en $\bar{G}$, luego IS ≤ₚ CLIQUE). Como IS es NP-difícil,
CLIQUE también lo es. ∎

### 4. Ejemplo con G = (5 vértices, aristas {1-2, 1-3, 2-3, 3-4, 4-5})

**(a) Clique máxima en G:**

Examinamos subgrafos completos:
- $\{1, 2, 3\}$: aristas 1-2 ✓, 1-3 ✓, 2-3 ✓. Es una 3-clique.
- No hay 4-clique (los vértices 4, 5 solo tienen grado 1-2).

**Clique máxima:** $\{1, 2, 3\}$, tamaño 3.

**(b) Traducción CLIQUE → IS:**

El grafo complemento $\bar{G}$ tiene las aristas que NO están en $G$:

Aristas de $G$: {1-2, 1-3, 2-3, 3-4, 4-5}  
Todas las posibles con 5 vértices: {1-2, 1-3, 1-4, 1-5, 2-3, 2-4, 2-5, 3-4, 3-5, 4-5}  

Aristas de $\bar{G}$: {1-4, 1-5, 2-4, 2-5, 3-5}

La instancia IS traducida es $\langle \bar{G}, 3 \rangle$.

**(c) IS máximo en $\bar{G}$:**

En $\bar{G}$ con aristas {1-4, 1-5, 2-4, 2-5, 3-5}:

- ¿Es $\{1, 2, 3\}$ IS en $\bar{G}$? Aristas entre ellos en $\bar{G}$: ninguna
  (1-2, 1-3, 2-3 sí están en $G$, no en $\bar{G}$). ✓ $\{1,2,3\}$ es IS de
  tamaño 3 en $\bar{G}$.

**IS máximo:** $\{1, 2, 3\}$, tamaño 3 — exactamente la clique que encontramos en $G$. ✓

## Comentario

Las reducciones CLIQUE ↔ IS ↔ VC forman un triángulo cerrado. Conociendo la
solución de cualquiera de los tres problemas, se pueden resolver los otros dos en
tiempo polinomial. Esta red de reducciones es la estructura fundamental de los
resultados de NP-completitud: no hay que reducir cada nuevo problema desde SAT;
basta con reducir desde cualquier problema NP-completo conocido.

## Para seguir

Demuestra que VERTEX COVER ≤ₚ SET COVER: dado un conjunto universo $U$ y una
familia de subconjuntos $\mathcal{F}$, ¿existe $\mathcal{F}' \subseteq \mathcal{F}$
con $|\mathcal{F}'| \leq k$ que cubre $U$? Construye explícitamente la reducción
y demuestra su corrección.
