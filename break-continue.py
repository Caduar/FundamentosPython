#imprimir unicamente las letras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin ciclo for")
    
print("Continua el programa.....")

#Imprimir solo numero pares
for i in range(6):
    if i%2 ==0:
        print(i)
    
for i in range(6):
    if i%2 !=0:
        continue
    print(i)