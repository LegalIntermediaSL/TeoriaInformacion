# Teoría de la Información en Redes

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min

## Prerrequisitos

- [Canales discretos y capacidad](04-canales-discretos-y-capacidad.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)
- [Teorema de Shannon y capacidad de canal](08-teorema-de-shannon-capacidad.md)

## Objetivos de aprendizaje

1. Extender el modelo de canal punto a punto de Shannon a escenarios con múltiples usuarios.
2. Enunciar la región de capacidad del canal de acceso múltiple (MAC) y verificar su derivación intuitiva.
3. Describir el canal de difusión (broadcast) y la codificación en capas para canales degradados.
4. Explicar las estrategias decode-and-forward y compress-and-forward en el canal de relevo.
5. Enunciar el teorema de Slepian-Wolf sobre compresión distribuida sin pérdida.
6. Calcular la capacidad secreta del canal de escucha (wiretap) de Wyner.

## Intuición

El teorema de Shannon (1948) resuelve de forma elegante el problema punto a punto: un transmisor, un receptor, un canal ruidoso. Pero las redes modernas son mucho más complejas. En WiFi, decenas de dispositivos comparten el mismo espectro radioeléctrico. En una red 5G, una estación base atiende simultáneamente a cientos de terminales. En una red de sensores, múltiples nodos recogen datos correlacionados y los envían a un centro de fusión que los procesa juntos.

Cada uno de estos escenarios plantea preguntas que el modelo clásico no puede responder: ¿cuánto pueden transmitir simultáneamente dos usuarios que comparten un canal? ¿Puede un transmisor enviar contenidos distintos a receptores con calidades de canal diferentes? ¿Ayuda un nodo intermediario (relevo) a mejorar la capacidad? ¿Es posible comprimir datos correlacionados de forma distribuida sin compartir información entre los compresores?

La **teoría de la información en redes** (o teoría de la información multiusuario) aborda estas preguntas. A diferencia del caso punto a punto, muchos de estos problemas siguen abiertos décadas después de su formulación, lo que los convierte en algunos de los problemas más desafiantes de la teoría de la información.

## Canal de acceso múltiple (MAC)

### Configuración

En el **canal de acceso múltiple** (*multiple access channel*, MAC) hay $k$ transmisores y un único receptor. El receptor recibe la suma (o combinación) de todas las señales más ruido. Este modelo captura situaciones como el canal de retorno en una red celular: varios terminales envían simultáneamente hacia la estación base.

Formalmente, $k$ usuarios transmiten símbolos $X_1, X_2, \ldots, X_k$ de forma independiente, y el receptor observa $Y$ con distribución condicional $p(y \mid x_1, x_2, \ldots, x_k)$.

### Región de capacidad

Para el caso de dos usuarios, la región de capacidad del MAC es el conjunto de tasas $(R_1, R_2)$ simultáneamente alcanzables con probabilidad de error tendiendo a cero:

$$
R_1 \leq I(X_1; Y \mid X_2)
$$

$$
R_2 \leq I(X_2; Y \mid X_1)
$$

$$
R_1 + R_2 \leq I(X_1, X_2; Y)
$$

donde el máximo se toma sobre distribuciones de entrada independientes $p(x_1)\,p(x_2)$.

**Interpretación:** La primera desigualdad dice que el usuario 1 no puede transmitir más información de la que el receptor podría recuperar si conociera perfectamente $X_2$. Es decir, la información mutua condicionada al conocimiento del otro usuario. La cota sobre la suma $R_1 + R_2$ refleja la limitación total del canal.

Para $k$ usuarios, la región se generaliza a un sistema de $2^k - 1$ desigualdades: para cada subconjunto no vacío $S \subseteq \{1, \ldots, k\}$,

$$
\sum_{i \in S} R_i \leq I\!\left(X_S;\, Y \mid X_{S^c}\right)
$$

donde $X_S = (X_i)_{i \in S}$ y $S^c = \{1,\ldots,k\} \setminus S$.

