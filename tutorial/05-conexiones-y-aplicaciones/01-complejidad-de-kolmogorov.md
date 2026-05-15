# 01 - Complejidad de Kolmogorov

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min


La entropía de Shannon mide incertidumbre promedio respecto de una fuente
probabilística. La complejidad de Kolmogorov, en cambio, pregunta por la cantidad
de información contenida en un objeto individual.

La idea central es sorprendentemente directa: una cadena contiene poca
información si puede describirse mediante un programa corto.

## Prerrequisitos

- [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)
- [Máquinas de Turing](../03-computabilidad/04-maquinas-de-turing.md)

## Objetivos de aprendizaje

1. Definir la complejidad de Kolmogorov K(x) mediante el programa más corto.
2. Entender la invarianza de K respecto de la máquina universal de referencia.
3. Demostrar que K no es computable y relacionarlo con el problema de la parada.


## Descripción mínima

Consideremos dos cadenas binarias:

```text
00000000000000000000000000000000
```

y:

```text
01101011100101000110101110100110
```

La primera tiene una descripción breve:

```text
imprime 32 ceros
```

La segunda quizá no tenga una descripción mucho más corta que escribirla tal
cual. Intuitivamente, parece más aleatoria.

La complejidad de Kolmogorov formaliza esta diferencia.

## Definición intuitiva

La complejidad de Kolmogorov de una cadena `x`, escrita `K(x)`, es la longitud
del programa más corto que imprime `x` y se detiene.

```text
K(x) = longitud del programa más corto que produce x
```

La definición depende de fijar un lenguaje o máquina universal, pero esa
dependencia solo cambia el valor por una constante. Para cadenas largas, esa
constante suele ser irrelevante en el análisis teórico.

## Compresibilidad

Una cadena es compresible si existe una descripción mucho más corta que la propia
cadena.

Por ejemplo:

```text
01010101010101010101010101010101
```

puede describirse como:

```text
repite "01" dieciseis veces
```

En cambio, una cadena sin patrones detectables puede no admitir una descripción
más corta. En ese caso decimos que es incompresible, al menos respecto del modelo
de descripción elegido.

## Aleatoriedad algorítmica

La complejidad de Kolmogorov permite definir una noción de aleatoriedad para
objetos individuales: una cadena es algorítmicamente aleatoria si no puede
comprimirse de forma significativa.

Esto conecta aleatoriedad con ausencia de patrones efectivos. No basta con que
una cadena "parezca desordenada"; la cuestión es si existe un procedimiento corto
que la genere.

## Ejemplo numérico: cotando K(x) para cadenas concretas

Fijamos $n = 32$ y comparamos tres cadenas de longitud 32:

| Cadena $x$ | Patrón | Descripción compacta | $\|d(x)\|$ (bits aprox.) |
|---|---|---|---|
| $\underbrace{00\cdots0}_{32}$ | Todo ceros | `print('0'*32)` → `rep(0,32)` | $\approx 10$ |
| $\underbrace{01\cdots01}_{32}$ | Alternado | `print('01'*16)` → `rep(01,16)` | $\approx 12$ |
| `01101011100101000110101110100110` | Sin patrón obvio | Copiar literalmente | $\approx 32$ |

**Cota superior para la cadena de ceros:** el programa `print('0'*32)` tiene unos 15 caracteres (≈15 bytes ≈ 120 bits en ASCII). En una máquina universal binaria compacta, basta con algo como el par $(k, n) = (0, 32)$ codificado en $O(\log n)$ bits, así que $K(0^{32}) \leq 2\log_2 32 + c = 10 + c$ para alguna constante $c$.

**Cota inferior para cualquier cadena:** existen $2^n$ cadenas de longitud $n$, pero solo $2^k - 1$ programas de longitud $< k$. Si $k < n$, al menos $2^n - 2^k + 1 > 2^n / 2$ cadenas no tienen descripción de longitud $< n$. En particular:

