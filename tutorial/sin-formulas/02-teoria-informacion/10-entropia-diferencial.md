> **Nota:** Esta es la versión sin fórmulas LaTeX de [10-entropia-diferencial](../../02-teoria-informacion/10-entropia-diferencial.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Entropía Diferencial y Fuentes Continuas

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min


## Prerrequisitos

- [Entropía e incertidumbre](01-entropia-incertidumbre.md)
- [Entropía conjunta y condicional](07-entropia-conjunta-y-condicional.md)

## Objetivos de aprendizaje

1. Definir la entropía diferencial h(X) para variables continuas.
2. Calcular h(X) para distribuciones gaussianas y uniformes.
3. Explicar por qué h(X) puede ser negativa y cómo difiere de H(X).


## Intuición

La entropía de Shannon se definió para variables aleatorias discretas. Las fuentes reales —audio,
temperatura, señales analógicas— son continuas. La **entropía diferencial** extiende la idea de
incertidumbre a distribuciones continuas, pero con diferencias importantes: puede ser negativa,
no está acotada inferiormente, y su interpretación requiere cuidado.

## Definición formal

Sea `X` una variable aleatoria continua con densidad `f(x)`. La **entropía diferencial** es:


> **Fórmula:** `h(X) = -∫_-∞^(∞) f(x) log f(x)  dx`


donde el logaritmo está en base 2 (bits) o en base `e` (nats).

**Diferencias respecto a la entropía discreta:**

| Propiedad | Discreta `H(X)` | Diferencial `h(X)` |
|-----------|----------------|---------------------|
| Rango | `[0, log|𝒳|]` | `(-∞, +∞)` |
| Invarianza | Bajo biyecciones | No: `h(aX) = h(X) + log|a|` |
| Significado | Bits necesarios para codificar | Límite de bits/símbolo al cuantizar |

## Ejemplos canónicos

### Distribución uniforme en `[0, a]`


> **Fórmula:** `f(x) = 1/a,  h(X) = log a`


Para `a < 1`, la entropía diferencial es negativa. No es una contradicción: refleja que la
distribución está más concentrada que una distribución uniforme en `[0,1]`.

### Distribución exponencial con parámetro `λ`


> **Fórmula:** `f(x) = λ e^(-λ x),  x ≥ 0,  h(X) = 1 - log λ  (nats)`


### Distribución Gaussiana `𝒩(μ, σ²)`


> **Fórmula:** `h(X) = 1/2 log(2π e σ²)`


La media no afecta a la entropía; solo importa la varianza.

## Máxima entropía para varianza fija

**Teorema.** Entre todas las distribuciones con media `μ` y varianza `σ²`, la distribución
Gaussiana `𝒩(μ, σ²)` **maximiza** la entropía diferencial.

**Demostración (esquema):** sea `g(x)` cualquier distribución con varianza `σ²`. Entonces:


> **Fórmula:** `h(g) - h(𝒩) = -∫ g log g + ∫ g log 𝒩 ≤ 0`


donde la desigualdad viene de que `D_KL(g ‖ 𝒩) ≥ 0`.

**Consecuencias prácticas:**
- El ruido Gaussiano es el más "destructivo" entre todos los ruidos de igual potencia.
- Justifica el teorema de Shannon-Hartley: la capacidad del canal Gaussiano `C = 1/2log(1+SNR)` se alcanza con señales Gaussianas.
- En aprendizaje automático, modelos que asumen Gaussiana son conservadores en el sentido de
  información: están haciendo la suposición de mínima información extra.

## Entropía diferencial y cuantización

La entropía diferencial surge naturalmente al cuantizar: si se discretiza `X` en intervalos de
tamaño `Δ`, la entropía de la variable discreta resultante satisface:


> **Fórmula:** `H(X_Δ) ≈ h(X) - log Δ`


Para `Δ → 0`, `H(X_Δ) → ∞`, pero la diferencia `H(X_Δ) - H(Y_Δ)`
converge a `h(X) - h(Y)`. Por esto la entropía diferencial es útil para comparar distribuciones
aunque su valor absoluto no tenga interpretación directa en bits.

## Información mutua diferencial

La información mutua es invariante bajo transformaciones biyectivas y tiene la misma interpretación
tanto en el caso discreto como en el continuo:


> **Fórmula:** `I(X;Y) = h(X) - h(X|Y) = h(Y) - h(Y|X)`


La información mutua diferencial es **siempre no negativa** y se anula si y solo si `X` e `Y`
son independientes. Es la cantidad que aparece en la capacidad de canal:


> **Fórmula:** `C = max_p(x) I(X;Y)`


## La desigualdad de potencia de entropía

**Entropy Power Inequality (EPI):** para variables independientes `X` e `Y`:


> **Fórmula:** `2^(2h(X+Y)/n) ≥ 2^(2h(X)/n) + 2^(2h(Y)/n)`


donde `n` es la dimensión. Para variables escalares:


> **Fórmula:** `e^(2h(X+Y)) ≥ e^(2h(X)) + e^(2h(Y))`


La igualdad se da si y solo si `X` e `Y` son Gaussianas con varianzas proporcionales.

**Interpretación:** la "potencia de entropía" `e^(2h(X))` se comporta como la varianza de una
Gaussiana de igual entropía. La EPI generaliza la ley de adición de varianzas al mundo de la entropía.

## Información de Fisher

La **información de Fisher** `J(X)` de una distribución con densidad `f(x; θ)` mide cuánta
información contiene una muestra sobre el parámetro `θ`:


> **Fórmula:** `J(θ) = 𝔼≤ft[≤ft(∂/(∂ θ) log f(X;θ))²]`


Para la familia de localización (`f(x;μ) = f(x-μ)`), la información de Fisher satisface la
**desigualdad de Cramér-Rao:** cualquier estimador insesgado `μ̂` satisface
`Var[μ̂] ≥ 1/J(μ)`.

**Relación con la entropía:** para la familia de localización gaussiana,
`J(μ) = 1/σ²` y `h(X) = 1/2log(2π e/J)`. La información de Fisher y la
entropía diferencial son conceptos complementarios: la entropía mide incertidumbre global
mientras que Fisher mide sensibilidad local a cambios del parámetro.

## Canal Gaussiano aditivo

El **canal Gaussiano aditivo** es el modelo estándar de comunicación analógica:


> **Fórmula:** `Y = X + Z,  Z ~ 𝒩(0, N),  𝔼[X²] ≤ P`


La capacidad es:

> **Fórmula:** `C = 1/2log≤ft(1 + P/N)  bits/uso`


La demostración usa que:
1. La señal óptima es `X ~ 𝒩(0, P)` (maximiza `h(X)`).
2. `h(Y) = h(X + Z) ≤ 1/2log(2π e(P+N))` con igualdad para `X` Gaussiana.
3. `h(Y|X) = h(Z) = 1/2log(2π eN)`.
4. `I(X;Y) = h(Y) - h(Y|X) = 1/2log(1 + P/N)`.

## AEP para fuentes continuas

El **teorema de equipartición asintótica** (AEP) tiene un análogo continuo: para una fuente
estacionaria ergódica continua, la probabilidad de la secuencia típica satisface:


> **Fórmula:** `-1/nlog f(X_1,…,X_n) → h(X)  en probabilidad`


Las secuencias típicas ocupan un volumen `≈ 2^(nh(X))` en `ℝ^n`, que crece
exponencialmente. Para representar `n` muestras con error de cuantización `ε`,
se necesitan `≈ n(h(X) + log(1/ε))` bits.

## Ideas clave

- La entropía diferencial `h(X) = -∫ flog f` puede ser negativa; su valor absoluto no
  tiene interpretación directa en bits, pero las diferencias sí.
- La Gaussiana maximiza la entropía entre distribuciones con varianza fija.
- La información mutua `I(X;Y) = h(X) - h(X|Y)` es siempre no negativa e invariante de
  escala.
- La EPI generaliza la adición de varianzas al dominio de la entropía.
- La capacidad del canal Gaussiano `C = 1/2log(1+P/N)` se obtiene directamente
  de la entropía diferencial de la Gaussiana.

## Ejercicios

1. Calcula `h(X)` para `X ~ Uniforme[0, 1]`, `X ~ Exponencial(2)` y
   `X ~ 𝒩(3, 4)`.
2. Demuestra que `h(aX+b) = h(X) + log|a|`. ¿Por qué esta fórmula tiene sentido intuitivo?
3. Muestra que `h(X, Y) ≤ h(X) + h(Y)` con igualdad si y solo si `X` e `Y` son independientes.
4. ¿Por qué la capacidad del canal Gaussiano depende solo del cociente `P/N` y no de `P` o
   `N` por separado?
5. La desigualdad de Cramér-Rao establece `Var[μ̂] ≥ 1/J(μ)`. Para una
   Gaussiana, ¿qué estimador alcanza esta cota?

## Véase también

- [Teoría de tasa-distorsión](09-teoria-tasa-distorsion.md)
- [Información y termodinámica](../05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md)


## Referencias

- Cover, T. y Thomas, J. (2006). *Elements of Information Theory*, 2ª ed., capítulos 8-9.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*.
- Stam, A. J. (1959). Some inequalities satisfied by the quantities of information of Fisher
  and Shannon. *Information and Control*.
