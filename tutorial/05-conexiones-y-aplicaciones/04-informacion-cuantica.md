# 04 - Información cuántica

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


La información cuántica estudia cómo se representa, transforma y transmite
información en sistemas gobernados por la mecánica cuántica.

No sustituye a la teoría clásica de la información, pero la amplía con fenómenos
que no aparecen en bits ordinarios.

## Prerrequisitos

- [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)
- [Álgebra lineal básica](../01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md)

## Objetivos de aprendizaje

1. Representar qubits como vectores en C² y operar con puertas unitarias.
2. Calcular la entropía de von Neumann de una matriz densidad.
3. Explicar el protocolo de teleportación cuántica.


## Bits y qubits

Un bit clásico tiene dos valores posibles:

```text
0
1
```

Un qubit puede estar en una superposición de estados. De forma simplificada:

```text
alpha |0> + beta |1>
```

donde `alpha` y `beta` son amplitudes complejas. Al medir, obtenemos resultados
clásicos con probabilidades determinadas por esas amplitudes.

## Superposición

La superposición permite que el estado cuántico combine posibilidades. Esto no
significa que al medir obtengamos todos los resultados, sino que antes de medir
el sistema no se describe como un único valor clásico.

La potencia de la computación cuántica no viene de "probar todo a la vez" de
forma simple, sino de manipular amplitudes para amplificar respuestas útiles y
cancelar otras.

## Entrelazamiento

Dos sistemas pueden estar entrelazados de modo que el estado conjunto no se
descompone como estados independientes de cada parte.

El entrelazamiento crea correlaciones que no tienen equivalente clásico directo.
Es un recurso central en información cuántica, comunicación y computación
cuántica.

## Medición

Medir un sistema cuántico produce un resultado clásico y cambia el estado del
sistema. Por eso no podemos observar un estado cuántico arbitrario sin
perturbarlo.

Esta diferencia afecta la comunicación, la criptografía y el diseño de
algoritmos.

## No clonación

El teorema de no clonación dice que no existe una operación física general que
copie perfectamente un estado cuántico desconocido.

Esto contrasta con la información clásica, donde copiar bits es una operación
fundamental y sencilla.

La no clonación es una pieza importante en criptografía cuántica.

## Computación cuántica

Un computador cuántico manipula qubits mediante puertas cuánticas. Algunos
algoritmos cuánticos ofrecen ventajas sobre los mejores algoritmos clásicos
conocidos.

Ejemplos famosos:

- algoritmo de Shor para factorización;
- algoritmo de Grover para búsqueda no estructurada;
- simulación de sistemas cuánticos.

Estas ventajas dependen del problema y del modelo físico disponible.

## Información clásica desde sistemas cuánticos

Aunque un estado de `n` qubits necesita muchos parámetros para describirse
matemáticamente, al medir obtenemos solo información clásica limitada.

Esto evita interpretaciones ingenuas: la dimensión del estado cuántico no
significa que podamos extraer arbitrariamente una cantidad exponencial de bits.

## Relación con el tutorial

La información cuántica conecta con:

- teoría de la información, por comunicación y entropía;
- computabilidad, por modelos de cálculo;
- complejidad, por clases como `BQP`;
- criptografía, por seguridad basada en principios físicos.

Es una extensión natural del mapa general.

## Idea para recordar

La información cuántica muestra que la forma física de representar información
importa. Qubits, medición, entrelazamiento y no clonación cambian las reglas de
procesamiento y transmisión.

## Ideas clave

- Un qubit es un vector unitario en ℂ², representado como |ψ⟩ = α|0⟩ + β|1⟩ con |α|²+|β|² = 1.
- La entropía de von Neumann S(ρ) = −tr(ρ log ρ) es la extensión cuántica de la entropía de Shannon.
- El entrelazamiento cuántico es un recurso sin análogo clásico: no puede crearse por operaciones locales y comunicación clásica (LOCC).
- La teleportación cuántica transfiere un estado desconocido usando un par de Bell y 2 bits clásicos, sin violar la relatividad.
- La criptografía cuántica (QKD, BB84) ofrece seguridad basada en física cuántica, no en complejidad computacional.


## Ejercicios

1. Explica la diferencia entre bit y qubit sin usar fórmulas avanzadas.
2. ¿Por qué medir un sistema cuántico no es como leer una variable clásica?
3. ¿Qué afirma el teorema de no clonación?
4. ¿Por qué la computación cuántica afecta a ciertas hipótesis criptográficas?

## Véase también

- [Criptografía y complejidad](02-criptografia-y-complejidad.md)
- [Información y termodinámica](06-informacion-y-termodinamica.md)

<!-- nav-start -->

---
← [03 - Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md) · [Información en el Aprendizaje Estadístico](05-informacion-en-aprendizaje.md) →

<!-- nav-end -->
