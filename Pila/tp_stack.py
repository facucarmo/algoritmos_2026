from stack import Stack

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila = Stack()

pila.push({"Nombre": "Black Widow","Pelis": 5})
pila.push({"Nombre": "Black Panther","Pelis": 3})
pila.push({"Nombre": "Diego","Pelis": 4})
pila.push({"Nombre": "Groot","Pelis": 1})
pila.push({"Nombre": "Rocket Raccoon","Pelis": 5})
pila.push({"Nombre": "Gaia","Pelis": 2})
pila.push({"Nombre": "Iron Man","Pelis": 4})
pila.push({"Nombre": "Thanos","Pelis": 3})

pila_aux = Stack()

while pila.size() > 0:
    value = pila.pop()
    if value["Pelis"] > 3:
        pila_aux.push(value)
pila_aux.show()

while pila_aux.size() > 0:
    value = pila_aux.pop()

