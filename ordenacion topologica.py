""" Algoritmo de Ordenación Topológica

 Objetivo:
 Este algoritmo calcula una ordenación topológica de un conjunto de tareas
 sujeto a ciertas restricciones de precedencia. Una ordenación topológica
 es un orden lineal de los nodos de un grafo dirigido tal que para cada arista
 dirigida (u, v) desde el nodo u al nodo v, el nodo u aparece antes en el orden
 que el nodo v.

 Variables de entrada:
 - n: El número total de tareas.
 - restricciones: Una lista de pares (i, j) donde cada par indica que la tarea i
   debe ser completada antes de que la tarea j pueda comenzar.
 Variables de salida:
 - ordenamiento: Una lista que representa la ordenación topológica de las tareas.
   Si no es posible una ordenación debido a restricciones contradictorias, devuelve None.

 Funcionalidad:
 1. Se construye un grafo dirigido donde cada nodo representa una tarea y las aristas
    representan las restricciones de precedencia entre las tareas.
 2. Se utiliza un algoritmo de búsqueda en profundidad (DFS) para recorrer el grafo
    y generar una lista de ordenamiento topológico.
 3. Si no es posible generar una ordenación debido a restricciones contradictorias,
    se devuelve None. En caso contrario, se devuelve la lista de ordenamiento topológico.
"""
def ordenacion_topologica(n, restricciones):
    # Crear un diccionario para almacenar las relaciones de precedencia
    grafo = {}
    # Inicializamos el grafo con listas vacías para cada tarea
    for i in range(1, n + 1):
        grafo[i] = []

    # Llenar el grafo con las restricciones
    for restriccion in restricciones:
        # Cada restricción es una tupla (i, j) donde i precede a j
        tarea_anterior, tarea_siguiente = restriccion
        # Añadimos la tarea_siguiente a la lista de tareas a las que precede la tarea_anterior
        grafo[tarea_anterior].append(tarea_siguiente)

    # Función auxiliar para realizar la búsqueda en profundidad (DFS)
    def dfs(v):
        # Marcar el nodo como visitado
        visited[v] = True
        # Recorrer todas las tareas a las que precede este nodo
        for u in grafo[v]:
            # Si la tarea a la que precede no ha sido visitada, visitarla
            if not visited[u]:
                dfs(u)
        # Después de visitar todas las tareas a las que precede este nodo, añadirlo al ordenamiento
        ordenamiento.append(v)

    # Inicializar la lista de visitados y la lista de ordenamiento
    visited = [False] * (n + 1)
    ordenamiento = []

    # Realizar la búsqueda en profundidad (DFS) desde cada nodo no visitado
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)

    # Si no se visitaron todos los nodos, no hay ordenación posible
    if len(ordenamiento) != n:
        return None
    else:
        # Devolver el ordenamiento topológico invertido (porque se está construyendo desde el final)
        return ordenamiento[::-1]

# Ejemplo de uso
n = 5
restricciones = [(1, 2), (2, 3), (2, 4), (3, 5), (4, 5)]

orden = ordenacion_topologica(n, restricciones)
if orden:
    print("Ordenación topológica:", orden)
else:
    print("No es posible una ordenación topológica debido a las restricciones.")
