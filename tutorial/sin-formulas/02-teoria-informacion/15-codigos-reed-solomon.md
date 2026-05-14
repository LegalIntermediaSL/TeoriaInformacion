> **Nota:** Esta es la versión sin fórmulas LaTeX de [15-codigos-reed-solomon](../../02-teoria-informacion/15-codigos-reed-solomon.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Códigos de Reed-Solomon y aplicaciones

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min

## Prerrequisitos

- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)
- [Combinatoria y conteo](../01-fundamentos-matematicos/03-combinatoria-y-conteo.md)
- [Grafos y estructuras discretas](../01-fundamentos-matematicos/04-grafos-y-estructuras-discretas.md)

## Objetivos de aprendizaje

1. Comprender la estructura algebraica de los campos de Galois `GF(2^m)` y por qué son necesarios para Reed-Solomon.
2. Definir un código Reed-Solomon como evaluación de polinomios y derivar su distancia mínima a partir de la cota de Singleton.
3. Calcular la capacidad de corrección de errores `t = ⌊(d-1)/2⌋` para un código concreto.
4. Describir cómo RS(255, 223) protege los datos en CD y cómo los códigos QR explotan una variante corta del mismo principio.
5. Comparar Reed-Solomon con los códigos LDPC modernos en cuanto a complejidad de decodificación y regímenes de operación.

---

## Intuición

Supón que quieres enviar una lista de `k` números y el receptor puede perder o corromper hasta `t` de ellos. Un polinomio de grado `k-1` queda determinado de forma única por `k` puntos; si evalúas ese polinomio en `n > k` puntos y envías todos los valores, el receptor puede reconstruir el polinomio aunque haya recibido solo `k` valores correctos. Cuantos más puntos extra envíes, más errores puedes tolerar.

Reed y Solomon (1960) formalizaron esta idea usando aritmética de cuerpos finitos para que todos los cálculos sean exactos y sin errores de redondeo.

## Campos de Galois: aritmética sin fracciones

Para operar con polinomios cuyos coeficientes son bits (o símbolos de `m` bits), se necesita un campo donde la suma y el producto estén bien definidos y todo elemento no nulo tenga inverso multiplicativo.

El **campo de Galois** `GF(2^m)` tiene exactamente `2^m` elementos. Se construye como el anillo de polinomios `𝔽_2[x]` módulo un polinomio irreducible `p(x)` de grado `m`:


> **Fórmula:** `GF(2^m) ≅ 𝔽_2[x] / ⟨ p(x) ⟩.`


La suma es XOR bit a bit. El producto es la multiplicación de polinomios seguida de reducción módulo `p(x)`.

**Ejemplo para `m=3`:** Sea `p(x) = x³ + x + 1` (irreducible sobre `𝔽_2`). Los 8 elementos son `\{0, 1, α, α², α²+α, …\}`, donde `α` es la raíz de `p`. La propiedad clave es que `α⁷ = 1`, de modo que `α` es un generador del grupo multiplicativo `GF(8)^*`, que es cíclico de orden `2^m - 1`.

Para `m = 8` se obtiene `GF(256)`, el campo usado por Reed-Solomon en CD y en QR codes.

## Definición formal

Un código **Reed-Solomon** `RS(n, k)` sobre `GF(q)` con `n ≤ q` se define escogiendo `n` puntos distintos `α_1, …, α_n ∈ GF(q)` y evaluando todos los polinomios `f ∈ GF(q)[x]` de grado `< k`:


> **Fórmula:** `RS(n,k) = \{ (f(α_1), …, f(α_n)) | f ∈ GF(q)[x], \deg f < k \}.`


Cada palabra código tiene `n` símbolos; cada símbolo toma valores en `GF(q)`. La tasa del código es `R = k/n`.

### Polinomio generador

Equivalentemente, `RS(n, k)` es un código cíclico cuyo **polinomio generador** es:


> **Fórmula:** `g(x) = (x - α)(x - α²)⋯(x - α^(n-k)),`


donde `α` es un elemento primitivo de `GF(q)`. Toda palabra código es un múltiplo de `g(x)` de grado `< n`.

## Teorema principal: cota de Singleton y distancia mínima

**Cota de Singleton:** para todo código lineal `[n, k, d]` sobre cualquier alfabeto,


> **Fórmula:** `d ≤ n - k + 1.`


