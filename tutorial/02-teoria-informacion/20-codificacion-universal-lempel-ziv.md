# Codificación Universal: Lempel-Ziv

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~22 min


## Prerrequisitos

- [Codificación de fuente y teorema de Shannon](03-codificacion-de-fuente.md)
- [Codificación aritmética](13-codificacion-aritmetica.md)
- [Procesos estocásticos y fuentes con memoria](14-procesos-estocasticos-y-fuentes-con-memoria.md)

## Objetivos de aprendizaje

1. Entender qué significa que un compresor sea *universal*: converge a la entropía sin conocer la distribución de la fuente.
2. Distinguir LZ77 (ventana deslizante) de LZ78 (diccionario incremental) y comprender sus garantías teóricas.
3. Relacionar LZ con el principio MDL y con la complejidad de Kolmogorov.
4. Interpretar correctamente las tasas de compresión de herramientas reales (gzip, zstd, 7z).


## Intuición

El teorema de codificación de fuente de Shannon establece que la longitud mínima de compresión de una fuente i.i.d. con entropía $H$ es $H$ bits por símbolo. Pero ese teorema supone que conocemos la distribución. ¿Qué ocurre cuando no la conocemos?

Abraham Lempel y Jacob Ziv respondieron esta pregunta en dos artículos publicados en 1977 y 1978. Su idea clave: en lugar de modelar la fuente, **reutilizar fragmentos ya vistos**. Un compresor que repite lo que ya vio es, implícitamente, un estimador de la distribución de la fuente — sin haber calculado ninguna probabilidad.

El resultado es sorprendente: ambos algoritmos convergen asintóticamente a la entropía de *cualquier* fuente ergódica estacionaria, sin ningún conocimiento previo sobre ella. Son **universalmente óptimos**.

## El problema de la codificación universal

Sea $X_1, X_2, \ldots$ un proceso estocástico estacionario ergódico con tasa de entropía:

$$\bar{H} = \lim_{n \to \infty} \frac{1}{n} H(X_1, \ldots, X_n)$$

Un codificador de longitud $L_n(x^n)$ es **universalmente óptimo** si para cualquier fuente de este tipo:

$$\lim_{n \to \infty} \frac{L_n(X^n)}{n} = \bar{H} \quad \text{con probabilidad 1}$$

La dificultad: no podemos usar la distribución verdadera para diseñar el código. Los algoritmos LZ la estiman implícitamente a partir de los propios datos.

## LZ78: diccionario incremental

LZ78 (Ziv y Lempel, 1978) construye un **diccionario** de frases durante la compresión.

### Algoritmo de compresión

1. Inicializar el diccionario con la frase vacía (índice 0).
2. Leer símbolos hasta encontrar una cadena $w$ que no esté en el diccionario.
3. Emitir el par $(\text{índice}(w[1..|w|-1]),\; w[|w|])$: el índice de la frase más larga ya conocida más el símbolo nuevo.
4. Añadir $w$ al diccionario con el siguiente índice disponible.
5. Repetir desde el paso 2.

### Ejemplo numérico

Fuente: `aababcababc`

| Paso | Frase nueva | Índice padre | Símbolo nuevo | Frase en dict. |
|------|------------|--------------|---------------|----------------|
| 1 | `a` | 0 (vacío) | a | 1: `a` |
| 2 | `ab` | 1 (`a`) | b | 2: `ab` |
| 3 | `aba` | 2 (`ab`) | a | 3: `aba` |
| 4 | `b` | 0 (vacío) | b | 4: `b` |
| 5 | `c` | 0 (vacío) | c | 5: `c` |
| 6 | `ababc` | 3 (`aba`) | b → continúa... | ... |

El diccionario crece de forma incremental. Cada nuevo símbolo extendido produce una entrada nueva: el número de frases $c(n)$ satisface $c(n) \cdot \log c(n) \approx n$, es decir $c(n) \approx n / \log n$.

### Codificación de los pares

Cada par (índice, símbolo) se codifica con $\lfloor \log_2 c \rfloor + 1$ bits para el índice (donde $c$ es el tamaño actual del diccionario) más $\log_2 |\mathcal{A}|$ bits para el símbolo. El coste total es:

$$L_n \approx c(n) \cdot (\log c(n) + \log |\mathcal{A}|) \approx n \cdot \frac{\log |\mathcal{A}| + 1}{1 + \log c(n) / \log |\mathcal{A}|}$$

### Garantía teórica (Ziv-Lempel 1978)

**Teorema.** Para cualquier fuente estacionaria ergódica con tasa de entropía $\bar{H}$:

$$\lim_{n \to \infty} \frac{L_n^{\text{LZ78}}(X^n)}{n} = \bar{H} \quad \text{c.s.}$$

La convergencia es en el sentido de casi segura (por la ley de los grandes números ergódica). La velocidad de convergencia es $O(1 / \log n)$ — lenta, por eso LZ78 necesita bloques largos para acercarse a la entropía.

