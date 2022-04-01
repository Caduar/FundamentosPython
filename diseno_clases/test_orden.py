from producto import Producto
from orden import Orden

#Creas los productos
producto1 = Producto("Camiseta", 1250)
producto2 = Producto("Pantalon", 111.15)
producto3 = Producto("zapatos", 250.25)
producto4 = Producto("anillo", 12)

productos = [producto1, producto2]

orden1 = Orden(productos)
print(orden1)

productos.append(producto3)
orden2 = Orden(productos)
orden2.agregar_producto(producto4)
print(orden2)
print(orden2.calcular_total())