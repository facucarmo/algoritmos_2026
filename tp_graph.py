from graph import Graph

# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
# para resolver las tareas, listadas a continuación:

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router,
# switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat,
# Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

#h- grafo no dirigido
grafo = Graph(is_dir=False)

#a- cada equipo guarda su tipo en other_values
grafo.add_vertex("Manjaro", "pc")
grafo.add_vertex("Parrot", "pc")
grafo.add_vertex("Fedora", "pc")
grafo.add_vertex("Ubuntu", "pc")
grafo.add_vertex("Mint", "pc")
grafo.add_vertex("Red Hat", "notebook")
grafo.add_vertex("Debian", "notebook")
grafo.add_vertex("Arch", "notebook")
grafo.add_vertex("Guaraní", "servidor")
grafo.add_vertex("MongoDB", "servidor")
grafo.add_vertex("Router 1", "router")
grafo.add_vertex("Router 2", "router")
grafo.add_vertex("Router 3", "router")
grafo.add_vertex("Switch 1", "switch")
grafo.add_vertex("Switch 2", "switch")
grafo.add_vertex("Impresora", "impresora")

grafo.add_edge(25, "Red Hat", "Router 2")
grafo.add_edge(9, "Guaraní", "Router 2")
grafo.add_edge(50, "Router 2", "Router 3")
grafo.add_edge(37, "Router 2", "Router 1")
grafo.add_edge(43, "Router 3", "Router 1")
grafo.add_edge(61, "Router 3", "Switch 2")
grafo.add_edge(40, "Switch 2", "Manjaro")
grafo.add_edge(12, "Switch 2", "Parrot")
grafo.add_edge(5, "Switch 2", "MongoDB")
grafo.add_edge(56, "Switch 2", "Arch")
grafo.add_edge(3, "Switch 2", "Fedora")
grafo.add_edge(17, "Debian", "Switch 1")
grafo.add_edge(29, "Switch 1", "Router 1")
grafo.add_edge(18, "Switch 1", "Ubuntu")
grafo.add_edge(22, "Switch 1", "Impresora")
grafo.add_edge(80, "Switch 1", "Mint")

grafo.show()
print()

#b- barrido en profundidad y amplitud desde las tres notebooks

def barridos():
    notebooks = ["Red Hat", "Debian", "Arch"]
    for notebook in notebooks:
        print(f"Barrido en profundidad desde {notebook}: ")
        grafo.deep_show(notebook)
        print()
        print(f"Barrido en amplitud desde {notebook}: ")
        grafo.amplitude_show(notebook)
        print()

barridos()

#c- camino mas corto desde Manjaro, Red Hat y Fedora hasta la impresora
# dijkstra devuelve una pila con [equipo, costo, anterior], se va armando el camino
# desde el destino hacia atras siguiendo el anterior de cada equipo
def camino_mas_corto(origen, destino):
    pila_caminos = grafo.dijkstra(origen)
    costo = None
    camino = ""
    while pila_caminos.size() > 0:
        value = pila_caminos.pop()
        if value[0] == destino:
            if costo is None:
                costo = value[1]
                camino = value[0]
            else:
                camino = value[0] + " - " + camino
            destino = value[2]
    return camino, costo

def caminos_impresora():
    equipos = ["Manjaro", "Red Hat", "Fedora"]
    for equipo in equipos:
        camino, costo = camino_mas_corto(equipo, "Impresora")
        print(f"El camino mas corto desde {equipo} a la impresora es: {camino}, con un costo de {costo}")

caminos_impresora()
print()

#d- arbol de expansion minima

def arbol_minimo():
    arbol = grafo.kruskal("Manjaro")
    peso_total = 0
    print("El arbol de expansion minima es: ")
    for arista in arbol.split(";"):
        origen, destino, peso = arista.split("-")
        print(f"{origen} - {destino} con un peso de {peso}")
        peso_total += int(peso)
    print(f"El peso total del arbol es: {peso_total}")

arbol_minimo()
print()

#e- desde que pc (no notebook) es el camino mas corto hasta Guaraní

def pc_mas_cercana():
    pc_cercana = None
    menor_costo = None
    for equipo in grafo:
        if equipo.other_values == "pc":
            camino, costo = camino_mas_corto(equipo.value, "Guaraní")
            print(f"Desde {equipo.value} a Guaraní: {camino}, con un costo de {costo}")
            if menor_costo is None or costo < menor_costo:
                menor_costo = costo
                pc_cercana = equipo.value
    print(f"La pc con el camino mas corto a Guaraní es: {pc_cercana}, con un costo de {menor_costo}")

pc_mas_cercana()
print()

