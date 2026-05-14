> **Nota:** Esta es la versión sin fórmulas LaTeX de [10-jerarquia-aritmetica](../../03-computabilidad/10-jerarquia-aritmetica.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Jerarquía aritmética

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [El problema de la parada](01-problema-de-la-parada.md)
- [Decidibilidad](02-decidibilidad-y-reconocibilidad.md)

## Objetivos de aprendizaje

1. Definir los niveles Σ₀, Σ₁, Π₁ y Δ₁ de la jerarquía aritmética.
2. Clasificar problemas canónicos (parada, TOT, FIN) en la jerarquía.
3. Entender el operador de salto de Turing y cómo genera la jerarquía.


## Intuición

El problema de la parada es indecidible, pero no todos los problemas indecidibles son igual de difíciles. Algunos son más indecidibles que otros: no se pueden resolver incluso con acceso a un oráculo que decide el problema de la parada. La **jerarquía aritmética** es una clasificación fina de los lenguajes de acuerdo con la complejidad de las fórmulas lógicas que los definen, y captura esta estructura graduada de dificultad.

## Tabla resumen de la jerarquía aritmética

| Clase | Cuantificadores | Nombre informal | Ejemplo canónico | Oráculo equivalente |
|-------|----------------|-----------------|-----------------|---------------------|
| `Δ_0⁰ = Σ_0⁰ = Π_0⁰` | Ninguno (acotados) | Decidible / computable | "¿es `n` primo?" | — |
| `Σ_1⁰` | `∃` (existencial) | Reconocible (RE) | Problema de la parada `\{⟨ M,w⟩ : M(w)\downarrow\}` | — |
| `Π_1⁰` | `∀` (universal) | Co-reconocible (coRE) | "`M` no se detiene en `w`" | — |
| `Δ_1⁰` | `∃ ∩ ∀` | Decidible (clasif. exacta) | Todos los lenguajes regulares | `∅` |
| `Σ_2⁰` | `∃∀` | RE relativo a `∅'` | "`M` se detiene en infinitas entradas" | `∅'` (HALT) |
| `Π_2⁰` | `∀∃` | coRE relativo a `∅'` | `TOT`: "`M` se detiene en toda entrada" | `∅'` |
| `Δ_2⁰` | `∃∀ ∩ ∀∃` | Decidible con HALT | Problema de la parada con tiempo acotado | `∅'` |
| `Σ_3⁰` | `∃∀∃` | RE relativo a `∅''` | "`L(M)` es infinito" | `∅''` |
| `Σ_n⁰` | `n` alternaciones (`∃` primero) | RE relativo a `∅^((n-1))` | — | `∅^((n-1))` |
| `Π_n⁰` | `n` alternaciones (`∀` primero) | coRE relativo a `∅^((n-1))` | — | `∅^((n-1))` |
| `Δ_n⁰` | Intersección | Decidible con oráculo nivel `n-1` | — | `∅^((n-1))` |

## Definiciones básicas

Un lenguaje `L ⊆ \{0,1\}^*` es **aritméticamente definible** si se puede expresar mediante una fórmula de primer orden sobre los naturales con cuantificadores sobre enteros y predicados computables.

La jerarquía se define por el número y alternancia de cuantificadores al inicio de la fórmula:

### Niveles de la jerarquía

| Clase | Definición | Intuición |
|-------|-----------|-----------|
| `Σ_0⁰ = Π_0⁰ = Δ_0⁰` | Decidible (sin cuantificadores no acotados) | Computable |
| `Σ_1⁰` | `∃ x_1 ∃ x_2 … R(n, x̄)` con `R` decidible | Reconocible (RE) |
| `Π_1⁰` | `∀ x_1 ∀ x_2 … R(n, x̄)` | Co-reconocible (co-RE) |
| `Σ_2⁰` | `∃ ∀ R(n, x̄)` | Verificable con oráculo de parada |
| `Π_2⁰` | `∀ ∃ R(n, x̄)` | Co-`Σ_2⁰` |
| `Σ_n⁰` | Bloque `∃∀∃…` de `n` alternaciones | — |
| `Π_n⁰` | Bloque `∀∃∀…` de `n` alternaciones | — |

La clase `Δ_n⁰ = Σ_n⁰ ∩ Π_n⁰` contiene los problemas decidibles con un oráculo de nivel `n-1`.

## Relaciones con RE y coRE

Las clases más importantes son las dos primeras:

- **`Σ_1⁰` = RE:** los lenguajes reconocibles son exactamente los definibles por una fórmula `∃ x̄ R(n, x̄)` donde `R` es decidible. El testigo `x̄` es la computación que acepta.

- **`Π_1⁰` = coRE:** complementos de los RE. El problema de la parada negado: "`M` *no* se detiene sobre `w`" es `Π_1⁰`.

- **`Δ_1⁰` = decidible:** `Σ_1⁰ ∩ Π_1⁰`. Un lenguaje es decidible si y solo si tanto él como su complemento son reconocibles.

## El oráculo de salto (jump)

La operación de **salto de Turing** sube un nivel en la jerarquía:


> **Fórmula:** `K = \{⟨ M ⟩ : M(⟨ M ⟩)  se detiene\}`


`K` es el problema de la parada diagonal. Es `Σ_1⁰`-completo (los más difíciles de RE).

El **salto de Turing** de un conjunto `A` es:


> **Fórmula:** `A' = \{⟨ M ⟩ : M^A(⟨ M ⟩)  se detiene\}`


donde `M^A` es una MT con oráculo `A`. Los saltos sucesivos generan la jerarquía:


> **Fórmula:** `∅ < ∅' < ∅'' < ∅''' < …`


donde `∅^((n))` es el conjunto de los `Σ_n⁰`-completos.

**Teorema.** `L ∈ Σ_n⁰ ⟺ L` es reducible a `∅^((n))` mediante una reducción muchos-a-uno computable.

## Ejemplos en cada nivel

### `Σ_1⁰` (RE)
- El problema de la parada: `\{⟨ M, w ⟩ : M(w) \downarrow\}`.
- El dominio de cualquier función parcialmente computable.
- El lenguaje de las MT que aceptan la cadena vacía: `\{⟨ M ⟩ : ε ∈ L(M)\}`.

### `Π_1⁰` (coRE)
- El complemento del problema de la parada: `\{⟨ M, w ⟩ : M(w) \uparrow\}`.
- Las MT que *no* aceptan una cadena dada.

### `Σ_2⁰`
- "`M` se detiene en infinitas entradas": `∃^∞ w  ⟨ M, w ⟩ ∈ K`.
  Fórmula: `∃ n ∀ m > n  M(m) \downarrow`.
- El problema `TOT`: "`M` se detiene en *toda* entrada" es `Π_2⁰`.
  Fórmula: `∀ w ∃ t  M` acepta `w` en `t` pasos.

### `Π_2⁰`
- "`M` se detiene en *todas* las entradas" (TOT).
- Las MT cuyo lenguaje es *finito*.

### `Σ_3⁰`
- "El lenguaje de `M` es infinito": `∃ n ∀ k ∃ w` con `|w| > k` tal que `M(w) \downarrow`.

## El teorema de Post

**Teorema de Post.** Para todo `n ≥ 1`:

1. `Σ_n⁰ ∪ Π_n⁰ ⊂neq Σ_n+1⁰ ∩ Π_n+1⁰`.
2. `Σ_n⁰ ≠ Π_n⁰` (la jerarquía no colapsa).
3. `Σ_n⁰ ≠ Σ_n+1⁰` (cada nivel es estrictamente más potente).

La jerarquía es infinita y estricta. No hay un nivel máximo: por encima de toda la jerarquía aritmética están los problemas **no aritméticos** (como la verdad de primer orden sobre los naturales, por el teorema de Tarski).

## Relación con el teorema de Rice

El teorema de Rice generalizado dice que para cualquier propiedad `P` no trivial del lenguaje de una MT:

- Si `P` es monotona (cerrada hacia arriba), entonces `\{M : L(M) ∈ P\}` es `Σ_3⁰` o más alto.
- Si `P` es co-monotona, es `Π_3⁰` o más alto.

Esto da límites precisos de complejidad para propiedades de programas, no solo "es indecidible".

## La jerarquía aritmética y la jerarquía polinómica

Existe una analogía entre la jerarquía aritmética (sin coste computacional) y la jerarquía polinómica (con coste polinomial):

| Aritmética | Polinómica |
|-----------|-----------|
| `Σ_1⁰` = RE | NP |
| `Π_1⁰` = coRE | coNP |
| `Σ_2⁰` | `Σ_2^P` |
| `Π_2⁰` | `Π_2^P` |
| `Δ_1⁰` = decidible | P |

La diferencia: en la jerarquía aritmética los cuantificadores cuantifican sobre todos los naturales; en la polinómica cuantifican sobre testigos polinomiales.

## Ideas clave

1. La jerarquía aritmética clasifica los problemas indecidibles por el número de alternaciones de cuantificadores en su definición lógica.
2. `Σ_1⁰` = RE, `Π_1⁰` = coRE, `Δ_1⁰` = decidible.
3. El oráculo de salto `A → A'` sube exactamente un nivel en la jerarquía.
4. La jerarquía es estricta e infinita (teorema de Post).
5. La analogía con la jerarquía polinómica revela la misma estructura en dos mundos distintos.

## Ejercicios

1. Clasifica estos problemas en `Σ_n⁰` o `Π_n⁰`: (a) "M acepta exactamente una cadena", (b) "L(M) contiene un número primo", (c) "M se detiene en todas las entradas de longitud ≤ 10".

2. Demuestra que `Δ_1⁰` = decidible, es decir, que `L` es decidible si y solo si `L ∈ Σ_1⁰ ∩ Π_1⁰`.

3. ¿Por qué el lenguaje de la verdad aritmética (el conjunto de fórmulas de primer orden verdaderas sobre `ℕ`) no pertenece a ningún nivel de la jerarquía?

4. Construye explícitamente un lenguaje `Σ_2⁰` que no sea `Σ_1⁰` usando el oráculo de salto.

## Véase también

- [Oráculos y relativización](11-oráculos-y-relativización.md)
- [Aleatoriedad algorítmica](12-aleatoriedad-algoritmica.md)


## Referencias

- Soare, R.I. (2016). *Turing Computability: Theory and Applications*. Springer.
- Rogers, H. (1987). *Theory of Recursive Functions and Effective Computability*. MIT Press.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3ª ed., cap. 6. Cengage.
- Odifreddi, P. (1989). *Classical Recursion Theory*. North-Holland.
