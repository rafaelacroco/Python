print ("Exercício 3")
d = int (input("digite a Quantidade de dias:"))
h = int (input ("digite a Quantidade de horas:"))
m = int(input("digite a Quantidade de minutos:"))
s = int (input ("digite a quantidade de segundos:"))

t = (d*24*60*60) + (h*60*60) + (m*60) + (s)
print ("O tempo total foi de %d segundos" % t)
