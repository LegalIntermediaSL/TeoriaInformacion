> **Nota:** Esta es la versión sin fórmulas LaTeX de [14-complejidad-cuantica-bqp-qma](../../04-complejidad-computacional/14-complejidad-cuantica-bqp-qma.md). Las expresiones matemáticas se muestran en texto plano y Unicode. Para la versión completa con renderizado de fórmulas, consulta el archivo original o el [sitio web del tutorial](https://legalintermediasl.github.io/TeoriaInformacion/).

---

# Complejidad cuántica: BQP y QMA

> **Dificultad:** ⭐⭐⭐ Avanzado · **Tiempo de lectura:** ~25 min

## Prerrequisitos

- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [Complejidad aleatoria](08-complejidad-aleatoria.md)
- [ETH, SETH y consecuencias](13-eth-seth-consecuencias.md)

## Objetivos de aprendizaje

1. Describir el modelo de cómputo cuántico (qubits, superposición, medición) en los términos mínimos necesarios para razonar sobre clases de complejidad.
2. Definir formalmente la clase BQP e identificar sus problemas completos y sus relaciones con P, BPP y la jerarquía polinomial.
3. Entender por qué los algoritmos de Shor (factorización) y Grover (búsqueda) colocan sus respectivos problemas en BQP y explicar sus ventajas asintóticas.
4. Definir QMA como el análogo cuántico de NP y enunciar el problema 5-local Hamiltonian como QMA-completo (Kitaev, 2002).
5. Discutir las implicaciones de BQP para la criptografía post-cuántica y las preguntas abiertas sobre la posición de BQP en la jerarquía de complejidad clásica.

---

## Intuición

La computación clásica procesa bits que en cada instante son 0 o 1. La computación cuántica procesa **qubits**, que pueden estar en superposición de ambos estados hasta que se miden. Las puertas cuánticas manipulan estas superposiciones de forma coherente, lo que permite que ciertos algoritmos exploten interferencias constructivas y destructivas para amplificar la probabilidad de la respuesta correcta.

La clase BQP (Bounded-error Quantum Polynomial time) captura lo que un ordenador cuántico puede resolver eficientemente. La clase QMA (Quantum Merlin-Arthur) captura lo que puede *verificarse* eficientemente con un certificado cuántico.

## El modelo: qubits, puertas y medición

Un **qubit** es un vector unitario en `ℂ²`:


> **Fórmula:** `|ψ⟩ = α|0⟩ + β|1⟩,  |α|² + |β|² = 1.`


Un registro de `n` qubits vive en `ℂ^(2^n)`; su estado es una superposición de los `2^n` estados de la base computacional `\{|0…0⟩, …, |1…1⟩\}`.

Una **puerta cuántica** sobre `k` qubits es una transformación unitaria `U ∈ U(2^k)`. Las puertas universales más usadas son Hadamard (`H`), CNOT y T. Un **circuito cuántico** compone `poly(n)` puertas de una rejilla finita universal.

La **medición** en la base computacional colapsa `|ψ⟩` al estado `|x⟩` con probabilidad `|⟨ x|ψ⟩|²`. Dado que la medición destruye la superposición, los algoritmos cuánticos deben diseñarse para que la respuesta correcta tenga alta probabilidad de amplitud al final del cómputo.

## La clase BQP

**Definición.** Un lenguaje `L` está en **BQP** (Bounded-error Quantum Polynomial time) si existe una familia uniforme de circuitos cuánticos `\{C_n\}` de tamaño `poly(n)` tal que:

- Si `x ∈ L`: `\Pr[salida(C_|x||x⟩) = 1] ≥ 2/3`.
- Si `x ∉ L`: `\Pr[salida(C_|x||x⟩) = 1] ≤ 1/3`.

La constante `1/3` es arbitraria: el error se puede reducir exponencialmente repitiendo el circuito `O(log 1/δ)` veces (amplificación de mayoría, igual que en BPP).

### Relaciones conocidas


> **Fórmula:** `P ⊆ BPP ⊆ BQP ⊆ PSPACE.`


Se sabe que `BQP ⊆ PP` (Adleman, DeMarrais, Huang, 1997) y por tanto `BQP ⊆ PSPACE`. No se conoce si `BQP ⊆ PH` (la jerarquía polinomial); se conjetura que no, y el oráculo de Raz-Tal (2019) provee evidencia relativa: existe un oráculo respecto al cual `BQP \not⊆ PH`.

No se sabe si `P = BQP` o `BPP = BQP`; es decir, si los computadores cuánticos son más poderosos que los clásicos para problemas de decisión sigue siendo una pregunta abierta.

## Algoritmo de Shor: factorización en BQP

El problema de **factorización** (FACTORING): dado `N` en binario, ¿tiene `N` un factor propio? Está en NP `∩` co-NP, pero no se conoce ningún algoritmo polinomial clásico.

**Shor (1994)** mostró que FACTORING `∈` BQP. El núcleo es la reducción de factorización a **encontrar el orden** de un elemento `a` en `ℤ_N^*`: el menor `r` tal que `a^r ≡ 1 ±od{N}`.

La **Transformada Cuántica de Fourier** (QFT) sobre `ℤ_2^m` es:


> **Fórmula:** `|j⟩ \longmapsto \frac{1}{√(2^m)} Σ_k=0^(2^m-1) e^(2π i jk / 2^m) |k⟩.`


Implementada en `O(m²)` puertas (frente a `O(m 2^m)` de la FFT clásica), la QFT extrae el período `r` de la función `f(x) = a^x \bmod N` con alta probabilidad mediante estimación de fase. La factorización completa de `N` tiene bits tarda `O(log³ N)` pasos cuánticos y `O(log² N)` pasos clásicos adicionales.

**Implicación criptográfica:** RSA, Diffie-Hellman y la criptografía de curva elíptica basan su seguridad en la dificultad de factorizar o calcular logaritmos discretos. Un computador cuántico con `~ 4000` qubits lógicos libre de ruido rompería RSA-2048 usando el algoritmo de Shor.

## Algoritmo de Grover: búsqueda cuadráticamente más rápida

Dado un oráculo `f: \{0,1\}^n → \{0,1\}` que evalúa si `x` es solución, el problema de búsqueda sin estructura requiere `Θ(2^n)` consultas clásicamente.

**Grover (1996):** el algoritmo de amplitud de Grover encuentra una solución con alta probabilidad en `O(√(2^n))` consultas cuánticas al oráculo. La aceleración cuadrática es **óptima**: ningún algoritmo cuántico puede hacerlo mejor para búsqueda no estructurada (Bennett et al., 1997).

El algoritmo aplica iterativamente el operador de Grover:


> **Fórmula:** `G = H^(⊗ n)(2|0⟩⟨ 0| - I)H^(⊗ n) · O_f,`


donde `O_f|x⟩ = (-1)^(f(x))|x⟩` es el oráculo de fase. Tras `O(√(N))` iteraciones, la amplitud del estado solución se aproxima a 1.

**Consecuencias para NP:** Grover no coloca NP en BQP. Una búsqueda en un espacio de `2^n` estados requiere `O(2^(n/2))` consultas cuánticas, que sigue siendo exponencial en `n`.

## La clase QMA: el NP cuántico

La clase **NP** permite que un verificador clásico compruebe en tiempo polinomial un certificado clásico. **QMA** generaliza esto a certificados cuánticos y verificadores cuánticos.

**Definición.** Un lenguaje `L` está en **QMA** (Quantum Merlin-Arthur) si existe un verificador cuántico `V` (circuito cuántico polinomial) tal que:

- Si `x ∈ L`: existe un estado cuántico `|ψ⟩` de `poly(|x|)` qubits tal que `\Pr[V  acepta  (x, |ψ⟩)] ≥ 2/3`.
- Si `x ∉ L`: para todo estado `|ψ⟩`, `\Pr[V  acepta  (x, |ψ⟩)] ≤ 1/3`.

De forma análoga a NP `⊆` QMA (todo certificado clásico es un estado cuántico en la base computacional):


> **Fórmula:** `NP ⊆ QMA ⊆ PP.`


No se sabe si `NP = QMA` o si `QMA ⊆ NP`.

## El problema Local Hamiltonian: QMA-completitud

**Kitaev (2002)** demostró el primer resultado de QMA-completitud, el análogo cuántico del teorema de Cook-Levin.

**Definición.** Un **`k`-local Hamiltonian** es un operador hermítico `H = Σ_i H_i` sobre `n` qubits, donde cada `H_i` actúa de forma no trivial sobre a lo sumo `k` qubits y `‖H_i‖ ≤ 1`.

**Problema `k`-LOCAL HAMILTONIAN:** dados `H` y constantes `a < b` con `b - a ≥ 1/poly(n)`, determinar si el valor propio mínimo de `H` (energía del estado fundamental) es `≤ a` o `≥ b`.

**Teorema de Kitaev (2002):** `5`-LOCAL HAMILTONIAN es QMA-completo. Watrous y otros redujeron el parámetro; hoy se sabe que `2`-LOCAL HAMILTONIAN ya es QMA-completo (Kempe, Kitaev, Regev, 2006).

**Relevancia física:** determinar la energía del estado fundamental de un Hamiltoniano local es el problema central de la física cuántica de la materia condensada y de la química cuántica. La QMA-completitud sugiere que este problema es intrínsecamente difícil incluso para un computador cuántico.

## Diagrama de inclusiones


> **Fórmula:** `P ⊆ BPP ⊆ BQP`


> **Fórmula:** `P ⊆ NP ⊆ QMA ⊆ PP ⊆ PSPACE`


> **Fórmula:** `BQP ⊆ PP ⊆ PSPACE`


La posición relativa de BQP y NP es desconocida: no se sabe si NP `⊆` BQP (lo que significaría que un computador cuántico resuelve NP eficientemente) ni si BQP `⊆` NP.

## Preguntas abiertas

1. **¿`BQP ⊆ PH`?** La conjetura dominante es que no: el oráculo de Raz-Tal (2019) separa BQP de PH de forma relativa. Probar la separación incondicional requeriría separar P de PSPACE.
2. **¿`NP ⊆ BQP`?** Si fuera cierto, Grover no sería óptimo para NP en el modelo de oráculo. Se cree que la respuesta es no.
3. **¿`BQP = BPP`?** Si fuera cierto, los computadores cuánticos no ofrecerían ventaja superpolinomial. Grover ya muestra una separación en el modelo de oráculo.
4. **QMA vs. QCMA:** ¿puede el certificado cuántico en QMA reemplazarse por uno clásico sin pérdida de poder? QCMA (certificado clásico, verificador cuántico) se cree estrictamente más débil que QMA, pero no se ha probado.

## Implicaciones para la criptografía post-cuántica

Dado que Shor implica que RSA, DSA y ECDSA son vulnerables a ataques cuánticos en tiempo polinomial, el NIST ha estandarizado (2024) esquemas basados en problemas presumiblemente difíciles para BQP:

- **CRYSTALS-Kyber** (ML-KEM): basado en el problema de vectores cortos en retículos (Learning With Errors, LWE).
- **CRYSTALS-Dilithium** (ML-DSA) y **FALCON**: firmas digitales en retículos.
- **SPHINCS+**: firmas basadas en funciones hash.

La dureza de LWE frente a computadores cuánticos se sustenta en reducciones de peor caso desde el problema del vector más corto en retículos (SVP), cuya mejor solución cuántica conocida requiere tiempo superpolinomial.

## Ideas clave

- BQP es la clase de los problemas decidibles eficientemente por un computador cuántico con error acotado; satisface `P ⊆ BPP ⊆ BQP ⊆ PSPACE`, pero su posición exacta en la jerarquía clásica es desconocida.
- El algoritmo de Shor pone la factorización en BQP mediante la QFT en `O(log³ n)` pasos, lo que quebraría la criptografía de clave pública clásica con hardware cuántico suficiente.
- Grover ofrece aceleración cuadrática `O(√(N))` para búsqueda no estructurada, pero esta aceleración es óptima y no coloca NP en BQP.
- QMA es el análogo cuántico de NP: el verificador y el certificado son cuánticos; satisface `NP ⊆ QMA ⊆ PP`.
- El problema `k`-local Hamiltonian es QMA-completo (Kitaev, 2002), lo que sugiere que calcular la energía del estado fundamental de sistemas cuánticos locales es difícil incluso cuánticamente.

## Ejercicios

1. Verifica que la QFT sobre `ℤ_4` (2 qubits) es unitaria escribiendo explícitamente la matriz `4 × 4` y comprobando que las columnas son ortonormales.
2. El algoritmo de Grover para `N = 1024` elementos requiere `O(√(N)) ≈ 32` iteraciones. ¿Cuántas iteraciones exactas maximizan la probabilidad de éxito? (Pista: la amplitud del estado solución sigue una función `\sin²`.)
3. Define formalmente el problema de decisión FACTORING y muestra que pertenece a NP `∩` co-NP. ¿Implica que está en BPP? ¿En BQP?
4. Explica por qué `2`-LOCAL HAMILTONIAN es QMA-completo pero `1`-LOCAL HAMILTONIAN no lo es. ¿Qué propiedad del caso `k=1` permite resolverlo eficientemente?
5. Considera el esquema ML-KEM (CRYSTALS-Kyber). El parámetro de seguridad es `q = 3329`, `n = 256`. ¿Cómo afectaría un hipotético algoritmo cuántico para LWE en tiempo `O(2^(n/2))` a la seguridad de nivel 1 (equivalente a AES-128)?
6. El oráculo de Raz-Tal (2019) separa BQP de PH relativamente. ¿Qué implica esta separación sobre la posibilidad de demostrar `BQP ⊆ PH` de forma incondicional con las técnicas actuales?

## Referencias

- Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM Journal on Computing*, 26(5), 1484–1509.
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *STOC 1996*, 212–219.
- Kitaev, A. Y., Shen, A. H. y Vyalyi, M. N. (2002). *Classical and Quantum Computation*. AMS.
- Kempe, J., Kitaev, A. y Regev, O. (2006). The complexity of the local Hamiltonian problem. *SIAM Journal on Computing*, 35(5), 1070–1097.
- Raz, R. y Tal, A. (2019). Oracle separation of BQP and PH. *STOC 2019*, 13–23.
- NIST (2024). *FIPS 203, 204, 205: Post-Quantum Cryptographic Standards*. NIST.
- Nielsen, M. A. y Chuang, I. L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press.

## Véase también

- [Complejidad aleatoria: BPP y RP](08-complejidad-aleatoria.md)
- [P, NP y NP-completitud](01-p-np-y-np-completitud.md)
- [ETH, SETH y consecuencias](13-eth-seth-consecuencias.md)
