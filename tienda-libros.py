print("Proporcione los siguientes datos: ")
nombre = input("proporcione el nombre: ")
id = int(input("Proporciona el ID: "))
precio = float(input("precio del libro: "))
envioGratuito = input("Indica si el envio es gratuito True/False: ")

if (envioGratuito == "True"):
    envioGratuito = True
elif envioGratuito =="False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto"

print("Nombre:",nombre)
print("Id:",id)
print("Precio:",precio)
print("Emvio gratuito:",envioGratuito)

print(type(envioGratuito))