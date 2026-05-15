# 01 - Entropía: medir incertidumbre

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


La entropía es una medida de incertidumbre. En teoría de la información, permite
cuantificar cuánta información esperamos recibir al observar el resultado de una
fuente aleatoria.

La idea intuitiva es sencilla: cuanto más impredecible es una fuente, más
información puede aportar cada observación.

## Prerrequisitos

- [Logaritmos, probabilidad y crecimiento](../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md)

## Objetivos de aprendizaje

1. Calcular la entropía de Shannon H(X) para distribuciones discretas.
2. Interpretar la entropía como medida de incertidumbre e información promedio.
3. Demostrar que la entropía se maximiza con la distribución uniforme.


## Sorpresa de un resultado

Un resultado muy probable sorprende poco. Un resultado improbable sorprende
mucho. Esta intuición se formaliza con la cantidad de información propia o
sorpresa:

```text
I(x) = -log2 p(x)
```

Si `p(x) = 1`, entonces `I(x) = 0`: el resultado era seguro y no aprendimos nada
nuevo. Si `p(x)` es pequeño, `-log2 p(x)` crece: el resultado era inesperado.

## Entropía de una fuente

La entropía de una variable aleatoria discreta `X` es la sorpresa media:

```text
H(X) = - sum_x p(x) log2 p(x)
```

La unidad es el bit cuando usamos logaritmo en base 2.

La entropía no mide la longitud de un mensaje concreto, sino la incertidumbre
promedio de la fuente que lo produce.

## Ejemplo: moneda equilibrada

Para una moneda equilibrada:

```text
P(cara) = 1/2
P(cruz) = 1/2
```

La entropía es:

```text
H(X) = -1/2 log2(1/2) - 1/2 log2(1/2) = 1 bit
```

Cada lanzamiento resuelve una elección entre dos alternativas igualmente
probables. Por eso aporta, en promedio, un bit de información.

## Ejemplo: moneda sesgada

Para una moneda muy sesgada:

```text
P(cara) = 0.9
P(cruz) = 0.1
```

La entropía es aproximadamente:

```text
H(X) = -0.9 log2(0.9) - 0.1 log2(0.1) ≈ 0.469 bits
```

La fuente sigue teniendo dos resultados posibles, pero no son igual de
inciertos. Como cara ocurre casi siempre, el promedio de información por
lanzamiento es menor que en una moneda equilibrada.

## Entropía máxima

Para un conjunto finito de `N` resultados, la entropía máxima se alcanza cuando
todos los resultados son equiprobables:

```text
p(x) = 1/N
H(X) = log2(N)
```

Esto encaja con la intuición: si todas las opciones son igualmente posibles,
antes de observar el resultado no tenemos ninguna razón para preferir una sobre
otra.

## Entropía y compresión

La entropía también puede interpretarse como un límite teórico para la
compresión sin pérdida. Si una fuente tiene baja entropía, contiene regularidad o
redundancia que puede aprovecharse para codificar sus mensajes con menos bits en
promedio.

Una fuente uniforme, en cambio, tiene menos margen de compresión. Si todos los
mensajes son igual de probables, no hay patrones probabilísticos claros que
explotar.

## Lo que la entropía no dice

La entropía no mide directamente significado, importancia o verdad. Dos mensajes
pueden tener la misma longitud y la misma probabilidad dentro de un modelo, pero
tener significados humanos completamente distintos.

La teoría de Shannon abstrae el significado para estudiar transmisión,
codificación y ruido con precisión matemática.

## Idea para recordar

La entropía mide la incertidumbre promedio de una fuente. Una fuente predecible
tiene baja entropía; una fuente impredecible tiene alta entropía.

## Ideas clave

- La entropía H(X) = −∑ p(x) log₂ p(x) mide la incertidumbre promedio de una variable aleatoria en bits.
- H(X) se maximiza con la distribución uniforme y vale 0 cuando el resultado es determinista.
- Un bit es la cantidad de información que resuelve una pregunta binaria equiprobable.
- La entropía es la cota inferior para la longitud media de cualquier código sin pérdida (primer teorema de Shannon).
- La entropía de Shannon y la entropía de Boltzmann describen la misma magnitud con un factor de escala kB ln 2.


## Ejercicios

1. Calcula la entropía de una fuente que produce cuatro símbolos equiprobables.
2. ¿Qué fuente tiene mayor entropía: una moneda equilibrada o una moneda con
   `P(cara) = 0.8`?
3. Explica por qué una fuente completamente predecible tiene entropía cero.
4. ¿Por qué la entropía se relaciona con la compresión sin pérdida?

## Véase también

- [Información mutua y divergencia KL](02-informacion-mutua.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)

<!-- nav-start -->

---
← [05 - Lógica booleana y proposicional](../01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md) · [02 - Información mutua](02-informacion-mutua.md) →

<!-- nav-end -->
