# 13 - MDL y selección de modelos

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~20 min

## Prerrequisitos

- [Complejidad de Kolmogorov](01-complejidad-de-kolmogorov.md)
- [Codificación de fuente y teorema de Shannon](../02-teoria-informacion/03-codificacion-de-fuente.md)
- [Divergencia KL y entropía relativa](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)

## Objetivos de aprendizaje

1. Formular el principio MDL de Rissanen y distinguirlo del criterio de máxima verosimilitud.
2. Derivar la complejidad estocástica y la distribución NML para modelos paramétricos.
3. Relacionar MDL con BIC y con la complejidad de Kolmogorov.
4. Conectar el prior universal de Solomonoff con la inducción bayesiana computable.
5. Aplicar MDL a problemas reales de selección de modelos estadísticos.

## Intuición

Imagina que has ajustado una curva a cien puntos de datos. Un polinomio de grado 1 no captura toda la variabilidad; un polinomio de grado 10 pasa exactamente por cada punto, pero dibuja oscilaciones absurdas entre ellos. El modelo de grado 10 *recuerda* los datos en lugar de *aprenderlos*.

El principio de longitud mínima de descripción (MDL, por *Minimum Description Length*) formaliza esta intuición mediante la teoría de la información: el mejor modelo no es el que ajusta mejor, sino el que **describe los datos más compactamente**. Describir bien implica tanto capturar regularidades como no malgastar bits en la estructura de un modelo demasiado complejo. Esta idea, debida a Jorma Rissanen, convierte la selección de modelos en un problema de compresión.

## Principio MDL de dos partes

### Formulación

Dado un conjunto de datos $x^n = (x_1, \ldots, x_n)$ y una clase de modelos $\mathcal{M}$, la **longitud total de descripción de dos partes** de un modelo $M \in \mathcal{M}$ es:

$$L(x^n, M) = L(M) + L(x^n \mid M)$$

donde:

- $L(M)$ es el número de bits necesarios para describir el modelo (parámetros, estructura),
- $L(x^n \mid M)$ es el número de bits para describir los datos dado el modelo, es decir, $-\log_2 p(x^n; \hat{\theta}(x^n))$ con el estimador de máxima verosimilitud $\hat{\theta}$.

El **modelo MDL óptimo** minimiza $L(x^n, M)$ sobre $\mathcal{M}$.

### Comparación con MLE

El estimador de máxima verosimilitud maximiza $\log p(x^n \mid M)$ sin ninguna penalización por la complejidad de $M$. En términos de longitud de descripción, MLE minimiza solo el segundo término e ignora $L(M)$. El resultado es que MLE sobreajusta sistemáticamente cuando la clase de modelos crece con los datos.

MDL añade explícitamente el coste de describir el modelo, penalizando la complejidad de forma proporcional a la información necesaria para especificarlo.

### Ejemplo: regresión polinómica

Consideremos $n = 100$ observaciones y modelos polinómicos de grado $d$. Cada coeficiente requiere aproximadamente $\tfrac{1}{2}\log_2 n$ bits bajo la penalización estándar (ver sección siguiente). La tabla muestra estimaciones ilustrativas:

| Grado $d$ | Parámetros $k$ | $-\log_2 p(x^n;\hat{\theta})$ (bits) | $L(M)$ (bits) | Total $L(x^n, M)$ |
|:---------:|:--------------:|:------------------------------------:|:-------------:|:-----------------:|
| 1         | 2              | 420                                  | 6.6           | 426.6             |
| 5         | 6              | 310                                  | 19.9          | 329.9             |
| 10        | 11             | 285                                  | 36.5          | 321.5             |

En este ejemplo hipotético el grado 10 gana, pero en presencia de ruido real la penalización $L(M)$ invierte ese resultado. El criterio MDL localiza el equilibrio automáticamente.

## Complejidad estocástica y la distribución NML

### Motivación

