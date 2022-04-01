class Arimetica:
    """Clase aritmetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operando1, operando2):
    #Atributos de la clase
        self.operando1 = operando1
        self.operando2 = operando2
    #Esto es un metodo 
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2

#Creamos un nuevo objeto
aritmetica = Arimetica(2, 4)
print(aritmetica.sumar())