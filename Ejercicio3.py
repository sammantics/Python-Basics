# Ejercicio 3: Escriba una función que elimine todas las apariciones de un elemento en una
# lista.

#Se establecen las listas deseadas.

lista = [20, 30, 40, 20, 5, 100, 5, 20]
lista2 = ['perro', 'gato', 'sombrero', 'gato', 'zanahoria']

#La función .remove() especifica cuales elementos 

lista.remove(20)
lista.remove(30)
lista2.remove('perro')
lista2.remove('gato')
lista2.remove('gato')

print(lista)
print(lista2)