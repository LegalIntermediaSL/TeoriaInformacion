# 19 - Teorema de Shannon y capacidad de canal

## Contexto

Este ejercicio acompaña el artículo
[Teorema de Shannon y capacidad de canal](../../02-teoria-informacion/08-teorema-de-shannon-capacidad.md).

## Enunciado

Considera un canal binario simétrico (BSC) con probabilidad de error $p = 0.1$.

1. Calcula la capacidad $C$ del BSC.

2. ¿Puede un código transmitir a tasa $R = 0.5$ bits/uso con probabilidad de error
   tendiendo a 0? ¿Y a $R = 0.6$ bits/uso?

3. Un canal gaussiano tiene ruido $Z \sim N(0, \sigma^2 = 1)$ y potencia de señal
   máxima $P = 3$. Calcula su capacidad $C$.

4. Si se cuadruplica la potencia (de $P = 3$ a $P = 12$), ¿en cuántos bits/uso
   aumenta la capacidad?

## Pista

**BSC:** $C = 1 - H_b(p)$ donde $H_b(p) = -p\log_2 p - (1-p)\log_2(1-p)$.

**Shannon:** si $R < C$, existen códigos con tasa $R$ y error → 0. Si $R > C$, es imposible.

**Canal gaussiano:** $C = \frac{1}{2}\log_2(1 + P/\sigma^2)$.

## Solución

### 1. Capacidad del BSC con p = 0.1

```text
H_b(0.1) = -0.1·log₂(0.1) - 0.9·log₂(0.9)
         = 0.1·3.322 + 0.9·0.152
         = 0.332 + 0.137
         = 0.469 bits
```

$$C = 1 - H_b(0.1) = 1 - 0.469 = 0.531 \text{ bits/uso}$$

### 2. Tasas posibles e imposibles

- **R = 0.5 bits/uso:** Como $0.5 < C = 0.531$, el teorema de Shannon garantiza
  que **sí existen** códigos con tasa 0.5 y probabilidad de error $\to 0$. La
  tasa está por debajo de la capacidad.

- **R = 0.6 bits/uso:** Como $0.6 > C = 0.531$, por el **converso del teorema de
  Shannon** es **imposible** transmitir con tasa 0.6 manteniendo probabilidad de
  error $\to 0$. Cualquier secuencia de códigos con esta tasa tendrá error
  acotado inferiormente por una constante positiva.

**Interpretación:** la capacidad $C = 0.531$ es la frontera exacta. No hay zona
gris: por debajo se puede, por encima es imposible.

### 3. Capacidad del canal gaussiano

Con $P = 3$ y $\sigma^2 = 1$:

$$C = \frac{1}{2}\log_2\left(1 + \frac{P}{\sigma^2}\right) = \frac{1}{2}\log_2(1 + 3) = \frac{1}{2}\log_2 4 = \frac{1}{2} \cdot 2 = 1 \text{ bit/uso}$$

### 4. Efecto de cuadruplicar la potencia

Con $P = 12$ y $\sigma^2 = 1$:

$$C' = \frac{1}{2}\log_2(1 + 12) = \frac{1}{2}\log_2 13 \approx \frac{1}{2} \cdot 3.700 = 1.850 \text{ bits/uso}$$

Aumento: $\Delta C = 1.850 - 1.000 = 0.850$ bits/uso.

**Observación:** cuadruplicar la potencia (factor 4×) aumenta la capacidad en
menos de 1 bit. El canal gaussiano tiene un comportamiento **logarítmico** en la
potencia: doblar la SNR añade $\frac{1}{2}$ bit/uso. Esto explica por qué en
comunicaciones inalámbricas la potencia tiene rendimientos decrecientes y se
prefiere aumentar el ancho de banda.

## Comentario

El teorema de Shannon es de **existencia**, no constructivo: garantiza que existen
buenos códigos pero no los construye. Los códigos LDPC y polares son los primeros
códigos eficientemente decodificables que alcanzan la capacidad en la práctica.
La diferencia entre el teorema y la práctica es la historia de los códigos
correctores de errores del siglo XX.

## Para seguir

Calcula la capacidad del canal de borrado binario (BEC) con parámetro de borrado
$\epsilon = 0.2$: cada bit transmitido se borra con probabilidad $0.2$
independientemente. ¿Cómo afecta el borrado a la capacidad comparado con el BSC
de igual "daño"?
