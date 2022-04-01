class Persona:
    def __init__(self, n):
        #Con el doble guion bajo se tiene un atributo privado
        #podemos crear variables asi no se declaren en el init
        self.__nombre = n
        self.__edad = 18
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    #Toca declarar el metodo get de los atributos extra
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
            self.__edad = edad    
p1 = Persona("Juan")
print(p1.get_nombre())

p1.set_nombre("Camilo")
p1.set_edad(25)
print(p1.get_nombre())
print(p1.get_edad())

