from list_ import List
from super_heroes_data import superheroes
from queue_ import Queue


# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

list_heroes15 = List()

class Superhero():

    def __init__(self, nombre, apodo, nombre_real, bio_corta, primer_aparicion, villano):
        self.name = nombre
        self.alias = apodo
        self.real_name = nombre_real
        self.bio = bio_corta
        self.first_app = primer_aparicion
        self.is_villain = villano

    def __str__(self):
        return f"{self.name} - {self.real_name} - {self.first_app} - {self.bio}"

for hero in superheroes[:15]:
    list_heroes15.append(
        Superhero(hero['name'], hero['alias'],hero['real_name'], hero ['short_bio'], hero['first_appearance'], hero['is_villain'] )
    )

def buscar_capitan_america(lista, i):
    if i == lista.size():
        return "El capitan America no se encuentra en la lista"
    elif lista[i].name == "Captain America":
        return "El capitan america esta en la lista"
    else: 
        return buscar_capitan_america(lista, i + 1)

def listar_heroes(lista, i):
    if i == lista.size():
        return 
    print(lista[i])
    listar_heroes(lista, i + 1)

print(buscar_capitan_america(list_heroes15, 0))
listar_heroes(list_heroes15, 0)


# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes.  X
# Determinar en que posicion esta The Thing y Rocket Raccoon.
# Listar todos los villanos de la lista.  X
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980. X
# Listar los superheores que comienzan con  Bl, G, My, y W. X
# Listado de personajes ordenado por nombre real de manera ascendente de los personajes. X
# Listado de superheroes ordenados por fecha de aparación. X
# Modificar el nombre real de Ant Man a Scott Lang. X
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit. X
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista. X

list_heroes = List()
queue_heroes = Queue()
queue_aux = Queue()


def by_name(item):
    return item.name

def by_real_name(item):
    return item.real_name

def by_first_app(item):
    return item.first_app

list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('real_name', by_real_name)
list_heroes.add_criterion('first_app', by_first_app)

for hero in superheroes:
    list_heroes.append(
        Superhero(hero['name'], hero['alias'],hero['real_name'], hero ['short_bio'], hero['first_appearance'], hero['is_villain'] )
    )


#Ordenar por nombre
print("La lista ordenada por nombre del heroe es: ")
list_heroes.sort_by_criterion('name')
list_heroes.show()

#Posiciones de The Thing y Rocket Raccoon
posicion_the_thing = list_heroes.search("The Thing", 'name')
posicion_rocket_raccoon = list_heroes.search("Rocket Raccoon", 'name')

print()
print(f'The Thing esta en la posicion: {posicion_the_thing}')
print(f'Rocket Raccoon esta en la posicion: {posicion_rocket_raccoon}')
print()

#Listar los villanos
print("Los villanos de la lista son: ")
print()
for hero in list_heroes:
    if hero.is_villain:
        print(hero)

print()
#Pasar los villanos a una queue
for hero in list_heroes:
    if hero.is_villain:
        value = hero
        queue_heroes.arrive(value)
#Mostrar los villanos que aparecieron antes de 1980
while queue_heroes.size() > 0:
    value = queue_heroes.attention()
    if value.first_app < 1980:
        queue_aux.arrive(value)

print("Villanos que aparecieron antes de 1980: ")
print()
queue_aux.show()

#Heroes que empiecen con Bl, G, My, W
print()
print("Los heroes que comienzan con Bl, G, My o W son: ")
print()
list_heroes.filter_start_with(("Bl", "G", "My", "W"))

print()
#Ordenados por nombre real:
print("La lista ordenada por año de aparicion es: ")
print()
list_heroes.sort_by_criterion('real_name')
list_heroes.show()

print()

#Ordenados por primer aparicion:
print("La lista ordenada por año de aparicion es: ")
print()
list_heroes.sort_by_criterion('first_app')
list_heroes.show()

print()

#Modificar el nombre de Ant-Man a Scott Lang
print("El nombre correcto de Ant Man es: ")
ant_man = list_heroes.search("Ant Man", 'name')
if ant_man is not None:
    list_heroes[ant_man].real_name = 'Scott Lang'
    print(list_heroes[ant_man])

print()

print("Los heroes que tienen Time traveling o Suit en su bio son: ")
list_heroes.filter_contain_on_bio(['time-traveling','suit'])
print()

print("Eliminar a Electro y Baron Zemo")
delete_electro = list_heroes.delete_value("Electro", 'name')
print(f'Valor eliminado {delete_electro}')

delete_electro = list_heroes.delete_value("Baron Zemo", 'name')
print(f'Valor eliminado {delete_electro}')