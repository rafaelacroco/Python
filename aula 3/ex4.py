x = float(input ("Qual é o seu salário:"))

if x > 1250.00:
    aumento = x * 0.10
    y = x + aumento
    print(y)
else:
    aumento_2 = x * 0.15
    z = x + aumento_2
    print(z)