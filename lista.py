nombres = ['holiwi', "Juan", "Carla", "Ricardo", "maria"]
print (nombres)
#Recorrer lista
#for nombre in nombres:
#    print(nombre)
    
#conocer largo de la lista
print(len(nombres))
#elemento cero
print(nombres[0])
#Naveghacion inversa
print(nombres[-1])
#imprimir rango
print(nombres[0:2]) #sin incluir el indice 2
#imprimir rango desde el inciio
print(nombres[:3]) #sin incluir el indice 2
#imprimir rango hasta el final desde el indcie proporcionado
print(nombres[1:]) #sin incluir el indice 2
#Cambiar elementos de una ista
nombres[3] = "Ivone"
print(nombres)
#revisar si un eemento existe en una ista
if "Ivone" in nombres:
    print("Ivone existe en la lista")
else:
    print("Ivone no existe en la lista")

#Agregar un nuevo elemento a la lista
nombres.append("Lorenzo")
print(nombres)
nombres.insert(1, "camilin")
print(nombres)
nombres.remove("holiwi")
print(nombres)
#Remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)
#remover el indice indicado de la lista
del nombres[0]
print(nombres)
#Limpiar elementos de nuestra lista
nombres.clear()
print(nombres)
#Eliminar lista
del nombres
