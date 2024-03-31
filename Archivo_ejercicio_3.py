n=input("BIENVENIDOS !! INGRESE LA CANTIDAD DE EQUIPOS QUE PARTICIPARAN DEL TORNEO : ")

matriz=[]
n=int(n)

for i in range(n):
    fila= [0]*n
    matriz.append(fila)
    
    
for a in range(n):
    for b in range(a + 1,n):
        resultado = int(input(f"INGRESE EL RESULTADO DEL PARTIDO DEL EQUIPO {a+1} CONTRA EQUIPO {b+1}:  "))
        matriz[a][b] = resultado
        matriz[b][a] = resultado


for filas in matriz:
    print(filas)
        




    