La formulación de dos partes depende de cómo se codifiquen los parámetros, lo que introduce arbitrariedad. Rissanen (1986) propuso una versión más fundamentada: en lugar de separar modelo y datos, buscar la distribución sobre $x^n$ que sea óptima de forma universal.

### Distribución NML

La **distribución de máxima verosimilitud normalizada** (*Normalized Maximum Likelihood*, NML) se define como:

$$p^*(x^n) = \frac{p(x^n;\, \hat{\theta}(x^n))}{C_n}$$

donde el denominador es la constante de normalización:

$$C_n = \sum_{y^n} p(y^n;\, \hat{\theta}(y^n))$$

La suma recorre todas las secuencias posibles de longitud $n$. NML asigna a cada secuencia una probabilidad proporcional a su mejor verosimilitud posible bajo la clase de modelos.

### Complejidad estocástica

La **complejidad estocástica** de $x^n$ respecto de la clase $\mathcal{M}$ es:

$$\mathrm{SC}(x^n) = -\log_2 p^*(x^n) = -\log_2 p(x^n;\, \hat{\theta}) + \log_2 C_n$$

Para modelos regulares con $k$ parámetros, una expansión de Laplace muestra que:

$$\log_2 C_n \approx \frac{k}{2}\log_2 n + O(1)$$

de modo que:

$$\mathrm{SC}(x^n) \approx -\log_2 p(x^n;\, \hat{\theta}) + \frac{k}{2}\log_2 n + O(1)$$

Este resultado conecta MDL refinado con el criterio BIC.

## Conexión con el criterio BIC

El criterio de información bayesiana (*Bayesian Information Criterion*) es:

$$\mathrm{BIC} = -2\ln \hat{L} + k \ln n$$

donde $\hat{L} = p(x^n; \hat{\theta})$ es la máxima verosimilitud. Dividiendo entre $2\ln 2$ para convertir a bits:

$$\frac{\mathrm{BIC}}{2\ln 2} = -\log_2 p(x^n;\, \hat{\theta}) + \frac{k}{2}\log_2 n$$

Esta expresión es **idéntica** a la complejidad estocástica salvo el término $O(1)$. BIC es, por tanto, una aproximación asintótica de MDL refinado.

La diferencia conceptual es relevante: MDL es exactamente óptimo en el sentido minimax de Rissanen (minimiza el exceso de longitud en el peor caso); BIC es una aproximación asintótica que coincide con MDL cuando $n \to \infty$ pero puede diferir en muestras pequeñas. El criterio AIC ($-2\ln\hat{L} + 2k$) no tiene esta interpretación MDL: penaliza menos la complejidad y es preferible cuando el objetivo es la predicción, no la identificación del modelo verdadero.

## Conexión con la complejidad de Kolmogorov

La complejidad de Kolmogorov $K(x)$ es el límite teórico del MDL: la longitud del programa más corto que produce $x$ en una máquina universal de Turing. Formalmente,

$$K(x) \approx \mathrm{MDL}(x) + O(1)$$

donde la constante aditiva depende de la máquina de referencia. La relación es bidireccional: toda descripción computable de $x$ acota superiormente $K(x)$, y $K(x)$ acota inferiormente cualquier descripción computable.

La diferencia práctica es fundamental: $K(x)$ no es computable (es equivalente al problema de la parada), mientras que las implementaciones de MDL son algoritmos que terminan. MDL opera como una **aproximación computable de la complejidad de Kolmogorov** dentro de una clase de modelos fijada.

La tabla siguiente resume las relaciones entre los distintos criterios:

