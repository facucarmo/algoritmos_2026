#CLASES
#Se define con la palabra class, el nombre y :
#Las clases tienen jerarquia
class MiClase:
    #Atributos
    #name, size = None, None

    #Constructor de una clase(metodo para crear objetos que son instancias de una clase)
    #Es un metodo opcional. Puedo definirlo o no
    #No se define el metodo constructor porque se hereda de la clase padre, Clase Object
    #En python el metodo constructor se llama asi:
    def __init__(self, name : str, size : int = None):
        self.__name = name
        self.size = size

    #Funciones
    def saludar(self):
        print(f"Hola, mi nombre es {self.__name}")


    #Esto es un getter:
    def get_name(self):
        return self.__name

    #Esto es un setter:
    def set_name(self, new_name:str):
        self.__name = new_name

    #Privacidad: Ocultamiento de la informacion. El objeto es el unico que puede modificar la informacion
    #Hay que agregarle __ antes de mi atributo para ponerlo privado por ejemplo __name

f = MiClase("Pepito")

#print(f.name)
f.saludar()
f.set_name("Falopin")
print(f.get_name)