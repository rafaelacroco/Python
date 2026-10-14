# Faça um programa para criar uma lista de 10 elementos inteiros
# Mostre todos os elementos que forem maiores que a soma de dois
# de seus antecessores
L = []
for i in range (10):
    num = int(input("Digite um número:"))
    L.append(num)
for i in range(2, len(L)):
    atual = L [i]
    anterior = L [i -1]
    anterior2 = L [i -2]
    soma = anterior + anterior2
    if atual > soma:
        print (atual)

