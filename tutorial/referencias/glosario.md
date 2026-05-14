# Glosario de términos

Definiciones breves de los conceptos y símbolos técnicos del tutorial,
ordenadas alfabéticamente. Cada entrada enlaza al artículo donde se introduce.

---

## A

**AEP (Asymptotic Equipartition Property)**
Propiedad fundamental que dice que para una fuente ergódica, casi todas las secuencias largas tienen probabilidad aproximadamente $2^{-nH}$. Permite definir el *conjunto típico*.
→ [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)

**Autómata finito (DFA/NFA)**
Modelo de computación con número finito de estados, sin memoria adicional. Reconoce exactamente los lenguajes regulares.
→ [Autómatas finitos y lenguajes regulares](../03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md)

**Autómata de pila (PDA)**
Autómata finito ampliado con una pila de memoria infinita. Reconoce exactamente los lenguajes libres de contexto (CFL).
→ [Autómatas de pila](../03-computabilidad/09-automatas-de-pila-y-lenguajes-contexto-libre.md)

---

## B

**BEC (Binary Erasure Channel)**
Canal binario donde cada bit se borra (se convierte en ?) con probabilidad $\varepsilon$. Capacidad: $C = 1 - \varepsilon$.
→ [Canales discretos y capacidad](../02-teoria-informacion/04-canales-discretos-y-capacidad.md)

**BPP**
*Bounded-error Probabilistic Polynomial time*. Clase de lenguajes decidibles por una MT probabilista con error $\leq 1/3$ en tiempo polinomial.
→ [Complejidad aleatoria](../04-complejidad-computacional/08-complejidad-aleatoria.md)

**BQP**
*Bounded-error Quantum Polynomial time*. Análogo cuántico de BPP. Contiene P y NP ∩ BQP al menos.
→ [Información cuántica](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md)

**BSC (Binary Symmetric Channel)**
Canal binario donde cada bit se voltea con probabilidad $p$. Capacidad: $C = 1 - H(p)$.
→ [Canales discretos y capacidad](../02-teoria-informacion/04-canales-discretos-y-capacidad.md)

---

## C

**Capacidad de canal $C$**
Máxima tasa de transmisión fiable sobre un canal ruidoso. $C = \max_{p(x)} I(X;Y)$.
→ [Canales discretos y capacidad](../02-teoria-informacion/04-canales-discretos-y-capacidad.md)

**Código prefijo**
Código donde ninguna palabra de código es prefijo de otra. Permite decodificación instantánea. Satisface la desigualdad de Kraft.
→ [Codificación de fuente](../02-teoria-informacion/03-codificacion-de-fuente.md)

**Complejidad de Kolmogorov $K(x)$**
Longitud del programa más corto (en una UTM fija) que produce la cadena $x$. Medida de la información *intrínseca* de una cadena.
→ [Complejidad de Kolmogorov](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)

**CFL (Context-Free Language)**
Lenguaje generado por una gramática libre de contexto (Tipo 2 de Chomsky). Reconocible por PDA.
→ [Gramáticas y jerarquía de Chomsky](../03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md)

---

## D

**Desigualdad de Gibbs**
$D_\text{KL}(P \| Q) \geq 0$, con igualdad si y solo si $P = Q$. Fundamento de muchos resultados en teoría de la información.
→ [Divergencia KL](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)

**Desigualdad de Kraft**
Para un código prefijo con palabras de longitud $l_1, \ldots, l_n$: $\sum_i 2^{-l_i} \leq 1$.
→ [Codificación de fuente](../02-teoria-informacion/03-codificacion-de-fuente.md)

**Desigualdad de procesamiento de datos**
Si $X \to Y \to Z$ forman una cadena de Markov, entonces $I(X;Z) \leq I(X;Y)$. El procesamiento de datos no puede aumentar la información mutua.
→ [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)

**Diagonalización**
Técnica de prueba que construye un objeto que difiere de cada elemento de una lista enumerable. Usada en la indecidibilidad de HALT y la separación de clases de complejidad.
→ [El problema de la parada](../03-computabilidad/01-problema-de-la-parada.md)

