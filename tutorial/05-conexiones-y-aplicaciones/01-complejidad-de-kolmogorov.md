# 01 - Complejidad de Kolmogorov

La entropía de Shannon mide incertidumbre promedio respecto de una fuente
probabilística. La complejidad de Kolmogorov, en cambio, pregunta por la cantidad
de información contenida en un objeto individual.

La idea central es sorprendentemente directa: una cadena contiene poca
información si puede describirse mediante un programa corto.

## Descripción mínima

Consideremos dos cadenas binarias:

```text
00000000000000000000000000000000
```

y:

```text
01101011100101000110101110100110
```

La primera tiene una descripción breve:

```text
imprime 32 ceros
```

La segunda quizá no tenga una descripción mucho más corta que escribirla tal
cual. Intuitivamente, parece más aleatoria.

La complejidad de Kolmogorov formaliza esta diferencia.

## Definición intuitiva

La complejidad de Kolmogorov de una cadena `x`, escrita `K(x)`, es la longitud
del programa más corto que imprime `x` y se detiene.

```text
K(x) = longitud del programa más corto que produce x
```

La definición depende de fijar un lenguaje o máquina universal, pero esa
dependencia solo cambia el valor por una constante. Para cadenas largas, esa
constante suele ser irrelevante en el análisis teórico.

## Compresibilidad

Una cadena es compresible si existe una descripción mucho más corta que la propia
cadena.

Por ejemplo:

```text
01010101010101010101010101010101
```

puede describirse como:

```text
repite "01" dieciseis veces
```

En cambio, una cadena sin patrones detectables puede no admitir una descripción
más corta. En ese caso decimos que es incompresible, al menos respecto del modelo
de descripción elegido.

## Aleatoriedad algorítmica

La complejidad de Kolmogorov permite definir una noción de aleatoriedad para
objetos individuales: una cadena es algorítmicamente aleatoria si no puede
comprimirse de forma significativa.

Esto conecta aleatoriedad con ausencia de patrones efectivos. No basta con que
una cadena "parezca desordenada"; la cuestión es si existe un procedimiento corto
que la genere.

## Relación con Shannon

La entropía de Shannon habla de fuentes y promedios:

```text
cuántos bits esperamos necesitar para codificar mensajes de esta fuente
```

La complejidad de Kolmogorov habla de objetos concretos:

```text
cuántos bits necesita la mejor descripción efectiva de esta cadena
```

Ambas ideas se conectan a través de la compresión, pero responden preguntas
distintas.

## Incomputabilidad

Un resultado profundo es que `K(x)` no es computable en general. No existe un
algoritmo que tome cualquier cadena `x` y devuelva exactamente la longitud del
programa más corto que la produce.

La razón se relaciona con el problema de la parada: para saber si un programa es
la descripción mínima, habría que comparar su comportamiento con el de muchos
otros programas, incluyendo programas que quizá no terminen.

Así, la complejidad de Kolmogorov conecta directamente información,
computabilidad y límites formales.

## Compresión práctica

Los compresores reales no calculan `K(x)`. Usan familias concretas de patrones:

- repeticiones;
- diccionarios;
- frecuencias estadísticas;
- estructura local;
- modelos predictivos.

Si un compresor no reduce una cadena, eso no prueba que la cadena sea
algorítmicamente aleatoria. Solo indica que no encontró patrones dentro de sus
capacidades.

## Idea para recordar

La complejidad de Kolmogorov mide la longitud de la mejor descripción efectiva
de un objeto. Una cadena es simple si tiene una explicación corta; parece
aleatoria si ninguna descripción corta la reproduce.

## Ejercicios

1. Propón una descripción corta para una cadena de 100 ceros.
2. ¿Por qué una cadena periódica suele ser compresible?
3. Explica la diferencia entre entropía de Shannon y complejidad de Kolmogorov.
4. ¿Por qué calcular exactamente `K(x)` entra en conflicto con los límites de la
   computabilidad?
