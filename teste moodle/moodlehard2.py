
cont = 2005
si = 5000
ano = int(input("Digite o ano desejado: "))
while ano >= cont:
    if ano > 2005:
        aumento_ano = ano + 1
        x = ano - cont
        porcentagem = (si/100)*((1.5**2)*x)
        aumento = si + porcentagem
        print (ano ,aumento)
        break
    else:
        print("Você não entrou em 2005")
        break

    