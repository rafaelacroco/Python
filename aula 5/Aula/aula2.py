cont = 0
soma = 0 

while cont < 10:
    x = int(input("Digite um valor:"))
    if x % 2 == 0:
        soma += x
        cont += 1

print(f"A soma total igual é {soma}")