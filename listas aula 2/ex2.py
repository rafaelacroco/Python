# h = [0 for i in range (1,10)]
# H [1] += 1

# 1 - Windows server; 2 - unix; 3 - linux; 4 - netware; 5 - mac os; 6 - outro;

Vetor = [0 for i in range(0,7)]
print ("Qual é o melhor sistema operacional para uso em servidores? \n 1 - Windows server; \n 2 - unix; \n 3 - linux; \n 4 - netware; \n 5 - mac os; \n 6 - outro;")
while True:
    voto = int(input("Digite seu voto:"))
    if voto == 0:
        break
    for i in range(len(Vetor)):
        if voto >= 1 or voto <= 6:
            Vetor[0] += 1
            Vetor[1] += 1
            Vetor[2] += 1
            Vetor[3] += 1
            Vetor[4] += 1
            Vetor[5] += 1
            Vetor[6] += 1
        else:
            print("Opção inválida! Digite um número de 1 a 9.")
print(f"Opção {Vetor[i]}: {Vetor[0]} voto(s) \n Opção {Vetor[i]}: {Vetor[1]} voto(s)")
