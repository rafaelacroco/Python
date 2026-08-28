import math #from math import ceil
a = float(input("Digite a altura:"))
r = float(input("Digite o raio:"))
a_base = 3.1415 *(r**2)
a_lateral = a * (2*3.1415*r)
a_pintar = a_base + a_lateral
q_litros = a_pintar / 3
q_latas = math.ceil (q_litros / 5)
#dá para fazer com if; else;else;else
if q_latas == 1:
    preco_1 = q_latas* 50.00
    print("Altura: %.1f \n Raio: %.1f \n Área a ser pintada: %.3f \n Quantidade de litros necessários: %.2f \n Quantidade de latas: %.0f \n Preço unitário: R$ 50,00 \n Custo total: %.2f" % (a, r, a_pintar, q_litros, q_latas, preco_1 ))
if q_latas == 2 :
    preco_2 = q_latas*48.00
    print("Altura: %.1f \n Raio: %.1f \n Área a ser pintada: %.3f \n Quantidade de litros necessários: %.2f \n Quantidade de latas:%.0f \n Preço unitário: R$ 48,00 \n Custo total: %.2f" % (a, r, a_pintar, q_litros, q_latas, preco_2 ))
if q_latas == 3 :
    preco_3 = 46.00* q_latas
    print("Altura: %.1f \n Raio: %.1f \n Área a ser pintada: %.3f \n Quantidade de litros necessários: %.2f \n Quantidade de latas: %.0f \n Preço unitário: R$ 46,00 \n Custo total: %.2f" % (a, r, a_pintar, q_litros, q_latas, preco_3 ))
if q_latas > 3 :
    preco_4 = 45.00*q_latas
    print("Altura: %.1f \n Raio: %.1f \n Área a ser pintada: %.3f \n Quantidade de litros necessários: %.2f \n Quantidade de latas: %.0f \n Preço unitário: R$ 45,00 \n Custo total: %.2f" % (a, r, a_pintar, q_litros, q_latas, preco_4 ))

