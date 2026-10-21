
dict = {
    "Fantasia": 1,
    "Principe Cruel": 2,
    "Mágia": 3,
    "Sombria": 3,
    "Fada": 2,
    "Livro": 1
}
print(dict)
print()


def procuraChave():
    x = int(input("Digite um número de 1 a 3: "))
    for v in dict.items():
        y = dict.values()
        if x == y:
            return(f"chave{v}")

        