from list_ import List
from super_heroes_data import superheroes

#6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,casa de comic a la que pertenece 
#(Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de apariciónsea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

list_heros = List()
def by_name(item):
    return item.name

def by_year(item):
    return item.year

class Superhero():
    def __init__(self, nombre, anio, casa, biografia):
        self.name = nombre
        self.year = anio 
        self.house = casa
        self.bio = biografia

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house} - {self.bio}"

    list_heros.add_criterion('name', by_name)
    list_heros.add_criterion('year', by_year)

for hero in superheroes:
    list_heros.append(
        Superhero(hero['name'], hero['first_appearance'], hero['house'], hero['short_bio'])
    )

#a-
linterna_verde = list_heros.search("Green Lantern", 'name')
if linterna_verde is not None:
    eliminado = list_heros.delete_value("Green Lantern", 'name')
    print(f"Se eliminó: {eliminado}")
#b-
wolverine = list_heros.search("Wolverine", 'name')
if wolverine is not None:
    print(f"El año de aparicion de Wolverine es: {list_heros[wolverine].year}")

#c-
dr_strange = list_heros.search("Dr Strange", 'name')
if dr_strange is not None:
    list_heros[dr_strange].house = "Marvel"
    print(f"La nueva casa de Dr. Strange es: {list_heros[dr_strange].house}")


#d-
print("Los heroes que tienen la palabra 'traje' o 'armadura' en su biografia son: ")
list_heros.filter_contain_on_bio(['suit','traje'])

#e-
print("Los heroes que aparecieron antes de 1963 son: ")
for hero in list_heros:
    if hero.year < 1963:
        print(f"{hero.name} - {hero.house}")

#f-
capitana_marvel = list_heros.search("Captain Marvel", 'name')
mujer_maravilla = list_heros.search("Wonder Woman", 'name')

if capitana_marvel is not None:
    print(f"Capitana Marvel pertenece a : {list_heros[capitana_marvel].house}")
else:
    print("Capitana Marvel no se encuentra en la lista")

if mujer_maravilla is not None:
    print(f"Mujer Maravilla pertenece a: {list_heros[mujer_maravilla].house}")
else:
    print("Mujer Maravilla no se encuentra en la lista")

#g-
flash = list_heros.search("Flash", 'name')
star_lord = list_heros.search("Star-Lord", 'name')

if flash is not None:
    print(f"La informacion de flash es: {list_heros[flash]}")
else:
    print("Flash no se encuentra en la lista")

if star_lord is not None:
    print(f"La informacion de Star-Lord es: {list_heros[star_lord]}")
else:
    print("Star-Lord no se encuentra en la lista")

#h-
print("Los heroes que empiezan con las letras 'B', 'M', 'S' son: ")
list_heros.filter_start_with(("B","M","S"))

#i-
cont_marvel = 0
cont_dc = 0


for hero in list_heros:
    if hero.house == "Marvel":
        cont_marvel += 1
    else:
        cont_dc += 1

print(f"Los heroes de Marvel son: {cont_marvel} y los heroes de DC son: {cont_dc}")




# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de 
# torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus
# Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades
# utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon
# deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;


list_entrenadores = List()

class Entrenador():
    def __init__(self, nombre, torneo, ganadas, perdidas):
        self.name = nombre
        self.championships = torneo
        self.wins = ganadas
        self.lose = perdidas
        self.pokemons = List()

    def __str__(self):
        return f"{self.name} - Torneos: {self.championships} - Ganadas: {self.wins} - Perdidas: {self.lose}"

class Pokemon():
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.name = nombre
        self.level = nivel
        self.type = tipo
        self.subtype = subtipo

    def __str__(self):
        return f"{self.name} - Nivel: {self.level} - Tipo: {self.type} - Subtipo: {self.subtype}"

