# El Teorema PCP y la Dureza de Aproximación

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Reducciones polinómicas](02-reducciones-polinomicas.md)
- [Aproximación y heurísticas](06-aproximacion-y-heuristicas.md)

## Objetivos de aprendizaje

1. Enunciar el teorema PCP: NP = PCP(log n, 1).
2. Entender cómo el teorema PCP implica cotas de inaproximabilidad.
3. Relacionar la conjetura del juego único (UGC) con los límites de aproximación.


## Intuición

El teorema PCP (Probabilistically Checkable Proofs) es uno de los resultados más profundos de la
complejidad computacional. Establece que cualquier demostración matemática puede reescribirse de
forma que un verificador aleatorio pueda comprobar su corrección leyendo solo **una cantidad
constante de bits**, con error acotado. La consecuencia inmediata es que muchos problemas de
optimización NP-difíciles son **difíciles de aproximar**, no solo de resolver exactamente.

## Pruebas verificables probabilísticamente

Un **sistema PCP** para un lenguaje $L$ es un par de parámetros $(r, q)$ y un verificador $V$
que, dado $x$ y acceso aleatorio a una prueba $\pi$:

1. Usa a lo sumo $r(|x|)$ bits aleatorios.
2. Lee a lo sumo $q(|x|)$ bits de $\pi$.
3. Si $x \in L$: existe $\pi$ tal que $V$ acepta con probabilidad 1.
4. Si $x \notin L$: para toda $\pi$, $V$ acepta con probabilidad $\leq 1/2$.

La clase PCP$(r, q)$ contiene todos los lenguajes con verificadores de este tipo.

**Observaciones:**

- PCP$(0, \text{poly})$ = NP: sin aleatoriedad, leer la prueba completa.
- PCP$(\text{poly}, 0)$ = P: sin leer la prueba, decidir directamente.
- PCP$(\log n, 1)$ es la clase "interesante" que aparece en el teorema.

## El teorema PCP

**Teorema PCP (Arora-Safra, Arora-Lund-Motwani-Sudan-Szegedy, 1992-1998).**

$$\text{NP} = \text{PCP}(\log n, 1)$$

Todo problema en NP tiene un verificador que usa $O(\log n)$ bits aleatorios y lee
solo un **número constante** de bits de la prueba.

Esto es sorprendente: una demostración de longitud $m$ puede verificarse estadísticamente
con solo $O(\log m)$ monedas y $O(1)$ consultas a la prueba.

## Consecuencia inmediata: Max-3SAT

### Ejemplo numérico: inaproximabilidad de Max-3SAT

Consideramos la fórmula $\phi = (x_1 \lor x_2 \lor x_3) \land (\neg x_1 \lor x_2 \lor \neg x_3) \land (x_1 \lor \neg x_2 \lor x_3) \land (\neg x_1 \lor \neg x_2 \lor \neg x_3)$ con 4 cláusulas.

| Asignación | Cláusulas satisfechas | Fracción |
|---|---|---|
| $(0,0,0)$ | 3 de 4 | 0.75 |
| $(1,0,0)$ | 3 de 4 | 0.75 |
| $(1,1,0)$ | 4 de 4 | **1.0** |
| $(0,0,1)$ | 3 de 4 | 0.75 |

La asignación óptima satisface $4/4 = 100\%$ de las cláusulas. El algoritmo aleatorio simple (asignar cada variable independientemente con $P(x_i=1)=1/2$) satisface en esperanza $7/8$ de las cláusulas por cláusula, ya que cada cláusula de 3 literales se viola con probabilidad $(1/2)^3 = 1/8$.

**Consecuencia del teorema PCP:** ningún algoritmo en tiempo polinomial puede satisfacer más de $7/8 + \varepsilon$ de las cláusulas para todo $\varepsilon > 0$, salvo que P = NP (Håstad, 1997). El algoritmo aleatorio es por tanto **óptimo** entre los algoritmos eficientes.

Consideramos el problema de optimización **Max-3SAT**: dada una fórmula 3-CNF, encontrar una
asignación que satisfaga el mayor número posible de cláusulas.

El teorema PCP implica:

**Corolario.** No existe algoritmo polinomial que, dada una fórmula 3-SAT insatisfacible,
encuentre una asignación que satisfaga más del $\alpha \approx 7/8$ de las cláusulas,
a menos que P = NP.

Notablemente, el algoritmo aleatorio que asigna cada variable uniformemente en $\{0,1\}$
satisface en promedio exactamente $7/8$ de las cláusulas. El teorema PCP dice que esto
es **óptimo**: no se puede hacer mejor en tiempo polinomial.

## Del teorema PCP a la dureza de aproximación

La conexión entre el teorema PCP y la aproximación funciona así:

1. Por el teorema PCP, NP ⊆ PCP$(log n, 1)$.
2. El verificador PCP puede modelarse como una instancia de un juego de **constraint satisfaction**.
3. Si la instancia es satisfacible (el problema original está en L), existe prueba que hace
   pasar todas las restricciones.
4. Si no es satisfacible, ninguna prueba pasa más de $(1/2)$ fracción de las restricciones.
5. Una reducción convierte esta dicotomía en una instancia de Max-3SAT (o Max-Clique, etc.)
   donde el gap entre el caso "sí" y el caso "no" es constante.

Este paradigma de **gap amplification** genera resultados de inaproximabilidad para docenas
de problemas.

