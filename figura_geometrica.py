#ABC = Abstract Base Class
#No es posible crear objetos de una clase abstracta
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    @abstractmethod
    def area(self):
        pass