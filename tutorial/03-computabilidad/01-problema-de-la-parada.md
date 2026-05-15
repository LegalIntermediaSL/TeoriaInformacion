# 01 - El problema de la parada

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~15 min


El problema de la parada es uno de los resultados más importantes de la teoría
de la computabilidad. Muestra que existen preguntas perfectamente precisas que
ningún algoritmo general puede responder siempre de forma correcta.

## Prerrequisitos

- [Conjuntos, funciones y relaciones](../01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md)

## Objetivos de aprendizaje

1. Enunciar y demostrar la indecidibilidad del problema de la parada.
2. Explicar el argumento de diagonalización de Turing.
3. Distinguir entre problemas decidibles y problemas semidecidibles.


## Planteamiento

Queremos saber si existe un programa `HALT` que reciba dos entradas:

```text
HALT(programa, entrada)
```

y responda:

```text
si  -> el programa termina con esa entrada
no  -> el programa se ejecuta para siempre con esa entrada
```

La pregunta es si puede existir un procedimiento universal que decida este
comportamiento para cualquier programa y cualquier entrada.

La respuesta es no.

## Qué significa "decidir"

Un problema de decisión tiene respuestas sí/no. Decidir un problema significa
dar un algoritmo que:

- termina siempre;
- responde correctamente sí o no;
- funciona para todas las entradas válidas.

No basta con acertar en muchos casos. Tampoco basta con funcionar en programas
sencillos. El algoritmo tendría que cubrir todos los programas posibles.

## La idea de la contradicción

Supongamos, para llegar a una contradicción, que `HALT` existe.

Con ese supuesto construimos un nuevo programa `D`:

```text
D(P):
    si HALT(P, P) dice "si":
        entrar en un bucle infinito
    si HALT(P, P) dice "no":
        terminar
```

El programa `D` hace lo contrario de lo que `HALT` predice cuando un programa se
ejecuta sobre su propia descripción.

Ahora preguntamos: ¿qué ocurre con `D(D)`?

## La contradicción

Hay dos posibilidades:

1. `HALT(D, D)` dice que `D(D)` termina. Entonces, por definición, `D(D)` entra
   en un bucle infinito.
2. `HALT(D, D)` dice que `D(D)` no termina. Entonces, por definición, `D(D)`
   termina.

En ambos casos hay contradicción. Por tanto, el supuesto inicial era falso:
`HALT` no puede existir.

## Qué demuestra este resultado

El problema de la parada no dice que nunca podamos saber si un programa concreto
termina. Muchos casos particulares sí pueden analizarse.

Lo que demuestra es que no existe un algoritmo general que resuelva todos los
casos posibles. No hay una herramienta universal perfecta que pueda examinar
cualquier programa y decidir siempre si terminará.

## Consecuencias

El problema de la parada abre la puerta a otros resultados de indecidibilidad.
Una estrategia común consiste en demostrar que, si pudiéramos decidir cierto
problema nuevo, entonces podríamos decidir también el problema de la parada. Como
esto último es imposible, el problema nuevo también debe ser indecidible.

Esta técnica se llama reducción.

## Relación con la práctica

En ingeniería de software existen analizadores estáticos, verificadores y
herramientas de detección de errores. Son útiles, pero necesariamente tienen
límites. Pueden funcionar para lenguajes restringidos, propiedades concretas o
conservando aproximaciones.

El problema de la parada explica por qué ninguna herramienta puede ser, al mismo
tiempo, completamente general, siempre terminante y perfectamente precisa para
todas las propiedades relacionadas con la ejecución de programas.

## Idea para recordar

Hay problemas bien formulados que no pueden resolverse por ningún algoritmo
general. La computabilidad estudia exactamente esa frontera.

## Ideas clave

- El problema de la parada (HALT) no es decidible: no existe ningún algoritmo que determine para todo par (M,w) si M se detiene con entrada w.
- La prueba usa diagonalización: construir una máquina D que hace lo contrario a lo que predice cualquier decididor hipotético.
- Todo lenguaje decidible es reconocible, pero hay lenguajes reconocibles que no son decidibles (HALT es el ejemplo canónico).
- La indecidibilidad es una propiedad semántica: muchas preguntas sobre el comportamiento de programas son indecidibles por el teorema de Rice.
- HALT reduce a docenas de problemas prácticos (verificación formal, análisis estático, equivalencia de programas), propagando la indecidibilidad.


## Ejercicios

1. Explica con tus palabras qué tendría que hacer un supuesto algoritmo `HALT`.
2. ¿Por qué el programa `D` usa como entrada la descripción de otro programa?
3. ¿Qué significa que un problema sea indecidible?
4. Busca un ejemplo práctico donde sea útil aproximar una respuesta aunque no
   pueda existir una solución perfecta y general.

## Véase también

- [Decidibilidad y reconocibilidad](02-decidibilidad-y-reconocibilidad.md)
- [Máquinas de Turing](04-maquinas-de-turing.md)

<!-- nav-start -->

---
← [Codificación Universal: Lempel-Ziv](../02-teoria-informacion/20-codificacion-universal-lempel-ziv.md) · [02 - Decidibilidad y reconocibilidad](02-decidibilidad-y-reconocibilidad.md) →

<!-- nav-end -->
