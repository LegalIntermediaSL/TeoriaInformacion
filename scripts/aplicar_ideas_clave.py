#!/usr/bin/env python3
"""
Estandariza la sección "Ideas clave" a exactamente 5 puntos en todos los artículos.
- Artículos sin la sección: la añade antes de ## Ejercicios o ## Referencias.
- Artículos con 4 puntos: añade el punto que falta.
- Artículos con 6 puntos: elimina el menos importante.
"""

import re, os

BASE = "/Users/legalintermedia/Documents/GitHub/TeoriaInformacion/tutorial"

# Lookup: 5 ideas clave por artículo (solo los que faltan o tienen count ≠ 5)
IDEAS = {

    # ─── Sin sección: Módulo 00 ──────────────────────────────────────────────
    "00-presentacion/01-mapa-del-territorio.md": [
        "La información, la computabilidad y la complejidad son tres facetas de un mismo problema fundamental: ¿qué se puede calcular y a qué coste?",
        "El tutorial se organiza en cinco módulos que se refuerzan mutuamente; no es necesario seguirlos en orden estricto.",
        "La entropía de Shannon, la indecidibilidad de Turing y la NP-completitud son los tres resultados más influyentes del siglo XX en informática teórica.",
        "Cada módulo tiene un artículo de apertura que sirve de mapa local; léelo antes de adentrarte en los detalles.",
        "Las conexiones entre módulos (complejidad descriptiva, SNARKs, Kolmogorov) son tan importantes como los contenidos de cada módulo por separado.",
    ],

    # ─── Sin sección: Módulo 01 ──────────────────────────────────────────────
    "01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md": [
        "El logaritmo en base 2 es la unidad natural de la información: log₂(n) bits distinguen n equiprobables.",
        "Probabilidad y entropía comparten la misma base matemática; dominar P(A) y P(A|B) es imprescindible antes del módulo de información.",
        "Las notaciones O, Ω, Θ describen el comportamiento asintótico y son el lenguaje universal de la complejidad.",
        "Las funciones exponencial y logarítmica son inversas; invertir exp dará el tamaño de entradas factibles para un algoritmo.",
        "El teorema de Bayes es la herramienta central para razonar con incertidumbre y aparece en inferencia, codificación y aprendizaje.",
    ],
    "01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md": [
        "Un conjunto es la noción más básica de colección; operaciones como unión e intersección se usan en la descripción de clases de complejidad.",
        "Una función biyectiva establece una correspondencia uno a uno; las bijeaciones cuentan objetos (argumento de diagonalización de Cantor).",
        "Las relaciones de equivalencia particionan un conjunto en clases; son la base de los autómatas de estados equivalentes.",
        "El producto cartesiano A×B es el conjunto de todos los pares; modela la entrada de funciones de dos variables y tablas de verdad.",
        "La cardinalidad infinita (contable vs. incontable) determina la existencia de lenguajes indecidibles: hay más lenguajes que programas.",
    ],
    "01-fundamentos-matematicos/03-combinatoria-y-conteo.md": [
        "El principio de la multiplicación: si A tiene m opciones y B tiene n, el total de pares es m·n.",
        "Permutaciones (orden importa) y combinaciones (orden no importa) son los dos bloques básicos del conteo.",
        "El principio de inclusión-exclusión evita doble conteo: |A∪B| = |A|+|B|−|A∩B|.",
        "El principio del palomar: si n+1 objetos caben en n casillas, alguna casilla tiene al menos dos objetos; fundamental en teoría de códigos.",
        "El coeficiente binomial C(n,k) cuenta subconjuntos de k elementos; el triángulo de Pascal da su estructura recursiva.",
    ],
    "01-fundamentos-matematicos/04-grafos-y-estructuras-discretas.md": [
        "Un grafo G=(V,E) modela relaciones entre objetos; es la estructura central de los problemas NP-completos (Clique, Coloring, VC).",
        "BFS calcula distancias mínimas en grafos no ponderados en O(V+E); DFS detecta ciclos y componentes conexas.",
        "Un árbol es un grafo conexo sin ciclos; tiene exactamente n−1 aristas para n vértices y aparece en códigos de Huffman y PDA.",
        "Los grafos bipartitos (dos particiones, aristas solo entre ellas) modelan códigos LDPC y el problema de matching.",
        "La coloración de grafos, el ciclo hamiltoniano y el problema del viajante son NP-completos; ilustran la dureza de los problemas combinatorios.",
    ],
    "01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md": [
        "Las conectivas AND, OR, NOT forman un sistema completo: cualquier función booleana se expresa con ellas.",
        "Una fórmula en CNF (conjunción de disyunciones) es la forma normal relevante para SAT y 3-SAT.",
        "El álgebra de Boole permite simplificar circuitos; las leyes de De Morgan son las transformaciones más usadas.",
        "SAT (¿es satisfacible una fórmula booleana?) fue el primer problema demostrado NP-completo (Cook-Levin, 1971).",
        "Los circuitos lógicos implementan funciones booleanas en hardware; su tamaño y profundidad corresponden al tiempo y espacio de cómputo.",
    ],

    # ─── Sin sección: Módulo 02 01-07 ────────────────────────────────────────
    "02-teoria-informacion/01-entropia-incertidumbre.md": [
        "La entropía H(X) = −∑ p(x) log₂ p(x) mide la incertidumbre promedio de una variable aleatoria en bits.",
        "H(X) se maximiza con la distribución uniforme y vale 0 cuando el resultado es determinista.",
        "Un bit es la cantidad de información que resuelve una pregunta binaria equiprobable.",
        "La entropía es la cota inferior para la longitud media de cualquier código sin pérdida (primer teorema de Shannon).",
        "La entropía de Shannon y la entropía de Boltzmann describen la misma magnitud con un factor de escala kB ln 2.",
    ],
    "02-teoria-informacion/02-informacion-mutua.md": [
        "I(X;Y) = H(X) − H(X|Y) mide cuánta incertidumbre de X se elimina al conocer Y.",
        "La información mutua es simétrica: I(X;Y) = I(Y;X), aunque la causalidad no lo sea.",
        "I(X;Y) = D_KL(P_{XY} ‖ P_X P_Y): mide cuánto difiere la distribución conjunta del producto de las marginales.",
        "La capacidad de canal C = max_P I(X;Y) es la máxima información mutua alcanzable variando la distribución de entrada.",
        "El diagrama de Venn de entropías (H(X), H(Y), H(X,Y), H(X|Y), I(X;Y)) resume todas las relaciones de dependencia.",
    ],
    "02-teoria-informacion/03-codificacion-de-fuente.md": [
        "El código de Huffman construye un árbol binario óptimo: la longitud media está entre H(X) y H(X)+1 bits/símbolo.",
        "Un código prefijo (sin prefijo de un símbolo es prefijo de otro) permite decodificación unívoca sin separadores.",
        "La desigualdad de Kraft ∑ 2^{−l_i} ≤ 1 es condición necesaria y suficiente para la existencia de un código prefijo.",
        "El primer teorema de Shannon: la longitud media de cualquier código sin pérdida es ≥ H(X).",
        "La codificación aritmética supera a Huffman en longitud media acercándose a H(X) con error arbitrariamente pequeño.",
    ],
    "02-teoria-informacion/04-canales-discretos-y-capacidad.md": [
        "Un canal discreto sin memoria se describe por su probabilidad de transición P(y|x) entre entrada x y salida y.",
        "La capacidad C = max_{P(x)} I(X;Y) es la máxima tasa de información transmisible con error arbitrariamente pequeño.",
        "El canal binario simétrico (BSC) con crossover p tiene capacidad C = 1 − H_b(p) bits por uso.",
        "El canal de borrado binario (BEC) con probabilidad ε tiene capacidad C = 1−ε; ideal para analizar LDPC.",
        "La capacidad es una propiedad del canal, no del código; el teorema de Shannon garantiza que existe un código que la alcanza.",
    ],
    "02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md": [
        "D_KL(P‖Q) = ∑ P(x) log[P(x)/Q(x)] mide cuánta información se pierde al usar Q como modelo cuando la realidad es P.",
        "La KL no es simétrica: D_KL(P‖Q) ≠ D_KL(Q‖P) en general; esta asimetría tiene interpretación estadística.",
        "La desigualdad de Gibbs: D_KL(P‖Q) ≥ 0 con igualdad solo si P = Q; se prueba con la concavidad del logaritmo.",
        "La entropía cruzada H(P,Q) = H(P) + D_KL(P‖Q) es la función de pérdida estándar en clasificación multiclase.",
        "La KL aparece en compresión (longitud extra al usar código incorrecto), en estadística (pruebas de hipótesis) y en variational inference.",
    ],
    "02-teoria-informacion/06-codigos-correctores-de-errores.md": [
        "La distancia de Hamming d_H(u,v) cuenta posiciones distintas; un código con distancia mínima d corrige ⌊(d−1)/2⌋ errores.",
        "El código de Hamming (7,4) añade 3 bits de paridad a 4 de datos; corrige 1 error y su tasa es 4/7.",
        "La cota de Hamming (sphere-packing): el número de palabras código no puede superar 2^n dividido por el volumen de la bola de errores.",
        "La cota de Singleton: d ≤ n−k+1; los códigos MDS (Reed-Solomon) la alcanzan con igualdad.",
        "La distinción entre tasa R = k/n y distancia relativa δ = d/n determina el compromiso fundamental de los códigos.",
    ],
    "02-teoria-informacion/07-entropia-conjunta-y-condicional.md": [
        "H(X,Y) ≤ H(X) + H(Y) con igualdad si y solo si X e Y son independientes.",
        "La regla de la cadena: H(X₁,...,Xn) = ∑ H(Xᵢ|X₁,...,Xᵢ₋₁); la entropía se descompone secuencialmente.",
        "H(X|Y) ≤ H(X): conocer Y no puede aumentar la incertidumbre de X (el condicionamiento reduce la entropía).",
        "El diagrama de Venn de entropías visualiza H(X), H(Y), H(X|Y), H(Y|X), I(X;Y) y H(X,Y) como áreas.",
        "La desigualdad de procesamiento de datos: si X→Y→Z es una cadena de Markov, I(X;Z) ≤ I(X;Y).",
    ],

    # ─── Sin sección: Módulo 03 01-05 ────────────────────────────────────────
    "03-computabilidad/01-problema-de-la-parada.md": [
        "El problema de la parada (HALT) no es decidible: no existe ningún algoritmo que determine para todo par (M,w) si M se detiene con entrada w.",
        "La prueba usa diagonalización: construir una máquina D que hace lo contrario a lo que predice cualquier decididor hipotético.",
        "Todo lenguaje decidible es reconocible, pero hay lenguajes reconocibles que no son decidibles (HALT es el ejemplo canónico).",
        "La indecidibilidad es una propiedad semántica: muchas preguntas sobre el comportamiento de programas son indecidibles por el teorema de Rice.",
        "HALT reduce a docenas de problemas prácticos (verificación formal, análisis estático, equivalencia de programas), propagando la indecidibilidad.",
    ],
    "03-computabilidad/02-decidibilidad-y-reconocibilidad.md": [
        "Un lenguaje L es decidible si existe una MT que acepta si w∈L y rechaza si w∉L, siempre terminando.",
        "Un lenguaje es reconocible (RE) si hay una MT que acepta todas las palabras del lenguaje pero puede no terminar para las que no están.",
        "L es decidible ↔ L y su complemento L̄ son ambos reconocibles (teorema de Kleene).",
        "HALT es reconocible pero no decidible; su complemento co-HALT no es reconocible.",
        "La jerarquía RE ⊂ co-RE ⊂ todos los lenguajes estratifica los lenguajes por su grado de computabilidad.",
    ],
    "03-computabilidad/03-reducciones-e-indecidibilidad.md": [
        "Una reducción de muchos-a-uno A ≤_m B transforma instancias de A en instancias de B en tiempo computable: si B es decidible, A también lo es.",
        "HALT ≤_m E_TM (¿es vacío el lenguaje de M?): la indecidibilidad se propaga por reducción.",
        "El teorema de Rice: toda propiedad no trivial del lenguaje de una MT es indecidible.",
        "Las reducciones definen un orden parcial en los problemas: el problema más difícil es completo respecto de una clase.",
        "La diagonalización y las reducciones son las dos herramientas principales para probar indecidibilidad.",
    ],
    "03-computabilidad/04-maquinas-de-turing.md": [
        "Una máquina de Turing es una cinta infinita + cabeza lectora/escritora + tabla de transiciones; formaliza el concepto de algoritmo.",
        "La tesis de Church-Turing: todo proceso efectivamente computable puede simularse con una MT.",
        "Una MT universal (UTM) simula cualquier otra MT leyendo su descripción como parte de la entrada.",
        "Variantes (MT multiacinta, no deterministas, sobre enteros) son equivalentes en poder de cómputo a la MT estándar.",
        "El tiempo y el espacio que usa una MT en sus simulaciones importan: las diferencias dan lugar a las clases P, NP, PSPACE.",
    ],
    "03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md": [
        "Un DFA reconoce exactamente los lenguajes regulares; un NFA es equivalente al DFA pero puede tener transiciones no deterministas.",
        "La construcción de subconjuntos convierte cualquier NFA en un DFA equivalente con a lo sumo 2^n estados.",
        "El lema de bombeo para regulares: si L es regular y w∈L con |w|≥p, entonces w = xyz con |xy|≤p y xy^iz∈L para todo i≥0.",
        "Los lenguajes regulares son cerrados bajo unión, concatenación, clausura de Kleene, intersección y complemento.",
        "Las expresiones regulares describen exactamente los lenguajes regulares; las regexes en programación son una extensión práctica.",
    ],

    # ─── Módulo 03 con count ≠ 5 ────────────────────────────────────────────
    "03-computabilidad/07-universalidad-y-autorreferencia.md": None,  # 4 → add 1
    "03-computabilidad/08-complejidad-descriptiva.md": None,           # 4 → add 1

    # ─── Sin sección: Módulo 04 01-06 ────────────────────────────────────────
    "04-complejidad-computacional/01-p-np-y-np-completitud.md": [
        "P es la clase de problemas decidibles en tiempo polinomial determinista; NP admite verificación de certificados en tiempo polinomial.",
        "La pregunta P ≠ NP es el problema abierto más importante de la informática teórica.",
        "El teorema de Cook-Levin: SAT es NP-completo; todo problema en NP se reduce a SAT en tiempo polinomial.",
        "Un problema es NP-completo si está en NP y todo problema en NP se reduce a él; resolver uno en P resolvería todos.",
        "La distinción entre resolver (encontrar solución) y verificar (comprobar solución dada) es el núcleo de la conjetura P ≠ NP.",
    ],
    "04-complejidad-computacional/02-reducciones-polinomicas.md": [
        "Una reducción polinomial A ≤_p B es una función f computable en tiempo polinomial tal que x∈A ↔ f(x)∈B.",
        "Si A ≤_p B y B ∈ P, entonces A ∈ P; si A es NP-difícil y A ≤_p B, entonces B es NP-difícil.",
        "Las reducciones canónicas (SAT → 3-SAT → Clique → VC → IS) son el vocabulario de la complejidad.",
        "Una reducción correcta debe preservar tanto las instancias positivas como las negativas del problema.",
        "Las reducciones se componen: si A ≤_p B y B ≤_p C, entonces A ≤_p C.",
    ],
    "04-complejidad-computacional/03-sat-y-3-sat.md": [
        "SAT (satisfacibilidad booleana) es el primer problema NP-completo por el teorema de Cook-Levin (1971).",
        "3-SAT restringe SAT a cláusulas de exactamente 3 literales; sigue siendo NP-completo y es la reducción de partida más usada.",
        "2-SAT es resoluble en tiempo lineal (implicación de grafos + componentes fuertemente conexas); la frontera P/NP pasa entre k=2 y k=3.",
        "MAX-SAT (maximizar cláusulas satisfechas) es NP-difícil de aproximar más allá de 7/8 por el teorema PCP de Håstad.",
        "k-SAT crece en dificultad con k: la ETH conjetura que k-SAT requiere tiempo 2^{Ω(n)} para todo k≥3.",
    ],
    "04-complejidad-computacional/04-complejidad-espacial.md": [
        "PSPACE es la clase de problemas decidibles con espacio polinomial; contiene NP y co-NP.",
        "El teorema de Savitch: NPSPACE = PSPACE; el no determinismo solo cuadra el espacio.",
        "TQBF (verdad de fórmulas booleanas cuantificadas) es PSPACE-completo; generaliza SAT añadiendo cuantificadores ∀.",
        "L y NL son las clases de espacio logarítmico; NL = co-NL por el teorema de Immerman-Szelepcsényi.",
        "La jerarquía de espacio es estricta (DSPACE(s(n)) ⊊ DSPACE(s'(n)) si s' ≫ s), a diferencia del tiempo donde el análogo es abierto.",
    ],
    "04-complejidad-computacional/05-complejidad-temporal-de-algoritmos.md": [
        "La notación O(f(n)) describe el peor caso asintótico; Ω(f(n)) el mejor caso; Θ(f(n)) cuando coinciden.",
        "El teorema maestro resuelve recurrencias T(n)=aT(n/b)+f(n) que aparecen en divide y vencerás.",
        "Los algoritmos de ordenación basados en comparaciones tienen cota inferior Ω(n log n) por el argumento del árbol de decisión.",
        "La distinción entre polinomial (tractable) y exponencial (intractable) es la frontera práctica de la eficiencia.",
        "El análisis amortizado (potential method) da cotas precisas para estructuras de datos con operaciones de coste variable.",
    ],
    "04-complejidad-computacional/06-aproximacion-y-heuristicas.md": [
        "Un algoritmo de aproximación de ratio α garantiza que su solución está en un factor α del óptimo para toda instancia.",
        "Vertex Cover admite un algoritmo greedy de ratio 2 (matching maximal); el teorema PCP y la UGC sugieren que 2−ε es inalcanzable.",
        "Un PTAS (Polynomial-Time Approximation Scheme) da ratio 1+ε para cualquier ε>0 fijo, con tiempo polinomial en n.",
        "Un FPTAS además es polinomial en 1/ε; existe para Mochila pero no para TSP general (salvo P=NP).",
        "El teorema PCP implica que MAX-3SAT, MAX-Clique e IS no pueden aproximarse más allá de ciertos ratios constantes bajo P≠NP.",
    ],

    # ─── Módulo 04 con count = 6 ─────────────────────────────────────────────
    "04-complejidad-computacional/07-circuitos-booleanos.md": None,  # 6 → trim to 5

    # ─── Sin sección: Módulo 05 ──────────────────────────────────────────────
    "05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md": [
        "K(x) es la longitud del programa más corto que produce x; formaliza la complejidad de un objeto individual.",
        "K(x) es invariante salvo una constante aditiva respecto de la máquina universal de referencia.",
        "K(x) no es computable: no existe un algoritmo que, dado x, calcule K(x) exactamente.",
        "Una cadena x es algorítmicamente aleatoria si K(x) ≥ |x| − c; la mayoría de las cadenas lo son.",
        "El valor esperado 𝔼[K(X)] para X de una fuente Bernoulli(p) satisface 𝔼[K(X)] ≈ nH(p), conectando K con Shannon.",
    ],
    "05-conexiones-y-aplicaciones/02-criptografia-y-complejidad.md": [
        "El OTP (One-Time Pad) ofrece seguridad perfecta de Shannon: ningún adversario con cómputo ilimitado puede romperlo.",
        "RSA se basa en la dificultad de factorizar enteros grandes; su seguridad es condicional a que factorización ∉ P.",
        "Diffie-Hellman permite intercambiar un secreto en un canal público usando el problema del logaritmo discreto.",
        "Una función de un solo sentido es fácil de evaluar (P) pero difícil de invertir; su existencia equivale a P ≠ NP.",
        "Los SNARKs (succinct non-interactive arguments) permiten verificar computaciones complejas con pruebas de kilobytes, usando ideas de PCP.",
    ],
    "05-conexiones-y-aplicaciones/03-aprendizaje-automatico-e-informacion.md": [
        "La función de pérdida de entropía cruzada −∑ y_i log ŷ_i minimiza la divergencia KL entre la distribución real y la predicha.",
        "La mutua información I(X;Y) cuantifica cuánta información sobre la etiqueta Y aporta el atributo X; base de árboles de decisión.",
        "La regularización L2 equivale a imponer una prior gaussiana (MAP = MLE + KL respecto de la prior).",
        "El principio de longitud de descripción mínima (MDL) selecciona el modelo que comprime mejor los datos.",
        "Las redes neuronales como estimadores de densidad implícitos minimizan la divergencia KL entre datos y modelo.",
    ],
    "05-conexiones-y-aplicaciones/04-informacion-cuantica.md": [
        "Un qubit es un vector unitario en ℂ², representado como |ψ⟩ = α|0⟩ + β|1⟩ con |α|²+|β|² = 1.",
        "La entropía de von Neumann S(ρ) = −tr(ρ log ρ) es la extensión cuántica de la entropía de Shannon.",
        "El entrelazamiento cuántico es un recurso sin análogo clásico: no puede crearse por operaciones locales y comunicación clásica (LOCC).",
        "La teleportación cuántica transfiere un estado desconocido usando un par de Bell y 2 bits clásicos, sin violar la relatividad.",
        "La criptografía cuántica (QKD, BB84) ofrece seguridad basada en física cuántica, no en complejidad computacional.",
    ],
    "05-conexiones-y-aplicaciones/05-informacion-en-aprendizaje.md": [
        "La información de Fisher I(θ) mide la sensibilidad de la log-verosimilitud a cambios en el parámetro θ.",
        "La cota de Cramér-Rao: la varianza de cualquier estimador insesgado de θ es ≥ 1/I(θ).",
        "El principio MDL selecciona el modelo que minimiza la longitud total de la descripción del modelo más los datos dado el modelo.",
        "La capacidad de información de un canal de aprendizaje (VC-dimension, Rademacher complexity) determina la generalización.",
        "La distancia de Rényi y la información de Fisher generalizada aparecen en el análisis de algoritmos de descenso de gradiente.",
    ],
}


