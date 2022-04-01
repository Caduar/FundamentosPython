class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "Nombre: " + self.nombre + ", Edad: " + str(self.edad)

class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo):
        #Acceder a los metodos y atributos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def __str__(self):
        return super().__str__() + ", Sueldo: " + str(self.sueldo)

persona = Persona("Camilo", 25)
print(persona)

empleado = Empleado("Camilin", "24", 6.49)
print(empleado)