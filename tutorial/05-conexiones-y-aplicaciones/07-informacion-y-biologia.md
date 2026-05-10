# Información y biología

## Intuición

El ADN es literalmente un código: un alfabeto de 4 letras (A, C, G, T) codifica instrucciones que los ribosomas "leen" para sintetizar proteínas. Esta analogía no es solo metafórica —los conceptos de entropía, redundancia, corrección de errores e información mutua tienen interpretaciones biológicas precisas y medibles. La teoría de la información ilumina preguntas sobre la evolución (¿cuánta información porta el genoma?), la regulación génica (¿cómo lee un factor de transcripción su secuencia diana?) y la evolución molecular (¿por qué el código genético es redundante?).

## El genoma como código

El ADN humano tiene aproximadamente $3 \times 10^9$ pares de bases. Con un alfabeto de 4 letras ($|\mathcal{A}| = 4$), la entropía máxima sería:

$$H_{\max} = \log_2 4 = 2 \text{ bits/base}$$

El genoma completo contendría hasta $6 \times 10^9$ bits de información si fuera completamente aleatorio. Pero el ADN no es aleatorio:

- Las bases no son equiprobables en todos los organismos (composición GC varía).
- Existen correlaciones de largo alcance (regiones codificantes, repeticiones, etc.).
- El contenido informativo real es mucho menor: la entropía estimada por compresión es $\approx 1.7$–1.9 bits/base en el genoma humano.

## El código genético y su redundancia

El **código genético** mapea tripletes de bases (codones) a aminoácidos:

- $4^3 = 64$ codones posibles.
- 20 aminoácidos estándar + 3 codones de parada.
- La asignación es **degenerada** (redundante): varios codones distintos codifican el mismo aminoácido.

**Entropía del código:** si los 64 codones fuesen equiprobables y los 21 "símbolos de salida" (20 aminoácidos + parada) equiprobables:

$$H(\text{codón}) = \log_2 64 = 6 \text{ bits}$$
$$H(\text{aminoácido}) = \log_2 21 \approx 4.39 \text{ bits}$$

La redundancia del código es $\approx 1.6$ bits/codón. Esta redundancia no es accidental: el código está estructurado para que mutaciones de un solo nucleótido en la tercera posición del codón (posición "wobble") frecuentemente no cambien el aminoácido —una forma de corrección de errores evolutiva.

## Información de Fisher en la evolución

La **información de Fisher** mide cuánta información porta una observación sobre un parámetro:

$$\mathcal{I}(\theta) = \mathbb{E}\left[\left(\frac{\partial}{\partial \theta} \log P(X;\theta)\right)^2\right]$$

En la teoría cuantitativa de la evolución, $\theta$ puede ser la frecuencia alélica de un gen en la población. La **Ecuación Fundamental de Fisher** establece que la tasa de cambio de la aptitud promedio es igual a la varianza aditiva en aptitud (proporcional a la información de Fisher):

$$\frac{d\bar{w}}{dt} = V_A(w)$$

donde $\bar{w}$ es la aptitud media y $V_A$ la varianza genética aditiva. Esto conecta velocidad de evolución con información en la población.

## Factores de transcripción: logos de secuencia

Los **factores de transcripción** (TF) se unen a secuencias específicas de ADN para regular la expresión génica. Un TF puede unirse a una región de $L$ bases con una "preferencia" descrita por una distribución $P(b | i)$ (probabilidad de la base $b$ en la posición $i$).

**Logo de secuencia (Schneider & Stephens, 1990):**

La información en la posición $i$ es:

$$R_i = \log_2 4 - H(P(\cdot | i)) = 2 - H_i$$

donde $H_i$ es la entropía de la distribución de bases en la posición $i$. El logo de secuencia visualiza $R_i$ con alturas proporcionales al contenido informativo.

**Contenido informativo total del sitio de unión:**

$$R_{\text{total}} = \sum_{i=1}^L R_i$$

Típicamente, los sitios de unión de TF tienen $R_{\text{total}} \approx \log_2 N_S$, donde $N_S$ es el número de sitios en el genoma donde el TF puede unirse con alta afinidad. El valor refleja la "especificidad" del TF.

## Canales con ruido en biología

La transmisión de información en sistemas biológicos puede modelarse como canales ruidosos:

### Canal de traducción

El canal de transcripción/traducción (ADN → ARNm → proteína) tiene ruido por:

