#2- Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def suma(num:int) -> int:
    """
    Suma todos los numeros enteros comprendidos entre el 0 y el numero dado
    """
    if num == 0:
        return 0
    else:
        return num + suma(num - 1)

#print(suma(5))

#3-Implementar una función para calcular el producto de dos números enteros dados.

def producto(num1:int, num2:int) -> int:
    if num2 == 0:
        return 0
    else:
        return num1 + producto(num1, (num2 - 1))   

#print(producto(5,4))

#4-Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.

def potencia(num1:int,num2:int) -> int:
    if num2 == 0:
        return 1
    else:
        return num1 * potencia(num1, (num2 - 1))
    
#print(potencia(5,3))

#6-Dada una secuencia de caracteres, obtener dicha secuencia invertida.
def invertir(palabra: str) -> str:
    if len(palabra) == 1:
        return palabra
    else:
        return palabra[-1:] + invertir(palabra[:-1])
    
print(invertir("UCAF"))
#10- Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def cantidad(num: int) -> int:
    if num < 10:
        return 1
    else:
        return 1 + cantidad(num//10)

print(cantidad(789456123))

#14- Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.

def digitos(num: int) -> int:
    if num < 10:
        return num 
    else:
        return num % 10 + digitos(num // 10)
    
print(digitos(123456))


#7- #Desarrollar un algoritmo que permita calcular la siguiente serie: h(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

def serie_h(num:int) -> float:
    if num == 1:
        return 1
    else:
        return 1/num + serie_h(num - 1)
    


