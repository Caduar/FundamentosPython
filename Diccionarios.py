#Un diccionario esta compuesto por una llave y un valor (Key, value)
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Managment System"
}
print(diccionario)
#Largo
print(len(diccionario))
#Accediendo a un elemento
print(diccionario["IDE"])
#Otra forma mismo resxultado
print(diccionario.get("IDE"))
#Modificando valores
diccionario["IDE"] = "integrated development environment"
print(diccionario)

for termino in diccionario:
    print(termino)
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)

#COmprobar existencia en el diccionario
print("IDE" in diccionario)

#Agregar nuevo elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#Remover elementos
diccionario.pop("DBMS")
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#eliminar por completo
del diccionario