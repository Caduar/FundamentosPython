try:
    archivo = open("C:\\CursoPython\\Fundamentos\\Hola.txt","r")
    #print(archivo.read())
    #print(archivo.read(5))
    #print(archivo.readline())
    #for linea in archivo:
    #    print(linea)
    #print(archivo.readlines())
    #print(archivo.readlines()[2])
    #Abrir nuevo archivo
    archivo2 = open("HolaCopia.txt","w+")
    archivo2.write(archivo.read())
    
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()