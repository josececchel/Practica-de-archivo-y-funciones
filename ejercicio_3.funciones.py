def impresion_de_lista(lista):
    return len(lista)

def main():
    lista = [4,7,8,9,4,7,5,4,6]
    longitud = impresion_de_lista(lista)
    print(f"LA LONGITUD DE LA LISTA DE NUMEROS ES DE : {longitud} ")

if __name__ == "__main__":
    main()