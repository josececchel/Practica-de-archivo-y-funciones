try:
    import csv
    mejor_puntaje = 0
    mejor_juego = ""
    with open("archivo.csv","r") as datos:
        datos_archivo = datos.readlines()
        
        for i in datos_archivo:
            datos_separados = i.strip().split(",")

            nombre_juego,punta_juego,precio = datos_separados

            puntaje = int(punta_juego)

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_juego = nombre_juego

            print(f"Juego: {nombre_juego}, Calificación: {punta_juego}, Precio del juego: ${precio}")
            
        


    print(f"El juego con mayor calificación es : {mejor_puntaje}, {mejor_juego}")
except FileNotFoundError:
    "ERROR ! NO SE PUDO ABRIR EL ARCHIVO, REINICIE EL SISTEMA"