class MiClase:
    variable_clase = "Variable de clase"
    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
#Si no creamos un objeto de la clase no se puede acceder a la instancia
objeto1 = MiClase("Hello")
MiClase.variable_instancia = "variable modificada instancia"
print(MiClase.variable_instancia) # valores distintos
print(objeto1.variable_instancia)

#podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)
# podemos acceder a las variables con el nombre de la clase
print(MiClase.variable_clase)

objeto1.variable_clase = "Modificando desde el objeto la variable de clase"
print(objeto1.variable_clase)

objeto2 = MiClase("Nuevo valor de instancia")
print(objeto2.variable_clase)

objeto3 = MiClase("Tercer objeto")
MiClase.variable_clase = "Cambio de la clase"
print("--------")
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)