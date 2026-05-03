# 06 - Códigos correctores de errores

Los canales reales introducen ruido. Un bit enviado como `0` puede recibirse como
`1`, un paquete puede perderse y una señal puede deformarse.

Los códigos correctores de errores añaden redundancia controlada para detectar o
corregir errores durante la transmisión o el almacenamiento.

## Redundancia útil

La redundancia suele verse como algo que la compresión intenta eliminar. En
comunicación con ruido, sin embargo, cierta redundancia es valiosa.

Si enviamos un bit una sola vez, un error puede cambiar completamente el mensaje.
Si lo enviamos varias veces, el receptor puede comparar las copias.

Por ejemplo:

```text
0 -> 000
1 -> 111
```

Este es un código de repetición de longitud 3.

## Decodificación por mayoría

Con el código de repetición:

```text
0 -> 000
1 -> 111
```

si recibimos:

```text
001
```

podemos decodificar como `0`, porque hay más ceros que unos.

Esto corrige un error en un bloque de tres bits. Si ocurren dos errores en el
mismo bloque, la mayoría puede fallar.

## Distancia de Hamming

La distancia de Hamming entre dos cadenas de igual longitud es el número de
posiciones donde difieren.

Por ejemplo:

```text
d(000, 001) = 1
d(000, 111) = 3
```

La distancia mínima entre palabras de código determina cuántos errores pueden
detectarse o corregirse.

## Detección y corrección

Si la distancia mínima de un código es `d`, entonces:

- puede detectar hasta `d - 1` errores;
- puede corregir hasta `floor((d - 1) / 2)` errores.

El código de repetición de longitud 3 tiene distancia mínima 3. Por tanto, puede
detectar hasta 2 errores y corregir 1 error.

## Coste de la redundancia

La corrección de errores no es gratis. El código:

```text
0 -> 000
1 -> 111
```

transmite 1 bit de información usando 3 bits físicos. Su tasa es:

```text
1/3
```

Una tasa baja significa más protección, pero menos eficiencia.

El diseño de códigos busca equilibrar tasa, capacidad de corrección y coste de
decodificación.

## Relación con Shannon

El teorema de codificación de canal afirma que, por debajo de la capacidad del
canal, existen códigos que permiten transmitir con probabilidad de error
arbitrariamente pequeña usando bloques largos.

Esto no dice que cualquier código simple sea suficiente. Dice que el límite
teórico existe y que la tarea práctica consiste en construir códigos eficientes
que se acerquen a él.

## Ejemplos modernos

Los códigos correctores aparecen en muchos sistemas:

- memorias y discos;
- comunicaciones móviles;
- sondas espaciales;
- códigos QR;
- transmisión de datos por redes;
- almacenamiento distribuido.

Cada contexto impone restricciones distintas de velocidad, ruido y recursos.

## Idea para recordar

La compresión elimina redundancia para ahorrar bits. La corrección de errores
añade redundancia para resistir ruido. Ambas ideas se entienden mejor cuando se
ven como usos complementarios de la información.

## Ejercicios

1. Calcula la distancia de Hamming entre `10101` y `11100`.
2. ¿Cuántos errores puede corregir un código con distancia mínima 5?
3. Explica por qué el código de repetición de longitud 3 falla si dos bits se
   invierten.
4. Da un ejemplo de sistema cotidiano que use corrección de errores.
