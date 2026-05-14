# Índice de notación matemática

Tabla de todos los símbolos utilizados en el tutorial, con su definición y referencia al artículo donde se introduce.

---

## Teoría de la información

| Símbolo | Nombre | Definición | Artículo |
|---------|--------|-----------|---------|
| $H(X)$ | Entropía de Shannon | $-\sum_x P(x)\log_2 P(x)$ | [01](../02-teoria-informacion/01-entropia-incertidumbre.md) |
| $H(X,Y)$ | Entropía conjunta | $H(X) + H(Y\|X)$ | [07](../02-teoria-informacion/07-entropia-conjunta-y-condicional.md) |
| $H(Y\|X)$ | Entropía condicional | $\sum_x P(x)H(Y\|X=x)$ | [07](../02-teoria-informacion/07-entropia-conjunta-y-condicional.md) |
| $h(X)$ | Entropía diferencial | $-\int f(x)\log_2 f(x)\,dx$ | [10](../02-teoria-informacion/10-entropia-diferencial.md) |
| $\bar{H}$ | Tasa de entropía | $\lim_{n\to\infty}\frac{1}{n}H(X_1,\ldots,X_n)$ | [12](../02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md) |
| $I(X;Y)$ | Información mutua | $H(X)+H(Y)-H(X,Y)$ | [02](../02-teoria-informacion/02-informacion-mutua.md) |
| $I(X;Y\|Z)$ | Inf. mutua condicional | $H(X\|Z)-H(X\|Y,Z)$ | [07](../02-teoria-informacion/07-entropia-conjunta-y-condicional.md) |
| $D_\text{KL}(P\|Q)$ | Divergencia KL | $\sum_x P(x)\log_2\frac{P(x)}{Q(x)}$ | [05](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md) |
| $H_\times(P,Q)$ | Entropía cruzada | $-\sum_x P(x)\log_2 Q(x)$ | [05](../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md) |
| $C$ | Capacidad del canal | $\max_{p(x)} I(X;Y)$ | [04](../02-teoria-informacion/04-canales-discretos-y-capacidad.md) |
| $R(D)$ | Función tasa-distorsión | $\min_{p(\hat{x}\|x):\mathbb{E}[d]\leq D} I(X;\hat{X})$ | [09](../02-teoria-informacion/09-teoria-tasa-distorsion.md) |
| $H_\alpha(X)$ | Entropía de Rényi | $\frac{1}{1-\alpha}\log_2\sum_x P(x)^\alpha$ | [04](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md) |

---

## Complejidad de Kolmogorov y aleatoriedad

| Símbolo | Nombre | Definición | Artículo |
|---------|--------|-----------|---------|
| $K(x)$ | Complejidad de Kolmogorov | $\min_{p:U(p)=x}\|p\|$ | [01](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md) |
| $K(x\|y)$ | Complejidad condicional | $\min_{p:U(p,y)=x}\|p\|$ | [01](../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md) |
| $\Omega$ | Número de Chaitin | $\sum_{p\text{ para}}2^{-\|p\|}$ | [12](../03-computabilidad/12-aleatoriedad-algoritmica.md) |

---

## Computabilidad y lenguajes

| Símbolo | Nombre | Descripción | Artículo |
|---------|--------|-------------|---------|
| $\Sigma$ | Alfabeto | Conjunto finito de símbolos | [05](../03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md) |
| $\Sigma^*$ | Clausura de Kleene | Conjunto de todas las cadenas sobre $\Sigma$ | [05](../03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md) |
| $L(M)$ | Lenguaje de $M$ | Conjunto de cadenas aceptadas por la MT $M$ | [04](../03-computabilidad/04-maquinas-de-turing.md) |
| $\varepsilon$ | Cadena vacía | Cadena de longitud 0 | [05](../03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md) |
| $\leq_m$ | Reducción muchos-a-uno | $A \leq_m B$: $A$ se reduce a $B$ | [03](../03-computabilidad/03-reducciones-e-indecidibilidad.md) |
| $\emptyset'$ | Oráculo de salto | $\{e : \phi_e(e)\!\downarrow\}$; completo para $\Sigma_1^0$ | [10](../03-computabilidad/10-jerarquia-aritmetica.md) |
| $\Sigma_k^0, \Pi_k^0$ | Jerarquía aritmética | Niveles de complejidad aritmética | [10](../03-computabilidad/10-jerarquia-aritmetica.md) |

---

## Complejidad computacional

