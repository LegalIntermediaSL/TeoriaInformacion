# Teoría de Juegos e Información Asimétrica

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Combinatoria y entropía](../01-fundamentos-matematicos/01-combinatoria-y-entropia.md)
- [Divergencia KL y divergencias de información](../02-entropía-y-divergencias/05-divergencia-kl.md)
- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)

## Objetivos de aprendizaje

1. Entender el equilibrio de Nash como punto fijo y su relación con la entropía máxima.
2. Formalizar la información asimétrica y sus consecuencias económicas (selección adversa).
3. Relacionar los mecanismos de señalización y screening con la divergencia KL.
4. Comprender el teorema de revelación y las subastas de segundo precio.
5. Conectar el correlated equilibrium con el principio de máxima entropía.


## Intuición

Cuando dos partes negocian sin conocer toda la información relevante del otro, la incertidumbre
no es solo psicológica: tiene un coste medible en bits. En la teoría de juegos con información
asimétrica, la divergencia KL cuantifica cuánto le cuesta a un agente bluffear — pretender ser
de un tipo distinto al real. Esta conexión transforma la economía de la información en un
problema formal de teoría de la información.

## Conceptos clave

### Equilibrio de Nash como punto fijo

Sea un juego con $n$ jugadores, conjuntos de estrategias $S_i$ y funciones de utilidad $u_i$.
Un perfil de estrategias mixtas $\sigma^* = (\sigma_1^*, \ldots, \sigma_n^*)$ es un
**equilibrio de Nash** si ningún jugador puede mejorar su utilidad desviándose unilateralmente:

$$\forall i, \forall \sigma_i \in \Delta(S_i): \quad u_i(\sigma_i^*, \sigma_{-i}^*) \geq u_i(\sigma_i, \sigma_{-i}^*)$$

Por el teorema del punto fijo de Kakutani (extendido por Nash, 1950), todo juego finito
tiene al menos un equilibrio de Nash en estrategias mixtas.

### Información asimétrica: el mercado de limones

Akerlof (1970) analizó el mercado de coches usados. Los vendedores conocen la calidad del
coche ("bueno" o "limón"), pero los compradores no. Si $q$ es la fracción de coches buenos
y los compradores solo pueden ofrecer el precio esperado $\bar{p} = q \cdot p_{\text{bueno}} + (1-q) \cdot p_{\text{limón}}$,
los vendedores de coches buenos rechazan el precio, el mercado colapsa hacia solo limones,
y el precio baja aún más. Este proceso de **selección adversa** puede destruir el mercado.

La entropía del tipo del vendedor $H(Q)$ mide la incertidumbre que soporta el comprador.
Con alta incertidumbre (mercado muy heterogéneo), la selección adversa es más severa.

### Señalización y screening

**Señalización (Spence, 1973):** el agente con información privada emite una señal costosa
para revelarla. Un graduado universitario con alta capacidad $\theta_H$ puede permitirse
cursar $e^*$ años de educación porque su coste marginal $c(\theta_H, e) < c(\theta_L, e)$.
El equilibrio separador existe cuando la señal es lo bastante costosa para los de baja
capacidad: $u(\theta_L, e^*) < u(\theta_L, 0)$.

**Screening:** el lado desinformado diseña un menú de contratos $\{(q_i, t_i)\}$ que induce
a cada tipo a autoseleccionarse. La restricción de compatibilidad de incentivos exige que
cada tipo prefiera su contrato asignado al del otro tipo.

### Mecanismos y teorema de revelación

**Subasta de segundo precio (Vickrey):** cada participante declara una valoración $b_i$; gana
el mayor postor y paga el segundo precio más alto $b_{(2)}$. Declarar la valoración
verdadera $b_i = v_i$ es **estrategia dominante** independientemente de lo que hagan los
demás.

**Teorema de revelación (Myerson, 1979):** para cualquier mecanismo Bayes-Nash implementable,
existe un mecanismo directo y verdadero-revelador que implementa el mismo resultado. Basta
estudiar los mecanismos donde los agentes reportan sus tipos privados y el diseñador les
cree.

### Coste informacional del bluffing

Si un agente de tipo $\theta_L$ pretende ser de tipo $\theta_H$, actúa según la distribución
de comportamiento de $\theta_H$, que difiere de su distribución óptima real. El coste
esperado de esta desviación tiene una cota inferior en términos de divergencia KL:

$$\text{Coste del bluffing} \geq D_{\mathrm{KL}}(P_{\theta_H} \| P_{\theta_L})$$

donde $P_\theta$ es la distribución de estrategias óptimas del tipo $\theta$.

### Correlated equilibrium y máxima entropía

Un **correlated equilibrium** (Aumann, 1974) es una distribución de probabilidad conjunta
$\mu$ sobre perfiles de estrategias tal que ningún jugador quiere desviarse dado su señal
recomendada. El conjunto de correlated equilibria es convexo, y el que maximiza la entropía
$H(\mu)$ es la solución de máxima entropía sujeta a las restricciones de racionalidad:

