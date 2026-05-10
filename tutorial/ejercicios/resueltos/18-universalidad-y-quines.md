# 18 - Universalidad y autorreferencia

## Contexto

Este ejercicio acompaña el artículo
[Universalidad y autorreferencia](../../03-computabilidad/07-universalidad-y-autorreferencia.md).

También se puede practicar con el cuaderno
[Universalidad y quines](../../cuadernos/ejercicios/15-universalidad-y-quines.ipynb).

## Enunciado

**Parte A — Quines:**

1. Explica la estructura de un quine en dos partes: datos `d` y código `c`. ¿Qué
   debe hacer cada parte para que el programa imprima su propio código fuente?

2. El siguiente esqueleto Python define un quine incompleto:

   ```python
   d = '...'
   print(d % d)
   ```

   ¿Qué valor debe tener `d` para que el programa sea un quine válido? Justifica.

**Parte B — Teorema de Rice:**

3. Enuncia el teorema de Rice. ¿Por qué la propiedad "el programa imprime `hola`"
   es no computable?

4. ¿Cuál de las siguientes propiedades de máquinas de Turing es **decidible**?
   Justifica cada respuesta.
   - (a) "M tiene exactamente 5 estados."
   - (b) "M acepta la cadena vacía ε."
   - (c) "M se detiene en a lo sumo 1000 pasos sobre cualquier entrada de longitud ≤ 10."
   - (d) "El lenguaje de M es el conjunto de todos los primos."

**Parte C — Teorema del punto fijo:**

5. Enuncia el teorema del punto fijo de Kleene. Da un ejemplo intuitivo de una
   máquina de Turing que sea su propio punto fijo.

## Pista

**Quines:** un quine tiene la forma `c(d)` donde `d` es una representación textual
de `c` y `c` es código que imprime su propia descripción. La clave es que `d` debe
contener `%s` o un marcador donde se insertará la copia de `d`.

**Rice:** una propiedad es **semántica** si solo depende del lenguaje aceptado (el
comportamiento), no de la descripción interna (el número de estados, las
transiciones). El teorema de Rice dice: toda propiedad semántica no trivial es
indecidible.

**Punto fijo:** el punto fijo de una transformación `f` es un programa `P` tal que
`f(P)` y `P` tienen el mismo comportamiento. Esto no significa que `P = f(P)` como
cadenas, sino que computan lo mismo.

## Solución

### Parte A — Quines

#### 1. Estructura de un quine

Un quine tiene dos partes:

- **Datos `d`:** una cadena literal que contiene el código completo del programa,
  incluyendo la representación de sí misma (o un patrón que la genera).

- **Código `c`:** instrucciones que toman `d` y producen la salida completa del
  programa: primero la parte de datos (asignando o imprimiendo `d` con sus
  delimitadores) y luego la parte de código.

La clave es la **autorreferencia controlada:** `d` es una representación de `c`
dentro del propio código, y `c` usa `d` para reconstruir el programa completo.
Ninguna parte puede generarse a sí misma sola; es la interacción entre ambas lo
que produce la autorreplicación.

#### 2. El quine en Python

El quine clásico en Python de dos líneas usa format strings:

```python
d = 'd = %r\nprint(d %% d)'
print(d % d)
```

**¿Por qué funciona?**

- `%r` formatea una cadena con sus comillas, de modo que `d % d` sustituye el
  primer `%r` por la representación de `d` incluyendo sus comillas.
- El `%%` se convierte en un `%` literal en la salida.

Cuando se ejecuta, la salida es:

```
d = 'd = %r\nprint(d %% d)'
print(d % d)
```

que es exactamente el código fuente original. ✓

**Verificación:** si guardamos el código en `quine.py` y ejecutamos
`python quine.py > out.py`, el archivo `out.py` es idéntico a `quine.py`.

### Parte B — Teorema de Rice

#### 3. Enunciado y aplicación

**Teorema de Rice.** Sea P una propiedad no trivial del lenguaje reconocido por
una máquina de Turing (es decir, P depende solo de L(M), no de la estructura
interna de M). Si P es no trivial (hay máquinas que la satisfacen y máquinas que
no), entonces decidir si una MT M satisface P es **indecidible**.

**La propiedad "M imprime `hola`" es no computable** porque:

