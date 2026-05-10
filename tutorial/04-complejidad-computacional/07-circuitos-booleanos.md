# Circuitos Booleanos y Complejidad de Circuitos

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Lógica booleana](../01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md)
- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Definir circuitos booleanos, tamaño y profundidad.
2. Relacionar las clases de circuitos AC0, NC1 con la jerarquía de complejidad.
3. Entender el programa de circuitos como enfoque hacia la separación P/NP.


## Intuición

Un circuito booleano es un programa sin bucles: una red de compuertas lógicas (AND, OR, NOT) que transforma una entrada de $n$ bits en una salida de $m$ bits. La **complejidad de circuitos** estudia cuántas compuertas necesita un circuito para resolver un problema, y cómo ese número escala con el tamaño de la entrada.

Los circuitos son el modelo natural para el hardware digital y para los algoritmos paralelos. Capturan la idea de computación en tiempo constante con muchos procesadores.

## Definición formal

Un **circuito booleano** $C$ sobre $n$ variables de entrada $x_1, \ldots, x_n$ es un grafo acíclico dirigido (DAG) donde:
- Los **nodos fuente** (sin aristas entrantes) son las variables de entrada $x_i$ o las constantes 0 y 1.
- Los **nodos internos** tienen aristas entrantes de sus argumentos y están etiquetados con una compuerta booleana: $\wedge$ (AND), $\vee$ (OR), $\neg$ (NOT).
- Los nodos de salida tienen sus valores etiquetados como salidas del circuito.

**Parámetros de complejidad:**
- **Tamaño** $s(C)$: número de compuertas (excluyendo entradas). Mide el coste de tiempo secuencial.
- **Profundidad** $d(C)$: longitud del camino más largo desde una entrada a una salida. Mide el tiempo de ejecución paralela.

## Completitud funcional

Cualquier función booleana $f: \{0,1\}^n \to \{0,1\}$ puede computarse con un circuito. La demostración es constructiva: la forma normal disyuntiva (DNF) de $f$ da directamente un circuito de profundidad 3 (NOT para literales, AND para cláusulas, OR final).

**Profundidad 3 y tamaño $\mathcal{O}(n \cdot 2^n)$:** para cada asignación que hace $f$ verdadera, una cláusula AND. La OR final combina todas.

**Bases de compuertas:** $\{\text{AND}, \text{OR}, \text{NOT}\}$ es funcionalmente completa. También lo es $\{\text{NAND}\}$ sola o $\{\text{NOR}\}$ sola. La base $\{\text{AND}, \text{XOR}\}$ captura el álgebra de $\mathbb{F}_2$.

## Familias de circuitos y lenguajes

Un circuito individual solo puede procesar entradas de un tamaño fijo. Para reconocer un lenguaje, se necesita una **familia de circuitos** $\{C_n\}_{n \geq 1}$ donde $C_n$ procesa entradas de longitud $n$.

**Decisión:** $x \in L$ si y solo si $C_{|x|}(x) = 1$.

Esta definición es extremadamente general: cualquier función booleana, incluso no computable, puede reconocerse con una familia de circuitos (pon la tabla de verdad en el circuito). Por eso se añade la condición de **uniformidad**: los circuitos deben poder construirse con un algoritmo eficiente.

## La clase P/poly

**P/poly** es el conjunto de lenguajes reconocibles por familias de circuitos de tamaño polinomial (sin restricción de uniformidad).

- P ⊆ P/poly: cualquier algoritmo en tiempo polinomial $T(n)$ se convierte en un circuito de tamaño $\mathcal{O}(T(n)^2)$.
- P/poly es más grande que P: contiene lenguajes no computable (no uniformes).
- Si NP ⊆ P/poly, entonces la jerarquía polinómica colapsa (resultado de Karp-Lipton).

## Circuitos de profundidad constante: AC0 y NC

