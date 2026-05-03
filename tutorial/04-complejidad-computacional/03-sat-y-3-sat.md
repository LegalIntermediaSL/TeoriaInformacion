# 03 - SAT y 3-SAT

SAT es uno de los problemas centrales de la complejidad computacional. Pregunta
si una fórmula booleana puede hacerse verdadera mediante alguna asignación de
valores a sus variables.

Su importancia no viene solo de su definición, sino de su papel histórico: SAT
fue el primer problema demostrado NP-completo.

## Variables y literales

Una variable booleana puede tomar dos valores:

```text
verdadero
falso
```

Un literal es una variable o su negación:

```text
x
not x
```

Una fórmula booleana combina variables con operadores como `and`, `or` y `not`.

## Satisfacibilidad

Una fórmula es satisfacible si existe una asignación de valores que la hace
verdadera.

Por ejemplo:

```text
(x or y) and (not x or z)
```

es satisfacible. Basta tomar:

```text
x = verdadero
z = verdadero
```

El valor de `y` ya no importa para que ambas cláusulas sean verdaderas.

## Forma normal conjuntiva

Una fórmula está en forma normal conjuntiva, o CNF, si es una conjunción de
cláusulas, y cada cláusula es una disyunción de literales.

Ejemplo:

```text
(x or y or not z) and (not x or z) and (not y or z)
```

Cada paréntesis es una cláusula. La fórmula completa exige que todas las
cláusulas sean verdaderas.

## El problema SAT

El problema SAT pregunta:

```text
dada una fórmula booleana, ¿existe una asignación que la haga verdadera?
```

SAT pertenece a NP porque, si alguien nos da una asignación candidata, podemos
verificar en tiempo polinómico si satisface la fórmula.

## Cook-Levin

El teorema de Cook-Levin demuestra que SAT es NP-completo.

La intuición profunda es que una fórmula booleana puede codificar la ejecución de
una máquina de cómputo acotada por tiempo polinómico. Satisfacer la fórmula
equivale a existir una ejecución válida que acepta.

Así, cualquier problema en NP puede traducirse a SAT.

## 3-SAT

3-SAT es una versión restringida de SAT donde cada cláusula tiene exactamente
tres literales:

```text
(a or b or c) and (not a or d or e) and ...
```

Aunque parece una restricción fuerte, 3-SAT también es NP-completo.

Esto es importante porque muchos otros problemas se prueban NP-completos
reduciendo desde 3-SAT.

## Por qué 2-SAT es distinto

Si cada cláusula tiene como máximo dos literales, obtenemos 2-SAT. A diferencia
de 3-SAT, 2-SAT puede resolverse en tiempo polinómico.

Este contraste muestra que pequeños cambios estructurales pueden separar
problemas tratables de problemas NP-completos.

## Búsqueda exhaustiva

Si una fórmula tiene `n` variables, hay:

```text
2^n
```

asignaciones posibles. Una búsqueda exhaustiva puede probarlas todas, pero su
coste crece exponencialmente.

SAT no es difícil porque verificar una asignación sea caro. Es difícil porque no
conocemos, en general, una forma polinómica de encontrar una asignación
satisfactoria si existe.

## Idea para recordar

SAT pregunta si existe una asignación que haga verdadera una fórmula. Es el
problema canónico de NP-completitud: verificar es fácil, encontrar puede ser
difícil.

## Ejercicios

1. Da una asignación que satisfaga `(x or y) and (not x or z)`.
2. Explica por qué SAT pertenece a NP.
3. ¿Cuántas asignaciones hay para una fórmula con 12 variables?
4. ¿Por qué el hecho de que 2-SAT esté en P no contradice que 3-SAT sea
   NP-completo?
