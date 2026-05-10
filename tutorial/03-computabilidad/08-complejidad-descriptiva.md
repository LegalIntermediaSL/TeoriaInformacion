# Complejidad Descriptiva

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Máquinas de Turing](04-maquinas-de-turing.md)
- [P y NP](../04-complejidad-computacional/01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Enunciar el teorema de Fagin: NP = ∃SO.
2. Expresar 3-colorabilidad como una fórmula de segundo orden existencial.
3. Entender cómo la lógica de punto fijo captura la clase P.


## Intuición

La complejidad computacional habitual mide cuántos pasos necesita un algoritmo. La
**complejidad descriptiva** hace una pregunta diferente: ¿qué fragmento de lógica matemática
es necesario para *describir* los lenguajes de una clase de complejidad? El resultado
sorprendente es que las clases P, NP, PSPACE tienen caracterizaciones lógicas precisas,
sin mencionar máquinas, tiempo ni espacio.

## Lógica de primer orden sobre estructuras finitas

Las **estructuras finitas** son grafos, cadenas, matrices y otros objetos combinatorios.
Una estructura sobre un vocabulario $\sigma$ es una tupla $\mathcal{A} = (A, R_1, \ldots, R_k)$
donde $A$ es el dominio finito y cada $R_i$ es una relación sobre $A$.

La **lógica de primer orden** (FO) sobre $\sigma$ usa:
- Variables de individuo $x, y, z, \ldots$ que recorren elementos de $A$.
- Cuantificadores $\forall x, \exists x$.
- Conectivos booleanos $\wedge, \vee, \neg$.
- Relaciones de $\sigma$ y la igualdad.

**Ejemplo:** la fórmula $\phi(x) = \exists y \, E(x,y)$ expresa "el nodo $x$ tiene al menos
un vecino" en un grafo con relación de aristas $E$.

## FO y AC0

**Teorema (Immerman-Vardi).** La clase de consultas sobre estructuras ordenadas expresables
en FO es exactamente **AC0**: los problemas reconocibles por circuitos de profundidad constante
y tamaño polinomial.

La orden es crucial: sin ella, FO ni siquiera puede expresar si un grafo tiene un número
par de nodos (problema de paridad, que no está en AC0).

**Consecuencias:**

- La conectividad de un grafo ($\exists$ camino entre dos nodos) no es expresable en FO.
  Requiere cuantificadores de segundo orden o el punto fijo.
- Las propiedades locales (grado de un nodo, existencia de un triángulo) sí son expresables en FO.

## Cierre bajo punto fijo: la clase P

Para capturar P se necesita potencia expresiva adicional. El operador de **punto fijo mínimo**
(LFP) extiende FO con la capacidad de definir relaciones inductivamente:

$$\text{LFP}[x, \phi(P, x)] = \text{la relación más pequeña } P \text{ tal que } \phi(P, x) \leftrightarrow P(x)$$

**Teorema (Immerman 1986, Vardi 1982).** Sobre estructuras ordenadas:

$$\text{P} = \text{FO + LFP}$$

Todo lenguaje decidible en tiempo polinomial puede describirse como la consulta de
una fórmula FO con operador de punto fijo mínimo sobre estructuras ordenadas finitas,
y viceversa.

**Ejemplo:** la conectividad de grafos ordenados es expresable con LFP:
Alcanzabilidad $(s, t)$ es el punto fijo de $R(x) \leftarrow x=s \vee \exists y(R(y) \wedge E(y,x))$.

## Segundo orden existencial: el teorema de Fagin

La **lógica de segundo orden** (SO) permite cuantificar sobre relaciones, no solo sobre
elementos. El fragmento **existencial de segundo orden** (∃SO) usa cuantificadores
existenciales $\exists R_1 \ldots \exists R_k$ seguidos de una fórmula de primer orden.

**Teorema de Fagin (1974).** Sobre estructuras finitas:

$$\text{NP} = \exists\text{SO}$$

Un lenguaje está en NP si y solo si puede expresarse como: "existe una relación $R$ tal que
la estructura extendida con $R$ satisface una propiedad de primer orden."

### Ejemplo numérico: 3-colorabilidad en ∃SO

El lenguaje 3-COLOR = $\{G : G \text{ es 3-coloreable}\}$ está en NP. Veamos su fórmula ∃SO:

$$\exists C_1 \exists C_2 \exists C_3 \;\Big[\underbrace{\forall x\,(C_1(x) \lor C_2(x) \lor C_3(x))}_{\text{todo vértice tiene color}} \;\land\; \underbrace{\forall x\,\neg(C_1(x) \land C_2(x))}_{\text{colores exclusivos}}\cdots\land\; \underbrace{\forall x\,\forall y\,(E(x,y) \to \neg\text{IgualColor}(x,y))}_{\text{aristas: colores distintos}}\Big]$$

**Estructura concreta:** para el triángulo $K_3 = \{1,2,3\}$ con aristas $\{(1,2),(2,3),(1,3)\}$:
- Asignamos $C_1 = \{1\}$, $C_2 = \{2\}$, $C_3 = \{3\}$.
- La fórmula se satisface: cada vértice tiene exactamente un color y no hay arista monocromática.
- Por tanto $K_3 \in$ 3-COLOR y la fórmula ∃SO es un certificado de su pertenencia a NP.

**Ejemplo:** 3-colorabilidad de grafos:

$$\exists C_1 \exists C_2 \exists C_3 \Bigl[ \forall x (C_1(x) \vee C_2(x) \vee C_3(x)) \wedge \forall x (\neg(C_1(x) \wedge C_2(x))) \wedge \ldots \wedge \forall x y (E(x,y) \to \neg \exists i (C_i(x) \wedge C_i(y))) \Bigr]$$

La relación existencialmente cuantificada $C_i$ corresponde al **certificado** del problema de NP.

**El teorema de Fagin tiene varias consecuencias:**

1. La clase de propiedades de grafos expresables en ∃SO está cerrada bajo complemento si y solo
   si NP = co-NP.
2. Caracteriza NP sin mencionar tiempo ni espacio: puramente en términos de la lógica.
3. La transformación de Fagin convierte cualquier fórmula ∃SO en una MT no determinista polinomial.

## SO universal y PSPACE

El fragmento **universal de segundo orden** (∀SO) captura co-NP. La lógica de segundo orden
completa (SO, con cuantificadores alternados) captura la **jerarquía polinómica** PH.

**Teorema.** $\text{PSPACE} = \text{FO + PFP}$ (punto fijo parcial, que permite que la
iteración no converja).

## Lógica modal y tiempo

Las lógicas modales (LTL, CTL) son fragmentos de FO que capturan propiedades de sistemas
de transición:

- **CTL** (Computation Tree Logic): propiedades de caminos en árboles de cómputo.
  Model checking en CTL es P-completo.
- **LTL** (Linear Temporal Logic): propiedades de caminos lineales.
  Model checking en LTL es PSPACE-completo.

La complejidad del model checking refleja la expresividad de la lógica: LTL habla de caminos
individuales (más difícil) mientras que CTL puede alternar cuantificadores en el árbol.

## El teorema de Büchi-Elgot-Trakhtenbrot

Sobre cadenas finitas, los lenguajes regulares se caracterizan exactamente por FO:

**Teorema.** Un lenguaje de cadenas es regular si y solo si es definible en FO con aritmética
sobre posiciones (lógica MSO monádica de segundo orden = FO + cuantificación sobre conjuntos).

Más precisamente: regulares = MSO; FO sin cuantificación de conjuntos captura exactamente los
lenguajes *sin prefijo de estrella* (star-free languages), que son los lenguajes regulares
reconocibles por autómatas sin ciclos.

## Complejidad descriptiva: resumen

| Clase de complejidad | Caracterización lógica |
|---------------------|----------------------|
| AC0 | FO (primer orden) |
| P | FO + LFP (punto fijo mínimo, sobre estructuras ordenadas) |
| NP | ∃SO (segundo orden existencial) |
| co-NP | ∀SO (segundo orden universal) |
| PH | SO (segundo orden completo) |
| PSPACE | FO + PFP (punto fijo parcial) |
| Lenguajes regulares | MSO sobre cadenas finitas |

## Ideas clave

- La complejidad descriptiva conecta la teoría de la complejidad computacional con la lógica
  matemática: las clases de complejidad son clases de definibilidad lógica.
- El teorema de Fagin (NP = ∃SO) fue el primer resultado de este tipo; establece que los
  certificados de NP corresponden a relaciones existencialmente cuantificadas.
- El teorema de Immerman-Vardi (P = FO+LFP sobre estructuras ordenadas) conecta la
  inducción matemática (punto fijo) con la computación polinomial.
- La ausencia de orden en la estructura puede hacer que lenguajes más ricos sean no expresables
  en FO; el orden actúa como "memoria" para la lógica.
- Los sistemas de model checking (CTL, LTL) son fragmentos de FO con complejidad P-completa y PSPACE-completa respectivamente.

## Ejercicios

1. Escribe una fórmula FO que exprese "el grafo tiene un nodo de grado exactamente $k$" para
   $k$ fijo. ¿Podría escribirse para $k$ como variable?
2. Escribe la fórmula ∃SO que expresa que un grafo tiene un clique de tamaño 3.
3. ¿Por qué la conectividad de grafos no es expresable en FO? (Pista: usa el teorema de
   Ehrenfeucht-Fraïssé.)
4. Justifica por qué la definición inducción de alcanzabilidad con LFP converge en a lo
   sumo $|A|$ pasos para un grafo con $|A|$ nodos.
5. Explica la conexión entre el teorema de Fagin y la definición de NP como "decidible por
   una MT no determinista en tiempo polinomial".

## Véase también

- [P, NP y NP-completitud](../04-complejidad-computacional/01-p-np-y-np-completitud.md)
- [El teorema PCP](../04-complejidad-computacional/09-teorema-pcp.md)


## Referencias

- Immerman, N. (1999). *Descriptive Complexity*. Springer.
- Fagin, R. (1974). Generalized first-order spectra and polynomial-time recognizable sets.
  *SIAM-AMS Proceedings*.
- Ebbinghaus, H. D. y Flum, J. (1999). *Finite Model Theory*. Springer.
