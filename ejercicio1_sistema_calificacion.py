#****** zona de funciones ******
def ingresar_calificaciones():
    pedidos = 0
    suma = 0
    excelentes = 0
    
    while True:
        calificacion = input("digite la calificacion (1-5) o 0 para terminar: ")
        
        if calificacion == "0":
            break
        
        calificacion = int(calificacion)
        
        pedidos += 1
        suma += calificacion
        
        if calificacion == 5:
            excelentes += 1
            
    return pedidos, suma, excelentes

def procesar_datos(pedidos,suma,):
    if pedidos == 0:
        return 0
    return suma / pedidos

def msotrar_resultados(pedidos,promedio,excelentes):
    if pedidos == 0:
        print("no se procesaron pedidos")
    else:
        print("pedidos procesados: ", promedio)
        print("promedio general: ", promedio)
        print("pedidos excelentes (5 estrellas): ",excelentes)
        
#********* zona de codigo principal ************
pedidos, suma, execelentes = ingresar_calificaciones()
promedio = procesar_datos(pedidos,suma, )
msotrar_resultados(pedidos, promedio, execelentes)        
               