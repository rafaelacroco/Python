# Neste exercício, você criará um programa que lê palavras do usuário até que o usuário entre com uma linha em branco.
# Após o usuário digitar uma linha em branco, seu programa deve
# exibir cada palavra digitada pelo usuário exatamente uma vez.
# As palavras devem ser exibidas na mesma ordem em que foram inseridas
L = []

while True:
    palavra = str(input("Digite uma palavra:"))
    if palavra == "":
        break
    if not palavra in L:
        L.append(palavra)

print("Palavras digitadas")
for palavra in L:
    print(palavra)

