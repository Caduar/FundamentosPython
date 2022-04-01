#Set es una coleccion sin orden y sin indices, no permite elementos repetidos
# Los elementos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
#Largo
print(len(planetas))
#revisar si un elemento esta en el set
print("Marte" in planetas)
#Agregar
planetas.add("Tierra")
print(planetas)
#remover, arroja excepcion si no aparece el elemento
planetas.remove("Tierra")
print(planetas)
#eliminar con discard no arroja excepcion
planetas.discard("Tierra")
print(planetas)
planetas.clear()
print(planetas)
#Eliminar el set
del planetas
