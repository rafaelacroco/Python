from random import randint, random

L = [randint(0, 10) for i in range(10)]
# print(L)
R = [ random()*10 for i in range(5)]
# print(R)
S = ["uva", "banana", "laranja", "abacaxi", "melancia", "morango", "caju"]

lista_completa = [] #serve para armazenar as três listas dentro de uma lista sem usar concatenar as listas, ou seja, as listar serão ainda sim individuais, mas estarão dentro de uma lista maior, que é a lista_completa
lista_completa.append(L)
lista_completa.append(R)
lista_completa.append(S)

L = []
R = []
S = []
print(lista_completa)
print()

for i in range (0, 3): #como são três listas dentro de uma lista, o range vai de 0 a 3
    for k in range(len(lista_completa[i])): #serve para percorrer cada elemento da lista interna
       print(lista_completa[i][k])
#pode usar tambem for i in range (len(lista_completa)) print (f"lista [{i+1}]: ") e for k in range(len(lista_completa[i])) print(lista_completa[i][k], end=" ") para percorrer cada elemento da lista interna.

