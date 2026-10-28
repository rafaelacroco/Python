# para criar um arquivo txt
# arquivo = open("teste.txt", "w")
# arquivo.write("vou te bloquear")
# arquivo.close()

arquivo = open("teste.txt", "r")

for linha in arquivo.readline ():
    print(linha, end= "")
arquivo.close()