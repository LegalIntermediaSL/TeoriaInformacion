# Jerarquía aritmética

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [El problema de la parada](01-problema-de-la-parada.md)
- [Decidibilidad](02-decidibilidad-y-reconocibilidad.md)

## Objetivos de aprendizaje

1. Definir los niveles Σ₀, Σ₁, Π₁ y Δ₁ de la jerarquía aritmética.
2. Clasificar problemas canónicos (parada, TOT, FIN) en la jerarquía.
3. Entender el operador de salto de Turing y cómo genera la jerarquía.


## Intuición

El problema de la parada es indecidible, pero no todos los problemas indecidibles son igual de difíciles. Algunos son más indecidibles que otros: no se pueden resolver incluso con acceso a un oráculo que decide el problema de la parada. La **jerarquía aritmética** es una clasificación fina de los lenguajes de acuerdo con la complejidad de las fórmulas lógicas que los definen, y captura esta estructura graduada de dificultad.

## Tabla resumen de la jerarquía aritmética

| Clase | Cuantificadores | Nombre informal | Ejemplo canónico | Oráculo equivalente |
|-------|----------------|-----------------|-----------------|---------------------|
| $\Delta_0^0 = \Sigma_0^0 = \Pi_0^0$ | Ninguno (acotados) | Decidible / computable | "¿es $n$ primo?" | — |
| $\Sigma_1^0$ | $\exists$ (existencial) | Reconocible (RE) | Problema de la parada $\{\langle M,w\rangle : M(w)\downarrow\}$ | — |
| $\Pi_1^0$ | $\forall$ (universal) | Co-reconocible (coRE) | "$M$ no se detiene en $w$" | — |
| $\Delta_1^0$ | $\exists \cap \forall$ | Decidible (clasif. exacta) | Todos los lenguajes regulares | $\emptyset$ |
| $\Sigma_2^0$ | $\exists\forall$ | RE relativo a $\emptyset'$ | "$M$ se detiene en infinitas entradas" | $\emptyset'$ (HALT) |
| $\Pi_2^0$ | $\forall\exists$ | coRE relativo a $\emptyset'$ | $\text{TOT}$: "$M$ se detiene en toda entrada" | $\emptyset'$ |
| $\Delta_2^0$ | $\exists\forall \cap \forall\exists$ | Decidible con HALT | Problema de la parada con tiempo acotado | $\emptyset'$ |
| $\Sigma_3^0$ | $\exists\forall\exists$ | RE relativo a $\emptyset''$ | "$L(M)$ es infinito" | $\emptyset''$ |
| $\Sigma_n^0$ | $n$ alternaciones ($\exists$ primero) | RE relativo a $\emptyset^{(n-1)}$ | — | $\emptyset^{(n-1)}$ |
| $\Pi_n^0$ | $n$ alternaciones ($\forall$ primero) | coRE relativo a $\emptyset^{(n-1)}$ | — | $\emptyset^{(n-1)}$ |
| $\Delta_n^0$ | Intersección | Decidible con oráculo nivel $n-1$ | — | $\emptyset^{(n-1)}$ |

## Definiciones básicas

Un lenguaje $L \subseteq \{0,1\}^*$ es **aritméticamente definible** si se puede expresar mediante una fórmula de primer orden sobre los naturales con cuantificadores sobre enteros y predicados computables.

La jerarquía se define por el número y alternancia de cuantificadores al inicio de la fórmula:

### Niveles de la jerarquía

| Clase | Definición | Intuición |
|-------|-----------|-----------|
| $\Sigma_0^0 = \Pi_0^0 = \Delta_0^0$ | Decidible (sin cuantificadores no acotados) | Computable |
| $\Sigma_1^0$ | $\exists x_1 \exists x_2 \ldots R(n, \bar{x})$ con $R$ decidible | Reconocible (RE) |
| $\Pi_1^0$ | $\forall x_1 \forall x_2 \ldots R(n, \bar{x})$ | Co-reconocible (co-RE) |
| $\Sigma_2^0$ | $\exists \forall R(n, \bar{x})$ | Verificable con oráculo de parada |
| $\Pi_2^0$ | $\forall \exists R(n, \bar{x})$ | Co-$\Sigma_2^0$ |
| $\Sigma_n^0$ | Bloque $\exists\forall\exists\ldots$ de $n$ alternaciones | — |
| $\Pi_n^0$ | Bloque $\forall\exists\forall\ldots$ de $n$ alternaciones | — |

La clase $\Delta_n^0 = \Sigma_n^0 \cap \Pi_n^0$ contiene los problemas decidibles con un oráculo de nivel $n-1$.

## Relaciones con RE y coRE

Las clases más importantes son las dos primeras:

- **$\Sigma_1^0$ = RE:** los lenguajes reconocibles son exactamente los definibles por una fórmula $\exists \bar{x} R(n, \bar{x})$ donde $R$ es decidible. El testigo $\bar{x}$ es la computación que acepta.

- **$\Pi_1^0$ = coRE:** complementos de los RE. El problema de la parada negado: "$M$ *no* se detiene sobre $w$" es $\Pi_1^0$.

- **$\Delta_1^0$ = decidible:** $\Sigma_1^0 \cap \Pi_1^0$. Un lenguaje es decidible si y solo si tanto él como su complemento son reconocibles.

## El oráculo de salto (jump)

La operación de **salto de Turing** sube un nivel en la jerarquía:

$$K = \{\langle M \rangle : M(\langle M \rangle) \text{ se detiene}\}$$

$K$ es el problema de la parada diagonal. Es $\Sigma_1^0$-completo (los más difíciles de RE).

