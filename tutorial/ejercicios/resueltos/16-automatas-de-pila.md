# 16 - Autómatas de pila y lenguajes independientes del contexto

## Contexto

Este ejercicio acompaña el artículo
[Autómatas de pila y lenguajes independientes del contexto](../../03-computabilidad/09-automatas-de-pila-y-lenguajes-contexto-libre.md).

También se puede practicar con el cuaderno
[Autómatas de pila: PDA y CYK](../../cuadernos/ejemplos/21-automatas-de-pila.ipynb).

## Enunciado

1. Diseña un PDA para el lenguaje L = {ww^R : w ∈ {a,b}*} (palíndromos pares).
   Describe las transiciones clave y traza la aceptación de `abba`.

2. Usa el lema de bombeo para CFL para demostrar que el siguiente lenguaje
   **no** es independiente del contexto:

   ```text
   L = {aⁿbⁿcⁿ : n ≥ 1}
   ```

3. La gramática G tiene las siguientes producciones:
   ```text
   S → AB | a
   A → aA | a
   B → bB | b
   ```
   ¿Pertenece la cadena `aab` a L(G)? Muestra la derivación o justifica que no.

## Pista

**Palíndromos pares:** el PDA no determinista adivina cuándo está en el centro
de la cadena y cambia de fase: primero hace push de cada símbolo leído; al llegar
al centro (ε-transición), compara haciendo pop con los símbolos que aún lee.

**Lema de bombeo:** sea p la constante de bombeo. Elige w = aᵖbᵖcᵖ.
Para cualquier descomposición w = uvxyz con |vxy| ≤ p y |vy| ≥ 1, la subcadena
vxy no puede abarcar las tres letras. Bombear i = 2 rompe el equilibrio.

**CYK:** aplica derivaciones; verifica si alguna secuencia produce `aab`.

## Solución

### 1. PDA para palíndromos pares

**Estados:** q₀ (fase push), q₁ (fase pop), q_f (aceptación).

**Transiciones clave:**

| Estado | Entrada | Tope pila | → Estado | Pila nueva | Acción |
|--------|---------|-----------|----------|------------|--------|
| q₀ | a | Z | q₀ | AZ | push A |
| q₀ | b | Z | q₀ | BZ | push B |
| q₀ | a | A | q₀ | AA | push A |
| q₀ | a | B | q₀ | AB | push A |
| q₀ | b | A | q₀ | BA | push B |
| q₀ | b | B | q₀ | BB | push B |
| q₀ | ε | cualquiera | q₁ | sin cambio | cambio no det. al centro |
| q₁ | a | A | q₁ | ε | pop A (match) |
| q₁ | b | B | q₁ | ε | pop B (match) |
| q₁ | ε | Z | q_f | Z | aceptar |

**Traza de `abba`:**

```text
(q₀, abba, Z) →push a→ (q₀, bba, AZ)
              →push b→ (q₀, ba, BAZ)
              →ε, cambio de fase→ (q₁, ba, BAZ)
              →pop B con b→ (q₁, a, AZ)
              →pop A con a→ (q₁, ε, Z)
              →ε, aceptar→ (q_f, ε, Z)  ✓
```

El PDA debe ser **no determinista** porque no sabe de antemano dónde está el
centro de la cadena; la ε-transición de q₀ a q₁ puede ocurrir en cualquier
momento.

### 2. {aⁿbⁿcⁿ} no es CFL

**Por contradicción.** Supóngase que L es CFL. Sea p su constante de bombeo.
Elige w = aᵖbᵖcᵖ ∈ L, que tiene longitud 3p ≥ p.

Por el lema de bombeo, existe descomposición w = uvxyz con:
- |vxy| ≤ p
- |vy| ≥ 1

Como |vxy| ≤ p, la subcadena vxy abarca a lo sumo dos de los tres bloques aᵖ, bᵖ, cᵖ.

**Caso 1:** vxy está dentro de aᵖbᵖ (no contiene ninguna c).
Al bombear i = 2 (w' = uv²xy²z), el número de a's o b's aumenta, pero el de c's
permanece en p. Por tanto w' ∉ L.

**Caso 2:** vxy está dentro de bᵖcᵖ. Análogo: las a's no crecen, contradicción.

**Caso 3:** vxy atraviesa la frontera a/b/c. Como |vxy| ≤ p, no puede abarcar los
tres bloques a la vez (cada bloque tiene longitud p). Al bombear, alguna letra
queda desequilibrada.

En todos los casos, uv²xy²z ∉ L. Contradicción con el lema de bombeo. **∴ L no es CFL.** ∎

### 3. Pertenencia de `aab` a L(G)

La gramática produce:
- S → AB | a
- A → aA | a  (genera aⁿ para n ≥ 1)
- B → bB | b  (genera bⁿ para n ≥ 1)

**Intento de derivar `aab`:**

```text
S → AB → aA B → aa B → aab  ✓
```

Derivación paso a paso:
```text
S ⟹ AB        (usando S → AB)
  ⟹ aAB       (usando A → aA, con la A restante)
  ⟹ aaB       (usando A → a)
  ⟹ aab       (usando B → b)
```

**`aab` ∈ L(G).** ✓

La gramática G genera exactamente L = {aⁿbᵐ : n ≥ 1, m ≥ 1} ∪ {a}, es decir,
cualquier cadena de una o más a's seguidas de una o más b's, más el símbolo `a` solo.

## Comentario

El lema de bombeo para CFL prueba no-pertenencia pero no puede usarse al revés:
si una cadena se puede "bombear", **no** se concluye que el lenguaje sea CFL.
El lema es condición necesaria, no suficiente.

## Para seguir

Demuestra que L = {ww : w ∈ {a,b}*} (concatenación de una cadena consigo misma,
no palíndromo) tampoco es CFL. Pista: usa w = aᵖbᵖaᵖbᵖ como testigo.