**$D_\text{KL}(P \| Q)$ (Divergencia de Kullback-Leibler)**
$D_\text{KL}(P \| Q) = \sum_x P(x) \log_2 \frac{P(x)}{Q(x)}$. Mide cuánta información extra se usa al codificar $P$ asumiendo $Q$. No es simétrica.
→ [Divergencia KL y entropía cruzada](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)

---

## E

**Entropía $H(X)$**
$H(X) = -\sum_x P(x) \log_2 P(x)$. Medida de la incertidumbre media de una variable aleatoria, en bits.
→ [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)

**Entropía condicional $H(Y|X)$**
$H(Y|X) = \sum_x P(x) H(Y|X=x)$. Incertidumbre sobre $Y$ una vez conocido $X$.
→ [Entropía conjunta y condicional](../02-teoria-informacion/07-entropia-conjunta-y-condicional.md)

**Entropía conjunta $H(X,Y)$**
$H(X,Y) = H(X) + H(Y|X)$. Incertidumbre total del par $(X,Y)$.
→ [Entropía conjunta y condicional](../02-teoria-informacion/07-entropia-conjunta-y-condicional.md)

**Entropía diferencial $h(X)$**
$h(X) = -\int f(x) \log_2 f(x)\, dx$. Extensión continua de la entropía. No está acotada inferiormente por 0.
→ [Entropía diferencial](../02-teoria-informacion/10-entropia-diferencial.md)

**Entropía de Rényi $H_\alpha$**
$H_\alpha(X) = \frac{1}{1-\alpha}\log_2 \sum_x P(x)^\alpha$. Generalización paramétrica de la entropía de Shannon. $H_1 = H$ (Shannon).
→ [Información cuántica](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md)

**Entropía de Von Neumann $S(\rho)$**
$S(\rho) = -\text{tr}(\rho \log_2 \rho)$. Extensión cuántica de la entropía de Shannon para matrices densidad.
→ [Información cuántica](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md)

**ETH (Exponential Time Hypothesis)**
Hipótesis: existe $\delta > 0$ tal que 3-SAT requiere tiempo $2^{\delta n}$ en el peor caso.
→ [ETH y SETH](../04-complejidad-computacional/13-eth-seth-consecuencias.md)

---

## F

**FPT (Fixed-Parameter Tractable)**
Problema resoluble en tiempo $f(k) \cdot n^c$ donde $k$ es un parámetro, $c$ es constante y $f$ es computable. La complejidad exponencial queda confinada al parámetro.
→ [Complejidad parametrizada](../04-complejidad-computacional/10-complejidad-parametrizada.md)

---

## G

**Gramática libre de contexto (CFG)**
Gramática donde todas las reglas tienen la forma $A \to \alpha$ con $A$ un no-terminal y $\alpha$ una cadena de terminales y no-terminales. Tipo 2 de Chomsky.
→ [Gramáticas y jerarquía de Chomsky](../03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md)

---

## H

**$H$ (Entropía de Shannon)**
Ver *Entropía $H(X)$*.

**$\bar{H}$ (Tasa de entropía)**
$\bar{H} = \lim_{n\to\infty} \frac{1}{n} H(X_1, \ldots, X_n)$. Entropía por símbolo para una fuente estacionaria. Para cadenas de Markov: $\bar{H} = -\sum_i \pi_i \sum_j P_{ij} \log_2 P_{ij}$.
→ [Cadenas de Markov y tasa de entropía](../02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md)

**HALT**
El problema de la parada: dado $(M, x)$, ¿termina la MT $M$ con entrada $x$? Es el problema indecidible más famoso.
→ [El problema de la parada](../03-computabilidad/01-problema-de-la-parada.md)

---

## I

**$I(X;Y)$ (Información mutua)**
$I(X;Y) = H(X) + H(Y) - H(X,Y) = D_\text{KL}(P_{XY} \| P_X P_Y)$. Reducción de incertidumbre sobre $X$ al conocer $Y$.
→ [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)

