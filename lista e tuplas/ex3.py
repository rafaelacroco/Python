#cai na ATIVIDADE

# criar uma lista para armazenar os dados
L = [] 
# pedir 10 números para o úsuario
for i in range (10):
    num = int(input())
    # adicionar os números na lista com o append
    L.append(num)
    # declarar valor para as variaveis
    maior = L [0]
    indMaior = 0
    # para percorrer a lista armazenada usa o for
    for i in range (len(L)):
        if L[i] > maior:
            maior = L[i]
            indMaior = i
print (maior, indMaior)

# maneira de fazer direto

# L = [] 
# maior = L [0]
# indMaior = 0
# for i in range (10):
    # num = int(input())
    # L.append(num)
    #if num > maior:
        # maior = num
        # indMaior = i
# print (maior, indMaior)