> **Teorema (capacidad del MAC, Ahlswede 1971; Liao 1972).** La región de capacidad del canal de acceso múltiple con $k$ usuarios es la clausura convexa del conjunto de tasas $(R_1, \ldots, R_k) \geq 0$ que satisfacen, para todo $S \subseteq \{1,\ldots,k\}$,
>
> $$\sum_{i \in S} R_i \leq I(X_S; Y \mid X_{S^c})$$
>
> para alguna distribución de entrada $\prod_{i=1}^k p_i(x_i)$.

La región del MAC tiene forma de polítopo (en 2 usuarios, un pentágono), y sus vértices se alcanzan con decodificación sucesiva por cancelación de interferencia (SIC): el receptor decodifica primero a un usuario, elimina su contribución de la señal recibida, y luego decodifica al siguiente.

### MAC gaussiano con dos usuarios

Para entradas con restricción de potencia $P_i$ y canal AWGN (ruido aditivo gaussiano blanco con varianza $N$):

$$
R_1 + R_2 \leq \frac{1}{2}\log_2\!\left(1 + \frac{P_1 + P_2}{N}\right)
$$

$$
R_1 \leq \frac{1}{2}\log_2\!\left(1 + \frac{P_1}{N}\right), \quad R_2 \leq \frac{1}{2}\log_2\!\left(1 + \frac{P_2}{N}\right)
$$

## Canal de difusión (Broadcast)

### Configuración

El **canal de difusión** (*broadcast channel*, BC) invierte la estructura del MAC: un transmisor único envía a $k$ receptores con calidades de canal distintas. Es el modelo del enlace de bajada en una red celular o de una transmisión de televisión digital.

El transmisor envía $X$, y el receptor $i$ observa $Y_i$ con distribución condicional $p(y_i \mid x)$. Se busca transmitir mensajes independientes $M_1, \ldots, M_k$ a cada receptor.

### Canal degradado y codificación en capas

Un canal de difusión con dos receptores es **degradado** (en el sentido de Bergmans) si $X \to Y_1 \to Y_2$ forma una cadena de Markov, es decir, $Y_2$ es una versión más degradada de $Y_1$. En este caso, el receptor 1 tiene mejor calidad de canal.

Cover (1972) propuso la **codificación en capas** (superposition coding): el transmisor superpone un mensaje de alta tasa para el receptor fuerte ($Y_1$) sobre un mensaje de baja tasa para el receptor débil ($Y_2$). Formalmente, $X = f(U, V)$ donde $U$ contiene el mensaje para $Y_2$ y $V$ el mensaje adicional para $Y_1$.

La región de capacidad del canal de difusión degradado con dos receptores es:

$$
R_1 \leq I(V; Y_1 \mid U), \quad R_2 \leq I(U; Y_2)
$$

para alguna cadena de Markov $U \to V \to X \to (Y_1, Y_2)$.

**Contraste con el MAC:** mientras que la región de capacidad del MAC está completamente caracterizada, la del canal de difusión general (no degradado) sigue siendo un **problema abierto**. Solo se conocen cotas interiores (región de Marton) y exteriores, pero salvo para casos especiales (degradado, menos ruidoso, sin memoria con entradas determinísticas) no coinciden en general.

## Canal de relevo

### Configuración

En el **canal de relevo** (*relay channel*) hay una fuente, un nodo relevo y un destino. La fuente quiere comunicarse con el destino, y el relevo puede escuchar a la fuente y reenviar información al destino. El modelo fue introducido por van der Meulen (1971) y analizado por Cover y El Gamal (1979).

### Estrategias de codificación

**Decode-and-forward (DF):** El relevo decodifica el mensaje de la fuente completamente y lo reenvía al destino. La cota de tasa alcanzable es:

$$
R_\text{DF} = \max_{p(x_1, x_2)} \min\!\left\lbraceI(X_1; Y_2 \mid X_2),\; I(X_1, X_2; Y_3)\right\rbrace
$$

