# 02 - Criptografía y complejidad

La criptografía moderna depende de una idea delicada: algunas tareas deben ser
fáciles para quien tiene cierta información secreta y difíciles para quien no la
tiene.

Por eso la complejidad computacional es una parte central del lenguaje
criptográfico.

## Fácil en una dirección, difícil en la inversa

Muchas construcciones criptográficas buscan funciones fáciles de calcular pero
difíciles de invertir.

La intuición es:

```text
x -> f(x)      fácil
f(x) -> x      difícil
```

Si conocemos información adicional, llamada trampa o clave secreta, la inversión
puede volverse fácil.

## Factorización

Un ejemplo clásico es multiplicar dos números primos grandes:

```text
p * q = N
```

Multiplicar `p` y `q` es fácil incluso para números enormes. Pero, dado solo
`N`, recuperar `p` y `q` puede ser difícil con algoritmos clásicos conocidos si
los números son suficientemente grandes.

La seguridad de sistemas como RSA se apoya en esta asimetría práctica.

## Dificultad no es imposibilidad

En criptografía, "difícil" no significa indecidible ni imposible en sentido
absoluto. Normalmente significa que no se conoce un algoritmo eficiente para
resolver el problema con los recursos disponibles.

Factorizar un número compuesto siempre es posible por búsqueda exhaustiva, pero
esa búsqueda puede ser inviable.

Aquí aparece la diferencia entre computabilidad y complejidad:

- computabilidad pregunta si existe un algoritmo;
- complejidad pregunta si existe un algoritmo eficiente.

## Peor caso y caso promedio

La NP-completitud habla sobre dificultad en peor caso. La criptografía necesita
algo más sutil: dificultad en casos generados de forma típica o aleatoria.

Un problema puede tener instancias muy difíciles pero ser fácil en la mayoría de
los casos. Para criptografía queremos que las instancias usadas realmente sean
difíciles para un atacante.

Esta diferencia entre peor caso y caso promedio es una de las conexiones más
profundas entre complejidad y seguridad.

## Funciones hash

Una función hash criptográfica toma una entrada de longitud variable y produce
una salida de longitud fija.

Se espera que sea difícil:

- encontrar una entrada que produzca un hash dado;
- encontrar dos entradas distintas con el mismo hash;
- predecir cómo cambia la salida al modificar la entrada.

Estas propiedades no se prueban solo con entropía. También dependen de hipótesis
computacionales sobre lo que un adversario puede hacer eficientemente.

## Aleatoriedad y claves

La teoría de la información también entra en juego. Una clave secreta debe tener
suficiente incertidumbre para resistir búsqueda exhaustiva.

Si una clave tiene `n` bits elegidos uniformemente, hay:

```text
2^n
```

claves posibles.

Pero si los usuarios eligen contraseñas predecibles, la entropía efectiva puede
ser mucho menor que la longitud aparente.

## Información perfecta y seguridad computacional

El cifrado de Vernam, o one-time pad, puede ofrecer seguridad perfecta si la
clave es verdaderamente aleatoria, tan larga como el mensaje y se usa una sola
vez.

La mayoría de sistemas prácticos no usan claves tan largas. En su lugar, buscan
seguridad computacional: romper el sistema debería requerir recursos
inviables.

Así, la criptografía práctica combina información, aleatoriedad y complejidad.

## Computación cuántica

La computación cuántica cambia algunas hipótesis. Por ejemplo, el algoritmo de
Shor factoriza enteros en tiempo polinómico en un computador cuántico ideal.

Esto amenaza criptosistemas basados en factorización o logaritmo discreto y
motiva la criptografía poscuántica.

El punto general es que la seguridad depende del modelo de cómputo disponible.

## Idea para recordar

La criptografía vive entre información y complejidad: una clave debe ocultar
incertidumbre, y un atacante debe enfrentarse a problemas computacionalmente
difíciles.

## Ejercicios

1. Explica la diferencia entre seguridad perfecta y seguridad computacional.
2. ¿Por qué una contraseña larga pero predecible puede ser débil?
3. ¿Qué diferencia hay entre dificultad en peor caso y dificultad promedio?
4. ¿Por qué la computación cuántica obliga a revisar ciertas hipótesis
   criptográficas?
