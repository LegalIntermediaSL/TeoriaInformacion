# Complejidad Aleatoria

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Probabilidad](../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md)

## Objetivos de aprendizaje

1. Definir las clases BPP, RP, ZPP y sus relaciones.
2. Entender por qué se conjetura que BPP = P.
3. Analizar la derandomización mediante generadores pseudoaleatorios.


## Intuición

Un algoritmo determinista siempre toma el mismo camino para una entrada dada. Un algoritmo **aleatorio** puede lanzar monedas durante su ejecución y elegir distintos caminos en distintas ejecuciones. Sorprendentemente, la aleatoriedad puede hacer que algunos problemas sean mucho más fáciles de resolver en la práctica, aunque no se sabe si añade poder computacional asintótico real.

## Modelos de computación aleatoria

Una **máquina de Turing probabilística** (PTM) tiene, en cada paso, la opción de leer un bit aleatorio además de leer la cinta. Equivalentemente, en cada configuración puede elegir entre dos transiciones con probabilidad $1/2$ cada una.

El resultado de la computación es ahora una variable aleatoria: la máquina puede aceptar o rechazar con cierta probabilidad. Hay que especificar qué significan los errores admisibles.

## Las clases BPP, RP y ZPP

**BPP** (*Bounded-error Probabilistic Polynomial time*): un lenguaje $L$ está en BPP si existe una PTM que se detiene en tiempo polinomial y satisface:
- Si $x \in L$: $\Pr[\text{acepta}] \geq 2/3$
- Si $x \notin L$: $\Pr[\text{acepta}] \leq 1/3$

La constante $2/3$ es arbitraria: cualquier separación positiva entre las dos probabilidades basta (amplificación por repetición).

**RP** (*Randomized Polynomial time*, error unilateral):
- Si $x \in L$: $\Pr[\text{acepta}] \geq 1/2$
- Si $x \notin L$: $\Pr[\text{acepta}] = 0$

Un rechazo es siempre correcto; solo la aceptación puede equivocarse. co-RP es la clase simétrica donde la aceptación es siempre correcta.

**ZPP** (*Zero-error Probabilistic Polynomial time*): el algoritmo siempre da la respuesta correcta, pero su tiempo de ejecución es una variable aleatoria con esperanza polinomial.

Relación entre las clases: $\text{P} \subseteq \text{ZPP} = \text{RP} \cap \text{co-RP} \subseteq \text{RP} \subseteq \text{BPP} \subseteq \text{P/poly}$.

## Amplificación del éxito

Si un algoritmo en BPP acepta con probabilidad $\geq 2/3$ o $\leq 1/3$, repetirlo $k$ veces e interpretar el voto mayoritario reduce el error a $2^{-\Omega(k)}$:

$$\Pr[\text{error tras } k \text{ repeticiones}] \leq e^{-2k(1/6)^2} = e^{-k/18}$$

Con $k = O(\log(1/\delta))$ repeticiones se baja el error a $\delta$.

## Ejemplo: test de Miller-Rabin

El **test de primalidad de Miller-Rabin** es un algoritmo en co-RP: dado $n$, elige un testigo aleatorio $a \in \{2, \ldots, n-2\}$ y comprueba una condición algebraica. Si $n$ es primo, siempre acepta. Si $n$ es compuesto, rechaza con probabilidad $\geq 3/4$.

El algoritmo se basa en las propiedades de los **pseudo-primos fuertes**. Para $n-1 = 2^s \cdot d$ con $d$ impar, $n$ es primo fuerte en base $a$ si:
- $a^d \equiv 1 \pmod{n}$, o
- $a^{2^r d} \equiv -1 \pmod{n}$ para algún $r \in \{0,\ldots,s-1\}$.

Si $n$ es compuesto, la fracción de bases que lo declaran erróneamente primo es $\leq 1/4$.

Con $k = 40$ repeticiones, la probabilidad de error es $\leq 4^{-40} \approx 10^{-24}$.

**Nota histórica:** en 2002, Agrawal, Kayal y Saxena demostraron que la primalidad está en P (algoritmo AKS). Pero Miller-Rabin sigue usándose en la práctica por su simplicidad y velocidad.

## Ejemplo: identidad polinomial (Schwartz-Zippel)

