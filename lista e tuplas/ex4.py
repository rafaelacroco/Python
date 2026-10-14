# esse cai

L = []
# definir o número inicial da soma e do índice
soma = 0 #acumulador
soma_ind = 0

for i in range(10):
    # pede 10 números e armazena na lista
    num = int(input("Digite o número:"))
    L.append(num)
    # if definindo que apenas se a divisão resultar 0,
    if num % 2 == 0:
        # deve somar os numeros OK
        soma += num
    if i % 2 == 0:
        soma_ind += num
print("A soma dos números pares é: %d" % soma)
print("A soma dos elementos de índices par é: %d" % soma_ind)

