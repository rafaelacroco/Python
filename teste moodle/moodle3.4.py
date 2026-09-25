x = int(input("Digite o código do produto:"))
y = float(input("Digite a quantidade do produto:"))
if x == 1:
    a = 6
elif x == 2 :
    a = 6.5
elif x == 3:
    a = 5
elif x == 4:
    a = 3
elif x == 5:
    a = 2
z = a*y
print(f"Total: R$ {z:.2f}")