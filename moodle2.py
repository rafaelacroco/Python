for i in range (5): #LEITURA DOS NÚMEROS 0 1 2 3 4 
    if i == 4: # QUANDO I FOR IGUAL A 4 VOCÊ CONTINUA O CÓDIGO NO ELSE E NÃO É EXIBIDO O NÚMERO 4 (PQ NÃO TEM UM I NO SEGUNDO PRINT)
        continue
    else: # QUANDO O I FOR MENOR QUE 4 VAI SER ECRITO OS MENORES NÚMERO, O "END" é a quebra de linha.
        print (i, end =" ")
else:
    print("aqui", end =" ")