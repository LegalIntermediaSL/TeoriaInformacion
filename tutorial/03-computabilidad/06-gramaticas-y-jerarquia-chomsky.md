# Gramáticas y la Jerarquía de Chomsky

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Autómatas finitos y lenguajes regulares](05-automatas-finitos-y-lenguajes-regulares.md)

## Objetivos de aprendizaje

1. Distinguir los cuatro tipos de gramáticas en la jerarquía de Chomsky.
2. Relacionar cada nivel de la jerarquía con su clase de autómata correspondiente.
3. Demostrar que los lenguajes regulares son un subconjunto propio de los CFL.


## Intuición

¿Cuánta potencia computacional necesita un modelo para reconocer un lenguaje? Chomsky clasificó los lenguajes formales en cuatro niveles según la complejidad de las gramáticas que los generan. Esta jerarquía conecta directamente con la jerarquía de máquinas: autómatas finitos, autómatas de pila, máquinas de Turing linealmente acotadas y máquinas de Turing generales.

Entender la jerarquía de Chomsky permite saber de qué tipo es un lenguaje antes de intentar reconocerlo, y elegir el modelo computacional más económico.

## Gramáticas formales

Una **gramática formal** $G = (V, \Sigma, R, S)$ consiste en:
- $V$: conjunto de **variables** (símbolos no terminales), por ejemplo $\{S, A, B\}$.
- $\Sigma$: **alfabeto** de terminales (los símbolos del lenguaje de salida), por ejemplo $\{a, b\}$.
- $R$: conjunto de **reglas de producción** $\alpha \to \beta$ donde $\alpha, \beta \in (V \cup \Sigma)^*$ y $\alpha$ contiene al menos una variable.
- $S \in V$: variable de inicio.

El **lenguaje** $L(G)$ es el conjunto de cadenas de terminales que se pueden derivar desde $S$ aplicando reglas de $R$.

## Los cuatro niveles

![Jerarquía de Chomsky representada como cuatro óvalos concéntricos: el más interior contiene los lenguajes regulares (reconocidos por autómatas finitos), el siguiente los lenguajes libres de contexto (autómatas de pila), luego los lenguajes dependientes del contexto (máquinas de Turing acotadas en espacio), y el exterior los lenguajes recursivamente enumerables (máquinas de Turing generales).](../imagenes/chomsky-hierarchy.svg)

### Tipo 3 — Lenguajes regulares

**Gramáticas regulares:** cada regla tiene la forma $A \to aB$ o $A \to a$ (regular a derecha) o $A \to Ba$ o $A \to a$ (regular a izquierda), donde $A, B \in V$ y $a \in \Sigma$.

**Modelo equivalente:** autómata finito determinista (DFA) o no determinista (NFA).

**Ejemplos de lenguajes regulares:**
- Cadenas binarias que contienen el patrón `01`.
- Identificadores de Python (letras, dígitos y guiones bajos que no empiezan con dígito).
- Cadenas de longitud par.

**Lo que no puede:** no puede reconocer $\{a^n b^n : n \geq 0\}$ porque necesitaría "recordar" cuántas $a$s vio, y la memoria de un autómata finito es constante.

### Tipo 2 — Lenguajes libres de contexto

**Gramáticas libres de contexto (CFG):** cada regla tiene la forma $A \to \gamma$ donde $A \in V$ y $\gamma \in (V \cup \Sigma)^*$.

**Modelo equivalente:** autómata de pila (pushdown automaton, PDA).

**Ejemplos:**
- $\{a^n b^n : n \geq 0\}$ — la gramática con $S \to aSb \mid \varepsilon$ genera exactamente este lenguaje.
- Expresiones aritméticas bien parentizadas: $E \to E + T \mid T$, $T \to T \ast F \mid F$, $F \to (E) \mid \text{número}$.
- La mayoría de los lenguajes de programación (su sintaxis es casi libre de contexto).

**Lo que no puede:** no puede reconocer $\{a^n b^n c^n : n \geq 0\}$ (necesitaría dos contadores independientes, y la pila solo permite uno).

### Tipo 1 — Lenguajes sensibles al contexto

**Gramáticas sensibles al contexto (CSG):** cada regla tiene la forma $\alpha A \beta \to \alpha \gamma \beta$ donde $A \in V$, $\alpha, \beta, \gamma \in (V \cup \Sigma)^*$ y $|\gamma| \geq 1$. El lado izquierdo puede ser más largo que una sola variable, pero las reglas no pueden reducir la longitud de la cadena.

**Modelo equivalente:** máquina de Turing linealmente acotada (LBA): una MT restringida a usar solo el espacio de la entrada.

**Ejemplo:** $\{a^n b^n c^n : n \geq 0\}$ es sensible al contexto.

**Propiedad:** los lenguajes sensibles al contexto son decidibles (siempre hay un algoritmo que termina), pero generalmente costosos de reconocer.

### Tipo 0 — Lenguajes recursivamente enumerables

**Gramáticas sin restricción:** las reglas $\alpha \to \beta$ pueden tener cualquier forma con $\alpha$ no vacío.

**Modelo equivalente:** máquina de Turing general.

**Ejemplo:** el lenguaje de las máquinas de Turing que se detienen sobre la cadena vacía es de tipo 0 pero no de tipo 1.

**Propiedad:** estos lenguajes son reconocibles pero puede que no decidibles. No existe algoritmo general que siempre termine para todos sus miembros.

## Tabla de la jerarquía

