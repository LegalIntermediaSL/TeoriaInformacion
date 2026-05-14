# 32 - #P y problemas de conteo

## Contexto

Este ejercicio acompaña el artículo
[#P y problemas de conteo](../../04-complejidad-computacional/11-sharp-p-y-conteo.md).

## Enunciado

**Parte A — La clase #P:**

1. Define la clase #P. ¿Qué diferencia hay entre decidir si $x \in L$ y calcular $\#L(x)$?
2. Demuestra que si $\#SAT \in FP$ (i.e., se puede contar en tiempo polinomial), entonces $P = NP$.
3. ¿Está #P contenida en PSPACE? Justifica sin usar el teorema de Toda.

**Parte B — #P-completitud:**

4. ¿Por qué el cálculo del **permanente** de una matriz 0-1 es #P-completo? ¿Por qué el **determinante** está en P?
5. Enuncia el teorema de Toda. ¿Qué dice sobre la relación entre #P y la jerarquía polinómica PH?

**Parte C — Aproximación:**

6. Describe el esquema de aproximación de Jerrum-Sinclair para el permanente de matrices 0-1. ¿Qué garantía de aproximación ofrece?

## Pista

**#P:** si $L \in NP$ con verificador $V$, entonces $f(x) = |\{y : V(x,y) = 1\}|$ es una función en #P.

**Permanente:** $\text{perm}(A) = \sum_{\sigma \in S_n} \prod_{i=1}^n A_{i,\sigma(i)}$. Cada término es 0 o 1 para matrices 0-1, y el permanente cuenta las coberturas perfectas en un bigrafo.

**Teorema de Toda:** $PH \subseteq P^{\#P}$.

## Solución

### Parte A — La clase #P

#### 1. Definición de #P

Una función $f: \{0,1\}^* \to \mathbb{N}$ está en **#P** si existe una MT no determinista $M$ que corre en tiempo polinomial tal que, para todo $x$:

$$f(x) = |\{\text{ramas aceptadoras de } M(x)\}|$$

La diferencia con NP:
- En NP solo importa si hay **alguna** rama aceptadora (existencia).
- En #P se pide **cuántas** ramas aceptadoras hay (conteo).
- Decidir $\exists$ es fácil (se puede aproximar); contar exactamente es generalmente mucho más difícil.

#### 2. $\#SAT \in FP \Rightarrow P = NP$

Si $\#SAT \in FP$, entonces en particular podemos determinar si $\#SAT(x) > 0$ en tiempo polinomial. Pero $\#SAT(x) > 0$ si y solo si la fórmula $x$ es satisfacible, i.e., $x \in SAT$. Así tendríamos $SAT \in P$, y como SAT es NP-completo, $P = NP$.

#### 3. $\#P \subseteq PSPACE$

Para calcular $\#L(x)$, podemos recorrer sistemáticamente todos los posibles certificados $y$ de longitud polinomial, verificar cada uno en tiempo polinomial, y llevar un contador. El espacio necesario es polinomial (para el contador en binario y el certificado actual). Por tanto $\#P \subseteq FPSPACE$, y en consecuencia las funciones en #P son computables en PSPACE.

### Parte B — #P-completitud

#### 4. Permanente vs. determinante

**Permanente:** $\text{perm}(A) = \sum_{\sigma \in S_n} \prod_{i=1}^n A_{i,\sigma(i)}$.

Para matrices 0-1, el permanente cuenta el número de **emparejamientos perfectos** en el bigrafo bipartito $G$ donde $A_{ij} = 1$ indica la arista $(i,j)$. Como contar emparejamientos perfectos es #P-completo (Valiant 1979), el permanente es #P-completo.

**Determinante:** $\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n A_{i,\sigma(i)}$.

La diferencia es el factor $\text{sgn}(\sigma) \in \{+1,-1\}$. Esta alternancia de signos permite la eliminación gaussiana (las canciones destructivas reducen el problema), dando un algoritmo de Gauss en tiempo $O(n^3)$. No hay contrapartida para el permanente: todos los términos son positivos y no se cancelan.

#### 5. Teorema de Toda

**Teorema (Toda 1991):** $PH \subseteq P^{\#P}$.

En palabras: toda la jerarquía polinómica (todos los niveles de $\Sigma_k^P$ y $\Pi_k^P$) es decidible en tiempo polinomial dado un oráculo para #SAT.

Consecuencia: si $\#P \subseteq FP$ (se puede contar en tiempo polinomial), entonces $PH = P$, es decir, toda la jerarquía colapsa a P. Esto muestra que #P es "más potente" que NP y toda la jerarquía polinómica.

### Parte C — Aproximación

#### 6. Esquema de Jerrum-Sinclair (FPRAS para el permanente)

Jerrum y Sinclair (1989) demostraron que el permanente de matrices 0-1 admite un **FPRAS** (Fully Polynomial Randomized Approximation Scheme): para todo $\varepsilon > 0$, el algoritmo devuelve un valor $\hat{p}$ tal que

$$P\!\left(\frac{\text{perm}(A)}{1+\varepsilon} \leq \hat{p} \leq (1+\varepsilon)\,\text{perm}(A)\right) \geq \frac{3}{4}$$

en tiempo $\text{poly}(n, 1/\varepsilon)$.

**Idea:** se usa una cadena de Markov sobre emparejamientos (no necesariamente perfectos) del bigrafo. La cadena mezcla rápidamente (mixing time polinomial), lo que permite estimar la razón $\text{perm}(A) / 2^{n^2}$ mediante muestreo de Monte Carlo. La mezcla rápida se prueba mostrando que el grafo de emparejamientos es un **expander** (buen conductance).

**Limitación importante:** el FPRAS funciona para matrices 0-1. Para matrices con entradas reales arbitrarias (o negativas), el permanente puede ser #P-difícil de aproximar (la alternancia de signos destruye la estructura de cadena de Markov positiva).
