# 05 - Lógica booleana y proposicional

La lógica booleana es el lenguaje de las proposiciones que pueden ser verdaderas
o falsas. Aparece en circuitos, condiciones de programas, satisfacibilidad,
verificación y muchas reducciones de complejidad.

Antes de estudiar SAT con más detalle, conviene fijar sus piezas básicas.

## Valores de verdad

Una proposición booleana toma uno de dos valores:

```text
verdadero
falso
```

Podemos representarlos como:

```text
True
False
```

o también como:

```text
1
0
```

según el contexto.

## Variables proposicionales

Una variable proposicional representa una afirmación cuyo valor puede cambiar:

```text
x
y
z
```

Una asignación da un valor concreto a cada variable:

```text
x = verdadero
y = falso
z = verdadero
```

Evaluar una fórmula significa calcular su valor bajo una asignación.

## Operadores básicos

Los operadores más comunes son:

```text
not x      negación
x and y    conjunción
x or y     disyunción
```

La negación invierte el valor de verdad. La conjunción exige que ambas partes
sean verdaderas. La disyunción exige que al menos una parte sea verdadera.

## Tablas de verdad

Una tabla de verdad enumera todas las asignaciones posibles y el valor de una
fórmula en cada una.

Para `x and y`:

```text
x      y      x and y
F      F      F
F      T      F
T      F      F
T      T      T
```

Si una fórmula tiene `n` variables, su tabla de verdad tiene:

```text
2^n
```

filas.

## Implicación

La implicación:

```text
x -> y
```

se lee "si x, entonces y". Solo es falsa cuando `x` es verdadera e `y` es falsa.

Puede escribirse usando `or` y `not`:

```text
x -> y  equivale a  (not x) or y
```

Esta equivalencia permite traducir operadores a formas más simples.

## Equivalencia lógica

Dos fórmulas son lógicamente equivalentes si tienen el mismo valor para toda
asignación.

Por ejemplo, por las leyes de De Morgan:

```text
not (x and y)  equivale a  (not x) or (not y)
not (x or y)   equivale a  (not x) and (not y)
```

Las equivalencias son útiles para transformar fórmulas sin cambiar su significado.

## Forma normal conjuntiva

Una fórmula está en forma normal conjuntiva, o CNF, si es una conjunción de
cláusulas, y cada cláusula es una disyunción de literales.

Ejemplo:

```text
(x or not y) and (y or z) and (not x or not z)
```

SAT suele estudiarse sobre fórmulas en CNF porque esta forma es estructurada y
facilita reducciones.

## Circuitos booleanos

Una fórmula booleana también puede verse como un circuito de puertas lógicas:

- puertas `and`;
- puertas `or`;
- puertas `not`.

Los circuitos conectan lógica con computación física y con clases de complejidad
basadas en tamaño y profundidad de circuitos.

## Idea para recordar

La lógica booleana permite convertir afirmaciones en objetos manipulables. SAT,
circuitos, verificadores y reducciones usan este lenguaje para hablar de
condiciones que pueden satisfacerse o no.

## Ejercicios

1. Construye la tabla de verdad de `x or y`.
2. Verifica con una tabla la ley `not (x and y) = (not x) or (not y)`.
3. Escribe la implicación `x -> y` usando solo `not` y `or`.
4. Convierte una condición cotidiana en una fórmula booleana.
