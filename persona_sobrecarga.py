class Persona():
    def __init__(self, nombre):
        self.__nombre = nombre
    #Metodo sobreescrito de la clase padre object
    def __add__(self, otro):
        return self.__nombre + " " +  otro.__nombre
    def __sub__(self, otro):
        return "Operacion no soportada"
p1 = Persona("Juan")
p2 = Persona("Camilo")
#Agregandole una nueva funcionalidad con la sobrecarga
print(p1 + p2)

#__add__ suma
#__sub__ restar
#__mul__ multiplicar
