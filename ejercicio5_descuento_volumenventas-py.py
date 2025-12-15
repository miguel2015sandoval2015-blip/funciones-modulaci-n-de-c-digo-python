#**** zona de funciones ******
def ingresar_productos():
    subtotal = 0
    
    while True :
        precio = float(input("digite el precio del producto ( 0 para terminar): "))
        if precio == 0:
            break
        
        cantidad = int(input("ingrese la cantidad: "))
        subtotal += precio * cantidad
        
    return subtotal

def calcular_descuento(subtotal):
    if subtotal > 1000:
        descuento = subtotal * 0.10 
        mensaje = "se aplico un descuento del 10%"
    elif subtotal > 500:
        descuento = subtotal * 0.05
        mensaje = "se aplico un descuento del 5%"
    else:
        descuento = 0
        mensaje = "no se aplico descuento"
        
            
    total = subtotal - descuento
    return total, mensaje

def mostrar_resultados(subtotal, total, mensaje):
    print("el resultado de la compra")
    print("subtotal:", subtotal)
    print(mensaje)
    print(" total a pagar es: ", total)

#**** zona de codigo principal ****
subtotal = ingresar_productos()
total, mensaje = calcular_descuento(subtotal)
mostrar_resultados(subtotal, total, mensaje)              