$$\max_\mu H(\mu) \quad \text{s.a.} \quad \mu \text{ es correlated equilibrium}$$

### Juegos de información incompleta (Harsanyi, 1967)

Harsanyi modeló la incertidumbre sobre las utilidades rivales mediante **tipos**: cada
jugador $i$ tiene un tipo privado $\theta_i$ extraído de una distribución de probabilidad
conjunta conocida $P(\theta_1, \ldots, \theta_n)$. Un **equilibrio de Bayes-Nash** es un
perfil de estrategias $\sigma_i(\theta_i)$ tal que cada jugador maximiza su utilidad esperada
dado su tipo y las estrategias de los demás.

## Ejemplo concreto

**Subasta de segundo precio con tres postores.** Valoraciones privadas: $v_1 = 100$, $v_2 = 70$, $v_3 = 50$.
Todos declaran su valoración verdadera (dominancia). Gana el postor 1 y paga 70 (segundo precio).
La utilidad del ganador es $100 - 70 = 30 > 0$. Si el postor 1 intentara declarar 60 para
reducir el pago, perdería la subasta a pesar de tener la valoración más alta — la estrategia
dominante protege contra este tipo de desviaciones.

## Teorema principal

**Teorema de equivalencia de ingresos (Myerson-Riley, 1981).** En subastas con valoraciones
simétricas e independientes, cualquier mecanismo que asigne el bien al postor de mayor
valoración y dé utilidad cero al de valoración más baja genera el mismo ingreso esperado
al vendedor.

$$\mathbb{E}[\text{ingreso}] = \mathbb{E}\left[v_{(n)} - \int_0^{v_{(n)}} F^{n-1}(t)\,dt\right]$$

donde $v_{(n)}$ es el máximo de las valoraciones y $F$ es su distribución común.

## Ideas clave

- El equilibrio de Nash en estrategias mixtas maximiza la entropía local: en un equilibrio,
  el jugador es indiferente entre las estrategias que mezcla, lo que corresponde a una
  distribución de máxima incertidumbre compatible con esa indiferencia.
- La selección adversa (mercado de limones) es una consecuencia directa de la incertidumbre
  informacional: cuanto mayor es $H(\text{tipo})$ para el comprador, mayor es la degradación
  del mercado.
- El coste del bluffing tiene una cota informacional: imitar un tipo ajeno exige actuar según
  una distribución diferente a la óptima, con un exceso de coste al menos proporcional a $D_{\mathrm{KL}}$.
- El teorema de revelación reduce el espacio de mecanismos a buscar: basta estudiar los
  directos y verdadero-reveladores, un subespacio enormemente más manejable.
- El correlated equilibrium con máxima entropía es la solución racional de un árbitro que
  debe ser justo (maximizar incertidumbre) y consistente con la racionalidad de los jugadores.

## Ejercicios

1. En el modelo de Akerlof con $q = 0.5$, $p_{\text{bueno}} = 10\,000$ y $p_{\text{limón}} = 2\,000$,
   calcula el precio de equilibrio y determina si el mercado colapsa completamente.
2. Calcula la divergencia KL entre las estrategias mixtas de equilibrio de dos jugadores en
   el juego de "cara o cruz" estándar. ¿Qué ocurre si uno de ellos bluffea con probabilidad $0.7$?
3. Diseña un menú de contratos para screening con dos tipos de consumidores ($\theta_L = 1$,
   $\theta_H = 3$) y función de utilidad $u = \theta q - t$. Verifica la compatibilidad de incentivos.
4. Demuestra que en la subasta de segundo precio, declarar la valoración verdadera es estrategia
   dominante considerando los dos casos: valoración mayor y menor que la de los rivales.
5. Calcula el correlated equilibrium de máxima entropía para el juego "Battle of the Sexes"
   y compáralo con los equilibrios de Nash puros.
6. En un juego de señalización de Spence con dos tipos, ¿qué condición sobre el coste de la
   educación garantiza un equilibrio separador? Exprésalo como una restricción sobre $D_{\mathrm{KL}}$.

## Véase también

- [Divergencia KL y divergencias de información](../02-entropía-y-divergencias/05-divergencia-kl.md)
- [Aprendizaje automático e información](03-aprendizaje-automatico-e-informacion.md)
- [Privacidad diferencial](11-privacidad-diferencial.md)
- [Información en aprendizaje estadístico](05-informacion-en-aprendizaje.md)

## Referencias

- Akerlof, G. A. (1970). The market for "lemons". *Quarterly Journal of Economics*, 84(3), 488–500.
- Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*, 87(3), 355–374.
- Myerson, R. B. (1979). Incentive compatibility and the bargaining problem. *Econometrica*, 47(1), 61–73.
- Harsanyi, J. C. (1967). Games with incomplete information played by "Bayesian" players. *Management Science*, 14(3), 159–182.
- Aumann, R. J. (1974). Subjectivity and correlation in randomized strategies. *Journal of Mathematical Economics*, 1(1), 67–96.