| Criterio              | Computable | Penaliza complejidad | Óptimo minimax | Interpretación probabilística |
|:----------------------|:----------:|:--------------------:|:--------------:|:-----------------------------:|
| $K(x)$ (Kolmogorov)   | No         | Sí (exacta)          | Sí (teórico)   | Prior universal de Solomonoff |
| MDL dos partes        | Sí         | Sí (aproximada)      | Parcial        | Código de dos partes          |
| NML / SC (Rissanen)   | Sí*        | Sí (exacta)          | Sí             | Máxima verosimilitud universal|
| BIC                   | Sí         | Sí (asintótica)      | Asintótico     | Aproximación de Laplace       |
| AIC                   | Sí         | Sí (fija)            | No             | Estimación del riesgo         |

(*NML puede ser intratable para clases de modelos grandes; $C_n$ requiere integración sobre todas las secuencias posibles.)

## Prior universal de Solomonoff

La distribución de Solomonoff asigna a cada cadena binaria $x$ una probabilidad proporcional a la suma de las probabilidades de todos los programas que la producen:

$$p_U(x) = \sum_{\substack{M :\, M \text{ produce } x}} 2^{-L(M)}$$

Este prior concentra la masa en las cadenas con descripciones cortas y realiza exactamente la navaja de Occam en un sentido matemático preciso.

MDL puede interpretarse como **inducción de Solomonoff con un prior computacionalmente realizable**: en lugar de sumar sobre todos los programas posibles (incluyendo los no computables), MDL restringe la clase de modelos a una familia paramétrica tratable. El precio es perder la universalidad; la ganancia es la computabilidad.

## Aplicaciones prácticas

**Selección de variables en regresión.** La penalización LASSO ($\ell_1$) tiene una interpretación MDL directa: imponer un prior de Laplace doble sobre los coeficientes equivale a penalizar la descripción de cada coeficiente no nulo. MDL proporciona así una justificación informacional para la regularización.

**Poda de árboles de decisión.** Un árbol más profundo ajusta mejor el conjunto de entrenamiento, pero requiere más bits para describir su estructura. MDL selecciona la profundidad donde el coste total —descripción del árbol más codificación de los errores residuales— es mínimo.

**Selección del número de clusters.** En $k$-means, MDL penaliza modelos con más centroides porque codificar $k$ centroides cuesta $O(k \log n)$ bits adicionales. El número óptimo de clusters equilibra la reducción del error de reconstrucción con el coste de descripción.

**Compresión universal.** Los compresores LZ (Lempel–Ziv) son implementaciones implícitas de MDL: construyen un diccionario de frases repetidas y codifican el texto como referencias a ese diccionario. Cada nueva frase añadida al diccionario tiene un coste ($L(M)$ aumenta) que se amortiza si aparece suficientes veces (reduciendo $L(x^n|M)$).

## Ejemplo numérico

Dos modelos compiten para explicar $n = 100$ observaciones. Usando la aproximación $L(M) \approx \frac{k}{2}\log_2 n$:

$$\log_2 100 \approx 6.644 \text{ bits}$$

| Modelo | Parámetros $k$ | $-\log_2 p(x^n;\hat{\theta})$ | $L(M) = \frac{k}{2}\log_2 n$ | Total |
|:------:|:--------------:|:-----------------------------:|:-----------------------------:|:-----:|
| A      | 2              | 150.0 bits                    | $1 \times 6.644 = 6.6$ bits  | **156.6 bits** |
| B      | 8              | 130.0 bits                    | $4 \times 6.644 = 26.6$ bits | **156.6 bits** |

El resultado es un **empate exacto**: el modelo B gana en verosimilitud exactamente lo que pierde en complejidad. En la práctica, ante un empate MDL elige el modelo más parsimonioso (modelo A), porque cualquier variación de los datos romperá el empate a favor del modelo más simple. Este comportamiento no aparece en MLE, que seleccionaría siempre el modelo B.

Si la log-verosimilitud del modelo B mejorara solo hasta $-135$ bits (en lugar de $-130$), el total sería $161.6 > 156.6$ y MDL seleccionaría el modelo A. La ganancia en ajuste no justificaría el coste en descripción.

## Ideas clave

