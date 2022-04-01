#En Py las clases deben iniciar en mayuscula y sitiene varias palabras todas inician con mayuscula
#La clase define unicamente la estructura de lo que se va a crear es una plantilla para la creacion de objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Modificar valores
Persona.nombre = "Juan"
Persona.edad = 28

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

#Creacion de un objeto
#Apartir de la clase Persona creamos una variable (objeto) que contiene esa informacion
persona = Persona("Camilo", 25)
#Luego mandamos a llamr la informacion en la variable persona (objeto) sus atributos !Esto nunca lo habia entendido bien, ahora si!
print(persona.nombre)
print(persona.edad)

#Creacion de un segundo objeto
persona2 = Persona("Ivan", 29)
print(persona2.nombre)
print(persona2.edad)