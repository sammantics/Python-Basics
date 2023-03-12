# Función 1: Escribir una función que reciba un número del usuario y despliegue en pantalla el siguiente patrón de números llegando hasta el número elegido:

# Versión original de la tarea 2
n = int(input("Insertar número: "))  # Se crear una opción interactiva para que el usuario inserte el número.

for i in range(1, n+1):  # Se genera una ciclo de serie de número desde 1 a n+1,según número insertado por usuario.
    for j in range(1, i+1):  #  En el ciclo interno, se genera la variable J para un ciclo númerico.
        print(j, end=" ")  # Despues de cada ciclo interno se imprime en función de J, segúido un espacio para separar cada ciclo númerico hasta que el ciclo se complete de 1 a n.
    print()  # move to the next line
    
# Versión alterada usando la función map()

# Se crear una opción interactiva para que el usuario inserte el número declarado como un entero y se denomina n.
n = int(input("Insertar número: "))

# se define la función lambda  por la variable 'patron', toma la variable x que aplica un string de digitos entre 1 a x.
patron = lambda x: ''.join(str(i) for i in range(1, x+1))

# La función map() aplica la función de patron al rango de entero entre 1 a n. Esto hace que el rtango de 1 a n se repita igual que x.
resultado = list(map(patron, range(1, n+1)))

# Se incluyen dentro de la variable 'resultado' y se imprime dentro de la variable 'fila' con la función de print().
for fila in resultado:
    print(fila)

# Referencia bibliográfica:

# Programa Resuelto (25 de enero, 2017), Escribir una figura con números dado un número ‘n’ (Ciclo For). https://www.youtube.com/watch?v=OjQFZwEBsBY

 # Franciscomelov (3 novimebre 2021) Funciones lambda en Python: Ejemplos de sintaxis. https://www.freecodecamp.org/espanol/news/funciones-lambda-en-python-ejemplos-de-sintaxis/