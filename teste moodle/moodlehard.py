q = int(input("Entre com a quantidade de números que serão digitados: "))
maior = float('-inf')
soma = q + 1
for i in range (1, soma):
    num = int(input(f"número {i}: "))
    if num > maior:
        maior = num
print(f'Maior número digitado: {maior:.0f}')


    