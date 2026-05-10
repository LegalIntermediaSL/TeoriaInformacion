# 02 - Decidibilidad y reconocibilidad

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~15 min


El problema de la parada muestra que no todos los problemas bien definidos
pueden resolverse mediante un algoritmo general. Para precisar este límite,
conviene distinguir entre problemas decidibles y problemas reconocibles.

La diferencia parece pequeña, pero es una de las fronteras centrales de la
computabilidad.

## Prerrequisitos

- [El problema de la parada](01-problema-de-la-parada.md)

## Objetivos de aprendizaje

1. Distinguir lenguajes decidibles, reconocibles y no reconocibles.
2. Demostrar que el complemento de un lenguaje RE que no es decidible no es RE.
3. Clasificar problemas estándar en la jerarquía de decidibilidad.


## Problemas como lenguajes

Cuando codificamos las entradas como cadenas, un problema de decisión puede verse
como un lenguaje:

```text
L subset Sigma*
```

Una cadena `w` pertenece a `L` si la respuesta del problema para `w` es "sí".
No pertenece a `L` si la respuesta es "no".

Decidir un problema equivale a decidir pertenencia:

```text
w in L ?
```

## Decidibilidad

Un lenguaje `L` es decidible si existe un algoritmo que, para toda entrada `w`:

- termina siempre;
- acepta si `w in L`;
- rechaza si `w notin L`.

La palabra clave es "siempre". El algoritmo no puede quedarse pensando para
siempre en los casos negativos ni en los positivos.

## Reconocibilidad

Un lenguaje `L` es reconocible si existe un algoritmo que:

- acepta si `w in L`;
- puede rechazar o quedarse ejecutando para siempre si `w notin L`.

En otras palabras, el algoritmo es fiable cuando encuentra un caso positivo,
pero quizá nunca logre confirmar algunos casos negativos.

## Diferencia intuitiva

Imaginemos una lista infinita que va enumerando soluciones válidas. Si una
entrada pertenece al lenguaje, tarde o temprano aparecerá una evidencia y el
algoritmo podrá aceptar.

Pero si la entrada no pertenece, quizá nunca aparezca nada que permita estar
seguros de que no aparecerá más adelante.

Reconocer es poder confirmar los "sí". Decidir es poder confirmar tanto los "sí"
como los "no".

## Todo decidible es reconocible

Si un lenguaje es decidible, entonces también es reconocible. Basta usar el
mismo algoritmo decisor:

- si acepta, aceptamos;
- si rechaza, rechazamos.

Como el decisor siempre termina, también cumple la condición de reconocer los
casos positivos.

La implicación contraria no siempre vale: hay lenguajes reconocibles que no son
decidibles.

## El lenguaje de la parada

Podemos definir el lenguaje:

```text
HALT = {(P, x) : el programa P termina con entrada x}
```

Este lenguaje es reconocible: podemos simular `P(x)`. Si termina, aceptamos.

Pero no es decidible: si `P(x)` no termina, la simulación tampoco terminará. El
problema de la parada demuestra que no existe un método general para detectar
siempre esos casos negativos.

## Complementos

El complemento de un lenguaje `L` contiene todas las cadenas que no están en `L`:

```text
complemento(L) = {w : w notin L}
```

Un resultado importante dice:

```text
L es decidible si y solo si L y complemento(L) son reconocibles
```

La intuición es que podemos ejecutar ambos reconocedores en paralelo. Si `w`
pertenece a `L`, aceptará el primero. Si no pertenece, aceptará el reconocedor
del complemento. En cualquiera de los dos casos obtenemos una respuesta.

## Semidecisión

A veces se usa la palabra semidecidible como sinónimo de reconocible. El nombre
subraya que solo tenemos la mitad de un decisor completo: podemos confirmar los
casos positivos, pero no siempre los negativos.

Este matiz es importante en lógica, verificación automática y análisis de
programas.

## Idea para recordar

Decidir exige terminar siempre con una respuesta correcta. Reconocer solo exige
terminar cuando la respuesta es afirmativa. Entre ambas nociones vive buena
parte de la teoría de la computabilidad.

## Ideas clave

- Un lenguaje L es decidible si existe una MT que acepta si w∈L y rechaza si w∉L, siempre terminando.
- Un lenguaje es reconocible (RE) si hay una MT que acepta todas las palabras del lenguaje pero puede no terminar para las que no están.
- L es decidible ↔ L y su complemento L̄ son ambos reconocibles (teorema de Kleene).
- HALT es reconocible pero no decidible; su complemento co-HALT no es reconocible.
- La jerarquía RE ⊂ co-RE ⊂ todos los lenguajes estratifica los lenguajes por su grado de computabilidad.


## Ejercicios

1. Explica con tus palabras la diferencia entre decidir y reconocer.
2. ¿Por qué todo lenguaje decidible es reconocible?
3. Describe un reconocedor para `HALT`.
4. Si un lenguaje y su complemento son reconocibles, ¿por qué el lenguaje es
   decidible?

## Véase también

- [El problema de la parada](01-problema-de-la-parada.md)
- [Reducciones e indecidibilidad](03-reducciones-e-indecidibilidad.md)

