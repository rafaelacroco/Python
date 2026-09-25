from math import sqrt
pergunta = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
a = float(input("Digite o valor da aresta a em metros: "))

if pergunta == "dodecaedro" and a != 0: 
    raiz = sqrt (5)
    v = ((15 + 7*raiz)/4)*(a**3)
    print (f"O volume de um dodecaedro regular com {a:.2f} de aresta é: {v:.2f} " )
else:
    raiz = sqrt (5)
    d = 5/12
    v =  d*(3 + raiz)*(a**3)
    print (f"O volume de um icosaedro regular com {a:.2f} de aresta é: {v:.2f} " )