**LZW** (Welch, 1984) es una variante de LZ78 donde el diccionario se inicializa con todos los símbolos del alfabeto, eliminando el campo "símbolo nuevo" del par emitido. Es la base de los formatos GIF y el comando `compress` de Unix.

## LZ77: ventana deslizante

LZ77 (Lempel y Ziv, 1977) usa un enfoque diferente: en lugar de un diccionario global creciente, busca coincidencias en una **ventana** de los $W$ bytes más recientes.

### Algoritmo de compresión

En cada posición de la entrada, el compresor busca la cadena más larga que aparezca en los últimos $W$ símbolos (la *ventana de búsqueda*). Emite una tripleta:

$$(\text{offset},\; \text{longitud},\; \text{símbolo siguiente})$$

- **offset:** cuántos símbolos atrás empieza la coincidencia.
- **longitud:** cuántos símbolos coinciden.
- **símbolo siguiente:** el primer símbolo que no coincide (o que inicia una nueva coincidencia).

Si no hay coincidencia, emite offset=0, longitud=0 y el símbolo literal.

### Ejemplo numérico

Texto: `abracadabra`, ventana $W = 10$.

| Posición | Coincidencia en ventana | Tripleta emitida |
|----------|------------------------|-----------------|
| 0: `a` | ninguna | (0, 0, a) |
| 1: `b` | ninguna | (0, 0, b) |
| 2: `r` | ninguna | (0, 0, r) |
| 3: `a` | pos 0, long 1 | (3, 1, c) |
| 5: `a` | pos 0, long 1 | (5, 1, d) |
| 7: `a` | pos 0, long 4 → `abra` | (7, 4, ∅) |

La tripleta `(7, 4, ∅)` en la posición 7 dice: "retrocede 7, copia 4 símbolos" → reproduce `abra` desde la ventana. Esto permite que LZ77 codifique repeticiones largas con un solo puntero.

### LZSS: variante práctica

LZSS (Storer-Szymanski, 1982) elimina el símbolo siguiente de las tripletas y usa un bit de control para distinguir literales de referencias. Reduce el overhead para coincidencias cortas. Es la base de **Deflate** (ZIP, gzip, PNG).

### Garantía teórica (Lempel-Ziv 1977)

**Teorema.** Para cualquier fuente estacionaria ergódica y ventana de tamaño $W \to \infty$:

$$\limsup_{n \to \infty} \frac{L_n^{\text{LZ77}}(X^n)}{n} \leq \bar{H} \quad \text{c.s.}$$

Con $W$ fijo, el exceso sobre $\bar{H}$ es $O(1 / \log W)$.

## Comparación LZ77 vs LZ78

| Característica | LZ77 | LZ78 / LZW |
|---------------|------|-----------|
| Estructura | Ventana deslizante | Diccionario incremental |
| Memoria | $O(W)$ — ventana fija | $O(2^k)$ — diccionario crece |
| Búsqueda de coincidencias | En la ventana (puede ser lenta) | En el diccionario (árbol/hash) |
| Convergencia | $O(1/\log W)$ | $O(1/\log n)$ |
| Aplicaciones | gzip, zlib, PNG, zstd (backend) | GIF, TIFF, PDF, `compress` |
| Decodificación | Un paso, muy rápida | Un paso, muy rápida |

La mayoría de los compresores modernos usan variantes de LZ77 porque la búsqueda en ventana se puede paralelizar y acelerar con estructuras como árboles de sufijos o tablas hash.

## Compresores modernos basados en LZ

| Compresor | Base | Velocidad | Ratio |
|-----------|------|-----------|-------|
| gzip | LZ77 + Huffman (Deflate) | Media | Bueno |
| bzip2 | BWT + RLE + Huffman | Lenta | Mejor |
| lz4 | LZ77 simplificado | Muy rápida | Menor |
| zstd | LZ77 + ANS | Muy rápida | Excelente |
| 7z (LZMA) | LZ77 + cadenas de Markov | Lenta | Óptimo en texto |
| xz | LZMA | Lenta | Óptimo en texto |

**Deflate** (RFC 1951), usado en gzip y PNG, combina LZ77 con códigos de Huffman: primero LZ77 reduce las repeticiones a punteros, luego Huffman comprime los literales y las longitudes. Esta combinación es la más usada en la historia de la compresión.

**zstd** (Facebook, 2016) es el estado del arte: velocidades de varios GB/s con ratios comparables a bzip2.

## Relación con la complejidad de Kolmogorov

La longitud de descripción LZ de una cadena $x^n$ es una aproximación computable de la **complejidad de Kolmogorov** $K(x^n)$: la longitud del programa más corto que genera $x^n$.

- Si $x^n$ tiene mucha estructura repetitiva → el diccionario LZ crece lentamente → $L_n^{\text{LZ}} \ll n$.
- Si $x^n$ es aleatoria → cada frase es nueva → $L_n^{\text{LZ}} \approx n$.

