#Tarea 3, Calculadora Python de terminal

#Este programa consta de una calculadora, la cúal se intreractúa por medio de la terminal.

# Se añade direcciones interactiva con terminal.

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

#Se añade interacción con usuario
operation=input()

#Se designa variable con dígitos a cada función usando del 1 al 6.
#Se selecciona la función deseada seleccionando valor del 1 al 6.

#Función de Suma, se designa con 1.
#Para funciones con n números, se designa la variable n como no igual a "" para delimitar el rtango según la cantidad de elementos deseada.
#Se aplica la fórmula de suma al establecer los elementos a sumar y la designación por medio de n.
#Luego se imprime el resultado y la cantidad de elementos introducida por el ususario.
if operation == "1":
   suma=0
   cantidad=0
   n=input("Ingrese el primer número que desee sumar: ")

   while(n!=""):
       suma=suma+int(n)
       cantidad=cantidad+1
       n=input("Ingrese el siguiente número: ")    
   print("El total de la suma es: ", suma)    
   print("cantidad de elementos: ",cantidad)

#Función de Resta, se designa con 2.
#Se establece la función de resta por medio de un string para incluir ambas variables dentro de una fórmula de resta con el uso de -.
#Luego se imprime el resultado y la cantidad de elementos introducida por el ususario.
elif operation == "2":
 num1 = input("inserte primer número: ")
 num2 = input("inserte segundo número: ")
 print("El resultado de la resta es: " + str(int(num1) - int(num2)))

#Función de Multiplicación, se designa con 3.
#Al igual que la suma, n se diferencia de "" para demilitar la cantidad de elementos dentro de una fórmula de multiplicación se´gun la cantidad de elementos necesaria de acuerdo con el ususario.
#Luego se imprime el resultado y la cantidad de elementos introducida por el ususario.
elif operation == "3":
 mult=1
 cantidad=0
 n=input("Ingrese el primer número que desee multiplicar: ")

 while(n!=""):
       mult=mult*int(n)
       cantidad=cantidad+1
       n=input("Ingrese el siguiente número: ")    
 print("El resultado de la multiplicacion: ", mult)    
 print("cantidad de elementos: ",cantidad)

##Función de División, se designa con 4.
#Se establece la función de división por medio de un string para incluir ambas variables dentro de una fórmula para dividir con el uso de /.
#Luego se imprime el resultado y la cantidad de elementos introducida por el usuario.
elif operation == "4":  
    num1 = input("inserte primer número: ")
    num2 = input("inserte segundo número: ")
    print("El resultado de la división es: " + str(int(num1) / int(num2)))

##Función de Factorial, se designa con 5.
#Se establece la delimitación de los elementos que pueden se introducidos al designar que los elementos deben ser mayor o igual a cero. 
#Si el elementos es menor o igual a cero, se solicita otro elemento aceptable.
#Se establece n como elementos a introducir y n+1 para la función de factorial hasta adquirir resultado deseado. 
elif operation == "5":
 num1 = int(input("Inserte el primer número: "))
 factorial=1
 if num1<=0:
        print("Error número negativo, por favor ingrese un número entero")
 if num1>=0:
        for i in range(1, num1+1):    
         factorial=factorial*i       
 print("El factorial es: ", factorial)

#Función de Potencial, se designa con 6.
# Se establecen el elemento que se desea elevar al introducir con num1. Se establece a cual potencia se quiere elevar el elemento num1 con num2.
#Función de pow() se impelementa para relaizar la fórmula de potencia.
#Luego se imprime el resultado y la cantidad de elementos introducida por el ususario.
elif operation == "6":
   num1 =int(input("Inserte primer número: "))
   num2 = int(input ("Ingrese la potencia: "))
   Potencia= pow(num1,num2)
   print("El resultado de la potencia es:", Potencia)

#Si no se introduce ninguno de los dígitos establecido, se imprime ERROR.
else:
    print ("Error de numero ingresado")  
    
#Programado por:

#-Andrés Fuentes Soto
#-Sebastián Margery Monge