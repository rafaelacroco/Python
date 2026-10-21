dict = {
    1: "exemplo",
    2: "de",
    3: "dicionário"
}
print(dict)
print(dict[3])

#print(dict.get(2)) puxa info do dicionário

# adicionar é só declara o dicionario e adicionar algo, ex-   dicionario[six] = seven

#para remover é ex-   del dict[six]

# tupla de cada par associado print(list(dict.keys()))

# retorna os valores dos "indices", ex-   print(list(dict.values()))

for k in dict.keys():
    print(f"chaves{k} - valor {dict[k]}")