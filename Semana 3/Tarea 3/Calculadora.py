#Tarea 3, Calculadora Python de terminal

# Se añade interacción con terminal
operation=input()
print("")
print("Seleccionar opercación a realizar:")
print("")
print("1.Sumar")
print("2.Resta")
print("3.Multiplicación")
print("4.Dividir")
print("5.Factorial")
print("6.Potencia")
print("")

operation=input()


if operation == 1:
    num1 = input("inserte primer número: ")
    num2 = input("inserte segundo número: ")
    print("La suma es: ")
    
elif operation == 2:
    num1 = input("inserte primer número: ")
    num2 = input("inserte segundo número: ")
    print("La resta es: " + num1 - num2)
    
elif operation == 3:
    num1 = input("inserte primer número: ")
    num2 = input("inserte segundo número: ")
    print("La multiplicación es: ")
    
elif operation == 4:
    num1 = input("inserte primer número: ")
    num2 = input("inserte segundo número: ")
    print("La división es: " + num1 / num2)
    
elif operation == 5:
    num1 = input("inserte primer número: ")
    factorial=1
    if num1<=0:
        print("Error número negativo, por favor ingrese un número entero")
    if num1>=0:
        for i in range(1, num1+1):    
            factorial=factorial*i       
            
    print("La factorial es: "+ factorial)
elif operation == 6:
    num1 = input("inserte primer número: ")
    potencial=1
    if num1<=0
        print("Error número negativo, por favor ingrese un número entero")
    if num1>=0
        for i in 
        
    print("La potencia es: ")


#ADD

#SUBTRACT

#MULTIPLY

#DIVIDE

