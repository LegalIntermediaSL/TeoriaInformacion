# Teorema de Shannon y Capacidad de Canal

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Canales discretos y capacidad](04-canales-discretos-y-capacidad.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)

## Objetivos de aprendizaje

1. Enunciar y entender el teorema de codificación de canal de Shannon.
2. Distinguir capacidad de canal, tasa y probabilidad de error.
3. Aplicar el argumento de codificación aleatoria en la prueba del teorema.


## Intuición

Shannon demostró en 1948 algo que parecía imposible: existe un límite preciso y alcanzable para la tasa de transmisión de información sin errores sobre un canal ruidoso. Ese límite es la **capacidad del canal** $C$, y el teorema de codificación de canal garantiza que se puede transmitir a cualquier tasa $R < C$ con probabilidad de error tan pequeña como se quiera, eligiendo el código adecuado.

Antes de Shannon, la intuición común era que reducir errores obligaba a reducir la velocidad de transmisión de forma continua: menos ruido exige más redundancia, más redundancia implica más lentitud. Shannon demostró que esto es falso: hay un umbral nítido, no un compromiso gradual.

## La capacidad de canal

Para un canal discreto sin memoria con entrada $X$, salida $Y$ y distribución condicional $p(y|x)$, la capacidad es:

$$
C = \max_{p(x)} I(X; Y)
$$

donde el máximo se toma sobre todas las distribuciones de entrada $p(x)$. La información mutua $I(X;Y) = H(Y) - H(Y|X)$ mide cuánta información sobre la entrada se puede recuperar en la salida.

**Canal binario simétrico (BSC):** la entrada $X \in \{0,1\}$ se voltea con probabilidad $\epsilon$ y se transmite correctamente con probabilidad $1-\epsilon$. La capacidad es:

$$
C_\text{BSC} = 1 - H_b(\epsilon) = 1 - (-\epsilon\log_2\epsilon - (1-\epsilon)\log_2(1-\epsilon))
$$

Para $\epsilon = 0$ (canal sin ruido): $C = 1$ bit. Para $\epsilon = 0.5$ (ruido máximo, canal inútil): $C = 0$. Para $\epsilon = 0.1$: $C \approx 0.531$ bits.

**Canal borrador binario (BEC):** la entrada $X \in \{0,1\}$ se recibe correctamente con probabilidad $1-\epsilon$ y se borra (símbolo $?$) con probabilidad $\epsilon$. La capacidad es:

$$
C_\text{BEC} = 1 - \epsilon
$$

La capacidad del BEC es más alta que la del BSC para el mismo nivel de ruido, porque el borrado indica cuándo falló la transmisión.

## El teorema de codificación de canal

**Teorema (Shannon, 1948):** Sea $C$ la capacidad de un canal discreto sin memoria. Para cualquier tasa $R < C$ y cualquier $\delta > 0$, existe un código de bloque de longitud $n$ suficientemente grande tal que la probabilidad máxima de error de decodificación es menor que $\delta$.

Recíprocamente, para cualquier secuencia de códigos con tasa $R > C$, la probabilidad máxima de error no puede tender a cero.

**Lo que garantiza:** se puede comunicar a tasa $R < C$ con error arbitrariamente pequeño. No dice cómo construir el código; solo que existe.

**Lo que no garantiza:** no dice que el código sea eficiente de construir ni de decodificar. Encontrar códigos que alcancen la capacidad con decodificación eficiente fue el problema central de la codificación de canal durante 50 años (turbocodes 1993, LDPC redescubiertos 1995, códigos polares 2009).

## Demostración: el argumento de codificación aleatoria

La prueba original de Shannon usa un argumento no constructivo: elige el código al azar y demuestra que en promedio funciona bien.

1. **Generación del libro de códigos:** elegir $M = 2^{nR}$ palabras código de longitud $n$ muestreando cada símbolo de forma i.i.d. según la distribución $p^*(x)$ que maximiza $I(X;Y)$.

2. **Codificación:** el mensaje $m \in \{1,\ldots,M\}$ se envía como la $m$-ésima palabra código.

3. **Decodificación por tipicidad:** el receptor declara que recibió el mensaje $m$ si la palabra código $m$ y la salida $y^n$ son **conjuntamente típicas** y ninguna otra palabra código lo es.

4. **Análisis del error:** la probabilidad de que la palabra código correcta no sea típica con $y^n$ tiende a 0 (por el teorema de equipartición). La probabilidad de que una palabra incorrecta sea conjuntamente típica con $y^n$ es aproximadamente $2^{-n(I(X;Y)-R)}$, que tiende a 0 si $R < I(X;Y)$.

