# Guía de rutas de profundización

## Para quién es esta guía

Has terminado el tutorial (o estás a punto de hacerlo) y quieres continuar. Esta guía propone rutas de lectura graduadas por nivel de dificultad y especialización, agrupadas por área de interés. Las referencias están ordenadas de menor a mayor exigencia dentro de cada ruta.

## Ruta A: Teoría de la información — profundidad matemática

Para quien quiere dominar la teoría con rigor completo (probabilidad, medida, ergodía).

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Cover & Thomas, *Elements of Information Theory* (2006, 2ª ed.) | El libro de referencia universal. Cubre todo el tutorial y mucho más, con demostraciones completas. |
| 2 — Avanzado | Csiszár & Körner, *Information Theory: Coding Theorems for Discrete Memoryless Systems* (2011) | Tratamiento riguroso con métodos del tipo. Para quien quiera demostrar teoremas. |
| 3 — Especialización | Polyanskiy & Wu, *Information Theory: From Coding to Learning* (2024, online) | Material de clase de MIT; cubre información de grano fino, gaussianas y aprendizaje. |
| Complemento | Gallager, *Information Theory and Reliable Communication* (1968) | Clásico de ingeniero; énfasis en códigos y canales prácticos. |

## Ruta B: Computabilidad — fundamentos lógicos

Para quien quiere entender las raíces matemáticas: lógica de primer orden, teoría de conjuntos recursivos.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Sipser, *Introduction to the Theory of Computation* (2013, 3ª ed.) | Clarísimo. Los primeros 4 capítulos del tutorial siguen este libro. |
| 2 — Intermedio | Cutland, *Computability: An Introduction to the Theory of Computability* (1980) | Formalización rigurosa sin exceso. |
| 3 — Avanzado | Soare, *Turing Computability: Theory and Applications* (2016) | Recursión, grados de Turing, jerarquía aritmética. Para especialistas. |
| Complemento | Rogers, *Theory of Recursive Functions and Effective Computability* (1987) | Referencia clásica en teoría de la computabilidad matemática. |

## Ruta C: Complejidad computacional — teoría moderna

Para quien quiere trabajar en la frontera de investigación en algoritmos y complejidad.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Sipser, *Introduction to the Theory of Computation* (2013), caps. 7-10 | Introduce P, NP, PSPACE y NL con claridad. |
| 2 — Intermedio | Papadimitriou, *Computational Complexity* (1994) | Más profundo que Sipser. Cubre la jerarquía polinómica y complejidad de conteo. |
| 3 — Avanzado | Arora & Barak, *Computational Complexity: A Modern Approach* (2009) | El texto de referencia en investigación. Disponible online. 800 páginas. |
| Especialización | Goldreich, *Computational Complexity: A Conceptual Perspective* (2008) | Énfasis en las ideas, no los formalismos. |

## Ruta D: Algoritmos de aproximación e inaproximabilidad

Para quien quiere entender qué se puede hacer con problemas NP-completos en la práctica.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Vazirani, *Approximation Algorithms* (2001) | Estándar del área. Cubre vertex cover, TSP, bin packing, etc. |
| 2 — PCP | Hastad's lecture notes on PCP theorem | Notas originales del inventor. Técnicas modernas de hard inaproximabilidad. |
| 3 — Avanzado | Williamson & Shmoys, *The Design of Approximation Algorithms* (2011, online gratis) | Libro moderno completo. |

## Ruta E: Complejidad parametrizada y algoritmos exactos

Para quien trabaja en problemas combinatorios y quiere entender el espacio entre P y NP.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Cygan et al., *Parameterized Algorithms* (2015, online gratis) | El texto de referencia. Cubre kernelización, árbol de búsqueda, treewidth. |
| 2 — Hardness | Downey & Fellows, *Fundamentals of Parameterized Complexity* (2013) | Teoría de la W-jerarquía y hardness FPT. |
| Complemento | Fomin & Kratsch, *Exact Algorithms for Hard Problems* (2010) | Algoritmos para problemas NP en el peor caso: $O^*(1.1996^n)$ para Vertex Cover, etc. |

