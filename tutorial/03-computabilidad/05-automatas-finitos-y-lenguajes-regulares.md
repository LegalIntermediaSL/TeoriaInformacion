# 05 - Autómatas finitos y lenguajes regulares

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


Los autómatas finitos son modelos de computación con memoria limitada. Son mucho
más simples que las máquinas de Turing, pero resultan fundamentales para estudiar
patrones, analizadores léxicos, expresiones regulares y protocolos sencillos.

Un autómata finito no puede recordar una cantidad arbitraria de información.
Esa limitación lo hace fácil de analizar.

## Prerrequisitos

- [Conjuntos, funciones y relaciones](../01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md)

## Objetivos de aprendizaje

1. Construir DFA y NFA para lenguajes regulares sencillos.
2. Aplicar la construcción de subconjuntos para pasar de NFA a DFA.
3. Usar el lema de bombeo para demostrar que un lenguaje no es regular.


## Estados

Un autómata finito tiene un conjunto finito de estados. En cada paso:

1. lee un símbolo de entrada;
2. cambia de estado según una regla;
3. avanza al siguiente símbolo.

Al terminar la entrada, acepta o rechaza según el estado final.

## Componentes

Un autómata finito determinista se describe mediante:

- un conjunto finito de estados;
- un alfabeto;
- un estado inicial;
- una función de transición;
- un conjunto de estados de aceptación.

La función de transición indica qué estado sigue al leer cada símbolo.

## Ejemplo: número par de unos

Queremos reconocer cadenas binarias con número par de unos.

Necesitamos dos estados:

- `par`: hemos visto una cantidad par de unos;
- `impar`: hemos visto una cantidad impar de unos.

Leer un `1` cambia de estado. Leer un `0` deja el estado igual.

El estado inicial es `par`, y también es el estado de aceptación.

## Lenguajes regulares

Un lenguaje es regular si puede ser reconocido por algún autómata finito.

Los lenguajes regulares capturan patrones que no requieren memoria ilimitada:

- cadenas que contienen cierta subcadena;
- cadenas que terminan en cierto símbolo;
- cadenas con paridad;
- tokens de muchos lenguajes de programación.

## Expresiones regulares

Las expresiones regulares describen exactamente los lenguajes regulares.

Por ejemplo:

```text
0*1*
```

describe cadenas formadas por ceros seguidos de unos.

La equivalencia entre autómatas finitos y expresiones regulares es uno de los
resultados clásicos de la teoría de lenguajes formales.

## Limitaciones

No todo lenguaje puede reconocerse con memoria finita.

Por ejemplo:

```text
L = {0^n 1^n : n >= 0}
```

requiere recordar cuántos ceros aparecieron para comparar con el número de unos.
Un autómata finito no tiene memoria suficiente para hacerlo para cualquier `n`.

## Por qué importan

Los autómatas finitos son útiles porque son simples, decidibles y eficientes.
Muchos problemas sobre ellos pueden resolverse automáticamente:

- si aceptan alguna cadena;
- si dos autómatas aceptan el mismo lenguaje;
- si una cadena pertenece al lenguaje;
- si el lenguaje es vacío.

Este contraste con máquinas de Turing ayuda a entender cómo el poder de cómputo
afecta la decidibilidad.

## Idea para recordar

Un autómata finito reconoce patrones con memoria limitada. Su simplicidad lo hace
menos poderoso que una máquina de Turing, pero mucho más manejable.

## Ideas clave

- Un DFA reconoce exactamente los lenguajes regulares; un NFA es equivalente al DFA pero puede tener transiciones no deterministas.
- La construcción de subconjuntos convierte cualquier NFA en un DFA equivalente con a lo sumo 2^n estados.
- El lema de bombeo para regulares: si L es regular y w∈L con |w|≥p, entonces w = xyz con |xy|≤p y xy^iz∈L para todo i≥0.
- Los lenguajes regulares son cerrados bajo unión, concatenación, clausura de Kleene, intersección y complemento.
- Las expresiones regulares describen exactamente los lenguajes regulares; las regexes en programación son una extensión práctica.


## Ejercicios

1. Diseña estados para reconocer cadenas binarias que terminan en `1`.
2. Explica por qué leer `0` no cambia la paridad del número de unos.
3. Da un ejemplo de patrón regular cotidiano.
4. ¿Por qué `{0^n 1^n}` no parece regular?

## Véase también

- [Gramáticas y jerarquía de Chomsky](06-gramaticas-y-jerarquia-chomsky.md)
- [Autómatas de pila y lenguajes libres de contexto](09-automatas-de-pila-y-lenguajes-contexto-libre.md)

