# 07 - Entropía conjunta y condicional

La entropía de una variable mide su incertidumbre. Pero muchos problemas
involucran varias variables relacionadas. Para analizarlas necesitamos entropía
conjunta y entropía condicional.

Estas nociones preparan el terreno para información mutua, canales y modelos
probabilísticos.

## Entropía conjunta

La entropía conjunta mide la incertidumbre de un par de variables aleatorias:

```text
H(X, Y)
```

Si conocemos la distribución conjunta `P(x, y)`, se define como:

```text
H(X, Y) = - sum_x sum_y P(x, y) log2 P(x, y)
```

Puede interpretarse como la incertidumbre promedio sobre el par completo
`(X, Y)`.

## Variables independientes

Si `X` e `Y` son independientes, conocer una no aporta información sobre la otra.
En ese caso:

```text
H(X, Y) = H(X) + H(Y)
```

Por ejemplo, dos lanzamientos independientes de monedas equilibradas tienen:

```text
H(X) = 1
H(Y) = 1
H(X, Y) = 2 bits
```

Hay cuatro pares igualmente probables.

## Variables dependientes

Si `Y` es una copia exacta de `X`, entonces el par `(X, Y)` no contiene el doble
de información. Basta conocer `X` para conocer `Y`.

Para una moneda equilibrada y `Y = X`:

```text
H(X) = 1
H(Y) = 1
H(X, Y) = 1 bit
```

La dependencia reduce la incertidumbre conjunta.

## Entropía condicional

La entropía condicional mide la incertidumbre que queda sobre `X` después de
conocer `Y`:

```text
H(X | Y)
```

Si `Y` determina completamente a `X`, entonces:

```text
H(X | Y) = 0
```

Si `Y` no dice nada sobre `X`, entonces:

```text
H(X | Y) = H(X)
```

## Regla de la cadena

La entropía conjunta puede descomponerse como:

```text
H(X, Y) = H(Y) + H(X | Y)
```

También:

```text
H(X, Y) = H(X) + H(Y | X)
```

Esta regla dice que la incertidumbre total puede contarse en dos pasos: primero
una variable y después la incertidumbre restante de la otra.

## Relación con información mutua

La información mutua se define como la reducción de incertidumbre:

```text
I(X; Y) = H(X) - H(X | Y)
```

También puede expresarse usando entropías conjuntas:

```text
I(X; Y) = H(X) + H(Y) - H(X, Y)
```

Si la entropía conjunta es menor que la suma de entropías, hay información
compartida.

## Canales

En un canal de comunicación, `X` es la entrada y `Y` la salida. La entropía
condicional `H(X | Y)` mide la incertidumbre sobre lo enviado después de ver lo
recibido.

Un canal sin ruido tiene baja entropía condicional. Un canal muy ruidoso deja
mucha incertidumbre residual.

## Idea para recordar

La entropía conjunta mide incertidumbre total de varias variables. La entropía
condicional mide incertidumbre restante después de observar información parcial.

## Ejercicios

1. Calcula `H(X, Y)` para dos monedas equilibradas independientes.
2. Si `Y = X`, ¿por qué `H(X, Y)` no es `H(X) + H(Y)`?
3. Explica la regla de la cadena con tus palabras.
4. Usa `I(X;Y) = H(X) + H(Y) - H(X,Y)` para explicar información compartida.
