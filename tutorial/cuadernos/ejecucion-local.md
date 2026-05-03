# Ejecución local de cuadernos

Los cuadernos Jupyter del tutorial están pensados para ejecutarse con una
instalación mínima de Python. La mayoría de celdas usa solo la biblioteca
estándar; `matplotlib` se usa únicamente para gráficas.

## Crear un entorno

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Abrir Jupyter

Con el entorno activado:

```bash
jupyter notebook
```

También puede usarse JupyterLab si está disponible:

```bash
jupyter lab
```

## Convenciones

- Los cuadernos de `ejemplos` muestran conceptos ya explicados en los artículos.
- Los cuadernos de `ejercicios` están pensados para modificar celdas y completar
  prácticas.
- Las salidas no se guardan por defecto para mantener el repositorio ligero.
- Si una gráfica no aparece en un entorno concreto, las celdas numéricas siguen
  siendo suficientes para revisar el resultado.

## Problemas habituales

Si `matplotlib` no está instalado, algunos cuadernos omitirán la gráfica y
mostrarán un mensaje. Instalar las dependencias con `requirements.txt` resuelve
ese caso.
