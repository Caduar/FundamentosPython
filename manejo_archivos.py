try:
    archivo = open("Hola.txt","w")
    archivo.write("Agregamos info al archivo \n")
    archivo.write("Agregamos info al archivo")
except Exception as e:
    print(e)
finally:
    archivo.close()