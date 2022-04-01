class Persona:
    #This es el apuntador del objeto
    #El asterisco es un parametro opcional
    
    def __init__(this, n,e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d
        
    def desplegar(this):
        print("Nombre:", this.nombre)
        print("Edad:", this.edad)
        print("valores (tupla):", this.valores)
        print("Diccionario:", this.diccionario)

p1 = Persona("Juan", 28)
print(p1.nombre)
print(p1.edad)   

p1.desplegar()

p2 = Persona("Caduar", 30, 2,4,5)
p2.desplegar()

p3 = Persona("Mar", 27, 2,4, m="manazana", p="Pera", j="jicama")
p3.desplegar()