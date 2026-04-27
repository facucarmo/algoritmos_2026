#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#c. Utilizar un vector para representar la mochila.


mochila = ["droga","coca","sable de luz","perro","bata","pan"]

def usar_la_fuerza(mochila, acum_obj=0):
    if not mochila:
        return "La mochila esta vacia"
    elif mochila[0] == "sable de luz":
        return f"Se encontro el sable de luz, y estaba en la posicion {acum_obj}"
    else:
        return usar_la_fuerza(mochila[1:], acum_obj + 1)
    
print(usar_la_fuerza(mochila))