# Algoritmo de Ordenación en Su Lugar para una Tabla de una Sola Línea
#
# Objetivo:
# Este algoritmo ordena una tabla de una sola línea de componentes comparables en su lugar,
# es decir, sin utilizar estructuras de datos adicionales para almacenar los elementos ordenados.
#
# Variables de entrada:
# - t: Una tabla de una sola línea que contiene los elementos a ordenar. Los elementos deben ser comparables.
#
# Variables de salida:
# - La tabla de entrada 't' será modificada y contendrá los elementos ordenados.
#
# Funcionalidad:
# 1. El algoritmo recorre la tabla 't' y compara cada elemento con los elementos restantes.
# 2. Si encuentra un elemento mayor que el siguiente, los intercambia.
# 3. Repite este proceso hasta que todos los elementos estén en orden.
#
# Complejidad:
# - La complejidad de este algoritmo es de O(n^2), donde n es el número de elementos en la tabla 't'.
#   Esto se debe a que hay dos bucles anidados que recorren la tabla, y en el peor caso,
#   cada elemento necesita ser comparado con todos los demás elementos.
#

def ordenar_en_su_lugar(t):
    # Obtener la longitud de la tabla
    n = len(t)
    
    # Verificar la precondición
    if n < 2:
        return  # No se puede ordenar una tabla con menos de dos elementos

    # Iterar sobre la tabla
    for i in range(n - 1):  # El último elemento no necesita ser comparado
        # Iterar sobre la porción no ordenada de la tabla
        for j in range(i + 1, n):
            # Si el elemento actual es mayor que el siguiente, intercambiar
            if t[i] > t[j]:
                t[i], t[j] = t[j], t[i]  # Intercambio de elementos

# Ejemplo de uso
t = [9, 5, 3, 7, 1, 8]
print("Tabla antes de ordenar:", t)
ordenar_en_su_lugar(t)
print("Tabla después de ordenar:", t)
