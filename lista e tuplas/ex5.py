# Faça um programa que:
#  Imprime uma sequência de n números em ordem inversa à da leitura
#  Utilize uma lista para isso.

L = []

quantidade = int(input ("Digite a quantidade de números:"))

for i in range (quantidade):
    num = int(input("Digite um número:"))
    L.append(num)
# ou L.reversed()
#Print (L)
for item in reversed(L):
    print (item)