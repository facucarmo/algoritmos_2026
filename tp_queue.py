from queue_ import Queue
from stack import Stack

# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,de las cual se cuenta
# con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’,
# si perder datos en la cola;

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57,
# y determinar cuántas son.

queue_notif = Queue()
queue_aux = Queue()
stack = Stack()

#Se crea la queue de notif
queue_notif.arrive({"Hora": "00:36", "Mensaje": "Revisa el post de Queue.01", "App": "Twitter"})
queue_notif.arrive({"Hora": "07:04", "Mensaje": "Tienes una nueva solicitud de amistad", "App": "Facebook"})
queue_notif.arrive({"Hora": "10:54", "Mensaje": "Nueva publicacion que podria interesarte", "App": "Facebook"})
queue_notif.arrive({"Hora": "12:53", "Mensaje": "Hola Pedro", "App": "Instagram"})
queue_notif.arrive({"Hora": "14:52", "Mensaje": "Algoritmos ha subido un nuevo video!", "App": "Youtube"})
queue_notif.arrive({"Hora": "17:14", "Mensaje": "Python tiene una nueva version!", "App": "Twitter"})
queue_notif.arrive({"Hora": "23:07", "Mensaje": "¿Has iniciado sesión en un nuevo dispositivo?", "App": "Facebook"})

#Se muestra la queue
print("Notificaciones: ")
queue_notif.show()
print()

cont = 0
while queue_notif.size() > 0:
    value = queue_notif.attention()
    if value["Hora"] < "15:57" and value["Hora"] > "11:43":
        cont += 1
        stack.push(value)
    else:
        queue_aux.arrive(value)

print(f"Las notificaciones entre las 11:43 y las 15:57 son {cont}: ")
stack.show()
print()

print()
queue_aux.show()
print()

while stack.size() > 0:
    value = stack.pop()
    queue_aux.arrive(value)

while queue_aux.size() > 0:
    value = queue_aux.attention()
    queue_notif.arrive(value)

#Eliminar notificacion de facebook

while queue_notif.size() > 0:
    value = queue_notif.attention()
    if value["App"] == "Facebook":
        print()
        print(f"Se ha eliminado la notificacion {value} por ser de facebook")
        print()
    else: 
        queue_aux.arrive(value)

#Mostrar la queue sin la notif de facebook
print("Notificaciones sin facebook: ")
queue_aux.show()
print()

#Vuelven los elementos a la queue
while queue_aux.size() > 0:
    value = queue_aux.attention()
    queue_notif.arrive(value)

while queue_notif.size() > 0:
    value = queue_notif.attention()
    if  value["App"] == "Twitter" and "Python" in value["Mensaje"]:
        queue_aux.arrive(value)
 
print("Estas notificaciones son de Twitter e incluyen 'Python': ")
queue_aux.show()
print()


# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc.,
#  desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

queue_marvel = Queue()
queue_marvel_aux = Queue()

queue_marvel.arrive({"Nombre": "Tony Stark", "Heroe": "Iron Man", "Genero": "M"})
queue_marvel.arrive({"Nombre": "Steve Rogers", "Heroe": "Capitan America", "Genero": "M"})
queue_marvel.arrive({"Nombre": "Scott Lang", "Heroe": "Ant Man", "Genero": "M"})
queue_marvel.arrive({"Nombre": "Stephen Strange", "Heroe": "Doctor Strange", "Genero": "M"})
queue_marvel.arrive({"Nombre": "Natasha Romanoff", "Heroe": "Black Widow", "Genero": "F"})
queue_marvel.arrive({"Nombre": "Francis Castle", "Heroe": "Punisher", "Genero": "M"})
queue_marvel.arrive({"Nombre": "Carol Danvers", "Heroe": "Capitana Marvel", "Genero": "F"})
queue_marvel.arrive({"Nombre": "Wanda Maximoff", "Heroe": "Scarlet Witch", "Genero": "F"})
queue_marvel.arrive({"Nombre": "Bruce Banner", "Heroe": "Hulk", "Genero": "M"})
queue_marvel.arrive({"Nombre": "Gamora", "Heroe": "Gamora", "Genero": "F"})

#Mostramos la queue
print()
queue_marvel.show()
print()

#Mostramos el nombre de Capitana Marvel
while queue_marvel.size() > 0:
    value = queue_marvel.attention()
    if value["Heroe"] == "Capitana Marvel":
        print(f"El nombre de la Capitana Marvel es: {value["Nombre"]}")
    queue_marvel_aux.arrive(value)

print()

#Vuelven los elementos a la queue original
while queue_marvel_aux.size() > 0:
    value = queue_marvel_aux.attention()
    queue_marvel.arrive(value)

#Mostramos los superheroes femeninos
while queue_marvel.size() > 0:
    value = queue_marvel.attention()
    if value["Genero"] == "F":
        print(f"Superheroes femeninos en la queue: {value["Heroe"]}")
    queue_marvel_aux.arrive(value)

print()

#Vuelven los elementos a la queue original
while queue_marvel_aux.size() > 0:
    value = queue_marvel_aux.attention()
    queue_marvel.arrive(value)

#Mostramos los nombres de los personajes masculinos
while queue_marvel.size() > 0:
    value = queue_marvel.attention()
    if value["Genero"] == "M":
        print(f"Personajes masculinos en la queue: {value["Nombre"]}")
    queue_marvel_aux.arrive(value)

print()

#Vuelven los elementos a la queue original
while queue_marvel_aux.size() > 0:
    value = queue_marvel_aux.attention()
    queue_marvel.arrive(value)

#Mostramos el nombre del superheroe de Scott Lang
while queue_marvel.size() > 0:
    value = queue_marvel.attention()
    if value["Nombre"] == "Scott Lang":
        print(f"El nombre del superheroe de Scott Lang es: {value["Heroe"]}")
    queue_marvel_aux.arrive(value)

print()

#Vuelven los elementos a la queue original
while queue_marvel_aux.size() > 0:
    value = queue_marvel_aux.attention()
    queue_marvel.arrive(value)

#Mostramos todos los datos de lo superheroes que comienza su nombre con S
while queue_marvel.size() > 0:
    value = queue_marvel.attention()
    if value["Nombre"][0] == "S" or value["Heroe"][0] == "S":
        print(f"Heroe/personaje que comienza con S: {value}")
    queue_marvel_aux.arrive(value)

print()

#Vuelven los elementos a la queue original
while queue_marvel_aux.size() > 0:
    value = queue_marvel_aux.attention()
    queue_marvel.arrive(value)

#Buscamos si se encuentra Carol Danvers, y mostramos su nombre de heroe
while queue_marvel.size() > 0:
    value = queue_marvel.attention()
    if value["Nombre"] == "Carol Danvers":
        print(f"Carol Danvers se encuentra en la queue, y su nombre de superheroe es: {value["Heroe"]}")
    
print()

#Vuelven los elementos a la queue original por ultima vez
while queue_marvel_aux.size() > 0:
    value = queue_marvel_aux.attention()
    queue_marvel.arrive(value)