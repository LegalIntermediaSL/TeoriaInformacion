# 20 - Gramáticas y jerarquía de Chomsky

## Contexto

Este ejercicio acompaña el artículo
[Gramáticas y jerarquía de Chomsky](../../03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md).

## Enunciado

1. Clasifica las siguientes gramáticas en la jerarquía de Chomsky (tipo 0, 1, 2 o
   3). Justifica.

   **G₁:**
   ```text
   S → aSb | ab
   ```

   **G₂:**
   ```text
   S → aB | bA
   A → a | aS | bAA
   B → b | bS | aBB
   ```

   **G₃:**
   ```text
   S → AB
   A → aA | ε
   B → Bb | ε
   ```

2. Convierte G₁ a forma normal de Chomsky (CNF).

3. ¿El lenguaje $L = \{a^n b^n : n \geq 1\}$ es regular? Usa el lema de bombeo
   para lenguajes regulares para justificar tu respuesta.

4. La gramática G₄ tiene las producciones:
   ```text
   S → XY
   X → aXb | ab
   Y → cYd | cd
   ```
   ¿Pertenece `aabbccdd` a $L(G_4)$? Muestra la derivación.

## Pista

**Jerarquía:** tipo 3 (regulares) ⊂ tipo 2 (CFL) ⊂ tipo 1 (sensibles al contexto)
⊂ tipo 0 (sin restricción). Tipo 3: producciones $A \to aB$ o $A \to a$. Tipo 2:
$A \to \alpha$ (lado derecho cualquiera). Tipo 1: $|\alpha| \leq |\beta|$ en
$\alpha \to \beta$ (sin borrar).

**CNF:** cada producción es $A \to BC$ o $A \to a$. Primero eliminar $\epsilon$-producciones
y producciones unitarias, luego binarizar.

**Lema de bombeo (regulares):** si $L$ es regular con constante $p$, toda cadena
$w \in L$ con $|w| \geq p$ tiene $w = xyz$ con $|xy| \leq p$, $|y| \geq 1$, y
$xy^iz \in L$ para todo $i \geq 0$.

## Solución

### 1. Clasificación de las gramáticas

**G₁: `S → aSb | ab`**

- Ambas producciones tienen la forma $A \to \alpha$ donde el lado izquierdo es
  un único no terminal. Es una **gramática libre de contexto (tipo 2)**.
- No es tipo 3 porque `S → aSb` tiene un no terminal en el medio del lado derecho,
  no al final. Para ser regular (tipo 3), debería ser $S \to aS$ o $S \to a$.
- **Tipo 2 (CFL).** Genera $\{a^n b^n : n \geq 1\}$.

**G₂:**

- `S → aB`: tipo 3 (regular).
- `A → aS`: tipo 3.
- `B → aBB`: lado derecho `aBB` tiene dos no terminales después de `a`. No es tipo 3
  (necesitaría como máximo un no terminal al final). Es tipo 2.
- **Tipo 2 (CFL).** Genera $\{w \in \{a,b\}^* : |w|_a = |w|_b\}$ (cadenas con
  igual número de a's y b's).

**G₃: `S → AB`, `A → aA | ε`, `B → Bb | ε`**

- `A → aA`: tipo 3 (recursiva a la derecha).
- `B → Bb`: el no terminal está a la **izquierda** del terminal, recursión
  izquierda. Esto es tipo 3 pero con recursión izquierda (gramática lineal
  izquierda). Las gramáticas regulares admiten recursión derecha O izquierda,
  pero no mixtas.
- Sin embargo, $S \to AB$ tiene dos no terminales en el lado derecho, lo que
  excluye tipo 3.
- **Tipo 2 (CFL).** Genera $\{a^m b^n : m, n \geq 0\}$.

### 2. CNF de G₁

**G₁:** `S → aSb | ab`

Producciones a transformar:

**Paso 1:** introducir variables para terminales en producciones largas.

```text
Tₐ → a
T_b → b
```

Reescribir:
```text
S → Tₐ S T_b | Tₐ T_b
Tₐ → a
T_b → b
```

**Paso 2:** binarizar `S → Tₐ S T_b` (tres símbolos en el lado derecho).

```text
S → Tₐ R
R → S T_b
```

**CNF final:**

```text
S  → Tₐ R  |  Tₐ T_b
R  → S T_b
Tₐ → a
T_b → b
```

Verificación: cada producción es $A \to BC$ o $A \to a$. ✓

### 3. $\{a^n b^n\}$ no es regular

**Por contradicción.** Supón que $L = \{a^n b^n : n \geq 1\}$ es regular. Sea $p$
su constante de bombeo.

Elige $w = a^p b^p \in L$ con $|w| = 2p \geq p$.

Por el lema de bombeo, $w = xyz$ con $|xy| \leq p$, $|y| \geq 1$.

Como $|xy| \leq p$, la subcadena $xy$ cae enteramente dentro del bloque $a^p$.
Luego $y = a^k$ para algún $k \geq 1$.

Bombeamos con $i = 2$: $xy^2z = a^{p+k} b^p$. Como $k \geq 1$, hay más a's que
b's: $p+k \neq p$, así que $xy^2z \notin L$.

**Contradicción** con el lema de bombeo. ∴ $L$ no es regular. ∎

### 4. ¿Pertenece `aabbccdd` a $L(G_4)$?

**G₄:** `S → XY`, `X → aXb | ab`, `Y → cYd | cd`.

Observamos: $X$ genera $\{a^n b^n : n \geq 1\}$ y $Y$ genera $\{c^m d^m : m \geq 1\}$.
El lenguaje es $L(G_4) = \{a^n b^n c^m d^m : n,m \geq 1\}$.

La cadena `aabbccdd` tiene $n = 2$ a's, $2$ b's, $2$ c's, $2$ d's. ✓

**Derivación:**

```text
S ⟹ XY
  ⟹ aXb · Y             (X → aXb)
  ⟹ a·ab·b · Y          (X → ab)
  ⟹ aabb · Y
  ⟹ aabb · cYd          (Y → cYd)
  ⟹ aabb · c·cd·d       (Y → cd)
  ⟹ aabbccdd  ✓
```

**`aabbccdd` ∈ L(G₄).** ✓

## Comentario

La jerarquía de Chomsky refleja el poder de diferentes modelos computacionales:
tipo 3 ↔ autómatas finitos, tipo 2 ↔ autómatas de pila, tipo 1 ↔ MT acotada
en espacio lineal, tipo 0 ↔ máquinas de Turing sin restricción. Subir un nivel
en la jerarquía añade un tipo de memoria: contadores sin memoria (tipo 3) →
pila ilimitada (tipo 2) → cinta acotada (tipo 1) → cinta ilimitada (tipo 0).

## Para seguir

Demuestra que $L = \{a^n b^n c^n : n \geq 1\}$ no es libre de contexto usando el
lema de bombeo para CFL. Compara con el caso regular anterior: ¿cuál es más
restrictivo y por qué?
