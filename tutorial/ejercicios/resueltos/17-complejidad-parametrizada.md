# 17 - Complejidad parametrizada

## Contexto

Este ejercicio acompaña el artículo
[Complejidad parametrizada](../../04-complejidad-computacional/10-complejidad-parametrizada.md).

También se puede practicar con el cuaderno
[Complejidad parametrizada: k-Vertex Cover](../../cuadernos/ejercicios/16-complejidad-parametrizada.ipynb).

## Enunciado

Considera el grafo G con 8 vértices y las siguientes aristas:

```text
{0-1, 0-2, 1-3, 2-3, 3-4, 4-5, 4-6, 5-7, 6-7}
```

1. Aplica las reglas de kernelización para k-Vertex Cover con k = 3:
   - Regla 1: si deg(v) > k, incluir v en el cover y reducir k.
   - Regla 2: si quedan más de k² aristas, la respuesta es NO.
   - ¿Qué vértices entran forzosamente? ¿Qué tamaño tiene el kernel?

2. Sobre el kernel resultante, aplica el árbol de búsqueda acotado para
   encontrar un vertex cover de tamaño ≤ k restante. Muestra el árbol.

3. ¿Cuál es la complejidad total del algoritmo (kernelización + BST)?

## Pista

**Kernelización:** calcula los grados. Cualquier vértice con grado > k debe estar
en el cover. Tras incluirlo, elimínalo y actualiza los grados y k.

**Árbol de búsqueda:** elige cualquier arista (u, v) del kernel. Haz dos ramas:
incluir u (k-1) o incluir v (k-1). Recursión hasta que no queden aristas (éxito)
o k = 0 con aristas restantes (fallo).

## Solución

### 1. Kernelización con k = 3

**Grados iniciales:**

```text
vértice 0: grado 2 (conectado a 1, 2)
vértice 1: grado 2 (conectado a 0, 3)
vértice 2: grado 2 (conectado a 0, 3)
vértice 3: grado 3 (conectado a 1, 2, 4)   ← grado = k = 3 (no > k)
vértice 4: grado 3 (conectado a 3, 5, 6)   ← grado = k = 3 (no > k)
vértice 5: grado 2 (conectado a 4, 7)
vértice 6: grado 2 (conectado a 4, 7)
vértice 7: grado 2 (conectado a 5, 6)
```

Ningún vértice tiene grado estrictamente mayor que k = 3. La regla 1 no fuerza
a nadie.

**Regla 2:** hay 9 aristas. Límite: k² = 9. Como 9 ≤ 9, no podemos concluir NO.

El kernel es el grafo completo (no se redujo). k_restante = 3.

**Nota:** con k = 2 sí se podría forzar: grados 3 y 4 son > 2.

### 2. Árbol de búsqueda acotado (k = 3 sobre el grafo original)

Elegimos la arista (3, 4) como primera arista a cubrir.

```
                    ¿cubrir 3 o 4?
                   /              \
            incluir 3              incluir 4
            k=2, aristas           k=2, aristas
            restantes:             restantes:
            {0-1,0-2,4-5,4-6,5-7,6-7}  {0-1,0-2,1-3,2-3,5-7,6-7}
               /       \              /          \
          cubrir 4    cubrir 5    cubrir 3    cubrir 1
          k=1          k=1         k=1          k=1
          {0-1,0-2,   {0-1,0-2,   {0-1,0-2,   {0-2,2-3,
           5-7,6-7}    4-6,6-7}    5-7,6-7}    5-7,6-7}
```

**Rama: 3, 4, luego resolver {0-1, 0-2, 5-7, 6-7} con k=1:**

Arista (0,1): cubrir 0 elimina {0-1, 0-2} → quedan {5-7, 6-7} con k=0. Fallo.
             cubrir 1 elimina {0-1} → quedan {0-2, 5-7, 6-7} con k=0. Fallo.

**Rama: 3, 5, luego resolver {0-1, 0-2, 4-6, 6-7} con k=1:**

Arista (4,6): cubrir 4 elimina {4-6} → quedan {0-1, 0-2, 6-7} con k=0. Fallo.
             cubrir 6 elimina {4-6, 6-7} → quedan {0-1, 0-2} con k=0. Fallo.

**Rama: 4, luego {0-1, 0-2, 1-3, 2-3, 5-7, 6-7} con k=2:**

Arista (0,1): cubrir 0 → quedan {1-3, 2-3, 5-7, 6-7} con k=1.
  Arista (1,3): cubrir 1 → quedan {2-3, 5-7, 6-7} con k=0. Fallo.
               cubrir 3 → quedan {5-7, 6-7} con k=0. Fallo.
             cubrir 1 → quedan {0-2, 2-3, 5-7, 6-7} con k=1.
  Arista (0,2): cubrir 0 → quedan {2-3, 5-7, 6-7} con k=0. Fallo.
               cubrir 2 → quedan {5-7, 6-7} con k=0. Fallo.

No hay vertex cover de tamaño 3 que funcione fácilmente con solo 3 vértices
para este grafo (el mínimo real es mayor).

**Cover mínimo real:** verificando, {3, 4, 7} cubre:
- 3 cubre: 1-3, 2-3, 3-4 ✓
- 4 cubre: 4-5, 4-6 ✓  (también 3-4 ya cubierta)
- 7 cubre: 5-7, 6-7 ✓
- Falta: 0-1, 0-2 ✗

Necesitamos al menos k = 4: cover válido es {0, 3, 4, 7}:
- 0 cubre: 0-1, 0-2
- 3 cubre: 1-3, 2-3, 3-4
- 4 cubre: 4-5, 4-6
- 7 cubre: 5-7, 6-7  ✓

### 3. Complejidad

- **Kernelización:** O(k · n) para aplicar las reglas de reducción una vez.
- **Árbol de búsqueda:** O(2^k · n) en el kernel de tamaño ≤ k².
- **Total:** O(k · n + 2^k · k²).

Para k fijo pequeño esto es polinomial en n. Con k = 4 y n = 8:

```text
2^4 · 4² = 16 · 16 = 256 operaciones en el kernel
```

vs. fuerza bruta: C(8, 4) = 70 subconjuntos a verificar (también manejable,
pero exponencial en k para n grande).

## Comentario

El ejemplo muestra que incluso la kernelización no siempre reduce el grafo:
cuando todos los grados están justo en el límite k, la regla de grado alto no
actúa. En grafos densos o regulares el kernel puede ser igual al grafo original.
El verdadero beneficio es para instancias donde muchos vértices tienen grado alto.

## Para seguir

Aplica las reglas de kernelización al grafo K₄ (clique de 4 vértices) con k = 3.
¿Cuántos vértices se incluyen forzosamente por la regla de grado alto?
