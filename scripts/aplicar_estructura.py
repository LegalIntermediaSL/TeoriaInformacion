#!/usr/bin/env python3
"""
Aplica mejoras estructurales a todos los artículos del tutorial:
- Metadatos (dificultad + tiempo) tras el H1
- Sección Prerrequisitos
- Sección Objetivos de aprendizaje
- Sección Véase también (si no existe)
- Estandarización de Ideas clave a 5 puntos (si tiene más de 5 o menos de 5)
"""

import re
import os

BASE = "/Users/legalintermedia/Documents/GitHub/TeoriaInformacion/tutorial"

# ---------------------------------------------------------------------------
# Tabla de metadatos por artículo
# path relativo a BASE, sin barra inicial
# d: dificultad ("⭐ Básico" / "⭐⭐ Intermedio" / "⭐⭐⭐ Avanzado")
# t: tiempo estimado de lectura
# pre: lista de cadenas de texto con el nombre del prerrequisito y su ruta relativa
# obj: exactamente 3 objetivos de aprendizaje
# vt: 2-3 artículos relacionados con su ruta relativa al archivo actual
# ---------------------------------------------------------------------------

METADATA = {
    # ─── Módulo 00 ───────────────────────────────────────────────────────────
    "00-presentacion/01-mapa-del-territorio.md": dict(
        d="⭐ Básico", t="~10 min",
        pre=[],
        obj=[
            "Comprender la estructura global del tutorial y la relación entre sus módulos.",
            "Identificar qué temas son imprescindibles y cuáles opcionales según tu perfil.",
            "Elegir la ruta de estudio más adecuada para tus objetivos.",
        ],
        vt=[
            ("../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md",
             "Logaritmos, probabilidad y crecimiento"),
            ("../02-teoria-informacion/01-entropia-incertidumbre.md",
             "Entropía e incertidumbre"),
        ],
    ),

    # ─── Módulo 01 ───────────────────────────────────────────────────────────
    "01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md": dict(
        d="⭐ Básico", t="~15 min",
        pre=[],
        obj=[
            "Manejar con soltura el logaritmo en distintas bases y sus propiedades.",
            "Calcular probabilidades básicas y aplicar el teorema de Bayes.",
            "Identificar tasas de crecimiento (exponencial, polinómica, logarítmica).",
        ],
        vt=[
            ("02-conjuntos-funciones-y-relaciones.md", "Conjuntos, funciones y relaciones"),
            ("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
        ],
    ),
    "01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md": dict(
        d="⭐ Básico", t="~20 min",
        pre=[("01-logaritmos-probabilidad-y-crecimiento.md",
               "Logaritmos, probabilidad y crecimiento")],
        obj=[
            "Operar con conjuntos (unión, intersección, complemento, producto cartesiano).",
            "Distinguir funciones inyectivas, sobreyectivas y biyectivas.",
            "Comprender relaciones de equivalencia y de orden.",
        ],
        vt=[
            ("03-combinatoria-y-conteo.md", "Combinatoria y conteo"),
            ("04-grafos-y-estructuras-discretas.md", "Grafos y estructuras discretas"),
        ],
    ),
    "01-fundamentos-matematicos/03-combinatoria-y-conteo.md": dict(
        d="⭐ Básico", t="~20 min",
        pre=[("01-logaritmos-probabilidad-y-crecimiento.md",
               "Logaritmos, probabilidad y crecimiento")],
        obj=[
            "Calcular permutaciones y combinaciones con y sin repetición.",
            "Aplicar el principio de inclusión-exclusión y el principio del palomar.",
            "Estimar el tamaño de espacios combinatorios relevantes en información y complejidad.",
        ],
        vt=[
            ("02-conjuntos-funciones-y-relaciones.md", "Conjuntos, funciones y relaciones"),
            ("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
        ],
    ),
    "01-fundamentos-matematicos/04-grafos-y-estructuras-discretas.md": dict(
        d="⭐ Básico", t="~20 min",
        pre=[("02-conjuntos-funciones-y-relaciones.md",
               "Conjuntos, funciones y relaciones")],
        obj=[
            "Representar problemas como grafos y reconocer sus propiedades básicas.",
            "Aplicar recorridos BFS/DFS para resolver problemas de conectividad.",
            "Identificar grafos bipartitos, árboles y grafos planares.",
        ],
        vt=[
            ("03-combinatoria-y-conteo.md", "Combinatoria y conteo"),
            ("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
        ],
    ),
    "01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md": dict(
        d="⭐ Básico", t="~15 min",
        pre=[("02-conjuntos-funciones-y-relaciones.md",
               "Conjuntos, funciones y relaciones")],
        obj=[
            "Evaluar fórmulas proposicionales y construir tablas de verdad.",
            "Simplificar expresiones booleanas con álgebra de Boole.",
            "Entender la base lógica del diseño de circuitos y la satisfacibilidad.",
        ],
        vt=[
            ("../04-complejidad-computacional/03-sat-y-3-sat.md", "SAT y 3-SAT"),
            ("../04-complejidad-computacional/07-circuitos-booleanos.md", "Circuitos booleanos"),
        ],
    ),

    # ─── Módulo 02 ───────────────────────────────────────────────────────────
    "02-teoria-informacion/01-entropia-incertidumbre.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md",
               "Logaritmos, probabilidad y crecimiento")],
        obj=[
            "Calcular la entropía de Shannon H(X) para distribuciones discretas.",
            "Interpretar la entropía como medida de incertidumbre e información promedio.",
            "Demostrar que la entropía se maximiza con la distribución uniforme.",
        ],
        vt=[
            ("02-informacion-mutua.md", "Información mutua y divergencia KL"),
            ("07-entropia-conjunta-y-condicional.md", "Entropía conjunta y condicional"),
        ],
    ),
    "02-teoria-informacion/02-informacion-mutua.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-entropia-incertidumbre.md", "Entropía e incertidumbre")],
        obj=[
            "Calcular la información mutua I(X;Y) entre dos variables aleatorias.",
            "Relacionar la información mutua con la entropía condicional y la KL.",
            "Interpretar I(X;Y) como la reducción de incertidumbre de X al conocer Y.",
        ],
        vt=[
            ("05-divergencia-kl-y-entropia-cruzada.md", "Divergencia KL y entropía cruzada"),
            ("04-canales-discretos-y-capacidad.md", "Canales discretos y capacidad"),
        ],
    ),
    "02-teoria-informacion/03-codificacion-de-fuente.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("02-informacion-mutua.md", "Información mutua")],
        obj=[
            "Construir códigos prefijo óptimos con el algoritmo de Huffman.",
            "Demostrar que la longitud media de Huffman está entre H(X) y H(X)+1.",
            "Comprender la distinción entre compresión sin pérdida y compresión de fuente.",
        ],
        vt=[
            ("13-codificacion-aritmetica.md", "Codificación aritmética"),
            ("01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
        ],
    ),
    "02-teoria-informacion/04-canales-discretos-y-capacidad.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("02-informacion-mutua.md", "Información mutua")],
        obj=[
            "Modelar un canal de comunicación ruidoso con una matriz de transición.",
            "Calcular la capacidad de canal C = max I(X;Y).",
            "Aplicar el límite de Shannon a canales binarios simétricos.",
        ],
        vt=[
            ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon y capacidad"),
            ("06-codigos-correctores-de-errores.md", "Códigos correctores de errores"),
        ],
    ),
    "02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md": dict(
        d="⭐⭐ Intermedio", t="~15 min",
        pre=[("01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("02-informacion-mutua.md", "Información mutua")],
        obj=[
            "Calcular la divergencia KL D(P‖Q) y la entropía cruzada H(P,Q).",
            "Entender por qué la KL no es una distancia pero mide disimilitud.",
            "Conectar la entropía cruzada con la función de pérdida en modelos generativos.",
        ],
        vt=[
            ("02-informacion-mutua.md", "Información mutua"),
            ("../05-conexiones-y-aplicaciones/03-aprendizaje-automatico-e-informacion.md",
             "Aprendizaje automático e información"),
        ],
    ),
    "02-teoria-informacion/06-codigos-correctores-de-errores.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("04-canales-discretos-y-capacidad.md", "Canales discretos y capacidad")],
        obj=[
            "Definir distancia de Hamming y radio de corrección de un código.",
            "Construir y decodificar códigos de Hamming lineales.",
            "Enunciar la cota de Singleton y la cota de Hamming (sphere-packing).",
        ],
        vt=[
            ("11-codigos-ldpc-y-turbo.md", "Códigos LDPC y turbo"),
            ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon y capacidad"),
        ],
    ),
    "02-teoria-informacion/07-entropia-conjunta-y-condicional.md": dict(
        d="⭐⭐ Intermedio", t="~15 min",
        pre=[("01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("02-informacion-mutua.md", "Información mutua")],
        obj=[
            "Calcular entropía conjunta H(X,Y) y entropía condicional H(X|Y).",
            "Demostrar la regla de la cadena para la entropía.",
            "Aplicar el diagrama de Venn de entropías para visualizar relaciones entre variables.",
        ],
        vt=[
            ("02-informacion-mutua.md", "Información mutua"),
            ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon y capacidad"),
        ],
    ),
    "02-teoria-informacion/08-teorema-de-shannon-capacidad.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("04-canales-discretos-y-capacidad.md", "Canales discretos y capacidad"),
             ("07-entropia-conjunta-y-condicional.md", "Entropía conjunta y condicional")],
        obj=[
            "Enunciar y entender el teorema de codificación de canal de Shannon.",
            "Distinguir capacidad de canal, tasa y probabilidad de error.",
            "Aplicar el argumento de codificación aleatoria en la prueba del teorema.",
        ],
        vt=[
            ("09-teoria-tasa-distorsion.md", "Teoría de tasa-distorsión"),
            ("06-codigos-correctores-de-errores.md", "Códigos correctores de errores"),
        ],
    ),
    "02-teoria-informacion/09-teoria-tasa-distorsion.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("07-entropia-conjunta-y-condicional.md", "Entropía conjunta y condicional"),
             ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon")],
        obj=[
            "Definir la función de tasa-distorsión R(D) y su interpretación.",
            "Calcular R(D) para la fuente Bernoulli y la fuente gaussiana.",
            "Entender el compromiso fundamental entre tasa de compresión y distorsión.",
        ],
        vt=[
            ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon y capacidad"),
            ("10-entropia-diferencial.md", "Entropía diferencial"),
        ],
    ),
    "02-teoria-informacion/10-entropia-diferencial.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("07-entropia-conjunta-y-condicional.md", "Entropía conjunta y condicional")],
        obj=[
            "Definir la entropía diferencial h(X) para variables continuas.",
            "Calcular h(X) para distribuciones gaussianas y uniformes.",
            "Explicar por qué h(X) puede ser negativa y cómo difiere de H(X).",
        ],
        vt=[
            ("09-teoria-tasa-distorsion.md", "Teoría de tasa-distorsión"),
            ("../05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md",
             "Información y termodinámica"),
        ],
    ),
    "02-teoria-informacion/11-codigos-ldpc-y-turbo.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("06-codigos-correctores-de-errores.md", "Códigos correctores de errores"),
             ("04-canales-discretos-y-capacidad.md", "Canales discretos")],
        obj=[
            "Comprender la estructura del grafo de Tanner para códigos LDPC.",
            "Describir el algoritmo de propagación de creencias (belief propagation).",
            "Entender por qué los códigos polares de Arıkan alcanzan la capacidad de Shannon.",
        ],
        vt=[
            ("06-codigos-correctores-de-errores.md", "Códigos correctores de errores"),
            ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon"),
        ],
    ),
    "02-teoria-informacion/12-cadenas-de-markov-y-tasa-de-entropia.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("07-entropia-conjunta-y-condicional.md", "Entropía conjunta y condicional")],
        obj=[
            "Definir una cadena de Markov homogénea y su distribución estacionaria.",
            "Calcular la tasa de entropía de una fuente de Markov.",
            "Aplicar el teorema ergódico para relacionar tiempo y esperanza.",
        ],
        vt=[
            ("14-procesos-estocasticos-y-fuentes-con-memoria.md",
             "Procesos estocásticos y fuentes con memoria"),
            ("07-entropia-conjunta-y-condicional.md", "Entropía conjunta y condicional"),
        ],
    ),
    "02-teoria-informacion/13-codificacion-aritmetica.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("03-codificacion-de-fuente.md", "Codificación de fuente (Huffman)")],
        obj=[
            "Explicar el principio de la codificación aritmética mediante subdivsión de [0,1).",
            "Implementar el algoritmo de codificación aritmética paso a paso.",
            "Comparar la longitud media de la codificación aritmética con Huffman.",
        ],
        vt=[
            ("03-codificacion-de-fuente.md", "Codificación de fuente"),
            ("12-cadenas-de-markov-y-tasa-de-entropia.md",
             "Cadenas de Markov y tasa de entropía"),
        ],
    ),
    "02-teoria-informacion/14-procesos-estocasticos-y-fuentes-con-memoria.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("12-cadenas-de-markov-y-tasa-de-entropia.md",
               "Cadenas de Markov y tasa de entropía")],
        obj=[
            "Definir fuentes estacionarias y ergódicas y su tasa de entropía.",
            "Calcular la entropía de fuentes de Markov de orden k.",
            "Entender el teorema de Shannon-McMillan-Breiman para fuentes ergódicas.",
        ],
        vt=[
            ("12-cadenas-de-markov-y-tasa-de-entropia.md",
             "Cadenas de Markov y tasa de entropía"),
            ("08-teorema-de-shannon-capacidad.md", "Teorema de Shannon"),
        ],
    ),

    # ─── Módulo 03 ───────────────────────────────────────────────────────────
    "03-computabilidad/01-problema-de-la-parada.md": dict(
        d="⭐⭐ Intermedio", t="~15 min",
        pre=[("../01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md",
               "Conjuntos, funciones y relaciones")],
        obj=[
            "Enunciar y demostrar la indecidibilidad del problema de la parada.",
            "Explicar el argumento de diagonalización de Turing.",
            "Distinguir entre problemas decidibles y problemas semidecidibles.",
        ],
        vt=[
            ("02-decidibilidad-y-reconocibilidad.md", "Decidibilidad y reconocibilidad"),
            ("04-maquinas-de-turing.md", "Máquinas de Turing"),
        ],
    ),
    "03-computabilidad/02-decidibilidad-y-reconocibilidad.md": dict(
        d="⭐⭐ Intermedio", t="~15 min",
        pre=[("01-problema-de-la-parada.md", "El problema de la parada")],
        obj=[
            "Distinguir lenguajes decidibles, reconocibles y no reconocibles.",
            "Demostrar que el complemento de un lenguaje RE que no es decidible no es RE.",
            "Clasificar problemas estándar en la jerarquía de decidibilidad.",
        ],
        vt=[
            ("01-problema-de-la-parada.md", "El problema de la parada"),
            ("03-reducciones-e-indecidibilidad.md", "Reducciones e indecidibilidad"),
        ],
    ),
    "03-computabilidad/03-reducciones-e-indecidibilidad.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-problema-de-la-parada.md", "El problema de la parada"),
             ("02-decidibilidad-y-reconocibilidad.md", "Decidibilidad")],
        obj=[
            "Construir reducciones de muchos-a-uno entre problemas de decisión.",
            "Demostrar la indecidibilidad de un lenguaje reduciéndolo desde HALT.",
            "Aplicar el teorema de Rice para clasificar propiedades de lenguajes.",
        ],
        vt=[
            ("02-decidibilidad-y-reconocibilidad.md", "Decidibilidad y reconocibilidad"),
            ("../04-complejidad-computacional/02-reducciones-polinomicas.md",
             "Reducciones polinómicas"),
        ],
    ),
    "03-computabilidad/04-maquinas-de-turing.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-problema-de-la-parada.md", "El problema de la parada")],
        obj=[
            "Definir formalmente una máquina de Turing y su cómputo.",
            "Simular a mano una MT sencilla para un lenguaje conocido.",
            "Enunciar la tesis de Church-Turing y su significado.",
        ],
        vt=[
            ("01-problema-de-la-parada.md", "El problema de la parada"),
            ("07-universalidad-y-autorreferencia.md", "Universalidad y autorreferencia"),
        ],
    ),
    "03-computabilidad/05-automatas-finitos-y-lenguajes-regulares.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("../01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md",
               "Conjuntos, funciones y relaciones")],
        obj=[
            "Construir DFA y NFA para lenguajes regulares sencillos.",
            "Aplicar la construcción de subconjuntos para pasar de NFA a DFA.",
            "Usar el lema de bombeo para demostrar que un lenguaje no es regular.",
        ],
        vt=[
            ("06-gramaticas-y-jerarquia-chomsky.md", "Gramáticas y jerarquía de Chomsky"),
            ("09-automatas-de-pila-y-lenguajes-contexto-libre.md",
             "Autómatas de pila y lenguajes libres de contexto"),
        ],
    ),
    "03-computabilidad/06-gramaticas-y-jerarquia-chomsky.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("05-automatas-finitos-y-lenguajes-regulares.md",
               "Autómatas finitos y lenguajes regulares")],
        obj=[
            "Distinguir los cuatro tipos de gramáticas en la jerarquía de Chomsky.",
            "Relacionar cada nivel de la jerarquía con su clase de autómata correspondiente.",
            "Demostrar que los lenguajes regulares son un subconjunto propio de los CFL.",
        ],
        vt=[],  # ya tiene Véase también
    ),
    "03-computabilidad/09-automatas-de-pila-y-lenguajes-contexto-libre.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("06-gramaticas-y-jerarquia-chomsky.md", "Gramáticas y jerarquía de Chomsky"),
             ("05-automatas-finitos-y-lenguajes-regulares.md", "Autómatas finitos")],
        obj=[
            "Definir un autómata de pila (PDA) y simular su cómputo paso a paso.",
            "Demostrar la equivalencia entre PDA y gramáticas libres de contexto.",
            "Usar el lema de bombeo para CFL para probar que {aⁿbⁿcⁿ} no es CFL.",
        ],
        vt=[],  # ya tiene Véase también
    ),
    "03-computabilidad/07-universalidad-y-autorreferencia.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("04-maquinas-de-turing.md", "Máquinas de Turing"),
             ("01-problema-de-la-parada.md", "El problema de la parada")],
        obj=[
            "Construir una máquina de Turing universal (UTM).",
            "Comprender el teorema del punto fijo de Kleene (teorema del quine).",
            "Relacionar la autorreferencia con la indecidibilidad y los quines.",
        ],
        vt=[
            ("04-maquinas-de-turing.md", "Máquinas de Turing"),
            ("../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md",
             "Complejidad de Kolmogorov"),
        ],
    ),
    "03-computabilidad/08-complejidad-descriptiva.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("04-maquinas-de-turing.md", "Máquinas de Turing"),
             ("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P y NP")],
        obj=[
            "Enunciar el teorema de Fagin: NP = ∃SO.",
            "Expresar 3-colorabilidad como una fórmula de segundo orden existencial.",
            "Entender cómo la lógica de punto fijo captura la clase P.",
        ],
        vt=[
            ("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("../04-complejidad-computacional/09-teorema-pcp.md", "El teorema PCP"),
        ],
    ),
    "03-computabilidad/10-jerarquia-aritmetica.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("01-problema-de-la-parada.md", "El problema de la parada"),
             ("02-decidibilidad-y-reconocibilidad.md", "Decidibilidad")],
        obj=[
            "Definir los niveles Σ₀, Σ₁, Π₁ y Δ₁ de la jerarquía aritmética.",
            "Clasificar problemas canónicos (parada, TOT, FIN) en la jerarquía.",
            "Entender el operador de salto de Turing y cómo genera la jerarquía.",
        ],
        vt=[
            ("11-oráculos-y-relativización.md", "Oráculos y relativización"),
            ("12-aleatoriedad-algoritmica.md", "Aleatoriedad algorítmica"),
        ],
    ),
    "03-computabilidad/11-oráculos-y-relativización.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("04-maquinas-de-turing.md", "Máquinas de Turing"),
             ("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P y NP")],
        obj=[
            "Definir máquinas de Turing con oráculo y su semántica.",
            "Entender el teorema de Baker-Gill-Solovay y sus consecuencias.",
            "Explicar por qué la diagonalización sola no puede separar P de NP.",
        ],
        vt=[
            ("10-jerarquia-aritmetica.md", "Jerarquía aritmética"),
            ("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
        ],
    ),
    "03-computabilidad/12-aleatoriedad-algoritmica.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md",
               "Complejidad de Kolmogorov"),
             ("04-maquinas-de-turing.md", "Máquinas de Turing")],
        obj=[
            "Definir la aleatoriedad de Martin-Löf mediante tests de nulidad.",
            "Entender la constante Ω de Chaitin como número real no computable.",
            "Relacionar la aleatoriedad algorítmica con la incompresibilidad de Kolmogorov.",
        ],
        vt=[
            ("../05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md",
             "Complejidad de Kolmogorov"),
            ("10-jerarquia-aritmetica.md", "Jerarquía aritmética"),
        ],
    ),

    # ─── Módulo 04 ───────────────────────────────────────────────────────────
    "04-complejidad-computacional/01-p-np-y-np-completitud.md": dict(
        d="⭐⭐ Intermedio", t="~25 min",
        pre=[("../03-computabilidad/04-maquinas-de-turing.md", "Máquinas de Turing"),
             ("05-complejidad-temporal-de-algoritmos.md",
              "Complejidad temporal de algoritmos")],
        obj=[
            "Definir las clases P y NP mediante máquinas de Turing deterministas y no deterministas.",
            "Demostrar la NP-completitud de SAT con el teorema de Cook-Levin.",
            "Entender el significado de la conjetura P ≠ NP y sus implicaciones.",
        ],
        vt=[
            ("02-reducciones-polinomicas.md", "Reducciones polinómicas"),
            ("03-sat-y-3-sat.md", "SAT y 3-SAT"),
        ],
    ),
    "04-complejidad-computacional/02-reducciones-polinomicas.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud")],
        obj=[
            "Construir reducciones polinómicas de muchos-a-uno entre problemas NP.",
            "Demostrar la NP-completitud de Clique, Vertex Cover e Independent Set.",
            "Distinguir entre reducción Karp y reducción Cook (con oráculo).",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("03-sat-y-3-sat.md", "SAT y 3-SAT"),
        ],
    ),
    "04-complejidad-computacional/03-sat-y-3-sat.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
             ("../01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md",
              "Lógica booleana")],
        obj=[
            "Definir SAT, 3-SAT y sus variantes (MAX-SAT, k-SAT).",
            "Reducir SAT a 3-SAT en tiempo polinomial.",
            "Aplicar la reducción de 3-SAT a otros problemas NP-completos.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("09-teorema-pcp.md", "El teorema PCP"),
        ],
    ),
    "04-complejidad-computacional/04-complejidad-espacial.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud")],
        obj=[
            "Definir las clases PSPACE, L y NL y sus relaciones con P y NP.",
            "Enunciar el teorema de Savitch: NPSPACE = PSPACE.",
            "Demostrar que PSPACE-completitud mediante el problema TQBF.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("07-circuitos-booleanos.md", "Circuitos booleanos"),
        ],
    ),
    "04-complejidad-computacional/05-complejidad-temporal-de-algoritmos.md": dict(
        d="⭐ Básico", t="~15 min",
        pre=[("../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md",
               "Logaritmos y crecimiento")],
        obj=[
            "Analizar la complejidad temporal de algoritmos con notación O, Ω, Θ.",
            "Resolver recurrencias con el teorema maestro.",
            "Clasificar problemas estándar según su complejidad asintótica.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("../01-fundamentos-matematicos/03-combinatoria-y-conteo.md", "Combinatoria y conteo"),
        ],
    ),
    "04-complejidad-computacional/06-aproximacion-y-heuristicas.md": dict(
        d="⭐⭐ Intermedio", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud")],
        obj=[
            "Definir un algoritmo de aproximación de ratio α y sus garantías.",
            "Analizar el algoritmo greedy para Vertex Cover (ratio 2).",
            "Distinguir entre PTAS, FPTAS y los límites de la aproximabilidad.",
        ],
        vt=[
            ("09-teorema-pcp.md", "El teorema PCP e inaproximabilidad"),
            ("10-complejidad-parametrizada.md", "Complejidad parametrizada"),
        ],
    ),
    "04-complejidad-computacional/07-circuitos-booleanos.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("../01-fundamentos-matematicos/05-logica-booleana-y-proposicional.md",
               "Lógica booleana"),
             ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud")],
        obj=[
            "Definir circuitos booleanos, tamaño y profundidad.",
            "Relacionar las clases de circuitos AC0, NC1 con la jerarquía de complejidad.",
            "Entender el programa de circuitos como enfoque hacia la separación P/NP.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("../03-computabilidad/08-complejidad-descriptiva.md", "Complejidad descriptiva"),
        ],
    ),
    "04-complejidad-computacional/08-complejidad-aleatoria.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
             ("../01-fundamentos-matematicos/01-logaritmos-probabilidad-y-crecimiento.md",
              "Probabilidad")],
        obj=[
            "Definir las clases BPP, RP, ZPP y sus relaciones.",
            "Entender por qué se conjetura que BPP = P.",
            "Analizar la derandomización mediante generadores pseudoaleatorios.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("11-sharp-p-y-conteo.md", "#P y problemas de conteo"),
        ],
    ),
    "04-complejidad-computacional/09-teorema-pcp.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("02-reducciones-polinomicas.md", "Reducciones polinómicas"),
             ("06-aproximacion-y-heuristicas.md", "Aproximación y heurísticas")],
        obj=[
            "Enunciar el teorema PCP: NP = PCP(log n, 1).",
            "Entender cómo el teorema PCP implica cotas de inaproximabilidad.",
            "Relacionar la conjetura del juego único (UGC) con los límites de aproximación.",
        ],
        vt=[
            ("06-aproximacion-y-heuristicas.md", "Aproximación y heurísticas"),
            ("../03-computabilidad/08-complejidad-descriptiva.md", "Complejidad descriptiva"),
        ],
    ),
    "04-complejidad-computacional/10-complejidad-parametrizada.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud")],
        obj=[
            "Definir la clase FPT y distinguirla de XP.",
            "Aplicar la técnica de árbol de búsqueda acotado a k-Vertex Cover.",
            "Entender la kernelización y el ancho de árbol como herramientas FPT.",
        ],
        vt=[
            ("06-aproximacion-y-heuristicas.md", "Aproximación y heurísticas"),
            ("13-eth-seth-consecuencias.md", "ETH y SETH"),
        ],
    ),
    "04-complejidad-computacional/11-sharp-p-y-conteo.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud")],
        obj=[
            "Definir la clase #P y su relación con el permanente.",
            "Enunciar el teorema de Toda: PH ⊆ P^{#P}.",
            "Entender por qué contar soluciones es estrictamente más difícil que decidir.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("08-complejidad-aleatoria.md", "Complejidad aleatoria (BPP, RP)"),
        ],
    ),
    "04-complejidad-computacional/12-complejidad-de-comunicacion.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
             ("../02-teoria-informacion/02-informacion-mutua.md", "Información mutua")],
        obj=[
            "Definir el modelo Alice-Bob y la complejidad de comunicación D(f).",
            "Demostrar el lower bound de igualdad Ω(n) con el argumento de rango.",
            "Conectar la complejidad de comunicación con lower bounds de circuitos.",
        ],
        vt=[
            ("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("../02-teoria-informacion/02-informacion-mutua.md", "Información mutua"),
        ],
    ),
    "04-complejidad-computacional/13-eth-seth-consecuencias.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
             ("03-sat-y-3-sat.md", "SAT y 3-SAT")],
        obj=[
            "Enunciar la ETH y la SETH y distinguir sus conjeturas.",
            "Derivar lower bounds condicionales para LCS, Edit Distance y Diameter.",
            "Entender qué significa que un algoritmo sea «óptimo» bajo ETH.",
        ],
        vt=[
            ("10-complejidad-parametrizada.md", "Complejidad parametrizada"),
            ("03-sat-y-3-sat.md", "SAT y 3-SAT"),
        ],
    ),

    # ─── Módulo 05 ───────────────────────────────────────────────────────────
    "05-conexiones-y-aplicaciones/01-complejidad-de-kolmogorov.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("../03-computabilidad/04-maquinas-de-turing.md", "Máquinas de Turing")],
        obj=[
            "Definir la complejidad de Kolmogorov K(x) mediante el programa más corto.",
            "Entender la invarianza de K respecto de la máquina universal de referencia.",
            "Demostrar que K no es computable y relacionarlo con el problema de la parada.",
        ],
        vt=[
            ("../03-computabilidad/12-aleatoriedad-algoritmica.md", "Aleatoriedad algorítmica"),
            ("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
        ],
    ),
    "05-conexiones-y-aplicaciones/03-aprendizaje-automatico-e-informacion.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("../02-teoria-informacion/02-informacion-mutua.md", "Información mutua")],
        obj=[
            "Conectar la entropía de Shannon con la función de pérdida en clasificación.",
            "Interpretar el entrenamiento de redes neuronales como minimización de entropía cruzada.",
            "Distinguir este artículo de 05/05 (información en aprendizaje estadístico).",
        ],
        vt=[],  # ya tiene Véase también
    ),
    "05-conexiones-y-aplicaciones/05-informacion-en-aprendizaje.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("03-aprendizaje-automatico-e-informacion.md", "Aprendizaje automático e información"),
             ("../02-teoria-informacion/05-divergencia-kl-y-entropia-cruzada.md",
              "Divergencia KL y entropía cruzada")],
        obj=[
            "Aplicar la divergencia KL y la información de Fisher al aprendizaje estadístico.",
            "Entender el principio MDL (Minimum Description Length) como selección de modelos.",
            "Relacionar la complejidad del modelo con el sobreajuste desde la perspectiva informacional.",
        ],
        vt=[],  # ya tiene Véase también
    ),
    "05-conexiones-y-aplicaciones/02-criptografia-y-complejidad.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
             ("01-complejidad-de-kolmogorov.md", "Complejidad de Kolmogorov")],
        obj=[
            "Entender OTP, RSA y Diffie-Hellman desde el punto de vista de la complejidad.",
            "Relacionar la seguridad criptográfica con problemas computacionalmente difíciles.",
            "Comprender el rol de las funciones de un solo sentido en la criptografía moderna.",
        ],
        vt=[
            ("../04-complejidad-computacional/01-p-np-y-np-completitud.md", "P, NP y NP-completitud"),
            ("04-informacion-cuantica.md", "Información cuántica"),
        ],
    ),
    "05-conexiones-y-aplicaciones/04-informacion-cuantica.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("../01-fundamentos-matematicos/02-conjuntos-funciones-y-relaciones.md",
              "Álgebra lineal básica")],
        obj=[
            "Representar qubits como vectores en C² y operar con puertas unitarias.",
            "Calcular la entropía de von Neumann de una matriz densidad.",
            "Explicar el protocolo de teleportación cuántica.",
        ],
        vt=[
            ("02-criptografia-y-complejidad.md", "Criptografía y complejidad"),
            ("06-informacion-y-termodinamica.md", "Información y termodinámica"),
        ],
    ),
    "05-conexiones-y-aplicaciones/06-informacion-y-termodinamica.md": dict(
        d="⭐⭐⭐ Avanzado", t="~25 min",
        pre=[("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre")],
        obj=[
            "Demostrar que la entropía de Shannon y la de Boltzmann son la misma cantidad.",
            "Explicar el exorcismo del demonio de Maxwell con el principio de Landauer.",
            "Calcular el coste energético mínimo de borrar 1 bit a temperatura T.",
        ],
        vt=[
            ("04-informacion-cuantica.md", "Información cuántica"),
            ("../02-teoria-informacion/10-entropia-diferencial.md", "Entropía diferencial"),
        ],
    ),
    "05-conexiones-y-aplicaciones/07-informacion-y-biologia.md": dict(
        d="⭐⭐⭐ Avanzado", t="~20 min",
        pre=[("../02-teoria-informacion/01-entropia-incertidumbre.md", "Entropía e incertidumbre"),
             ("../02-teoria-informacion/06-codigos-correctores-de-errores.md",
              "Códigos correctores de errores")],
        obj=[
            "Cuantificar la redundancia del código genético como código corrector.",
            "Aplicar la información de Fisher al contexto de la selección natural.",
            "Estimar la entropía del genoma humano y comparar con límites de Shannon.",
        ],
        vt=[
            ("../02-teoria-informacion/06-codigos-correctores-de-errores.md",
             "Códigos correctores de errores"),
            ("06-informacion-y-termodinamica.md", "Información y termodinámica"),
        ],
    ),
    "05-conexiones-y-aplicaciones/08-mapa-de-conexiones.md": dict(
        d="⭐ Básico", t="~15 min",
        pre=[],
        obj=[
            "Identificar las conexiones transversales entre los cinco módulos del tutorial.",
            "Localizar el resultado o herramienta más relevante para un problema dado.",
            "Planificar rutas de profundización tras completar el tutorial.",
        ],
        vt=[
            ("../00-presentacion/01-mapa-del-territorio.md", "Mapa del territorio"),
            ("../00-presentacion/02-rutas-de-profundizacion.md", "Rutas de profundización"),
        ],
    ),
}