1. MDL formaliza la navaja de Occam: el modelo óptimo minimiza la longitud total de descripción $L(M) + L(x^n \mid M)$.
2. La distribución NML es el código universal óptimo en el sentido minimax; su longitud esperada define la complejidad estocástica.
3. BIC es una aproximación asintótica de la complejidad estocástica, válida cuando $n \to \infty$.
4. La complejidad de Kolmogorov es el límite no computable del MDL; las implementaciones prácticas son aproximaciones computables dentro de clases paramétricas.
5. El prior de Solomonoff realiza MDL universal; restringirlo a una familia computable da lugar al MDL práctico.
6. MDL proporciona una justificación informacional para LASSO, la poda de árboles, la selección de clusters y los compresores LZ.

## Ejercicios

1. **(AIC vs BIC vs MDL)** Para $n = 50$ datos de una regresión lineal, compara los modelos $k=3$ y $k=7$ usando AIC, BIC y MDL-dos-partes cuando las log-verosimilitudes son $-80$ y $-65$ respectivamente. ¿Qué criterio selecciona cada uno? Discute por qué AIC y MDL pueden diferir para muestras pequeñas.

2. **(NML para Bernoulli)** Sea $\mathcal{M}$ la familia de distribuciones de Bernoulli $\mathrm{Bern}(\theta)$ con $\theta \in [0,1]$. Para una secuencia con $k$ éxitos en $n$ ensayos, el estimador MLE es $\hat{\theta} = k/n$. Demuestra que la constante de normalización NML es:
$$C_n = \sum_{k=0}^{n} \binom{n}{k} \left(\frac{k}{n}\right)^k \left(1 - \frac{k}{n}\right)^{n-k}$$
y verifica numéricamente para $n = 10$ que $\log_2 C_n \approx \tfrac{1}{2}\log_2 n + O(1)$.

3. **(¿Por qué MDL no sobreajusta?)** Argumenta formalmente por qué un modelo con $k$ parámetros libres, al añadir un parámetro adicional irrelevante (que no mejora la log-verosimilitud esperada en el modelo generador verdadero), aumenta el MDL en media. ¿Qué cantidad controla ese aumento? ¿Cómo se relaciona con la divergencia KL entre el modelo verdadero y el modelo sobreajustado?

4. **(Conexión con LZ)** El compresor LZ78 construye un diccionario de frases; sea $d(n)$ el número de frases distintas en la compresión de $x^n$. La longitud de la descripción del diccionario es $O(d(n) \log d(n))$ bits y la de los índices es $O(n)$ bits. Explica cómo este esquema puede interpretarse como MDL de dos partes e identifica qué término corresponde a $L(M)$ y cuál a $L(x^n \mid M)$. ¿Qué ocurre cuando $n \to \infty$ con fuentes ergódicas?

## Véase también

- [Complejidad de Kolmogorov](01-complejidad-de-kolmogorov.md)
- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)
- [Información en aprendizaje estadístico](05-informacion-en-aprendizaje.md)
- [Mapa de conexiones](08-mapa-de-conexiones.md)


<!-- nav-start -->

---
← [Geometría de la Información](12-geometria-de-la-informacion.md) · [14 - El cuello de botella de la información](14-cuello-de-botella-de-la-informacion.md) →

<!-- nav-end -->
## Referencias

- Rissanen, J. (1978). Modeling by shortest data description. *Automatica*, 14(5), 465–471.
- Rissanen, J. (1986). Stochastic complexity and modeling. *Annals of Statistics*, 14(3), 1080–1100.
- Grünwald, P. (2007). *The Minimum Description Length Principle*. MIT Press.
- Grünwald, P. y Vitányi, P. (2004). Shannon information and Kolmogorov complexity. *arXiv:cs/0410002*.
- Barron, A., Rissanen, J. y Yu, B. (1998). The minimum description length principle in coding and modeling. *IEEE Transactions on Information Theory*, 44(6), 2743–2760.
