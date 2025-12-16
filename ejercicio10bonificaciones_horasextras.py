#*** zona de funcones *****

def ingresar_horas_extra():
    horas = int(input("digite las horas extras trabajadas(negativo para terminar ): "))
    return horas
    
def calcular_bonificaciones(horas):
    if horas > 5:
        return horas * 15
    else:
        return horas * 10
    
def mostrar_resultados(total,empleados): 
    print("resultados:")
    print("total pagado en bonificaciones ",total)
    print("empleados con bonificacion: ",empleados)
    
    
#**** zona de codigo principal *****
total_bonificaciones = 0
empleados = 0

while True: 
    horas = ingresar_horas_extra()
    
    if horas < 0:
        break 
    
    bonificaciones = calcular_bonificaciones(horas)
    total_bonificaciones += bonificaciones 
    empleados += 1
    
mostrar_resultados(total_bonificaciones, empleados)         
            