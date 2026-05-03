# 05 - Divergencia KL y entropía cruzada

La entropía mide incertidumbre de una distribución. La información mutua mide
dependencia entre variables. La divergencia de Kullback-Leibler, o divergencia
KL, compara dos distribuciones de probabilidad.

Esta comparación es central en estadística, aprendizaje automático, compresión y
modelado probabilístico.

## Dos distribuciones

Supongamos que una fuente real sigue una distribución `P`, pero usamos un modelo
`Q` para describirla.

La pregunta es:

```text
¿cuánto perdemos por usar Q cuando la distribución real es P?
```

Si `Q` se parece mucho a `P`, la pérdida será pequeña. Si `Q` asigna
probabilidades muy distintas, la pérdida será grande.

## Entropía cruzada

La entropía cruzada de `P` respecto de `Q` es:

```text
H(P, Q) = - sum_x P(x) log2 Q(x)
```

Puede interpretarse como la longitud media de código si los datos vienen de `P`,
pero usamos un código optimizado para `Q`.

Si `Q` es un mal modelo de `P`, necesitaremos más bits en promedio.

## Divergencia KL

La divergencia KL se define como:

```text
D_KL(P || Q) = sum_x P(x) log2(P(x) / Q(x))
```

También puede escribirse como:

```text
D_KL(P || Q) = H(P, Q) - H(P)
```

Es el exceso de bits por usar `Q` en lugar de `P`.

## No es una distancia ordinaria

Aunque compara distribuciones, la divergencia KL no es una distancia en sentido
matemático estricto.

En general:

```text
D_KL(P || Q) != D_KL(Q || P)
```

La dirección importa. No es lo mismo medir el coste de aproximar `P` con `Q` que
aproximar `Q` con `P`.

## Caso de probabilidad cero

Si `P(x) > 0` pero `Q(x) = 0`, entonces `Q` declara imposible un evento que sí
puede ocurrir bajo `P`.

En ese caso:

```text
D_KL(P || Q) = infinito
```

Esto refleja una penalización extrema: un modelo que asigna probabilidad cero a
un evento real no puede codificarlo correctamente.

## Ejemplo simple

Sea:

```text
P(cara) = 0.5
P(cruz) = 0.5
```

y:

```text
Q(cara) = 0.9
Q(cruz) = 0.1
```

`Q` espera una moneda muy sesgada. Si la moneda real es equilibrada, usar `Q`
como modelo será ineficiente.

La divergencia KL cuantifica esa ineficiencia.

## Aprendizaje automático

En clasificación probabilística, un modelo produce una distribución `Q` sobre
clases posibles. La etiqueta real puede verse como una distribución `P` que pone
toda la probabilidad en la clase correcta.

Minimizar entropía cruzada empuja al modelo a asignar alta probabilidad a la
clase correcta.

Por eso la entropía cruzada aparece como función de pérdida en muchos modelos de
clasificación.

## Relación con compresión

Si conocemos la distribución real de una fuente, podemos diseñar códigos
eficientes. Si usamos una distribución aproximada, aparece un coste adicional.

Ese coste adicional promedio es exactamente lo que mide la divergencia KL.

Así, comparar modelos probabilísticos también puede entenderse como comparar
costes de codificación.

## Idea para recordar

La entropía cruzada mide cuánto cuesta codificar datos reales usando un modelo.
La divergencia KL mide el exceso de coste frente al modelo ideal.

## Ejercicios

1. ¿Por qué `D_KL(P || Q)` no suele ser igual a `D_KL(Q || P)`?
2. Explica qué ocurre si `Q(x) = 0` para un evento con `P(x) > 0`.
3. Interpreta la entropía cruzada como longitud media de código.
4. Da un ejemplo de modelo probabilístico malo para una fuente real.
