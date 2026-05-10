# 15 - Complejidad aleatoria

## Contexto

Este ejercicio acompaña el artículo
[Complejidad aleatoria](../../04-complejidad-computacional/08-complejidad-aleatoria.md).

También se puede practicar con el cuaderno
[Complejidad aleatoria y tests probabilísticos](../../cuadernos/ejercicios/13-complejidad-aleatoria.ipynb).

## Enunciado

**Parte A — Amplificación:**

Sea un algoritmo de Monte Carlo de una cara con error ε = 1/3 (responde NO con
probabilidad 1 si la respuesta es NO; responde SÍ correctamente con probabilidad
al menos 2/3 si la respuesta es SÍ).

1. Si se ejecutan k rondas independientes y se toma mayoría de respuestas SÍ,
   ¿cuál es la probabilidad de error tras k = 10 rondas?
2. ¿Cuántas rondas k se necesitan para bajar el error a menos de 2^{-50}?

**Parte B — Test de Miller-Rabin:**

Sea n = 221. Se quiere comprobar si n es compuesto usando Miller-Rabin.

3. Descompón n - 1 = 220 en la forma 2^s · d con d impar. ¿Cuáles son s y d?
4. Con a = 2, comprueba si n supera el test de Miller-Rabin: calcula 2^d mod n
   y aplica las condiciones del test. ¿Declara n primo o compuesto?

## Pista

**Amplificación:** si cada ronda tiene error ε, tras k rondas independientes con
decisión por mayoría la probabilidad de error es ≤ (2ε)^k para ε < 1/2.

**Miller-Rabin:** n-1 = 2^s · d (d impar). El test declara n compuesto si:
- a^d ≢ 1 (mod n), Y
- a^{2^r·d} ≢ -1 (mod n) para todo r = 0, 1, ..., s-1.

Si pasa todas las condiciones, n es probablemente primo (testigo falso).

## Solución

### Parte A — Amplificación

#### 1. Probabilidad de error tras k = 10 rondas

Con ε = 1/3, el error de la mayoría está acotado por:

```text
P(error) ≤ (2ε)^k = (2/3)^k
```

Para k = 10:

```text
P(error) ≤ (2/3)^10 = 1024 / 59049 ≈ 0.0173 ≈ 1.73%
```

La probabilidad de error baja del 33% inicial al 1.73% con solo 10 repeticiones.

#### 2. Rondas para error < 2^{-50}

Se necesita (2/3)^k < 2^{-50}. Tomando logaritmos:

```text
k · log₂(2/3) < -50
k · (-0.585) < -50
k > 50 / 0.585 ≈ 85.5
```

Se necesitan al menos **k = 86 rondas** para garantizar error < 2^{-50}.

En la práctica, implementaciones de Miller-Rabin usan k = 40-64 rondas, dando
error < 4^{-40} ≈ 10^{-24} (negligible para cualquier aplicación criptográfica).

### Parte B — Miller-Rabin con n = 221

#### 3. Descomposición de n - 1 = 220

```text
220 = 2 · 110 = 2² · 55 = 4 · 55
```

Verificación: 55 es impar ✓

```text
s = 2,  d = 55
```

#### 4. Test con a = 2

**Paso 1:** Calcular x = 2^55 mod 221.

Usando exponenciación rápida (cuadrados sucesivos):

```text
2^1   = 2
2^2   = 4
2^4   = 16
2^8   = 256 mod 221 = 35
2^16  = 35² mod 221 = 1225 mod 221 = 1225 - 5·221 = 1225 - 1105 = 120
2^32  = 120² mod 221 = 14400 mod 221 = 14400 - 65·221 = 14400 - 14365 = 35
2^55  = 2^32 · 2^16 · 2^4 · 2^2 · 2^1
      = 35 · 120 · 16 · 4 · 2  (todo mod 221)
```

Calculamos paso a paso:
```text
35 · 120 = 4200 mod 221 = 4200 - 19·221 = 4200 - 4199 = 1
1 · 16   = 16
16 · 4   = 64
64 · 2   = 128
```

Así **x = 2^55 mod 221 = 128**.

**Paso 2:** ¿x ≡ 1 (mod 221)? 128 ≠ 1. Continuar.

**Paso 3:** r = 0: ¿x ≡ -1 ≡ 220 (mod 221)? 128 ≠ 220. Continuar.

**Paso 4:** r = 1: x = x² mod 221 = 128² mod 221 = 16384 mod 221.

```text
16384 / 221 ≈ 74.1  →  74 · 221 = 16354
16384 - 16354 = 30
```

x = 30. ¿x ≡ 220 (mod 221)? 30 ≠ 220.

**Conclusión:** se han agotado los r = 0, 1 (hay s = 2 iteraciones) sin que x sea
1 al inicio ni -1 en ninguna. Miller-Rabin **declara 221 compuesto** con testigo a = 2.

Efectivamente: 221 = 13 × 17.

## Comentario

El test de Miller-Rabin es co-RP: si n es compuesto, al menos 3/4 de los valores
de a lo detectan. El error de tipo II (declarar compuesto un primo) nunca ocurre.
Por eso se usa para generar primos en RSA: se toma un número impar aleatorio y se
aplican 40-64 rondas de Miller-Rabin; si pasa todas, es primo con probabilidad
astronómicamente alta.

## Para seguir

Comprueba n = 341 = 11 × 31 con a = 2. ¿Pasa o falla Miller-Rabin? (341 es el
pseudoprimo de Fermat más pequeño en base 2; verifica que Miller-Rabin sí lo detecta
como compuesto a diferencia del test de Fermat simple.)
