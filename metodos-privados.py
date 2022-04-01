class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre
        #Parcialmente privado sin necesidad de crear el metodo get o set para acceder o modificar el tributo
        self._apellido_paterno = ape_paterno
        self.__apellido_materno = ape_materno
    
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
    def metodo_publico(self):
        self.__metodo_privado()
    
    #Toca declarar el metodo get de los atributos extra
    def get_apellido_materno(self):
        return self.__apellido_materno
    def set_apellido_materno(self, apellidoMaterno):
            self.__apellido_materno = apellidoMaterno     
        
p1 = Persona("Camilo", "Duarte", "Rincon")

p1.metodo_publico()

print(p1.nombre)
#Deberiamos respetar el get o set para modificar
print(p1._apellido_paterno)
p1.set_apellido_materno("Lopez")
print(p1.get_apellido_materno())