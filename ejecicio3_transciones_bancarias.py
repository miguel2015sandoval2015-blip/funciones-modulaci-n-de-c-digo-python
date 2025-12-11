#****** zona de funciones ********
def ingrsar_transacciones(saldo_inicial):
    saldo = saldo_inicial
    transacciones_validas = 0
    
    while True:
        tipo = input("ingrese el tipo de transaccion a realizar (D=deposito, R=retiro, FIN para terminar): ").upper()
        
        if tipo == "FIN":
            break
        
        if tipo not in ("D", "R"):
            print("tipo de transaccion invalida.")
            continue
        
        monto = float(input("ingrese el monto de la transaccion a realizar: "))
         
        if tipo == "D":
            saldo += monto
            transacciones_validas += 1
            
        elif tipo == "R":
            if saldo - monto >= 0:
                saldo -= monto
                transacciones_validas += 1
            else:
                print(" El retiro del dinero no es permitido: saldo insuficiente")
                
        else:
            print(" tipo de transaccion invalidad.")
    return saldo, transacciones_validas


def procesar_datos(saldo):
    return saldo

def mostrar_resultados(saldo, transacciones):
    print(" saldo final: ", saldo) 
    print(" transacciones validas: ", transacciones)
    
#**** zona de codigo principal *******
saldo_final, transacciones = ingrsar_transacciones(1000)
saldo_final = procesar_datos(saldo_final)
mostrar_resultados(saldo_final, transacciones)                       