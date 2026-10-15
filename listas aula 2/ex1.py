L = []
Cont_0_25 = 0
Cont_26_50 = 0
Cont_51_75 = 0
Cont_76_100 = 0
while True:
    num = int(input("Digite um número:"))
    if num < 0:
        break
    L.append(num)
    for x in range(len(L)):
        if 0 <= x <= 25:
            Cont_0_25 = x + 1 
        elif 26 <= x <= 50:
            Cont_26_50 = x + 1
        elif 51 <= x <= 75:
            Cont_51_75 = x + 1
        else:
            Cont_76_100 = x + 1

print(f"Intervalo [0-25]: {Cont_0_25}")
print(f"Intervalo [26-50]: {Cont_26_50}")
print(f"Intervalo [51-75]: {Cont_51_75}")
print(f"Intervalo [76-100]: {Cont_76_100}")