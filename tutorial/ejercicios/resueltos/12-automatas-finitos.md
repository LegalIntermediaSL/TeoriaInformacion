# Autómatas finitos y lenguajes regulares: ejercicios resueltos

**Artículo asociado:** [Autómatas finitos y lenguajes regulares](../../03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md)  
**Cuadernos relacionados:** [Autómata finito para paridad](../../cuadernos/ejemplos/10-automata-finito-paridad.ipynb), [Autómatas y lenguajes](../../cuadernos/ejercicios/12-automatas-y-lenguajes.ipynb)

---

## Ejercicio 1: cadenas binarias que terminan en `01`

**Enunciado.** Construye un DFA sobre $\{0,1\}$ que acepte exactamente las cadenas que terminan en `01`. Verifica los casos: `"01"`, `"1001"`, `"10101"`, `""`, `"0"`, `"10"`, `"011"`.

### Pista

Para saber si una cadena termina en `01` basta recordar los dos últimos símbolos. ¿Cuántos pares de sufijos relevantes existen?

### Solución

Los únicos prefijos que importan son los tres sufijos posibles del último par leído:

| Estado | Significado |
|--------|-------------|
| `q_init` | Sufijo relevante vacío o no `0` ni `01` |
| `q_0` | El último símbolo leído fue `0` |
| `q_01` | Los últimos dos símbolos fueron `01` (estado de aceptación) |

**Función de transición $\delta$:**

| Estado | `0` | `1` |
|--------|-----|-----|
| `q_init` | `q_0` | `q_init` |
| `q_0` | `q_0` | `q_01` |
| `q_01` | `q_0` | `q_init` |

**Lectura de la tabla.** Desde `q_init`:
- Un `1` no cambia nada (seguimos sin sufijo útil).
- Un `0` abre la posibilidad de terminar en `01`.

Desde `q_0`:
- Un `0` adicional: el sufijo sigue siendo `0` (el nuevo `0` reemplaza al anterior).
- Un `1`: hemos completado `01` → aceptar.

Desde `q_01`:
- Un `0`: el nuevo sufijo es solo `0` (perdemos el `1` previo).
- Un `1`: el nuevo sufijo es solo `1` → volvemos a `q_init`.

**Verificación de `"1001"`:**

```
q_init → '1' → q_init
q_init → '0' → q_0
q_0    → '0' → q_0
q_0    → '1' → q_01  → ACEPTA ✓
```

**Verificación de `"011"`:**

```
q_init → '0' → q_0
q_0    → '1' → q_01
q_01   → '1' → q_init  → RECHAZA ✓  (termina en '1', no en '01')
```

**Correctitud.** El autómata es correcto porque los tres estados capturan todos los sufijos distinguibles: dos cadenas $u$ y $v$ van al mismo estado si y solo si para cualquier continuación $w$, $uw$ termina en `01` si y solo si $vw$ termina en `01`. Este razonamiento (clases de equivalencia de Myhill-Nerode) muestra además que 3 es el número mínimo de estados.

---

## Ejercicio 2: número de `a` divisible por 3

**Enunciado.** Sobre $\{a, b\}$, construye un DFA que acepte las cadenas donde el número de `a` es múltiplo de 3 (incluyendo 0). Verifica: `""`, `"aaa"`, `"baaab"`, `"a"`, `"aa"`, `"aaaa"`.

### Pista

El número de `a` vistas modulo 3 es exactamente la información que hay que recordar.

### Solución

**Estados:** `r0` (conteo ≡ 0 mod 3), `r1` (≡ 1), `r2` (≡ 2). Estado de aceptación: `r0`.

**Función de transición $\delta$:**

| Estado | `a` | `b` |
|--------|-----|-----|
| `r0` | `r1` | `r0` |
| `r1` | `r2` | `r1` |
| `r2` | `r0` | `r2` |

**Lectura.** Cada `a` avanza el contador módulo 3; cada `b` lo deja intacto. Cuando el contador vuelve a 0 (estado `r0`) hemos visto un múltiplo de 3 de `a`.

**Verificación de `"baaab"`:**

```
r0 → 'b' → r0
r0 → 'a' → r1
r1 → 'a' → r2
r2 → 'a' → r0
r0 → 'b' → r0  → ACEPTA ✓  (3 aes)
```

**Verificación de `"aaaa"`:**

```
r0 → 'a' → r1
r1 → 'a' → r2
r2 → 'a' → r0
r0 → 'a' → r1  → RECHAZA ✓  (4 aes, 4 mod 3 = 1 ≠ 0)
```

**Mínimo de estados.** Las tres clases de equivalencia de Myhill-Nerode son las cadenas con 0, 1 y 2 `a` módulo 3. Son distinguibles entre sí (por continuaciones `""`, `"aa"` y `"a"` respectivamente), así que 3 estados es el mínimo.

---

## Ejercicio 3: el pumping lemma

