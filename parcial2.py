# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total)
# de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool)
# y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a
# los datos contemplando lo siguiente: Los índices de cada uno de los árboles deben ser nombre, número y tipo;
# a- mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por 
# proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# b- mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# c- realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# d- mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# e- mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# f- determinar cuantos Pokémons tienen megaevolucion.
# g- determinar cuantos Pokémons tiene forma gigamax.
# h- cargue al menos 100 Pokémons.



from tree import BinaryTree
from pokemons_data import pokemons

pokemon_name_tree = BinaryTree()
pokemon_number_tree = BinaryTree()
pokemon_types_tree = BinaryTree()

for pokemon in pokemons:
    pokemon_name_tree.insert_node(pokemon['name'], pokemon)
    pokemon_number_tree.insert_node(pokemon['number'], pokemon)
    for tipo in pokemon['types']:
        pokemon_types_tree.insert_node(tipo, pokemon)


# a-
def num_datos():
    num_buscado = int(input("Ingrese un numero de pokemon: "))
    pos = pokemon_number_tree.search(num_buscado)

    if pos is not None:
        print(f"Los datos del pokemon numero {num_buscado} son: {pos.other_values}")
    else:
        print("No existe ningun pokemon con ese numero")

num_datos()

def name_datos():
    name_buscado = input("Ingrese el nombre del pokemon a buscar: ")
    pokemon_name_tree.proxy_search(name_buscado)

name_datos()

# b-

def type_search():
    types_buscados = ["Fantasma", "Fuego", "Eléctrico", "Acero"]
    for types in types_buscados:
        print(f"Los pokemons de tipo {types} son: ")
        pokemon_types_tree.proxy_search(types)

type_search()

# c-

def pokemons_ordenados():
    print("Los pokemones ordenados por numero de manera ascendente son: ")
    pokemon_number_tree.inorder()
    print("Los pokemones ordenados por nombre de manera ascendente son: ")
    pokemon_name_tree.inorder()
    print("Los pokemones ordenados por nivel por nombre son: ")
    pokemon_name_tree.by_level()

pokemons_ordenados()

# e-
def cantidad_por_tipo():
    tipos = ['acero', 'agua', 'bicho', 'dragón', 'eléctrico', 'fantasma', 'fuego', 'hada', 'hielo',
             'lucha', 'normal', 'planta', 'psíquico', 'roca', 'siniestro', 'tierra', 'veneno', 'volador']
    for tipo in tipos:
        print(f"Tipo {tipo}: {pokemon_types_tree.count_type(tipo)} pokemons")

cantidad_por_tipo()


# f-
print(f"La cantidad de pokemones que tiene mega evolucion es: {pokemon_name_tree.count_mega()}")

# g-
print(f"La cantidad de pokemones que tiene forma gigamax es: {pokemon_name_tree.count_giga()}")





# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las 
# siguientes tareas:
# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron
# juntos ambos personajes que se relacionan;
# a- hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# b- determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden
# con dicho número;
# c- cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo,
# R2-D2, BB-8;
# d- calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# e- indicar qué personajes aparecieron en los nueve episodios de la saga.


from graph import Graph

star_wars_graph = Graph(is_dir=False)

# c-
personajes = ['Luke Skywalker', 'Darth Vader','Yoda','Boba Fett','C3PO','Leia','Rey','Kylo Ren','Chewbacca', 'Han Solo', 'R2D2', 'BB8']

for personaje in personajes:
    star_wars_graph.add_vertex(personaje)

star_wars_graph.add_edge(9, 'C3PO', 'R2D2')
star_wars_graph.add_edge(2, 'Kylo Ren', 'Rey')
star_wars_graph.add_edge(3, 'Kylo Ren', 'BB8')
star_wars_graph.add_edge(4, 'Luke Skywalker', 'Leia')
star_wars_graph.add_edge(5, 'Darth Vader', 'Yoda')
star_wars_graph.add_edge(4, 'Leia', 'Han Solo')
star_wars_graph.add_edge(2, 'Kylo Ren', 'Han Solo')
star_wars_graph.add_edge(6, 'C3PO', 'Luke Skywalker')
star_wars_graph.add_edge(6, 'R2D2', 'Luke Skywalker')
star_wars_graph.add_edge(6, 'C3PO', 'Leia')
star_wars_graph.add_edge(6, 'R2D2', 'Leia')
star_wars_graph.add_edge(6, 'C3PO', 'Darth Vader')
star_wars_graph.add_edge(6, 'R2D2', 'Darth Vader')
star_wars_graph.add_edge(7, 'R2D2', 'Yoda')
star_wars_graph.add_edge(7, 'C3PO', 'Chewbacca')
star_wars_graph.add_edge(6, 'Chewbacca', 'Leia')
star_wars_graph.add_edge(4, 'Chewbacca', 'Han Solo')
star_wars_graph.add_edge(3, 'Chewbacca', 'Rey')
star_wars_graph.add_edge(3, 'Luke Skywalker', 'Darth Vader')
star_wars_graph.add_edge(4, 'Luke Skywalker', 'Yoda')
star_wars_graph.add_edge(3, 'Luke Skywalker', 'Han Solo')
star_wars_graph.add_edge(2, 'Luke Skywalker', 'Rey')
star_wars_graph.add_edge(3, 'Boba Fett', 'Darth Vader')
star_wars_graph.add_edge(2, 'Boba Fett', 'Han Solo')
star_wars_graph.add_edge(3, 'Rey', 'BB8')
star_wars_graph.add_edge(3, 'Rey', 'Leia')
star_wars_graph.add_edge(3, 'BB8', 'C3PO')
star_wars_graph.add_edge(3, 'BB8', 'R2D2')


# a-
def arbol_expansion_minimo(personaje):
    min_tree = star_wars_graph.kruskal(personaje)
    peso_total = 0
    print(f"Árbol de expansión mínimo desde {personaje}:")
    for edge in min_tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f'origin {origin} destination {destination} episodios {weight}')
        peso_total += int(weight)
    print(f'peso total: {peso_total}')

arbol_expansion_minimo('C3PO')
arbol_expansion_minimo('Yoda')
arbol_expansion_minimo('Leia')


# b-
max_episodios = 0
for vertex in star_wars_graph:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight

print(f"El máximo de episodios compartidos es: {max_episodios}")
print("Los pares que comparten esa cantidad son:")
for vertex in star_wars_graph:
    vertex.visited = False

for vertex in star_wars_graph:
    vertex.visited = True
    for edge in vertex.edges:
        destination_pos = star_wars_graph.search(edge.destination, 'value')
        if edge.weight == max_episodios and not star_wars_graph[destination_pos].visited:
            print(f"{vertex.value} - {edge.destination}")

# d-
def camino_mas_corto(origen, destino):
    if star_wars_graph.exist_path(origen, destino):
        paths = star_wars_graph.dijkstra(origen)
        peso_total = None
        camino_completo = []

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == destino:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                destino = value[2]

        camino_completo.reverse()
        print(f"El camino mas corto es: {' -> '.join(camino_completo)} con un costo de {peso_total}")
    else:
        print(f"No existe un camino entre {origen} y {destino}")

camino_mas_corto('C3PO', 'R2D2')
camino_mas_corto('Yoda', 'Darth Vader')

# e-
print("Los personajes que aparecieron en los nueve episodios son:")
for vertex in star_wars_graph:
    aparecio_en_nueve = False
    for edge in vertex.edges:
        if edge.weight == 9:
            aparecio_en_nueve = True
    if aparecio_en_nueve:
        print(vertex.value)


