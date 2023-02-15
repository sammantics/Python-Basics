#Ejercicio 1: Cree una función que cuente e imprima en pantalla todos los números,
#letras y caracteres especiales presentes en una string.


def contar_digitos_letras_caracteres(cadena):
    digit = 0
    letr = 0
    caract = 0

    for c in cadena:
        if c.isdigit():
            digit += 1
        elif c.isalpha():
            letr += 1
        else:
            caract += 1 

    return digit,letr,caract

texto = input('Digite texto: ')
resultado = contar_digitos_letras_caracteres (texto)

print('Cantidad de dígitos: %i' % resultado[0])
print('Cantidad de letras: %i' % resultado[1])
print('Cantidad de caractéres:%i' % resultado[2])
