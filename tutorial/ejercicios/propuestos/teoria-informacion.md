# Ejercicios propuestos — Teoría de la información

Extraídos de los artículos del módulo 02.

---

## Entropía y fuentes discretas (02/01)

1. Calcula la entropía $H(X)$ de una moneda sesgada con $P(\text{cara}) = 0.3$.
2. ¿Cuándo es máxima la entropía de una variable aleatoria con $n$ valores?
3. Demuestra que $H(X) \geq 0$ para cualquier distribución discreta.

## Información mutua (02/02)

4. Si $X$ e $Y$ son independientes, ¿cuánto vale $I(X;Y)$? Justifica con la definición.
5. Calcula $I(X;Y)$ para el canal binario simétrico con parámetro $p=0.1$ y distribución de entrada uniforme.
6. Demuestra la desigualdad de procesamiento de datos: si $X \to Y \to Z$, entonces $I(X;Z) \leq I(X;Y)$.

## Códigos prefijo y Huffman (02/03)

7. Construye el código Huffman para la distribución $P = (0.4, 0.3, 0.2, 0.1)$ y calcula la longitud media.
8. ¿Por qué todo código Huffman satisface la desigualdad de Kraft $\sum 2^{-l_i} \leq 1$?
9. Diseña un código de bloque de orden 2 para la fuente $P = (0.9, 0.1)$ y compara la longitud media con la entropía.

## Canal binario simétrico (02/08)

10. Calcula la capacidad del BSC con $p = 0.05$ y $p = 0.5$. ¿Qué observas en los casos extremos?
11. Para un canal con capacidad $C = 0.7$ bits/uso, ¿qué tasas $R$ son transmisibles con probabilidad de error arbitrariamente pequeña?
12. Explica en palabras el significado del teorema de Shannon (codificación de canal). ¿Qué no garantiza?

## Tasa-distorsión (02/09)

13. Para una fuente Bernoulli($p=0.3$) con distorsión de Hamming, calcula $R(D)$ para $D = 0$ y $D = 0.1$.
14. ¿Por qué $R(D)$ es convexa en $D$? ¿Qué implica intuitivamente?
15. Una imagen de 8 bits/píxel se comprime con distorsión máxima $D = 5\%$. ¿Cuánto puede reducirse la tasa respecto al caso sin distorsión?

## Codificación aritmética (02/13)

16. Codifica la cadena "00" con codificación aritmética para la distribución $P(0) = 0.6$, $P(1) = 0.4$.
17. ¿Por qué la codificación aritmética se acerca más a la entropía que Huffman para cadenas largas?

## Procesos estocásticos (02/14)

18. Una cadena de Markov de orden 1 tiene matriz de transición $T = \begin{pmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{pmatrix}$. Calcula su tasa de entropía.
19. ¿Por qué las fuentes ergódicas permiten estimar la tasa de entropía a partir de una única cadena larga?
