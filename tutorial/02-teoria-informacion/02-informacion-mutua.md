# 02 - Información mutua

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


La entropía mide la incertidumbre de una variable aleatoria. Pero muchas veces
queremos comparar dos variables: cuánto nos dice una sobre la otra, cuánto se
solapan sus incertidumbres o cuánta dependencia hay entre ambas.

La información mutua responde a esa pregunta. Mide la reducción promedio de
incertidumbre sobre una variable cuando observamos otra.

## Prerrequisitos

- [Entropía e incertidumbre](01-entropia-incertidumbre.md)

## Objetivos de aprendizaje

1. Calcular la información mutua I(X;Y) entre dos variables aleatorias.
2. Relacionar la información mutua con la entropía condicional y la KL.
3. Interpretar I(X;Y) como la reducción de incertidumbre de X al conocer Y.


## Intuición

Supongamos que queremos predecir si lloverá mañana. Antes de mirar nada tenemos
cierta incertidumbre. Si observamos un informe meteorológico, esa incertidumbre
puede disminuir.

La información mutua entre:

```text
X = clima real de mañana
Y = informe meteorológico de hoy
```

mide cuánto reduce `Y`, en promedio, la incertidumbre sobre `X`.

Si el informe es útil, la información mutua será positiva. Si el informe no
tiene ninguna relación con el clima real, la información mutua será cero.

## Entropía condicional

La entropía condicional mide la incertidumbre que queda sobre `X` después de
conocer `Y`.

```text
H(X | Y)
```

Si conocer `Y` permite predecir perfectamente `X`, entonces:

```text
H(X | Y) = 0
```

Si `Y` no aporta nada sobre `X`, entonces la incertidumbre no cambia:

```text
H(X | Y) = H(X)
```

## Definición de información mutua

La información mutua se define como:

```text
I(X; Y) = H(X) - H(X | Y)
```

Es decir: incertidumbre inicial menos incertidumbre restante.

También puede escribirse de forma simétrica:

```text
I(X; Y) = H(Y) - H(Y | X)
```

Por eso la información mutua no mide una dirección causal. Mide dependencia
estadística compartida.

## Casos extremos

Si `X` e `Y` son independientes, conocer una no cambia la distribución de la
otra. En ese caso:

```text
I(X; Y) = 0
```

Si `Y` determina completamente a `X`, entonces:

```text
H(X | Y) = 0
I(X; Y) = H(X)
```

Esto significa que `Y` contiene toda la información necesaria para conocer `X`.

## Ejemplo: dos copias de una moneda

Sea `X` el resultado de lanzar una moneda equilibrada y sea `Y = X`, una copia
exacta del mismo resultado.

Sabemos que:

```text
H(X) = 1 bit
H(X | Y) = 0 bits
```

Por tanto:

```text
I(X; Y) = 1 bit
```

Observar `Y` elimina toda la incertidumbre sobre `X`.

## Ejemplo: monedas independientes

Ahora supongamos que `X` e `Y` son dos lanzamientos independientes de monedas
equilibradas.

Conocer `Y` no ayuda a predecir `X`, así que:

```text
H(X | Y) = H(X) = 1 bit
I(X; Y) = 0 bits
```

Aunque ambas variables tengan entropía, no comparten información.

## Información mutua y redundancia

La información mutua permite detectar redundancia. Si dos variables dicen casi
lo mismo, comparten mucha información. Si capturan aspectos distintos de un
fenómeno, comparten poca.

Esta idea aparece en:

- compresión de datos;
- selección de variables;
- aprendizaje automático;
- análisis de canales de comunicación;
- comparación de representaciones.

## Relación con canales

En un canal de comunicación, `X` puede representar el símbolo enviado e `Y` el
símbolo recibido. Si el canal no tiene ruido, `Y` determina a `X`. Si el canal
tiene mucho ruido, `Y` dice poco sobre `X`.

La capacidad de canal se define, de forma intuitiva, como la mayor información
mutua que podemos lograr entre entrada y salida eligiendo bien la distribución
de entrada.

## Lo que no implica

Información mutua alta no significa causalidad. Dos variables pueden compartir
información porque una causa la otra, porque ambas dependen de una tercera o
porque el modelo de datos introduce una dependencia artificial.

La información mutua mide relación estadística, no explicación causal.

## Idea para recordar

La información mutua mide cuánta incertidumbre sobre una variable desaparece al
observar otra. Si dos variables son independientes, no comparten información.

## Ideas clave

- I(X;Y) = H(X) − H(X|Y) mide cuánta incertidumbre de X se elimina al conocer Y.
- La información mutua es simétrica: I(X;Y) = I(Y;X), aunque la causalidad no lo sea.
- I(X;Y) = D_KL(P_{XY} ‖ P_X P_Y): mide cuánto difiere la distribución conjunta del producto de las marginales.
- La capacidad de canal C = max_P I(X;Y) es la máxima información mutua alcanzable variando la distribución de entrada.
- El diagrama de Venn de entropías (H(X), H(Y), H(X,Y), H(X|Y), I(X;Y)) resume todas las relaciones de dependencia.


## Ejercicios

1. Si `H(X) = 3` bits y `H(X | Y) = 1` bit, calcula `I(X; Y)`.
2. Da un ejemplo cotidiano de dos variables con información mutua alta.
3. Da un ejemplo de dos variables con entropía positiva pero información mutua
   cero.
4. Explica por qué información mutua no significa necesariamente causalidad.

## Véase también

- [Divergencia KL y entropía cruzada](05-divergencia-kl-y-entropia-cruzada.md)
- [Canales discretos y capacidad](04-canales-discretos-y-capacidad.md)

<!-- nav-start -->

---
← [01 - Entropía: medir incertidumbre](01-entropia-incertidumbre.md) · [03 - Codificación de fuente](03-codificacion-de-fuente.md) →

<!-- nav-end -->
