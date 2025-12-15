
# ***** zona de funciones ******
def ingresar_mediciones():
    total_mediciones = 0
    alertas = 0
    
    while True:
        uso = float(input("ingrese el uso de la cpu en (%), negativo para terminar: "))
        
        if uso < 0:
            break
        
        total_mediciones += 1
        
        if uso > 90:
            print("alerta de uso critico")
            alertas += 2
            
    return total_mediciones, alertas

def procesar_datos(total_mediciones, alertas):
    return total_mediciones, alertas

def mostrar_resultados(total_mediciones, alertas):
    print ("el resultado es:") 
    print ("el total_mediciones ", total_mediciones)
    print("total alertas ", alertas)
    
#**** zona de codigo principal *******
total, alertas = ingresar_mediciones()
total, alertas = procesar_datos(total, alertas)
mostrar_resultados( total, alertas)    