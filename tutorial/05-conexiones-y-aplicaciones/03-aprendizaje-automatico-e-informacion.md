# 03 - Aprendizaje automático e información

El aprendizaje automático puede verse como un proceso de extracción de
regularidades a partir de datos. Esa descripción lo conecta de forma natural con
la teoría de la información, la compresión y la complejidad.

Un modelo útil no memoriza sin más. Aprende una representación que permite
generalizar.

## Datos como señales

Un conjunto de datos contiene patrones, ruido y sesgos. La teoría de la
información ayuda a preguntar:

- qué variables reducen incertidumbre;
- qué representaciones conservan información útil;
- qué ruido puede ignorarse;
- qué regularidades permiten comprimir.

Estas preguntas no sustituyen la estadística ni la optimización, pero ofrecen un
lenguaje común.

## Entropía e incertidumbre

En clasificación, la salida de un modelo suele ser una distribución de
probabilidad sobre clases.

Si el modelo asigna probabilidades parecidas a muchas clases, su incertidumbre
es alta. Si concentra casi toda la probabilidad en una clase, su entropía es
baja.

Esto no garantiza que el modelo esté en lo correcto. Un modelo puede estar muy
seguro y equivocarse.

## Entropía cruzada como pérdida

La entropía cruzada se usa a menudo como función de pérdida en clasificación.

Si la clase correcta es `y` y el modelo le asigna probabilidad `q(y)`, la pérdida
asociada es:

```text
-log q(y)
```

Asignar baja probabilidad a la respuesta correcta produce una penalización alta.

## Información mutua y variables

La información mutua puede usarse para medir cuánto dice una variable sobre
otra. Por ejemplo:

```text
I(X; Y)
```

puede indicar cuánto ayuda una característica `X` a predecir una etiqueta `Y`.

Pero hay que tener cuidado: una variable puede tener información mutua alta con
la etiqueta por razones espurias o por sesgos del conjunto de datos.

## Compresión y generalización

Hay una intuición profunda que conecta aprender con comprimir: si un modelo
encuentra una descripción breve de los datos que además predice bien nuevos
casos, ha capturado estructura.

Memorizar todos los datos no es lo mismo que aprender. Una descripción demasiado
ajustada puede fallar fuera del conjunto de entrenamiento.

Esta tensión aparece en ideas como:

- regularización;
- principio de longitud mínima de descripción;
- sesgo inductivo;
- selección de modelos.

## Complejidad computacional

Entrenar modelos puede ser costoso. Algunas tareas de aprendizaje son difíciles
por razones computacionales, no solo por falta de datos.

Además, la búsqueda de buenos parámetros puede involucrar espacios enormes. Los
algoritmos prácticos usan aproximaciones, heurísticas y estructura del problema.

La pregunta no es solo qué modelo existe, sino si podemos encontrarlo con los
recursos disponibles.

## Información y privacidad

Si un modelo retiene demasiada información específica sobre sus datos de
entrenamiento, puede filtrar detalles sensibles.

Esto conecta aprendizaje con:

- privacidad diferencial;
- memorization;
- ataques de inferencia;
- anonimización;
- compresión de representaciones.

La información útil y la información sensible no siempre son fáciles de separar.

## Idea para recordar

Aprender es transformar datos en representaciones útiles. La teoría de la
información ayuda a medir incertidumbre, dependencia y compresión; la complejidad
ayuda a entender los límites de encontrar buenos modelos.

## Ejercicios

1. Explica por qué baja entropía en la salida de un modelo no garantiza acierto.
2. ¿Qué penaliza la pérdida de entropía cruzada?
3. Da un ejemplo de variable con información mutua alta pero potencialmente
   engañosa.
4. Relaciona compresión y generalización con tus propias palabras.
