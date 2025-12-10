#********* zona de funciones ****************
def ingresar_codigo():
    codigo_correcto = "inv - 001"
    permitidos = 0
    denegados = 0
    registros = []
 
    while True:
        codigo = input("ingrese el codigo del empleado para accerder a esta zona o SALIR para terminar: ")
        
        if codigo.upper() == "SALIR":
            break
        
        if codigo == codigo_correcto:
            registros.append("acceso PERMITIDO para codigo: " + codigo)
            permitidos += 1
        else:
            registros.append("acceso DENEGADO para codigo: " + codigo)
            denegados += 1
            
    return permitidos, denegados, registros

def procesar_datos(permitidos, denegados):
    total_intentos = permitidos + denegados
    return total_intentos

def mostrar_resultados(permitidos, denegados, total):
    print("\------ resultados del sistema --------") 
    print("accesos permitidos:", permitidos)
    print("accesos denegados: ", denegados)
    print("total de intentos: ", total)           
    
#*** zona de codigo principal ****
permitidos,denegados, resgistros = ingresar_codigo()
total = procesar_datos(permitidos, denegados, )
mostrar_resultados(permitidos,denegados,total)    