ash = Entrenador("Ash Ketchum", 3, 15, 2)
misty = Entrenador("Misty", 1, 5, 15)
brook = Entrenador("Brook", 2, 10, 10)
lionel = Entrenador("Lionel", 5, 25, 0)
james = Entrenador("James", 0, 5, 10)
jesse = Entrenador("Jesse", 0, 5, 15)

steelix = Pokemon("Steelix", 10, "Acero", None)
aggron = Pokemon("Aggron", 15, "Acero", None)
metagross = Pokemon("Metagross", 5, "Acero", None)
blastoise = Pokemon("Blastoise",11,"Agua",None)
psyduck = Pokemon("Psyduck", 5, "Agua", "Psiquico")
gyarados = Pokemon("Gyarados", 20, "Agua", "Volador")
vaporeon = Pokemon("Vaporeon", 30, "Agua", None)
dragonite = Pokemon("Dragonite", 14, "Dragon", None)
latias =  Pokemon("Latias", 150, "Dragon", "Legendario")
pikachu = Pokemon("Pikachu", 100, "Electrico", None)
gengar = Pokemon("Gengar", 58, "Fantasma", None)
charizard = Pokemon("Charizard", 66, "Fuego", "Dragon")
magmar = Pokemon("Magmar", 13, "Fuego", None)
flareon = Pokemon("Flareon", 50, "Fuego", "Planta")
blaziken = Pokemon("Blaziken", 40, "Fuego", None)
glalie = Pokemon("Glalie", 5, "Hielo", None)
machamp = Pokemon("Machamp", 17, "Luchador", None)
alakazam = Pokemon("Alakazam", 32, "Psiquico", None)



ash.pokemons.append(glalie)
ash.pokemons.append(magmar)
ash.pokemons.append(machamp)
ash.pokemons.append(pikachu)
ash.pokemons.append(pikachu)
misty.pokemons.append(aggron)
misty.pokemons.append(metagross)
misty.pokemons.append(psyduck)
misty.pokemons.append(magmar)
brook.pokemons.append(dragonite)
brook.pokemons.append(machamp)
brook.pokemons.append(aggron)
lionel.pokemons.append(latias)
lionel.pokemons.append(blaziken)
lionel.pokemons.append(flareon)
lionel.pokemons.append(gengar)
lionel.pokemons.append(charizard)
jesse.pokemons.append(psyduck)
jesse.pokemons.append(blastoise)
jesse.pokemons.append(metagross)
james.pokemons.append(gyarados)
james.pokemons.append(dragonite)
james.pokemons.append(vaporeon)


list_entrenadores.append(ash)
list_entrenadores.append(misty)
list_entrenadores.append(brook)
list_entrenadores.append(lionel)
list_entrenadores.append(james)
list_entrenadores.append(jesse)

list_entrenadores.add_criterion('name', by_name)

# a. obtener la cantidad de Pokémons de un determinado entrenador;
def contador_pokemon(nombre_entrenador):
    pos = list_entrenadores.search(nombre_entrenador, 'name')
    if pos is not None:
        print (f"La cantidad de pokemones de {nombre_entrenador} es: {list_entrenadores[pos].pokemons.size()}")
    else: 
        print(f"El entrenador '{nombre_entrenador}' no se encuentra en la lista")

contador_pokemon("Misty")

# b. listar los entrenadores que hayan ganado más de tres torneos;
def ganadores():
    for entrenador in list_entrenadores:
        if entrenador.championships > 3:
            print(f"Tiene mas de 3 torneos: {entrenador}")

ganadores()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
max_champ = list_entrenadores[0]
for entrenador in list_entrenadores:
    if max_champ.championships < entrenador.championships:
        max_champ = entrenador
print(max_champ)

max_level = max_champ.pokemons[0]
for pokemon in max_champ.pokemons:
    if max_level.level < pokemon.level:
        max_level = pokemon
print(max_level)

