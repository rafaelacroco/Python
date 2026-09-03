#Preço do produto e código de origem;
#mostre o preço e sua procedência;
c = int(input ("Qual é o código de origem do produto?"))
p =  float(input ("Qual é o preço do produto?"))

if c < 1 and c > 20 and c < 25 and c > 30:
    if c == 1:
         print ("Código de origem: 1 \n Procedência: Sul \n Preço: R$ %.2f "% p)
    if c == 2:
        print ("Código de origem: 2 \n Procedência: Norte \n Preço: R$ %.2f "% p)
    if c == 3:
        print ("Código de origem: 3 \n Procedência: Leste \n Preço: R$ %.2f "% p)
    if c == 4:
        print ("Código de origem: 4 \n Procedência: oeste \n Preço: R$ %.2f "% p)
    if c == 5 or c == 6 or c >=25 or c<= 30:
        print ("Código de origem: 5 ou 6 ou 25 até 30 \n procedência: Nordeste \n Preço: R$ %.2f "% p)
    if c >= 7 and c<= 9 :
        print ("Código de origem: 7,8 ou 9 \n procedência: sudeste \n Preço: R$ %.2f "% p)
    if c >=10 and c <= 20:
        print("Código de origem: 10 até 20 \n procedência: Nordeste \n Preço: R$ %.2f "% p)
else:
    print("procedência: Importado \n Preço: R$ %.2f "% p)