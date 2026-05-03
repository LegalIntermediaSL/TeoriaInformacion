# 09 - Canales y capacidad

## Contexto

Este ejercicio acompaña los artículos:

- [Canales discretos y capacidad](../../02-teoria-informacion/04-canales-discretos-y-capacidad.md)
- [Códigos correctores de errores](../../02-teoria-informacion/06-codigos-correctores-de-errores.md)

También se puede practicar con:

- [Canal binario simétrico](../../cuadernos/ejemplos/03-canal-binario-simetrico.ipynb)
- [Código de repetición y corrección de errores](../../cuadernos/ejemplos/08-codigos-repeticion-correccion.ipynb)

## Enunciado

Considera un canal binario simétrico con probabilidad de error `p`.

1. Escribe la fórmula de la entropía binaria `H_b(p)`.
2. Escribe la capacidad del canal.
3. Calcula la capacidad cuando `p = 0`, `p = 0.5` y `p = 0.1`.
4. Interpreta los resultados.

## Pista

Usa:

```text
H_b(p) = -p log2(p) - (1-p) log2(1-p)
C = 1 - H_b(p)
```

Para `p = 0` y `p = 1`, se toma `0 log2(0)` como `0` por continuidad.

## Solución

La entropía binaria es:

```text
H_b(p) = -p log2(p) - (1-p) log2(1-p)
```

La capacidad del canal binario simétrico es:

```text
C = 1 - H_b(p)
```

### Caso `p = 0`

No hay errores.

```text
H_b(0) = 0
C = 1 - 0 = 1 bit por uso
```

El canal transmite perfectamente un bit por uso.

### Caso `p = 0.5`

La salida es completamente aleatoria respecto de la entrada.

```text
H_b(0.5) = 1
C = 1 - 1 = 0 bits por uso
```

El canal no transmite información útil.

### Caso `p = 0.1`

Calculamos:

```text
H_b(0.1) = -0.1 log2(0.1) - 0.9 log2(0.9)
         ≈ 0.469 bits
```

Por tanto:

```text
C ≈ 1 - 0.469 = 0.531 bits por uso
```

## Comentario

La capacidad no dice que cada símbolo individual se reciba sin error. Dice cuál
es el ritmo máximo de transmisión fiable posible usando códigos adecuados y
bloques largos.

## Para seguir

Calcula la capacidad para `p = 0.01`, `0.2` y `0.4`. Observa cómo se aproxima a
cero cuando `p` se acerca a `0.5`.
