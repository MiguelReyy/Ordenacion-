# Ordenacion- Miguel Rey Carballo

# 1 Ordenacion por Insercion Dicotomica
Este proyecto implementa un algoritmo para ordenar una lista utilizando el método de inserción dicotómica con búsqueda binaria para encontrar las posiciones correctas de inserción.

## Introducción

El objetivo de este proyecto es implementar un método de ordenación que combine la eficiencia de la búsqueda binaria con el método de inserción. El algoritmo sigue estos pasos:

1. **Recorrido Inicial:**
   - Se recorre la lista desde el segundo elemento hasta el final.
   - Cada elemento se trata como una "clave" que debe colocarse en el lugar correcto dentro de la sección ya ordenada.

2. **Búsqueda de Posición:**
   - Para cada "clave", se usa la técnica de búsqueda binaria para localizar la posición exacta donde debe insertarse dentro de la parte previamente ordenada.
   - La búsqueda binaria descarta la mitad de las posiciones posibles en cada paso.

3. **Inserción y Desplazamiento:**
   - Una vez identificada la posición correcta, la clave se inserta ahí.
   - Los elementos existentes entre esa posición y la posición original de la clave se desplazan para hacer espacio.

# 2 Una ordenación topológica 

Este proyecto implementa un algoritmo de ordenación topológica utilizando el algoritmo de Kahn para ordenar una serie de tareas con restricciones de precedencia.

## Introducción

La ordenación topológica es un método para organizar tareas que dependen unas de otras. El algoritmo de Kahn proporciona un enfoque eficiente usando un grafo dirigido acíclico (DAG). 

### Pasos Principales:

1. **Construcción del Grafo:** 
   - Se crea una representación de las tareas usando listas de adyacencia para modelar las dependencias.

2. **Cálculo de Grados de Entrada:**
   - Cada nodo (tarea) mantiene un conteo del número de nodos que dependen de él, conocido como el grado de entrada.

3. **Cola de Nodos Sin Dependencias:**
   - Se utiliza una cola para manejar los nodos con un grado de entrada cero, indicando que no tienen dependencias.

4. **Proceso de Ordenación:**
   - Se saca cada nodo de la cola, se agrega al orden resultante y se reducen los grados de entrada de sus nodos sucesores.
   - Los nodos sucesores con grado de entrada reducido a cero se agregan a la cola para su procesamiento posterior.

# 3 Completar las especificaciones
Este proyecto implementa un algoritmo que verifica si un segmento de una lista ha sido explorado correctamente, según un conjunto de reglas específicas.

## Introducción

El objetivo de este proyecto es identificar si un segmento de una lista cumple con las siguientes reglas:

1. **Identificación del Máximo:** El valor máximo dentro del segmento debe ser el primer elemento.
2. **Desplazamiento:** Todos los elementos en el segmento se desplazan una posición hacia la izquierda, excepto el máximo.
3. **Colocación del Máximo:** El valor máximo se coloca en la última posición del segmento.

## Uso

Para utilizar el código, sigue estos pasos:

1. **Definir los Datos:**
   - Define una lista `valores` que contenga los datos con los que deseas trabajar.
   - Especifica el rango `inicio` y `fin` que define el segmento a explorar.

2. **Ejecutar la Verificación:**
   - Llama a la función `segmento_explorado(valores, inicio, fin)`.
   - Esta función retornará `True` si el segmento fue correctamente explorado según las reglas, o `False` si no cumple con las condiciones.

3. **Resultados:**
   - La lista original se modificará para reflejar el estado del segmento explorado.
