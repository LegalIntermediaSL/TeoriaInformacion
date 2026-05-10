# 24 - El teorema PCP

## Contexto

Este ejercicio acompaña el artículo
[El teorema PCP](../../04-complejidad-computacional/09-teorema-pcp.md).

## Enunciado

1. Enuncia el teorema PCP en la forma:
   ```text
   NP = PCP(log n, O(1))
   ```
   Explica qué significa cada parámetro.

2. Un verificador PCP para 3-SAT lee 3 bits de la prueba y acepta o rechaza.
   - Si la fórmula es satisfacible: el verificador acepta con probabilidad 1.
   - Si la fórmula no es satisfacible: el verificador rechaza con probabilidad ≥ 1/2.
   ¿Cuántas cláusulas debe tener la "pregunta aleatoria" del verificador?

3. Explica cómo el teorema PCP implica que MAX-3SAT no puede aproximarse con
   ratio mejor que $7/8$ (a menos que P = NP).

4. ¿Qué diferencia hay entre un **sistema de prueba interactiva** (IP) y un
   **verificador PCP**? ¿Por qué el PCP es más fuerte para inaproximabilidad?

## Pista

**PCP($r, q$):** $r$ bits de aleatoriedad (→ $2^r$ posibles "preguntas"), $q$ bits
de la prueba leídos. El verificador es eficiente (tiempo polinomial en la longitud
de la entrada más el certificado).

**Inaproximabilidad:** si MAX-3SAT tuviese ratio $> 7/8$, podría distinguir
"fórmulas satisfacibles" de "fórmulas con fracción de cláusulas satisfechas $\leq 7/8$",
lo que permitiría decidir SAT.

## Solución

### 1. El teorema PCP

**Enunciado.** $\text{NP} = \text{PCP}(\log n, O(1))$.

**Significado de los parámetros:**

- **$\text{PCP}(r(n), q(n))$:** clase de problemas decidibles por un verificador
  probabilístico que:
  - Lee la **entrada** $x$ completamente.
  - Usa $r(n)$ bits de **aleatoriedad** para elegir su "pregunta" (cuáles bits de
    la prueba leer).
  - Lee a lo sumo $q(n)$ bits de una **prueba** $\pi$ (de longitud potencialmente
    exponencial).
  - Acepta o rechaza en tiempo polinomial.

- **$r(n) = \log n$:** la aleatoriedad es logarítmica en $|x|$. Esto implica que
  el verificador elige entre $2^{\log n} = n$ posibles "preguntas" — polinómiamente
  muchas, pero el certificado no se lee entero.

- **$q = O(1)$:** el verificador lee solo un número **constante** de bits de la prueba
  (típicamente 3). Un observador que ve la prueba completa no obtiene más información
  que quien lee 3 bits al azar.

**Completitud y solidez:**
- Si $x \in L$: existe prueba $\pi$ tal que el verificador acepta con probabilidad 1.
- Si $x \notin L$: para toda prueba $\pi$, el verificador rechaza con probabilidad $\geq 1/2$.

### 2. El verificador de 3 bits para 3-SAT

El verificador para 3-SAT:
1. Con $\log n$ bits de aleatoriedad, elige una cláusula $C_i = (x_a \vee x_b \vee x_c)$ de la fórmula.
2. Lee los 3 bits de la prueba correspondientes a la asignación de $x_a, x_b, x_c$.
3. Acepta si y solo si la cláusula está satisfecha.

**Si la fórmula es satisfacible:** existe una asignación que satisface todas las
cláusulas. La prueba puede contener esa asignación. Para cualquier cláusula elegida,
el verificador acepta. Probabilidad de aceptación: **1**.

**Si la fórmula no es satisfacible:** toda asignación falla en al menos una
fracción $\epsilon > 0$ de las cláusulas. El verificador elige una cláusula
uniformemente al azar, y con probabilidad $\geq \epsilon$ elige una cláusula que
falla. Para que el rechazo sea $\geq 1/2$, se necesita $\epsilon \geq 1/2$ — es
decir, que cualquier asignación falle al menos en la mitad de las cláusulas.