donde $X_1$ es la entrada de la fuente, $X_2$ la del relevo, $Y_2$ la salida en el relevo y $Y_3$ la salida en el destino. El mínimo refleja el cuello de botella: o la fuente no puede comunicar al relevo (primer término) o el par fuente-relevo no puede llegar al destino (segundo término).

**Compress-and-forward (CF):** El relevo no decodifica; comprime su observación $Y_2$ y la envía al destino, que combina la señal recibida directamente de la fuente con la información comprimida del relevo. Esta estrategia puede superar a DF cuando el canal fuente-relevo es peor que el fuente-destino.

> **Problema abierto:** La capacidad exacta del canal de relevo en el caso general es desconocida. Las cotas DF y CF no coinciden en general, y no se sabe cuál estrategia es óptima ni si existe alguna que las supere. Este es uno de los problemas fundamentales abiertos en teoría de la información en redes.

## Compresión distribuida: Slepian-Wolf

### El problema

Dos fuentes $X$ e $Y$ están estadísticamente correlacionadas (distribución conjunta $p(x,y)$) y son observadas por dos codificadores separados que no pueden comunicarse entre sí. Cada codificador comprime su fuente de forma independiente. Un único decodificador recibe ambas versiones comprimidas y debe reconstruir $(X, Y)$ sin error (en el sentido asintótico).

Intuitivamente parece que cada codificador debe trabajar al menos a la tasa de entropía de su fuente propia: $R_1 \geq H(X)$, $R_2 \geq H(Y)$. Slepian y Wolf (1973) demostraron que esto es innecesariamente conservador.

### Teorema de Slepian-Wolf

> **Teorema (Slepian-Wolf, 1973).** La región de tasas $(R_1, R_2)$ alcanzables para la compresión distribuida sin pérdida de $(X, Y)$ es:
>
> $$R_1 \geq H(X \mid Y)$$
> $$R_2 \geq H(Y \mid X)$$
> $$R_1 + R_2 \geq H(X, Y)$$

La tasa suma mínima $H(X,Y)$ es lo que se necesitaría si los dos codificadores pudieran cooperar. ¡La distribución permite alcanzar esta tasa incluso sin cooperación!

**Intuición de la prueba:** aunque los codificadores no se comunican, el decodificador los puede usar conjuntamente. El codificador 1 puede usar un código de tipo binning (partición aleatoria del espacio de secuencias) a tasa $R_1 \approx H(X \mid Y)$, porque el decodificador, al conocer $Y$, puede resolver la ambigüedad entre las pocas secuencias $X$ compatibles con $Y$ que caen en el mismo bin.

**Dualidad fuente-canal:** existe una dualidad profunda entre el teorema de Slepian-Wolf y la región de capacidad del MAC. La región $\{R_1 \geq H(X|Y), R_2 \geq H(Y|X), R_1+R_2 \geq H(X,Y)\}$ es el "espejo" de la región de capacidad del MAC, con entropías en lugar de informaciones mutuas.

## Canal de escucha: el wiretap de Wyner

### Configuración y seguridad informacional

En el **canal de escucha** (*wiretap channel*) de Wyner (1975), el transmisor Alice envía un mensaje secreto a Bob, pero existe un escucha pasivo Eve que intercepta una versión degradada del canal. El objetivo es comunicar información a Bob de forma que Eve no pueda obtener ninguna información en el sentido de la teoría de la información (no solo computacionalmente).

La seguridad se formaliza como $I(M; Z^n) \to 0$ cuando $n \to \infty$, donde $M$ es el mensaje y $Z^n$ es la secuencia observada por Eve. Esta es la noción de **secreto perfecto** o seguridad informacional.

### Capacidad secreta

