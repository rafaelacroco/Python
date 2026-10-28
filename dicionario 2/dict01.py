# exercicio 1 matriz e função
def procuraChave(dict, valor):
    L = []
    for chave in dict:
        if dict[chave] == valor:
            L.append(chave)
    return L

dict = {
    "fantasia": 1,
    "Magia": 2,
    "Principe Cruel": 3,
    "Fada": 1
}

print(procuraChave(dict, 1))