# 03 - Combinatoria y conteo

> **Dificultad:** ⭐ Básico · **Tiempo de lectura:** ~20 min


La combinatoria estudia cómo contar objetos discretos. En este tutorial aparece
cada vez que queremos saber cuántos mensajes son posibles, cuántas cadenas hay
de cierta longitud, cuántas configuraciones debe explorar un algoritmo o cuántos
certificados podrían existir para un problema.

Contar bien es una forma de medir tamaño. Y medir tamaño es el primer paso para
hablar de información y complejidad.

## Prerrequisitos

- [Logaritmos, probabilidad y crecimiento](01-logaritmos-probabilidad-y-crecimiento.md)

## Objetivos de aprendizaje

1. Calcular permutaciones y combinaciones con y sin repetición.
2. Aplicar el principio de inclusión-exclusión y el principio del palomar.
3. Estimar el tamaño de espacios combinatorios relevantes en información y complejidad.


## Regla del producto

Si una elección puede hacerse de `a` formas y, después de ella, otra elección
puede hacerse de `b` formas, entonces el número total de pares de elecciones es:

```text
a * b
```

Por ejemplo, si un alfabeto tiene 2 símbolos y queremos formar cadenas de
longitud 3, tenemos:

```text
2 * 2 * 2 = 2^3 = 8
```

cadenas posibles.

## Cadenas sobre un alfabeto

Si un alfabeto `Sigma` tiene `k` símbolos, el número de cadenas de longitud `n`
es:

```text
k^n
```

Para un alfabeto binario:

```text
Sigma = {0, 1}
```

hay:

```text
2^n
```

cadenas binarias de longitud `n`.

Esta fórmula aparece constantemente en teoría de la información: para distinguir
entre `2^n` posibilidades hacen falta `n` bits.

## Conteo y bits

El vínculo entre conteo e información es directo. Si hay `N` posibilidades
equiprobables, la cantidad de bits necesaria para identificar una de ellas es:

```text
log2(N)
```

Si `N = 2^n`, entonces:

```text
log2(2^n) = n
```

Por eso una cadena binaria de longitud `n` puede nombrar `2^n` posibilidades.

## Permutaciones

Una permutación es una ordenación de elementos distintos.

Si tenemos `n` elementos distintos, el número de formas de ordenarlos es:

```text
n! = n * (n - 1) * ... * 2 * 1
```

Por ejemplo, tres elementos `a`, `b`, `c` pueden ordenarse de:

```text
3! = 6
```

formas distintas.

El factorial crece muy rápido. Esta es una de las razones por las que muchos
problemas de búsqueda combinatoria se vuelven intratables.

## Combinaciones

Una combinación selecciona elementos sin importar el orden.

El número de formas de elegir `k` elementos de un conjunto de `n` elementos es:

```text
C(n, k) = n! / (k! (n-k)!)
```

También se escribe:

```text
binom(n, k)
```

Esta cantidad aparece en problemas como elegir subconjuntos, formar comités,
seleccionar variables o analizar certificados.

## Subconjuntos

Todo elemento de un conjunto puede estar o no estar en un subconjunto. Si el
conjunto tiene `n` elementos, hay:

```text
2^n
```

subconjuntos posibles.

Esto conecta directamente con problemas como `SUBSET-SUM`: una búsqueda
exhaustiva sobre todos los subconjuntos de `n` números tiene, en principio,
`2^n` candidatos.

## Explosión combinatoria

La explosión combinatoria ocurre cuando el número de posibilidades crece tan
rápido que enumerarlas deja de ser viable.

Por ejemplo:

```text
2^10  = 1 024
2^30  ≈ 1 000 millones
2^100 ≈ 1.27 x 10^30
```

Un algoritmo que pruebe todas las posibilidades puede funcionar en ejemplos
pequeños y fracasar por completo cuando la entrada crece.

## Conteo y límites

En computabilidad, el conteo ayuda a demostrar que hay más problemas posibles
que programas posibles bajo ciertas codificaciones. En complejidad, ayuda a
entender por qué la búsqueda exhaustiva puede ser inviable. En información,
ayuda a convertir número de posibilidades en número de bits.

La combinatoria es una herramienta silenciosa: muchas veces no aparece como
protagonista, pero sostiene los argumentos.

## Idea para recordar

Contar posibilidades permite medir información y estimar costes. Cuando el
número de candidatos crece como `2^n` o `n!`, la búsqueda directa suele volverse
impracticable.

## Ideas clave

- El principio de la multiplicación: si A tiene m opciones y B tiene n, el total de pares es m·n.
- Permutaciones (orden importa) y combinaciones (orden no importa) son los dos bloques básicos del conteo.
- El principio de inclusión-exclusión evita doble conteo: |A∪B| = |A|+|B|−|A∩B|.
- El principio del palomar: si n+1 objetos caben en n casillas, alguna casilla tiene al menos dos objetos; fundamental en teoría de códigos.
- El coeficiente binomial C(n,k) cuenta subconjuntos de k elementos; el triángulo de Pascal da su estructura recursiva.


## Ejercicios

1. ¿Cuántas cadenas binarias de longitud 10 existen?
2. ¿Cuántos subconjuntos tiene un conjunto de 20 elementos?
3. Calcula `C(5, 2)` e interpreta el resultado.
4. Explica por qué probar todas las permutaciones de 15 elementos puede ser
   inviable.

## Véase también

- [Conjuntos, funciones y relaciones](02-conjuntos-funciones-y-relaciones.md)
- [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)

<!-- nav-start -->

---
← [02 - Conjuntos, funciones y relaciones](02-conjuntos-funciones-y-relaciones.md) · [04 - Grafos y estructuras discretas](04-grafos-y-estructuras-discretas.md) →

<!-- nav-end -->