Esto no es cierto para todas las instancias insatisfacibles, pero el verificador
PCP real usa una **codificación de error corrector** de la prueba que amplifica
el fallo hasta $\geq 1/2$.

### 3. PCP → inaproximabilidad de MAX-3SAT

**MAX-3SAT:** dada una 3-CNF, maximizar la fracción de cláusulas satisfechas.

**La barrera de 7/8:** por aleatoriedad, una asignación uniforme al azar satisface
cada cláusula de 3 literales con probabilidad $7/8$ en expectativa. Existe un
algoritmo aleatorizado trivial con ratio $7/8$.

**Teorema de Hastad (1997).** MAX-3SAT no puede aproximarse con ratio $> 7/8 + \epsilon$
para ningún $\epsilon > 0$, a menos que P = NP.

**Argumento:**

Si existiese un algoritmo de aproximación $A$ con ratio $> 7/8$, podríamos
decidir SAT:

1. Dado una fórmula $\phi$ con $m$ cláusulas:
   - Si $\phi$ es satisfacible: OPT = 1 (todas las cláusulas satisfechas). $A$
     devuelve $\geq (7/8 + \epsilon) > 7/8$ cláusulas satisfechas.
   - Si $\phi$ es insatisfacible (por el teorema PCP): existe $\delta > 0$ tal que
     toda asignación satisface a lo sumo $(7/8)$ fracción de cláusulas (tras
     reducción PCP apropiada). $A$ devuelve $\leq 7/8$ cláusulas.

2. La distinción entre los dos casos separa satisfacible de no satisfacible,
   decidiendo SAT en tiempo polinomial → P = NP.

**En la práctica:** el ratio $7/8$ es alcanzable (algoritmo SDP de Goemans-Williamson
para MAX-2SAT alcanza 0.878; MAX-3SAT tiene el ratio trivial 7/8). La barrera es óptima.

### 4. IP vs PCP: diferencias clave

| Característica | IP (Prueba Interactiva) | PCP (Probabilistically Checkable) |
|---------------|----------------------|----------------------------------|
| Rondas | Múltiples (polinómicas) | Una sola ronda (no interactivo) |
| Aleatoriedad | Pública o privada | Pública |
| Bits leídos | Todos los mensajes | Constante (O(1)) |
| Potencia | IP = PSPACE | PCP(log n, O(1)) = NP |
| Uso principal | Demostrar IP=PSPACE | Inaproximabilidad |

**Por qué PCP es más útil para inaproximabilidad:**

En un sistema IP, el verificador puede preguntar al probador sobre cualquier
bit, con interacción. En PCP, el verificador lee solo $O(1)$ bits de una
prueba **estática** (sin interacción). Esta restricción convierte el verificador
PCP en un "test de consistencia local" que puede usarse para construir gadgets
de inaproximabilidad.

La clave: si la prueba es inconsistente en una fracción $\delta$ de posiciones,
el verificador PCP la detecta con probabilidad $\geq \delta/q$ por su naturaleza
local. Los sistemas IP no tienen esta propiedad de detección local.

## Comentario

El teorema PCP fue votado por la comunidad teórica como uno de los resultados
más importantes del siglo XX en ciencias de la computación. Resolverse en 1992-1998
(Arora, Lund, Motwani, Sudan, Safra, Hastad) unificó la teoría de la aproximación
con la complejidad computacional: la "barra" de lo que es aproximable es un
reflejo directo de la estructura de las pruebas verificables probabilísticamente.

## Para seguir

Investiga el **Unique Games Conjecture (UGC)** de Khot (2002): si la UGC es cierta,
muchas barreras de inaproximabilidad son óptimas (vertex cover 2-aproximación es
óptima, MAX-CUT 0.878 es óptimo). ¿Cuál es la relación entre UGC y ETH?
