# Máquinas de Turing con oráculo y relativización

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Máquinas de Turing](04-maquinas-de-turing.md)
- [P y NP](../04-complejidad-computacional/01-p-np-y-np-completitud.md)

## Objetivos de aprendizaje

1. Definir máquinas de Turing con oráculo y su semántica.
2. Entender el teorema de Baker-Gill-Solovay y sus consecuencias.
3. Explicar por qué la diagonalización sola no puede separar P de NP.


## Intuición

¿Por qué es tan difícil demostrar que P ≠ NP? Una pista viene de la **relativización**: si añadimos a todas las máquinas acceso a un oráculo externo (una caja negra que responde preguntas), las clases de complejidad cambian de manera inconsistente. Para algunos oráculos P^A = NP^A; para otros P^A ≠ NP^A. Esto demuestra que cualquier prueba de P ≠ NP que también valga para todos los oráculos está condenada al fracaso. Este resultado —el teorema de Baker-Gill-Solovay— reorientó durante décadas la investigación en teoría de la complejidad.

## Máquinas de Turing con oráculo

Una **máquina de Turing con oráculo** $M^A$ tiene acceso a un conjunto $A \subseteq \{0,1\}^*$ como caja negra:

- Tiene una **cinta de consulta** especial.
- En cualquier paso, puede escribir una cadena $q$ en la cinta de consulta y entrar en el **estado de consulta** $q_{?}$.
- En el siguiente paso, la máquina recibe la respuesta: entra en $q_{sí}$ si $q \in A$, o en $q_{no}$ si $q \notin A$.
- La consulta ocupa un solo paso de tiempo, independientemente del tamaño de $q$.

Las clases relativizadas se definen análogamente:

$$\text{P}^A = \bigcup_{k} \text{DTIME}^A(n^k) \qquad \text{NP}^A = \bigcup_{k} \text{NTIME}^A(n^k)$$

donde el superíndice indica que las máquinas tienen acceso al oráculo $A$.

## El teorema de Baker-Gill-Solovay (1975)

**Teorema.** Existen oráculos $A$ y $B$ tales que:

$$\text{P}^A = \text{NP}^A \qquad \text{y} \qquad \text{P}^B \neq \text{NP}^B$$

### Construcción de A: oráculo que colapsa

Sea $A = \text{PSPACE}$. Entonces $\text{P}^A = \text{NP}^A = \text{PSPACE}^A = \text{PSPACE}$.

Cualquier consulta a $A$ permite resolver problemas PSPACE en tiempo constante, elevando todo a PSPACE. Las clases P y NP quedan aplastadas.

### Construcción de B: oráculo que separa

Sea $B$ un conjunto elegido de modo que:

$$L_B = \{1^n : \exists x \in \{0,1\}^n, x \in B\}$$

sea difícil para P^B pero fácil para NP^B. El argumento es:

- **NP^B acepta $L_B$:** el testigo es la cadena $x \in B$ de longitud $n$. Basta verificar la consulta en tiempo constante.
- **P^B no acepta $L_B$:** mediante una construcción diagonal. En la ronda $n$, si la máquina determinista $M_n$ hace menos de $2^{n/2}$ consultas (lo que ocurre en tiempo polinomial), puede verse que hay cadenas de longitud $n$ que $M_n$ no exploró. Se pone $B$ de modo que $M_n$ falle en esa longitud.

El argumento es una diagonalización que mezcla la potencia exponencial de NP (puede adivinar y verificar una cadena de longitud $n$ en tiempo polinomial) con la incapacidad de P para explorar los $2^n$ candidatos.

## Traza concreta: construyendo el oráculo B para n = 3

El argumento diagonal para el oráculo $B$ que separa se entiende mejor con un ejemplo numérico. Fijemos $n = 3$: queremos que $L_B = \{1^3\} \in \text{NP}^B \setminus \text{P}^B$.

**Paso 1 — Candidatos de longitud 3.** Hay $2^3 = 8$ cadenas de longitud 3:

```
000  001  010  011  100  101  110  111
```

Inicialmente, ninguna pertenece a $B$.

**Paso 2 — La MT determinista $M_1$ hace consultas en tiempo polinomial.** Supongamos que $M_1$, la primera MT de la enumeración, ejecuta en $n^2 = 9$ pasos sobre entrada $1^3$ y realiza a lo sumo $\lfloor 2^{3/2} \rfloor = 2$ consultas (cota de la construcción: $< 2^{n/2}$ consultas).

Supón que $M_1$ consulta `010` y `101`. Decide que $1^3 \notin L_B$ (output 0).

**Paso 3 — Ajuste de $B$.** Las 6 cadenas de longitud 3 no consultadas son: `000`, `001`, `011`, `100`, `110`, `111`. Elegimos **poner `011` en $B$** (cualquiera de las no consultadas sirve). Ahora $\exists x \in \{0,1\}^3 : x \in B$ (a saber, `011`), así que $1^3$ *debería* estar en $L_B$.

Pero $M_1$ nunca consultó `011`, de modo que su respuesta (output 0) es **incorrecta**: $M_1$ rechaza $1^3$ aunque $1^3 \in L_B$. Diagonalizamos: $M_1$ falla en la longitud $n = 3$.

