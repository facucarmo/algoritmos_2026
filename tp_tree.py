from tree import BinaryTree
from super_heroes_data import superheroes

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe(MCU)
# desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica
# si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en
# el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos,
# luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.


heroes_tree = BinaryTree()
super_heroes_tree = BinaryTree()
villain_tree = BinaryTree()

for hero in superheroes:
    heroes_tree.insert_node(hero['name'], hero)

#B-

print("Villanos ordenados: ")
heroes_tree.inorden_villain()

#C-
print("Heroes que comienzan con la letra C ordenados: ")
heroes_tree.inorden_hero_starts_with("C")

#D-
print(f"La cantidad de heroes es: {heroes_tree.count_heroes()}")

#E- 

def new_dr_strange(tree):
    tree.proxy_search("dr")
    nombre, datos = tree.delete_node("Dr Strange")
    if datos is not None:
        datos['name'] = "Doctor Strange"
        tree.insert_node(datos['name'], datos)
    else:
        print("No se encontró a Dr Strange en el árbol")
    tree.proxy_search("strange")

new_dr_strange(heroes_tree)

#F

heroes_tree.postorden_hero()

#G

heroes_tree.bosque_hero_villano(villain_tree, super_heroes_tree)

#G-I
print(f"El arbol de superheroes tiene {super_heroes_tree.count_nodes()} nodos")
print(f"El arbol de villanos tiene {villain_tree.count_nodes()} nodos")
print()

#G-II
print("Barrido ordenado del arbol de superheroes: ")
super_heroes_tree.inorder()
print()
print("Barrido ordenado del arbol de villanos: ")
villain_tree.inorder()
print()



# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

criaturas_tree = BinaryTree()

#g- cada nodo tiene el campo "capturada", ademas de quien la derroto y su descripcion
def cargar_criatura(nombre, derrotado_por):
    criaturas_tree.insert_node(nombre, {"derrotado_por": derrotado_por, "descripcion": None, "capturada": None})

cargar_criatura("Ceto", None)
cargar_criatura("Tifón", "Zeus")
cargar_criatura("Equidna", "Argos Panoptes")
cargar_criatura("Dino", None)
cargar_criatura("Pefredo", None)
cargar_criatura("Enio", None)
cargar_criatura("Escila", None)
cargar_criatura("Caribdis", None)
cargar_criatura("Euríale", None)
cargar_criatura("Esteno", None)
cargar_criatura("Medusa", "Perseo")
cargar_criatura("Ladón", "Heracles")
cargar_criatura("Águila del Cáucaso", None)
cargar_criatura("Quimera", "Belerofonte")
cargar_criatura("Hidra de Lerna", "Heracles")
cargar_criatura("León de Nemea", "Heracles")
cargar_criatura("Esfinge", "Edipo")
cargar_criatura("Dragón de la Cólquida", None)
cargar_criatura("Cerbero", None)
cargar_criatura("Cerda de Cromión", "Teseo")
cargar_criatura("Ortro", "Heracles")
cargar_criatura("Toro de Creta", "Teseo")
cargar_criatura("Jabalí de Calidón", "Atalanta")
cargar_criatura("Carcinos", None)
cargar_criatura("Gerión", "Heracles")
cargar_criatura("Cloto", None)
cargar_criatura("Láquesis", None)
cargar_criatura("Átropos", None)
cargar_criatura("Minotauro de Creta", "Teseo")
cargar_criatura("Harpías", None)
cargar_criatura("Argos Panoptes", "Hermes")
cargar_criatura("Aves del Estínfalo", None)
cargar_criatura("Talos", "Medea")
cargar_criatura("Sirenas", None)
cargar_criatura("Pitón", "Apolo")
cargar_criatura("Cierva de Cerinea", None)
cargar_criatura("Basilisco", None)
cargar_criatura("Jabalí de Erimanto", None)

#a- listado inorden de las criaturas y quien las derroto
print("Listado de criaturas y quien las derroto: ")
criaturas_tree.inorden_defeated_by()
print()

#b- cargar una breve descripcion de una criatura

