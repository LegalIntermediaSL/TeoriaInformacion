# 03 - Reducciones e indecidibilidad

Las reducciones no solo sirven para comparar dificultad computacional. En
computabilidad son una herramienta fundamental para demostrar que ciertos
problemas son indecidibles.

La idea es transportar una imposibilidad conocida hacia un problema nuevo.

## Recordatorio: el problema de la parada

El problema de la parada pregunta si un programa `P` termina al ejecutarse con
una entrada `x`:

```text
HALT(P, x)
```

Sabemos que no existe un algoritmo general que decida correctamente este problema
para todos los programas y todas las entradas.

Este resultado funciona como punto de partida para muchas otras demostraciones.

## Reducción entre problemas

Para demostrar que un problema `B` es indecidible, podemos reducir un problema
indecidible conocido `A` a `B`.

La estructura del argumento es:

```text
si B fuera decidible, entonces A también sería decidible
pero A no es decidible
por tanto, B no puede ser decidible
```

La reducción construye una forma de usar un supuesto decisor de `B` para resolver
`A`.

## Dirección correcta

La dirección es crucial. Si queremos probar que `B` es indecidible, necesitamos:

```text
A <= B
```

donde `A` ya sabemos que es indecidible.

Reducir `B` a `A` no demuestra que `B` sea indecidible. Solo diría que `B` puede
resolverse usando una herramienta imposible para `A`, lo cual no aporta una
contradicción.

## Ejemplo informal: programas que imprimen algo

Consideremos el problema:

```text
PRINTS(P) = ¿el programa P imprime algún símbolo?
```

Para mostrar por qué puede ser indecidible, imaginemos que tuviéramos un decisor
perfecto para `PRINTS`.

Dado un par `(P, x)`, podemos construir un programa `Q` que:

1. ejecuta `P(x)`;
2. si `P(x)` termina, imprime `ok`;
3. si `P(x)` no termina, nunca imprime nada.

Entonces:

```text
Q imprime algo si y solo si P(x) termina
```

Un decisor para `PRINTS` permitiría decidir `HALT`. Como `HALT` es indecidible,
`PRINTS` también debe serlo.

## Propiedades semánticas

Muchas propiedades interesantes de programas dependen de lo que hacen al
ejecutarse:

- si terminan;
- si imprimen algo;
- si devuelven cierto valor;
- si aceptan alguna entrada;
- si aceptan todas las entradas;
- si dos programas calculan la misma función.

Estas propiedades suelen ser difíciles porque hablan del comportamiento
semántico del programa, no solo de su texto.

## Teorema de Rice

El teorema de Rice formaliza esta intuición. Dice, de forma resumida, que toda
propiedad semántica no trivial de los programas es indecidible.

"No trivial" significa que la propiedad no es siempre verdadera ni siempre falsa
para todos los programas.

Por ejemplo, la propiedad "este programa acepta alguna cadena" es semántica y no
trivial. Por tanto, no puede haber un decisor general perfecto para ella.

## Sintaxis frente a semántica

No toda pregunta sobre programas es indecidible. Algunas propiedades sintácticas
sí pueden decidirse:

- si el programa contiene cierta palabra clave;
- si tiene paréntesis balanceados;
- si respeta una gramática simple.

La indecidibilidad aparece cuando preguntamos por el comportamiento general del
programa al ejecutarse.

## Idea para recordar

Una reducción de indecidibilidad muestra que resolver un problema nuevo
permitiría resolver uno que ya sabemos imposible. Así convertimos un límite
conocido en una familia de límites nuevos.

## Ejercicios

1. Explica la forma general de una prueba por reducción de indecidibilidad.
2. ¿Por qué importa reducir desde un problema ya indecidible?
3. Describe un programa `Q` que imprima algo solo si otro programa termina.
4. Da un ejemplo de propiedad sintáctica decidible y otro de propiedad semántica
   sospechosa de ser indecidible.
