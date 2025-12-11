#****** zona de funciones *************
def procesar_lote_con_registro():
    unidades = int(input("digite la cantidad de unidades del lote: "))
    defectuosas = 0
    registro = []
    
    for i in range(1, unidades + 1):
        estado = input(f"unidad {i} (O=ok, D=defectuosa): ").upper()
        
        if estado == "D":
            defectuosas += 1
            registro.append(f"fallo en unidad {i} ")
        elif estado == "O":
            registro.append(f"unidad {i} OK")
        else:
            print(" estado invalido. se marcara como defectuosa. ")    
            defectuosas += 1
            registro.append(f"fallo en unidad {i}")
    
    porcentaje = (defectuosas / unidades) * 100
    return unidades, defectuosas, porcentaje, registro        

def mostrar_datos(unidades, defectuosas, porcentaje, registro):
    print("\---- detalles del lote -----")
    for linea in registro:
        print(linea)
        
    print("\--- resumen ----")
    print("total de unidades: ", unidades)
    print("defectuosas: ", defectuosas)
    print(f"porcentaje defectuosas:: {porcentaje:.2f}%")
    print("-----------\n")


#**** zona de codigo principal ********   
def menu_principal():
    while True:
        opcion = input(" ingrese 'L'para procesar lote o 'stop' para terminar: ").upper()
        
        if opcion == "STOP":
            print("proceso finalizado")
            break
        
        elif opcion == "L":
            unidades, defectuosas, porcentaje, registro = procesar_lote_con_registro()
            mostrar_datos(unidades, defectuosas, porcentaje, registro)
        else:
            print("opcion invalida. intentar de nuevo.\n ")
            
menu_principal()                        