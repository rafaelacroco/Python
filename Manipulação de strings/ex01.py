palavra = str(input("Digite uma string:"))
nova_palavra = ""
for char in palavra:
    if char == 'a'or char == 'e' or char == 'i'or char == 'o' or char == 'u':
        nova_palavra += (chr(ord(char) - 32))
    else:
        nova_palavra += (char)
print(nova_palavra)
vogais = ['a', 'e', 'i', 'o', 'u']
for i in range (len(palavra)):
    if palavra[i] in vogais:
        palavra = palavra.replace(palavra[i], palavra[i].upper())
print(palavra)