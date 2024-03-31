def guardomedia_txt(lista):
    with open("archivo_datos_media.txt","w") as r:
        for i in lista:
            r.write(str(i)+"\n")

lista=[]
while True:
    ingreso = input("ELIJA LA OPCIÓN DESEADA :[0] SALIR, [1] PARA IMPRMIR TODA LA FACTURACIÓN DEL ARCHIVO CON SU RESPECTIVA MEDIA, [2] PARA IR A UN AÑO ESPECIFICO, [3] PARA ALMACENAR LA FACTURACIÓN COMPLETA Y LOS RESULTADOS DE LA MEDIA EN UN ARCHIVO INDEPENDIENTE :")
    with open("archivo_fac_empresa.csv", "r") as archivo:
        archivo_empresa = archivo.readlines()
        
        for i in archivo_empresa:
            archivo_empresa_dividido = i.strip().split(";")
            año,periodo_uno,periodo_dos,periodo_tres,periodo_cuatro = archivo_empresa_dividido
            periodo_uno = int(periodo_uno)
            periodo_dos=int(periodo_dos)
            periodo_tres=int(periodo_tres)
            periodo_cuatro=int(periodo_cuatro)
            media = (periodo_uno+periodo_dos+periodo_tres+periodo_cuatro)/4
            lista.append((año,periodo_uno,periodo_dos,periodo_tres,periodo_cuatro,media))
            if ingreso == "1" :
                print(f"facturaciòn cuatrimestral año : {año}, periodo 1 : ${periodo_uno}, periodo 2 : ${periodo_dos}, periodo 3 : ${periodo_tres}, periodo 4 : ${periodo_cuatro}, media : {media}")
            elif ingreso == "2" : 
                ingresoaño = input("INGRESE EL AÑO EN NUMEROS : ")
                if ingresoaño == año:
                    print(f"facturaciòn cuatrimestral año : {año}, periodo 1 : ${periodo_uno}, periodo 2 : ${periodo_dos}, periodo 3 : ${periodo_tres}, periodo 4 : ${periodo_cuatro}, media : {media}")
            elif ingreso == "3" : 
                guardomedia_txt(lista)
            elif ingreso == "0":
                bucle = False




                
