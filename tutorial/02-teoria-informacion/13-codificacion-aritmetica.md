# Codificación aritmética

## Intuición

El código de Huffman asigna un número entero de bits a cada símbolo. Esto introduce un desperdicio inevitable cuando la entropía no es entera: si un símbolo tiene probabilidad 0.9, merece $-\log_2 0.9 \approx 0.15$ bits, pero Huffman le asigna 1 bit. La **codificación aritmética** elimina esa ineficiencia representando un mensaje entero como un único número real dentro del intervalo $[0, 1)$, y puede acercarse arbitrariamente a la entropía de la fuente sin necesidad de símbolo por símbolo.

## El intervalo como código

La idea central: se asigna a cada posible mensaje de longitud $n$ un subintervalo de $[0,1)$ de longitud proporcional a su probabilidad. Para descodificar, basta saber en qué subintervalo cae el número recibido.

**Codificación de una secuencia $x_1 x_2 \ldots x_n$:**

1. Comienza con el intervalo $[0, 1)$.
2. Para cada símbolo $x_i$ con distribución $P$:
   - Divide el intervalo actual en subintervalos proporcionales a las probabilidades de cada símbolo, en orden fijo.
   - Selecciona el subintervalo correspondiente a $x_i$.
3. Tras procesar todos los símbolos, el intervalo final tiene longitud $\prod_i P(x_i) = P(x_1 \ldots x_n)$.
4. Transmite cualquier número binario que caiga dentro de ese intervalo, usando $\lceil -\log_2 P(x_1 \ldots x_n) \rceil + 1$ bits.

## Ejemplo detallado

Fuente binaria con $P(0) = 0.8$, $P(1) = 0.2$. Codificar la secuencia `011`.

**Paso 1:** Intervalo inicial $[0, 1)$.

Asignación de subintervalos (siempre el mismo orden):
- $0 \to [0.0, 0.8)$
- $1 \to [0.8, 1.0)$

**Paso 2:** Símbolo `0` → seleccionar $[0.0, 0.8)$.

Dentro de $[0.0, 0.8)$, dividir proporcionalmente:
- $0 \to [0.00, 0.64)$  (0.8 del intervalo)
- $1 \to [0.64, 0.80)$ (0.2 del intervalo)

**Paso 3:** Símbolo `1` → seleccionar $[0.64, 0.80)$.

Dentro de $[0.64, 0.80)$, longitud $= 0.16$:
- $0 \to [0.640, 0.768)$ (0.8 de 0.16 = 0.128)
- $1 \to [0.768, 0.800)$ (0.2 de 0.16 = 0.032)

**Paso 4:** Símbolo `1` → seleccionar $[0.768, 0.800)$.

Intervalo final: $[0.768, 0.800)$, longitud $= 0.032 = 0.8 \cdot 0.2 \cdot 0.2 = P(011)$.

**Longitud del código:** $\lceil -\log_2 0.032 \rceil + 1 = \lceil 4.97 \rceil + 1 = 6$ bits.

Entropía teórica de `011`: $H(0.8) \cdot 3 \approx 0.722 \cdot 3 = 2.17$ bits. El overhead con este método es pequeño y tiende a cero conforme $n \to \infty$.

## Algoritmo de descodificación

Dado un número $v \in [0,1)$ y la longitud $n$ del mensaje original:

```
intervalo ← [0, 1)
para i = 1 hasta n:
    para cada símbolo s (en orden):
        subintervalo ← parte de [intervalo] proporcional a P(s)
        si v ∈ subintervalo:
            emitir s
            intervalo ← subintervalo
            romper
```

La descodificación es unívoca porque los subintervalos de cada paso son disjuntos.

## Implementación entera (aproximación práctica)

Los números reales de precisión arbitraria son costosos. En la práctica se usa aritmética entera con un rango $[0, 2^M)$ (típicamente $M = 32$):

