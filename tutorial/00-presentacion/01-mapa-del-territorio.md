# 01 - Mapa del territorio: información, cálculo y dificultad

La teoría de la información, la computabilidad y la complejidad computacional
pueden estudiarse como tres respuestas complementarias a una misma pregunta:
¿qué significa procesar información?

La teoría de la información mide incertidumbre, transmisión, compresión y
redundancia. La computabilidad pregunta qué puede ser calculado por un
procedimiento mecánico. La complejidad computacional estudia cuántos recursos
son necesarios para resolver un problema cuando ese problema sí es computable.

## Tres preguntas centrales

El tutorial puede leerse como una ruta guiada por tres preguntas:

1. ¿Cuánta información hay en una fuente, un mensaje o una observación?
2. ¿Existe un algoritmo que resuelva un problema dado?
3. Si existe, ¿cuánto tiempo, memoria u otros recursos necesita?

Estas preguntas no son independientes. Un mensaje puede ser informativo pero
difícil de comprimir. Un problema puede estar perfectamente definido pero no ser
decidible. Un problema puede ser decidible y, aun así, requerir tantos recursos
que resulte impracticable.

## Información

En teoría de la información, la noción central es la incertidumbre. Un mensaje
aporta información cuando reduce el conjunto de posibilidades que consideramos
plausibles.

Si una fuente siempre produce el mismo símbolo, observarla no sorprende. Si una
fuente puede producir muchos símbolos con probabilidades similares, cada
observación puede decirnos mucho más. La entropía formaliza esta intuición.

La teoría de la información no pregunta inicialmente por el significado semántico
de un mensaje, sino por su estructura probabilística: qué tan impredecible es,
cuánto puede comprimirse y qué tan bien puede transmitirse por un canal con
ruido.

## Computabilidad

La computabilidad estudia los límites absolutos del cálculo. Su pregunta no es
si un algoritmo es rápido o lento, sino si existe algún algoritmo que siempre
produzca la respuesta correcta en tiempo finito.

El resultado clásico es que hay problemas bien definidos que no pueden resolverse
por ningún algoritmo general. El ejemplo más famoso es el problema de la parada:
dado un programa y una entrada, determinar si el programa terminará o se quedará
ejecutándose para siempre.

Este tipo de resultado muestra que el límite de la computación no es solo
tecnológico. No depende de tener mejores procesadores, más memoria o más tiempo:
hay barreras formales.

## Complejidad

La complejidad computacional empieza donde la computabilidad no termina. Supone
que un problema sí puede resolverse y pregunta por el coste de resolverlo.

Dos algoritmos pueden ser correctos, pero tener comportamientos radicalmente
distintos. Uno puede crecer de forma lineal con el tamaño de la entrada y otro de
forma exponencial. Para entradas pequeñas ambos pueden funcionar; para entradas
grandes, solo el primero será viable.

La distinción entre problemas tratables e intratables es una de las ideas
centrales de la complejidad. Las clases P, NP y los problemas NP-completos forman
parte de ese mapa.

## Por qué estudiarlas juntas

Estas áreas comparten una preocupación profunda: entender los límites del
procesamiento de información.

- La teoría de la información pregunta por los límites de codificación,
  transmisión y compresión.
- La computabilidad pregunta por los límites de lo calculable.
- La complejidad pregunta por los límites de lo eficientemente calculable.

Juntas permiten distinguir entre lo que se puede describir, lo que se puede
calcular y lo que se puede calcular de manera práctica.

## Ruta recomendada

Una lectura natural del tutorial es:

1. Repasar los fundamentos matemáticos: conjuntos, probabilidad, logaritmos y
   crecimiento asintótico.
2. Estudiar entropía, información mutua, compresión y canales.
3. Introducir modelos de computación y problemas indecidibles.
4. Analizar recursos computacionales y clases de complejidad.
5. Explorar conexiones: información algorítmica, aleatoriedad, criptografía,
   aprendizaje automático e información cuántica.

## Idea para recordar

La información no solo se almacena o se transmite: también se transforma,
comprime, verifica, calcula y limita. Este tutorial trata de construir el
lenguaje formal necesario para hablar de todo ello con precisión.

## Preguntas de reflexión

1. ¿Puede un mensaje ser muy largo y contener poca información?
2. ¿Qué diferencia hay entre un problema difícil y un problema imposible de
   resolver algorítmicamente?
3. ¿Por qué un algoritmo correcto puede no ser útil en la práctica?
4. ¿Qué relación intuitiva hay entre compresión e identificación de patrones?
