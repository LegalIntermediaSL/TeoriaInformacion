# 02 - Reducciones polinómicas

Las reducciones son una herramienta para comparar problemas. Permiten decir que
un problema no es más difícil que otro, o que un problema concentra la dificultad
de muchos otros.

En complejidad computacional, las reducciones polinómicas son esenciales para
definir NP-completitud y para transportar resultados de dificultad entre
problemas.

## La idea básica

Supongamos que queremos resolver un problema `A`, pero ya sabemos resolver un
problema `B`. Una reducción transforma cada instancia de `A` en una instancia de
`B` de forma que la respuesta se conserve.

La forma general es:

```text
instancia de A -> transformación -> instancia de B
```

y debe cumplirse:

```text
la respuesta en A es "sí" si y solo si la respuesta transformada en B es "sí"
```

## Reducción many-one

Una reducción many-one de `A` a `B` es una función `f` tal que:

```text
x in A si y solo si f(x) in B
```

Si además `f` puede calcularse en tiempo polinómico, escribimos informalmente:

```text
A <=p B
```

Esto se lee como "`A` se reduce polinómicamente a `B`".

## Qué significa la dirección

La dirección suele ser fuente de confusión. Si:

```text
A <=p B
```

entonces resolver `B` permite resolver `A`. Por tanto, `B` es al menos tan
difícil como `A`.

La reducción no dice que `A` y `B` sean iguales. Dice que `A` puede traducirse a
`B` sin perder la respuesta y sin gastar más que tiempo polinómico.

## Por qué importa que sea polinómica

En complejidad, queremos preservar la noción de eficiencia. Si la transformación
fuera exponencial, podríamos esconder todo el coste en la reducción.

Una reducción polinómica garantiza que, si `B` tiene un algoritmo polinómico,
entonces `A` también lo tiene:

```text
resolver A = transformar a B + resolver B
```

La suma o composición de costes polinómicos sigue siendo polinómica.

## Ejemplo simple: buscar caminos

Consideremos dos problemas:

```text
PATH: ¿existe un camino de s a t en un grafo dirigido?
REACH: ¿t es alcanzable desde s en un grafo dirigido?
```

Estos problemas son esencialmente el mismo problema con nombres distintos. Una
reducción puede tomar una instancia de `PATH` y devolver la misma instancia como
instancia de `REACH`.

Este ejemplo es trivial, pero ayuda a ver que una reducción es una traducción de
instancias.

## Reducciones y NP-completitud

Para demostrar que un problema `B` es NP-completo necesitamos:

1. Probar que `B` está en NP.
2. Probar que todo problema de NP se reduce a `B`.

En la práctica, no se reduce cada problema de NP desde cero. Se usa un problema
ya conocido como NP-completo, por ejemplo `SAT`, y se demuestra:

```text
SAT <=p B
```

Como `SAT` ya representa la dificultad de todo NP, esa reducción transporta la
dificultad a `B`.

## Reducciones como traducciones de estructura

Una buena reducción no solo cambia nombres. Mapea la estructura relevante de un
problema a la estructura de otro.

Por ejemplo, una reducción desde fórmulas booleanas a grafos puede convertir:

- variables en elecciones;
- cláusulas en restricciones;
- satisfacibilidad en existencia de cierto subgrafo.

La dificultad está en diseñar una traducción que preserve exactamente los casos
"sí" y "no".

## Errores comunes

Un error común es invertir la dirección. Para demostrar que un problema nuevo
`B` es difícil, hay que reducir un problema difícil conocido a `B`, no al revés.

Otro error es construir una transformación que parece intuitiva pero no prueba
ambas direcciones del "si y solo si". Una reducción debe preservar tanto los
casos positivos como los negativos.

## Idea para recordar

Reducir `A` a `B` significa resolver `A` usando un solucionador de `B`. Si la
traducción es polinómica, la eficiencia se conserva. Por eso las reducciones son
el lenguaje central para comparar dificultad.

## Ejercicios

1. Si `A <=p B` y `B` está en P, ¿qué puedes concluir sobre `A`?
2. Si quieres demostrar que `B` es NP-difícil, ¿en qué dirección debe ir la
   reducción desde un problema NP-completo conocido?
3. Explica por qué una reducción exponencial no serviría para demostrar
   pertenencia a P.
4. Da un ejemplo informal de dos problemas que puedan verse como traducciones
   uno del otro.