# d. mostrar todos los datos de un entrenador y sus Pokémos;
def mostrar_entrenador():
    entrenador = input("Ingrese el entrenador para mostrar: ")
    buscado = list_entrenadores.search(entrenador, 'name')
    if buscado is not None:
        print(list_entrenadores[buscado])
        list_entrenadores[buscado].pokemons.show()
    else:
        print(f"El entrenador {entrenador} no esta en la lista")


mostrar_entrenador()

#e-mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %

def porcentaje():
    for entrenador in list_entrenadores:
        total = entrenador.wins + entrenador.lose
        porc = (entrenador.wins * 100) / total
        if porc > 79:
            print(f"{entrenador}, tiene mas de 79% de victorias")

porcentaje()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo);

def tipos():
    for entrenador in list_entrenadores:
        for pokemon in entrenador.pokemons:
            if pokemon.type == "Agua" and pokemon.subtype == "Volador":
                print(f"El entrenador: {entrenador}, tiene los siguientes pokemones de tipo agua/volador: {pokemon}")

            if pokemon.type == "Fuego" and pokemon.subtype == "Planta":
                print(f"El entrenador {entrenador} tiene los siguientes pokemones de tipo fuego/planta: {pokemon}")

tipos()

# g. el promedio de nivel de los Pokémons de un determinado entrenador;

def prom_levels():
    nombre = input("Ingrese un entrenador: ")
    buscado = list_entrenadores.search(nombre, 'name')
    if buscado is not None:
        entrenador = list_entrenadores[buscado]
        cont_levels = 0
        cont_pokemons = 0
        for pokemon in entrenador.pokemons:
            cont_pokemons +=  1
            cont_levels += pokemon.level
        if cont_pokemons > 0:
            promedio = cont_levels / cont_pokemons
            print(f"El promedio de nivel de los pokemons de {entrenador.name} es: {promedio}")
        else:
            print(f"El entrenador {entrenador.name} no tiene pokemons")

prom_levels()        

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;

def pokemon_esp():
    pokemon_buscado = input("Ingrese el pokemon que quiere buscar: ")
    cont = 0
    for entrenador in list_entrenadores:
        for pokemon in entrenador.pokemons:
            if pokemon_buscado == pokemon.name:
                cont += 1
    print(f"La cantidad de entrenadores que tiene a {pokemon_buscado} son :", cont)


pokemon_esp()


# i. mostrar los entrenadores que tienen Pokémons repetidos;

def repetidos():
    for entrenador in list_entrenadores:
        vistos = []
        repetidos = False
        for pokemon in entrenador.pokemons:
            if pokemon.name in vistos:
                repetidos = True
            else: 
                vistos.append(pokemon.name)
        if repetidos:
            print(f"El entrenador {entrenador.name} tiene pokemons repetidos")


repetidos()


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;

def poke_ttw():
    pokemones_ttw = ["Tyrantrum", "Terrakion", "Wingull"]
    for entrenador in list_entrenadores:
        for pokemon in entrenador.pokemons:
            if pokemon.name in pokemones_ttw:
                print(f"El entrenador {entrenador} posee a {pokemon.name}")

poke_ttw()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon
# deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

def buscador_x_y():
    nombre_entrenador = input("Ingrese el entrenador: ")
    nombre_pokemon = input("Ingrese el pokemon: ")
    pos = list_entrenadores.search(nombre_entrenador, 'name')
    if pos is not None:
        entrenador = list_entrenadores[pos]
        encontrado = None
        for pokemon in entrenador.pokemons:
            if pokemon.name == nombre_pokemon:
                encontrado = pokemon
        if encontrado is not None:
            print(f"{entrenador.name} tiene a {nombre_pokemon}")
            print(entrenador)
            print(encontrado)
        else:
            print(f"{entrenador.name} no tiene a {nombre_pokemon}")
    else:
        print(f"El entrenador {nombre_entrenador} no se encuentra en la lista")

buscador_x_y()