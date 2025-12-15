#*** zona de funciones *******
def leer_ventas():
    meta = 5000
    total_vendedores = 0
    cumplen_meta = 0
    
    while True:
        venta =float(input("digite las ventas del vendedor (0 o negativo paraterminar ): "))
        
        if venta <= 0:
            break
        
        total_vendedores += 1
        
        if venta >= meta:
            cumplen_meta += 1
            
    return total_vendedores, cumplen_meta

def no_cumplen_metas(total, cumplen):
    return total - cumplen   

def mostrar_resultados(total, cumplen, no_cumplen):
    print("resultados") 
    print("total de vendedores: ", total)
    print("cumplieron metas: ", cumplen)
    print("no cumplieron metas: ", no_cumplen)
    
    
#*** zona de codigo principal *****
total, cumplen = leer_ventas()
no_cumplen = no_cumplen_metas(total,cumplen)
mostrar_resultados(total, cumplen, no_cumplen)        