v_h = float(input ("Digite o valor da hora trabalhada:"))
nh = int (input ("Digite o número de horas trabalhadas no mês:"))
Salário_bruto = (v_h*nh)
Ir = Salário_bruto * (11/100)
Inss = Salário_bruto * (8/100) 
Sindicato = Salário_bruto * (5/100)
Salário_Liquido = Salário_bruto - Ir - Inss - Sindicato
print(" +Salário bruto: %.2f \n {-IR(11%%): %.2f} \n {-INSS (8%%): %.2f} \n {-Sindicato (5%%):} %.2f \n Salário líquido: %.2f" % (Salário_bruto, Ir, Inss, Sindicato, Salário_Liquido))