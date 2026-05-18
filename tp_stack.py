from stack import Stack

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas 
#en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila = Stack()

pila.push({"Nombre": "Black Widow","Pelis": 5})
pila.push({"Nombre": "Black Panther","Pelis": 3})
pila.push({"Nombre": "Diego","Pelis": 4})
pila.push({"Nombre": "Groot","Pelis": 1})
pila.push({"Nombre": "Gaia","Pelis": 2})
pila.push({"Nombre": "Iron Man","Pelis": 4})
pila.push({"Nombre": "Thanos","Pelis": 3})
pila.push({"Nombre": "Rocket Raccoon","Pelis": 5})

pila.show()

pila_aux = Stack()

posicion = 1

#Posicion donde se encuentra Rocket Raccoon y Groot
while pila.size() > 0:
     value = pila.pop()
     pila_aux.push(value)
     if value["Nombre"] == "Rocket Raccoon":
         print(f"Rocket Raccoon esta en la posicion: {posicion}")
    
     if value["Nombre"] == "Groot":
         print(f"Groot esta en la posicion: {posicion}")

     posicion = posicion + 1

#Vuelven todos los elementos a su orden original
while pila_aux.size() > 0:
     value = pila_aux.pop()
     pila.push(value)

#Mostrar los que estan en 5 o mas pelis
while pila.size() > 0:
      value = pila.pop()
      pila_aux.push(value)
      if value["Pelis"] >= 5:
         print(f"El personaje {value["Nombre"]} tiene {value["Pelis"]} peliculas")

#Vuelven todos los elementos a su orden original
while pila_aux.size() > 0:
     value = pila_aux.pop()
     pila.push(value)

#Determinar en cuantas peliculas aparecio Black Widow
while pila.size() > 0:
      value = pila.pop()
      pila_aux.push(value)
      if value["Nombre"] == "Black Widow":
          print(f"Black Widow aparece en {value["Pelis"]} peliculas")


#Vuelven todos los elementos a su orden original
while pila_aux.size() > 0:
     value = pila_aux.pop()
     pila.push(value)


#Mostrar todos los personajes cuyos nombre empiezan con C, D y G.

iniciales = ["C", "D", "G"]

while pila.size() > 0:
     value = pila.pop()
     pila_aux.push(value)
     if value["Nombre"][0] in iniciales:
         print (f"Los personajes que su nombre empieza con C, D o G son: {value["Nombre"]}")

# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

pila_robot = Stack()
pila_robot_aux = Stack()

for i in range(3):
    pasos = int(input("Ingrese sus pasos: "))
    direccion = input("Ingrese su direccion: ")
    pila_robot.push({"pasos": pasos, "direccion": direccion})

print("El camino del robot es: ")
pila_robot.show()
print()

while pila_robot.size() > 0:
    value = pila_robot.pop()
    direc = value["direccion"]
    vuelta = None

    if direc == "N":
        vuelta = "S"
    elif direc == "S":
         vuelta = "N"
    elif direc == "E":
         vuelta = "O"
    elif direc == "O":
         vuelta = "E"
    elif direc == "SE":
         vuelta = "NO"
    elif direc == "NO":
         vuelta = "SE"
    elif direc == "SO":
         vuelta = "NE"
    elif direc == "NE":
         vuelta = "SO"

    pila_robot_aux.push({"pasos": value["pasos"],"direccion": vuelta})

print("El camino de vuelta del robot es: ")
pila_robot_aux.show()
print()