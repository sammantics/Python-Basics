#Programa para encontrar el factorial de cualquier número.

def factorial(n): 
    
    factorial=1

    for i in range (n):
        factorial*=i+1

    return factorial

print(factorial(7))