El **salto de Turing** de un conjunto $A$ es:

$$A' = \{\langle M \rangle : M^A(\langle M \rangle) \text{ se detiene}\}$$

donde $M^A$ es una MT con oráculo $A$. Los saltos sucesivos generan la jerarquía:

$$\emptyset < \emptyset' < \emptyset'' < \emptyset''' < \ldots$$

donde $\emptyset^{(n)}$ es el conjunto de los $\Sigma_n^0$-completos.

**Teorema.** $L \in \Sigma_n^0 \Leftrightarrow L$ es reducible a $\emptyset^{(n)}$ mediante una reducción muchos-a-uno computable.

## Ejemplos en cada nivel

### $\Sigma_1^0$ (RE)
- El problema de la parada: $\{\langle M, w \rangle : M(w) \downarrow\}$.
- El dominio de cualquier función parcialmente computable.
- El lenguaje de las MT que aceptan la cadena vacía: $\{\langle M \rangle : \epsilon \in L(M)\}$.

### $\Pi_1^0$ (coRE)
- El complemento del problema de la parada: $\{\langle M, w \rangle : M(w) \uparrow\}$.
- Las MT que *no* aceptan una cadena dada.

### $\Sigma_2^0$
- "$M$ se detiene en infinitas entradas": $\exists^\infty w \; \langle M, w \rangle \in K$.
  Fórmula: $\exists n \forall m > n \; M(m) \downarrow$.
- El problema $\text{TOT}$: "$M$ se detiene en *toda* entrada" es $\Pi_2^0$.
  Fórmula: $\forall w \exists t \; M$ acepta $w$ en $t$ pasos.

### $\Pi_2^0$
- "$M$ se detiene en *todas* las entradas" (TOT).
- Las MT cuyo lenguaje es *finito*.

### $\Sigma_3^0$
- "El lenguaje de $M$ es infinito": $\exists n \forall k \exists w$ con $|w| > k$ tal que $M(w) \downarrow$.

## El teorema de Post

**Teorema de Post.** Para todo $n \geq 1$:

1. $\Sigma_n^0 \cup \Pi_n^0 \subsetneq \Sigma_{n+1}^0 \cap \Pi_{n+1}^0$.
2. $\Sigma_n^0 \neq \Pi_n^0$ (la jerarquía no colapsa).
3. $\Sigma_n^0 \neq \Sigma_{n+1}^0$ (cada nivel es estrictamente más potente).

La jerarquía es infinita y estricta. No hay un nivel máximo: por encima de toda la jerarquía aritmética están los problemas **no aritméticos** (como la verdad de primer orden sobre los naturales, por el teorema de Tarski).

## Relación con el teorema de Rice

El teorema de Rice generalizado dice que para cualquier propiedad $P$ no trivial del lenguaje de una MT:

- Si $P$ es monotona (cerrada hacia arriba), entonces $\{M : L(M) \in P\}$ es $\Sigma_3^0$ o más alto.
- Si $P$ es co-monotona, es $\Pi_3^0$ o más alto.

Esto da límites precisos de complejidad para propiedades de programas, no solo "es indecidible".

## La jerarquía aritmética y la jerarquía polinómica

Existe una analogía entre la jerarquía aritmética (sin coste computacional) y la jerarquía polinómica (con coste polinomial):

| Aritmética | Polinómica |
|-----------|-----------|
| $\Sigma_1^0$ = RE | NP |
| $\Pi_1^0$ = coRE | coNP |
| $\Sigma_2^0$ | $\Sigma_2^P$ |
| $\Pi_2^0$ | $\Pi_2^P$ |
| $\Delta_1^0$ = decidible | P |

La diferencia: en la jerarquía aritmética los cuantificadores cuantifican sobre todos los naturales; en la polinómica cuantifican sobre testigos polinomiales.

## Ideas clave

1. La jerarquía aritmética clasifica los problemas indecidibles por el número de alternaciones de cuantificadores en su definición lógica.
2. $\Sigma_1^0$ = RE, $\Pi_1^0$ = coRE, $\Delta_1^0$ = decidible.
3. El oráculo de salto $A \to A'$ sube exactamente un nivel en la jerarquía.
4. La jerarquía es estricta e infinita (teorema de Post).
5. La analogía con la jerarquía polinómica revela la misma estructura en dos mundos distintos.

## Ejercicios

1. Clasifica estos problemas en $\Sigma_n^0$ o $\Pi_n^0$: (a) "M acepta exactamente una cadena", (b) "L(M) contiene un número primo", (c) "M se detiene en todas las entradas de longitud ≤ 10".

2. Demuestra que $\Delta_1^0$ = decidible, es decir, que $L$ es decidible si y solo si $L \in \Sigma_1^0 \cap \Pi_1^0$.

3. ¿Por qué el lenguaje de la verdad aritmética (el conjunto de fórmulas de primer orden verdaderas sobre $\mathbb{N}$) no pertenece a ningún nivel de la jerarquía?

4. Construye explícitamente un lenguaje $\Sigma_2^0$ que no sea $\Sigma_1^0$ usando el oráculo de salto.

## Véase también

- [Oráculos y relativización](11-oráculos-y-relativización.md)
- [Aleatoriedad algorítmica](12-aleatoriedad-algoritmica.md)


## Referencias

- Soare, R.I. (2016). *Turing Computability: Theory and Applications*. Springer.
- Rogers, H. (1987). *Theory of Recursive Functions and Effective Computability*. MIT Press.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., cap. 6. Cengage.
- Odifreddi, P. (1989). *Classical Recursion Theory*. North-Holland.
