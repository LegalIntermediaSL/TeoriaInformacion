# 27 - Información cuántica

## Contexto

Este ejercicio acompaña el artículo
[Información cuántica](../../05-conexiones-y-aplicaciones/04-informacion-cuantica.md).

## Enunciado

**Parte A — Qubits y puertas:**

1. El qubit $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ con $\alpha = 1/\sqrt{2}$,
   $\beta = 1/\sqrt{2}$. ¿Cuáles son las probabilidades de medir 0 y 1? ¿Qué estado
   queda después de la medición?

2. Aplica la puerta de Hadamard $H$ al estado $|0\rangle$ y luego al resultado.
   $$H = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\\1 & -1\end{pmatrix}$$

3. El estado de dos qubits es $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$.
   - ¿Es este estado separable (producto tensorial)? Justifica.
   - Si se mide el primer qubit y da 0, ¿en qué estado queda el segundo?

**Parte B — Entropía de Von Neumann:**

4. Calcula $S(\rho)$ para:
   - (a) Estado puro $|\psi\rangle = |0\rangle$: matriz densidad $\rho = |0\rangle\langle 0|$.
   - (b) Mezcla clásica $\rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|$.

## Pista

**Medición:** $P(\text{resultado} = k) = |\langle k|\psi\rangle|^2$. Tras medir $k$,
el estado colapsa a $|k\rangle$.

**Separabilidad:** $|\psi\rangle = |\phi_A\rangle \otimes |\phi_B\rangle$. Un estado
entrelazado no se puede escribir así.

**Von Neumann:** $S(\rho) = -\text{tr}(\rho \log_2 \rho) = -\sum_i \lambda_i \log_2 \lambda_i$
donde $\lambda_i$ son los valores propios de $\rho$.

## Solución

### Parte A — Qubits y puertas

#### 1. Medición del qubit $|\psi\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$

Probabilidades:

$$P(\text{medir } 0) = |\alpha|^2 = \left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}$$

$$P(\text{medir } 1) = |\beta|^2 = \left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}$$

**Tras la medición:**
- Si el resultado es 0: el estado colapsa a $|0\rangle$.
- Si el resultado es 1: el estado colapsa a $|1\rangle$.

La superposición se destruye irreversiblemente al medir. El estado $|\psi\rangle$
antes de la medición es una superposición de ambos resultados con igual peso.

#### 2. Hadamard aplicada dos veces

**Primera aplicación:** $H|0\rangle$

$$H|0\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\\1 & -1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{|0\rangle + |1\rangle}{\sqrt{2}} = |+\rangle$$

**Segunda aplicación:** $H|+\rangle = H(H|0\rangle)$

$$H|+\rangle = H \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1+1\\1-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2\\0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix} = |0\rangle$$

**$H$ es su propia inversa:** $H^2 = I$. Aplicar Hadamard dos veces devuelve
el estado original. Esto se debe a que $H$ es una puerta unitaria y hermítica
($H^\dagger = H$), luego $H^2 = H H^\dagger = I$.

#### 3. Estado de Bell $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$

**¿Es separable?**

Supón que $|\Phi^+\rangle = |\phi_A\rangle \otimes |\phi_B\rangle = (\alpha|0\rangle + \beta|1\rangle) \otimes (\gamma|0\rangle + \delta|1\rangle)$.

Expandiendo: $\alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle$.

Comparando con $\frac{1}{\sqrt{2}}|00\rangle + 0|01\rangle + 0|10\rangle + \frac{1}{\sqrt{2}}|11\rangle$:

```text
αγ = 1/√2,  αδ = 0,  βγ = 0,  βδ = 1/√2
```

De $\alpha\delta = 0$: $\alpha = 0$ o $\delta = 0$.
- Si $\alpha = 0$: entonces $\alpha\gamma = 0 \neq 1/\sqrt{2}$. Contradicción.
- Si $\delta = 0$: entonces $\beta\delta = 0 \neq 1/\sqrt{2}$. Contradicción.

**$|\Phi^+\rangle$ no es separable.** Es un estado **entrelazado**. ∎

**Tras medir el primer qubit y obtener 0:**

El estado $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B)$.

Al medir el qubit $A$ y obtener $0$, el estado colapsa a la parte proporcional a
$|0\rangle_A$:

$$|\psi\text{ tras medición}\rangle = |0\rangle_A \otimes |0\rangle_B$$

**El segundo qubit queda en el estado $|0\rangle$**, con probabilidad 1 dada la
medición del primero.

**Entrelazamiento:** aunque los qubits podían estar separados espacialmente, la
medición de uno determina instantáneamente el estado del otro. Este es el fenómeno
del entrelazamiento cuántico (EPR, 1935).

### Parte B — Entropía de Von Neumann

#### 4. (a) Estado puro $\rho = |0\rangle\langle 0|$

$$\rho = \begin{pmatrix}1 & 0\\0 & 0\end{pmatrix}$$

Valores propios: $\lambda_1 = 1$, $\lambda_2 = 0$.

$$S(\rho) = -\sum_i \lambda_i \log_2 \lambda_i = -(1 \cdot \log_2 1 + 0 \cdot \log_2 0)$$

Usando $0 \cdot \log_2 0 = 0$ por continuidad:

$$S(\rho) = -(1 \cdot 0 + 0) = 0 \text{ bits}$$

**Los estados puros tienen entropía cero.** No hay incertidumbre cuántica sobre
el estado: está perfectamente especificado. La incertidumbre en la medición
no es falta de conocimiento del estado, sino una propiedad intrínseca.

#### 4. (b) Mezcla clásica $\rho = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|$

$$\rho = \frac{1}{2}\begin{pmatrix}1 & 0\\0 & 0\end{pmatrix} + \frac{1}{2}\begin{pmatrix}0 & 0\\0 & 1\end{pmatrix} = \begin{pmatrix}1/2 & 0\\0 & 1/2\end{pmatrix}$$

Valores propios: $\lambda_1 = \lambda_2 = 1/2$.

$$S(\rho) = -2 \cdot \frac{1}{2}\log_2\frac{1}{2} = -2 \cdot \frac{1}{2} \cdot (-1) = 1 \text{ bit}$$

**Máxima entropía para un qubit.** Este estado es la mezcla completamente aleatoria:
no hay preferencia por ningún estado de base. Es el análogo cuántico de la distribución
uniforme $\{1/2, 1/2\}$, cuya entropía de Shannon también es 1 bit.

## Comentario

La entropía de Von Neumann tiene propiedades análogas a la entropía de Shannon:
subaditividad $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$, con igualdad para estados
de producto; y la propiedad notable de que un estado entrelazado puede tener entropía
máxima subsistema ($S(\rho_A) = 1$) aunque el estado conjunto sea puro ($S(\rho_{AB}) = 0$).
Esto no tiene análogo clásico y es una de las características más sorprendentes del
mundo cuántico.

## Para seguir

El **canal cuántico de borrado** borra el estado de un qubit con probabilidad $\epsilon$
(lo reemplaza por un estado ortogonal conocido). La capacidad cuántica de este canal
es $C_Q = (1 - 2\epsilon)$ qubits/uso. Compara con la capacidad del canal de borrado
clásico $C = 1 - \epsilon$ bits/uso. ¿Por qué la capacidad cuántica cae más rápido?