1. Es **semántica:** depende de si `hola` está en la salida de M, no de su
   estructura interna.
2. Es **no trivial:** la MT que siempre imprime `hola` la satisface; la MT que
   siempre rechaza no la satisface.

Por el teorema de Rice, no existe ningún algoritmo que, dado ⟨M⟩, decida si M
imprime `hola`.

**Demostración esquemática:** supóngase que existe el decisor D para esta
propiedad. Usando D se podría construir un decisor para el problema de la parada:
dado ⟨M, w⟩, construir M' que simula M(w) y, si se detiene, imprime `hola`. Si D
acepta M', entonces M se detuvo sobre w. Esto decide el problema de la parada —
contradicción con su indecidibilidad.

#### 4. ¿Cuál propiedad es decidible?

**(a) "M tiene exactamente 5 estados."**

**Decidible.** Esta es una propiedad **sintáctica** (depende de la descripción de
M, no de su comportamiento). Basta contar los estados de la representación ⟨M⟩.
El teorema de Rice no aplica porque no es una propiedad del lenguaje.

**(b) "M acepta la cadena vacía ε."**

**Indecidible.** Es una propiedad semántica no trivial: hay MTs que aceptan ε y
MTs que no. Por Rice, es indecidible. (Se puede también reducir directamente desde
el problema de la parada.)

**(c) "M se detiene en a lo sumo 1000 pasos sobre cualquier entrada de longitud ≤ 10."**

**Decidible.** Hay un número finito de entradas de longitud ≤ 10 y un número
finito de configuraciones posibles en 1000 pasos. Se puede simular M
exhaustivamente sobre todas esas entradas y verificar que se detiene. La
propiedad es sobre el comportamiento acotado, que es siempre decidible.

**(d) "El lenguaje de M es el conjunto de todos los primos."**

**Indecidible.** Es una propiedad semántica no trivial sobre L(M). Por Rice, es
indecidible. (Decidir si L(M) = PRIMES requeriría verificar infinitas entradas.)

### Parte C — Teorema del punto fijo

#### 5. Enunciado y ejemplo

**Teorema del punto fijo de Kleene.** Para cualquier función computable
f: ⟨M⟩ ↦ ⟨M'⟩, existe una máquina de Turing P tal que P y f(⟨P⟩) son
**computacionalmente equivalentes**: L(P) = L(f(⟨P⟩)).

Intuitivamente: ninguna transformación computable puede escapar de tener un punto
fijo. Siempre existe un programa que "sobrevive" a la transformación.

**Ejemplo intuitivo:** sea f(⟨M⟩) = ⟨M⟩ (la identidad). Entonces toda MT es
su propio punto fijo trivialmente.

**Ejemplo no trivial:** sea f(⟨M⟩) la MT que ejecuta M y niega su respuesta
(acepta ↔ rechaza). Por el teorema del punto fijo, existe P tal que P y f(⟨P⟩)
son equivalentes, es decir, P y "P con respuesta negada" aceptan el mismo
lenguaje. Esto solo es posible si L(P) = ∅ o L(P) = Σ* (la negación de un
lenguaje vacío es Σ*, pero ∅ y Σ* no son iguales en general — la resolución es
que P no se detiene sobre ninguna entrada, haciendo que la comparación sea vacua).

**El quine como punto fijo:** un quine es el punto fijo de la función
f(⟨M⟩) = "la MT que imprime ⟨M⟩". El quine P satisface: "P imprime ⟨P⟩" y
"f(⟨P⟩) también imprime ⟨P⟩". Son computacionalmente equivalentes. ✓

## Comentario

El teorema de Rice y el teorema del punto fijo son dos caras de la misma moneda.
Rice dice que no puedes verificar el comportamiento desde fuera. El punto fijo
dice que siempre puedes construir un programa que se autorreferencia de forma
controlada. Juntos explican por qué la verificación automática de software tiene
límites fundamentales: no es solo un problema de ingeniería, sino de lógica.

## Para seguir

Demuestra formalmente que el problema de decidir si L(M) = Σ* (si M acepta todo)
es indecidible, usando el teorema de Rice y la reducción desde el problema de la
parada. ¿Es el lenguaje {⟨M⟩ : L(M) = Σ*} reconocible o co-reconocible?