**Información de Fisher $I(\theta)$**
$I(\theta) = \mathbb{E}[(\partial_\theta \ln f(X;\theta))^2]$. Cantidad de información sobre $\theta$ en una observación. Cota la varianza de cualquier estimador insesgado (Cramér-Rao).
→ [Información y biología](../05-conexiones-y-aplicaciones/07-informacion-y-biologia.md)

---

## K

**$K(x)$ (Complejidad de Kolmogorov)**
Ver *Complejidad de Kolmogorov*.

**KL (Kullback-Leibler)**
Ver *$D_\text{KL}$*.

---

## L

**Landauer, principio de**
Borrar 1 bit de información requiere disipación de al menos $k_B T \ln 2$ julios de energía.
→ [Información y termodinámica](../05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md)

**LDPC (Low-Density Parity-Check)**
Familia de códigos correctores de errores con matriz de paridad dispersa. Alcanzan la capacidad de Shannon mediante el decodificador BP (belief propagation).
→ [Códigos LDPC y Turbo](../02-teoria-informacion/11-codigos-ldpc-y-turbo.md)

**Lema de bombeo (Pumping Lemma)**
Propiedad de todos los lenguajes regulares (y CFL, con versión propia): cadenas suficientemente largas pueden "bombearse". Usado para probar que un lenguaje no es regular/CFL.
→ [Autómatas finitos](../03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md)

---

## M

**Máquina de Turing (MT)**
Modelo de computación con cinta infinita, cabezal de lectura/escritura y tabla de transiciones finita. Equivale en potencia a cualquier computador real.
→ [Máquinas de Turing](../03-computabilidad/04-maquinas-de-turing.md)

**MDL (Minimum Description Length)**
Principio de selección de modelos: el mejor modelo es el que minimiza la longitud total de la descripción del modelo más la descripción de los datos dado el modelo.
→ [Información en el aprendizaje estadístico](../05-conexiones-y-aplicaciones/05-informacion-en-aprendizaje.md)

---

## N

**NP**
Clase de problemas cuya solución puede *verificarse* en tiempo polinomial. Equivalentemente: decidibles por una MT no determinista en tiempo polinomial.
→ [P, NP y NP-completitud](../04-complejidad-computacional/01-p-np-y-np-completitud.md)

**NP-completo**
Problema en NP tal que todo problema de NP se reduce a él en tiempo polinomial (NP-hard y en NP). SAT es el prototipo.
→ [SAT y 3-SAT](../04-complejidad-computacional/03-sat-y-3-sat.md)

---

## O

**$\Omega$ (número de Chaitin)**
$\Omega = \sum_{p \text{ para}} 2^{-|p|}$. Probabilidad de parada de una UTM con entrada aleatoria. Es algorítmicamente aleatorio e incomputable.
→ [Aleatoriedad algorítmica](../03-computabilidad/12-aleatoriedad-algoritmica.md)

---

## P

**P**
Clase de problemas decidibles en tiempo polinomial por una MT determinista.
→ [P, NP y NP-completitud](../04-complejidad-computacional/01-p-np-y-np-completitud.md)

**PCP (Probabilistically Checkable Proof)**
Sistema de prueba donde un verificador aleatorio lee $O(\log n)$ bits de aleatoriedad y $O(1)$ bits de la prueba. $\text{PCP}(\log n, 1) = \text{NP}$.
→ [El teorema PCP](../04-complejidad-computacional/09-teorema-pcp.md)

**Principio de Landauer**
Ver *Landauer, principio de*.

**PSPACE**
Clase de problemas decidibles con espacio polinomial (tiempo potencialmente exponencial). $\text{P} \subseteq \text{NP} \subseteq \text{PSPACE}$.
→ [Complejidad espacial](../04-complejidad-computacional/04-complejidad-espacial.md)

---

## R

**$R(D)$ (Función tasa-distorsión)**
Mínima tasa de compresión compatible con distorsión media $\leq D$. Generaliza la entropía a compresión con pérdida.
→ [Teoría de la tasa-distorsión](../02-teoria-informacion/09-teoria-tasa-distorsion.md)