Un código que alcanza esta cota se llama **MDS** (*Maximum Distance Separable*).

**Teorema:** `RS(n, k)` es un código MDS con distancia mínima


> **Fórmula:** `d = n - k + 1.`


*Demostración (esbozo):* cualquier polinomio no nulo de grado `< k` tiene a lo sumo `k-1` raíces en `GF(q)`. Por tanto, la imagen de evaluación en `n` puntos puede ser cero en a lo sumo `k-1` posiciones, lo que significa que hay al menos `n - (k-1) = n - k + 1` posiciones no nulas. `\square`

### Capacidad de corrección

Un código con distancia mínima `d` puede corregir hasta


> **Fórmula:** `t = ≤ft⌊ (d-1)/2 ⌋`


errores (errores en posición desconocida) y detectar hasta `d - 1` errores.

## Ejemplo concreto: RS(7, 3) sobre GF(8)

- `n = 7`, `k = 3`, `d = 5`, `t = 2`.
- Mensaje: tres coeficientes `(m_0, m_1, m_2) ∈ GF(8)³`.
- Polinomio mensaje: `f(x) = m_0 + m_1 x + m_2 x²`.
- Palabra código: `(f(α⁰), f(α¹), …, f(α⁶))`.

Si durante la transmisión se corrompen dos de los siete símbolos, el decodificador puede recuperar `f` y, por tanto, los tres símbolos originales del mensaje.

## Aplicaciones reales

### CD: RS(255, 223)

Los discos compactos usan un esquema CIRC (*Cross-Interleaved Reed-Solomon Coding*) con dos capas de Reed-Solomon sobre `GF(256)`:

- Capa exterior: `RS(32, 28)`, `d = 5`, corrige hasta 2 errores por bloque.
- Capa interior: `RS(28, 24)`, `d = 5`, ídem.
- El interleaving dispersa las ráfagas de errores producidas por rayones.

El estándar ECMA-130 define el equivalente efectivo `RS(255, 223)`: `n = 255` símbolos de 8 bits, `k = 223` datos, `d = 33`, `t = 16`. Una capa de corrección de errores de este tipo puede recuperar hasta 16 bytes erróneos por bloque de 255 bytes.

### Códigos QR

Los códigos QR (ISO/IEC 18004) usan Reed-Solomon sobre `GF(256)` en cuatro niveles de corrección:

| Nivel | Nombre | Corrección máxima |
|-------|--------|-------------------|
| L | Low | 7 % de codewords |
| M | Medium | 15 % |
| Q | Quartile | 25 % |
| H | High | 30 % |

En nivel H, un código QR de versión 40 usa bloques `RS(68, 14)` con `d = 55`, `t = 27`: puede recuperar hasta el 30 % de los módulos del símbolo, lo que permite imprimir logotipos encima del código y seguir leyéndolo.

### Almacenamiento: RAID y SSDs

Reed-Solomon se usa en sistemas RAID-6 (dos discos de paridad toleran dos fallos simultáneos) y en la capa FEC de unidades SSD de alta fiabilidad. El esquema estándar del almacenamiento distribuido es `RS(14, 10)`: 10 fragmentos de datos y 4 de paridad, tolerando la pérdida de cualquier 4 de los 14 fragmentos.

## Decodificación: algoritmo de Berlekamp-Massey

El decodificador clásico opera en tres pasos:

1. **Calcular síndromes** `S_i = r(α^i)` para `i = 1, …, n-k`, donde `r` es la palabra recibida.
2. **Localizar errores** con el algoritmo de Berlekamp-Massey (BM): encuentra el polinomio localizador de errores `Λ(x)` a partir de los síndromes en tiempo `O(t²) = O(n²)` en el peor caso.
3. **Corregir valores**: evaluar `Λ` en `GF(q)^*`, hallar las posiciones erróneas y resolver un sistema lineal pequeño para los valores.

La complejidad total del decodificador BM es `O(n²)`, dominada por el paso 2. Para `n = 255` esto supone del orden de `64000` operaciones en `GF(256)`, implementables en hardware a altas velocidades de transferencia con registros de desplazamiento de retroalimentación lineal (LFSR).

## Comparación con LDPC

