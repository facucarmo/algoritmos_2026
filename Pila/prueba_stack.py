from random import randint
from Pila.stack import Stack

pila = Stack()

#1. Determinar el número de ocurrencias de un determinado elemento en una pila.

# for i in range(10):
#     pila.push(randint(1,5))

# print()
# pila.show()
# print()

# search_value = int(input("Ingrese un numero"))
# acum = 0

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         acum += 1

# print(f"Cantidad de ocurrencias de {search_value} es {acum}")


#2. Eliminar de una pila todos los elementos impares
# , es decir que en la misma solo queden números pares.

# for i in range(10):
#     pila.push(randint(1, 5))

# print()
# pila.show()
# print()

# pila_aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     if value % 2 == 0:
#         pila_aux.push(value)
    
# while pila_aux.size() > 0:
#     value = pila_aux.pop()
#     pila.push(value)

# pila.show()

#3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

# for i in range(5):
#     pila.push(randint(1,10))

# print()
# pila.show()
# print()

# pila_aux = Stack()

# value_determ = int(input("Ingrese el numero a reemplazar: "))
# value_reemplaz = int(input("Ingrese el nuevo numero: "))

# while pila.size() > 0:
#     value = pila.pop()
#     if value == value_determ:
#         pila_aux.push(value_reemplaz)
#     else:
#         pila_aux.push(value)

# while pila_aux.size() > 0:
#     value = pila_aux.pop()
#     pila.push(value)

# pila.show()

#4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

# for i in range(5):
#     pila.push(randint(1,10))

# print()
# pila.show()
# print()

# pila_aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     pila_aux.push(value)

# pila_aux.show()

#6. Leer una palabra y visualizarla en forma inversa.

# pila.push("L")
# pila.push("O")
# pila.push("B")
# pila.push("R")
# pila.push("A")

# print()
# pila.show()
# print()

# pila_aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     pila_aux.push(value)

# print()
# pila_aux.show()
# print()

#7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

# pila.push("gato")
# pila.push("pato")
# pila.push("vaca")
# pila.push("oveja")
# pila.push("camello")
# pila.push("caballo")
# pila.push("raton")
# pila.push("ganso")
# pila.push("perro")

# pila_aux = Stack()

# while pila.size() > 1:
#     value = pila.pop()
#     pila_aux.push(value)
#     while pila.size() == 1:
#         pila.pop()

# pila_aux.show()
# pila.show()


#11. Dada una pila de letras determinar cuántas vocales contiene.

# pila_aux = Stack()

# pila.push("a")
# pila.push("o")
# pila.push("t")
# pila.push("e")
# pila.push("g")
# pila.push("s")
# pila.push("a")
# pila.push("b")

# cont_vocales = 0

# while pila.size() > 0:
#     if pila.pop() == "a" or "e" or "i" or "o" or "u":
#         value = pila.pop()
#         pila_aux.push(value)
#         cont_vocales = cont_vocales + 1
#     else:
#         value = pila.pop()
#         pila_aux.push(value)
    
# print(f"La pila tiene {cont_vocales} vocales")

#5. Determinar si una cadena de caracteres es un palíndromo.

pila_aux = Stack()

pila.push("O")
pila.push("S")
pila.push("O")

while pila.size() > 0:
    value = pila.pop()
    pila_aux.push(value)

