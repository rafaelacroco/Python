#qual o problema desse while? antes era que não existia a incrementação e decrementação i +1 e j -1


palavra = input("Digite a palavra: ")

i = 0
j = len(palavra) - 1
palindromo = True
while i <= j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    i += 1
    j -= 1
if palindromo:
    print("é palindromo!")
else:
    print("não é palindromo")