**Reducción (polinómica)**
$A \leq_p B$: existe un algoritmo polinomial que transforma instancias de $A$ en instancias de $B$. Si $B \in P$, entonces $A \in P$.
→ [Reducciones polinómicas](../04-complejidad-computacional/02-reducciones-polinomicas.md)

---

## S

**SAT (Satisfacibilidad booleana)**
Dado una fórmula booleana, ¿existe una asignación que la satisfaga? Primer problema NP-completo (Cook-Levin 1971).
→ [SAT y 3-SAT](../04-complejidad-computacional/03-sat-y-3-sat.md)

**SETH (Strong Exponential Time Hypothesis)**
Para todo $\varepsilon > 0$, existe $k$ tal que $k$-SAT requiere tiempo $2^{(1-\varepsilon)n}$.
→ [ETH y SETH](../04-complejidad-computacional/13-eth-seth-consecuencias.md)

**$\Sigma$ (alfabeto)**
Conjunto finito de símbolos. Las cadenas y los lenguajes se definen sobre $\Sigma^*$.

**$\Sigma_k^P / \Pi_k^P$ (Jerarquía polinómica)**
$\Sigma_0^P = \Pi_0^P = P$, $\Sigma_{k+1}^P = NP^{\Sigma_k^P}$, $\Pi_{k+1}^P = co\text{-}NP^{\Sigma_k^P}$. Generaliza P y NP a $k$ alternaciones de cuantificadores.
→ [P, NP y NP-completitud](../04-complejidad-computacional/01-p-np-y-np-completitud.md)

**Szilard, motor de**
Experimento mental donde un demonio mide la posición de una molécula y extrae trabajo. Resolución: medir (adquirir información) tiene coste entrópico.
→ [Información y termodinámica](../05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md)

---

## T

**Tasa de entropía $\bar{H}$**
Ver *$\bar{H}$*.

**Teorema AEP**
Ver *AEP*.

**Teorema de Fagin**
NP = ∃SO (lógica de segundo orden existencial sobre estructuras finitas).
→ [Complejidad descriptiva](../03-computabilidad/08-complejidad-descriptiva.md)

**Teorema de Rice**
Toda propiedad semántica no trivial de los programas es indecidible.
→ [Universalidad y autorreferencia](../03-computabilidad/07-universalidad-y-autorreferencia.md)

**Teorema de Shannon (codificación de canal)**
Para un canal de capacidad $C$, se puede transmitir a cualquier tasa $R < C$ con error arbitrariamente pequeño. No se puede transmitir de forma fiable con $R > C$.
→ [Teorema de Shannon](../02-teoria-informacion/08-teorema-de-shannon-capacidad.md)

**Teorema de Toda**
$PH \subseteq P^{\#P}$. Toda la jerarquía polinómica es reductible a un oráculo de conteo.
→ [#P y conteo](../04-complejidad-computacional/11-sharp-p-y-conteo.md)

**Treewidth**
Parámetro de grafos que mide cuánto se parece a un árbol. Muchos problemas NP-difíciles son FPT parametrizados por treewidth (Teorema de Courcelle).
→ [Complejidad parametrizada](../04-complejidad-computacional/10-complejidad-parametrizada.md)

---

## U

**UTM (Universal Turing Machine)**
Máquina de Turing que simula cualquier otra MT cuando se le da la descripción de ésta como entrada. Base teórica de los computadores modernos.
→ [Universalidad y autorreferencia](../03-computabilidad/07-universalidad-y-autorreferencia.md)

---

## V

**VC (Vapnik-Chervonenkis), dimensión**
Tamaño del mayor conjunto de puntos que puede ser "destrozado" por una clase de hipótesis $\mathcal{H}$. Controla la capacidad de generalización en aprendizaje PAC.
→ [Información en el aprendizaje estadístico](../05-conexiones-y-aplicaciones/05-informacion-en-aprendizaje.md)