- Tasas de error de la ARN polimerasa: $\approx 10^{-5}$ por base.
- Tasas de error del ribosoma: $\approx 10^{-4}$ por codón.

La **capacidad** de este canal en términos de tasa de error $\epsilon$ es:

$$C \approx 1 - H_b(\epsilon) \approx 1 + \epsilon \log_2 \epsilon \quad \text{(canal binario simétrico)}$$

Para $\epsilon = 10^{-5}$, $C \approx 0.9998$ bits/base: el canal biológico es casi perfecto.

### Señalización celular

Las vías de señalización (receptor → proteína G → mensajero secundario → respuesta) tienen capacidad limitada. Cada etapa introduce ruido y saturación. Se puede modelar como un canal en cascada donde la información mutua $I(\text{señal}; \text{respuesta})$ mide la capacidad de discriminar estados ambientales.

## Entropía en la evolución molecular

**Distancia evolutiva:** la divergencia KL entre la distribución de aminoácidos de dos proteínas ortólogas mide la distancia evolutiva:

$$D_{KL}(P_1 \| P_2) = \sum_a P_1(a) \log \frac{P_1(a)}{P_2(a)}$$

En sustituciones neutrales, los aminoácidos se fijan según la composición de equilibrio. En regiones funcionales, la selección purificadora mantiene baja la divergencia.

**Información mutua en el alineamiento:** para detectar co-evolución entre posiciones de una proteína (pares de residuos que coevolucionan por restricción de estructura), se calcula:

$$I(X_i; X_j) = H(X_i) + H(X_j) - H(X_i, X_j)$$

donde $X_i$ es el aminoácido en la posición $i$ a través de múltiples secuencias homólogas. Pares con alta $I$ suelen estar en contacto físico en la estructura 3D (base del método DCA, *Direct Coupling Analysis*).

## El principio de codificación eficiente en neurociencia

La hipótesis de **codificación eficiente** (Barlow, 1961) propone que el sistema visual (y otros sistemas sensoriales) están organizados para maximizar la información transmitida sobre el entorno mientras minimizan los recursos (spikes neuronales).

Matemáticamente, las neuronas implementan aproximadamente una **independización**: la distribución de respuestas maximiza $I(\text{estímulo}; \text{respuesta})$ bajo restricciones de energía. El análisis de componentes independientes (ICA) aplicado a imágenes naturales reproduce los campos receptivos de las células simples del cortex visual.

## Ideas clave

1. El ADN es un código con entropía $\approx 1.7$–1.9 bits/base, menor que la máxima por correlaciones.
2. La redundancia del código genético es una adaptación evolutiva para tolerar mutaciones puntuales.
3. Los logos de secuencia miden la especificidad de los sitios de unión proteína-ADN en bits.
4. Las vías de señalización tienen capacidad de canal finita; la información mutua cuantifica discriminación.
5. La co-evolución de residuos proteicos es detectable por información mutua y permite predecir contactos 3D.

## Ejercicios

1. El genoma de *E. coli* tiene $4.6 \times 10^6$ pares de bases con composición GC del 51%. Calcula la entropía de la distribución de bases asumiendo independencia. ¿Cuánto se desvía de 2 bits/base?

2. El codón UUU codifica fenilalanina y UUC también. ¿Cuánta información (en bits) se pierde en la tercera posición del codón para distinguir fenilalanina de otros aminoácidos?

3. Si un factor de transcripción tiene $R_{\text{total}} = 12$ bits, ¿cuántos sitios de unión esperamos en el genoma humano (3×10⁹ bases)?

4. Dos proteínas homólogas tienen la misma frecuencia de aminoácidos en regiones no funcionales. ¿Qué indica una alta $D_{KL}$ en un dominio específico?

## Referencias

- Schneider, T.D. y Stephens, R.M. (1990). Sequence logos: a new way to display consensus sequences. *Nucleic Acids Research*, 18(20), 6097–6100.
- Barlow, H.B. (1961). Possible principles underlying the transformation of sensory messages. En Rosenblith (ed.), *Sensory Communication*, 217–234. MIT Press.
- Tkačik, G. y Bialek, W. (2016). Information processing in living systems. *Annual Review of Condensed Matter Physics*, 7, 89–117.
- Morcos, F. et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. *PNAS*, 108(49), E1293–E1301.
