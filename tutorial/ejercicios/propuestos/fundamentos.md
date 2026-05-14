# Ejercicios propuestos — Fundamentos matemáticos

Extraídos de los artículos del módulo 01.

---

## Logaritmos, probabilidad y crecimiento asintótico (01/01)

1. Calcula $\log_2 1024$. ¿Cuántos bits se necesitan para representar 1000 valores distintos?
2. Si $P(A) = 0.3$ y $A$ y $B$ son independientes con $P(B) = 0.5$, calcula $P(A \cup B)$.
3. Ordena de mayor a menor tasa de crecimiento: $n^2$, $2^n$, $n \log n$, $n!$, $\sqrt{n}$, $n^{100}$.
4. Demuestra que $\log(n!)= \Theta(n \log n)$ usando la aproximación de Stirling.
5. ¿Para qué valores de $n$ es $2^n > n^{10}$? Estima el cruce.

## Conjuntos, funciones y relaciones (01/02)

6. Demuestra que $|2^A| = 2^{|A|}$ para cualquier conjunto finito $A$.
7. Sea $f: A \to B$ inyectiva. ¿Qué puedes concluir sobre $|A|$ y $|B|$?
8. ¿Cuántas relaciones de equivalencia distintas existen sobre un conjunto de 3 elementos?
9. Demuestra que la composición de dos funciones biyectivas es biyectiva.
10. Sea $R$ una relación de orden parcial. Da un ejemplo donde no exista ni máximo ni mínimo.

## Combinatoria y conteo (01/03)

11. ¿De cuántas formas se pueden distribuir 10 bolas idénticas en 4 cajas distintas?
12. Calcula el coeficiente binomial $\binom{20}{3}$ sin calculadora.
13. ¿Cuántas cadenas binarias de longitud 8 tienen exactamente 3 unos?
14. Enuncia y demuestra el principio de inclusión-exclusión para 3 conjuntos.
15. ¿Cuántos árboles de expansión tiene el grafo completo $K_4$? (Usa la fórmula de Cayley.)

## Grafos y estructuras discretas (01/04)

16. ¿Cuántas aristas tiene un grafo completo $K_n$? Justifica con una fórmula cerrada.
17. Demuestra que todo grafo con $n \geq 2$ vértices tiene al menos dos vértices del mismo grado.
18. ¿Es planar el grafo $K_5$? Aplica la fórmula de Euler $V - E + F = 2$.
19. Da un ejemplo de grafo bipartito y demuestra que no contiene ciclos de longitud impar.
20. Describe el algoritmo BFS y analiza su complejidad en términos de $|V|$ y $|E|$.

## Lógica booleana y proposicional (01/05)

21. Convierte la fórmula $(A \lor B) \land \neg C$ a CNF (forma normal conjuntiva).
22. Demuestra que $\{$NAND$\}$ es un conjunto funcionalmente completo.
23. ¿Cuántas interpretaciones distintas satisfacen una tautología con 4 variables proposicionales?
24. Aplica resolución para demostrar que $\{p \lor q,\ \neg p \lor r,\ \neg q \lor r\} \models r$.
25. ¿Qué significa que una fórmula sea satisfacible? ¿Qué problema computacional corresponde a decidirlo?