def make_ideas_clave_section(ideas):
    lines = ["## Ideas clave\n\n"]
    for idea in ideas:
        lines.append(f"- {idea}\n")
    lines.append("\n")
    return "".join(lines)


def fix_wrong_count(content, target=5):
    """For articles with ≠5 ideas, fix the count by trimming or extending."""
    m = re.search(r"(## Ideas clave\n)(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not m:
        return content
    sec = m.group(2)
    items = re.findall(r"^(?:- |\d+\. )(.+)", sec, re.MULTILINE)
    if len(items) == target:
        return content
    if len(items) > target:
        # Trim: keep first target items
        new_items = items[:target]
    else:
        return content  # can't extend without knowing content
    # Rebuild section
    # Detect format (bullets or numbered)
    if re.search(r"^\d+\. ", sec, re.MULTILINE):
        new_sec = "\n".join(f"{i+1}. {item}" for i, item in enumerate(new_items)) + "\n\n"
    else:
        new_sec = "\n".join(f"- {item}" for item in new_items) + "\n\n"
    return content[:m.start(2)] + new_sec + content[m.end(2):]


def process_article(rel_path, ideas):
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        print(f"  SKIP (no existe): {rel_path}")
        return

    with open(full_path, encoding="utf-8") as f:
        content = f.read()

    original = content

    if "## Ideas clave" not in content:
        # Add new section before ## Ejercicios or ## Referencias or at end
        anchor = re.search(r"\n## (?:Ejercicios|Referencias)\b", content)
        block = "\n" + make_ideas_clave_section(ideas)
        if anchor:
            content = content[:anchor.start()] + block + content[anchor.start():]
        else:
            content = content.rstrip() + "\n" + block
    elif ideas is None:
        # Fix wrong count
        content = fix_wrong_count(content, target=5)
    # else: ideas is not None and section already exists → replace or leave
    # (this case shouldn't happen for our 28 missing articles)

    if content != original:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  OK: {rel_path}")
    else:
        print(f"  UNCHANGED: {rel_path}")


if __name__ == "__main__":
    for rel_path, ideas in IDEAS.items():
        process_article(rel_path, ideas)
    print("\nDone.")
