#**** zona de funciones ******
def ingresar_edades():
    total_presonas = 0
    suma_edades = 0
    publico_objectivo = 0
    
    while True:
        edad = int(input("ingresar la edad(0 para terminar): "))
        
        if edad == 0:
            break
        
        total_presonas += 1
        suma_edades += edad
        
        if edad >= 25 and edad <= 45:
            publico_objectivo += 1
            
    return total_presonas, suma_edades, publico_objectivo

def calcular_promedio(total,suma):
    if total == 0:
        return 0
    return suma / total

def mostrar_resltados(total,promedio,publico_objectivo):
    print("total de particioantes: ", total)
    print("personas en publico objectivo", publico_objectivo)
    print("edad promedio es: ", promedio)
    
#*** zona de codigo principal *****
total, suma, publico = ingresar_edades()
promedio = calcular_promedio(total, suma)
mostrar_resltados(total, promedio, publico)
    