def cargar_descripcion():
    nombre = input("Ingrese la criatura a la que quiere cargarle una descripcion: ")
    criatura = criaturas_tree.search(nombre)
    if criatura is not None:
        descripcion = input(f"Ingrese la descripcion de {nombre}: ")
        criatura.other_values["descripcion"] = descripcion
        print(f"Se cargo la descripcion de {nombre}")
    else:
        print(f"La criatura {nombre} no se encuentra en el arbol")

cargar_descripcion()
print()

#c- mostrar toda la informacion de Talos

def mostrar_talos():
    talos = criaturas_tree.search("Talos")
    if talos is not None:
        print(f"Criatura: {talos.value}")
        print(f"Derrotado por: {talos.other_values['derrotado_por']}")
        print(f"Descripcion: {talos.other_values['descripcion']}")
        print(f"Capturada por: {talos.other_values['capturada']}")
    else:
        print("Talos no se encuentra en el arbol")

mostrar_talos()
print()

#d- los 3 heroes o dioses que derrotaron mayor cantidad de criaturas

def top_tres_heroes():
    heroes = criaturas_tree.count_defeated()
    print("Los 3 heroes o dioses que derrotaron mas criaturas son: ")
    for puesto in range(1, 4):
        mejor_heroe = None
        for heroe in heroes:
            if mejor_heroe is None or heroes[heroe] > heroes[mejor_heroe]:
                mejor_heroe = heroe
        if mejor_heroe is not None:
            print(f"{puesto}. {mejor_heroe} con {heroes[mejor_heroe]} criaturas")
            heroes.pop(mejor_heroe)

top_tres_heroes()
print()

#e- criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles: ")
criaturas_tree.inorden_by_hero("Heracles")
print()

#f- criaturas que no han sido derrotadas
print("Criaturas que no han sido derrotadas: ")
criaturas_tree.inorden_not_defeated()
print()

#h- Heracles atrapo a Cerbero, Toro de Creta, Cierva de Cerinea y Jabalí de Erimanto

def capturas_heracles():
    capturadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for nombre in capturadas:
        criatura = criaturas_tree.search(nombre)
        if criatura is not None:
            criatura.other_values["capturada"] = "Heracles"
            print(f"{nombre} fue capturada por Heracles")
        else:
            print(f"La criatura {nombre} no se encuentra en el arbol")

capturas_heracles()
print()

#i- busqueda por coincidencia

def buscar_criatura():
    texto = input("Ingrese el texto a buscar: ")
    print(f"Criaturas que coinciden con '{texto}': ")
    criaturas_tree.proxy_search(texto)

buscar_criatura()
print()

#j- eliminar al Basilisco y a las Sirenas

def eliminar_criaturas():
    eliminar = ["Basilisco", "Sirenas"]
    for nombre in eliminar:
        eliminado, datos = criaturas_tree.delete_node(nombre)
        if eliminado is not None:
            print(f"Se elimino a {eliminado}")
        else:
            print(f"La criatura {nombre} no se encuentra en el arbol")

eliminar_criaturas()
print()

#k- Heracles derroto a las Aves del Estínfalo

def modificar_aves():
    aves = criaturas_tree.search("Aves del Estínfalo")
    if aves is not None:
        aves.other_values["derrotado_por"] = "Heracles"
        aves.other_values["descripcion"] = "Heracles derroto a varias"
        print(f"Se modifico {aves.value}: derrotado por {aves.other_values['derrotado_por']}")
    else:
        print("Las Aves del Estínfalo no se encuentran en el arbol")

modificar_aves()
print()

#l- cambiar el nombre de Ladón por Dragón Ladón

def renombrar_ladon():
    nombre, datos = criaturas_tree.delete_node("Ladón")
    if nombre is not None:
        criaturas_tree.insert_node("Dragón Ladón", datos)
        print("Ladón ahora se llama Dragón Ladón")
    else:
        print("Ladón no se encuentra en el arbol")

renombrar_ladon()
print()

#m- listado por nivel del arbol
print("Listado por nivel del arbol: ")
criaturas_tree.by_level()
print()

#n- criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles: ")
criaturas_tree.inorden_captured_by("Heracles")

