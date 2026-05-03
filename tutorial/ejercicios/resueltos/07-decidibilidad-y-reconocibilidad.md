# 07 - Decidibilidad y reconocibilidad

## Contexto

Este ejercicio acompaña los artículos:

- [Decidibilidad y reconocibilidad](../../03-computabilidad/02-decidibilidad-y-reconocibilidad.md)
- [El problema de la parada](../../03-computabilidad/01-problema-de-la-parada.md)

## Enunciado

Sea `L` un lenguaje reconocible. Esto significa que existe un programa `R` que:

- acepta si `w in L`;
- puede rechazar o no terminar si `w notin L`.

Responde:

1. ¿Por qué todo lenguaje decidible es reconocible?
2. ¿Por qué el lenguaje `HALT` es reconocible?
3. ¿Por qué reconocible no significa decidible?
4. Si `L` y su complemento son reconocibles, demuestra que `L` es decidible.

## Pista

Para la última parte, imagina ejecutar dos reconocedores en paralelo:

- uno para `L`;
- otro para el complemento de `L`.

## Solución

### Todo decidible es reconocible

Si `L` es decidible, existe un programa `D` que siempre termina y responde
correctamente si `w in L`.

Para reconocer `L`, usamos el mismo programa:

- si `D` acepta, aceptamos;
- si `D` rechaza, rechazamos.

Como `D` siempre termina, cumple más de lo que exige un reconocedor.

### `HALT` es reconocible

Definimos:

```text
HALT = {(P, x) : el programa P termina con entrada x}
```

Un reconocedor para `HALT` hace lo siguiente:

```text
simular P(x)
si P(x) termina, aceptar
```

Si `P(x)` termina, el reconocedor acepta. Si `P(x)` no termina, la simulación
tampoco termina.

Esto basta para reconocer `HALT`, pero no para decidirlo.

### Reconocible no significa decidible

Un lenguaje reconocible puede dejar sin respuesta algunos casos negativos.

En `HALT`, si el programa no termina, la simulación directa nunca alcanza una
evidencia definitiva. El problema de la parada demuestra que no existe otro
método general que siempre termine y responda correctamente.

Por eso `HALT` es reconocible pero no decidible.

### Si `L` y su complemento son reconocibles, `L` es decidible

Supongamos que tenemos:

- `R_L`, reconocedor de `L`;
- `R_C`, reconocedor del complemento de `L`.

Dada una entrada `w`, ejecutamos ambos reconocedores en paralelo, alternando
pasos:

```text
un paso de R_L(w)
un paso de R_C(w)
un paso de R_L(w)
un paso de R_C(w)
...
```

Si `w in L`, entonces `R_L` aceptará en algún momento. Respondemos "sí".

Si `w notin L`, entonces `w` pertenece al complemento, así que `R_C` aceptará en
algún momento. Respondemos "no".

En ambos casos, uno de los dos reconocedores acepta. Por tanto, el procedimiento
termina siempre y decide `L`.

## Comentario

La diferencia entre reconocer y decidir es una frontera fundamental: reconocer
confirma casos positivos; decidir exige resolver positivos y negativos.

## Para seguir

Explica por qué el complemento de `HALT` no puede ser reconocible.
