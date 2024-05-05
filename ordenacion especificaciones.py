"""
Propósito:
Verificar si un segmento en una tabla t ha sido explorado correctamente, siguiendo ciertos pasos específicos en este caso el índice inicio debe ser menor o igual que el índice fin.

devuelve:
        bool: True si el segmento se ha explorado correctamente, False de lo contrario.

Parámetros de Entrada:
lista: La tabla de componentes.
inicio: El índice de inicio del segmento.
fin: El índice de fin del segmento.
Salida:
Un valor booleano que indica si el segmento ha sido explorado correctamente.
"""

def exploracion_segmento(lista, inicio, fin):
    # Verificar que los índices sean válidos y que el segmento no esté vacío
    if not (0 <= inicio < len(lista)) or not (0 <= fin < len(lista)) or inicio >= fin:
        return False

    # Encontrar el índice del máximo dentro del segmento
    indice_maximo = inicio + lista[inicio:fin + 1].index(max(lista[inicio:fin + 1]))

    # Verificar si el máximo está en la posición correcta
    if indice_maximo != fin:
        return False

    # Desplazar los elementos del segmento a la izquierda, manteniendo el orden
    lista[inicio:fin] = lista[inicio:indice_maximo] + lista[indice_maximo + 1:fin + 1]

    # Colocar el máximo al final del segmento
    lista[fin] = max(lista[inicio:fin + 1])

    return True

# Ejemplo de uso con un segmento no correctamente explorado
valores = [5, 10, 6, 9, 7, 15, 14]
inicio_incorrecto = 2
fin_incorrecto = 6
exploracion_incorrecta = exploracion_segmento(valores, inicio_incorrecto, fin_incorrecto)
print("¿Segmento (incorrecto) explorado correctamente?", exploracion_incorrecta)
print("Lista modificada (incorrecta):", valores)

# Restaurar la lista a su estado original para un ejemplo correcto
valores = [5, 10, 6, 9, 7, 15, 14]
inicio_correcto = 3
fin_correcto = 5
exploracion_correcta = exploracion_segmento(valores, inicio_correcto, fin_correcto)
print("¿Segmento (correcto) explorado correctamente?", exploracion_correcta)
print("Lista modificada (correcta):", valores)
