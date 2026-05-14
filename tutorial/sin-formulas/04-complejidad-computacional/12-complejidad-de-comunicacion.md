> **Nota:** Esta es la versión sin fórmulas LaTeX de [12-complejidad-de-comunicacion](../../04-complejidad-computacional/12-complejidad-de-comunicacion.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Complejidad de comunicación

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)

## Objetivos de aprendizaje

1. Definir el modelo Alice-Bob y la complejidad de comunicación D(f).
2. Demostrar el lower bound de igualdad Ω(n) con el argumento de rango.
3. Conectar la complejidad de comunicación con lower bounds de circuitos.


## Intuición

Dos jugadores, Alicia y Bob, tienen entradas `x` e `y` respectivamente. Quieren calcular conjuntamente una función `f(x, y)` intercambiando la menor cantidad posible de bits. La **complejidad de comunicación** estudia cuántos bits necesitan intercambiar en el peor caso, independientemente del poder computacional de cada uno. El modelo es sorprendentemente rico: permite demostrar cotas inferiores para circuitos, memoria de computadores y complejidad espacial que serían muy difíciles de obtener de otro modo.

## El modelo básico

**Protocolo de dos partes:**
- Alicia tiene `x ∈ 𝒳`, Bob tiene `y ∈ 𝒴`.
- Se alternan enviando bits según una función determinista de su entrada y lo que han recibido hasta el momento.
- Al final, alguna de las partes (o ambas) conoce `f(x, y)`.

La **complejidad de comunicación determinista** `D(f)` es el número de bits transmitidos en el peor caso por el mejor protocolo:


> **Fórmula:** `D(f) = min_protocolo  P max_x, y bits(P, x, y)`


## Matrices de comunicación y rectángulos

Representamos `f: 𝒳 × 𝒴 → \{0,1\}` como una matriz `M_f` con `M_f[x][y] = f(x,y)`.

Un **rectángulo combinatorio** es un subconjunto `R = A × B ⊆ 𝒳 × 𝒴`. Los rectángulos son los bloques indivisibles de la comunicación: en un nodo hoja del árbol de comunicación, el conjunto de `(x,y)` que llegaron a ese nodo es siempre un rectángulo.

**Lema.** En cualquier protocolo determinista de `c` bits, el árbol de comunicación tiene a lo sumo `2^c` hojas, y cada hoja corresponde a un rectángulo monócromo (todos 0 o todos 1).

**Corolario.** `D(f) ≥ log_2 C(f)`, donde `C(f)` es el número mínimo de rectángulos monocromos que recubren la matriz.

## El problema de igualdad (EQ)

El problema de igualdad: `EQ_n(x, y) = 1` si y solo si `x = y`, para `x, y ∈ \{0,1\}^n`.

**Cotas:**
- `D(EQ_n) ≤ n + 1` bits: Alicia envía `x`, Bob compara.
- `D(EQ_n) ≥ n + 1` bits: la demostración usa que la matriz de EQ es la identidad `n × n`, que requiere `2^n` rectángulos monocromos.

**Protocolo aleatorizado:** con errores tolerados hasta `1/3`, el protocolo de hashing de Freivalds usa solo `O(log n)` bits:
1. Bob elige primo aleatorio `p ≈ n²`.
2. Bob envía `y \mod p` a Alicia.
3. Alicia verifica si `x \mod p` coincide.

Si `x = y`, siempre correcto. Si `x ≠ y`, la probabilidad de error es `O(1/n)`.

## Métodos para cotas inferiores

### El rango (rank lower bound)

**Lema del rango.** `D(f) ≥ log_2 rank(M_f)` donde el rango es sobre `ℝ`.

Para EQ: la matriz es la identidad, rango `= 2^n`, cota inferior `= n`.

El rango sobre `𝔽_2` da la cota para protocolos de paridad.

### El método de la cubierta (covering bound)

`D(f) ≥ log_2 C(f)` donde `C(f)` es el número mínimo de rectángulos monocromos que cubren `M_f`.

### El método de discrepancia

La **discrepancia** de `f` respecto a una distribución `μ` sobre `𝒳 × 𝒴` es:


