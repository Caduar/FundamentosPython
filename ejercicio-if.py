mes = int(input("diligencie el mes del año del 1 al 12: "))
estacion = None
if (mes == 1 or mes ==2 or mes == 12):
    estacion = "invierno"
elif(mes == 3 or mes == 4 or mes == 5):
    estacion = "Primavera"
elif(mes == 6 or mes == 7 or mes == 8):
    estacion = "Verano"
elif(mes == 9 or mes == 10 or mes == 11):
    estacion = "Verano"
else:
    estacion = "Mes incorrecto"
    
print("Estacion:", estacion, "para el mes", mes)