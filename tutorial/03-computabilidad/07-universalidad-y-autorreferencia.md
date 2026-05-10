# Universalidad y Autorreferencia

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Máquinas de Turing](04-maquinas-de-turing.md)
- [El problema de la parada](01-problema-de-la-parada.md)

## Objetivos de aprendizaje

1. Construir una máquina de Turing universal (UTM).
2. Comprender el teorema del punto fijo de Kleene (teorema del quine).
3. Relacionar la autorreferencia con la indecidibilidad y los quines.


## Intuición

Una máquina de Turing puede simular a otra: basta con codificar la descripción de la máquina simulada en la cinta. Esta idea —que un programa puede operar sobre otros programas— está en el corazón de la computación moderna y de los resultados más profundos sobre los límites del cómputo.

## La máquina de Turing universal (UTM)

Una **máquina de Turing universal** $U$ toma como entrada la descripción $\langle M \rangle$ de una máquina de Turing $M$ y una entrada $w$, y simula el comportamiento de $M$ sobre $w$:

$$U(\langle M \rangle, w) = M(w)$$

La existencia de la UTM no es obvia: requiere que la descripción $\langle M \rangle$ sea una codificación finita y que $U$ pueda interpretar esa codificación como instrucciones.

**Construcción esquemática:** la UTM usa tres porciones de su cinta:
1. La descripción de $M$ (función de transición).
2. La simulación de la cinta de $M$.
3. El estado actual de $M$.

En cada paso, $U$ consulta el estado actual y el símbolo bajo el cabezal de $M$ (usando la porción 3 y 2), busca la transición correspondiente en la descripción de $M$ (porción 1), y actualiza la simulación.

**Complejidad:** simular $T$ pasos de $M$ en la UTM cuesta $O(T \cdot |\langle M \rangle|)$ pasos; hay una sobrecarga logarítmica en el tamaño de la descripción.

## Codificación de máquinas de Turing

Para que la UTM funcione, las máquinas deben tener una representación finita y uniforme. Se puede usar una codificación binaria estándar:

- Enumerar los estados como $q_1, q_2, \ldots$
- Enumerar los símbolos de cinta.
- Codificar cada transición $(q_i, a) \mapsto (q_j, b, d)$ como una tupla binaria.
- Concatenar todas las transiciones con separadores.

Esto produce una biyección entre cadenas binarias y máquinas de Turing (con algunas cadenas que no corresponden a máquinas válidas, que se tratan como la MT que rechaza todo). Así, $\langle M \rangle$ es simplemente un número natural que describe $M$.

## El teorema del punto fijo (teorema de Kleene)

**Teorema.** Para cualquier función computable $f$, existe una máquina de Turing $M$ tal que $M$ y $f(\langle M \rangle)$ computan la misma función.

Intuitivamente: siempre existe un programa que se comporta igual que cualquier transformación computable aplicada a su propia descripción.

**Demostración.** Sea $q(w)$ la máquina que calcula $\langle M_w \rangle$, la descripción de la máquina que, al recibir una entrada $x$, primero computa $w$ y luego simula $M_w(x)$. Define $h(\langle M \rangle) = f(\langle M_{\langle M \rangle} \rangle)$. Entonces $M = M_{\langle h \rangle}$ es el punto fijo buscado.

**Consecuencia.** El teorema del punto fijo formaliza la autorreferencia: podemos construir programas que razonan sobre su propio código.

## Autorreferencia y el problema de la parada

La autorreferencia está en el corazón de la indecidibilidad del problema de la parada. La demostración clásica es una diagonalización:

Supongamos que existe una MT $H$ que decide si $M$ se detiene sobre $w$:
$$H(\langle M \rangle, w) = \begin{cases} \text{acepta} & \text{si } M(w) \text{ se detiene} \\ \text{rechaza} & \text{en otro caso} \end{cases}$$

Construye $D(\langle M \rangle)$ que:
- Simula $H(\langle M \rangle, \langle M \rangle)$.
- Si $H$ acepta (es decir, $M$ se detiene sobre $\langle M \rangle$): entra en bucle infinito.
- Si $H$ rechaza: acepta.

Evaluando $D(\langle D \rangle)$:
- Si $D$ se detiene sobre $\langle D \rangle$: $H$ acepta, entonces $D$ entra en bucle → contradicción.
- Si $D$ no se detiene sobre $\langle D \rangle$: $H$ rechaza, entonces $D$ acepta → contradicción.

La máquina $D$ no puede existir, luego $H$ tampoco.

## El teorema de Rice

