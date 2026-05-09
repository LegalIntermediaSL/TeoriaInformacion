# Códigos LDPC y Turbo: Hacia la Capacidad de Shannon

## Intuición

Durante casi 50 años tras el teorema de Shannon (1948), los códigos existentes quedaban
lejos de la capacidad teórica: el "abismo de Shannon" parecía inalcanzable en la práctica.
Los **códigos turbo** (Berrou et al., 1993) y los **códigos LDPC** (Gallager, 1960; redescubiertos
en 1995) rompieron esta barrera, demostrando que se puede comunicar a tasas arbitrariamente
cercanas a la capacidad con decodificadores de coste polinomial.

## Códigos LDPC

Un **código LDPC** (*Low-Density Parity-Check*) es un código lineal binario definido por
una matriz de paridad $H$ de baja densidad: la mayoría de las entradas son 0.

**Parámetros:**
- $n$: longitud del bloque (número de bits).
- $k$: dimensión (bits de información). Tasa $R = k/n$.
- $m = n - k$: número de ecuaciones de paridad (filas de $H$).
- $d_v$: grado de las variables (número de 1 en cada columna de $H$).
- $d_c$: grado de las restricciones (número de 1 en cada fila de $H$).

Un código $(d_v, d_c)$-regular tiene todos los grados iguales, con $Rd_c = d_v$ (por
conteo de aristas).

### Representación bipartita: grafo de Tanner

El código se visualiza como un **grafo bipartito** (Tanner graph) con:
- **Nodos variable** $v_1, \ldots, v_n$: un nodo por cada bit del codeword.
- **Nodos restricción** $c_1, \ldots, c_m$: un nodo por cada ecuación de paridad.
- Una arista $(v_i, c_j)$ si $H_{ji} = 1$.

La ausencia de ciclos cortos (especialmente de longitud 4) es crucial para el rendimiento
del decodificador.

## Decodificación por propagación de creencias (Belief Propagation)

El algoritmo de **propagación de creencias** (BP, también llamado *sum-product* o
*mensaje-pasante*) es el decodificador estándar para LDPC.

**Idea:** cada nodo pasa mensajes a sus vecinos. Los mensajes son distribuciones de probabilidad
sobre los valores posibles del nodo. La iteración converge (en grafos sin ciclos, exactamente;
en grafos con ciclos, aproximadamente) a las probabilidades marginales.

**Mensajes de nodo variable $v$ a restricción $c$:**
$$\mu_{v \to c}(x) \propto p(y_v | x) \prod_{c' \in \mathcal{N}(v) \setminus c} \mu_{c' \to v}(x)$$

**Mensajes de restricción $c$ a variable $v$:**
$$\mu_{c \to v}(x) \propto \sum_{\mathbf{x}': x'_v = x} \mathbf{1}[\text{paridad cumplida}] \prod_{v' \in \mathcal{N}(c) \setminus v} \mu_{v' \to c}(x'_{v'})$$

**Inicialización:** $\mu_{c \to v}^{(0)} = (1/2, 1/2)$ (uniforme).

**Criterio de parada:** cuando todas las ecuaciones de paridad se satisfacen, o tras
un número máximo de iteraciones.

En la práctica se trabaja con **log-likelihood ratios** (LLRs) $L = \log(P(x=0)/P(x=1))$,
lo que convierte multiplicaciones en sumas y mejora la estabilidad numérica.

## Análisis de densidad de evolución

Para códigos LDPC irregulares aleatorios, el comportamiento asintótico del decodificador BP
puede analizarse exactamente mediante **density evolution** (DE):

- Para un canal BSC con volteo $p$, la distribución de los LLRs en cada iteración
  es determinista en el límite $n \to \infty$.
- Existe un **umbral** $p^*$ tal que BP decodifica correctamente si $p < p^*$.
- El umbral puede optimizarse sobre la distribución de grados del código (diseño DE).

Los códigos LDPC irregulares optimizados vía DE llegan a $< 0.01$ dB del límite de Shannon.

## Códigos turbo

Los **códigos turbo** (Berrou, Glavieux, Thitimajshima, 1993) consisten en:

