def cantidad_palabras(cadena_caracteres):
    palabras = cadena_caracteres.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabra_mas_repetida(diccionario):
    contador = 0
    palabra_repetida = ""
    for palabra in diccionario:
        repeticion = diccionario[palabra]
        if repeticion > contador:
            contador = repeticion
            palabra_repetida = palabra
    return (palabra_repetida,contador)


def main():

    cadena_caracteres = str(input("INGRESE EL ESTRIBILLO DE UNA CANCIÓN PARA CALCULAR LA CANTIDAD DE VECES QUE SE REPITE UNA PALABRA :  "))
    frecuencia_de_palabras = cantidad_palabras(cadena_caracteres)
    palabra,repeticion = palabra_mas_repetida(frecuencia_de_palabras)
    print(f"Diccionario de frecuencia de palabras: {frecuencia_de_palabras} y la palabra mas repetida es {palabra} en cantidad de veces {repeticion} ")




if __name__ == "__main__":
    main()