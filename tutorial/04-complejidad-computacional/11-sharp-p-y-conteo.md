# #P y problemas de conteo

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Definir la clase #P y su relación con el permanente.
2. Enunciar el teorema de Toda: PH ⊆ P^{#P}.
3. Entender por qué contar soluciones es estrictamente más difícil que decidir.


## Intuición

NP pregunta si *existe* una solución; #P pregunta *cuántas* soluciones existen. Esta diferencia parece menor, pero resulta dramática: contar soluciones es mucho más difícil que verificar que hay alguna. El ejemplo más impactante es el permanente de una matriz 0-1: decidir si el permanente es mayor que cero es fácil (en P), pero calcular su valor exacto es #P-completo. El teorema de Toda (1991) conecta #P con toda la jerarquía polinómica, mostrando que el conteo captura una forma de poder computacional que supera a NP.

## Definición de #P

**Definición.** Un problema de función $f: \{0,1\}^* \to \mathbb{N}$ pertenece a **#P** si existe una MT no determinista $M$ en tiempo polinomial tal que:

$$f(x) = \#\{\text{ramas de aceptación de } M(x)\}$$

Es decir, $f(x)$ cuenta el número de certificados (testigos) de longitud polinomial para la entrada $x$.

**Ejemplos:**

| Problema de decisión (NP) | Versión conteo (#P) |
|--------------------------|---------------------|
| SAT: ¿existe asignación satisfaciente? | #SAT: ¿cuántas asignaciones satisfacen $\phi$? |
| k-Coloreo: ¿existe k-coloreo del grafo? | #k-Coloreo: ¿cuántos k-coloreos existen? |
| Matching perfecto: ¿existe uno? | #Matching: ¿cuántos hay? |
| Camino Hamiltoniano: ¿existe? | #Hamiltonian: ¿cuántos caminos hay? |

## #P-completitud

Un problema $f \in \#P$ es **#P-completo** si todo problema de #P se reduce a $f$ mediante una reducción Turing de tiempo polinomial (posiblemente con consultas adaptativas a $f$).

### El permanente

El **permanente** de una matriz $A$ de $n \times n$ es:

$$\text{perm}(A) = \sum_{\sigma \in S_n} \prod_{i=1}^n A_{i,\sigma(i)}$$

donde la suma es sobre todas las permutaciones $\sigma$. El permanente cuenta el número de **matchings perfectos** en el grafo bipartito asociado a $A$:

$$\text{perm}(A) = \#\{\text{matchings perfectos en } G_A\}$$

**Teorema de Valiant (1979).** El cómputo del permanente de una matriz 0-1 es #P-completo.

Esto contrasta con el **determinante** ($\det A = \sum_\sigma \text{sgn}(\sigma) \prod A_{i,\sigma(i)}$), que se calcula en tiempo $O(n^3)$ con eliminación gaussiana. La única diferencia es el signo, pero esa diferencia es fundamental: el permanente no admite cancelaciones y requiere enumerar todas las permutaciones.

### #SAT es #P-completo

Cualquier función $f \in \#P$ puede reducirse a #SAT: dado $x$, construir una fórmula $\phi_x$ cuyas asignaciones satisfacientes correspondan biyectivamente a los testigos de $f(x)$. Esta construcción es análoga a la reducción de Cook-Levin para NP.

## El teorema de Toda (1991)

**Teorema de Toda.** $\text{PH} \subseteq \text{P}^{\#P}$.

Es decir, toda la jerarquía polinómica puede resolverse con una sola consulta a un oráculo #P. Esto implica que:

- Si #P es "fácil" (pudiera resolverse en tiempo polinomial), toda la jerarquía polinómica colapsaría a P.
- El poder de conteo supera al de alternación de cuantificadores: una sola llamada a #P hace más que cualquier número fijo de cuantificadores NP/coNP.

**Esquema de la demostración.** Se basa en dos ingredientes:
1. $\oplus P$ (decidir paridad del número de soluciones) es difícil para PH (via randomización y el lema de Valiant-Vazirani).
2. $\oplus P \subseteq \text{P}^{\#P}$ (calcular el conteo permite determinar la paridad).

## Aproximación para problemas de conteo

Dado que #P es en general intratable (suponiendo que FP ≠ #P), se estudian aproximaciones:

### FPRAS

Un **esquema de aproximación completamente polinomial con aleatoriedad** (FPRAS) para una función $f$ es un algoritmo aleatorizado que, dado $(x, \epsilon, \delta)$:

$$P\left[\left|\frac{\hat{f}}{f(x)} - 1\right| \leq \epsilon\right] \geq 1 - \delta$$

en tiempo $\text{poly}(|x|, 1/\epsilon, \log(1/\delta))$.

### Matchings perfectos en grafos densos (Jerrum-Sinclair-Vigoda)

**Teorema (Jerrum-Sinclair-Vigoda, 2004).** Existe un FPRAS para contar matchings perfectos en grafos generales (el permanente de matrices 0-1).

La demostración usa una cadena de Markov sobre matchings cuya mezcla rápida garantiza que el muestreo aleatorio es eficiente. Este fue un resultado de alto impacto porque el conteo exacto es #P-completo.

### Estimación por muestreo Monte Carlo

Para muchos problemas de conteo, si se puede **muestrear uniformemente** de las soluciones, se puede estimar el conteo. La relación es:

$$\text{muestreo uniforme eficiente} \Leftrightarrow \text{aproximación eficiente del conteo}$$

para una amplia clase de problemas (auto-reducibildad).

## Ejemplos de dificultad de conteo

### Coloración de grafos

Decidir si un grafo es 3-coloreable es NP-completo. Contar el número de 3-coloraciones es #P-completo. Sin embargo, existe un FPRAS para #k-coloreo en grafos con grado máximo $\Delta < k/2$ (via cadenas de Markov de Glauber).

### Partición en física estadística

La **función de partición** en física estadística:

$$Z = \sum_{\sigma} e^{-\beta H(\sigma)}$$

sobre configuraciones $\sigma$ es exactamente un problema de conteo ponderado. En el modelo de Ising, calcular $Z$ es #P-completo en general. Las aproximaciones por MCMC (Monte Carlo de cadena de Markov) son la herramienta estándar.

## Ideas clave

1. #P cuenta los testigos de un problema NP: es fundamentalmente más difícil que decidir su existencia.
2. El permanente de una matriz 0-1 cuenta matchings perfectos y es #P-completo (Valiant 1979).
3. El teorema de Toda (1991): toda la jerarquía polinómica se reduce a una sola consulta #P.
4. Para algunos problemas de conteo existen FPRAS eficientes aunque el conteo exacto sea #P-completo.
5. Muestreo uniforme eficiente y aproximación del conteo son computacionalmente equivalentes.

## Ejercicios

1. ¿Por qué el número de 2-coloraciones de un grafo conexo no es #P-completo? ¿Cuánto vale?

2. Dado el grafo $K_4$ (completo con 4 vértices), calcula manualmente $\text{perm}(A_{K_4})$ donde $A$ es la matriz de adyacencia (sin diagonal). ¿Coincide con el número de matchings perfectos?

3. Explica por qué la suma del permanente y el determinante de una matriz 0-1 es siempre par.

4. Si existiera un algoritmo en tiempo polinomial para #SAT, ¿qué implicaría sobre NP? ¿Sobre PH?

## Véase también

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Complejidad aleatoria (BPP, RP)](08-complejidad-aleatoria.md)



<!-- nav-start -->

---
← [Complejidad Parametrizada](10-complejidad-parametrizada.md) · [Complejidad de comunicación](12-complejidad-de-comunicacion.md) →

<!-- nav-end -->
## Referencias

- Valiant, L.G. (1979). The complexity of computing the permanent. *Theoretical Computer Science*, 8(2), 189–201.
- Toda, S. (1991). PP is as hard as the polynomial-time hierarchy. *SIAM J. Computing*, 20(5), 865–877.
- Jerrum, M., Sinclair, A. y Vigoda, E. (2004). A polynomial-time approximation algorithm for the permanent of a matrix. *J. ACM*, 51(4), 671–697.
- Arora, S. y Barak, B. (2009). *Computational Complexity: A Modern Approach*, cap. 17. Cambridge.
