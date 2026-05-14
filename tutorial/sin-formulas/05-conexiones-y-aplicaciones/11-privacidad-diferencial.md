> **Nota:** Esta es la versión sin fórmulas LaTeX de [11-privacidad-diferencial](../../05-conexiones-y-aplicaciones/11-privacidad-diferencial.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Privacidad Diferencial

> **Dificultad:** ⭐⭐ Intermedio · **Tiempo de lectura:** ~20 min


## Prerrequisitos

- [Divergencia KL y divergencias de información](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Criptografía y complejidad](02-criptografia-y-complejidad.md)
- [Entropía de Shannon](../02-teoria-informacion/01-entropia-incertidumbre.md)

## Objetivos de aprendizaje

1. Definir formalmente la `ε`-privacidad diferencial y entender su significado probabilístico.
2. Describir los mecanismos de Laplace y gaussiano y calcular el ruido necesario.
3. Relacionar la privacidad diferencial con la divergencia de Rényi.
4. Analizar el trade-off privacidad-precisión y las técnicas de amplificación.
5. Distinguir privacidad diferencial de anonimización clásica.


## Intuición

La anonimización clásica (eliminar el nombre de un registro) no protege la privacidad: en 2006,
Narayanan y Shmatikoff reidentificaron usuarios del dataset de Netflix cruzándolo con IMDb.
La **privacidad diferencial** (Dwork, 2006) ofrece una garantía matemática mucho más fuerte:
el resultado de una consulta sobre una base de datos es casi indistinguible si un individuo
concreto está o no está en ella. La cantidad `ε` mide exactamente cuánta indistinguibilidad
se garantiza, en unidades de nats o bits de información sobre la presencia del individuo.

## Definición formal

### `ε`-privacidad diferencial

Un mecanismo aleatorio `ℳ: \mathcal{D} → \mathcal{R}` satisface
**`ε`-privacidad diferencial** si para todo par de bases de datos adyacentes
`D, D' ∈ \mathcal{D}` (que difieren en exactamente un registro) y todo subconjunto de
salidas `S ⊆ \mathcal{R}`:


> **Fórmula:** `\Pr[ℳ(D) ∈ S] ≤ e^ε · \Pr[ℳ(D') ∈ S]`


La adyacencia puede definirse por inserción/eliminación de un individuo o por cambio de
un registro. El parámetro `ε > 0` controla la privacidad: `ε = 0` es
privacidad perfecta (salida independiente de los datos), `ε` grande permite
revelar más información.

### `(ε, δ)`-privacidad diferencial

La variante con `δ > 0` relaja la garantía: permite que la condición falle con
probabilidad pequeña `δ`, lo que admite mecanismos gaussianos más eficientes:


> **Fórmula:** `\Pr[ℳ(D) ∈ S] ≤ e^ε · \Pr[ℳ(D') ∈ S] + δ`


## Mecanismos fundamentales

### Mecanismo de Laplace

Para una consulta numérica `f: \mathcal{D} → ℝ` con **sensibilidad global**
`Δ f = max_D, D' ‖f(D) - f(D')‖_1`, el mecanismo de Laplace añade ruido:


> **Fórmula:** `ℳ(D) = f(D) + Lap≤ft((Δ f)/ε)`


donde `Lap(λ)` es la distribución de Laplace con escala `λ` y densidad
`p(x) = 1/2λ e^(-|x|/λ)`. Este mecanismo es `ε`-diferencial-privado.

**Ejemplo:** contar cuántos usuarios tienen más de 30 años. `Δ f = 1` (añadir un usuario
cambia el conteo en 1). Con `ε = 1`, se añade ruido `Lap(1)` con desviación
estándar `√(2) ≈ 1.41`.

### Mecanismo gaussiano

Para `(ε, δ)`-privacidad diferencial, el mecanismo gaussiano añade:


> **Fórmula:** `ℳ(D) = f(D) + 𝒩≤ft(0, σ²),  σ = \frac{Δ_2 f · √(2 ln(1.25/δ))}{ε}`


donde `Δ_2 f` es la sensibilidad `\ell_2`. Para `δ` pequeño, el mecanismo gaussiano
requiere menos ruido que el de Laplace en consultas vectoriales de alta dimensión.

## Composición y degradación

Si se realizan `k` consultas independientes con `ε`-privacidad diferencial cada una,
el mecanismo compuesto satisface **`kε`-privacidad diferencial** (composición básica):


> **Fórmula:** `ε_total = Σ_i=1^k ε_i = k ε`


La composición avanzada (Dwork et al., 2010) da una cota mejor con `δ' > 0`:


> **Fórmula:** `ε_total ≈ √(2k ln(1/δ')) · ε + kε(e^ε - 1)`


Esto explica por qué el presupuesto de privacidad se "gasta" con cada consulta y hay que
gestionarlo cuidadosamente.

## Conexión con la divergencia de Rényi

La **divergencia de Rényi de orden `α`** es `D_α(P ‖ Q) = 1/(α-1) log Σ_x P(x)^α Q(x)^(1-α)`.

Si `ℳ` es `ε`-diferencial-privado, entonces para `α > 1`:


> **Fórmula:** `D_α(ℳ(D) ‖ ℳ(D')) ≤ ε · α`


Esta conexión es la base de la **privacidad Rényi diferencial** (Mironov, 2017), que permite
composición más precisa: en lugar de sumar `ε`, se suman las divergencias de Rényi
y se convierte al final al formato `(ε, δ)` estándar.

## Privacidad diferencial local vs central

En el **modelo central**, existe un curador de confianza que recibe los datos sin ruido y
aplica el mecanismo. En el **modelo local** (LDP), cada individuo aplica el mecanismo a sus
propios datos antes de enviarlos:


> **Fórmula:** `\Pr[ℳ(x) ∈ S] ≤ e^ε · \Pr[ℳ(x') ∈ S]  ∀ x, x'`


LDP no requiere curador de confianza, pero necesita más ruido para la misma precisión:
para estimar una media con error `± α`, el modelo central requiere `O(1/α²)`
usuarios mientras que LDP requiere `O(e^(2ε)/α²)` usuarios.

**Aplicaciones reales:** Google RAPPOR (Chrome, estadísticas de uso), Apple (iOS: frecuencia
de emojis, sugerencias de teclado), US Census Bureau (Census 2020).

## Amplificación por muestreo

Si el mecanismo `ℳ` es `ε`-diferencial-privado y se aplica a una submuestra
aleatoria de fracción `q` de la base de datos, el mecanismo amplificado es
`(O(qε), qδ)`-diferencial-privado (**amplificación por muestreo**):


> **Fórmula:** `ε_amplificado ≤ log(1 + q(e^ε - 1)) ≈ qε  (ε  pequeño)`


Esto explica por qué el SGD diferencial-privado (DP-SGD, Abadi et al., 2016) puede entrenar
redes neuronales con presupuesto razonable: en cada iteración solo se usa un mini-batch.

## Trade-off privacidad-precisión

Para estimar una media en `[0,1]` con `m` usuarios:

| Mecanismo | Error cuadrático medio |
|-----------|----------------------|
| Sin privacidad | `O(1/m)` |
| Laplace (central) | `O(1/m + Δ²/ε² m)` |
| LDP (aleatorización) | `O(e^(2ε)/m)` |

Para `ε < 1`, LDP es prácticamente inútil con menos de `10⁶` usuarios — este es
el régimen habitual en despliegues industriales. La curva de trade-off es el límite fundamental:
no existe mecanismo que mejore simultáneamente privacidad y precisión.

## Anonimización vs privacidad diferencial

La **anonimización** (eliminación de identificadores, `k`-anonimato) no da garantías
computacionales: un adversario con datos auxiliares puede reidentificar individuos.
La privacidad diferencial garantiza que incluso un adversario con poder de cómputo ilimitado
y conocimiento auxiliario completo aprende muy poco sobre la presencia de un individuo concreto.
La diferencia clave es que la privacidad diferencial es una propiedad del **mecanismo**,
no de los datos publicados.

## Ideas clave

- La `ε`-privacidad diferencial garantiza que la probabilidad de cualquier salida
  no cambia más de un factor `e^ε` si un individuo está o no en la base de datos.
- El mecanismo de Laplace añade ruido proporcional a la sensibilidad dividida por `ε`;
  el mecanismo gaussiano es preferible en alta dimensión bajo `(ε,δ)`-DP.
- La composición básica degrada la privacidad linealmente con el número de consultas:
  `k` consultas cuestan `kε`. La composición avanzada y Rényi DP mejoran esta cota.
- La privacidad diferencial local elimina la necesidad de un curador de confianza pero a
  costa de un factor `e^ε` en la varianza del estimador.
- La anonimización clásica no ofrece garantías ante ataques de reidentificación con datos
  auxiliares; la privacidad diferencial es robusta por construcción.

## Ejercicios

1. Calcula el ruido de Laplace necesario para responder con `ε = 0.5` a la consulta
   "¿cuántos usuarios tienen ingresos superiores a 50 000 €?" en una base de datos de 1000 personas.
2. Comprueba que el mecanismo de Laplace satisface `ε`-DP calculando el cociente de
   densidades `p(y | D) / p(y | D')` para dos bases de datos adyacentes.
3. Si realizas 100 consultas con `ε = 0.01` cada una, ¿cuál es el `ε` total
   con composición básica? ¿Y con amplificación por muestreo con `q = 0.01`?
4. Deriva la cota de la divergencia de Rényi de orden 2 para el mecanismo gaussiano con
   parámetros `σ` y sensibilidad `Δ_2 f = 1`.
5. Diseña un protocolo LDP para estimar la fracción de usuarios que usan contraseñas débiles,
   con `ε = 2` y error máximo de `± 0.05`. ¿Cuántos usuarios necesitas?
6. Explica intuitivamente por qué la amplificación por muestreo mejora la privacidad: si un
   individuo no está en el mini-batch, ¿qué aprende el adversario de esa iteración?

## Véase también

- [Divergencia KL y divergencias de información](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md)
- [Criptografía y complejidad](02-criptografia-y-complejidad.md)
- [Aprendizaje profundo desde la información](10-aprendizaje-profundo-desde-la-informacion.md)
- [Teoría de juegos e información asimétrica](09-teoria-de-juegos-e-informacion.md)

## Referencias

- Dwork, C. et al. (2006). Calibrating noise to sensitivity in private data analysis. *TCC 2006*, LNCS 3876, 265–284.
- Dwork, C. y Roth, A. (2014). *The Algorithmic Foundations of Differential Privacy*. Foundations and Trends in TCS.
- Mironov, I. (2017). Rényi differential privacy. *IEEE CSF 2017*.
- Abadi, M. et al. (2016). Deep learning with differential privacy. *ACM CCS 2016*.
- Erlingsson, Ú. et al. (2014). RAPPOR: Randomized aggregatable privacy-preserving ordinal response. *ACM CCS 2014*.
