class MiClase:
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "variable instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
       #Desde un metodo estatico/class method no podemos acceder a las vartiables de instancia
       # print(MiClase.variable_instancia)
    @classmethod
    def metodo_clase(cls):
            print("Metodo de clase:" + str(cls))
            print(cls.variable_clase)
    def metodo_intancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        

MiClase.metodo_estatico()
MiClase.metodo_clase()
print()
objeto1 = MiClase()
objeto1.metodo_intancia()