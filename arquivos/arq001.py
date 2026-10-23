
arquivo_par = open("números_pares.txt", "w")
print("pares criados")
arquivo_impares = open("números_impares.txt", "w")
print("impares criados")

for i in range(1000):
    if i % 2 == 0:
        arquivo_par.write(str(i) +"\n")
    else:
        arquivo_impares.write(str(i) +"\n")