| Símbolo | Nombre | Descripción | Artículo |
|---------|--------|-------------|---------|
| $P$ | Tiempo polinomial | Decidibles en tiempo $n^{O(1)}$ | [01](../04-complejidad-computacional/01-p-np-y-np-completitud.md) |
| $NP$ | No determinista polinomial | Verificables en tiempo polinomial | [01](../04-complejidad-computacional/01-p-np-y-np-completitud.md) |
| $\text{co-}NP$ | Complemento de NP | $L \in \text{co-}NP \Leftrightarrow \overline{L} \in NP$ | [01](../04-complejidad-computacional/01-p-np-y-np-completitud.md) |
| $PSPACE$ | Espacio polinomial | Decidibles con espacio $n^{O(1)}$ | [04](../04-complejidad-computacional/04-complejidad-espacial.md) |
| $EXP$ | Tiempo exponencial | Decidibles en tiempo $2^{n^{O(1)}}$ | [01](../04-complejidad-computacional/01-p-np-y-np-completitud.md) |
| $BPP$ | Error acotado probabilista | Error $\leq 1/3$ en tiempo polinomial | [08](../04-complejidad-computacional/08-complejidad-aleatoria.md) |
| $RP$ | Aleatorio en un lado | Error de falsos negativos $\leq 1/2$ | [08](../04-complejidad-computacional/08-complejidad-aleatoria.md) |
| $\#P$ | Sharp-P (conteo) | Funciones que cuentan ramas aceptadoras de NP | [11](../04-complejidad-computacional/11-sharp-p-y-conteo.md) |
| $\Sigma_k^P, \Pi_k^P$ | Jerarquía polinómica | $\Sigma_1^P=NP$, $\Pi_1^P=\text{co-}NP$, etc. | [01](../04-complejidad-computacional/01-p-np-y-np-completitud.md) |
| $PH$ | Jerarquía polinómica | $PH = \bigcup_k \Sigma_k^P$ | [01](../04-complejidad-computacional/01-p-np-y-np-completitud.md) |
| $P^A$ | P con oráculo $A$ | Tiempo polinomial + consultas en $O(1)$ a $A$ | [11](../03-computabilidad/11-oráculos-y-relativización.md) |
| $\leq_p$ | Reducción polinómica | Transformación en tiempo polinomial | [02](../04-complejidad-computacional/02-reducciones-polinomicas.md) |
| $\text{tw}(G)$ | Treewidth de $G$ | Ancho de árbol del grafo $G$ | [10](../04-complejidad-computacional/10-complejidad-parametrizada.md) |

---

## Información cuántica

| Símbolo | Nombre | Definición | Artículo |
|---------|--------|-----------|---------|
| $\|{0}\rangle, \|{1}\rangle$ | Estados de la base computacional | Vectores de la base estándar de $\mathbb{C}^2$ | [04](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md) |
| $\|\psi\rangle$ | Estado cuántico puro | $\alpha\|0\rangle + \beta\|1\rangle$, $\|\alpha\|^2+\|\beta\|^2=1$ | [04](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md) |
| $\rho$ | Matriz densidad | $\rho \geq 0$, $\text{tr}(\rho)=1$ | [04](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md) |
| $S(\rho)$ | Entropía de Von Neumann | $-\text{tr}(\rho\log_2\rho)$ | [04](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md) |
| $H$ | Puerta de Hadamard | $\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | [04](../05-conexiones-y-aplicaciones/04-informacion-cuantica.md) |

---

## Probabilidad y estadística

| Símbolo | Nombre | Descripción | Módulo |
|---------|--------|-------------|--------|
| $P(A)$ | Probabilidad de $A$ | Medida en $[0,1]$ | 01 |
| $P(A\|B)$ | Probabilidad condicional | $P(A\cap B)/P(B)$ | 01 |
| $\mathbb{E}[X]$ | Esperanza de $X$ | $\sum_x x\, P(X=x)$ | 01 |
| $\text{Var}(X)$ | Varianza de $X$ | $\mathbb{E}[X^2]-(\mathbb{E}[X])^2$ | 01 |
| $I(\theta)$ | Información de Fisher | $\mathbb{E}[(\partial_\theta \ln f(X;\theta))^2]$ | [07](../05-conexiones-y-aplicaciones/07-informacion-y-biologia.md) |
| $\pi$ | Distribución estacionaria | $\pi P = \pi$ para cadena de Markov | [12](../02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md) |

---

## Notación asintótica

| Símbolo | Nombre | Definición informal |
|---------|--------|-------------------|
| $O(f(n))$ | Cota superior asintótica | Crece a lo sumo como $f(n)$ |
| $\Omega(f(n))$ | Cota inferior asintótica | Crece al menos como $f(n)$ |
| $\Theta(f(n))$ | Cota ajustada | Crece exactamente como $f(n)$ |
| $o(f(n))$ | Cota superior estricta | Crece estrictamente más lento que $f(n)$ |
| $\omega(f(n))$ | Cota inferior estricta | Crece estrictamente más rápido que $f(n)$ |
