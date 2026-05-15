# Información y Termodinámica

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Entropía e incertidumbre](../02-teoria-informacion/01-entropia-incertidumbre.md)

## Objetivos de aprendizaje

1. Demostrar que la entropía de Shannon y la de Boltzmann son la misma cantidad.
2. Explicar el exorcismo del demonio de Maxwell con el principio de Landauer.
3. Calcular el coste energético mínimo de borrar 1 bit a temperatura T.


## Intuición

La entropía de Shannon y la entropía de Boltzmann no son una mera analogía
de nombres: son la misma cantidad. El demonio de Maxwell —un ser imaginario
que viola el segundo principio de la termodinámica— fue exorcizado definitivamente
con un argumento de teoría de la información. La conexión entre información, trabajo
y calor es profunda y lleva a límites físicos fundamentales sobre el coste energético
de la computación.

## Entropía de Boltzmann y entropía de Shannon

En termodinámica estadística, la entropía de un sistema con $\Omega$ microestados
igualmente probables es:

$$S = k_B \ln \Omega$$

donde $k_B = 1.38 \times 10^{-23}$ J/K es la constante de Boltzmann.

Si el sistema está en el microestado $i$ con probabilidad $p_i$, la **entropía de
Gibbs** generaliza esto:

$$S = -k_B \sum_i p_i \ln p_i$$

Comparando con la entropía de Shannon $H = -\sum_i p_i \log_2 p_i$:

$$S = k_B \ln 2 \cdot H$$

La constante $k_B \ln 2 \approx 9.57 \times 10^{-24}$ J/K convierte bits en unidades
termodinámicas. **Un bit de entropía de información corresponde a $k_B \ln 2$ J/K de
entropía física.** Boltzmann (1877) y Shannon (1948) describían la misma cantidad desde
perspectivas distintas.

## El demonio de Maxwell

![Diagrama del demonio de Maxwell: un ser inteligente abre una trampilla entre dos compartimentos de gas. Izquierda — partículas rápidas; derecha — partículas lentas. Una flecha lateral muestra el coste de Landauer: borrar el bit de memoria del demonio cuesta k_B·T·ln2 julios, preservando el segundo principio de la termodinámica.](../imagenes/maxwell-demon.svg)

En 1867, James Clerk Maxwell propuso un experimento mental: un ser diminuto (luego
llamado "demonio de Maxwell") vigila las moléculas de un gas dividido en dos
compartimentos por una pared con una compuerta. El demonio abre y cierra la compuerta
selectivamente, permitiendo el paso solo de moléculas rápidas de izquierda a derecha
y moléculas lentas de derecha a izquierda.

El resultado: el compartimento derecho se calienta y el izquierdo se enfría, sin
realizar trabajo externo aparente. Esto parecería violar el segundo principio de la
termodinámica (la entropía total debe aumentar o mantenerse).

**El exorcismo de Szilard (1929):** Szilard identificó que el demonio debe **medir**
la velocidad de cada molécula para decidir si abrir la compuerta. Esta medición
adquiere 1 bit de información por molécula. La información almacenada en la memoria
del demonio tiene un coste entrópico.

**El argumento de Landauer (1961):** la medición en sí no tiene coste energético
mínimo obligatorio. El coste viene al **borrar** la información al final de un ciclo
completo (para que el demonio pueda operar indefinidamente). Borrar 1 bit de
información requiere disipar al menos:

$$W_{\text{mín}} = k_B T \ln 2$$

de energía como calor al entorno a temperatura $T$. Esto restaura exactamente el
aumento de entropía que el demonio parecía suprimir.

## El principio de Landauer

El **principio de Landauer** (1961, demostrado rigurosamente por Bennett 1982) afirma:

> Borrar 1 bit de información en un entorno a temperatura $T$ requiere disipar al
> menos $k_B T \ln 2 \approx 2.85 \times 10^{-21}$ J a temperatura ambiente (T = 300 K).

Este es el **límite de Landauer** para la eficiencia energética de la computación.
A 300 K:

$$E_{\text{mín}} = k_B T \ln 2 \approx 2.85 \times 10^{-21} \text{ J} \approx 0.017 \text{ eV}$$

Los transistores modernos disipan aproximadamente $10^4$ veces más que este límite
por operación, lo que indica que hay margen de mejora de varios órdenes de magnitud.

**Operaciones lógicas irreversibles:** las puertas lógicas irreversibles (AND, OR, NOT
con pérdida de información) son físicamente costosas. Una puerta AND recibe 2 bits y
produce 1, descartando 1 bit → debe disipar al menos $k_B T \ln 2$.

**Computación reversible:** Fredkin y Toffoli (1982) demostraron que toda computación
puede realizarse con puertas **reversibles** (biyecciones entre entradas y salidas),
que en principio no tienen coste de Landauer. La puerta de Toffoli $(a,b,c) \to (a,b,c \oplus ab)$
es universal para la computación reversible.

## Segundo principio y aumento de entropía

El **segundo principio de la termodinámica** en su formulación moderna de información:

