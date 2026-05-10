# 26 - Criptografía y complejidad

## Contexto

Este ejercicio acompaña el artículo
[Criptografía y complejidad](../../05-conexiones-y-aplicaciones/02-criptografia-y-complejidad.md).

## Enunciado

**Parte A — Cifrado de Vernam (OTP):**

1. Alicia quiere cifrar el mensaje $m = 1011$ con la clave $k = 0110$ usando OTP
   ($c = m \oplus k$). ¿Cuál es el cifrado $c$? Si Eve intercepta $c$ sin conocer
   $k$, ¿qué información obtiene sobre $m$?

2. ¿Por qué el OTP no puede reutilizarse? Si Alicia cifra $m_1$ y $m_2$ con la
   misma clave $k$, ¿qué obtiene Eve si captura $c_1 = m_1 \oplus k$ y $c_2 = m_2 \oplus k$?

**Parte B — Aritmética modular y RSA:**

3. Calcula $3^{10} \mod 11$ usando el pequeño teorema de Fermat.

4. Sean $p = 5$, $q = 11$. Construye un sistema RSA:
   - Calcula $n = pq$ y $\phi(n)$.
   - Elige la clave pública $e = 3$ y calcula la clave privada $d$.
   - Cifra el mensaje $m = 4$ con la clave pública.
   - Descifra el cifrado obtenido.

## Pista

**OTP:** $m \oplus k \oplus k = m$. La seguridad perfecta de Shannon: $I(M; C) = 0$
si $K$ es uniforme y tan largo como $M$.

**Fermat:** si $p$ es primo y $\gcd(a,p)=1$, entonces $a^{p-1} \equiv 1 \pmod{p}$.

**RSA:** $d = e^{-1} \mod \phi(n)$. El descifrado: $m = c^d \mod n$.

## Solución

### Parte A — OTP

#### 1. Cifrado y seguridad

Con $m = 1011$ y $k = 0110$:

```text
m   = 1 0 1 1
k   = 0 1 1 0
c   = 1 1 0 1  (XOR bit a bit)
```

**¿Qué sabe Eve con solo $c = 1101$?**

Eve no obtiene ninguna información sobre $m$. Formalmente, la seguridad perfecta
de Shannon garantiza:

$$P(M = m | C = c) = P(M = m) \quad \text{para todo } m, c$$

Esto se prueba porque para cada par $(m, c)$ existe exactamente una clave $k = m \oplus c$
que produce $c$ a partir de $m$, y si $k$ es uniforme, todos los mensajes son
igualmente plausibles dado $c$.

En nuestro ejemplo, Eve ve $c = 1101$. Los cuatro mensajes posibles de 4 bits
son igualmente compatibles con $c$ (con claves $k = 1101, 0011, 0110, \ldots$),
así que Eve no descarta ningún mensaje.

#### 2. Reutilización de clave

Si Alicia usa la misma clave $k$ dos veces:

$$c_1 = m_1 \oplus k$$
$$c_2 = m_2 \oplus k$$

Eve calcula:

$$c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = m_1 \oplus m_2$$

Eve conoce $m_1 \oplus m_2$: la XOR de los dos mensajes. Si conoce uno (por ejemplo,
si $m_1$ tiene un formato conocido, como un encabezado), puede recuperar el otro.

**Ataque "two-time pad":** en la práctica, los textos en inglés cifrados con la
misma clave OTP pueden descifrarse con análisis estadístico de frecuencias en $m_1 \oplus m_2$.

### Parte B — RSA

#### 3. Pequeño teorema de Fermat

Con $p = 11$ primo y $a = 3$:

$$3^{10} \equiv 1 \pmod{11} \quad \text{(Fermat: } a^{p-1} \equiv 1 \pmod p\text{)}$$

Verificación: $3^{10} = 59049$. $59049 / 11 = 5368.09\ldots$, $5368 \times 11 = 59048$.
$59049 - 59048 = 1$. ✓

**Cómo usar Fermat en la práctica:**

$$3^{10} \mod 11 = 1 \quad \Rightarrow \quad 3^{100} = (3^{10})^{10} \equiv 1^{10} = 1 \pmod{11}$$

#### 4. Sistema RSA con $p = 5$, $q = 11$

**Paso 1:** $n = pq = 5 \times 11 = 55$.

**Paso 2:** $\phi(n) = (p-1)(q-1) = 4 \times 10 = 40$.

**Paso 3:** clave pública $e = 3$. Verificar $\gcd(3, 40) = 1$ ✓.

**Paso 4:** clave privada $d = e^{-1} \mod 40$.

Buscamos $d$ tal que $3d \equiv 1 \pmod{40}$. Algoritmo extendido de Euclides:

```text
40 = 13·3 + 1
→ 1 = 40 - 13·3
→ 3·(-13) ≡ 1 (mod 40)
→ d = -13 mod 40 = 27
```

Verificación: $3 \times 27 = 81 = 2 \times 40 + 1 \equiv 1 \pmod{40}$. ✓

**Clave pública:** $(e, n) = (3, 55)$.  
**Clave privada:** $(d, n) = (27, 55)$.

**Paso 5:** cifrar $m = 4$.

$$c = m^e \mod n = 4^3 \mod 55 = 64 \mod 55 = 9$$

**Cifrado:** $c = 9$.

**Paso 6:** descifrar $c = 9$.

$$m' = c^d \mod n = 9^{27} \mod 55$$

Usando exponenciación rápida (cuadrados sucesivos):

```text
9^1  = 9
9^2  = 81 mod 55 = 26
9^4  = 26² mod 55 = 676 mod 55 = 676 - 12·55 = 676 - 660 = 16
9^8  = 16² mod 55 = 256 mod 55 = 256 - 4·55 = 256 - 220 = 36
9^16 = 36² mod 55 = 1296 mod 55 = 1296 - 23·55 = 1296 - 1265 = 31

27 = 16 + 8 + 2 + 1
9^27 = 9^16 · 9^8 · 9^2 · 9^1 mod 55
     = 31 · 36 · 26 · 9 mod 55
```

Paso a paso:
```text
31 · 36 = 1116 mod 55 = 1116 - 20·55 = 1116 - 1100 = 16
16 · 26 = 416 mod 55 = 416 - 7·55 = 416 - 385 = 31
31 · 9  = 279 mod 55 = 279 - 5·55 = 279 - 275 = 4
```

$m' = 4 = m$ ✓

**El descifrado recupera correctamente el mensaje original.**

## Comentario

La seguridad de RSA descansa en la dificultad de **factorizar** $n$ dado $(e, n)$:
si se conocen los factores $p, q$, se puede calcular $\phi(n)$ y luego $d$. No se
conoce ningún algoritmo clásico que factorice en tiempo polinomial, pero el
algoritmo cuántico de Shor lo hace en $O((\log n)^3)$ tiempo. RSA con $n$ de
2048 bits es seguro contra ataques clásicos pero vulnerable a computación cuántica
suficientemente potente.

## Para seguir

Investiga el **protocolo de Diffie-Hellman**: ¿cómo permite a dos partes establecer
un secreto compartido sobre un canal no seguro? ¿Qué problema computacional asume
como difícil (problema del logaritmo discreto)? ¿Por qué Shor también lo rompe?