- Los límites del intervalo se mantienen como enteros `low` y `high`.
- Cuando el intervalo se estrecha y los bits superiores de `low` y `high` coinciden, se emite ese bit y se escala el intervalo ($\times 2$).
- Se añade la técnica de **underflow** para casos donde los límites convergen sin compartir el bit más significativo.

Este mecanismo hace que la codificación aritmética sea **online** (emite bits sin necesidad de procesar todo el mensaje de antemano) y se ejecute en tiempo $O(n)$.

## Relación con la entropía

**Teorema.** La longitud esperada del código aritmético sobre una fuente i.i.d. con probabilidades $P$ satisface:

$$H(X) \leq \mathbb{E}[L_n] / n < H(X) + 2/n$$

Para $n$ grande, la tasa de bits tiende a la entropía $H(X)$. Esto supera a Huffman en dos aspectos:

1. Huffman sobre símbolos individuales puede superar $H(X) + 1$ bits por símbolo.
2. Huffman sobre bloques de $k$ símbolos reduce el exceso a $1/k$, pero requiere construir un árbol de $|\Sigma|^k$ símbolos. La codificación aritmética obtiene el mismo resultado sin este coste.

## Aplicaciones

La codificación aritmética es el corazón de:

- **DEFLATE** (zlib, PNG, ZIP): combinado con LZ77 para modelado de contexto.
- **CABAC** en H.264/H.265/H.266 (video): codificación aritmética adaptativa basada en contexto para comprimir residuos de predicción.
- **JPEG2000**: usa codificación aritmética en los coeficientes wavelet.
- **LZMA / 7-Zip**: modelo de contexto con probabilidades adaptativas + codificación aritmética de rango.

La clave práctica es combinar un **modelo probabilístico** (que estima $P(x_i | x_1 \ldots x_{i-1})$) con el codificador aritmético: cuanto mejor el modelo, más se acerca la tasa a la entropía condicional $H(X_i | X_{i-1} \ldots)$.

## Codificación adaptativa

En lugar de probabilidades fijas, se actualizan las estimaciones de $P$ conforme se codifica:

1. Inicializar con distribución uniforme.
2. Codificar $x_i$ con las probabilidades actuales.
3. Actualizar el modelo con la observación $x_i$ (conteos o mezcla Bayesiana).

Este esquema logra tasas próximas a $H(X)$ **sin conocer de antemano las probabilidades de la fuente**, y es el fundamento teórico de compresores universales como Prediction by Partial Matching (PPM).

## Ideas clave

1. La codificación aritmética representa mensajes enteros como intervalos reales, no símbolo a símbolo.
2. La longitud del intervalo es exactamente la probabilidad del mensaje.
3. La longitud del código se acerca a la entropía con error que tiende a cero.
4. La implementación práctica usa aritmética entera con escalado bit a bit.
5. Combinada con un buen modelo adaptativo es la base de los mejores compresores actuales.

## Ejercicios

1. Codifica la secuencia `000` con la fuente del ejemplo ($P(0) = 0.8$). ¿Cuántos bits necesitas? Compara con Huffman.

2. ¿Por qué el decodificador puede recuperar la secuencia original aunque haya infinitos números reales en el intervalo final?

3. Demuestra que el intervalo final de la codificación de $x_1 \ldots x_n$ tiene longitud $\prod_{i=1}^n P(x_i)$.

4. ¿Qué ventaja tiene la codificación aritmética adaptativa sobre Huffman adaptativo para alfabetos con alta entropía ($H \approx \log_2 |\Sigma|$)?

## Referencias

- Cover, T.M. y Thomas, J.A. (2006). *Elements of Information Theory*, 2ª ed., cap. 5. Wiley.
- Rissanen, J. y Langdon, G.G. (1979). Arithmetic coding. *IBM Journal of Research and Development*, 23(2), 149–162.
- Witten, I.H., Neal, R.M. y Cleary, J.G. (1987). Arithmetic coding for data compression. *Communications of the ACM*, 30(6), 520–540.
- Moffat, A., Neal, R.M. y Witten, I.H. (1998). Arithmetic coding revisited. *ACM TOIS*, 16(3), 256–294.