$$\Delta S_{\text{total}} = \Delta S_{\text{sistema}} + \Delta S_{\text{entorno}} \geq 0$$

con igualdad solo para procesos reversibles. La conexión de Shannon permite reescribir esto:

Cuando un sistema físico evoluciona de la distribución $p$ a la distribución $q$,
el cambio de entropía libre no puede ser positivo si el entorno está a temperatura $T$:

$$\Delta F = \Delta U - T \Delta S \leq W_{\text{externo}}$$

donde $\Delta S = k_B \ln 2 \cdot [H(q) - H(p)]$ es el cambio de entropía de Shannon
escalado por $k_B \ln 2$.

## Divergencia KL y trabajo extraíble

La máxima cantidad de trabajo extraíble de un sistema en distribución $p$ respecto a
la distribución de equilibrio $q$ (distribución de Boltzmann) es:

$$W_{\text{máx}} = k_B T \ln 2 \cdot D_{\text{KL}}(p \| q)$$

Esto conecta directamente la divergencia KL con la eficiencia termodinámica: la KL mide
el "alejamiento del equilibrio" que puede convertirse en trabajo. Un sistema que ha
adquirido información sobre su estado (no está en $q$) puede, en principio, realizar
trabajo aprovechando esa información.

## Entropía y reversibilidad en computación cuántica

En computación cuántica, la evolución unitaria es **perfectamente reversible**:
no hay aumento de entropía cuántica de von Neumann durante la evolución coherente.

Solo la **medición** produce colapso de la función de onda e irreversibilidad. El
coste de Landauer aparece precisamente en el momento de la medición: borrar el estado
del qubit medido al estado de referencia requiere disipar $k_B T \ln 2$.

Esto sugiere que la computación cuántica no evita el principio de Landauer en el
límite termodinámico, aunque los cálculos intermedios pueden ser reversibles.

## Información en biofísica

**Eficiencia termodinámica de sistemas biológicos:**

- Un motor molecular como la miosina convierte ATP en trabajo mecánico con una
  eficiencia $\approx 25\%$ del límite de Carnot.
- El canal iónico necesita información sobre la concentración exterior para decidir
  si abrir o cerrar: el coste de esta "medición molecular" tiene una cota de Landauer.
- La síntesis de proteínas (traducción del ARNm) puede verse como decodificación de
  un código: la redundancia del código genético actúa como protección frente a errores
  de síntesis (análogo al código corrector de errores).

## Ideas clave

- La entropía de Shannon y la de Boltzmann son la misma cantidad con un factor de
  escala: $S = k_B \ln 2 \cdot H$.
- El demonio de Maxwell se exorciza con el principio de Landauer: borrar 1 bit de
  información requiere disipar al menos $k_B T \ln 2$ de energía.
- Las operaciones lógicas irreversibles (AND, OR) tienen un coste energético mínimo;
  la computación reversible puede, en principio, operar sin coste de Landauer.
- La divergencia KL mide el trabajo máximo extraíble de un sistema fuera del equilibrio.
- Los límites físicos de la computación están aún varios órdenes de magnitud por
  encima del rendimiento de los procesadores actuales.

## Ejercicios

1. A temperatura ambiente $T = 300$ K, calcula la energía mínima para procesar
   $10^9$ operaciones por segundo durante un año si cada operación borra 1 bit.
   Compara con el consumo de un smartphone moderno.
2. La puerta NAND es universalmente irreversible. ¿Cuántos bits de información
   descarta una puerta NAND? ¿Cuál es su coste de Landauer?
3. Demuestra que la puerta de Toffoli $(a,b,c) \to (a, b, c \oplus ab)$ es reversible
   aplicándola dos veces al mismo estado.
4. Si un sistema físico pasa de la distribución uniforme $U$ sobre $n$ estados a
   un estado determinista (una distribución delta), ¿cuánta entropía de Shannon
   se pierde? ¿Cuánto trabajo mínimo se debe disipar?
5. Explica intuitivamente por qué el límite de Landauer implica que una computadora
   perfectamente eficiente no puede funcionar a temperatura cero.

## Véase también

- [Información cuántica](04-informacion-cuantica.md)
- [Entropía diferencial](../02-teoria-informacion/10-entropia-diferencial.md)



<!-- nav-start -->

---
← [Información en el Aprendizaje Estadístico](05-informacion-en-aprendizaje.md) · [Información y biología](07-informacion-y-biologia.md) →

<!-- nav-end -->
## Referencias

- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.*
- Bennett, C. H. (1982). The thermodynamics of computation. *Int. J. Theor. Phys.*
- Maxwell, J. C. (1867). Theory of Heat. Macmillan.
- Szilard, L. (1929). Über die Entropieverminderung in einem thermodynamischen System. *Z. Phys.*
- Fredkin, E. y Toffoli, T. (1982). Conservative logic. *Int. J. Theor. Phys.*
- Cover, T. y Thomas, J. (2006). *Elements of Information Theory*, capítulo 9.
