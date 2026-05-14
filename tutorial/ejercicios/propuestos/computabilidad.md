# Ejercicios propuestos — Computabilidad

Extraídos de los artículos del módulo 03.

---

## El problema de la parada (03/01)

1. Enuncia el teorema de indecidibilidad de la parada. ¿Cuál es la hipótesis que se contradice en la prueba diagonal?
2. ¿Por qué no puede existir un programa `HALT(P, x)` que devuelva siempre la respuesta correcta en tiempo finito?
3. Si modificamos el problema de la parada a "¿para toda entrada?", ¿el nuevo problema es decidible, reconocible o ninguno? Justifica.

## Decidibilidad y reconocibilidad (03/02)

4. Da un ejemplo de lenguaje: (a) decidible, (b) reconocible pero no decidible, (c) no reconocible.
5. Demuestra que el complemento de un lenguaje reconocible no tiene por qué ser reconocible.
6. Si $L$ y $\overline{L}$ son ambos reconocibles, ¿qué se puede concluir sobre $L$? Justifica con la técnica del dovetailing.

## Reducciones e indecidibilidad (03/03)

7. Usa una reducción de HALT para demostrar que el problema de "¿produce $M$ alguna salida?" es indecidible.
8. ¿Qué significa que $A \leq_m B$ (reducción muchos-a-uno)? ¿Qué se puede concluir si $B$ es decidible?
9. Demuestra que el problema de equivalencia de dos máquinas de Turing (¿aceptan el mismo lenguaje?) es indecidible.

## Máquinas de Turing (03/04)

10. Diseña una MT que acepte $\{a^n b^n \mid n \geq 1\}$ y describe sus estados y transiciones.
11. ¿Cómo simula una MT de una cinta a una MT multicinta? ¿Qué coste temporal introduce la simulación?
12. ¿Qué es una MT no determinista? ¿Cambia la clase de lenguajes que puede reconocer?

## Autómatas finitos y lenguajes regulares (03/05)

13. Construye un DFA que acepte las cadenas sobre $\{0,1\}$ cuyo valor binario es divisible por 3.
14. Aplica el lema de bombeo para demostrar que $L = \{0^n 1^n \mid n \geq 0\}$ no es regular.
15. Convierte el NFA de 4 estados que acepta cadenas que terminan en "01" a un DFA equivalente.

## Gramáticas y jerarquía de Chomsky (03/06)

16. Clasifica cada lenguaje en la jerarquía de Chomsky: $\{w \mid w \text{ es palíndromo}\}$, $\{a^n b^n c^n\}$, $\{a^*\}$.
17. Escribe una gramática libre de contexto para $\{a^n b^n \mid n \geq 0\} \cup \{a^n b^{2n} \mid n \geq 0\}$.
18. ¿Por qué la unión de dos lenguajes libres de contexto es CFL pero la intersección no tiene por qué serlo?

## Universalidad y autorreferencia (03/07)

19. ¿Qué es la máquina de Turing universal (UTM)? ¿Qué overhead introduce respecto a la máquina simulada?
20. Enuncia el teorema del punto fijo (de Kleene). Da una interpretación informal.
21. ¿Por qué el teorema de Rice implica que casi ninguna propiedad semántica de programas es decidible?

## Complejidad descriptiva (03/08)

22. Enuncia el teorema de Fagin: ¿qué clase de complejidad corresponde a $\exists$SO?
23. ¿Por qué FO (lógica de primer orden) solo captura AC0? Da un ejemplo de propiedad que FO no puede expresar.
24. ¿Qué añade el operador de punto fijo mínimo (LFP) a la lógica de primer orden? ¿Qué clase captura FO+LFP?

## Autómatas de pila y lenguajes independientes del contexto (03/09)

25. Diseña un PDA que acepte $\{a^n b^n c^n \mid n \geq 0\}$. ¿Puedes hacerlo? Razona por qué sí o no usando el lema de bombeo para CFL.
26. Describe la equivalencia entre PDA y gramáticas libres de contexto: ¿cuál es la idea de la construcción?
27. Aplica el algoritmo CYK para determinar si "aabb" pertenece a la gramática con reglas $S \to AB$, $A \to a$, $B \to b$, $A \to AS$, $B \to SB$.

## Jerarquía aritmética (03/10)

28. ¿En qué nivel de la jerarquía aritmética está el problema de la parada? ¿Y su complemento?
29. Define $\Sigma_2^0$ informalmente. Da un ejemplo de problema en $\Sigma_2^0 \setminus \Sigma_1^0$.
30. ¿Qué es el oráculo de salto $\emptyset'$? ¿Cómo se relaciona con $\Sigma_1^0$?

## Oráculos y relativización (03/11)

31. Enuncia el resultado de Baker-Gill-Solovay. ¿Qué implica para las técnicas de diagonalización en la resolución de P vs. NP?
32. ¿Existe un oráculo $A$ tal que $\text{P}^A = \text{NP}^A$? ¿Y uno tal que $\text{P}^A \neq \text{NP}^A$? ¿Qué significa esto?
33. ¿Por qué la existencia de un oráculo que separa P de NP no constituye una prueba de que P ≠ NP?

## Aleatoriedad algorítmica (03/12)

34. ¿Cuál es la definición de Kolmogorov de una cadena aleatoria? ¿Por qué no puede verificarse computacionalmente?
35. ¿Qué es el número $\Omega$ de Chaitin? ¿En qué sentido es "lo más aleatorio posible"?
36. Describe la definición de Martin-Löf de aleatoriedad. ¿Qué ventaja tiene sobre la definición de Kolmogorov?