**Enunciado.** Usa el pumping lemma para demostrar que $L = \{a^n b^n : n \geq 1\}$ no es regular.

### Solución

Supongamos por contradicción que $L$ es regular con constante de bombeo $p$.

**Elección de la cadena.** Tomamos $w = a^p b^p \in L$. Claramente $|w| = 2p \geq p$.

**Descomposición.** Por el pumping lemma, existe una descomposición $w = xyz$ con:
- $|xy| \leq p$
- $|y| \geq 1$
- $xy^i z \in L$ para todo $i \geq 0$

Dado que $|xy| \leq p$ y los primeros $p$ símbolos de $w$ son `a`, tanto $x$ como $y$ están formados únicamente por `a`. Por tanto $y = a^k$ para algún $k \geq 1$.

**Bombeo.** Consideramos $i = 2$:
$$xy^2z = a^{|x|} \cdot a^{2k} \cdot z = a^{p+k} b^p$$
Esta cadena tiene $p + k$ aes y $p$ bes. Como $k \geq 1$, tenemos $p + k > p$, por lo que $a^{p+k} b^p \notin L$.

Esto contradice el pumping lemma. Por tanto, $L$ no es regular. $\square$

**Intuición.** Un DFA tiene finitely many estados. Para reconocer $\{a^n b^n\}$ necesitaría recordar el valor exacto de $n$ tras leer las `a`, pero ningún número finito de estados puede representar todos los valores posibles de $n$.

---

## Ejercicio 4: minimización de DFA

**Enunciado.** El siguiente DFA tiene 5 estados. Muestra que puede minimizarse a 3 estados.

DFA inicial sobre $\{0, 1\}$:

| Estado | `0` | `1` | ¿Acepta? |
|--------|-----|-----|---------|
| `p` | `q` | `r` | No |
| `q` | `p` | `s` | No |
| `r` | `s` | `p` | No |
| `s` | `s` | `s` | Sí |
| `t` | `p` | `t` | No |

Estado inicial: `p`.

### Solución

Aplicamos el algoritmo de marcado de pares distinguibles.

**Paso 1 — marcar pares de distinto tipo de aceptación:**  
`s` es el único estado de aceptación. Son distinguibles de los demás: `{(p,s), (q,s), (r,s), (t,s)}`.

**Paso 2 — propagación iterativa:**

- ¿Son distinguibles `p` y `t`? Miramos `δ(p,0)=q` y `δ(t,0)=p`. ¿Es `(q,p)` distinguible? Miramos `δ(q,1)=s` y `δ(p,1)=r`. El par `(s,r)` ya está marcado → `(q,p)` distinguible → `(p,t)` distinguible.
- ¿Son distinguibles `p` y `q`? `δ(p,1)=r`, `δ(q,1)=s` → par `(r,s)` marcado → `(p,q)` distinguible.
- ¿Son distinguibles `p` y `r`? `δ(p,1)=r`, `δ(r,1)=p` → par `(r,p)` que es el mismo bajo análisis; `δ(p,0)=q`, `δ(r,0)=s` → par `(q,s)` marcado → `(p,r)` distinguible.
- ¿Son distinguibles `q` y `r`? `δ(q,0)=p`, `δ(r,0)=s` → par `(p,s)` marcado → `(q,r)` distinguible.
- ¿Son distinguibles `q` y `t`? `δ(q,0)=p`, `δ(t,0)=p` (misma celda), y `δ(q,1)=s`, `δ(t,1)=t` → par `(s,t)` marcado → `(q,t)` distinguible.
- ¿Son distinguibles `r` y `t`? `δ(r,1)=p`, `δ(t,1)=t` → par `(p,t)` ya marcado → `(r,t)` distinguible.

Todos los pares son distinguibles: el DFA ya tiene los 5 estados mínimos.

> *Nota:* el enunciado era un ejemplo didáctico. Si ningún par fuera equivalente, la minimización no reduce el autómata.

**Corrección del algoritmo.** El algoritmo marca un par $(u,v)$ si existe una cadena $w$ tal que $\hat{\delta}(u,w) \in F$ pero $\hat{\delta}(v,w) \notin F$ (o al revés). Los pares no marcados al terminar son **indistinguibles** y pueden fusionarse en un único estado.

---

## Ideas clave

- Los estados de un DFA codifican **clases de equivalencia** de prefijos: dos prefijos son equivalentes si toda continuación posible les da el mismo resultado.
- El **teorema de Myhill-Nerode** establece que el DFA mínimo tiene exactamente tantos estados como clases de equivalencia distinguibles.
- El **pumping lemma** es la herramienta para demostrar que un lenguaje *no* es regular: se elige una cadena larga en el lenguaje y se muestra que ningún bombeo la mantiene dentro.
- La **minimización** (algoritmo de marcado) identifica pares de estados indistinguibles y los fusiona, obteniendo el DFA de menor número de estados para un lenguaje dado.
