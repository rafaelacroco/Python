votos = [0 for i in range (7)]
SO = ["", "Windows server", "unix" ,"linux" , "netware" , "mac os" , "outro"]
while True:
    v = int(input("Digite o número do candidato (1 a 6) ou 0 para encerrar: "))
    if v == 0:
        break
    else:
        if 0 < v <= 6:
            votos[v] += 1 
print("sistema operacional  | votos |  %")
print(("-"*25))
for i in range(1,7):
    print(f"{SO[i]} | {votos[i]} | {votos[i]/sum(votos)*100:.2f}%")
print(("-"*25))
print("Total:", sum(votos))