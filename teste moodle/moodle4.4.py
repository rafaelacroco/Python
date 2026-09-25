x = float(input("Digite o valor da compra: "))
y = int(input("Digite a quantidade de parcelas: "))

if y == 1 and x > 5000:
    a = (x/100)*15
    b = x - a
    p = b/y
    print(f"Desconto total:{a:.2f} \n Valor final da compra com desconto:{b:.2f} \n Cada parcela será de: {p:.2f}")
elif y == 1 and x < 5000:
    a = (x/100)*10
    b = x - a
    p = b/y
    print(f"Desconto total:{a:.2f} \n Valor final da compra com desconto:{b:.2f} \n Cada parcela será de: {p:.2f}")
elif (y >= 2 or y <= 3) and x < 5000:
    a = (x/100)*5
    b = x - a
    p = b/y
    print(f"Desconto total:{a:.2f} \n Valor final da compra com desconto:{b:.2f} \n Cada parcela será de: {p:.2f}")
elif (y == 2 or y == 3) and x > 5000:
    a = (x/100)*10
    b = x - a
    p = b/y
    print(f"Desconto total:{a:.2f} \n Valor final da compra com desconto:{b:.2f} \n Cada parcela será de: {p:.2f}")
elif y > 3 and x < 5000:
    a = (x/100)*0
    b = x - a
    p = b/y
    print(f"Desconto total:{a:.2f} \n Valor final da compra com desconto:{b:.2f} \n Cada parcela será de: {p:.2f}")
elif y > 3 and x > 5000:
    a = (x/100)*5
    b = x - a
    p = b/y
    print(f"Desconto total:{a:.2f} \n Valor final da compra com desconto:{b:.2f} \n Cada parcela será de: {p:.2f}")

    