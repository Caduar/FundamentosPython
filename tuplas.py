#Tupla mantiene el roden, pero ya no se puede modificar y s eusa parentesis
frutas = ("Naranja", "platano","Guayaba")
print(frutas)
# largo de la tupla
print(len(frutas))
#Accediendo a un elemneto
print(frutas[2])
#Navegacion inversa
print(frutas[-1])
#Rangos
print(frutas[0:2])
# Cambiar tupla
frutasLista = list(frutas)
frutasLista[0] = "Naranjita"
frutas = tuple(frutasLista)
print(frutas)
for fruta in frutas:
    print(fruta, end = ", ")
#No podemos agregar ni eliminar elementos
#podemos eliminar completamente la tupla
del frutas