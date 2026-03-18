#Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def suma(num:int) -> int:
    """
    Suma todos los numeros enteros comprendidos entre el 0 y el numero dado
    """
    if num == 0:
        return 0
    else:
        return num + suma(num - 1)

#print(suma(5))

#Implementar una función para calcular el producto de dos números enteros dados.

def producto(num1:int, num2:int) -> int:
    if num2 == 0:
        return 0
    else:
        return num1 + producto(num1, (num2 - 1))   

#print(producto(5,4))

#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.

def potencia(num1:int,num2:int) -> int:
    if num2 == 0:
        return 1
    else:
        return num1 * potencia(num1, (num2 - 1))
    
print(potencia(5,3))
