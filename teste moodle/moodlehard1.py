num = int(input("Digite o número desejado: "))
x = num + 1
E = 1
if num <= 0:
    print ("O número precisa ser maior que zero!")
for i in range (1, x):
    E = E + (1/i)
print (f"{E:.3f}")


#DIFICIL PRA PORRA
# COMO VOU FAZER ISSO SEM TESTE AAAAAAAAAAA