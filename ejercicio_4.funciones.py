def impresion_de_lista(lista):
    lista_cuadrados=[]
    for i in lista:
        j = i**2
        lista_cuadrados.append(j)

    return lista_cuadrados

def main():
    lista = [4,7,8,9,4,7,5,4,6]
    cuadrado = impresion_de_lista(lista)
    print(f" EL CUADRADO DE CADA NUMERO DE LA LISTA ES : {cuadrado} ")

if __name__ == "__main__":
    main()