> **Teorema (Wyner, 1975).** Para el canal de escucha degradado $X \to Y \to Z$ (Bob recibe $Y$, Eve recibe $Z$), la capacidad secreta es:
>
> $$C_s = \max_{p(x)}\, [I(X; Y) - I(X; Z)]^+$$
>
> donde $[a]^+ = \max(a, 0)$.

Si el canal de Alice a Bob es mejor que el de Alice a Eve (en el sentido de degradación), existe una capacidad positiva de comunicación secreta sin ninguna clave compartida previamente. Si Eve tiene un canal mejor que Bob, $C_s = 0$.

La codificación que logra $C_s$ usa **binning estocástico**: Alice transmite a una tasa $R + R_e$, donde $R$ es la tasa de información útil y $R_e \approx I(X;Z)$ es la tasa de "ruido" añadida intencionalmente para confundir a Eve. Bob puede decodificar a tasa $R + R_e \leq I(X;Y)$, mientras que Eve solo ve $I(X;Z)$ bits, siendo los restantes $R$ bits inaccesibles para ella.

**Conexión con criptografía:** el cifrado de Vernam (one-time pad) es el caso extremo de seguridad informacional perfecta con una clave compartida. El resultado de Wyner muestra que en ciertos canales físicos se puede obtener seguridad sin clave, explotando la ventaja de canal de Bob sobre Eve. Esto es la base de la **criptografía de capa física** (*physical layer security*), área de investigación activa en 5G y comunicaciones cuánticas.

## Tabla resumen

| Modelo | Configuración | Resultado principal | Estado |
|---|---|---|---|
| MAC ($k$ usuarios) | $k$ TX, 1 RX | Región de $2^k-1$ desigualdades: $\sum_{S} R_i \leq I(X_S;Y\|X_{S^c})$ | Resuelto (Ahlswede, Liao 1971-72) |
| Broadcast (2 RX, degradado) | 1 TX, $k$ RX con calidades distintas | Codificación en capas; región de Cover | Resuelto solo para caso degradado |
| Broadcast general | 1 TX, $k$ RX | Solo cotas (región de Marton interior) | **Abierto** |
| Canal de relevo | Fuente → Relevo → Destino | Cotas DF y CF; ninguna domina en general | **Abierto** (capacidad exacta desconocida) |
| Slepian-Wolf | 2 fuentes correlacionadas, codif. separada | $R_1 \geq H(X\|Y)$, $R_2 \geq H(Y\|X)$, $R_1+R_2 \geq H(X,Y)$ | Resuelto (Slepian-Wolf 1973) |
| Wyner wiretap (degradado) | TX → Bob (bueno), TX → Eve (degradado) | $C_s = \max[I(X;Y)-I(X;Z)]^+$ | Resuelto para caso degradado |
| Wyner wiretap general | Canal arbitrario para Bob y Eve | Generalización de Csiszár-Körner | Resuelto (Csiszár-Körner 1978) |

## Ideas clave

1. La **región de capacidad** del MAC es un polítopo alcanzable con decodificación sucesiva (SIC); su estructura de $2^k-1$ desigualdades refleja que cualquier subconjunto de usuarios compite por la misma salida.
2. El **broadcast** es fundamentalmente más difícil que el MAC: incluso con dos receptores, la región de capacidad general sigue sin caracterizarse exactamente.
3. El **canal de relevo** ilustra que incluso problemas de tres nodos pueden ser extraordinariamente difíciles; la capacidad exacta sigue siendo desconocida.
4. **Slepian-Wolf** es contraintuitivo: codificadores sin comunicación pueden alcanzar la misma tasa suma que si cooperaran, gracias a la correlación y al decodificador conjunto.
5. La **capacidad secreta** de Wyner muestra que la seguridad informacional perfecta es posible sin clave compartida, explotando la física del canal; conecta teoría de la información con criptografía.
6. La mayoría de los problemas de redes multiusuario son **NP-difíciles de caracterizar** o directamente abiertos; la teoría de la información en redes es un campo activo con grandes preguntas sin respuesta.

