# 21 - Complejidad descriptiva

## Contexto

Este ejercicio acompaña el artículo
[Complejidad descriptiva](../../03-computabilidad/08-complejidad-descriptiva.md).

## Enunciado

La complejidad descriptiva (o de Kolmogorov) $K(x)$ de una cadena $x$ es la
longitud del programa más corto (para una máquina de Turing universal fija $U$)
que produce $x$ como salida.

1. Calcula o acota $K(x)$ para las siguientes cadenas:
   - (a) $x = \underbrace{00\ldots0}_{1000}$ (1000 ceros)
   - (b) $x = $ los primeros 1000 dígitos de $\pi$ en binario
   - (c) $x = $ una cadena binaria aleatoria de 1000 bits

2. Demuestra que $K(x) \leq |x| + c$ para alguna constante $c$ independiente
   de $x$.

3. Demuestra que al menos la mitad de las cadenas de longitud $n$ tienen
   $K(x) \geq n - 1$.

4. ¿Por qué $K$ no es computable? Esboza la demostración.

## Pista

**Cotas:** $K(x) \leq |p| + O(1)$ donde $p$ es cualquier programa que genera $x$.

**Incompresibilidad:** un argumento de conteo: si todas las cadenas se pudieran
comprimir significativamente, habría más cadenas que descripciones.

**No computabilidad:** supón que $K$ es computable y construye una paradoja de
tipo Berry.

## Solución

### 1. Cotas de $K(x)$

**(a) $x = 0^{1000}$ (1000 ceros)**

Existe un programa corto que genera $0^{1000}$:

```python
print('0' * 1000)
```

Este programa tiene longitud $O(\log 1000) \approx 30$ caracteres (o bits si se
codifica en binario). Más formalmente, la descripción `("imprimir ceros × 1000")`
se puede codificar en $O(\log 1000) = O(10)$ bits.

$$K(0^{1000}) \leq O(\log n) = O(10) \text{ bits}$$

La constante exacta depende de la máquina universal $U$, pero el orden es
logarítmico. Esta cadena es **muy compresible**.

**(b) $x = $ primeros 1000 bits de $\pi$**

Existe un programa corto que calcula $\pi$ y extrae los primeros 1000 bits:

```python
# calcular pi con N decimales y tomar primeros 1000 bits
```

El código fuente del algoritmo de Machin (o BBP) más el número `1000` tiene
longitud $O(\log 1000 + |\text{algoritmo}|)$. El algoritmo es una constante fija
(no depende de $n$), así que:

$$K(\pi_{1000}) \leq O(\log 1000) + c_\pi$$

donde $c_\pi$ es la constante que describe el algoritmo para calcular $\pi$.
Esta cadena también es compresible (aunque en la práctica los dígitos de $\pi$
parecen "aleatorios", el hecho de ser los primeros 1000 dígitos de $\pi$ tiene
una descripción muy corta).

**(c) $x = $ cadena binaria aleatoria de 1000 bits**

Con alta probabilidad, una cadena tomada al azar de $\{0,1\}^{1000}$ tiene:

$$K(x) \geq 1000 - O(1) \text{ bits}$$

Es decir, no se puede comprimir significativamente. El argumento se da en el
apartado 3. No existe descripción corta para la mayoría de cadenas aleatorias.

### 2. Cota superior $K(x) \leq |x| + c$

**Demostración.** Considéremos el siguiente programa para la máquina universal $U$:

```
PROGRAMA P(x): 
  "imprimir los siguientes n bits: [x]"
```

donde $x$ está codificado literalmente en el programa. El tamaño de este programa
es $|x| + O(1)$ bits (la descripción del formato `"imprimir los siguientes..."` es
una constante $c$ independiente de $x$).

Por definición de $K$:

$$K(x) \leq |P| = |x| + c$$

donde $c$ es la longitud del "preámbulo" del programa. ∎

**Interpretación:** siempre se puede describir $x$ copiándolo literalmente. La
complejidad $K(x)$ nunca puede superar la longitud de $x$ más que por una constante.

### 3. Al menos la mitad de las cadenas tienen $K(x) \geq n - 1$

**Demostración (argumento de conteo).**

El número de programas (descripciones) de longitud $< n - 1$ es:

$$|\{p : |p| < n-1\}| = \sum_{k=0}^{n-2} 2^k = 2^{n-1} - 1 < 2^{n-1}$$

El número total de cadenas binarias de longitud $n$ es $2^n$.

Por tanto, **a lo sumo $2^{n-1} - 1$ cadenas** de longitud $n$ pueden tener
$K(x) < n - 1$ (porque no hay suficientes programas cortos para describirlas a todas).

El resto —al menos $2^n - (2^{n-1} - 1) > 2^{n-1}$ cadenas, es decir, **más de
la mitad**— satisface $K(x) \geq n - 1$. ∎

**Corolario:** las cadenas incompresibles son las "típicas"; las compresibles son
la minoría.

### 4. $K$ no es computable

**Esquema de la paradoja de Berry.**

Supón que $K$ es computable. Entonces existe un programa $P$ que, dado $n$,
calcula el menor $K(x) \geq n$ (o una cadena $x^*$ con $K(x^*) \geq n$).

Construimos el siguiente programa $Q$ parametrizado por $n$:

> "Encuentra la primera cadena $x$ (en orden lexicográfico) tal que $K(x) \geq n$.
> Imprime $x$."

Este programa $Q$ tiene descripción fija (el código de $Q$) más la representación
de $n$, con longitud $|Q| = O(\log n) + c$.

Pero $Q$ genera una cadena $x^*$ con $K(x^*) \geq n$. Para $n$ grande ($n > |Q|$),
tenemos:

$$K(x^*) \leq |Q| = O(\log n) < n \leq K(x^*)$$

**Contradicción.** La suposición de que $K$ es computable lleva a una cadena cuya
complejidad es simultáneamente $\geq n$ y $< n$. ∎

Este argumento es la **paradoja de Berry** formalizada: "el menor entero no
describible en menos de trece palabras" se describe en menos de trece palabras.

## Comentario

La complejidad de Kolmogorov captura la "aleatoriedad" de cadenas individuales,
a diferencia de la entropía de Shannon que caracteriza distribuciones. Ambas
convergen: la entropía de una fuente i.i.d. es el límite de la complejidad de
Kolmogorov promedio de muestras típicas. La no computabilidad de $K$ es el precio
de esta generalidad: no existe ningún algoritmo que mida la aleatoriedad perfectamente.

## Para seguir

La **complejidad de Kolmogorov condicional** $K(x | y)$ es la longitud del programa
más corto que genera $x$ dado $y$ como entrada auxiliar. Demuestra que
$K(x, y) \leq K(x) + K(y) + O(\log \min(K(x), K(y)))$ (cadena de la desigualdad).
