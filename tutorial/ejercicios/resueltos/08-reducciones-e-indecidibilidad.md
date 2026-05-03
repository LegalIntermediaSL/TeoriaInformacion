# 08 - Reducciones e indecidibilidad

## Contexto

Este ejercicio acompaña los artículos:

- [Reducciones e indecidibilidad](../../03-computabilidad/03-reducciones-e-indecidibilidad.md)
- [El problema de la parada](../../03-computabilidad/01-problema-de-la-parada.md)

## Enunciado

Define el problema:

```text
PRINTS = {P : el programa P imprime al menos un símbolo}
```

Demuestra que `PRINTS` es indecidible reduciendo desde `HALT`.

## Pista

Dado un par `(P, x)`, construye un programa `Q` que:

1. simula `P(x)`;
2. imprime algo solo si `P(x)` termina.

## Solución

Queremos demostrar que `PRINTS` es indecidible.

Suponemos, para llegar a una contradicción, que existe un decisor:

```text
D_PRINTS(Q)
```

que responde si un programa `Q` imprime alguna vez.

Ahora tomamos una instancia arbitraria de `HALT`:

```text
(P, x)
```

Construimos un programa `Q`:

```text
Q:
    ejecutar P(x)
    si P(x) termina:
        imprimir "ok"
```

Observa la equivalencia:

```text
Q imprime algo si y solo si P(x) termina
```

Entonces podríamos decidir `HALT` así:

```text
construir Q a partir de P y x
ejecutar D_PRINTS(Q)
si D_PRINTS dice "sí", responder que P(x) termina
si D_PRINTS dice "no", responder que P(x) no termina
```

Eso sería un decisor para `HALT`.

Pero sabemos que `HALT` es indecidible. Por tanto, el supuesto inicial era falso:
no puede existir `D_PRINTS`.

Así, `PRINTS` es indecidible.

## Dirección de la reducción

La dirección correcta es:

```text
HALT <= PRINTS
```

Esto significa que si pudiéramos decidir `PRINTS`, podríamos decidir `HALT`.

Como `HALT` no se puede decidir, `PRINTS` tampoco.

## Comentario

La reducción no necesita que `PRINTS` y `HALT` sean el mismo problema. Solo
necesita traducir cada instancia de `HALT` a una instancia de `PRINTS`
preservando la respuesta.

## Para seguir

Demuestra de forma análoga que el problema "¿este programa devuelve el número
0?" es indecidible.
