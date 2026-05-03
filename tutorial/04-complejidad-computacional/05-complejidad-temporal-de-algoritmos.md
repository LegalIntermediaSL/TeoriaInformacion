# 05 - Complejidad temporal de algoritmos

La complejidad temporal estudia cómo crece el número de pasos de un algoritmo
cuando aumenta el tamaño de la entrada. No busca medir segundos exactos, sino
comparar ritmos de crecimiento.

Esta mirada permite distinguir algoritmos que escalan bien de algoritmos que se
vuelven inviables.

## Tamaño de entrada

El tamaño de entrada suele escribirse como `n`. Puede representar:

- número de elementos en una lista;
- número de vértices de un grafo;
- número de bits de una cadena;
- número de variables de una fórmula;
- longitud de un texto.

Elegir bien qué significa `n` es parte del análisis.

## Operaciones básicas

Un análisis simple cuenta operaciones elementales:

- comparaciones;
- asignaciones;
- accesos a memoria;
- iteraciones;
- llamadas recursivas.

No siempre importa el coste exacto de cada operación. Para entradas grandes,
domina el término que crece más rápido.

## Bucles

Un bucle que recorre `n` elementos suele tener coste lineal:

```text
O(n)
```

Dos bucles anidados sobre la misma entrada suelen producir:

```text
O(n^2)
```

Tres bucles anidados pueden dar:

```text
O(n^3)
```

Estas reglas son aproximaciones, pero sirven para empezar.

## Búsqueda lineal

Buscar un elemento en una lista sin ordenar puede requerir revisar todos los
elementos:

```text
O(n)
```

En el peor caso, el elemento no está o aparece al final.

## Búsqueda binaria

Si la lista está ordenada, la búsqueda binaria divide el espacio a la mitad en
cada paso.

Su coste es:

```text
O(log n)
```

Esto muestra cómo una estructura adicional en los datos puede cambiar
radicalmente la eficiencia.

## Ordenación

Muchos algoritmos de ordenación eficientes, como mergesort o heapsort, tienen
coste:

```text
O(n log n)
```

Otros métodos simples, como insertion sort en el peor caso, pueden tener:

```text
O(n^2)
```

La diferencia se vuelve importante con entradas grandes.

## Búsqueda exhaustiva

Algunos problemas se resuelven probando todos los candidatos. Si hay `2^n`
candidatos, el coste puede ser exponencial:

```text
O(2^n)
```

Esto ocurre, por ejemplo, al probar todas las asignaciones de una fórmula booleana
con `n` variables.

## Peor caso, mejor caso y promedio

Un mismo algoritmo puede comportarse de forma distinta según la entrada.

- peor caso: coste máximo para entradas de tamaño `n`;
- mejor caso: coste mínimo;
- caso promedio: coste esperado bajo una distribución de entradas.

La complejidad teórica suele centrarse en el peor caso porque ofrece garantías.

## Idea para recordar

La complejidad temporal no pregunta cuánto tarda hoy un programa concreto, sino
cómo crecerá su coste mañana cuando la entrada sea mucho mayor.

## Ejercicios

1. ¿Qué coste tiene recorrer una lista una vez?
2. ¿Por qué dos bucles anidados suelen sugerir `O(n^2)`?
3. Explica por qué búsqueda binaria requiere datos ordenados.
4. ¿Cuántas asignaciones tiene una fórmula con 20 variables?