**NC** (Nick's Class): lenguajes reconocibles por familias de circuitos de tamaño polinomial y profundidad $\mathcal{O}(\log^k n)$ para algún $k$. Captura los problemas paralelizables eficientemente.

**AC0**: familias de circuitos de tamaño polinomial, profundidad constante, pero con compuertas AND y OR de aridad ilimitada.

Ejemplos:
- La suma de dos enteros de $n$ bits: en NC1 (profundidad $\mathcal{O}(\log n)$).
- El producto de dos enteros: en NC1.
- La paridad: **no está en AC0** (teorema de Håstad, 1987). Requiere profundidad $\Omega(\log n)$ con compuertas de AND y OR de aridad polinomial. La paridad necesita profundidad logarítmica.

La jerarquía es: AC0 ⊂ NC1 ⊆ NC ⊆ P.

## La función paridad y el teorema de Håstad

La función de **paridad** $\text{PAR}(x_1,\ldots,x_n) = x_1 \oplus x_2 \oplus \cdots \oplus x_n$ (XOR de todos los bits) no puede computarse en AC0.

**Argumento intuitivo:** un circuito de profundidad constante y tamaño polinomial solo "ve" una pequeña fracción de las variables a través de cada compuerta. Las restricciones aleatorias (fijar la mayoría de variables al azar) pueden simplificar el circuito a una función constante con alta probabilidad, pero la paridad de las variables restantes sigue siendo no constante. Este método de switching lemma de Håstad formaliza el argumento.

**Consecuencia:** si quisiéramos resolver SAT con circuitos de profundidad constante (un tipo de algoritmo paralelo), no podríamos hacerlo con tamaño polinomial, lo que sugiere que P ≠ NC si la jerarquía de NC colapsa.

## Reducción a circuitos satisfacibles

La clase NP tiene una caracterización en términos de circuitos:

**Teorema de Cook-Levin en lenguaje de circuitos:** $L \in$ NP si y solo si existe una familia de circuitos de tamaño polinomial $\{V_n\}$ (verificadores) tal que $x \in L$ si y solo si existe $y$ con $V_{|x|+|y|}(x,y) = 1$, donde $|y|$ es polinomial en $|x|$.

SAT es el problema de determinar si un circuito booleano (o fórmula propositional) tiene una asignación que lo satisface. La NP-completitud de SAT equivale a decir que SAT es el problema más difícil de NP también en la versión de circuitos.

## Compuertas de umbral y circuitos neuronales

Una **compuerta de umbral** (threshold gate) $\text{THR}_{t,n}$ activa si al menos $t$ de sus $n$ entradas son 1. Generaliza AND ($t=n$) y OR ($t=1$).

La clase **TC0** (threshold circuits de profundidad constante con compuertas de umbral de aridad polinomial) es más potente que AC0:
- La multiplicación de enteros está en TC0.
- La división y la raíz cuadrada también.
- Se conjetura TC0 ⊂ NC1 ⊂ L ⊂ P, pero no se ha demostrado la separación.

Las redes neuronales artificiales de profundidad constante corresponden exactamente a circuitos de TC0.

## Ejemplo: circuito para la suma de dos bits

El semisumador (suma de dos bits $a, b$ con resultado de un bit de suma $s$ y un bit de acarreo $c$):

$$
s = a \oplus b = (a \vee b) \wedge \neg(a \wedge b)
$$
$$
c = a \wedge b
$$

Tamaño: 4 compuertas. Profundidad: 3 (para $s$). El sumador completo (con acarreo entrante) necesita 9 compuertas y profundidad 5.

Para sumar dos números de $n$ bits encadenando $n$ sumadores completos se obtiene profundidad $\mathcal{O}(n)$. Usando suma por adelanto de acarreo (carry-lookahead) se baja a profundidad $\mathcal{O}(\log n)$ con tamaño $\mathcal{O}(n \log n)$.

## Ideas clave
- Un circuito booleano es un DAG de compuertas que computa una función $\{0,1\}^n \to \{0,1\}$.
- Tamaño mide el coste secuencial; profundidad mide el tiempo paralelo.
- Cualquier función booleana tiene un circuito (DNF), pero puede ser de tamaño exponencial.
- P/poly captura los lenguajes reconocibles por circuitos de tamaño polinomial (posiblemente no uniformes).
- AC0 son los circuitos de profundidad constante; la paridad no está en AC0 (Håstad).


## Ejercicios

1. Construir un circuito de profundidad 2 (compuertas AND de primer nivel, OR final) para la función $f(x_1,x_2,x_3) = (x_1 \wedge x_2) \vee (\neg x_1 \wedge x_3)$.
2. Demostrar que $\{\text{NAND}\}$ es funcionalmente completo expresando AND, OR y NOT solo con compuertas NAND.
3. Calcular el tamaño y la profundidad del circuito que implementa la suma de dos números de 4 bits con sumadores completos encadenados.
4. ¿Por qué la familia de circuitos $C_n = $ "circuito que acepta todo" reconoce el lenguaje del problema de la parada? ¿Qué condición falta para que esto sea un algoritmo legítimo?
5. Mostrar que si un problema tiene un algoritmo determinista de tiempo $T(n)$, existe una familia de circuitos de tamaño $\mathcal{O}(T(n)^2)$ que lo resuelve.

## Véase también

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Complejidad descriptiva](../03-computabilidad/08-complejidad-descriptiva.md)


## Referencias

- Arora, S. y Barak, B. (2009). *Computational Complexity: A Modern Approach*, capítulo 6. Disponible en línea.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., capítulo 9.
- Håstad, J. (1987). Computational limitations of small-depth circuits. *MIT Press*.
