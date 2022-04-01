from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre)

empleado = Empleado("Camilo", 1000)
imprimir_detalles(empleado)
empleado = Gerente("Mar", 2000, "RRHH")
imprimir_detalles(empleado)