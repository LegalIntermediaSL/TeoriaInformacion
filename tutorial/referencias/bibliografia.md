# Bibliografía ampliada

Selección curada de libros y artículos de referencia, organizada por tema y
nivel de dificultad. Los marcados con ★ son especialmente recomendados como
punto de entrada.

---

## Teoría de la información

### Textos introductorios y de referencia

- ★ **Cover, T. M. y Thomas, J. A.** (2006). *Elements of Information Theory* (2ª ed.). Wiley.
  El texto estándar universitario. Cubre entropía, canales, tasa-distorsión, compresión universal y Kolmogorov. Imprescindible.

- ★ **MacKay, D. J. C.** (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.
  Acceso libre en [inference.org.uk](http://www.inference.org.uk/mackay/itila/). Enfoque probabilístico y conexión con ML. Muy legible.

- **Gallager, R. G.** (1968). *Information Theory and Reliable Communication*. Wiley.
  Tratamiento riguroso de canales y codificación. Clásico de ingeniería.

- **Csiszár, I. y Körner, J.** (2011). *Information Theory: Coding Theorems for Discrete Memoryless Systems* (2ª ed.). Cambridge University Press.
  Tratamiento matemático avanzado. Para profundizar en la teoría de la información en redes.

### Artículos fundacionales

- **Shannon, C. E.** (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423 y 623–656.
  El artículo que fundó el campo. Lectura obligatoria histórica.

- **Shannon, C. E.** (1959). Coding theorems for a discrete source with a fidelity criterion. *IRE National Convention Record*, 4, 142–163.
  Fundación de la teoría de tasa-distorsión.

- **Huffman, D. A.** (1952). A method for the construction of minimum-redundancy codes. *Proc. IRE*, 40(9), 1098–1101.

---

## Codificación de canal y códigos modernos

### Libros

- ★ **Richardson, T. y Urbanke, R.** (2008). *Modern Coding Theory*. Cambridge University Press.
  Códigos LDPC, turbo, polares y análisis de density evolution. El texto de referencia moderno.

- **Lin, S. y Costello, D. J.** (2004). *Error Control Coding* (2ª ed.). Prentice Hall.
  Amplio y detallado. Cubre desde Hamming hasta turbo y LDPC.

- **Moon, T. K.** (2005). *Error Correction Coding: Mathematical Methods and Algorithms*. Wiley.
  Enfoque algorítmico. Buen complemento a Richardson-Urbanke.

### Artículos clave

- **Gallager, R. G.** (1962). Low-density parity-check codes. *IRE Trans. Information Theory*, 8(1), 21–28. — Fundación de LDPC.

- **Berrou, C., Glavieux, A. y Thitimajshima, P.** (1993). Near Shannon limit error-correcting coding and decoding: Turbo-codes. *Proc. IEEE ICC*, 1064–1070. — Fundación de turbo codes.

- **Bahl, L. R., Cocke, J., Jelinek, F. y Raviv, J.** (1974). Optimal decoding of linear codes for minimizing symbol error rate. *IEEE Trans. Information Theory*, 20(2), 284–287. — Algoritmo BCJR.

- **Arıkan, E.** (2009). Channel polarization: A method for constructing capacity-achieving codes. *IEEE Trans. Information Theory*, 55(7), 3051–3073. — Fundación de códigos polares.

- **Tal, I. y Vardy, A.** (2015). List decoding of polar codes. *IEEE Trans. Information Theory*, 61(5), 2428–2451. — SCL, estándar práctico.

---

## Compresión de datos y codificación universal

### Libros

- ★ **Salomon, D. y Motta, G.** (2010). *Handbook of Data Compression* (5ª ed.). Springer.
  Referencia exhaustiva: LZ77, LZ78, Huffman, aritmética, BWT, codificación de imagen y vídeo.

- **Sayood, K.** (2017). *Introduction to Data Compression* (5ª ed.). Morgan Kaufmann.
  Texto universitario accesible. Buen equilibrio entre teoría y práctica.

- **Bell, T. C., Cleary, J. G. y Witten, I. H.** (1990). *Text Compression*. Prentice Hall.
  El libro clásico sobre compresión de texto. LZ, PPM, codificación aritmética.

### Artículos clave

- **Ziv, J. y Lempel, A.** (1977). A universal algorithm for sequential data compression. *IEEE Trans. Information Theory*, 23(3), 337–343. — LZ77.

- **Lempel, A. y Ziv, J.** (1978). Compression of individual sequences via variable-rate coding. *IEEE Trans. Information Theory*, 24(5), 530–536. — LZ78.

- **Welch, T. A.** (1984). A technique for high-performance data compression. *IEEE Computer*, 17(6), 8–19. — LZW.

- **Witten, I. H., Neal, R. y Cleary, J. G.** (1987). Arithmetic coding for data compression. *Commun. ACM*, 30(6), 520–540.

- **Cilibrasi, R. y Vitányi, P.** (2005). Clustering by compression. *IEEE Trans. Information Theory*, 51(4), 1523–1545. — Distancia de compresión normalizada (NCD).

---

## Computabilidad y teoría de la computación

### Textos introtorios y de referencia

- ★ **Sipser, M.** (2013). *Introduction to the Theory of Computation* (3ª ed.). Cengage Learning.
  El texto universitario estándar. Claro, riguroso y bien estructurado.

- **Hopcroft, J. E., Motwani, R. y Ullman, J. D.** (2006). *Introduction to Automata Theory, Languages, and Computation* (3ª ed.). Pearson.
  Más detallado que Sipser en autómatas y gramáticas. Clásico del campo.

- **Rogers, H.** (1987). *Theory of Recursive Functions and Effective Computability*. MIT Press.
  Tratamiento matemático avanzado de computabilidad. Para profundizar.

- **Davis, M.** (1958). *Computability and Unsolvability*. McGraw-Hill.
  El texto clásico original sobre indecidibilidad.

### Complejidad de Kolmogorov y aleatoriedad algorítmica

- ★ **Li, M. y Vitányi, P.** (2008). *An Introduction to Kolmogorov Complexity and Its Applications* (3ª ed.). Springer.
  La referencia definitiva sobre complejidad de Kolmogorov.

- **Chaitin, G. J.** (1975). A theory of program size formally identical to information theory. *J. ACM*, 22(3), 329–340.

- **Martin-Löf, P.** (1966). The definition of random sequences. *Information and Control*, 9(6), 602–619.

- **Nies, A.** (2009). *Computability and Randomness*. Oxford University Press.

---

## Complejidad computacional

### Textos de referencia

- ★ **Arora, S. y Barak, B.** (2009). *Computational Complexity: A Modern Approach*. Cambridge University Press.
  Acceso libre en [theory.cs.princeton.edu](http://theory.cs.princeton.edu/complexity/). La referencia actual del campo.

- **Papadimitriou, C. H.** (1994). *Computational Complexity*. Addison-Wesley.
  Clásico formal. Excelente para PSPACE, jerarquía polinómica y conteo.

- **Moore, C. y Mertens, S.** (2011). *The Nature of Computation*. Oxford University Press.
  Visión interdisciplinar: física, matemáticas, complejidad. Muy recomendable como lectura complementaria.

### Inaproximabilidad y teorema PCP

- **Arora, S. y Safra, S.** (1998). Probabilistic checking of proofs. *J. ACM*, 45(1), 70–122.

- **Arora, S. et al.** (1998). Proof verification and the hardness of approximation problems. *J. ACM*, 45(2), 501–555.

- **Dinur, I.** (2007). The PCP theorem by gap amplification. *J. ACM*, 54(3), 12.

- **Håstad, J.** (2001). Some optimal inapproximability results. *J. ACM*, 48(4), 798–859.

- **Vazirani, V. V.** (2001). *Approximation Algorithms*. Springer.

### Complejidad parametrizada y fine-grained

- **Cygan, M. et al.** (2015). *Parameterized Algorithms*. Springer. Acceso libre.

- **Downey, R. G. y Fellows, M. R.** (2013). *Fundamentals of Parameterized Complexity*. Springer.

- **Impagliazzo, R. y Paturi, R.** (2001). On the complexity of k-SAT. *J. Comput. Syst. Sci.*, 62(2), 367–375. — ETH.

---

## Información cuántica

### Textos de referencia

- ★ **Nielsen, M. A. y Chuang, I. L.** (2010). *Quantum Computation and Quantum Information* (10th anniversary ed.). Cambridge University Press.
  La referencia estándar. Exhaustivo.

- **Watrous, J.** (2018). *The Theory of Quantum Information*. Cambridge University Press.
  Acceso libre. Enfoque matemático riguroso. Excelente para información cuántica avanzada.

- **Aaronson, S.** (2013). *Quantum Computing Since Democritus*. Cambridge University Press.
  Divulgación rigurosa. Conecta computación cuántica con complejidad y filosofía.

- **Wilde, M. M.** (2017). *Quantum Information Theory* (2ª ed.). Cambridge University Press.
  Acceso libre. Cubre capacidad cuántica, entrelazamiento y corrección de errores cuánticos.

---

## Aprendizaje automático e información

### Textos de referencia

- ★ **Goodfellow, I., Bengio, Y. y Courville, A.** (2016). *Deep Learning*. MIT Press.
  Acceso libre en [deeplearningbook.org](http://www.deeplearningbook.org). Perspectiva informacional en caps. 3, 5 y 20.

- **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer.
  Tratamiento bayesiano. KL, entropía cruzada y modelos generativos.

- **Vapnik, V.** (1998). *Statistical Learning Theory*. Wiley. — Bases teóricas del aprendizaje.

### Cuello de botella y redes neuronales

- **Tishby, N., Pereira, F. y Bialek, W.** (1999). The information bottleneck method. *Allerton Conference*.

- **Alemi, A. A. et al.** (2017). Deep variational information bottleneck. *ICLR 2017*.

- **Shwartz-Ziv, R. y Tishby, N.** (2017). Opening the black box of deep neural networks via information. arXiv:1703.00810.

- **Saxe, A. M. et al.** (2018). On the information bottleneck theory of deep learning. *ICLR 2018*.

### Información mutua y estimación

- **Belghazi, M. I. et al.** (2018). MINE: Mutual information neural estimation. *ICML 2018*.

- **Poole, B. et al.** (2019). On variational bounds of mutual information. *ICML 2019*.

---

## Geometría de la información

- ★ **Amari, S.** (2016). *Information Geometry and Its Applications*. Springer.

- **Amari, S. y Nagaoka, H.** (2000). *Methods of Information Geometry*. AMS/Oxford.

- **Nielsen, F.** (2020). An elementary introduction to information geometry. *Entropy*, 22(10), 1100.

- **Martens, J.** (2020). New insights and perspectives on the natural gradient method. *JMLR*, 21, 146.

---

## MDL y complejidad estocástica

- ★ **Grünwald, P.** (2007). *The Minimum Description Length Principle*. MIT Press.

- **Rissanen, J.** (1978). Modeling by shortest data description. *Automatica*, 14(5), 465–471.

- **Rissanen, J.** (1989). *Stochastic Complexity in Statistical Inquiry*. World Scientific.

- **Barron, A., Rissanen, J. y Yu, B.** (1998). The minimum description length principle in coding and modeling. *IEEE Trans. Inf. Theory*, 44(6), 2743–2760.

---

## Información y física / biología

### Termodinámica e información

- **Landauer, R.** (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.*, 5(3), 183–191.

- **Bennett, C. H.** (1982). The thermodynamics of computation. *Int. J. Theor. Phys.*, 21(12), 905–940.

- **Szilard, L.** (1929). Über die Entropieverminderung in einem thermodynamischen System. *Z. Phys.*, 53, 840–856.

### Biología e información

- **Adami, C.** (2004). Information theory in molecular biology. *Physics of Life Reviews*, 1(1), 3–22.

- **Schneider, T. D. y Stephens, R. M.** (1990). Sequence logos: A new way to display consensus sequences. *Nucleic Acids Research*, 18(20), 6097–6100.

---

## Criptografía y complejidad

- ★ **Katz, J. y Lindell, Y.** (2020). *Introduction to Modern Cryptography* (3ª ed.). CRC Press.

- **Goldreich, O.** (2001). *Foundations of Cryptography*, vol. 1. Cambridge University Press.

- **Shannon, C. E.** (1949). Communication theory of secrecy systems. *Bell System Technical Journal*, 28(4), 656–715. — Fundación teórico-informacional de la criptografía.

---

## Recursos libres en línea

| Recurso | Autor | URL |
|---------|-------|-----|
| *Information Theory, Inference, and Learning Algorithms* | D. MacKay | inference.org.uk/mackay/itila |
| *Computational Complexity: A Modern Approach* | Arora y Barak | theory.cs.princeton.edu/complexity |
| *Parameterized Algorithms* | Cygan et al. | parameterized.mimuw.edu.pl |
| *Quantum Information Theory* | M. Wilde | arxiv.org/abs/1106.1445 |
| *The Theory of Quantum Information* | J. Watrous | cs.uwaterloo.ca/~watrous/TQI |
| *Deep Learning* | Goodfellow et al. | deeplearningbook.org |
| *Entropy and Information Theory* | R. Gray | ee.stanford.edu/~gray/it.html |
| Lecture notes de complejidad (MIT 6.045) | M. Sipser | ocw.mit.edu |
| Lecture notes de información (Stanford EE376A) | T. Weissman | web.stanford.edu/class/ee376a |
