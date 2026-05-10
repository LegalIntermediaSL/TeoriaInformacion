# Ejercicios propuestos — Complejidad computacional

Extraídos de los artículos del módulo 04.

---

## P y NP (04/01)

1. ¿Es el problema de decidir si un grafo tiene un vértice de grado ≥ k miembro de P? Argumenta.
2. Describe informalmente qué significa que un problema sea NP-completo.
3. Si alguien demuestra P = NP, ¿qué implicaría para RSA y la criptografía actual?

## Reducciones polinómicas (04/02)

4. Muestra que 3-SAT ≤ₚ CLIQUE. Describe la reducción en palabras.
5. Si $A \leq_p B$ y $B \in \text{P}$, ¿qué se puede concluir sobre $A$?
6. ¿Por qué las reducciones deben ser en tiempo polinomial para preservar la complejidad?

## Complejidad aleatoria (04/08)

7. ¿Cuál es la diferencia entre RP, coRP y BPP? Da un ejemplo intuitivo de cada uno.
8. El test de Miller-Rabin para primalidad está en BPP. ¿Cómo se amplifica su precisión?
9. ¿Por qué no se sabe si P = BPP, aunque se cree que sí?

## El teorema PCP (04/09)

10. Enuncia el teorema PCP y describe qué son los parámetros $r$ (bits de aleatoriedad) y $q$ (bits leídos).
11. ¿Qué implica el teorema PCP para la aproximabilidad de MAX-3SAT?
12. Explica la diferencia entre el teorema PCP y el resultado de inaproximabilidad para MAX-CLIQUE.

## Complejidad parametrizada (04/10)

13. Define "fijo-parámetro tratable" (FPT). ¿Por qué k-Vertex Cover es FPT pero k-Clique probablemente no?
14. Describe el árbol de búsqueda acotada para k-Vertex Cover y calcula el número máximo de hojas para k=4.
15. ¿En qué se diferencian las clases FPT y W[1]?

## #P y conteo (04/11)

16. ¿Por qué el permanente de una matriz 0-1 es #P-completo pero el determinante está en P?
17. Enuncia el teorema de Toda. ¿Qué dice sobre la relación entre #P y la jerarquía polinómica PH?
18. Define FPRAS. ¿Qué garantiza el algoritmo de Jerrum-Sinclair-Vigoda para el permanente?

## Complejidad de comunicación (04/12)

19. ¿Cuántos bits necesita Alice para convencer a Bob de que $x = y$ (igualdad de n-bits) en el peor caso? ¿Y en promedio (protocolo aleatorizado)?
20. Describe el protocolo hash de Freivalds para igualdad y calcula su probabilidad de falso positivo.
21. ¿Por qué la complejidad de comunicación sirve para demostrar lower bounds de circuitos?

## ETH y SETH (04/13)

22. Enuncia la hipótesis ETH. ¿Qué implica para el tiempo de resolución de 3-SAT?
23. ¿Por qué LCS (longest common subsequence) tiene un lower bound de $\Omega(n^2)$ bajo SETH?
24. Explica la diferencia entre ETH y SETH. ¿Cuál es más fuerte?