| Tipo | Nombre | Gramática | Autómata | Decidible |
|------|--------|-----------|----------|-----------|
| 3 | Regular | Regular | DFA/NFA | Sí |
| 2 | Libre de contexto | CFG | PDA | Sí |
| 1 | Sensible al contexto | CSG | LBA | Sí |
| 0 | Recursivamente enumerable | Sin restricción | MT | No necesariamente |

La jerarquía es estricta: cada nivel contiene estrictamente al anterior.

## Autómata de pila (PDA)

Un PDA es una NFA con una pila infinita. La transición depende del estado actual, el símbolo leído y el tope de la pila. La pila permite contar y verificar estructuras anidadas.

**Ejemplo de PDA para $\{a^n b^n\}$:**
- Estado inicial $q_0$.
- Al leer $a$: empujar $A$ en la pila.
- Al leer $b$ con $A$ en el tope: desapilar (cada $b$ consume una $a$).
- Aceptar si la pila queda vacía al terminar la cadena.

**No determinismo en PDA:** a diferencia de los DFA, los PDA no deterministas son estrictamente más potentes que los deterministas para lenguajes libres de contexto. El lenguaje $\{ww^R : w \in \{a,b\}^*\}$ (palíndromos) es libre de contexto y solo reconocible por un NPDA (no determinista).

## El pumping lemma para cada nivel

**Pumping lemma para lenguajes regulares:** si $L$ es regular, existe $p$ tal que toda cadena $w \in L$ con $|w| \geq p$ puede dividirse como $w = xyz$ con $|xy| \leq p$, $|y| \geq 1$ y $xy^iz \in L$ para todo $i \geq 0$.

**Uso:** demostrar que un lenguaje no es regular encontrando una cadena que no puede "bombearse". Por ejemplo, $\{a^n b^n\}$: elegir $w = a^p b^p$; cualquier $y$ con $|xy| \leq p$ solo contiene $a$s; bombeando $y$ se obtiene más $a$s que $b$s, contradicción.

**Pumping lemma para libres de contexto:** análogo pero con divisiones en cinco partes $w = uvxyz$, donde $vxy$ es la parte bombeada. Permite demostrar que $\{a^n b^n c^n\}$ no es libre de contexto.

## Conexión con expresiones regulares

Las expresiones regulares son otra forma de describir lenguajes regulares. El teorema de Kleene establece la equivalencia:

**Lenguaje regular ↔ expresión regular ↔ DFA**

Las tres descripciones son intercambiables: un DFA puede convertirse en una expresión regular, y una expresión regular puede compilarse en un DFA. Esta es la base del matching de patrones (`grep`, `re` en Python, expresiones regulares en cualquier lenguaje de programación).

Ejemplo: la expresión regular `(a|b)*abb` describe el lenguaje de cadenas sobre $\{a,b\}$ que terminan en `abb`. El DFA equivalente tiene 4 estados.

## Ideas clave

- La jerarquía de Chomsky clasifica lenguajes según la complejidad de sus gramáticas: regular ⊂ libre de contexto ⊂ sensible al contexto ⊂ recursivamente enumerable.
- A cada nivel corresponde un modelo de autómata: DFA, PDA, LBA, MT.
- Los pumping lemas son la herramienta estándar para demostrar que un lenguaje no pertenece a un nivel dado.
- Las gramáticas libres de contexto describen la sintaxis de la mayoría de lenguajes de programación.
- La expresión regular y el DFA son dos caras del mismo concepto: los lenguajes regulares.

## Ejercicios

1. Diseñar una CFG para el lenguaje de cadenas de la forma $a^i b^j c^k$ con $i = j$ o $j = k$ (o ambos).
2. Demostrar que $L = \{a^n b^n c^n : n \geq 1\}$ no es libre de contexto usando el pumping lemma para CFG.
3. Convertir la expresión regular `(0|1)*10(0|1)*` en un NFA y luego en un DFA.
4. Diseñar un PDA que reconozca el lenguaje de paréntesis bien anidados sobre `{(, )}`.
5. ¿Cuál es el nivel mínimo en la jerarquía de Chomsky del lenguaje $\{ww : w \in \{a,b\}^*\}$? Justificar.


<!-- nav-start -->

---
← [05 - Autómatas finitos y lenguajes regulares](05-automatas-finitos-y-lenguajes-regulares.md) · [Universalidad y Autorreferencia](07-universalidad-y-autorreferencia.md) →

<!-- nav-end -->
## Referencias

- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., capítulos 1, 2 y 5.
- Hopcroft, J.E., Motwani, R. y Ullman, J.D. (2007). *Introduction to Automata Theory, Languages, and Computation*, 3ª ed.
- Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory*, 2(3), 113–124.

## Véase también

- [Autómatas de pila y lenguajes libres de contexto](09-automatas-de-pila-y-lenguajes-contexto-libre.md) — los PDA son exactamente la cara operacional de las gramáticas libres de contexto: el teorema de equivalencia CFG ↔ PDA cierra el cuadro de esta jerarquía.
- [Autómatas finitos y lenguajes regulares](05-automatas-finitos-y-lenguajes-regulares.md) — el nivel más bajo de la jerarquía; los expresiones regulares y los DFA son la herramienta práctica de las gramáticas de tipo 3.
- [Complejidad descriptiva](08-complejidad-descriptiva.md) — la lógica de primer orden captura exactamente los lenguajes en PTIME; una conexión profunda con la jerarquía de Chomsky.
