# 05 - SAT y verificación de asignaciones

## Contexto

Este ejercicio acompaña los artículos:

- [Lógica booleana y proposicional](../../01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md)
- [SAT y 3-SAT](../../04-complejidad-computacional/03-sat-y-3-sat.md)

También se puede practicar con:

- [Búsqueda exhaustiva para SAT](../../cuadernos/ejercicios/04-busqueda-sat.ipynb)
- [Tablas de verdad](../../cuadernos/ejercicios/07-tablas-de-verdad.ipynb)

## Enunciado

Considera la fórmula:

```text
(x or y) and (not x or z) and (not y or z)
```

1. Verifica si la asignación `x = verdadero`, `y = verdadero`, `z = verdadero`
   satisface la fórmula.
2. Verifica si `x = verdadero`, `y = falso`, `z = falso` la satisface.
3. Explica por qué este tipo de verificación es eficiente.
4. ¿Cuántas asignaciones posibles hay para `n` variables?

## Pista

Una fórmula en CNF se satisface si todas sus cláusulas son verdaderas.

Una cláusula con `or` es verdadera si al menos uno de sus literales es verdadero.

## Solución

### Primera asignación

```text
x = verdadero
y = verdadero
z = verdadero
```

Evaluamos cada cláusula:

```text
(x or y)       = verdadero or verdadero = verdadero
(not x or z)   = falso or verdadero = verdadero
(not y or z)   = falso or verdadero = verdadero
```

Todas las cláusulas son verdaderas. La fórmula se satisface.

### Segunda asignación

```text
x = verdadero
y = falso
z = falso
```

Evaluamos:

```text
(x or y)       = verdadero or falso = verdadero
(not x or z)   = falso or falso = falso
(not y or z)   = verdadero or falso = verdadero
```

La segunda cláusula es falsa, así que la fórmula completa es falsa.

### Verificación eficiente

Verificar una asignación consiste en recorrer las cláusulas y evaluar sus
literales. Si la fórmula tiene `m` cláusulas y cada cláusula tiene longitud
acotada, el coste es proporcional a `m`.

Por eso SAT está en NP: si alguien entrega una asignación candidata, podemos
verificarla en tiempo polinómico.

### Número de asignaciones

Cada variable booleana tiene dos valores posibles. Para `n` variables hay:

```text
2^n
```

asignaciones.

## Comentario

La diferencia entre verificar y encontrar es el corazón de NP. Verificar una
solución puede ser rápido aunque encontrarla requiera explorar un espacio enorme.

## Para seguir

Construye una fórmula con tres variables que no sea satisfacible.
