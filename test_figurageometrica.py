from cuadrado import Cuadrado
from figura_geometrica import FiguraGeometrica
#No se pueden crear objetos de una clase abstracta
#figuraGeometrica = FiguraGeometrica(ancho, alto)
cuadrado = Cuadrado(5, "rojo")
print(cuadrado.area())
print(cuadrado.color)

# Metodo para saber en que orden se ejeuctan las clases
print(Cuadrado.mro())