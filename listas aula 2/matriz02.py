import random

M = []
for i in range(10):
    L = [random.randint(0,9) for j in range(15)]
    M.append(L)
#Matriz completa
for i in range(len(M)):
    for j in range (len(M[i])):
        print(M[i][j], end =" ")
    print()
#primeira coluna
print()
for i in range(len(M)):
    print(M[i][0])
    