# Función alterad 2.py 

# Función 2:Crea un programa que elimine los elementos repetidos de una lista.

# # Versión original de la tarea 2

# lista = [1, 2, 2, 3, 4, 4, 5] # Se hace entero de la lista.

# nuevalista = set(lista) # se usa set() para remover elementos repetidos.

# print(nuevalista) # se imprime el nuevo entero con los elementos duplicados removidos.



# Versión alterada usando la función map()

lista_de_listas = [[1, 2, 2, 3], [3, 4, 4, 5], [6, 7, 7, 8, 8]] # Se define la variable de la lista_de_listas.

nueva_lista_de_listas = list(map(lambda lst: list(set(lst)), lista_de_listas)) #se define la nueva variable por medio de map(). Lamb La función lambda se define al tomar una lista como entrada (lst), la convierte en un conjunto para eliminar duplicados usando la función set() y luego la vuelve a convertir en una lista.

 # map() luego continua aplicando la funsión de set() a las listas internas de lista_de_listas. El resultado se vcovnirte en una lista nueva usando la función de list().

print(nueva_lista_de_listas) # Se genera la nueva lista dentro de la variable nueva_lista_de_listas y se imprime las listas sin resultado.

# Referencia bibliográfica:

# Programación ATS (12 de dicimebre 2018) 34. Programación en Python | Colecciones | Ejercicio 1 – Eliminar duplicados de una lista https://www.youtube.com/watch?v=Nl_CxwKaZJk