#f- desde que computadora del Switch 1 es el camino mas corto a MongoDB

def computadora_switch1():
    pos_switch = grafo.search("Switch 1", "value")
    if pos_switch is not None:
        computadora_cercana = None
        menor_costo = None
        for arista in grafo[pos_switch].edges:
            pos_equipo = grafo.search(arista.destination, "value")
            tipo = grafo[pos_equipo].other_values
            if tipo == "pc" or tipo == "notebook":
                camino, costo = camino_mas_corto(arista.destination, "MongoDB")
                print(f"Desde {arista.destination} a MongoDB: {camino}, con un costo de {costo}")
                if menor_costo is None or costo < menor_costo:
                    menor_costo = costo
                    computadora_cercana = arista.destination
        print(f"La computadora del Switch 1 con el camino mas corto a MongoDB es: {computadora_cercana}, con un costo de {menor_costo}")
    else:
        print("El Switch 1 no se encuentra en el grafo")

computadora_switch1()
print()

#g- cambiar la conexion de la impresora al Router 2 y volver a resolver
# el enunciado no indica el peso de la nueva conexion, se mantiene el anterior (22)

eliminada = grafo.delete_edge("Switch 1", "Impresora")
if eliminada is not None:
    grafo.add_edge(22, "Router 2", "Impresora")
    print("La impresora ahora esta conectada al Router 2")
    print()
    barridos()
    caminos_impresora()
else:
    print("La impresora no estaba conectada al Switch 1")



# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las
# siguientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1,
# baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para
# conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

casa = Graph(is_dir=False)

#a- cada vertice es un ambiente de la casa
casa.add_vertex("Cocina")
casa.add_vertex("Comedor")
casa.add_vertex("Cochera")
casa.add_vertex("Quincho")
casa.add_vertex("Baño 1")
casa.add_vertex("Baño 2")
casa.add_vertex("Habitación 1")
casa.add_vertex("Habitación 2")
casa.add_vertex("Sala de estar")
casa.add_vertex("Terraza")
casa.add_vertex("Patio")

#b- distancias en metros, Cocina y Sala de estar tienen 5 aristas, el resto al menos 3
casa.add_edge(4, "Cocina", "Comedor")
casa.add_edge(8, "Cocina", "Cochera")
casa.add_edge(10, "Cocina", "Quincho")
casa.add_edge(7, "Cocina", "Patio")
casa.add_edge(6, "Cocina", "Sala de estar")
casa.add_edge(3, "Sala de estar", "Comedor")
casa.add_edge(9, "Sala de estar", "Habitación 1")
casa.add_edge(5, "Sala de estar", "Baño 1")
casa.add_edge(7, "Sala de estar", "Terraza")
casa.add_edge(6, "Comedor", "Terraza")
casa.add_edge(12, "Cochera", "Patio")
casa.add_edge(15, "Cochera", "Quincho")
casa.add_edge(11, "Cochera", "Baño 2")
casa.add_edge(5, "Quincho", "Patio")
casa.add_edge(9, "Patio", "Terraza")
casa.add_edge(10, "Terraza", "Habitación 2")
casa.add_edge(3, "Habitación 1", "Baño 1")
casa.add_edge(4, "Habitación 1", "Habitación 2")
casa.add_edge(3, "Habitación 2", "Baño 2")
casa.add_edge(2, "Baño 1", "Baño 2")

#c- arbol de expansion minima y metros de cable para conectar todos los ambientes

def cable_ambientes():
    arbol = casa.kruskal("Cocina")
    metros_totales = 0
    print("El arbol de expansion minima de la casa es: ")
    for arista in arbol.split(";"):
        origen, destino, metros = arista.split("-")
        print(f"{origen} - {destino}: {metros} metros")
        metros_totales += int(metros)
    print(f"Se necesitan {metros_totales} metros de cable para conectar todos los ambientes")

cable_ambientes()
print()

#d- camino mas corto desde la Habitación 1 hasta la Sala de estar (router -> Smart Tv)

def cable_router_tv():
    origen = "Habitación 1"
    destino = "Sala de estar"
    pila_caminos = casa.dijkstra(origen)
    metros = None
    camino = ""
    while pila_caminos.size() > 0:
        value = pila_caminos.pop()
        if value[0] == destino:
            if metros is None:
                metros = value[1]
                camino = value[0]
            else:
                camino = value[0] + " - " + camino
            destino = value[2]
    print(f"El camino mas corto desde la Habitación 1 hasta la Sala de estar es: {camino}")
    print(f"Se necesitan {metros} metros de cable de red para conectar el router con el Smart Tv")

cable_router_tv()