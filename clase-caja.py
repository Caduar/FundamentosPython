class Caja:
    def __init__(self, alto, largo, ancho):
        self.alto = alto
        self.largo = largo
        self.ancho = ancho
    
    def volumen(self):
        return self.alto * self.ancho * self.largo

caja = Caja(3, 2, 2)
print(caja.volumen())