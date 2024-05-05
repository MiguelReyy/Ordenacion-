"""
# Algoritmo de Ordenación "En Su Lugar" para una Tabla de una Sola Línea
#
# Objetivo:
# Este algoritmo ordena una tabla de una sola línea de componentes comparables "en su lugar",
# es decir, sin utilizar estructuras de datos adicionales para almacenar los elementos ordenados.
#
# Variables de entrada:
# - t: Una tabla de una sola línea que contiene los elementos a ordenar. Los elementos deben ser comparables.
#
# Variables de salida:
# - La tabla de entrada 't' será modificada y contendrá los elementos ordenados.
#
# Funcionalidad:
# 1. Se crea una tabla vacía 'r' con el mismo tamaño que 't'.
# 2. Por cada elemento 'x' en 't', se busca su posición correcta en 'r' para mantener el orden.
# 3. Se inserta 'x' en la posición correcta en 'r' sin cambiar el orden de los elementos previamente insertados.
# 4. Una vez que todos los elementos se han insertado en 'r', se copian de regreso a 't' para actualizar la tabla original.
#
# Complejidad:
# - La complejidad de este algoritmo es de O(n^2), donde 'n' es el número de elementos en la tabla 't'.
#   Esto se debe a que, en el peor escenario, para cada elemento en 't', se debe recorrer 'r' para encontrar
#   su posición correcta, lo que requiere comparaciones lineales.

"""

def ordenar_en_su_lugar(t):
    # Crear una tabla vacía con el mismo tamaño que t
    r = [None] * len(t)

    # Iterar sobre cada elemento en t
    for x in t:
        # Buscar la posición correcta de x en r manteniendo el orden
        insertar_en = 0
        while insertar_en < len(r) and (r[insertar_en] is not None and r[insertar_en] < x):
            insertar_en += 1
        
        # Insertar x en la posición correcta en r
        if insertar_en < len(r):
            r.insert(insertar_en, x)
            r.pop()
        else:
            r[-1] = x

    # Copiar los elementos ordenados de r a t
    for i, elemento in enumerate(r):
        t[i] = elemento

# Ejemplo de uso
t = [9, 5, 3, 7, 1, 8]
print("Tabla antes de ordenar:", t)
ordenar_en_su_lugar(t)
print("Tabla después de ordenar:", t)