## Ruta F: Criptografía y teoría de la complejidad

Para quien quiere entender los fundamentos matemáticos de la seguridad informática.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Boneh & Shoup, *A Graduate Course in Applied Cryptography* (2023, online gratis) | Moderno y completo. Desde OTP hasta ZK proofs. |
| 2 — Fundamentos | Goldreich, *The Foundations of Cryptography*, vol. 1 y 2 (2001/2004) | Rigor matemático completo. Para teoristas. |
| Complemento | Katz & Lindell, *Introduction to Modern Cryptography* (2021, 3ª ed.) | Equilibrio entre rigor y aplicabilidad. |

## Ruta G: Información cuántica y computación cuántica

Para quien quiere entrar en el campo cuántico con base sólida.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Accesible | Aaronson, *Quantum Computing Since Democritus* (2013) | Conceptual y brillante. Sin álgebra lineal compleja. |
| 2 — Técnico | Nielsen & Chuang, *Quantum Computation and Quantum Information* (2000) | El texto estándar del área. Completo y riguroso. |
| 3 — Información cuántica | Wilde, *Quantum Information Theory* (2017, 2ª ed., online gratis) | Énfasis en teoría de la información cuántica: entropía de Von Neumann, capacidad cuántica. |

## Ruta H: Aplicaciones — machine learning y estadística

Para quien trabaja en ML y quiere la perspectiva de información.

| Nivel | Recurso | Por qué |
|-------|---------|---------|
| 1 — Base | Goodfellow et al., *Deep Learning* (2016), cap. 3 (probabilidad e información) | Contexto para ML. Cover & Thomas cap. 2 como alternativa. |
| 2 — Teoría | Shalev-Shwartz & Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014, online) | VC dimension, PAC learning, MDL. |
| 3 — Bottleneck | Tishby, Pereira & Bialek, *The Information Bottleneck Method* (1999) — artículo | El artículo original del bottleneck de información. |
| Complemento | Bialek, *Biophysics: Searching for Principles* (2012) | Información en sistemas biológicos: retina, genoma, redes neuronales. |

## Recursos de libre acceso online

| Recurso | URL |
|---------|-----|
| Arora & Barak | cs.princeton.edu/theory/complexity/ |
| Williamson & Shmoys | designofapproxalgs.com |
| Wilde, QIT | arxiv.org/abs/1106.1445 |
| Boneh & Shoup | toc.cryptobook.us |
| Cygan et al. | parameterized.mimuw.edu.pl |
| Cover & Thomas (acceso institucional) | wiley.com |

## Conferencias y journals de referencia

| Área | Conferencias top | Journal de referencia |
|------|-----------------|----------------------|
| Teoría de la información | IEEE ISIT, ITW | IEEE Trans. Information Theory |
| Computabilidad | CIE, Computability | Annals of Pure and Applied Logic |
| Complejidad | STOC, FOCS, CCC | SIAM J. Computing, Theory of Computing |
| Algoritmos | SODA, ESA | Algorithmica, J. ACM |
| Criptografía | CRYPTO, EUROCRYPT | Journal of Cryptology |

## Próximos pasos recomendados

Si terminas el tutorial sin especialización clara, la lectura con mayor relación beneficio/coste es:

1. **Cover & Thomas** (caps. 2, 5, 7, 8): teoría de la información completa.
2. **Arora & Barak** (caps. 1-5): complejidad moderna.
3. **Aaronson, *Quantum Computing Since Democritus***: perspectiva unificadora.

Juntos dan una base suficiente para leer artículos de investigación en cualquiera de las áreas del tutorial.

<!-- nav-start -->

---
← [01 - Mapa del territorio: información, cálculo y dificultad](01-mapa-del-territorio.md) · [01 - Logaritmos, probabilidad y crecimiento](../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md) →

<!-- nav-end -->
