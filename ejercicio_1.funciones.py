
bucle = True

def iva_incluido(monto):
    monto_mas_iva = monto*1.21
    print(monto_mas_iva)

def incluir_iva(monto,iva):
    monto_mas_iva_ingresado = monto * (1 + iva / 100)
    return print(monto_mas_iva_ingresado)


def main():
    bucle = True
    while bucle:
        try:
            comando= str(input("ELIJA LA OPCIÓN DESEADA : PRESIONE A PARA CALCULAR EL VALOR AGREGADO DEL IVA 21% A UN MONTO INGRESADO POR USTED, PRESIONE B PARA CALCULAR EL VALOR AGREGADO DE UN MONTO Y IVA INGRESADO POR USTED, PRESIONA C PARA SALIR:  ")).upper()
        except ValueError:
            print("INGRESO NO VALIDO")
        if comando == ("A"):
            try:
                monto = float(input("POR FAVOR INGRESE EL MONTO POR EL CUAL QUIERE CALCULAR EL VALOR AGREGADO DEL IVA DEL 21%:    "))
                iva_incluido(monto)
            except ValueError:
                 print("INGRESO NO VALIDO")
            
        elif comando == "B":
                try:
                    monto = float(input("POR FAVOR INGRESE EL MONTO:   "))
                    iva = float(input("POR FAVOR INGRESE EL PORCENTAJE DE IVA A INCLUIR:   %"))
                    incluir_iva()
                except ValueError:
                     print("INGRESO NO VALIDO")
                
        elif comando == "C":
             bucle = False
             print("A DIOS ! REGRESE CUANDO USTED NECESITE, ESTAMOS A VUESTRO SERVICIO")
             break 
        else :
             if comando != "A" or comando !="B" or comando != "C":
                  print("ERROR !! INGRESE UNA OPCIÓN VALDA ")
                 
                  
if __name__ == "__main__":
    main()
