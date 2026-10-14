L = []
soma_i1 = 0
soma_i2 = 0
soma_i3 = 0
soma_i4 = 0
while True:
    num = int(input("Digite um número:"))
    if num < 0:
        break
    if num > 0: 
        L.append(num)
    for i in range (len(L)):
        x = L[0:25]
        soma_i1 += i

print(soma_i1)

    
