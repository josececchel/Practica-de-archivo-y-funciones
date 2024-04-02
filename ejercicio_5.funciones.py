#Algoritmo de euclide.
def maximo_comun_divison(a,b):
    while b!= 0:
        a, b = b, a % b # SE OBTIENE EL RESTO DE LA DIVISIÓN Y SE VA GUARDANDO EN B PARA SEGUIR MULTIPLICANDO 
    return a 
    
def minimo_comun_multiplo(a,b):

    return (a*b) // maximo_comun_divison(a,b)

def main():
    a = int(input("INGRESE EL PRIMER NUMERO:  "))
    b = int(input("INGRESE EL SEGUNDO NUMERO:  "))
    if a > b : 
        z = b 
        b = a
        a = z
    resultado1 = maximo_comun_divison(a,b)
    print(f"EL MAXIMO COMÚN DIVISOR DE LOS NUMEROS INGRESADOS ES : {resultado1}")
    resultado2  = minimo_comun_multiplo(a,b)
    print(f"EL MINIMO COMÚN MULTIPLO DE LOS NUMEROS INGRESADO ES : {resultado2}")
    
    
if __name__ == "__main__":
    main()