$$\Pr_{x \sim U\{0,1\}^n}[K(x) < n - c] \leq 2^{-c}$$

Para $c = 5$: solo $1/32$ de las cadenas de 32 bits tienen $K(x) < 27$. **La cadena típica es casi incompresible.**

**Cálculo para la tercera cadena:** si `01101011...0110` es una muestra aleatoria de $\{0,1\}^{32}$, esperamos $K(x) \approx 32$ bits (más una constante de descripción de la máquina). El mejor compresor práctico (LZ77, BZIP2) tampoco la reduciría significativamente, lo que es consistente con $K(x) \approx n$.

**Relación con la entropía:** una fuente Bernoulli(1/2) produce cadenas con entropía $H = 1$ bit/símbolo. El valor esperado $\mathbb{E}[K(X)]$ para $X \sim \text{Bernoulli}(1/2)^n$ satisface:

$$n - O(\log n) \leq \mathbb{E}[K(X)] \leq n + O(1)$$

Para fuentes sesgadas Bernoulli($p$) con $p \neq 1/2$, las cadenas típicas tienen $K(x) \approx nH(p)$ bits, exactamente como predice Shannon.

## Relación con Shannon

La entropía de Shannon habla de fuentes y promedios:

```text
cuántos bits esperamos necesitar para codificar mensajes de esta fuente
```

La complejidad de Kolmogorov habla de objetos concretos:

```text
cuántos bits necesita la mejor descripción efectiva de esta cadena
```

Ambas ideas se conectan a través de la compresión, pero responden preguntas
distintas.

## Incomputabilidad

Un resultado profundo es que `K(x)` no es computable en general. No existe un
algoritmo que tome cualquier cadena `x` y devuelva exactamente la longitud del
programa más corto que la produce.

La razón se relaciona con el problema de la parada: para saber si un programa es
la descripción mínima, habría que comparar su comportamiento con el de muchos
otros programas, incluyendo programas que quizá no terminen.

Así, la complejidad de Kolmogorov conecta directamente información,
computabilidad y límites formales.

## Compresión práctica

Los compresores reales no calculan `K(x)`. Usan familias concretas de patrones:

- repeticiones;
- diccionarios;
- frecuencias estadísticas;
- estructura local;
- modelos predictivos.

Si un compresor no reduce una cadena, eso no prueba que la cadena sea
algorítmicamente aleatoria. Solo indica que no encontró patrones dentro de sus
capacidades.

## Idea para recordar

La complejidad de Kolmogorov mide la longitud de la mejor descripción efectiva
de un objeto. Una cadena es simple si tiene una explicación corta; parece
aleatoria si ninguna descripción corta la reproduce.

## Ideas clave

- K(x) es la longitud del programa más corto que produce x; formaliza la complejidad de un objeto individual.
- K(x) es invariante salvo una constante aditiva respecto de la máquina universal de referencia.
- K(x) no es computable: no existe un algoritmo que, dado x, calcule K(x) exactamente.
- Una cadena x es algorítmicamente aleatoria si K(x) ≥ |x| − c; la mayoría de las cadenas lo son.
- El valor esperado 𝔼[K(X)] para X de una fuente Bernoulli(p) satisface 𝔼[K(X)] ≈ nH(p), conectando K con Shannon.


## Ejercicios

1. Propón una descripción corta para una cadena de 100 ceros.
2. ¿Por qué una cadena periódica suele ser compresible?
3. Explica la diferencia entre entropía de Shannon y complejidad de Kolmogorov.
4. ¿Por qué calcular exactamente `K(x)` entra en conflicto con los límites de la
   computabilidad?

## Véase también

- [Aleatoriedad algorítmica](../03-computabilidad/12-aleatoriedad-algoritmica.md)
- [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)

<!-- nav-start -->

---
← [Complejidad cuántica: BQP y QMA](../04-complejidad-computacional/14-complejidad-cuantica-bqp-qma.md) · [02 - Criptografía y complejidad](02-criptografia-y-complejidad.md) →

<!-- nav-end -->