**Paso 4 — NP^B acepta trivialmente.** La MT no determinista adivina $x = \text{`011'}$ y consulta $B$: `011` ∈ B → acepta. Un paso de oráculo.

**Paso 5 — Iteración.** Se repite para $n = 4, 5, \ldots$ con la siguiente MT $M_2, M_3, \ldots$ de la enumeración. En cada ronda $n$, la MT determinista $M_n$ hace $< 2^{n/2}$ consultas, dejando al menos $2^n - 2^{n/2}$ cadenas de longitud $n$ sin examinar; se pone una en $B$ (o no, según sea necesario para que la MT falle). El conjunto $B$ resultante es un oráculo perfectamente definido.

**Conclusión numérica.** Con $n = 3$ y $M_1$ haciendo 2 consultas, bastó **1 cadena** añadida a $B$ para que $M_1$ fallara. Esto ilustra la asimetría central: NP^B puede verificar en 1 paso no determinista lo que P^B no puede encontrar en tiempo polinomial.

## ¿Qué implica la relativización para P vs NP?

El teorema de Baker-Gill-Solovay no prueba ni que P = NP ni que P ≠ NP. Su implicación es **metalógica**:

> Cualquier demostración de P = NP o P ≠ NP que use solo **diagonalización** y **simulación** se puede relativizar a cualquier oráculo, y por tanto no puede funcionar: para algún oráculo daría la respuesta equivocada.

Las técnicas que no se relativizan incluyen:

- **Circuitos booleanos de tamaño polinomial** (usado en el teorema de Karp-Lipton).
- **Álgebra lineal y polinomios** (base del método de la aproximación).
- **Sumas y verificadores interactivos** (IP = PSPACE, que sí se relativiza de forma no trivial).

## Técnicas no relativizantes

### Algebrización

La **algebrización** (Aaronson-Wigderson 2009) extiende el concepto de relativización: en lugar de consultas a $A$, se permite consultar la **extensión algebraica** $\hat{A}$ de $A$ (el polinomio sobre un cuerpo finito que extiende la función característica de $A$). La mayoría de las técnicas conocidas algebrizan, lo que sigue sin ser suficiente para resolver P vs NP.

### El método de la complejidad de circuitos

Resultados como el teorema de Razborov-Smolensky (funciones de paridad requieren circuitos AC⁰ de tamaño superpolinomial) no se pueden formular como preguntas sobre oráculos clásicos. Son resultados **no relativizantes** que han tenido éxito parcial.

## Jerarquía de oráculos y complejidad

El formalismo de máquinas con oráculo también permite definir la jerarquía polinómica:

$$\Sigma_0^P = \Pi_0^P = P$$
$$\Sigma_{k+1}^P = \text{NP}^{\Sigma_k^P}$$
$$\Pi_{k+1}^P = \text{coNP}^{\Sigma_k^P}$$

Si P = NP, entonces la jerarquía polinómica colapsa a P. El teorema de Karp-Lipton dice que si NP ⊆ P/poly, la jerarquía colapsa a $\Sigma_2^P$.

## El teorema de la jerarquía con oráculos

Para la computabilidad sin restricción de tiempo, el oráculo de salto $K$ satisface:

$$\text{Decidible}^K = \Sigma_2^0 \cap \Pi_2^0 = \Delta_2^0$$

Las MT que deciden con oráculo $K$ resuelven exactamente los problemas de nivel $\Delta_2^0$ en la jerarquía aritmética. Esto muestra cómo los oráculos "compran" poder computacional en niveles discretos.

## Ideas clave

1. Una MT con oráculo puede consultar a un conjunto externo en tiempo constante por consulta.
2. El teorema Baker-Gill-Solovay (1975): existen oráculos que hacen P=NP y otros que hacen P≠NP.
3. Esto implica que las técnicas de diagonalización y simulación puras no pueden resolver P vs NP.
4. Las técnicas "no relativizantes" (algebrización, circuitos) son las candidatas a producir una prueba real.
5. Los oráculos generan la jerarquía polinómica y la jerarquía aritmética de forma uniforme.

## Ejercicios

1. Define formalmente $\text{PSPACE}^A$ para un oráculo $A$. ¿Por qué $\text{NP}^{\text{PSPACE}} = \text{PSPACE}$?

2. Explica en qué sentido el argumento diagonal de Baker-Gill-Solovay para B es análogo a la diagonalización de Cantor.

3. ¿Por qué el resultado IP = PSPACE (sistemas de prueba interactivos) no se relativiza trivialmente y fue un avance importante?

4. Si la jerarquía polinómica colapsara a $\Sigma_3^P$, ¿qué implicaría eso sobre la relación entre NP y coNP?

## Véase también

- [Jerarquía aritmética](10-jerarquia-aritmetica.md)
- [P, NP y NP-completitud](../04-complejidad-computacional/01-p-np-y-np-completitud.md)



<!-- nav-start -->

---
← [Jerarquía aritmética](10-jerarquia-aritmetica.md) · [Aleatoriedad algorítmica](12-aleatoriedad-algoritmica.md) →

<!-- nav-end -->
## Referencias

- Baker, T., Gill, J. y Solovay, R. (1975). Relativizations of the P=?NP question. *SIAM J. Computing*, 4(4), 431–442.
- Aaronson, S. y Wigderson, A. (2009). Algebrization: A new barrier in complexity theory. *ACM TOCT*, 1(1), 1–54.
- Arora, S. y Barak, B. (2009). *Computational Complexity: A Modern Approach*, cap. 3 y 14. Cambridge.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., cap. 9. Cengage.
