# 01 - Logaritmos, probabilidad y crecimiento

> **Dificultad:** ⭐ Básico · **Tiempo de lectura:** ~15 min


Antes de estudiar entropía, computabilidad y complejidad conviene fijar tres
herramientas básicas: logaritmos, probabilidad discreta y crecimiento
asintótico. Aparecen una y otra vez porque permiten medir información, modelar
incertidumbre y comparar costes computacionales.

## Prerrequisitos

Ninguno — este artículo es punto de entrada.

## Objetivos de aprendizaje

1. Manejar con soltura el logaritmo en distintas bases y sus propiedades.
2. Calcular probabilidades básicas y aplicar el teorema de Bayes.
3. Identificar tasas de crecimiento (exponencial, polinómica, logarítmica).


## Logaritmos como medida de escala

El logaritmo responde a una pregunta simple: ¿a qué exponente hay que elevar una
base para obtener un número?

Si usamos base 2:

```text
log2(8) = 3, porque 2^3 = 8
```

En teoría de la información, la base 2 es especialmente natural porque mide en
bits. Un bit distingue entre dos posibilidades igualmente probables. Dos bits
distinguen entre cuatro posibilidades. Tres bits distinguen entre ocho.

En general, si hay `N` opciones equiprobables, hacen falta `log2(N)` bits para
identificar una opción entre ellas.

## Cambio de base

Los logaritmos en distintas bases solo difieren por un factor constante:

```text
log_b(x) = log_a(x) / log_a(b)
```

Esto importa en complejidad computacional porque, cuando estudiamos crecimiento
asintótico, los factores constantes suelen ignorarse. Por eso expresiones como
`log2(n)`, `ln(n)` o `log10(n)` pertenecen al mismo orden de crecimiento.

La base sí importa cuando queremos una interpretación concreta. En información,
base 2 significa bits; base `e` significa nats; base 10 significa dígitos
decimales.

## Probabilidad discreta

Muchos modelos iniciales trabajan con un conjunto finito o numerable de
resultados. Una variable aleatoria discreta `X` toma valores `x` con
probabilidad `p(x)`.

Las probabilidades deben cumplir:

```text
p(x) >= 0
sum_x p(x) = 1
```

Ejemplo: una moneda sesgada puede modelarse como:

```text
P(cara) = 0.9
P(cruz) = 0.1
```

Aunque hay dos resultados posibles, no contienen la misma incertidumbre que una
moneda equilibrada. Si casi siempre sale cara, observar una cara sorprende poco;
observar una cruz sorprende mucho.

## Esperanza

La esperanza es un promedio ponderado por probabilidades. Si una variable
aleatoria `X` toma valores numéricos, su esperanza es:

```text
E[X] = sum_x x p(x)
```

En teoría de la información, la entropía puede entenderse como una esperanza: el
promedio de la sorpresa asociada a cada resultado.

## Crecimiento asintótico

La complejidad computacional no suele preocuparse por el tiempo exacto en una
máquina concreta. Le interesa cómo crece el coste cuando crece el tamaño de la
entrada.

Algunos órdenes frecuentes son:

```text
O(1)       constante
O(log n)   logarítmico
O(n)       lineal
O(n log n) cuasilineal
O(n^2)     cuadrático
O(2^n)     exponencial
O(n!)      factorial
```

Para entradas pequeñas, estas diferencias pueden parecer moderadas. Para
entradas grandes, son decisivas.

## Ejemplo de comparación

Supongamos `n = 100`.

```text
log2(n)  ≈ 6.64
n        = 100
n^2      = 10 000
2^n      ≈ 1.27 x 10^30
```

Esta comparación explica por qué los algoritmos exponenciales pueden volverse
imposibles de usar incluso para tamaños de entrada relativamente modestos.

## Conexión con el resto del tutorial

Los logaritmos permiten medir información. La probabilidad permite modelar
incertidumbre. El crecimiento asintótico permite hablar de eficiencia.

Estas tres herramientas forman una pequeña gramática común para el resto del
recorrido.

## Ideas clave

- El logaritmo en base 2 es la unidad natural de la información: log₂(n) bits distinguen n equiprobables.
- Probabilidad y entropía comparten la misma base matemática; dominar P(A) y P(A|B) es imprescindible antes del módulo de información.
- Las notaciones O, Ω, Θ describen el comportamiento asintótico y son el lenguaje universal de la complejidad.
- Las funciones exponencial y logarítmica son inversas; invertir exp dará el tamaño de entradas factibles para un algoritmo.
- El teorema de Bayes es la herramienta central para razonar con incertidumbre y aparece en inferencia, codificación y aprendizaje.


## Ejercicios

1. ¿Cuántos bits hacen falta para distinguir entre 16 opciones equiprobables?
2. Calcula `log2(1024)`.
3. Ordena de menor a mayor crecimiento: `n^2`, `log n`, `2^n`, `n`.
4. Considera una moneda con `P(cara) = 0.99`. ¿Qué resultado aporta más sorpresa:
   cara o cruz?

## Véase también

- [Conjuntos, funciones y relaciones](02-conjuntos-funciones-y-relaciones.md)
- [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)

<!-- nav-start -->

---
← [Guía de rutas de profundización](../00-presentacion/02-rutas-de-profundizacion.md) · [02 - Conjuntos, funciones y relaciones](02-conjuntos-funciones-y-relaciones.md) →

<!-- nav-end -->