## Resultados de inaproximabilidad seleccionados

| Problema | Ratio del mejor algoritmo | Inaproximable en |
|----------|--------------------------|-----------------|
| Max-3SAT | $7/8 + \epsilon$ (aleatorio) | $(7/8+\epsilon)$ bajo P≠NP |
| Max-Clique | $n^{1-\epsilon}$ | $n^{1-\epsilon}$ bajo P≠NP |
| Conjunto independiente | $n^{1-\epsilon}$ | $n^{1-\epsilon}$ bajo P≠NP |
| Vertex Cover | $2 - \epsilon$ (teorema de Dinur) | $(2-\epsilon)$ bajo Conjetura del Juego Único |
| Coloración cromática | $O(n^{0.199})$ | mejor que $n^{1/3-\epsilon}$ bajo P≠NP |

## La conjetura del juego único (Unique Games Conjecture)

Khot (2002) propuso la **Unique Games Conjecture (UGC)**: para todo $\epsilon > 0$, es NP-difícil
distinguir instancias de un juego de restricciones únicas donde:
- El caso "sí": fracción $\geq 1 - \epsilon$ de restricciones satisfacibles.
- El caso "no": fracción $\leq \epsilon$ de restricciones satisfacibles.

Bajo la UGC:

- Vertex Cover es inaproximable en ratio $2 - \epsilon$ (cota de Khot-Regev).
- Max-Cut es inaproximable más allá de $\approx 0.878$ (algoritmo de Goemans-Williamson es óptimo).
- Muchos problemas de optimización con algoritmos SDP son óptimos.

La UGC sigue sin demostrarse ni refutarse; es la frontera activa de la teoría de aproximación.

## El argumento de la amplificación del gap

La demostración del teorema PCP (en su versión simplificada) combina varias ideas:

1. **Codificación de Hadamard:** las pruebas se codifican con corrección de errores robusta.
2. **Test lineal de Blum-Luby-Rubinfeld:** se puede verificar con pocas consultas si una
   función es lineal (es decir, si es un homomorfismo de $\mathbb{F}_2^n$).
3. **Composición de verificadores:** verificadores de alta completitud y baja solidez se
   componen para mantener ambas propiedades.
4. **Amplificación de la brecha:** iteraciones de una expander graph walk amplifican la
   brecha entre el caso satisfacible y el insatisfacible.

La demostración completa ocupa decenas de páginas; la versión de Dinur (2007) usando
amplificación de brecha sobre grafos es la más elegante.

## PCP y criptografía

Los sistemas PCP tienen conexiones profundas con la **criptografía**:

- **Argument systems:** versiones interactivas de PCP con criptografía producen argumentos
  de conocimiento cero (zero-knowledge proofs) sucinctos.
- **SNARKs** (Succinct Non-interactive ARguments of Knowledge): usados en blockchains para
  verificar computaciones complejas con pocas kilobytes de prueba.
- La transformación de Fiat-Shamir convierte protocolos interactivos en no interactivos
  usando funciones hash, conectando PCP con pruebas con papel y lápiz.

## Ideas clave

- El teorema PCP (NP = PCP$(log n, 1)$) establece que las demostraciones de NP pueden
  verificarse con aleatoriedad logarítmica y consultas constantes.
- La consecuencia directa es que Max-3SAT y otros problemas tienen cotas de inaproximabilidad
  que coinciden con los mejores algoritmos conocidos.
- El paradigma de gap amplification es la herramienta central: generar instancias donde hay un
  salto constante entre el caso satisfacible y el no satisfacible.
- La Conjetura del Juego Único (UGC) refina estos límites para muchos problemas de corte.
- Los SNARKs y las pruebas de conocimiento cero son aplicaciones prácticas de las ideas PCP.

## Ejercicios

1. El algoritmo que asigna cada variable de 3-SAT uniformemente al azar satisface en promedio
   $7/8$ de las cláusulas. Verifica esto calculando la probabilidad de que una cláusula de 3
   literales sea satisfecha por una asignación aleatoria.
2. Explica intuitivamente por qué verificar una prueba con acceso aleatorio a $q$ bits es
   equivalente a verificar una instancia de un juego de satisfacibilidad con $2^q$ valores posibles.
3. ¿Qué diferencia hay entre un algoritmo de aproximación de ratio $\alpha$ y un algoritmo FPTAS?
   ¿Puede existir un FPTAS para Max-3SAT?
4. El algoritmo de Goemans-Williamson para Max-Cut tiene ratio $\approx 0.878$. Bajo la UGC,
   ningún algoritmo polinomial puede superar este ratio. ¿Qué dice esto sobre la estructura
   de los problemas de corte en grafos?
5. Investiga qué es un SNARK y en qué sentido utiliza ideas de los sistemas PCP.

## Véase también

- [Aproximación y heurísticas](06-aproximacion-y-heuristicas.md)
- [Complejidad descriptiva](../03-computabilidad/08-complejidad-descriptiva.md)


## Referencias

- Arora, S. y Barak, B. (2009). *Computational Complexity: A Modern Approach*, capítulo 11.
- Dinur, I. (2007). The PCP theorem by gap amplification. *J. ACM*.
- Khot, S. (2002). On the power of unique 2-prover 1-round games. *STOC 2002*.
- Goemans, M. y Williamson, D. (1995). Improved approximation algorithms for maximum cut
  and satisfiability problems. *J. ACM*.
