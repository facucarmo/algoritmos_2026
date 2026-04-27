#5. Desarrollar una función que permita convertir un número romano en un número decimal.

valores = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romanos(numero):
    if len(numero) == 0:
        return 0
    elif len(numero) == 1:
        return valores[numero]
    elif valores[numero[0]] >= valores[numero[1]]:
        return valores[numero[0]] + romanos(numero[1:])
    else:
        return valores[numero[1]] - valores[numero[0]] + romanos(numero[2:])
    
print(romanos('MCMICIX'))