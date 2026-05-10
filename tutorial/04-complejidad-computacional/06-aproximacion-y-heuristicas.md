# 06 - Aproximación y heurísticas

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


Que un problema sea difícil en el peor caso no significa que debamos rendirnos.
En la práctica, muchas veces aceptamos soluciones aproximadas, algoritmos
heurísticos o métodos que funcionan bien en ciertas familias de instancias.

La complejidad ayuda a entender cuándo buscamos exactitud y cuándo conviene
negociar.

## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Definir un algoritmo de aproximación de ratio α y sus garantías.
2. Analizar el algoritmo greedy para Vertex Cover (ratio 2).
3. Distinguir entre PTAS, FPTAS y los límites de la aproximabilidad.


## Soluciones exactas

Un algoritmo exacto devuelve siempre la respuesta óptima o correcta.

Para algunos problemas, esto puede requerir demasiado tiempo en entradas grandes.
Por ejemplo, una búsqueda exhaustiva puede garantizar la mejor solución, pero
explorar un número exponencial de candidatos.

## Algoritmos de aproximación

Un algoritmo de aproximación busca una solución cercana a la óptima con alguna
garantía formal.

Por ejemplo, si un problema es de minimización, un algoritmo con factor 2 produce
una solución cuyo coste es como máximo el doble del óptimo.

La garantía no dice que siempre obtengamos la solución perfecta. Dice que el
error está controlado.

## Heurísticas

Una heurística es una estrategia práctica que suele funcionar bien, aunque no
ofrezca una garantía fuerte para todos los casos.

Ejemplos:

- elegir siempre la opción localmente mejor;
- usar búsqueda aleatoria;
- reiniciar cuando una búsqueda se estanca;
- simplificar el problema;
- explotar estructura específica de los datos.

Las heurísticas pueden ser muy útiles, pero deben evaluarse con cuidado.

## Algoritmos voraces

Un algoritmo voraz toma decisiones locales que parecen buenas en el momento.

En algunos problemas, esta estrategia produce soluciones óptimas. En otros, puede
fallar.

La pregunta importante es si existe una propiedad del problema que justifique la
decisión local.

## Parámetros e instancias reales

Un problema puede ser difícil en general y manejable en instancias reales.

Esto puede ocurrir porque:

- las entradas son pequeñas;
- tienen estructura especial;
- ciertos parámetros son bajos;
- aceptamos aproximación;
- usamos preprocesamiento.

La complejidad de peor caso es un mapa de límites, no una predicción directa de
toda ejecución práctica.

## Complejidad parametrizada

La complejidad parametrizada estudia problemas usando, además del tamaño `n`, un
parámetro `k`.

Un algoritmo puede ser costoso en `k` pero casi lineal en `n`. Si `k` es pequeño
en la práctica, el método puede ser útil.

Esto permite refinar la frontera entre tratable e intratable.

## Riesgos

Las heurísticas pueden fallar silenciosamente. Un método que funciona en ejemplos
pequeños puede degradarse en casos adversos.

Por eso conviene distinguir:

- garantía formal;
- evidencia experimental;
- supuestos sobre los datos;
- tolerancia al error.

## Idea para recordar

Cuando la solución exacta es demasiado cara, podemos buscar aproximaciones,
heurísticas o parámetros que hagan útil el problema. La clave es saber qué
garantías se conservan y cuáles se abandonan.

## Ideas clave

- Un algoritmo de aproximación de ratio α garantiza que su solución está en un factor α del óptimo para toda instancia.
- Vertex Cover admite un algoritmo greedy de ratio 2 (matching maximal); el teorema PCP y la UGC sugieren que 2−ε es inalcanzable.
- Un PTAS (Polynomial-Time Approximation Scheme) da ratio 1+ε para cualquier ε>0 fijo, con tiempo polinomial en n.
- Un FPTAS además es polinomial en 1/ε; existe para Mochila pero no para TSP general (salvo P=NP).
- El teorema PCP implica que MAX-3SAT, MAX-Clique e IS no pueden aproximarse más allá de ciertos ratios constantes bajo P≠NP.


## Ejercicios

1. Explica la diferencia entre algoritmo exacto y heurística.
2. ¿Qué significa una aproximación con factor 2?
3. Da un ejemplo cotidiano de decisión voraz.
4. ¿Por qué una heurística útil puede no tener garantía de peor caso?

## Véase también

- [El teorema PCP e inaproximabilidad](09-teorema-pcp.md)
- [Complejidad parametrizada](10-complejidad-parametrizada.md)

