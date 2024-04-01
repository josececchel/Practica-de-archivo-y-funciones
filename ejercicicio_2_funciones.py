#Escribir una función que calcule el area de un circulo y otra que calcule el volumen de un cilindro usando la primera función. 
import math
def area_circulo(radio):
    area = math.pi * (radio**2)
    return area

def volumen_cilindro(area,altura):
    volumen = area * altura
    return volumen

def main():
    comando = True
    while comando:
        try:
            radiocirculo = float(input("¡ BIENVENIDO AL PROGRAMA DE CALCULO AREA Y VOLUMEN DE UN CILINDRO ! INGRESE EL RADIO DEL CILINDRO EN ESTUDIO O PRECIONE CUALQUIER OTRO DIGITO DISTINTO A UN NUMERO PARA SALIR:     "))
            area = area_circulo(radiocirculo)
            arearedondeada = round(area,2)
            print(f"EL AREA DEL CIRCULO ES: {arearedondeada}")
            altocilindro = float(input("SI QUIERE CALCULAR EL VOLUMEN DEL CILINDRO INGRESE SU ALTURA, SI QUIERE SALIR PRESIONE CUALQUIER DIGITO DISTINTO A UN NUMERO  :    "))
            volumen = volumen_cilindro(area,altocilindro)
            volumenredondeado = round(volumen,2)
            print(f"EL VOLUMEN DEL CILINDRO ES: {volumenredondeado}")
        except ValueError: 
            comando=False
            print("¡¡NOS VEMOS LUEGO!!")

if __name__ == "__main__":
    main()