#para ler o menor valor
t = [11, 7, 2, 4] #lista de números
menor = t [0] #menor = primeiro indice
for valor in t:
#para cada valor de t compare:
    if valor < menor: 
        menor = valor 
print(menor)