Dado un polinomio multivariable $p(x_1,\ldots,x_n)$ de grado $d$ expresado como árbol de operaciones, ¿es el polinomio cero identicamente?

**Lema de Schwartz-Zippel:** si $p$ no es el polinomio cero y se evalúa en un punto aleatorio $r \in S^n$ donde $S$ es un conjunto finito de tamaño $|S| \geq 2d$, entonces:
$$\Pr[p(r_1,\ldots,r_n) = 0] \leq \frac{d}{|S|}$$

Esto da un algoritmo en co-RP para verificar que un polinomio es idénticamente cero.

**Aplicación:** comparación de polinomios, verificación de coincidencias en estructuras algebraicas, comprobación de isomorfismo de grafos bipartitos (matching polinomial).

## BPP y la hipótesis de desaleatorización

Una conjetura central en complejidad computacional es que **BPP = P**: la aleatoriedad no añade poder computacional asintótico. La evidencia a favor incluye:

- **Generadores pseudoaleatorios (PRG):** si existe un PRG computable en tiempo polinomial que expande $O(\log n)$ bits verdaderamente aleatorios a $n$ bits indistinguibles de aleatoria, entonces BPP = P.
- **Dureza de funciones:** si existen funciones booleanas que requieren circuitos de tamaño exponencial (hipótesis de dureza), entonces existen PRG que derrandomizan BPP.
- **Resultado de Impagliazzo-Wigderson (1997):** si existe un problema en E = $\text{TIME}(2^{O(n)})$ que requiere circuitos de tamaño $2^{\Omega(n)}$, entonces BPP = P.

## IP y PSPACE

La aleatoriedad también aparece en los **sistemas de prueba interactivos** (IP), donde un verificador probabilístico interactúa con un demostrador todopoderoso.

**Teorema (Shamir, 1992):** IP = PSPACE.

Esto significa que cualquier problema en PSPACE puede verificarse en tiempo polinomial por un verificador que pueda hacer preguntas aleatorias a un demostrador (sin límite de tiempo para el demostrador). Un resultado sorprendente: la aleatoriedad en el verificador equivale a una cantidad enorme de cómputo.

**Ejemplo:** el lenguaje de fórmulas cuantificadas insatisfacibles (co-NP-completo) admite un protocolo de prueba interactiva donde el verificador puede convencerse con alta probabilidad de que la fórmula es insatisfacible.

## Ideas clave

- BPP captura los problemas "eficientemente resolubles con aleatoriedad"; la mayoría de expertos creen que BPP = P.
- La amplificación permite reducir el error a $2^{-\Omega(k)}$ con $k$ repeticiones independientes.
- El test de Miller-Rabin (primalidad en co-RP) y el lema de Schwartz-Zippel (identidad polinomial en co-RP) son aplicaciones prácticas centrales.
- La conjetura de desaleatorización (BPP = P) está vinculada a la existencia de funciones booleanas duras, conectando complejidad aleatoria con complejidad de circuitos.
- IP = PSPACE muestra que la interactividad y la aleatoriedad juntas son sorprendentemente poderosas.

## Ejercicios

1. Muestra que si $L \in \text{RP}$, entonces existe un algoritmo que, tras $k$ repeticiones, rechaza erróneamente con probabilidad $\leq 2^{-k}$.
2. Explica por qué ZPP = RP ∩ co-RP.
3. Describe un escenario práctico donde el lema de Schwartz-Zippel se usa para verificar la multiplicación de matrices (algoritmo de Freivalds).
4. ¿Por qué la existencia de un PRG seguro implicaría BPP = P? Esboza el argumento.
5. El problema del isomorfismo de grafos (GI) está en NP pero no se sabe si está en P o es NP-completo. ¿En qué clase de complejidad aleatoria está GI? Justifica.

## Véase también

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [#P y problemas de conteo](11-sharp-p-y-conteo.md)



<!-- nav-start -->

---
← [Circuitos Booleanos y Complejidad de Circuitos](07-circuitos-booleanos.md) · [El Teorema PCP y la Dureza de Aproximación](09-teorema-pcp.md) →

<!-- nav-end -->
## Referencias

- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., capítulo 10.
- Arora, S. y Barak, B. (2009). *Computational Complexity: A Modern Approach*, capítulos 7-8.
- Impagliazzo, R. y Wigderson, A. (1997). P = BPP if E requires exponential circuits. *STOC 1997*.
