M = []
soma_diagona = 0
for i in range (3): #quantidade de listas
    L = []
    for j in range (3): #quantidades de elementos dentro da lista
        x = int(input("Número: "))
        L.append(x)
    M.append(L) #adiciona as listas a matriz

 #L = [int(input()) for j in range (3)]    list compreenshion 

 #print da matriz estruturada
for i in range (3): 
    for j in range (3):
        if i == j:
            soma_diagona += M[i][j]
        print(M[i][j], end= " ")
    print()
print(soma_diagona)

