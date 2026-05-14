# 30 - Oráculos y relativización

## Contexto

Este ejercicio acompaña el artículo
[Oráculos y relativización](../../03-computabilidad/11-oráculos-y-relativización.md).

## Enunciado

**Parte A — Computación con oráculo:**

1. Define qué es una máquina de Turing con oráculo $A$ ($M^A$). ¿Cómo modela el acceso en tiempo O(1) a $A$?
2. Define la clase $P^A$ y $NP^A$. ¿Qué significa que $L \in P^{SAT}$?
3. Describe un problema en $P^{NP}$ que no sea obviamente en P ni en NP. ¿Por qué la jerarquía polinómica $PH$ colapsa si $P = NP$?

**Parte B — Teorema de Baker-Gill-Solovay:**

4. Enuncia formalmente el teorema de Baker-Gill-Solovay (1975). ¿Qué concluye sobre las técnicas de prueba que relativizan?
5. Describe la idea de la construcción del oráculo $A$ tal que $P^A = NP^A$.
6. Describe (a nivel intuitivo) por qué existe un oráculo $B$ tal que $P^B \neq NP^B$. ¿Qué propiedad de $L_B$ lo garantiza?

**Parte C — Barreras:**

7. ¿Por qué la diagonalización no puede resolver P vs. NP? ¿Qué demostraron Razborov y Rudich sobre las "natural proofs"?

## Pista

**Oráculo:** la MT tiene un estado especial de consulta; escribe la consulta en una cinta especial, accede al resultado en un paso.

**Baker-Gill-Solovay:** un oráculo trivial $A = \emptyset$ da $P^\emptyset = P$; con $A = $ PSPACE se obtiene $P^A = NP^A$ (porque PSPACE tiene la potencia suficiente).

**Oráculo de separación:** $L_B = \{1^n \mid |B \cap \{0,1\}^n| \text{ es impar}\}$. Una MT determinista con oráculo necesita explorar exponencialmente muchas cadenas para determinar la paridad.

## Solución

### Parte A — Computación con oráculo

#### 1. Máquina de Turing con oráculo

Una MT con oráculo $A$ es una MT estándar ampliada con:
- Una **cinta de consulta** donde se escribe la cadena $w$.
- Un estado especial $q_?$ de consulta.
- Al entrar en $q_?$, la máquina transita instantáneamente a $q_{si}$ si $w \in A$, o a $q_{no}$ si $w \notin A$.

El acceso es en tiempo $O(1)$ (un solo paso de computación) independientemente de la complejidad interna de $A$.

#### 2. Clases $P^A$ y $NP^A$

- $P^A$: lenguajes decidibles por una MT con oráculo $A$ en tiempo polinomial.
- $NP^A$: lenguajes decidibles por una MT **no determinista** con oráculo $A$ en tiempo polinomial.

$L \in P^{SAT}$ significa que existe un algoritmo polinomial que, con acceso gratuito a un resolvedor de SAT, decide si $x \in L$. Por ejemplo: determinar el mínimo número de cláusulas de una fórmula SAT equivalente es un problema en $P^{SAT}$.

#### 3. $P^{NP}$ y jerarquía polinómica

Un problema en $P^{NP} = \Delta_2^P$: dado un grafo $G$, ¿cuál es el tamaño del clique máximo? (Se puede buscar por búsqueda binaria haciendo consultas al oráculo NP-completo de clique $\geq k$.)

La jerarquía polinómica $PH = \bigcup_k \Sigma_k^P$. Si $P = NP$, entonces $\Sigma_1^P = \Delta_1^P = P$, y por inducción toda la jerarquía colapsa a $P$.

### Parte B — Teorema de Baker-Gill-Solovay

#### 4. Enunciado formal

**Teorema (Baker, Gill, Solovay 1975):** Existen oráculos $A$ y $B$ tales que:

$$P^A = NP^A \quad \text{y} \quad P^B \neq NP^B$$

**Consecuencia:** ninguna técnica de prueba que *relativice* (que produce el mismo resultado cuando se aplica a $M^A$ en lugar de $M$) puede resolver la pregunta $P \stackrel{?}{=} NP$. En particular, la diagonalización clásica relativiza.

#### 5. Oráculo $A$ con $P^A = NP^A$

Sea $A = \text{PSPACE}$. Entonces:
- $NP^A \subseteq PSPACE^{PSPACE} = PSPACE$ (porque PSPACE es cerrado bajo oráculos de PSPACE).
- $P^A = P^{PSPACE} \supseteq PSPACE$.
- Por tanto $P^A \supseteq PSPACE \supseteq NP^A$, lo que da $P^A = NP^A$.

#### 6. Oráculo $B$ con $P^B \neq NP^B$

Se toma $B$ como un subconjunto aleatorio de $\{0,1\}^*$ y se define:

$$L_B = \{1^n \mid |B \cap \{0\text{,}1\}^n| \text{ es impar}\}$$

- $L_B \in NP^B$: el certificado es una cadena $w \in B \cap \{0,1\}^n$ (verificable en tiempo O(1) con el oráculo).
- Pero cualquier algoritmo determinista con oráculo $B$ que intente determinar la paridad de $|B \cap \{0,1\}^n|$ necesita hacer $\Omega(2^n / n^k)$ consultas para cualquier $k$ fijo. Con solo $n^k$ consultas (tiempo polinomial), la paridad puede cambiar sin que el algoritmo lo detecte.

Por tanto $L_B \notin P^B$ con alta probabilidad (y para la construcción explícita, con certeza).

### Parte C — Barreras

#### 7. Diagonalización y natural proofs

**Diagonalización:** la prueba de indecidibilidad de HALT y la separación de DTIME son por diagonalización. Pero como la diagonalización relativiza, el teorema Baker-Gill-Solovay implica que no puede separar P de NP (ni tampoco probar P = NP).

**Natural proofs (Razborov-Rudich 1994):** una "prueba natural" es aquella que usa una propiedad booleana $f$ que es: (1) útil: separa la función target de las fáciles, (2) constructiva: decidible en tiempo $2^{O(n)}$, y (3) grande: verdadera para una fracción $1/poly$ de funciones booleanas. Bajo conjeturas criptográficas estándar (existencia de funciones pseudoaleatorias), no existen pruebas naturales para separar P de NP. La existencia de funciones pseudoaleatorias precisamente implica que no hay propiedades "grandes y constructivas" que separen circuitos pequeños de funciones difíciles.

Estas dos barreras (más la algebrización de Aaronson-Wigderson 2009) indican que la resolución de P vs. NP requerirá técnicas radicalmente nuevas.