## Ejercicios

1. **(MAC gaussiano, potencias asimétricas.)** Considera un MAC gaussiano con dos usuarios con potencias $P_1 = 6$ y $P_2 = 2$, y varianza de ruido $N = 1$. (a) Calcula la tasa suma máxima $R_1 + R_2$. (b) Calcula las tasas individuales máximas $R_1^{\max}$ y $R_2^{\max}$ (asumiendo que el otro usuario ocupa toda su potencia). (c) ¿Es el punto $(R_1^{\max}, R_2^{\max})$ alcanzable simultáneamente? Justifica usando la región del MAC.

2. **(Slepian-Wolf, fuentes binarias correlacionadas.)** Sean $X$ e $Y$ variables binarias tales que $Y = X \oplus E$, donde $E \sim \text{Bernoulli}(0.1)$ independiente de $X \sim \text{Bernoulli}(0.5)$. (a) Calcula $H(X)$, $H(Y)$, $H(X,Y)$, $H(X|Y)$ e $H(Y|X)$. (b) Representa la región de Slepian-Wolf en el plano $(R_1, R_2)$. (c) ¿Cuántos bits por símbolo ahorra la codificación conjunta en la tasa suma respecto a comprimir $X$ e $Y$ de forma completamente independiente?

3. **(Broadcast, aspecto conceptual.)** Un transmisor desea enviar datos de video en alta definición a un receptor cercano y simultáneamente datos de audio a un receptor lejano, usando el mismo canal. El canal al receptor cercano tiene capacidad $C_1 = 5$ Mbps y el canal al receptor lejano tiene capacidad $C_2 = 1$ Mbps (el canal es degradado: el lejano recibe una versión más ruidosa que el cercano). (a) ¿A qué tasa máxima puede recibir datos el receptor lejano si el cercano necesita exactamente $R_1 = 3$ Mbps? (b) ¿Por qué la codificación en capas es más eficiente que la división de tiempo entre ambos receptores? (c) Explica intuitivamente por qué el receptor cercano puede decodificar el mensaje del lejano y luego "cancelarlo" para extraer su propio mensaje.

4. **(Wiretap, seguridad física.)** En un canal de escucha degradado, Alice transmite a Bob con $I(X;Y) = 3$ bits/uso y a Eve con $I(X;Z) = 1$ bit/uso. (a) ¿Cuál es la capacidad secreta $C_s$? (b) Si Alice desea transmitir a $R = 1.5$ bits/uso de forma segura, ¿a qué tasa total $R + R_e$ debe transmitir y cuántos bits por uso se "sacrifican" para confundir a Eve? (c) Si mejoramos el canal de Eve hasta $I(X;Z) = 3.5$ bits/uso, ¿qué ocurre con $C_s$? ¿Qué implicación tiene esto para la seguridad de capa física?

## Véase también

- [Canales discretos y capacidad](04-canales-discretos-y-capacidad.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)
- [Teorema de Shannon y capacidad de canal](08-teorema-de-shannon-capacidad.md)
- [Teoría tasa-distorsión](09-teoria-tasa-distorsion.md)

## Referencias

- Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory* (2ª ed.). Wiley-Interscience. Caps. 14-17.
- El Gamal, A. & Kim, Y.-H. (2011). *Network Information Theory*. Cambridge University Press.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379-423.
- Slepian, D. & Wolf, J. K. (1973). Noiseless coding of correlated information sources. *IEEE Transactions on Information Theory*, 19(4), 471-480.
- Wyner, A. D. (1975). The wire-tap channel. *Bell System Technical Journal*, 54(8), 1355-1387.
- Cover, T. M. & El Gamal, A. (1979). Capacity theorems for the relay channel. *IEEE Transactions on Information Theory*, 25(5), 572-584.
- Csiszár, I. & Körner, J. (1978). Broadcast channels with confidential messages. *IEEE Transactions on Information Theory*, 24(3), 339-348.