> **Fórmula:** `disc_μ(f) = max_R  rectángulo ≤ft|μ(R ∩ f⁻¹(1)) - μ(R ∩ f⁻¹(0))|`


**Lema.** `R^(1/3)(f) ≥ 1/2 log_2 1/disc_μ(f)` para todo `μ`, donde `R^(1/3)` es la complejidad aleatoria con error `≤ 1/3`.

La discrepancia pequeña implica alta complejidad de comunicación. Se usa para demostrar cotas para IP (producto interno modular 2).

## El problema del producto interno (IP)

`IP_n(x, y) = ⟨ x, y ⟩ \mod 2 = Σ_i x_i y_i \mod 2`.

**Teorema.** `R^(1/3)(IP_n) = Θ(n)`.

Demostración de cota inferior: la discrepancia de IP con distribución uniforme es `2^(-n/2)`, que da `R^(1/3) ≥ n/2`.

Cota superior: `O(n)` bits obviamente basta. IP es "dura" incluso para protocolos aleatorios.

## Complejidad de comunicación multipartita

**Modelo número en frente (number-in-hand):** `k` jugadores `P_1, …, P_k` tienen entradas `x_1, …, x_k`. Todos los mensajes son públicos (pizarra compartida). La complejidad de comunicación es el número total de bits escritos.

**Modelo número en cabeza (number-on-forehead):** el jugador `P_i` ve todas las entradas **excepto** `x_i`. Este modelo está relacionado con circuitos de profundidad constante (AC⁰): cotas inferiores en complejidad de comunicación con cabeza implican cotas de circuitos.

## Aplicaciones a circuitos y espacio

### Cotas de circuitos (AC⁰)

Razborov (1987) y Smolensky (1987) usaron variantes de argumentos de comunicación para demostrar que la función mayoría requiere circuitos de AC⁰ exponencialmente grandes. Hastad demostró en 1988 que la paridad requiere profundidad `Ω(log n / log log n)` en AC⁰.

### Complejidad espacial (PSPACE)

**Teorema de Lund et al.** IP = PSPACE. La demostración usa protocolos de comunicación interactivos (verificadores) que permiten verificar en `O(n)` rondas y espacio polinomial cosas que parecerían requerir exponencial.

### Complejidad de streaming

En el modelo de **streaming** un algoritmo procesa una secuencia de datos con memoria limitada. Muchas cotas inferiores de memoria en streaming se demuestran reduciendo el problema a un problema de comunicación de dos partes.

## Ideas clave

1. La complejidad de comunicación mide los bits intercambiados para calcular `f(x,y)` en el peor caso.
2. La matriz `M_f` y sus rectángulos monocromos son la estructura fundamental del análisis.
3. Métodos de cota inferior: rango, cubierta, discrepancia.
4. El problema EQ requiere `Ω(n)` bits deterministas pero solo `O(log n)` aleatorios.
5. Las cotas de comunicación implican cotas de circuitos, espacio y streaming.

## Ejercicios

1. Calcula el rango sobre `ℝ` de la matriz `M_AND_n` donde `AND_n(x,y) = x \wedge y` para `x,y ∈ \{0,1\}`. ¿Qué cota inferior da para `D(AND_n)`?

2. Diseña un protocolo de comunicación de `⌈ log_2 n ⌉ + 1` bits para calcular `GT_n(x,y) = [x > y]` (mayor-que) con entradas de `n` bits.

3. ¿Por qué el protocolo de hashing para EQ requiere que `p` sea mucho mayor que `x` e `y`? ¿Qué pasa si `p` es demasiado pequeño?

4. Demuestra que `D(f) ≤ min(|𝒳|, |𝒴|) + 1` para cualquier función `f`.

## Véase también

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Información mutua](../02-teoria-informacion/02-informacion-mutua.md)


## Referencias

- Kushilevitz, E. y Nisan, N. (1997). *Communication Complexity*. Cambridge University Press.
- Razborov, A.A. (1992). On the distributional complexity of disjointness. *Theoretical Computer Science*, 106(2), 385–390.
- Raz, R. (1992). On the complexity of matrix product. *Proc. STOC*, 144–151.
- Arora, S. y Barak, B. (2009). *Computational Complexity*, cap. 13. Cambridge.