La clave es el **teorema de equipartición asintótica (AEP)**: para una fuente i.i.d. de entropía $H$, casi toda secuencia larga pertenece al **conjunto típico** de tamaño $\approx 2^{nH}$, y la probabilidad de cada elemento típico es $\approx 2^{-nH}$.

## El conjunto típico

Sea $\epsilon > 0$. El conjunto típico $A_\epsilon^{(n)}$ de la fuente i.i.d. $p(x)$ con entropía $H(X)$ es:

$$
A_\epsilon^{(n)} = \left\{ x^n : \left| -\frac{1}{n}\log p(x^n) - H(X) \right| < \epsilon \right\}
$$

Propiedades:
- $P(A_\epsilon^{(n)}) > 1 - \epsilon$ para $n$ suficientemente grande.
- $|A_\epsilon^{(n)}| \leq 2^{n(H+\epsilon)}$.
- $|A_\epsilon^{(n)}| \geq (1-\epsilon) \cdot 2^{n(H-\epsilon)}$.

Intuitivamente: aunque hay $2^n$ secuencias posibles, casi toda la probabilidad se concentra en $\approx 2^{nH}$ de ellas. Esto justifica que $H$ bits sean suficientes para comprimir la fuente.

## Capacidad del canal gaussiano

El canal gaussiano con ruido aditivo es $Y = X + Z$ con $Z \sim \mathcal{N}(0, N)$ y restricción de potencia $E[X^2] \leq P$. Su capacidad es:

$$
C = \frac{1}{2}\log_2\left(1 + \frac{P}{N}\right) \text{ bits por uso}
$$

Esta es la **fórmula de Shannon-Hartley**, y es la base de la capacidad de cualquier canal de comunicaciones analógico. La relación señal-ruido (SNR) $P/N$ determina completamente la capacidad. Duplicar la potencia añade medio bit de capacidad; duplicar el ancho de banda (más usos por segundo) duplica la capacidad.

## Separación fuente-canal

Un resultado notable del teorema de Shannon es el **principio de separación**: es óptimo diseñar el compresor (codificación de fuente) y el corrector de errores (codificación de canal) de forma independiente.

- Primero comprimir la fuente hasta su entropía $H$ (codificación de fuente óptima).
- Luego añadir redundancia hasta la capacidad del canal $C$ (codificación de canal óptima).

Si $H < C$, la transmisión sin error arbitrariamente pequeña es posible. Si $H > C$, es imposible, sin importar el sistema que se diseñe. La separación es óptima asintóticamente, aunque en sistemas de baja latencia puede ser subóptima.

## Ideas clave

- La capacidad $C = \max_{p(x)} I(X;Y)$ es el máximo de información mutua sobre todas las distribuciones de entrada.
- El teorema de Shannon garantiza comunicación sin errores a cualquier tasa $R < C$; por encima de $C$ es imposible.
- La prueba usa codificación aleatoria y decodificación por tipicidad, no una construcción explícita.
- El conjunto típico es el núcleo del argumento: $2^{nH}$ secuencias concentran casi toda la probabilidad.
- La fórmula Shannon-Hartley $C = \frac{1}{2}\log(1+\text{SNR})$ rige la capacidad de los canales analógicos.

## Ejercicios

1. Calcular $C_\text{BSC}$ para $\epsilon \in \{0.01, 0.1, 0.2, 0.5\}$ y dibujar la curva $C$ frente a $\epsilon$.
2. Un canal borra cada bit con probabilidad $0.3$ y transmite el resto correctamente. ¿Cuántos bits de mensaje pueden transmitirse por cada 100 usos del canal?
3. Verificar que el conjunto típico de una fuente uniforme sobre $\{0,1\}^n$ es todo $\{0,1\}^n$. ¿Cuánto vale $H$ en ese caso?
4. Demostrar que si $R > C$, la probabilidad de error media sobre libros de códigos aleatorios no puede tender a cero. (Pista: usar la desigualdad de Fano.)

## Véase también

- [Teoría de tasa-distorsión](09-teoria-tasa-distorsion.md)
- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)


## Referencias

- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423.
- Cover, T.M. y Thomas, J.A. (2006). *Elements of Information Theory*, 2ª ed., capítulos 7 y 8.
- MacKay, D.J.C. (2003). *Information Theory, Inference, and Learning Algorithms*, capítulo 9. Disponible en línea.
