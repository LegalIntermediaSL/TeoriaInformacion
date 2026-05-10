# 04 - Canales discretos y capacidad

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


Un canal de comunicación modela cómo se transforma un símbolo enviado en un
símbolo recibido. Puede introducir ruido, errores o pérdida de información.

La teoría de la información permite preguntar cuánto puede transmitirse de forma
fiable a través de un canal.

## Prerrequisitos

- [Información mutua](02-informacion-mutua.md)

## Objetivos de aprendizaje

1. Modelar un canal de comunicación ruidoso con una matriz de transición.
2. Calcular la capacidad de canal C = max I(X;Y).
3. Aplicar el límite de Shannon a canales binarios simétricos.


## Entrada y salida

Un canal discreto tiene un conjunto de símbolos de entrada y un conjunto de
símbolos de salida. Se describe mediante probabilidades condicionales:

```text
P(Y = y | X = x)
```

Esto significa: si enviamos `x`, ¿con qué probabilidad recibimos `y`?

La variable `X` representa lo enviado. La variable `Y` representa lo recibido.

## Canal sin ruido

En un canal ideal, cada símbolo se recibe exactamente como fue enviado:

```text
P(Y = x | X = x) = 1
```

En ese caso, observar `Y` determina completamente `X`. La información mutua
entre entrada y salida es máxima para la distribución de entrada elegida.

## Canal binario simétrico

El canal binario simétrico es uno de los modelos más simples. Su entrada y salida
son bits. Con probabilidad `p`, el canal invierte el bit:

```text
0 -> 1
1 -> 0
```

Con probabilidad `1 - p`, lo deja igual.

Si `p = 0`, no hay ruido. Si `p = 0.5`, la salida no conserva información útil
sobre la entrada.

## Información mutua del canal

La información mutua:

```text
I(X; Y)
```

mide cuánto nos dice la salida `Y` sobre la entrada `X`.

Si el canal es ruidoso, `H(X | Y)` aumenta: después de observar la salida todavía
queda incertidumbre sobre lo enviado. Por tanto, la información mutua disminuye.

## Capacidad de canal

La capacidad de un canal es la máxima información mutua entre entrada y salida,
optimizando la distribución de entrada:

```text
C = max P(X) I(X; Y)
```

Intuitivamente, la capacidad mide cuántos bits de información pueden transmitirse
por uso del canal en el mejor caso.

Para el canal binario simétrico:

```text
C = 1 - H_b(p)
```

donde `H_b(p)` es la entropía binaria.

## Ruido y redundancia

Si el canal introduce errores, podemos añadir redundancia al mensaje. Por
ejemplo, repetir bits o usar códigos correctores de errores.

La redundancia no aumenta la información original, pero ayuda al receptor a
detectar o corregir errores.

El desafío es equilibrar dos objetivos:

- transmitir muchos datos;
- mantener baja la probabilidad de error.

## Teorema de codificación de canal

El teorema de codificación de canal de Shannon dice, de forma informal, que si
transmitimos por debajo de la capacidad del canal, existen códigos que permiten
hacer la probabilidad de error tan pequeña como queramos usando bloques largos.

Si intentamos transmitir por encima de la capacidad, no hay estrategia que evite
errores de forma fiable.

Este resultado separa lo posible de lo imposible en comunicación con ruido.

## Idea para recordar

Un canal ruidoso reduce la información que la salida conserva sobre la entrada.
La capacidad mide el máximo ritmo fiable de transmisión que el canal permite.

## Ideas clave

- Un canal discreto sin memoria se describe por su probabilidad de transición P(y|x) entre entrada x y salida y.
- La capacidad C = max_{P(x)} I(X;Y) es la máxima tasa de información transmisible con error arbitrariamente pequeño.
- El canal binario simétrico (BSC) con crossover p tiene capacidad C = 1 − H_b(p) bits por uso.
- El canal de borrado binario (BEC) con probabilidad ε tiene capacidad C = 1−ε; ideal para analizar LDPC.
- La capacidad es una propiedad del canal, no del código; el teorema de Shannon garantiza que existe un código que la alcanza.


## Ejercicios

1. ¿Qué ocurre con la capacidad de un canal binario simétrico cuando `p = 0`?
2. ¿Por qué `p = 0.5` destruye la información útil en un canal binario
   simétrico?
3. Explica la diferencia entre añadir redundancia y añadir información nueva.
4. Da un ejemplo cotidiano de canal con ruido.

## Véase también

- [Teorema de Shannon y capacidad](08-teorema-de-shannon-capacidad.md)
- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)