**Teorema (Rice, 1953).** Cualquier propiedad no trivial del lenguaje de una MT es indecidible.

Una propiedad de lenguajes $P$ es:
- **Trivial** si es satisfecha por todos los lenguajes o por ninguno.
- **No trivial** en otro caso.

**Ejemplos de propiedades no triviales (todas indecidibles):**
- "La MT acepta la cadena vacía."
- "El lenguaje de la MT es regular."
- "La MT se detiene en todas las entradas."
- "La MT acepta exactamente 3 cadenas."

**Demostración (esquema).** Sea $P$ una propiedad no trivial y sea $L_P$ el lenguaje de todas las codificaciones $\langle M \rangle$ de MTs que satisfacen $P$. Se puede reducir el problema de la parada a $L_P$: dado $(\langle M \rangle, w)$, construye $M'$ que simula $M$ sobre $w$ y, si $M$ se detiene, se comporta como una MT de referencia que satisface o no satisface $P$.

**Alcance del teorema.** El teorema de Rice dice que no se puede saber nada no trivial sobre qué computa un programa solo analizando su código (análisis estático es computacionalmente limitado). Esto tiene implicaciones directas en verificación de programas, análisis de malware y compilación.

## Conexión con la incompletitud de Gödel

El segundo teorema de incompletitud de Gödel (1931) y la indecidibilidad del problema de la parada (Turing, 1936) comparten la misma estructura lógica:

| Gödel | Turing |
|-------|--------|
| Sistema formal $F$ | Máquina de Turing $H$ |
| Fórmula "Esta fórmula es indemostrable en $F$" | Máquina $D$ que se contradice |
| $F$ no puede demostrar su propia consistencia | $H$ no puede decidir el problema de la parada |
| Incompletitud | Indecidibilidad |

Ambos resultados se formalizan mediante **autorreferencia codificada**: en Gödel, la codificación de fórmulas mediante números (números de Gödel); en Turing, la codificación de máquinas como cadenas binarias.

Church (1936), Kleene (1936) y Post (1936) llegaron independientemente a resultados equivalentes usando diferentes formalismos: el cálculo lambda de Church, las funciones recursivas de Kleene y los sistemas de producción de Post.

## Variantes de la UTM

La UTM mínima es un objeto de estudio propio. Se busca la máquina más pequeña (en número de estados y símbolos) que sea universal:

- La UTM más pequeña conocida tiene **2 estados y 18 símbolos** (Minsky, 1962).
- Con 3 símbolos: **2 estados y 3 símbolos** (Wolfram, 2002).
- Con 4 estados: **4 estados y 6 símbolos**.

El problema de determinar si una MT de 2 estados y 3 símbolos es universal fue objeto de un premio de Wolfram Research; fue resuelto afirmativamente en 2007 por Alex Smith.

## Ideas clave

- La UTM establece que existe un único "computador universal": cualquier cómputo puede simularse por un único programa que recibe los datos y el programa como entrada.
- El teorema del punto fijo garantiza que siempre existen programas autorreferenciales con cualquier propiedad computable.
- La indecidibilidad del problema de la parada y el teorema de Rice muestran los límites del análisis estático de programas.
- La estructura de autorreferencia diagonal es la herramienta matemática unificadora de la incompletitud de Gödel y la indecidibilidad de Turing.
- Los quines (programas que imprimen su propio código) existen en cualquier lenguaje Turing-completo; son consecuencia directa del teorema del punto fijo de Kleene.

## Ejercicios

1. Describe cómo codificarías una MT de 3 estados y 2 símbolos como cadena binaria.
2. Usa el teorema del punto fijo para mostrar que existe una MT $M$ tal que $M(\langle M \rangle)$ acepta y $M(w)$ rechaza para todo $w \neq \langle M \rangle$.
3. Aplica el teorema de Rice para demostrar que es indecidible si la MT $M$ acepta exactamente las cadenas de longitud par.
4. ¿Por qué el análisis estático de programas (linting, verificación formal) no puede ser completo? Relaciona con el teorema de Rice.
5. Esboza la diferencia entre los formalismos de Church (cálculo lambda) y Turing (MT): ¿son equivalentes? ¿Qué establece la tesis de Church-Turing?

## Véase también

- [Máquinas de Turing](04-maquinas-de-turing.md)
- [Complejidad de Kolmogorov](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)


## Referencias

- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., capítulos 3-5.
- Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proc. London Math. Soc.*
- Kleene, S. C. (1952). *Introduction to Metamathematics*. North-Holland.
- Rice, H. G. (1953). Classes of recursively enumerable sets and their decision problems. *Trans. Amer. Math. Soc.*
