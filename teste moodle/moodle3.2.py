x = float(input("Digite o valor do primeiro produto: "))
y = float(input("Digite o valor do segundo produto: "))
z = float(input("Digite o valor do terceiro produto: "))

a = x + y + z
if a > 500:
    b = (a/100)*20
    print("Desconto: %.2f" % b) 
else:
    c = (a/100)*10
    print("Desconto: %.2f" % c)