Los **códigos LDPC** (artículo 11) trabajan sobre `GF(2)` con grafos Tanner dispersos y se decodifican con propagación de creencias (*belief propagation*), un algoritmo iterativo de complejidad `O(n)` por iteración. Reed-Solomon opera con símbolos de `m` bits y usa álgebra exacta.

| Característica | Reed-Solomon | LDPC |
|---------------|-------------|------|
| Año | 1960 | 1963 (redescubierto 1996) |
| Alfabeto | `GF(2^m)`, simbólico | `GF(2)`, binario |
| Distancia | MDS exacta | Sub-MDS, aleatorizada |
| Decodificador | Berlekamp-Massey, `O(n²)` | Belief propagation, `O(n)` iterativo |
| Régimen | Ráfagas de errores | Canal AWGN, capacidad |
| Aplicaciones | CD, QR, RAID | 5G, Wi-Fi, DVBT-2 |

En transmisión sobre canal AWGN a tasas próximas a la capacidad de Shannon, LDPC supera a RS. En corrección de ráfagas de errores en almacenamiento o en canales por bloques, RS mantiene ventajas gracias a su propiedad MDS y a su decodificador algebraico determinista.

## Ideas clave

- Los campos de Galois `GF(2^m)` proporcionan aritmética exacta de `m` bits donde todo elemento no nulo tiene inverso: el sustrato algebraico indispensable de RS.
- La cota de Singleton `d ≤ n - k + 1` es un límite absoluto; RS la alcanza, siendo MDS: ningún código puede corregir más errores con la misma redundancia.
- La capacidad de corrección `t = ⌊(d-1)/2⌋` surge de que dos palabras código distintas deben estar a distancia `> 2t` para que los discos de corrección no se solapen.
- RS(255, 223) sobre `GF(256)` es el caballo de batalla de almacenamiento desde los años 80: 32 bytes de paridad corrigen 16 bytes erróneos en 255, con decodificación hardware en nanosegundos.
- El decodificador de Berlekamp-Massey, de complejidad `O(n²)`, es el cuello de botella de RS frente a LDPC (`O(n)`), pero su corrección es exacta y determinista.

## Ejercicios

1. Construye la tabla de multiplicación de `GF(4) = 𝔽_2[x]/⟨ x²+x+1⟩` y verifica que todo elemento no nulo tiene inverso multiplicativo.
2. Para `RS(7,3)` sobre `GF(8)`, escoge el mensaje `(1, α, α²)` y computa la palabra código evaluando `f(x) = 1 + α x + α² x²` en `α⁰, …, α⁶`.
3. Demuestra que la distancia mínima de `RS(n, k)` es exactamente `n - k + 1` usando el hecho de que un polinomio de grado `k-1` tiene como máximo `k-1` raíces.
4. Un CD tiene un rayón que borra 2,5 mm de pista. Si la densidad lineal es 3 µm/bit y cada bloque de 255 bytes ocupa 765 µm, ¿cuántos bloques quedan parcialmente afectados? ¿Puede RS(255, 223) recuperarlos?
5. Compara `RS(255, 223)` y `RS(255, 191)`: ¿cuál tiene mayor capacidad de corrección? ¿Cuál tiene mayor tasa de información? Calcula `R = k/n` y `t` para ambos.
6. El algoritmo de Berlekamp-Massey construye el LFSR más corto que genera la secuencia de síndromes. Explica, en términos de grado del polinomio de conexión, por qué su complejidad es `O(t²)` y no `O(t)`.

## Referencias

- Reed, I. S. y Solomon, G. (1960). Polynomial codes over certain finite fields. *Journal of the Society for Industrial and Applied Mathematics*, 8(2), 300–304.
- Berlekamp, E. R. (1968). *Algebraic Coding Theory*. McGraw-Hill.
- MacWilliams, F. J. y Sloane, N. J. A. (1977). *The Theory of Error-Correcting Codes*. North-Holland.
- ISO/IEC 18004:2015. *Information technology — Automatic identification and data capture techniques — QR Code bar code symbology specification*.
- Lin, S. y Costello, D. J. (2004). *Error Control Coding*, 2.ª ed. Pearson Prentice Hall.

## Véase también

- [Códigos correctores de errores](06-codigos-correctores-de-errores.md)
- [Códigos LDPC y Turbo](11-codigos-ldpc-y-turbo.md)
- [Teorema de Shannon y capacidad](08-teorema-de-shannon-capacidad.md)
