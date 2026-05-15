# 04 - Máquinas de Turing

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


Las máquinas de Turing son uno de los modelos formales más influyentes de
computación. No fueron propuestas como un diseño práctico de hardware, sino como
una forma precisa de capturar la idea de procedimiento mecánico.

Su fuerza está en su sencillez: una cinta, una cabeza de lectura y escritura, un
conjunto finito de estados y reglas de transición.

## Prerrequisitos

- [El problema de la parada](01-problema-de-la-parada.md)

## Objetivos de aprendizaje

1. Definir formalmente una máquina de Turing y su cómputo.
2. Simular a mano una MT sencilla para un lenguaje conocido.
3. Enunciar la tesis de Church-Turing y su significado.


## Componentes

Una máquina de Turing tiene:

- una cinta dividida en celdas;
- un alfabeto de símbolos;
- una cabeza que lee y escribe una celda;
- un conjunto finito de estados;
- una función de transición;
- estados especiales de aceptación o rechazo.

La cinta puede imaginarse como ilimitada hacia la derecha, o en ambas
direcciones según la variante. Estas diferencias no cambian el poder computacional
esencial del modelo.

## Configuración

Una configuración describe el estado completo de la máquina en un instante:

- contenido de la cinta;
- posición de la cabeza;
- estado actual.

Ejecutar la máquina significa pasar de una configuración a la siguiente mediante
la regla de transición.

## Transiciones

Una transición indica qué hacer cuando la máquina está en cierto estado y lee
cierto símbolo:

```text
(estado, símbolo) -> (nuevo estado, símbolo escrito, movimiento)
```

El movimiento suele ser izquierda, derecha o quedarse en la misma celda,
dependiendo de la variante.

## Aceptar, rechazar o no terminar

Una máquina puede:

- aceptar una entrada;
- rechazar una entrada;
- ejecutarse para siempre.

Esta tercera posibilidad es crucial. La diferencia entre decidir y reconocer
depende precisamente de si exigimos que la máquina termine en todos los casos.

## Lenguajes reconocidos

Una máquina de Turing reconoce un lenguaje `L` si acepta exactamente las cadenas
que pertenecen a `L`.

Para cadenas fuera de `L`, puede rechazar o no terminar.

Una máquina decide `L` si, además, termina para todas las entradas.

## Variantes

Existen muchas variantes:

- varias cintas;
- cinta infinita en ambas direcciones;
- alfabetos distintos;
- máquinas no deterministas;
- movimiento con quedarse quieta.

Estas variantes suelen cambiar la comodidad o la eficiencia, pero no el conjunto
de problemas computables.

## Tesis de Church-Turing

La tesis de Church-Turing afirma, de forma informal, que toda función calculable
por un procedimiento efectivo puede ser calculada por una máquina de Turing.

No es un teorema matemático en sentido estricto, porque depende de la noción
informal de "procedimiento efectivo". Pero está respaldada por la equivalencia
entre muchos modelos independientes de computación.

## Máquinas universales

Una máquina de Turing universal puede recibir como entrada la descripción de otra
máquina y simular su ejecución.

Esta idea anticipa el concepto moderno de programa almacenado: los programas
pueden tratarse como datos.

También hace posible formular problemas como el de la parada.

## Idea para recordar

Las máquinas de Turing no importan por ser prácticas, sino por ser precisas.
Ofrecen un lenguaje formal para hablar de algoritmos, límites de cálculo y
programas como objetos matemáticos.

## Ideas clave

- Una máquina de Turing es una cinta infinita + cabeza lectora/escritora + tabla de transiciones; formaliza el concepto de algoritmo.
- La tesis de Church-Turing: todo proceso efectivamente computable puede simularse con una MT.
- Una MT universal (UTM) simula cualquier otra MT leyendo su descripción como parte de la entrada.
- Variantes (MT multiacinta, no deterministas, sobre enteros) son equivalentes en poder de cómputo a la MT estándar.
- El tiempo y el espacio que usa una MT en sus simulaciones importan: las diferencias dan lugar a las clases P, NP, PSPACE.


## Ejercicios

1. Enumera los componentes básicos de una máquina de Turing.
2. ¿Qué información contiene una configuración?
3. Explica la diferencia entre reconocer y decidir usando máquinas de Turing.
4. ¿Por qué una máquina universal permite tratar programas como datos?

## Véase también

- [El problema de la parada](01-problema-de-la-parada.md)
- [Universalidad y autorreferencia](07-universalidad-y-autorreferencia.md)

<!-- nav-start -->

---
← [03 - Reducciones e indecidibilidad](03-reducciones-e-indecidibilidad.md) · [05 - Autómatas finitos y lenguajes regulares](05-automatas-finitos-y-lenguajes-regulares.md) →

<!-- nav-end -->
