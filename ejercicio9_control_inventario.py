#***** zona de funciones ******
    

def leer_ventas():
    ventas = int(input("digite la cantidad vendida de hoy: "))
    return ventas

def actualizar_stock(stock,ventas):
    stock = stock - ventas
    
    if stock <= 10:
        return stock, True
    else:
        return stock, False
    
    
def mostrar_resultados(stock,reposicion):
    print("stock actual: ", stock)
    
    if reposicion:
        print("reposicion necesaria del stock")
        
# ****** zona de codigo principal ****
stock = 50

while True:
    ventas = leer_ventas()
    stock, reposicion = actualizar_stock(stock,ventas)
    mostrar_resultados(stock,reposicion)
    
    if reposicion:
        break
        
        