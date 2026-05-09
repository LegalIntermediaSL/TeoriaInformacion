# Máquinas de Turing: ejercicios resueltos

**Artículo asociado:** [Máquinas de Turing](../../03-computabilidad/04-maquinas-de-turing.md)  
**Cuadernos relacionados:** [Simulación de MT](../../cuadernos/ejemplos/13-maquina-de-turing-simulacion.ipynb), [Ejercicios básicos de MT](../../cuadernos/ejercicios/11-maquinas-de-turing-basicas.ipynb)

---

## Ejercicio 1: reconocer el lenguaje $\{a^n b^n : n \geq 0\}$

**Enunciado.** Diseña una MT determinista que acepte exactamente las cadenas de la forma $a^n b^n$ (igual número de `a` seguidas de igual número de `b`). Verifica tu diseño con los casos: `""`, `"ab"`, `"aabb"`, `"a"`, `"ba"`, `"abab"`.

### Pista

¿Cómo saber si hay la misma cantidad de `a` que de `b` sin contarlas directamente? Empareja de uno en uno: marca una `a`, busca la primera `b` y márcala, regresa al inicio y repite. Si al terminar de emparejar no queda ningún símbolo sin marcar, la cadena es correcta.

### Solución

**Estados necesarios:**

| Estado | Rol |
|--------|-----|
| `q0` | Buscar la siguiente `a` sin marcar |
| `q1` | Moverse a la derecha para encontrar la siguiente `b` |
| `q2` | Volver al inicio para reiniciar el ciclo |
| `qa` | Aceptar |
| `qr` | Rechazar |

**Marcas:** `X` para `a` ya emparejada, `Y` para `b` ya emparejada.

**Función de transición $\delta$:**

| Estado | Lee | Escribe | Mueve | Nuevo estado |
|--------|-----|---------|-------|--------------|
| `q0` | `a` | `X` | R | `q1` |
| `q0` | `X` | `X` | R | `q0` |
| `q0` | `Y` | `Y` | R | `q0` |
| `q0` | `_` | `_` | R | `qa` |
| `q0` | `b` | `b` | R | `qr` |
| `q1` | `a` | `a` | R | `q1` |
| `q1` | `X` | `X` | R | `q1` |
| `q1` | `Y` | `Y` | R | `q1` |
| `q1` | `b` | `Y` | L | `q2` |
| `q1` | `_` | `_` | L | `qr` |
| `q2` | `a` | `a` | L | `q2` |
| `q2` | `X` | `X` | L | `q2` |
| `q2` | `Y` | `Y` | L | `q2` |
| `q2` | `_` | `_` | R | `q0` |

**Verificación manual para `"aabb"`:**

```
Inicio: q0, cinta = [a, a, b, b]

Ciclo 1:
  q0 lee 'a' → escribe 'X', mueve R, va a q1
  q1 lee 'a' → avanza R
  q1 lee 'b' → escribe 'Y', mueve L, va a q2
  q2 retrocede hasta '_' → mueve R, va a q0
  Cinta: [X, a, Y, b]

Ciclo 2:
  q0 lee 'X' → avanza R (ya marcado)
  q0 lee 'a' → escribe 'X', mueve R, va a q1
  q1 lee 'Y' → avanza R
  q1 lee 'b' → escribe 'Y', mueve L, va a q2
  q2 retrocede hasta '_' → va a q0
  Cinta: [X, X, Y, Y]

Ciclo 3:
  q0 lee 'X' → avanza R
  q0 lee 'X' → avanza R
  q0 lee 'Y' → avanza R
  q0 lee 'Y' → avanza R
  q0 lee '_' → va a qa → ACEPTA ✓
```

**Análisis de complejidad.** En cada ciclo la MT recorre aproximadamente toda la cinta (longitud $2n$) para marcar un par. Son $n$ ciclos en total, lo que da $\Theta(n^2)$ pasos. Esta es la complejidad temporal de la estrategia de emparejamiento iterativo.

---

## Ejercicio 2: reconocer el lenguaje $0^*1^*$

**Enunciado.** Diseña una MT que acepte todas las cadenas sobre $\{0,1\}$ donde todos los `0` preceden a todos los `1`, incluyendo la cadena vacía, cadenas solo con `0` y cadenas solo con `1`. Rechaza si aparece un `1` antes que algún `0`.

### Pista

Este problema no requiere retroceder: basta con leer la cinta de izquierda a derecha una sola vez. El patrón que invalida una cadena es la subsecuencia `10`.

### Solución

**Estados:**

| Estado | Rol |
|--------|-----|
| `q_ceros` | Leyendo (posiblemente) ceros |
| `q_unos` | Ya encontramos al menos un `1` |
| `qa` | Aceptar |
| `qr` | Rechazar |

**Función de transición:**

| Estado | Lee | Escribe | Mueve | Nuevo estado |
|--------|-----|---------|-------|--------------|
| `q_ceros` | `0` | `0` | R | `q_ceros` |
| `q_ceros` | `1` | `1` | R | `q_unos` |
| `q_ceros` | `_` | `_` | R | `qa` |
| `q_unos` | `1` | `1` | R | `q_unos` |
| `q_unos` | `0` | `0` | R | `qr` |
| `q_unos` | `_` | `_` | R | `qa` |

**Corrección.** La MT acepta si y solo si no aparece ningún `0` después de haber visto un `1`. Esta condición equivale exactamente a que la cadena sea de la forma $0^*1^*$.

**Análisis de complejidad.** La MT lee cada símbolo exactamente una vez y se detiene en el blanco. El número de pasos es $n + 1$ para una entrada de longitud $n$: complejidad $\Theta(n)$, lineal.

---

## Ejercicio 3: incrementar un número unario

**Enunciado.** En representación unaria, el número $n$ se escribe con $n$ palitos `|`. Diseña una MT que, dada una cinta con $n$ palitos, produzca una cinta con $n+1$ palitos.

### Solución

Solo se necesitan dos estados: uno para avanzar y uno para haber terminado.

**Función de transición:**

| Estado | Lee | Escribe | Mueve | Nuevo estado |
|--------|-----|---------|-------|--------------|
| `q0` | `\|` | `\|` | R | `q0` |
| `q0` | `_` | `\|` | R | `qa` |

**Ejecución para `"|||"` ($n = 3$):**

```
q0, cinta = [|, |, |]
  Lee '|' → avanza; [|, |, |]
  Lee '|' → avanza; [|, |, |]
  Lee '|' → avanza; [|, |, |]
  Lee '_' → escribe '|'; [|, |, |, |] → qa → ACEPTA
```

El resultado es `"||||"` ($n + 1 = 4$). La MT nunca retrocede; su complejidad es $\Theta(n)$.

---

## Reflexión

Los tres ejercicios ilustran un patrón común en el diseño de máquinas de Turing:

1. **El estado codifica la memoria** de lo que se ha visto: un residuo, un símbolo memorizado, o un bit de paridad.
2. **Las marcas en la cinta** sustituyen el conteo explícito: en lugar de llevar un número, dejamos una huella del trabajo ya hecho.
3. **La complejidad temporal depende de cuántas veces se recorre la cinta**: un solo recorrido es $\Theta(n)$; un recorrido por cada elemento procesado es $\Theta(n^2)$.

Una MT eficiente minimiza los retrocesos. Para $\{a^n b^n\}$, una estrategia de marcado binario (marcar $\lfloor n/2 \rfloor$ en cada pasada) bajaría a $\Theta(n \log n)$; con dos cintas se alcanza $\Theta(n)$.
