#las variables se declaran antes del bloque try
from numeros_identicos import NumerosIdenticos
resultado = None
a = 10
b = 10
try:
    if a == b:
        raise NumerosIdenticos("Ocurrio alguito por numeros identicos")
#Se pueden poner varias exception y toca poner la demenor jerarqui primero
except ZeroDivisionError as ex:
    print("Ocurrió un error de division", ex)
    print(type(ex))
except Exception as ex:
    print("Ocurrió un error", ex)
    print(type(ex))
else:
    print("No hubo ninguna excepcion")
finally:
    print("Todo pasa por aca")
print("Resultado:", resultado)