# ─── Helpers ────────────────────────────────────────────────────────────────

DIFFICULTY_BADGE = {
    "⭐ Básico":       "⭐ Básico",
    "⭐⭐ Intermedio":  "⭐⭐ Intermedio",
    "⭐⭐⭐ Avanzado":  "⭐⭐⭐ Avanzado",
}


def make_metadata_line(d, t):
    return f"> **Dificultad:** {d} · **Tiempo de lectura:** {t}\n"


def make_prereqs_section(pre):
    if not pre:
        return "## Prerrequisitos\n\nNinguno — este artículo es punto de entrada.\n\n"
    lines = ["## Prerrequisitos\n\n"]
    for path, name in pre:
        lines.append(f"- [{name}]({path})\n")
    lines.append("\n")
    return "".join(lines)


def make_objetivos_section(obj):
    lines = ["## Objetivos de aprendizaje\n\n"]
    for i, o in enumerate(obj, 1):
        lines.append(f"{i}. {o}\n")
    lines.append("\n")
    return "".join(lines)


def make_vease_tambien_section(vt):
    lines = ["## Véase también\n\n"]
    for path, name in vt:
        lines.append(f"- [{name}]({path})\n")
    lines.append("\n")
    return "".join(lines)


def process_article(rel_path, meta):
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        print(f"  SKIP (no existe): {rel_path}")
        return

    with open(full_path, encoding="utf-8") as f:
        content = f.read()

    original = content

    # ── 1. Metadata line after H1 ──────────────────────────────────────────
    if "**Dificultad:**" not in content and "Dificultad:" not in content:
        h1_match = re.match(r"(# .+\n)", content)
        if h1_match:
            insert_pos = h1_match.end()
            meta_line = "\n" + make_metadata_line(meta["d"], meta["t"]) + "\n"
            content = content[:insert_pos] + meta_line + content[insert_pos:]

    # ── 2+3. Prerrequisitos + Objetivos (inserted together, in order) ──────
    needs_pre = "## Prerrequisitos" not in content
    needs_obj = "## Objetivos de aprendizaje" not in content

    if needs_pre or needs_obj:
        block = ""
        if needs_pre:
            block += make_prereqs_section(meta["pre"])
        if needs_obj:
            block += make_objetivos_section(meta["obj"])
        # Insert the whole block before the first content ## heading
        first_h2 = re.search(r"\n## ", content)
        if first_h2:
            content = content[:first_h2.start()] + "\n" + block + content[first_h2.start():]
        else:
            content = content.rstrip() + "\n\n" + block

    # ── 4. Véase también section ──────────────────────────────────────────
    if "## Véase también" not in content and meta.get("vt"):
        ref_match = re.search(r"\n## Referencias\b", content)
        vt_block = "\n" + make_vease_tambien_section(meta["vt"])
        if ref_match:
            content = content[:ref_match.start()] + vt_block + content[ref_match.start():]
        else:
            content = content.rstrip() + "\n" + vt_block

    if content != original:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  OK: {rel_path}")
    else:
        print(f"  UNCHANGED: {rel_path}")


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    for rel_path, meta in METADATA.items():
        process_article(rel_path, meta)
    print("\nDone.")