1. **Dos codificadores convolucionales** de tasa $1/2$ conectados por un entrelazador
   (permutación pseudoaleatoria de los bits de información).
2. La secuencia transmitida incluye los bits de información y las paridades de ambos
   codificadores (tasa total $\approx 1/3$).

**Decodificación iterativa:**
1. El decodificador 1 calcula probabilidades suaves usando el canal y la información
   extrínseca del decodificador 2.
2. El decodificador 2 refina esas probabilidades usando la permutación inversa.
3. Las iteraciones se repiten hasta convergencia.

Cada decodificador usa el algoritmo **BCJR** (Bahl-Cocke-Jelinek-Raviv), que calcula
las probabilidades a posteriori óptimas para un código convolucional.

El entrelazador es crucial: rompe las correlaciones entre los dos decodificadores,
permitiendo que cada uno "descubra" errores que el otro no puede ver.

## Códigos polares

Los **códigos polares** (Arıkan, 2009) son la única familia de códigos de corrección
de errores que **alcanza exactamente** la capacidad de canal con complejidad $O(n \log n)$.

Se basan en la **polarización de canal**: combinar $n$ copias ruidosas del canal produce
dos tipos de canales sintéticos: unos muy buenos (fiables) y otros muy malos (completamente
ruidosos). La información se transmite solo por los canales buenos.

La construcción es recursiva: para $n = 2^k$, se construyen $n$ canales sintéticos
usando $\frac{n}{2}$ pares $(u_1 + u_2, u_2)$.

Los códigos polares son el estándar en 5G (control plane, canal de control de acceso).

## Comparación práctica

| Código | Gap a la capacidad | Complejidad decodificación |
|--------|-------------------|---------------------------|
| Hamming (7,4) | $> 2$ dB | $O(n)$ |
| Convolucional + Viterbi | $\approx 2$ dB | $O(n \cdot 2^K)$ |
| Turbo | $< 0.5$ dB | $O(n \cdot I)$ iteraciones |
| LDPC irregular | $< 0.1$ dB | $O(n \cdot I)$ iteraciones |
| Polar | $\to 0$ asintóticamente | $O(n \log n)$ |

## Ideas clave

- Los códigos LDPC se definen por matrices de paridad escasas y se decodifican con
  propagación de creencias (BP) en el grafo de Tanner.
- La evolución de densidad permite analizar y optimizar el umbral de decodificación BP
  para acercarse a la capacidad de Shannon.
- Los códigos turbo explotan la decodificación iterativa entre dos codificadores convolucionales
  vinculados por un entrelazador.
- Los códigos polares son los únicos que alcanzan teóricamente la capacidad con $O(n \log n)$.
- Todos estos códigos son usados en sistemas modernos: LDPC en WiFi (802.11) y 5G (data plane);
  polares en 5G (control plane); turbo en 3G/4G.

## Ejercicios

1. Dibuja el grafo de Tanner del código con matriz de paridad $H = \begin{pmatrix} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 1 \end{pmatrix}$. ¿Tiene ciclos de longitud 4?
2. ¿Cuántos bits de información tiene un código LDPC $(3,6)$-regular de longitud $n$? ¿Cuál es su tasa?
3. Explica intuitivamente por qué los ciclos cortos en el grafo de Tanner degradan el rendimiento del decodificador BP.
4. ¿Por qué el entrelazador es esencial en los códigos turbo? ¿Qué ocurriría si los dos codificadores procesaran los bits en el mismo orden?
5. Los códigos polares alcanzan la capacidad pero tienen mal rendimiento en longitudes cortas. ¿Qué técnica práctica se usa para mejorarlos en ese régimen?

## Referencias

- Gallager, R. G. (1962). Low-density parity-check codes. *IRE Trans. Information Theory*.
- Berrou, C., Glavieux, A. y Thitimajshima, P. (1993). Near Shannon limit error-correcting coding. *ICC 1993*.
- Richardson, T. y Urbanke, R. (2008). *Modern Coding Theory*. Cambridge University Press.
- Arıkan, E. (2009). Channel polarization. *IEEE Trans. Information Theory*.