Esta conexión justifica usar la **distancia de compresión normalizada** (NCD) como medida de similitud entre cadenas, sin necesidad de un modelo probabilístico explícito.

## Relación con el principio MDL

Desde la perspectiva MDL, el compresor LZ implementa un **estimador implícito del modelo**: el diccionario o la ventana codifican la regularidad de la fuente. La longitud de compresión LZ es la longitud de descripción MDL del modelo más los datos dado el modelo, integrados en un solo paso.

Para $n$ grande, el teorema de Ziv-Lempel garantiza que este estimador implícito es asintóticamente óptimo: ningún modelo explícito puede hacer mejor.

## Ejemplo: estimación de entropía por compresión

Dado un texto de $n = 100{,}000$ bytes en español comprimido a $L = 35{,}000$ bytes con gzip:

$$\hat{\bar{H}} \approx \frac{L}{n} \times 8 \text{ bits/byte} = \frac{35{,}000}{100{,}000} \times 8 = 2.8 \text{ bits/byte}$$

Esto es una estimación de la tasa de entropía del español a nivel de byte. La entropía real del español a nivel de carácter es aproximadamente 1.3 bits/carácter — la diferencia se debe al encoding UTF-8 (multibyte) y al overhead del compresor en bloques finitos.


## Ideas clave

- Un compresor universal converge a $\bar{H}$ sin conocer la distribución de la fuente, solo observando los datos.
- LZ77 usa una ventana deslizante y emite punteros (offset, longitud); LZ78 construye un diccionario incremental de frases.
- Ambos convergen a la tasa de entropía de cualquier fuente estacionaria ergódica: son universalmente óptimos.
- La velocidad de convergencia es $O(1/\log n)$ — lenta; gzip y zstd aceleran esto con Huffman/ANS como segunda etapa.
- La longitud de compresión LZ es una aproximación computable de la complejidad de Kolmogorov y un estimador MDL implícito.

## Ejercicios

1. Aplicar LZ78 a la cadena `aaabaaab`. Construir el diccionario paso a paso y calcular el número de frases $c(n)$. ¿Cuántos bits necesitas para codificar los pares si el diccionario usa $\lfloor \log_2 c \rfloor + 1$ bits para el índice?

2. Aplicar LZ77 con ventana $W = 6$ a la cadena `abcabcabc`. Listar las tripletas emitidas y calcular la longitud total si cada offset usa 3 bits, cada longitud 3 bits, y cada literal 8 bits.

3. Una fuente produce bits i.i.d. con $P(0) = 0.9$, $P(1) = 0.1$. Su entropía es $H \approx 0.469$ bits/símbolo. Si LZ78 produce $c(n) = n / \log n$ frases en una secuencia de $n = 10^6$ bits, estima la longitud de la descripción LZ y compárala con el óptimo $nH$.

4. Explica por qué LZW (variante de LZ78 usada en GIF) no puede representar imágenes fotográficas eficientemente. ¿Qué característica de las imágenes lo hace ineficaz?

5. La distancia de compresión normalizada entre dos cadenas $x$ e $y$ se define como:
$$\text{NCD}(x, y) = \frac{C(xy) - \min(C(x), C(y))}{\max(C(x), C(y))}$$
donde $C(\cdot)$ es la longitud comprimida. Calcular $\text{NCD}$ para $x = \texttt{aaaa}$ e $y = \texttt{bbbb}$ con un compresor ideal. ¿Y para $x = y = \texttt{aaaa}$?

## Véase también

- [Codificación de fuente y teorema de Shannon](03-codificacion-de-fuente.md)
- [Codificación aritmética](13-codificacion-aritmetica.md)
- [Complejidad de Kolmogorov](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md)
- [MDL y selección de modelos](../05-conexiones-y-aplicaciones/13-mdl-y-seleccion-de-modelos.md)



<!-- nav-start -->

---
← [Códigos Turbo y el Algoritmo BCJR](19-codigos-turbo.md) · [01 - El problema de la parada](../03-computabilidad/01-problema-de-la-parada.md) →

<!-- nav-end -->
## Referencias

- Ziv, J. y Lempel, A. (1977). A universal algorithm for sequential data compression. *IEEE Trans. Information Theory*, 23(3), 337–343.
- Ziv, J. y Lempel, A. (1978). Compression of individual sequences via variable-rate coding. *IEEE Trans. Information Theory*, 24(5), 530–536.
- Welch, T.A. (1984). A technique for high-performance data compression. *IEEE Computer*, 17(6), 8–19.
- Cover, T.M. y Thomas, J.A. (2006). *Elements of Information Theory*, 2ª ed. Wiley, cap. 13.
- Deutsch, P. (1996). DEFLATE Compressed Data Format Specification. RFC 1951.
- Collet, Y. (2016). Zstandard — Real-time data compression algorithm. Facebook Open Source.
